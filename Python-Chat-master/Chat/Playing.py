import pygame
import Sound

filename = 'input_voice_file.wav'


def playing(msg):
    Sound.get(msg)
    # 初始化pygame
    pygame.init()

    try:
        # 加载音频文件
        pygame.mixer.music.load(filename)

        # 播放音频
        pygame.mixer.music.play()

        # 等待音频播放完毕
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

    except pygame.error as e:
        print(f"An error occurred: {e}")

    finally:
        # 退出pygame
        pygame.quit()
