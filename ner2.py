import torch
from transformers import RobertaTokenizer, RobertaForTokenClassification
from transformers import pipeline

tokenizer = RobertaTokenizer.from_pretrained("Jean-Baptiste/roberta-large-ner-english")
model = RobertaForTokenClassification.from_pretrained("Jean-Baptiste/roberta-large-ner-english")


def get_entity(text):
    nlp = pipeline("ner", model=model, tokenizer=tokenizer)
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
    from read_data import get_data
    text = get_data()[1][0:100]
    # text = "The new assembly hall, Dasaratha’s latest pride, was crowded all"
    inputs = tokenizer(
        text, add_special_tokens=False, return_tensors="pt"
    )
    tokenized_text = tokenizer.tokenize(text)

    with torch.no_grad():
        logits = model(**inputs).logits

    predicted_token_class_ids = logits.argmax(-1)

    # Note that tokens are classified rather then input words which means that
    # there might be more predicted token classes than words.
    # Multiple token classes might account for the same word
    predicted_tokens_classes = [model.config.id2label[t.item()] for t in predicted_token_class_ids[0]]
    predicted_tokens_classes
