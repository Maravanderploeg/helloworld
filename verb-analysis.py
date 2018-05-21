import urllib.request as ur
from wiktionaryparser import WiktionaryParser
from bs4 import BeautifulSoup
import treetaggerwrapper
from examples import articles


def get_info_from_wiktionary(one_word):
    parser = WiktionaryParser()

    word = parser.fetch(one_word, 'german')

    definitions = word[0]['definitions']
    print(definitions)


def get_text_from_url(url):
    """
    :param url: a string with the url where to get the stuff from
    :return: the text of the url
    """
    s = ur.urlopen(url)
    html = s.read().decode('utf-8')

    soup = BeautifulSoup(html)
    for script in soup(["script", "style"]):
        script.extract()
    text = soup.get_text()

    return text


def print_particle_verbs(tags):
    """

    :param tags: a list of tags from treetagger
    :return: doesn't return anything but prints out stuff
    """

    for each in tags:
        try:
            word, pos, lemma = each.split('\t')
            if pos[0] == 'V':
                current_verb = word
                current_lemma = lemma
            if pos == 'PTKVZ':
                print(current_verb + " " + word)
                infinitive = word + current_lemma
                print(infinitive)
                get_info_from_wiktionary(infinitive)

        except:
            print("!" + each)


def get_tagger(language: str):
    """
    :param language: language code e.g. de,nl
    :return: tagger object
    """
    tagger = treetaggerwrapper.TreeTagger(TAGLANG=language)
    return tagger


def is_particle_verb(word: str, sentence: str, language: str):
    """
    :param word: the word that we want to find out if it's a particle verb
    :param sentence: the sentence in which the word is found
    :param language: the language of the sentence
    :return:
    """
    if word not in sentence:
        return False

    if not has_particle_verb(sentence, language):
        return False

    tagger = get_tagger(language)
    pos_in_sentence = tagger.tag_text(sentence)
    for each in pos_in_sentence:
        triple = each.split("\t")
        if triple[0] == word:
            if triple[1] == "VVFIN":
                return True
    return False


def has_particle_verb(sentence: str, language: str):
    tagger = get_tagger(language)
    pos_in_sentence = tagger.tag_text(sentence)
    print(pos_in_sentence)
    for each in pos_in_sentence:
        triple = each.split("\t")
        print(triple[1])
        if "PTKVZ" == triple[1]:
            return True
    return False


# assert (True == is_particle_verb("kom", "Ik kom in Berlin aan", "nl"))
assert (False == is_particle_verb("müde", "Du siehst müde aus", "de"))
assert (True == is_particle_verb("siehst", "Du siehst müde aus", "de"))
assert (True == is_particle_verb("komme", "Ich komme in Berlin an", "de"))
assert (False == is_particle_verb("an", "Ich komme in Berlin an", "de"))



# print(has_particle_verb("Du siehst müde aus"))

# for article_url in articles:
#     german_text = get_text_from_url(article_url)
#
#     tagger = treetaggerwrapper.TreeTagger(TAGLANG='de')
#     the_tags = tagger.tag_text(german_text)
#
#     print_particle_verbs(the_tags)
