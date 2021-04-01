import json

class Common():
    file = open('important.json')
    data = json.load(file)

    selfUserId = data['selfUserId']
    botChannelId = data['botChannelId']
    region = data['region']

    file.close()