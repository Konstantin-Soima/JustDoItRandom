import requests
from time import sleep
from random import seed
from random import randint

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
    #Нужен массив из ClientID и вариантов
    a = {}
    seed(1)
    while True:
        if update_id == last_update(get_updates_json(url))['update_id']:
            chat_id = get_chat_id(last_update(get_updates_json(url)))
            if chat_id not in a:
                a[chat_id]=[]
            client_text = get_chat_text(last_update(get_updates_json(url)))
            #Если текст был не /random то выводить "Введите вариант", иначе Результат "Пожалуй это лучшее решение: "
            result_text = 'Enter opinion' if client_text<>'/random' else 'Just Do It: '
            if client_text<>'/random':
                a[chat_id].append(client_text)
            elif client_text == '/random':
                if chat_id not in a:
                    result_text = 'Before type some opinions'
                elif len(a[chat_id])<1:
                    result_text = 'Before type some opinions'
                else:
                    size = len(a[chat_id])
                    index = randint(0,size-1)
                    result_text += a[chat_id][index]
                    del a[chat_id]
            send_mess(chat_id, result_text)
            update_id += 1
        sleep(1)

if __name__ == '__main__':
    main()
