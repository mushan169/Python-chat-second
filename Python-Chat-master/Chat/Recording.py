import Emotion
import pyaudio
import wave
import IdentifyVerbal
import langchain_getInfo
import Global_variable

filename = "input_voice_file.wav"


def remove_whitespace_and_dashes(input_string):
    # 去除所有空格
    result = input_string.replace(' ', '')
    # 去除所有破折号
    result = result.replace('-', '')
    result = result.replace('.', '')
    result = result.replace('：', '')
    return result


def recording():
    print(123)
    # 以1024个样本为一组记录
    chunk = 1024
    # 每个样本16位
    sample_format = pyaudio.paInt16
    chanels = 2

    # 每秒记录44400个样本
    smpl_rt = 44400
    seconds = 4

    # 创建PortAudio接口
    pa = pyaudio.PyAudio()

    stream = pa.open(format=sample_format, channels=chanels,
                     rate=smpl_rt, input=True,
                     frames_per_buffer=chunk)

    print('Recording...')

    # 初始化用于存储帧的数组
    frames = []

    # 将数据分块存储8秒
    for i in range(0, int(smpl_rt / chunk * seconds)):
        data = stream.read(chunk)
        frames.append(data)

    # 停止并关闭流
    stream.stop_stream()
    stream.close()

    # Terminate-PortAudio接口
    pa.terminate()

    print('Done !!! ')

    # 将录制的数据保存为.wav格式
    sf = wave.open(filename, 'wb')
    sf.setnchannels(chanels)
    sf.setsampwidth(pa.get_sample_size(sample_format))
    sf.setframerate(smpl_rt)
    sf.writeframes(b''.join(frames))
    sf.close()

    # 语音转换为文字,文字为输入给gpt的内容
    verbal = IdentifyVerbal.IdentifyVerbal()
    context = verbal(filename)

    chat = langchain_getInfo.GetChatContent()

    result = remove_whitespace_and_dashes(context)

    # 得到回答
    chatResult = chat(result)

    Global_variable.Emotion = Emotion.EmotionClassifier.classify(context)
    Global_variable.UserInputMessage = context
    Global_variable.AIOutputMessage = chatResult

    print(chatResult)
