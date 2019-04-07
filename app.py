import requests
from time import sleep

url = "https://api.telegram.org/bot780148416:AAF7vAzAs7kHR5jmHA6ANsP3ZL5KnAWettU/"

def get_updates_json(request):
    response = requests.get(request + 'getUpdates')
    return response.json()


def last_update(data):
    results = data['result']
    total_updates = len(results) - 1
    return results[total_updates]

def get_chat_id(update):
    chat_id = update['message']['chat']['id']
    return chat_id

def get_chat_text(update):
    text = update['message']['text']
    return text

def send_mess(chat, text):
    params = {'chat_id': chat, 'text': text}
    response = requests.post(url + 'sendMessage', data=params)
    return response

#chat_id = get_chat_id(last_update(get_updates_json(url)))
#send_mess(chat_id, 'this shit work')
def main():
    update_id = last_update(get_updates_json(url))['update_id']
    
    while True:
        if update_id == last_update(get_updates_json(url))['update_id']:
            client_text = get_chat_text(last_update(get_updates_json(url)))
            send_mess(get_chat_id(last_update(get_updates_json(url))), 'This poebota work, because you write ' + client_text)
            update_id += 1
        sleep(1)

if __name__ == '__main__':
    main()
