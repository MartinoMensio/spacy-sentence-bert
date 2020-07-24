from setuptools import setup, find_packages

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

def setup_package():
    setup(name="spacy_sentence_bert",
    packages=find_packages(),
    long_description=long_description,
    long_description_content_type='text/markdown',
    package_data={'spacy_sentence_bert': ['meta/*.json']},
    include_package_data=True
    )

if __name__ == "__main__":
    setup_package()
    