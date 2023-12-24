import json
import sys
import threading

import Playing
import Recording


class Display(object):
    def __init__(self, order):
        self.order = order
        if not self.order == '1':
            sys.exit()

    # 开始记录声音和处理声音
    def on_recording_click(self):
        record_audio_thread = threading.Thread(target=Recording.recording)
        record_audio_thread.start()

        record_audio_thread.join()

    # 播放声音
    def on_playing_click(self):
        play_audio_thread = threading.Thread(target=Playing.playing)
        play_audio_thread.start()


if __name__ == '__main__':
    Display('1')
