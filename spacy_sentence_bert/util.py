import json
from pathlib import Path

try:  # Python 3.8
    import importlib.metadata as importlib_metadata
except ImportError:
    import importlib_metadata  # noqa: F401


pkg_meta = importlib_metadata.metadata(__name__.split(".")[0])

configs = {
    'en_bert_base_nli_mean_tokens': {
        'spacy_base_model': 'en',
        'dimensions': 768,
        'name': 'bert-base-nli-mean-tokens'
    },
    'en_bert_base_nli_max_tokens': {
        'spacy_base_model': 'en',
        'dimensions': 768,
        'name': 'bert-base-nli-max-tokens'
    },
    'en_bert_base_nli_cls_token': {
        'spacy_base_model': 'en',
        'dimensions': 768,
        'name': 'bert-base-nli-cls-token'
    },
    'en_bert_large_nli_mean_tokens': {
        'spacy_base_model': 'en',
        'dimensions': 1024,
        'name': 'bert-large-nli-mean-tokens'
    },
    'en_bert_large_nli_max_tokens': {
        'spacy_base_model': 'en',
        'dimensions': 1024,
        'name': 'bert-large-nli-max-tokens'
    },
    'en_bert_large_nli_cls_token': {
        'spacy_base_model': 'en',
        'dimensions': 1024,
        'name': 'bert-large-nli-cls-token'
    },
    'en_roberta_base_nli_mean_tokens': {
        'spacy_base_model': 'en',
        'dimensions': 768,
        'name': 'roberta-base-nli-mean-tokens'
    },
    'en_roberta_large_nli_mean_tokens': {
        'spacy_base_model': 'en',
        'dimensions': 1024,
        'name': 'roberta-large-nli-mean-tokens'
    },
    'en_distilbert_base_nli_mean_tokens': {
        'spacy_base_model': 'en',
        'dimensions': 768,
        'name': 'distilbert-base-nli-mean-tokens'
    },
    'en_bert_base_nli_stsb_mean_tokens': {
        'spacy_base_model': 'en',
        'dimensions': 768,
        'name': 'bert-base-nli-stsb-mean-tokens'
    },
    'en_bert_large_nli_stsb_mean_tokens': {
        'spacy_base_model': 'en',
        'dimensions': 1024,
        'name': 'bert-large-nli-stsb-mean-tokens'
    },
    'en_roberta_base_nli_stsb_mean_tokens': {
        'spacy_base_model': 'en',
        'dimensions': 768,
        'name': 'roberta-base-nli-stsb-mean-tokens'
    },
    'en_roberta_large_nli_stsb_mean_tokens': {
        'spacy_base_model': 'en',
        'dimensions': 1024,
        'name': 'roberta-large-nli-stsb-mean-tokens'
    },
    'en_distilbert_base_nli_stsb_mean_tokens': {
        'spacy_base_model': 'en',
        'dimensions': 768,
        'name': 'distilbert-base-nli-stsb-mean-tokens'
    },
    'xx_distiluse_base_multilingual_cased': {
        'spacy_base_model': 'xx',
        'dimensions': 512,
        'name': 'distiluse-base-multilingual-cased'
    },
    'xx_xlm_r_base_en_ko_nli_ststb': {
        'spacy_base_model': 'xx',
        'dimensions': 768,
        'name': 'xlm-r-base-en-ko-nli-ststb'
    },
    'xx_xlm_r_large_en_ko_nli_ststb': {
        'spacy_base_model': 'xx',
        'dimensions': 1024,
        'name': 'xlm-r-large-en-ko-nli-ststb'
    },
}

def create_lang(model_name):
    '''Creates a Language object from the `model_name`'''
    from . import language
    if model_name not in configs:
        raise ValueError(f'Model "{model_name}" not available')
    selected_config = configs[model_name]
    nlp = language.create_nlp(model_name)
    nlp.vocab.reset_vectors(width=selected_config['dimensions'])
    with open(Path(__file__).parent.absolute() / 'meta' / f'{model_name}.json') as f:
        nlp.meta = json.load(f)
    return nlp

def name_spacy_to_sentencebert(spacy_name):
    # remove initial prefix
    # result = spacy_name[3:]
    # from underscore to dash
    result = spacy_name.replace('_', '-')
    return result
