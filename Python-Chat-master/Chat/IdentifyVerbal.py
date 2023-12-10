from modelscope.pipelines import pipeline
from modelscope.utils.constant import Tasks


class IdentifyVerbal:
    def __init__(self):
        self.inference_pipeline = pipeline(
            task=Tasks.auto_speech_recognition,
            model='damo/speech_paraformer-large-vad-punc_asr_nat-zh-cn-16k-common-vocab8404-pytorch',
            model_revision="v1.2.4")

    def __call__(self, url):
        rec_result = self.inference_pipeline(
            audio_in=f'{url}')

        return rec_result['text']


if __name__ == '__main__':
    identifyVerbal = IdentifyVerbal()
    res = identifyVerbal(
        "https://isv-data.oss-cn-hangzhou.aliyuncs.com/ics/MaaS/ASR/test_audio/asr_vad_punc_example.wav")
    print(res)
