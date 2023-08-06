import spacy
import en_core_web_md
from spacy.lang.en.stop_words import STOP_WORDS
from spacy import displacy
from collections import Counter
import string

nlp = en_core_web_md.load()
PUNCT = string.punctuation


def clean_stop_words(text: str) -> list:

    preprocessed_text: spacy.tokens.doc.Doc = nlp(text)

    sans_stop_words = [
        token.lemma_.lower() for token in preprocessed_text 
        if (not token.is_stop) and
        (token.pos_ == "NOUN" or token.pos_ == "ADJ") and
        (token.text not in PUNCT)
    ]

    return sans_stop_words

def difference(tokens_cv: list[str], tokens_job: list[str]) -> list[str]:

    set_cv = Counter(tokens_cv)
    set_job = Counter(tokens_job)

    difference = [token for token in set_job.keys() if token not in set_cv]
    difference.sort()

    return difference

def difference_score(tokens_cv: list[str], tokens_job: list[str]) -> float:

    unique = difference(tokens_cv, tokens_job)

    return (len(unique)/(len(tokens_job)))

def hash_score(tokens_cv: list[str], tokens_job: list[str]) -> float:

    set_cv = Counter(tokens_cv)
    set_job = Counter(tokens_job)

    matches: Counter[str] = set_cv & set_job
    numerator = matches.values()
    denominator = set_job.values()

    return sum(numerator) / sum(denominator)

def similarity(tokens_a: list[str], tokens_b: list[str]) -> float:

    tokens_a = list(set(tokens_a))
    tokens_a.sort()

    tokens_b = list(set(tokens_b))
    tokens_b.sort()

    string_a: spacy.tokens.doc.Doc = nlp(' '.join(tokens_a))
    string_b: spacy.tokens.doc.Doc = nlp(' '.join(tokens_b))

    return string_b.similarity(string_a)