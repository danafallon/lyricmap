import sqlite3


def create_places_table(cursor):
    cursor.execute("""
        CREATE TABLE places (
            id integer PRIMARY KEY,
            name text NOT NULL,
            full_name text,
            type text,
            geojson text,
        )
    """)

def create_songs_table(cursor):
    cursor.execute("""
        CREATE TABLE songs (
            id integer PRIMARY KEY,
            title text NOT NULL,
            artist text NOT NULL,
            lyrics text NOT NULL,
            album text,
            year text,
            genre text,
        )
    """)

def create_mentions_table(cursor):
    cursor.execute("""
        CREATE TABLE mentions (
            id integer PRIMARY KEY,
            place_id integer,
            song_id integer,
            position integer,
            context text,
            FOREIGN KEY (place_id) REFERENCES places (id)
            FOREIGN KEY (song_id) REFERENCES songs (id)
        )
    """)

def create_all_tables():
    conn = sqlite3.connect('lyricmap.db')
    cursor = conn.cursor()
    create_places_table(cursor)
    create_songs_table(cursor)
    create_mentions_table(cursor)
    conn.commit()
    conn.close()
