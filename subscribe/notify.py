import requests

def send_wechat_message(key, content):
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

# 示例调用
key = '693axxx6-7aoc-4bc4-97a0-0ec2sifa5aaa'
content = 'hello world'
send_wechat_message(key, content)
