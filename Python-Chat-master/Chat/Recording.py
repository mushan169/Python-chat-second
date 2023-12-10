# define PY_SSIZE_T_CLEAN
import json

import pyaudio
import wave
import IdentifyVerbal
import Playing
import langchain_getInfo

KEYWORD = "推荐"
filename = "path_of_file.wav"
cache = {}


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

    # if KEYWORD in context:
    #     chat = Answer.Chat()
    #     require_ls = chat(context)
    # else:
    #     getKey = langchain_getInfo.GetKeyOfMeal()
    #
    #     recipe_name = getKey(context)
    #     if recipe_name in cache.keys():
    #         print('yes')
    #         result = cache[recipe_name]
    #     else:
    #         print('no')
    #         getRecipe = langchain_getInfo.GetRecipe()
    #         result = remove_whitespace_and_dashes(getRecipe(recipe_name))
    #         cache[recipe_name] = result
    #     require_ls = result.split("\n")
    chat = langchain_getInfo.GetChatContent()

    result = remove_whitespace_and_dashes(context)

    # 得到回答
    chatResult = chat(result)
    print(chatResult)
    ans = {'content': chatResult}
    with open('ans.json', 'w') as f:
        json.dump(ans, f)
    # require_ls = result.split("\n")
    print(chatResult)

    #Playing.playing(chatResult)

    # 返回回答结果
