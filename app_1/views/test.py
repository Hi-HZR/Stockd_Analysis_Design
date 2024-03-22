# from openai import OpenAI
#
# client = OpenAI(
#     api_key="sk-fjEgj6bXlkBZhGkjKCqhjvchpQVARH7Xv9ME44tBOLYAsyyc",
#     base_url="https://api.moonshot.cn/v1",
# )
#
# completion = client.chat.completions.create(
#   model="moonshot-v1-8k",
#   messages=[
#     {"role": "user", "content": "你好，1+23等于多少？"}
#   ],
#   temperature=0.3,
# )
#
# print(completion.choices[0].message)