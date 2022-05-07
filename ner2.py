from transformers import pipeline
from transformers import RobertaTokenizer, RobertaForTokenClassification


class RobertaNER:
    def __init__(self):
        self.tokenizer = RobertaTokenizer.from_pretrained("Jean-Baptiste/roberta-large-ner-english")
        self.model = RobertaForTokenClassification.from_pretrained("Jean-Baptiste/roberta-large-ner-english")

    def get_entity(self, text: str) -> list:
        """
        :param text: text needed to be inferenced
        :return: return a list of ['tags', 'words']
        """
        nlp = pipeline("ner", model=self.model, tokenizer=self.tokenizer)
        entities = nlp(text)
        words = []
        labels = []
        for i, ety in enumerate(entities):
            if ord(ety['word'][0]) == 288:
                words.append(ety['word'])
                labels.append(ety['entity'])
            else:
                words[-1] += ety['word']

        output = []
        for word, label in zip(words, labels):
            output += [[label, word[1:]]]

        return output


if __name__ == '__main__':
    obj = RobertaNER()
    print(obj.get_entity('I am om rastogi'))