import spacy

from spacy.language import Language
from spacy.tokens import Doc, Span, Token
from sentence_transformers import SentenceTransformer

from . import util


def get_vector(sent):
    doc = sent.doc
    model_name = doc._.sentence_bert_model_name
    model = SentenceBert.get_model(model_name)
    vector = model.encode([sent.text])[0]
    return vector

# create an extension where the model will be used
Doc.set_extension('sentence_bert_model_name', default=None, force=True)

# set the extension both on doc and span level. This will contain the computed vector
Token.set_extension('sentence_bert', getter=get_vector, force=True)
Span.set_extension('sentence_bert', getter=get_vector, force=True)
Doc.set_extension('sentence_bert', getter=get_vector, force=True)

# the pipeline stage factory
@Language.factory('sentence_bert', default_config={
    'model_name': None,
    'debug': True
})
def sentence_bert_factory(nlp, name, model_name, debug):
    if model_name:
        # esplicitly chosen
        if model_name in util.configs:
            # one of the known ones
            config = util.configs[model_name]
            model_name = config['name']
        else:
            # may be a SentenceBert model name directly
            try:
                return SentenceBert(model_name, debug=debug)
            except:
                raise ValueError(f'Model "{model_name}" not available. Please choose one of {list(util.configs.keys())} or use one of the allowed values by SentenceBert.')
    else:
        # try to map from existing nlp
        # the language code needs to match
        meta_lang = nlp.meta['lang']
        # try to map from the model name
        meta_name = nlp.meta["name"]
        model_name = f'{meta_lang}_{meta_name}'
        if model_name not in util.configs:
            raise ValueError(f'Could not map nlp.meta["lang"]={meta_lang} and nlp.meta["name"]={meta_name} to an existing model.\n'
                    f'Please set the parameter "model_name" to one of {list(util.configs.keys())} or to a SentenceBert model name.')
    return SentenceBert(model_name, debug=debug)


class SentenceBert(object):

    models = {}

    def __init__(self, model_name: str, debug: bool) -> None:
        self.model = SentenceBert.get_model(model_name)
        self.model_name = model_name

    def __call__(self, doc):
        doc._.sentence_bert_model_name = self.model_name
        set_hooks(doc)
        return doc

    @staticmethod
    def get_model(model_name: str):
        if model_name in SentenceBert.models:
            model = SentenceBert.models[model_name]
        else:
            model = SentenceTransformer(model_name)
            SentenceBert.models[model_name] = model
        return model


def set_hooks(doc):
    '''Overwrites the vectors from extension attributes'''
    doc.user_hooks["vector"] = lambda a: a._.sentence_bert
    doc.user_span_hooks["vector"] = lambda a: a._.sentence_bert
    doc.user_token_hooks["vector"] = lambda a: a._.sentence_bert
    return doc


def create_nlp(model_name, nlp=None):
    if not nlp:
        if model_name not in util.configs:
            raise ValueError(f'Model "{model_name}" not available')
        config = util.configs[model_name]
        nlp = spacy.blank(config['spacy_base_model'])
        nlp.add_pipe('sentencizer')
    nlp.add_pipe('sentence_bert', config={'model_name': model_name}, first=True)

    return nlp
