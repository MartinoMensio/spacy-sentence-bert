import typer
from spacy_sentence_bert import language, util

def main(model_name):
    if model_name not in util.configs:
        raise ValueError(f'Model "{model_name}" not available')
    nlp = util.create_lang(model_name)
    print(nlp.pipe_names)
    doc = nlp('Hello my friend')
    print(doc.vector.shape)
    nlp.to_disk(f'models/{model_name}')

if __name__ == "__main__":
    typer.run(main)