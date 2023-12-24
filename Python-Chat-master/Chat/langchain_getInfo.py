from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

import IdentifyVerbal

import os

os.environ["OPENAI_API_KEY"] = "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"
model_name = "gpt-3.5-turbo"


class GetChatContent:
    def __init__(self):
        llm = ChatOpenAI(model_name=model_name)

        chat_template = """
        请根据我的说话内容:{input_text}。和我进行聊天
        
        AI回答
        """
        # 创建模板(chatgpt聊天模板)
        chat_extraction_prompt = PromptTemplate(
            input_variables=["text_input"],
            template=chat_template
        )

        # 定义chain
        self.chat_extraction_chain = LLMChain(llm=llm, prompt=chat_extraction_prompt)

    def __call__(self, text):
        chatContent = self.chat_extraction_chain(text)
        return chatContent


# 测试
if __name__ == '__main__':
    verbal = IdentifyVerbal.IdentifyVerbal()
    res = verbal(
        "https://isv-data.oss-cn-hangzhou.aliyuncs.com/ics/MaaS/ASR/test_audio/asr_vad_punc_example.wav")
    Content = GetChatContent()
    print(Content(res))
