import spacy

def test_basic_load():
    nlp = spacy.blank("en")
    p = nlp.add_pipe('sentence_bert', config={'model_name': 'stsb-roberta-base'})
    assert p != None
    assert 'sentence_bert' in nlp.pipe_names

def test_load_vector():
    nlp = spacy.blank("en")
    p = nlp.add_pipe('sentence_bert', config={'model_name': 'stsb-roberta-base'})
    assert p != None
    assert 'sentence_bert' in nlp.pipe_names
    doc = nlp("This is a test")
    vector = doc.vector
    assert vector is not None
    shape = vector.shape
    assert shape != None