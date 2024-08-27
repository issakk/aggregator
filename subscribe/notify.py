import requests

def send_wechat_message(content):
    key = os.environ.get('WECHAT_KEY')
    url = f'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key={key}'
    headers = {
        'Content-Type': 'application/json'
    }
    data = {
        "msgtype": "text",
        "text": {
            "content": content
        }
    }
    
    response = requests.post(url, headers=headers, json=data)
    
    if response.status_code == 200:
        print("Message sent successfully!")
    else:
        print(f"Failed to send message. Status code: {response.status_code}")
        print(response.text)

