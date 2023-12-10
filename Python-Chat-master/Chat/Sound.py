import requests as reqt

# 通过调取接口,将文字转换为某个角色的语音
def get(msg):
    url = f'https://api.lolimi.cn/API/yyhc/y.php?msg={msg}&speaker=%E6%B4%BE%E8%92%99&Length=1&noisew=0.8&sdp=0.1&noise=0.6&type='
    resp = reqt.get(url)
    if resp.json()['text'] == "获取成功！":
        content = reqt.get(resp.json()['music']).content
        with open("path_of_file.wav", 'wb') as f:
            f.write(content)
    else:
        print("Fail!")