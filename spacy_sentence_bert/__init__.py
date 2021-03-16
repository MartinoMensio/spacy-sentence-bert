# coding: utf8
from __future__ import unicode_literals

import warnings
from spacy.tokens import Doc
from spacy.util import load_model_from_init_py

from sentence_transformers import SentenceTransformer

from . import util, language
from .language import SentenceBert
from .util import create_lang as load_model

__version__ = util.pkg_meta["version"]



# warning suppress for empty vocabulary
warnings.filterwarnings('ignore', message=r"\[W007\]", category=UserWarning)

def load(**overrides):
    return load_model_from_init_py(__file__, **overrides)


def create_from(nlp, model_name):
    '''From an existing `nlp` object, adds the vectors from the specific `model_name` by adding pipeline stages'''
    return language.SentenceBert.create_nlp(model_name, nlp)

def doc_from_bytes(nlp, bytes):
    """Returns a serialised doc from the bytes coming from `doc.to_bytes()` """
    doc = Doc(nlp.vocab).from_bytes(bytes)
    language.set_hooks(doc)
    return doc
