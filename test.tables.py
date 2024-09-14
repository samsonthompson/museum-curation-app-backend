import
conn = sqlite3.connect('museum_curator.db')
cursor = conn.cursor()


cursor.execute('''
CREATE TABLE IF NOT EXISTS artworks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    api_source TEXT NOT NULL,
    artwork_id TEXT NOT NULL UNIQUE,
    title TEXT NOT NULL,
    artist TEXT,
    date_created DATE,
    medium TEXT,
    dimensions TEXT,
    description TEXT,
    image_url TEXT,
    more_info_url TEXT
);
''')


cursor.execute('''
CREATE TABLE IF NOT EXISTS exhibitions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
''')


cursor.execute('''
CREATE TABLE IF NOT EXISTS exhibition_artworks (
    exhibition_id INTEGER,
    artwork_id INTEGER,
    PRIMARY KEY (exhibition_id, artwork_id),
    FOREIGN KEY (exhibition_id) REFERENCES exhibitions(id),
    FOREIGN KEY (artwork_id) REFERENCES artworks(id)
);
''')


conn.commit()
conn.close()

print("Tables created successfully.")
