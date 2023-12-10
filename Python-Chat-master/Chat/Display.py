import json
import sys
import tkinter as tk
import threading

import Playing
import Recording


class Display(object):
    def __init__(self, order):
        self.order = order
        if not self.order == '1':
            sys.exit()
        # 否则结束程序
        # self.window = tk.Tk()
        # btn_recording = tk.Button(self.window, text="按下说话", command=self.on_recording_click)
        # btn_recording.pack()
        # self.window.bind("<Key>", self.handle_x_ket)
        # self.window.mainloop()

    def on_recording_click(self):
        record_audio_thread = threading.Thread(target=Recording.recording)
        record_audio_thread.start()

        record_audio_thread.join()

        with open('ans.json', 'r') as f:
            ans = json.load(f)
        return ans

        # 在这里获取Recording.recording函数的返回值
        # return Recording.recording()

    # 播放声音
    def on_playing_click(self):
        play_audio_thread = threading.Thread(target=Playing.playing)
        play_audio_thread.start()

    # def handle_x_ket(self, event):
    #     if event.char == 'x':
    #         self.on_recording_click()


if __name__ == '__main__':
    Display('1')
