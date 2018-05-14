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


for article_url in articles:
    german_text = get_text_from_url(article_url)

    tagger = treetaggerwrapper.TreeTagger(TAGLANG='de')
    the_tags = tagger.tag_text(german_text)

    print_particle_verbs(the_tags)
