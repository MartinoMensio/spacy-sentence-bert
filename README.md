# Sentence-BERT for spaCy

This package wraps [sentence-transformers](https://github.com/UKPLab/sentence-transformers) (also known as [sentence-BERT](http://arxiv.org/abs/1908.10084)) directly in spaCy.
You can substitute the vectors provided in any [spaCy model](https://spacy.io/models) with vectors that have been tuned specifically for semantic similarity.

The models below are suggested for analysing sentence similarity, as the STS benchmark indicates.
Keep in mind that `sentence-transformers` are configured with a maximum sequence length of 128. Therefore for longer texts it may be more suitable to work with other models (e.g. [Universal Sentence Encoder](https://github.com/MartinoMensio/spacy-universal-sentence-encoder-tfhub)).

## Install

To install this package, you can run one of the following:

- `pip install spacy_sentence_bert`
-  `pip install git+https://github.com/MartinoMensio/spacy-sentence-bert.git`

You can install standalone spaCy packages from GitHub with pip.
From the [full list of models](https://docs.google.com/spreadsheets/d/14QplCdTCDwEmTqrn1LH4yrbKvdogK4oQvYO1K1aPR5M/edit#gid=0) this table describes the models available.


|  sentence-BERT name                    |  spacy model name  |  dimensions          |  language  | STS benchmark | standalone install |
|----------------------------------------|--------------------|----------------------|------------|---------------|---------|
| `bert-base-nli-mean-tokens`            | `en_bert_base_nli_mean_tokens`            |  768 | en | 77.12          | `pip install https://github.com/MartinoMensio/spacy-sentence-bert/releases/download/v0.0.4/en_bert_base_nli_mean_tokens-0.0.4.tar.gz#en_bert_base_nli_mean_tokens-0.0.4`  |
| `bert-base-nli-max-tokens`             | `en_bert_base_nli_max_tokens`             |  768 | en | 77.21          | `pip install https://github.com/MartinoMensio/spacy-sentence-bert/releases/download/v0.0.4/en_bert_base_nli_max_tokens-0.0.4.tar.gz#en_bert_base_nli_max_tokens-0.0.4`  |
| `bert-base-nli-cls-token`              | `en_bert_base_nli_cls_token`              |  768 | en | 76.30          | `pip install https://github.com/MartinoMensio/spacy-sentence-bert/releases/download/v0.0.4/en_bert_base_nli_cls_token-0.0.4.tar.gz#en_bert_base_nli_cls_token-0.0.4`  |
| `bert-large-nli-mean-tokens`           | `en_bert_large_nli_mean_tokens`           | 1024 | en | 79.19          | `pip install https://github.com/MartinoMensio/spacy-sentence-bert/releases/download/v0.0.4/en_bert_large_nli_mean_tokens-0.0.4.tar.gz#en_bert_large_nli_mean_tokens-0.0.4`  |
| `bert-large-nli-max-tokens`            | `en_bert_large_nli_max_tokens`            | 1024 | en | 78.41          | `pip install https://github.com/MartinoMensio/spacy-sentence-bert/releases/download/v0.0.4/en_bert_large_nli_max_tokens-0.0.4.tar.gz#en_bert_large_nli_max_tokens-0.0.4`  |
| `bert-large-nli-cls-token`             | `en_bert_large_nli_max_tokens`            | 1024 | en | 78.29          | `pip install https://github.com/MartinoMensio/spacy-sentence-bert/releases/download/v0.0.4/en_bert_large_nli_max_tokens-0.0.4.tar.gz#en_bert_large_nli_max_tokens-0.0.4`  |
| `roberta-base-nli-mean-tokens`         | `en_roberta_base_nli_mean_tokens`         |  768 | en | 77.49          | `pip install https://github.com/MartinoMensio/spacy-sentence-bert/releases/download/v0.0.4/en_roberta_base_nli_mean_tokens-0.0.4.tar.gz#en_roberta_base_nli_mean_tokens-0.0.4`  |
| `roberta-large-nli-mean-tokens`        | `en_roberta_large_nli_mean_tokens`        | 1024 | en | 78.69          | `pip install https://github.com/MartinoMensio/spacy-sentence-bert/releases/download/v0.0.4/en_roberta_large_nli_mean_tokens-0.0.4.tar.gz#en_roberta_large_nli_mean_tokens-0.0.4`  |
| `distilbert-base-nli-mean-tokens`      | `en_distilbert_base_nli_mean_tokens`      |  768 | en | 76.97          | `pip install https://github.com/MartinoMensio/spacy-sentence-bert/releases/download/v0.0.4/en_distilbert_base_nli_mean_tokens-0.0.4.tar.gz#en_distilbert_base_nli_mean_tokens-0.0.4`  |
| `bert-base-nli-stsb-mean-tokens`       | `en_bert_base_nli_stsb_mean_tokens`       |  768 | en | 85.14          | `pip install https://github.com/MartinoMensio/spacy-sentence-bert/releases/download/v0.0.4/en_bert_base_nli_stsb_mean_tokens-0.0.4.tar.gz#en_bert_base_nli_stsb_mean_tokens-0.0.4`  |
| `bert-large-nli-stsb-mean-tokens`      | `en_bert_large_nli_stsb_mean_tokens`      | 1024 | en | 85.29          | `pip install https://github.com/MartinoMensio/spacy-sentence-bert/releases/download/v0.0.4/en_bert_large_nli_stsb_mean_tokens-0.0.4.tar.gz#en_bert_large_nli_stsb_mean_tokens-0.0.4`  |
| `roberta-base-nli-stsb-mean-tokens`    | `en_roberta_base_nli_stsb_mean_tokens`    |  768 | en | 85.40          | `pip install https://github.com/MartinoMensio/spacy-sentence-bert/releases/download/v0.0.4/en_roberta_base_nli_stsb_mean_tokens-0.0.4.tar.gz#en_roberta_base_nli_stsb_mean_tokens-0.0.4`  |
| `roberta-large-nli-stsb-mean-tokens`   | `en_roberta_large_nli_stsb_mean_tokens`   | 1024 | en | 86.31          | `pip install https://github.com/MartinoMensio/spacy-sentence-bert/releases/download/v0.0.4/en_roberta_large_nli_stsb_mean_tokens-0.0.4.tar.gz#en_roberta_large_nli_stsb_mean_tokens-0.0.4`  |
| `distilbert-base-nli-stsb-mean-tokens` | `en_distilbert_base_nli_stsb_mean_tokens` |  768 | en | 84.38          | `pip install https://github.com/MartinoMensio/spacy-sentence-bert/releases/download/v0.0.4/en_distilbert_base_nli_stsb_mean_tokens-0.0.4.tar.gz#en_distilbert_base_nli_stsb_mean_tokens-0.0.4`  |
| `distiluse-base-multilingual-cased`    | `xx_distiluse_base_multilingual_cased`    |  512 | Arabic, Chinese, Dutch, English, French, German, Italian, Korean, Polish, Portuguese, Russian, Spanish, Turkish | 80.10 | `pip install https://github.com/MartinoMensio/spacy-sentence-bert/releases/download/v0.0.4/xx_distiluse_base_multilingual_cased-0.0.4.tar.gz#xx_distiluse_base_multilingual_cased-0.0.4`  |
| `xlm-r-base-en-ko-nli-ststb`           | `xx_xlm_r_base_en_ko_nli_ststb`           |  768 | en,ko | 81.47       | `pip install https://github.com/MartinoMensio/spacy-sentence-bert/releases/download/v0.0.4/xx_xlm_r_base_en_ko_nli_ststb-0.0.4.tar.gz#xx_xlm_r_base_en_ko_nli_ststb-0.0.4`  |
| `xlm-r-large-en-ko-nli-ststb`          | `xx_xlm_r_base_en_ko_nli_ststb`           | 1024 | en,ko | 84.05       | `pip install https://github.com/MartinoMensio/spacy-sentence-bert/releases/download/v0.0.4/xx_xlm_r_base_en_ko_nli_ststb-0.0.4.tar.gz#xx_xlm_r_base_en_ko_nli_ststb-0.0.4`  |



## Usage

With this package installed you can obtain a Language model with:

```python
import spacy_sentence_bert
nlp = spacy_sentence_bert.load_model('en_roberta_large_nli_stsb_mean_tokens')
```

Or if a specific standalone model is installed from GitHub, you can load it from spaCy:
```bash
pip install https://github.com/MartinoMensio/spacy-sentence-bert/releases/download/en_roberta_large_nli_stsb_mean_tokens-0.0.4/en_roberta_large_nli_stsb_mean_tokens-0.0.4.tar.gz
```

```python
import spacy
nlp = spacy.load('en_roberta_large_nli_stsb_mean_tokens')
```

Or if you want to use one of the sentence embeddings over an existing Language object, you can use the `create_from` method:

```python
import spacy
import spacy_sentence_bert
nlp_base = spacy.load('en')
nlp = spacy_sentence_bert.create_from(nlp_base, 'en_bert_base_nli_cls_token')
nlp.pipe_names
```

Once you have loaded the model, simply use it to obtain `vector`s and using the `similarity` method of spaCy:

```python
# get two documents
doc_1 = nlp('Hi there, how are you?')
doc_2 = nlp('Hello there, how are you doing today?')
# get the vector of the Doc, Span or Token
print(doc_1.vector.shape)
print(doc_1[3].vector.shape)
print(doc_1[2:4].vector.shape)
# or use the similarity method that is based on the vectors, on Doc, Span or Token
print(doc_1.similarity(doc_2[0:7]))
```




The models, when first used, download to the folder defined with `TORCH_HOME` in the environment variables (default `~/.cache/torch`).


## Utils

To build and upload
```bash
VERSION=0.0.4
# build the standalone models
./build_models.sh
# build dist/spacy_sentence_bert-${VERSION}.tar.gz
python setup.py sdist
# upload to pypi
twine upload dist/spacy_sentence_bert-${VERSION}.tar.gz
```