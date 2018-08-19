import csv
from collections import Counter

import nltk


def extract_place_names(text):
    words = nltk.word_tokenize(text)
    pos_tagged_words = nltk.pos_tag(words)
    tree = nltk.ne_chunk(pos_tagged_words)
    places = []
    for node in tree:
        if isinstance(node, nltk.tree.Tree):
            entity_name = ' '.join([leaf[0] for leaf in node.leaves()])
            print(entity_name, node.label())
            if node.label() in ['GPE', 'LOCATION', 'PERSON', 'ORGANIZATION']:
                places.append(entity_name)
    return places


def ingest_songdata():
    filepath = './data/songdata.csv'
    with open(filepath, newline='') as csvfile:
        reader = csv.reader(csvfile)
        headers = next(reader)
        for row in reader:
            artist, song, link, text = row
            ingest(text, song, artist)


def ingest(lyrics, song_title, artist):
    entries = []
    place_names = extract_place_names(lyrics)
    if not place_names:
        return
    counts = Counter(place_names)
    for name, count in counts.items():
        entries.append({
            'place_name': name,
            'occurrences': count,
            'song': song_title,
            'artist': artist
        })

    return entries
