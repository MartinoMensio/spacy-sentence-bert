set -e


VERSION=0.1.2

for FILE_NAME in spacy_sentence_bert/meta/*.json
do
    MODEL_NAME="$(basename -- ${FILE_NAME%.*})"
    echo $MODEL_NAME
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
