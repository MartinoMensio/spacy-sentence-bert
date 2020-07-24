# Sentence-BERT for spaCy

This package wraps [sentence-transformers](https://github.com/UKPLab/sentence-transformers) (also known as [sentence-BERT](http://arxiv.org/abs/1908.10084)) directly in spaCy.
You can substitute the vectors provided in any [spaCy model](https://spacy.io/models) with vectors that have been tuned specifically for semantic similarity.

The models below are suggested for analysing sentence similarity, as the STS benchmark indicates.
Keep in mind that `sentence-transformers` are configured with a maximum sequence length of 128. Therefore for longer texts it may be more suitable to work with other models (e.g. [Universal Sentence Encoder](https://github.com/MartinoMensio/spacy-universal-sentence-encoder-tfhub)).

## Install

To install this package, you can run one of the following:

- `pip install spacy_sentence_bert`
-  `pip install git+https://github.com/MartinoMensio/spacy-sentence-bert.git`

## Usage

With this package installed
```python
import spacy_sentence_bert
nlp = spacy_sentence_bert.load_model('en_bert_base_nli_cls_token')
```

Or if a specific model is installed (e.g. `pip install https://github.com/MartinoMensio/spacy-sentence-bert/releases/download/en_bert_base_nli_cls_token-0.1.0/en_bert_base_nli_cls_token-0.1.0.tar.gz`)
```python
import spacy
nlp = spacy.load('en_bert_base_nli_cls_token')
```

```python
import spacy
import spacy_sentence_bert
nlp_base = spacy.load('en')
nlp = spacy_sentence_bert.create_from(nlp_base, 'en_bert_base_nli_cls_token')
nlp.pipe_names
```


Full list of models
https://docs.google.com/spreadsheets/d/14QplCdTCDwEmTqrn1LH4yrbKvdogK4oQvYO1K1aPR5M/edit#gid=0


|  sentence-BERT name                    |  spacy model name  |  dimensions  |  language  | STS benchmark |
|----------------------------------------|--------------------|--------------|------------|---|
| `bert-base-nli-mean-tokens`            | `en_bert_base_nli_mean_tokens` | 768 | en | 77.12 |
| `bert-base-nli-max-tokens`             | `en_bert_base_nli_max_tokens` | 768 | en | 77.21 |
| `bert-base-nli-cls-token`              | `en_bert_base_nli_cls_token` | 768 | en | 76.30 |
| `bert-large-nli-mean-tokens`           | `en_bert_large_nli_mean_tokens` | 1024 | en | 79.19 |
| `bert-large-nli-max-tokens`            | `en_bert_large_nli_max_tokens` | 1024 | en | 78.41 |
| `bert-large-nli-cls-token`             | `en_bert_large_nli_max_tokens` | 1024 | en | 78.29 |
| `roberta-base-nli-mean-tokens`         | `en_roberta_base_nli_mean_tokens` | 768 | en | 77.49 |
| `roberta-large-nli-mean-tokens`        | `en_roberta_large_nli_mean_tokens` | 1024 | en | 78.69 |
| `distilbert-base-nli-mean-tokens`      | `en_distilbert_base_nli_mean_tokens` | 768 | en | 76.97 |
| `bert-base-nli-stsb-mean-tokens`       | `en_bert_base_nli_stsb_mean_tokens` | 768 | en | 85.14 |
| `bert-large-nli-stsb-mean-tokens`      | `en_bert_large_nli_stsb_mean_tokens` | 1024 | en | 85.29 |
| `roberta-base-nli-stsb-mean-tokens`    | `en_roberta_base_nli_stsb_mean_tokens` | 768 | en | 85.40 |
| `roberta-large-nli-stsb-mean-tokens`   | `en_roberta_large_nli_stsb_mean_tokens` | 1024 | en | 86.31 |
| `distilbert-base-nli-stsb-mean-tokens` | `en_distilbert_base_nli_stsb_mean_tokens` | 768 | en | 84.38 |
| `distiluse-base-multilingual-cased`    | `xx_distiluse_base_multilingual_cased` | 512 | Arabic, Chinese, Dutch, English, French, German, Italian, Korean, Polish, Portuguese, Russian, Spanish, Turkish | 80.10 |
| `xlm-r-base-en-ko-nli-ststb`           | `xx_xlm_r_base_en_ko_nli_ststb` | 768 | en,ko | 81.47 |
| `xlm-r-large-en-ko-nli-ststb`          | `xx_xlm_r_base_en_ko_nli_ststb` | 1024 | en,ko | 84.05 |


The models, when first used, download to the folder defined with `TORCH_HOME` in the environment variables (default `~/.cache/torch`).