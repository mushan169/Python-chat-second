from modelscope.pipelines import pipeline
from modelscope.utils.constant import Tasks


# 情绪识别
class TextClassification:
    task = Tasks.text_classification
    model_name = 'damo/nlp_structbert_emotion-classification_chinese-base'
    model_revision = 'v1.0.0'

    def __init__(self):
        self.semantic_cls = pipeline(self.task, self.model_name, model_revision=self.model_revision)

    def classify(self, input_text):
        classifyDict = self.semantic_cls(input=input_text)
        self.semantic_cls(input=input_text)
        scores = classifyDict['scores']
        labels = classifyDict['labels']
        max_value = max(scores)
        max_index = [i for i, x in enumerate(scores) if x == max_value][0]
        return labels[max_index]


if __name__ == '__main__':
    text_classification = TextClassification()
    result = text_classification.classify('新年快乐！')
    print(result)
