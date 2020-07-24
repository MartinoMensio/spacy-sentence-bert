set -e


VERSION=0.0.4

for MODEL_NAME in en_bert_base_nli_cls_token en_bert_base_nli_max_tokens en_bert_base_nli_mean_tokens \
    en_bert_large_nli_mean_tokens en_bert_large_nli_max_tokens en_bert_large_nli_cls_token \
    en_roberta_base_nli_mean_tokens en_roberta_large_nli_mean_tokens \
    en_distilbert_base_nli_mean_tokens \
    en_bert_base_nli_stsb_mean_tokens en_bert_large_nli_stsb_mean_tokens \
    en_roberta_base_nli_stsb_mean_tokens en_roberta_large_nli_stsb_mean_tokens \
    en_distilbert_base_nli_stsb_mean_tokens \
    xx_distiluse_base_multilingual_cased xx_xlm_r_base_en_ko_nli_ststb xx_xlm_r_large_en_ko_nli_ststb
do
    echo "Creating $MODEL_NAME package"
    mkdir -p models/$MODEL_NAME
    # create the nlp and save to disk
    python create.py $MODEL_NAME
    # overwrite meta.json
    # cp spacy_universal_sentence_encoder/meta/$MODEL_NAME.json models/$MODEL_NAME/meta.json

    # create the package
    mkdir -p packages
    python -m spacy package models/$MODEL_NAME packages --force
    pushd packages/$MODEL_NAME-$VERSION
    # zip it
    python setup.py sdist
    # install the tar.gz from dist folder
    pip install dist/$MODEL_NAME-$VERSION.tar.gz
    popd

    python test.py $MODEL_NAME
    echo "$MODEL_NAME-$VERSION has been created successfully"
done
