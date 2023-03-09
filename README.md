[![Tests](https://github.com/MartinoMensio/spacy-sentence-bert/actions/workflows/tests.yml/badge.svg)](https://github.com/egerber/spaCy-entity-linker/actions/workflows/tests.yml)
[![Downloads](https://static.pepy.tech/badge/spacy-sentence-bert)](https://pepy.tech/project/spacy-sentence-bert)
[![Current Release Version](https://img.shields.io/github/release/MartinoMensio/spacy-sentence-bert.svg?style=flat-square&logo=github)](https://github.com/MartinoMensio/spacy-sentence-bert/releases)
[![pypi Version](https://img.shields.io/pypi/v/spacy-sentence-bert.svg?style=flat-square&logo=pypi&logoColor=white)](https://pypi.org/project/spacy-sentence-bert/)
# Sentence-BERT for spaCy

This package wraps [sentence-transformers](https://github.com/UKPLab/sentence-transformers) (also known as [sentence-BERT](http://arxiv.org/abs/1908.10084)) directly in spaCy.
You can substitute the vectors provided in any [spaCy model](https://spacy.io/models) with vectors that have been tuned specifically for semantic similarity.

The models below are suggested for analysing sentence similarity, as the STS benchmark indicates.
Keep in mind that `sentence-transformers` are configured with a maximum sequence length of 128. Therefore for longer texts it may be more suitable to work with other models (e.g. [Universal Sentence Encoder](https://github.com/MartinoMensio/spacy-universal-sentence-encoder-tfhub)).

## Install

Compatibility:
- python 3.7/3.8/3.9/3.10
- spaCy>=3.0.0,<4.0.0, last tested on version 3.5
- sentence-transformers: tested on version 2.2.2

To install this package, you can run one of the following:

- `pip install spacy-sentence-bert`
-  `pip install git+https://github.com/MartinoMensio/spacy-sentence-bert.git`

You can install standalone spaCy packages from GitHub with pip. If you install standalone packages, you will be able to load a language model directly by using the `spacy.load` API, without need to add a pipeline stage.
This table takes the models listed on the [Sentence Transformers documentation](https://www.sbert.net/docs/pretrained_models.html) and shows some statistics along with the instruction to install the standalone models.
If you don't want to install the standalone models, you can still use them by adding a pipeline stage (see below).


|  sentence-BERT name                    |  spacy model name  |  dimensions          |  language  | STS benchmark | standalone install |
|----------------------------------------|--------------------|----------------------|------------|---------------|---------|
| `paraphrase-distilroberta-base-v1`     | `en_paraphrase_distilroberta_base_v1`            |  768 | en | 81.81          | `pip install https://github.com/MartinoMensio/spacy-sentence-bert/releases/download/v0.1.2/en_paraphrase_distilroberta_base_v1-0.1.2.tar.gz#en_paraphrase_distilroberta_base_v1-0.1.2`  |
| `paraphrase-xlm-r-multilingual-v1`     | `xx_paraphrase_xlm_r_multilingual_v1`            |  768 | 50+ | 83.50          | `pip install https://github.com/MartinoMensio/spacy-sentence-bert/releases/download/v0.1.2/xx_paraphrase_xlm_r_multilingual_v1-0.1.2.tar.gz#xx_paraphrase_xlm_r_multilingual_v1-0.1.2`  |
| `stsb-roberta-large`   | `en_stsb_roberta_large`   | 1024 | en | 86.39          | `pip install https://github.com/MartinoMensio/spacy-sentence-bert/releases/download/v0.1.2/en_stsb_roberta_large-0.1.2.tar.gz#en_stsb_roberta_large-0.1.2`  |
| `stsb-roberta-base`    | `en_stsb_roberta_base`    |  768 | en | 85.44          | `pip install https://github.com/MartinoMensio/spacy-sentence-bert/releases/download/v0.1.2/en_stsb_roberta_base-0.1.2.tar.gz#en_stsb_roberta_base-0.1.2`  |
| `stsb-bert-large`      | `en_stsb_bert_large`      | 1024 | en | 85.29          | `pip install https://github.com/MartinoMensio/spacy-sentence-bert/releases/download/v0.1.2/en_stsb_bert_large-0.1.2.tar.gz#en_stsb_bert_large-0.1.2`  |
| `stsb-distilbert-base` | `en_stsb_distilbert_base` |  768 | en | 85.16          | `pip install https://github.com/MartinoMensio/spacy-sentence-bert/releases/download/v0.1.2/en_stsb_distilbert_base-0.1.2.tar.gz#en_stsb_distilbert_base-0.1.2`  |
| `stsb-bert-base`       | `en_stsb_bert_base`       |  768 | en | 85.14          | `pip install https://github.com/MartinoMensio/spacy-sentence-bert/releases/download/v0.1.2/en_stsb_bert_base-0.1.2.tar.gz#en_stsb_bert_base-0.1.2`  |
| `nli-bert-large`           | `en_nli_bert_large`           | 1024 | en | 79.19          | `pip install https://github.com/MartinoMensio/spacy-sentence-bert/releases/download/v0.1.2/en_nli_bert_large-0.1.2.tar.gz#en_nli_bert_large-0.1.2`  |
| `nli-distilbert-base`      | `en_nli_distilbert_base`      |  768 | en | 78.69          | `pip install https://github.com/MartinoMensio/spacy-sentence-bert/releases/download/v0.1.2/en_nli_distilbert_base-0.1.2.tar.gz#en_nli_distilbert_base-0.1.2`  |
| `nli-roberta-large`        | `en_nli_roberta_large`        | 1024 | en | 78.69          | `pip install https://github.com/MartinoMensio/spacy-sentence-bert/releases/download/v0.1.2/en_nli_roberta_large-0.1.2.tar.gz#en_nli_roberta_large-0.1.2`  |
| `nli-bert-large-max-pooling`            | `en_nli_bert_large_max_pooling`            | 1024 | en | 78.41          | `pip install https://github.com/MartinoMensio/spacy-sentence-bert/releases/download/v0.1.2/en_nli_bert_large_max_pooling-0.1.2.tar.gz#en_nli_bert_large_max_pooling-0.1.2`  |
| `nli-bert-large-cls-pooling`             | `en_nli_bert_large_cls_pooling`            | 1024 | en | 78.29          | `pip install https://github.com/MartinoMensio/spacy-sentence-bert/releases/download/v0.1.2/en_nli_bert_large_cls_pooling-0.1.2.tar.gz#en_nli_bert_large_cls_pooling-0.1.2`  |
| `nli-distilbert-base-max-pooling`             | `en_nli_distilbert_base_max_pooling`            | 768 | en | 77.61          | `pip install https://github.com/MartinoMensio/spacy-sentence-bert/releases/download/v0.1.2/en_nli_distilbert_base_max_pooling-0.1.2.tar.gz#en_nli_distilbert_base_max_pooling-0.1.2`  |
| `nli-roberta-base`         | `en_nli_roberta_base`         |  768 | en | 77.49          | `pip install https://github.com/MartinoMensio/spacy-sentence-bert/releases/download/v0.1.2/en_nli_roberta_base-0.1.2.tar.gz#en_nli_roberta_base-0.1.2`  |
| `nli-bert-base-max-pooling`             | `en_nli_bert_base_max_pooling`             |  768 | en | 77.21          | `pip install https://github.com/MartinoMensio/spacy-sentence-bert/releases/download/v0.1.2/en_nli_bert_base_max_pooling-0.1.2.tar.gz#en_nli_bert_base_max_pooling-0.1.2`  |
| `nli-bert-base`            | `en_nli_bert_base`            |  768 | en | 77.12          | `pip install https://github.com/MartinoMensio/spacy-sentence-bert/releases/download/v0.1.2/en_nli_bert_base-0.1.2.tar.gz#en_nli_bert_base-0.1.2`  |
| `nli-bert-base-cls-pooling`              | `en_nli_bert_base_cls_pooling`              |  768 | en | 76.30          | `pip install https://github.com/MartinoMensio/spacy-sentence-bert/releases/download/v0.1.2/en_nli_bert_base_cls_pooling-0.1.2.tar.gz#en_nli_bert_base_cls_pooling-0.1.2`  |
| `average_word_embeddings_glove.6B.300d`              | `en_average_word_embeddings_glove.6B.300d`              |  768 | en | 61.77          | `pip install https://github.com/MartinoMensio/spacy-sentence-bert/releases/download/v0.1.2/en_average_word_embeddings_glove.6B.300d-0.1.2.tar.gz#en_average_word_embeddings_glove.6B.300d-0.1.2`  |
| `average_word_embeddings_komninos`              | `en_average_word_embeddings_komninos`              |  768 | en | 61.56          | `pip install https://github.com/MartinoMensio/spacy-sentence-bert/releases/download/v0.1.2/en_average_word_embeddings_komninos-0.1.2.tar.gz#en_average_word_embeddings_komninos-0.1.2`  |
| `average_word_embeddings_levy_dependency`              | `en_average_word_embeddings_levy_dependency`              |  768 | en | 59.22          | `pip install https://github.com/MartinoMensio/spacy-sentence-bert/releases/download/v0.1.2/en_average_word_embeddings_levy_dependency-0.1.2.tar.gz#en_average_word_embeddings_levy_dependency-0.1.2`  |
| `average_word_embeddings_glove.840B.300d`              | `en_average_word_embeddings_glove.840B.300d`              |  768 | en | 52.54          | `pip install https://github.com/MartinoMensio/spacy-sentence-bert/releases/download/v0.1.2/en_average_word_embeddings_glove.840B.300d-0.1.2.tar.gz#en_average_word_embeddings_glove.840B.300d-0.1.2`  |
| `quora-distilbert-base`              | `en_quora_distilbert_base`              |  768 | en | N/A          | `pip install https://github.com/MartinoMensio/spacy-sentence-bert/releases/download/v0.1.2/en_quora_distilbert_base-0.1.2.tar.gz#en_quora_distilbert_base-0.1.2`  |
| `quora-distilbert-multilingual`              | `xx_quora_distilbert_multilingual`              |  768 | 50+ | N/A          | `pip install https://github.com/MartinoMensio/spacy-sentence-bert/releases/download/v0.1.2/xx_quora_distilbert_multilingual-0.1.2.tar.gz#xx_quora_distilbert_multilingual-0.1.2`  |
| `msmarco-distilroberta-base-v2`              | `en_msmarco_distilroberta_base_v2`              |  768 | en | N/A          | `pip install https://github.com/MartinoMensio/spacy-sentence-bert/releases/download/v0.1.2/en_msmarco_distilroberta_base_v2-0.1.2.tar.gz#en_msmarco_distilroberta_base_v2-0.1.2`  |
| `msmarco-roberta-base-v2`              | `en_msmarco_roberta_base_v2`              |  768 | en | N/A          | `pip install https://github.com/MartinoMensio/spacy-sentence-bert/releases/download/v0.1.2/en_msmarco_roberta_base_v2-0.1.2.tar.gz#en_msmarco_roberta_base_v2-0.1.2`  |
| `msmarco-distilbert-base-v2`              | `en_msmarco_distilbert_base_v2`              |  768 | en | N/A          | `pip install https://github.com/MartinoMensio/spacy-sentence-bert/releases/download/v0.1.2/en_msmarco_distilbert_base_v2-0.1.2.tar.gz#en_msmarco_distilbert_base_v2-0.1.2`  |
| `nq-distilbert-base-v1`              | `en_nq_distilbert_base_v1`              |  768 | en | N/A          | `pip install https://github.com/MartinoMensio/spacy-sentence-bert/releases/download/v0.1.2/en_nq_distilbert_base_v1-0.1.2.tar.gz#en_nq_distilbert_base_v1-0.1.2`  |
| `distiluse-base-multilingual-cased-v2`              | `xx_distiluse_base_multilingual_cased_v2`              |  512 | 50+ | N/A          | `pip install https://github.com/MartinoMensio/spacy-sentence-bert/releases/download/v0.1.2/xx_distiluse_base_multilingual_cased_v2-0.1.2.tar.gz#xx_distiluse_base_multilingual_cased_v2-0.1.2`  |
| `stsb-xlm-r-multilingual`    | `xx_stsb_xlm_r_multilingual`    |  768 | 50+ | N/A | `pip install https://github.com/MartinoMensio/spacy-sentence-bert/releases/download/v0.1.2/xx_stsb_xlm_r_multilingual-0.1.2.tar.gz#xx_stsb_xlm_r_multilingual-0.1.2`  |
| `T-Systems-onsite/cross-en-de-roberta-sentence-transformer`              | `xx_cross_en_de_roberta_sentence_transformer`              |  768 | en,de | N/A          | `pip install https://github.com/MartinoMensio/spacy-sentence-bert/releases/download/v0.1.2/xx_cross_en_de_roberta_sentence_transformer-0.1.2.tar.gz#xx_cross_en_de_roberta_sentence_transformer-0.1.2`  |
| `LaBSE`              | `xx_LaBSE`              |  768 | 109 | N/A          | `pip install https://github.com/MartinoMensio/spacy-sentence-bert/releases/download/v0.1.2/xx_LaBSE-0.1.2.tar.gz#xx_LaBSE-0.1.2`  |
| `allenai-specter`              | `en_allenai_specter`              |  768 | en | N/A          | `pip install https://github.com/MartinoMensio/spacy-sentence-bert/releases/download/v0.1.2/en_allenai_specter-0.1.2.tar.gz#en_allenai_specter-0.1.2`  |

If your model is not in this list (e.g., `xlm-r-base-en-ko-nli-ststb`), you can still use it with this library but not as a standalone language. You will need to add a pipeline stage properly configured (see below the `nlp.add_pipe` API).



## Usage

There are different ways to load the models of `sentence-bert`.

- `spacy.load` API: you need to have installed one of the models from the table above
- `spacy_sentence_bert.load_model`: you can load one of the models from the table above without having installed the standalone packages
- `nlp.add_pipe` API: you can load any of the `sentence-bert` models on top of your `nlp` object


### `spacy.load` API

Standalone model installed from GitHub (e.g., from the table above, `pip install https://github.com/MartinoMensio/spacy-sentence-bert/releases/download/v0.1.2/en_stsb_roberta_large-0.1.2.tar.gz#en_stsb_roberta_large-0.1.2`), you can load directly the model with the spaCy API:

```python
import spacy
nlp = spacy.load('en_stsb_roberta_large')
```

### `spacy_sentence_bert.load_model` API

You can obtain the same result without having to install the standalone model, by using this method:

```python
import spacy_sentence_bert
nlp = spacy_sentence_bert.load_model('en_stsb_roberta_large')
```

### `nlp.add_pipe` API

If you want to use one of the sentence embeddings over an existing Language object, you can use the `nlp.add_pipe` method.
This also works if you want to use a language model that is not listed in the table above. Just make sure that [sentence-transformers](https://github.com/UKPLab/sentence-transformers) supports it.

```python
import spacy
nlp = spacy.blank('en')
nlp.add_pipe('sentence_bert', config={'model_name': 'allenai-specter'})
nlp.pipe_names
```

The models, when first used, download sentence-BERT to the folder defined with `TORCH_HOME` in the environment variables (default `~/.cache/torch`).

Once you have loaded the model, use it through the `vector` property and the `similarity` method of spaCy:

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



## Utils

To build and upload
```bash
VERSION=0.1.2
# build the standalone models (17)
./build_models.sh
# build the archive at dist/spacy_sentence_bert-${VERSION}.tar.gz
python setup.py sdist
# upload to pypi
twine upload dist/spacy_sentence_bert-${VERSION}.tar.gz
```