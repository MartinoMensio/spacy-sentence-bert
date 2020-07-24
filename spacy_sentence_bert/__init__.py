# coding: utf8
from __future__ import unicode_literals

import os
from pathlib import Path
import spacy
from spacy.util import load_model_from_init_py, get_model_meta
from spacy.language import Language
from spacy.tokens import Span
from spacy.matcher import Matcher
import warnings
from . import util
from .util import create_lang
from sentence_transformers import SentenceTransformer

from .util import create_lang as load_model

__version__ = util.pkg_meta["version"]


from .language import SentenceBert
SentenceBert.install_extensions()

# warning suppress for empty vocabulary
warnings.filterwarnings('ignore', message=r"\[W007\]", category=UserWarning)

Language.factories['sentencebert_overwrite_vectors'] = lambda nlp, **cfg: OverwriteVectors(nlp, **cfg)
Language.factories['sentencebert_add_model_to_doc'] = lambda nlp, **cfg: AddModelToDoc(nlp, **cfg)

def load(**overrides):
    return load_model_from_init_py(__file__, **overrides)


def create_from(nlp, model_name):
    '''From an existing `nlp` object, adds the vectors from the specific `model_name` by adding pipeline stages'''
    if model_name not in util.configs:
        raise ValueError(f'Model "{model_name}" not available')
    config = util.configs[model_name]
    return SentenceBert.create_nlp(config, nlp)


class OverwriteVectors(object):
    '''Factory of the `sentencebert_overwrite_vectors` pipeline stage. It tells spacy how to create the stage '''
    name = 'sentencebert_overwrite_vectors'

    def __init__(self, nlp):
        # TODO could add a cache, configurable, to store already computed vectors
        # enable_cache = cfg.get('enable_cache', True)
        pass

    def __call__(self, doc):
        SentenceBert.overwrite_vectors(doc)
        return doc

class AddModelToDoc(object):
    '''Factory of the `sentencebert_add_model_to_doc` pipeline stage. It tells spacy how to create the stage '''
    name = 'sentencebert_add_model_to_doc'

    def __init__(self, nlp):
        spacy_name = nlp.meta['name']
        model_name = util.name_spacy_to_sentencebert(spacy_name)
        self.model = SentenceTransformer(model_name)


    def __call__(self, doc):
        doc._.sentence_bert_model = self.model
        return doc
