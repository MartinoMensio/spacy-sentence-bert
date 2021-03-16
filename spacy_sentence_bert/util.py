import json
from pathlib import Path

try:  # Python 3.8
    import importlib.metadata as importlib_metadata
except ImportError:
    import importlib_metadata  # noqa: F401


pkg_meta = importlib_metadata.metadata(__name__.split(".")[0])

# From https://www.sbert.net/docs/pretrained_models.html
configs = {
    # Paraphrase Identification
    'en_paraphrase_distilroberta_base_v1': {
        'spacy_base_model': 'en',
        'dimensions': 768,
        'name': 'paraphrase-distilroberta-base-v1'
    },
    'xx_paraphrase_xlm_r_multilingual_v1': {
        'spacy_base_model': 'xx',
        'dimensions': 768,
        'name': 'paraphrase-xlm-r-multilingual-v1'
    },
    # Semantic Textual Similarity
    # https://docs.google.com/spreadsheets/d/14QplCdTCDwEmTqrn1LH4yrbKvdogK4oQvYO1K1aPR5M/edit#gid=0
    'en_stsb_roberta_large': { # previously named en_roberta_large_nli_stsb_mean_tokens
        'spacy_base_model': 'en',
        'dimensions': 1024,
        'name': 'stsb-roberta-large'
    },
    'en_stsb_roberta_base': { # previously named en_roberta_base_nli_stsb_mean_tokens
        'spacy_base_model': 'en',
        'dimensions': 768,
        'name': 'stsb-roberta-base'
    },
    'en_stsb_bert_large': { # previously named en_bert_large_nli_stsb_mean_tokens
        'spacy_base_model': 'en',
        'dimensions': 1024,
        'name': 'stsb-bert-large'
    },
    'en_stsb_distilbert_base': { # previously named en_distilbert_base_nli_stsb_mean_tokens
        'spacy_base_model': 'en',
        'dimensions': 768,
        'name': 'stsb-distilbert-base'
    },
    'en_stsb_bert_base': { # previously named en_bert_base_nli_stsb_mean_tokens
        'spacy_base_model': 'en',
        'dimensions': 768,
        'name': 'stsb-bert-base'
    },
    'en_nli_bert_large': { # previously named en_bert_large_nli_mean_tokens
        'spacy_base_model': 'en',
        'dimensions': 1024,
        'name': 'nli-bert-large'
    },
    'en_nli_distilbert_base': { # previously named en_distilbert_base_nli_mean_tokens
        'spacy_base_model': 'en',
        'dimensions': 768,
        'name': 'nli-distilbert-base'
    },
    'en_nli_roberta_large': { # previously named en_roberta_large_nli_mean_tokens
        'spacy_base_model': 'en',
        'dimensions': 1024,
        'name': 'nli-roberta-large'
    },
    'en_nli_bert_large_max_pooling': { # previously named en_bert_large_nli_max_tokens
        'spacy_base_model': 'en',
        'dimensions': 1024,
        'name': 'nli-bert-large-max-pooling'
    },
    'en_nli_bert_large_cls_pooling': { # previously named en_bert_large_nli_cls_token
        'spacy_base_model': 'en',
        'dimensions': 1024,
        'name': 'nli-bert-large-cls-pooling'
    },
    'en_nli_distilbert_base_max_pooling': { # new
        'spacy_base_model': 'en',
        'dimensions': 768,
        'name': 'nli-distilbert-base-max-pooling'
    },
    'en_nli_roberta_base': { # previously named en_roberta_base_nli_mean_tokens
        'spacy_base_model': 'en',
        'dimensions': 768,
        'name': 'nli-roberta-base'
    },
    'en_nli_bert_base_max_pooling': { # previously named en_bert_base_nli_max_tokens
        'spacy_base_model': 'en',
        'dimensions': 768,
        'name': 'nli-bert-base-max-pooling'
    },
    'en_nli_bert_base': { # previously named en_bert_base_nli_mean_tokens
        'spacy_base_model': 'en',
        'dimensions': 768,
        'name': 'nli-bert-base'
    },
    'en_nli_bert_base_cls_pooling': { # previously named en_bert_base_nli_cls_token
        'spacy_base_model': 'en',
        'dimensions': 768,
        'name': 'nli-bert-base-cls-pooling'
    },
    # Average Word Embeddings Models
    'en_average_word_embeddings_glove.6B.300d': {
        'spacy_base_model': 'en',
        'dimensions': 300,
        'name': 'average_word_embeddings_glove.6B.300d'
    },
    'en_average_word_embeddings_komninos': {
        'spacy_base_model': 'en',
        'dimensions': 300,
        'name': 'average_word_embeddings_komninos'
    },
    'en_average_word_embeddings_levy_dependency': {
        'spacy_base_model': 'en',
        'dimensions': 300,
        'name': 'average_word_embeddings_levy_dependency'
    },
    'en_average_word_embeddings_glove.840B.300d': {
        'spacy_base_model': 'en',
        'dimensions': 300,
        'name': 'average_word_embeddings_glove.840B.300d'
    },
    # Duplicate Questions Detection
    'en_quora_distilbert_base': {
        'spacy_base_model': 'en',
        'dimensions': 768,
        'name': 'quora-distilbert-base'
    },
    'xx_quora_distilbert_multilingual': {
        'spacy_base_model': 'xx',
        'dimensions': 768,
        'name': 'quora-distilbert-multilingual'
    },
    # Question-Answer Retrieval - MSMARCO
    'en_msmarco_distilroberta_base_v2': {
        'spacy_base_model': 'en',
        'dimensions': 768,
        'name': 'msmarco-distilroberta-base-v2'
    },
    'en_msmarco_roberta_base_v2': {
        'spacy_base_model': 'en',
        'dimensions': 768,
        'name': 'msmarco-roberta-base-v2'
    },
    'en_msmarco_distilbert_base_v2': {
        'spacy_base_model': 'en',
        'dimensions': 768,
        'name': 'msmarco-distilbert-base-v2'
    },
    # Question-Answer Retrieval - Natural Questions
    'en_nq_distilbert_base_v1': {
        'spacy_base_model': 'en',
        'dimensions': 768,
        'name': 'nq-distilbert-base-v1'
    },
    # Multi-Lingual Models
    'xx_distiluse_base_multilingual_cased_v2': {
        'spacy_base_model': 'xx',
        'dimensions': 512,
        'name': 'distiluse-base-multilingual-cased-v2'
    },
    'xx_stsb_xlm_r_multilingual': {
        'spacy_base_model': 'xx',
        'dimensions': 768,
        'name': 'stsb-xlm-r-multilingual'
    },
    'xx_cross_en_de_roberta_sentence_transformer': {
        'spacy_base_model': 'xx',
        'dimensions': 768,
        'name': 'T-Systems-onsite/cross-en-de-roberta-sentence-transformer'
    },
    # Bitext mining
    'xx_LaBSE': {
        'spacy_base_model': 'xx',
        'dimensions': 768,
        'name': 'LaBSE'
    },
    # Scientific Publications
    'en_allenai_specter': {
        'spacy_base_model': 'en',
        'dimensions': 768,
        'name': 'allenai-specter'
    },




    ### These old models can still be loaded from their SentenceBert model name
    # 'xx_distiluse_base_multilingual_cased': {
    #     'spacy_base_model': 'xx',
    #     'dimensions': 512,
    #     'name': 'distiluse-base-multilingual-cased'
    # },
    # 'xx_xlm_r_base_en_ko_nli_ststb': {
    #     'spacy_base_model': 'xx',
    #     'dimensions': 768,
    #     'name': 'xlm-r-base-en-ko-nli-ststb'
    # },
    # 'xx_xlm_r_large_en_ko_nli_ststb': {
    #     'spacy_base_model': 'xx',
    #     'dimensions': 1024,
    #     'name': 'xlm-r-large-en-ko-nli-ststb'
    # },
}

def create_lang(model_name):
    '''Creates a Language object from the `model_name`'''
    from . import language
    nlp = language.create_nlp(model_name)
    if model_name in configs:
        selected_config = configs[model_name]
        nlp.vocab.reset_vectors(width=selected_config['dimensions']) # does not do anything!
        with open(Path(__file__).parent.absolute() / 'meta' / f'{model_name}.json') as f:
            nlp.meta = json.load(f)
    return nlp

def name_spacy_to_sentencebert(spacy_name):
    # remove initial prefix
    # result = spacy_name[3:]
    # from underscore to dash
    result = spacy_name.replace('_', '-')
    return result
