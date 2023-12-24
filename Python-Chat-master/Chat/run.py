from flask import Flask, render_template, request, jsonify
import Display
import threading
import Playing
import Global_variable

app = Flask(__name__, static_folder='static')


@app.route('/')
# @app.route('/back')
def user():
    return render_template('talk.html')


@app.route('/record', methods=['POST', 'GET'])
def login():
    json = request.json
    # 测试接收数据
    print('recv:', json)
    # 判断录音指令
    if json['order'] == '1':
        # 录音对话开始
        Display.Display(json['order'])

        print("success")

        # 开启另外一个线程，播放声音
        audio_thread = threading.Thread(target=Playing.playing(Global_variable.AIOutputMessage))
        audio_thread.start()

        # 转换为json格式,将对话的内容传到前端
        return jsonify({'user': Global_variable.UserInputMessage, 'ai': Global_variable.AIOutputMessage})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
