import typer
import spacy
from spacy_sentence_bert import util

def main(model_name):
    nlp = spacy.load(model_name)

    assert nlp.meta['lang'] == model_name[:2]

    assert nlp.meta['name'] == model_name[3:]

    doc = nlp('hi')
    cfg = util.configs[model_name]

    assert doc.vector.shape[0] == cfg['dimensions']


if __name__ == "__main__":
    typer.run(main)