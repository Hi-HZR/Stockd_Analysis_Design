import aip


def emotion_sdk(my_text):
    app_id = '57118734'
    api_key = 'MhsCMaKfJX9JyopuyviPbiK5'
    secret_key = 'RGKHayxmxEfKAN2tqhrZsiCmoBLEQUs3'
    my_nlp = aip.nlp.AipNlp(app_id, api_key, secret_key)

    result = my_nlp.sentimentClassify(my_text)
    value = result.get("items")
    positive_prob = value[0]["positive_prob"]
    negative_prob = value[0]["negative_prob"]
    return positive_prob, negative_prob
