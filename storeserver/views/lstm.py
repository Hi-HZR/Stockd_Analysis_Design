import matplotlib.pyplot as plt
from django.shortcuts import render
from matplotlib.font_manager import FontProperties
import pandas as pd
import torch
from torch import nn
import mpld3

from storeserver.views.trans import tran


def definite_lstm(request):
    w = FontProperties(fname='D:/PythonProject/djangoProject/storeserver/static/fonts/OPPOSans-Medium.ttf')
    w.set_size(16)
    # Returns a DataFrame
    data = pd.read_excel("D:/PythonProject/djangoProject/point.xlsx")
    print('data.shape:', data.shape)

    timeseries = data[["price"]].values.astype('float32')
    fig = plt.figure(dpi=100, figsize=(10, 4))
    plt.plot(timeseries, color='black')
    axes = plt.subplot()
    axes.set_xlabel('5天时间', fontproperties=w)
    axes.set_ylabel('股价', fontproperties=w)
    axes.set_title('沪深300股价图', fontproperties=w)
    mpld3.save_html(fig, 'png_origin.html')

    # 训练集和测试集的分割
    train_size = int(len(timeseries) * 0.6)
    test_size = len(timeseries) - train_size
    # 通过索引把训练集，测试集给索引出来
    train, test = timeseries[:train_size], timeseries[train_size:]
    print('train.shape:', train.shape)
    print('test.shape:', test.shape)

    # 把pandas格式数据转换为tensor格式的数据,batch_size,time_step,input_dimension
    train_tensor = torch.FloatTensor(train).view(-1, train.shape[0], 1)
    test_tensor = torch.FloatTensor(test).view(-1, test.shape[0], 1)

    # 定义网络结构
    class LSTMModel(nn.Module):
        def __init__(self, input_size=1, hidden_size=50, num_layers=1, output_size=1):
            super(LSTMModel, self).__init__()
            self.hidden_size = hidden_size
            self.num_layers = num_layers

            # LSTM层
            self.lstm = nn.LSTM(input_size, hidden_size, num_layers, batch_first=True)

            # 输出层
            self.fc = nn.Linear(hidden_size, output_size)

        def forward(self, x):
            # 初始化h0,c0
            h0 = torch.rand(self.num_layers, x.size(0), self.hidden_size)
            c0 = torch.rand(self.num_layers, x.size(0), self.hidden_size)

            # 输出output数据
            output, (_, _) = self.lstm(x, (h0.detach(), c0.detach()))

            # output结构为[batch_size,seq_len,hidden-size]
            out = self.fc(output[:, :, :])
            return out

    # 超参数的设置
    input_size = 1
    hidden_size = 16
    num_layers = 2
    output_size = 1
    # 扩大学习率
    learning_rate = 0.1
    # 增加总迭代次数
    num_epochs = 200

    # 实例化模型
    model = LSTMModel(input_size, hidden_size, num_layers, output_size)

    # 定义损失函数与优化算法
    criterion = nn.MSELoss(reduction="mean")
    optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)

    # 开始训练
    for epoch in range(num_epochs):
        outputs = model(train_tensor)
        optimizer.zero_grad()
        loss = criterion(outputs[:, 1:, :], train_tensor[:, 1:, :])  # 修正损失函数计算
        loss.backward()
        optimizer.step()

        if (epoch + 1) % 50 == 0:
            print(f'Epoch[{epoch + 1}]/{num_epochs},Loss:{loss.item()}')

    print('完成训练')

    model.eval()
    test_outputs = model(test_tensor).detach().numpy()

    fig_1 = plt.figure(dpi=100, figsize=(10, 4))
    plt.plot(train, linewidth=5, color='#0FC513')
    axes_1 = plt.subplot()
    axes_1.set_xlabel('预测次数', fontproperties=w)
    axes_1.set_ylabel('股价', fontproperties=w)
    axes_1.set_title("股价预测图", fontproperties=w)
    mpld3.save_html(fig_1, 'png_train.html')

    fig_2 = plt.figure(dpi=100, figsize=(10, 4))
    plt.plot(test, linewidth=5, color='#FF6964')
    axes_2 = plt.subplot()
    axes_2.set_xlabel('预测次数', fontproperties=w)
    axes_2.set_ylabel('股价', fontproperties=w)
    axes_2.set_title('测试图', fontproperties=w)
    mpld3.save_html(fig_2, 'png_test.html')
    tran(request)

    return train, test


def lstm(request):
    train, test = definite_lstm(request)
    # print('------训练集-------')
    # print(train)
    print('训练集平均值', train.mean())
    # print('------测试集-------')
    # print(test)
    print('测试集平均值', test.mean())

    return render(request, 'lstm.html')
