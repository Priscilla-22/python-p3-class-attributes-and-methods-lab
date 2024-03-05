class Song:
    count = 0
    artists = []
    genres = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        Song.add_song_to_count()
        self.artist = artist
        Song.add_to_artists(artist)
        self.genre = genre
        Song.add_to_genres(genre)
        Song.add_to_artist_count(artist)
        Song.add_to_genre_count(genre)

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)
            cls.genre_count[genre] = 0

    @classmethod
    def add_to_artists(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)
            cls.artist_count[artist] = 0

    @classmethod
    def add_to_genre_count(cls, genre):
        if genre not in cls.genre_count:
            cls.genre_count[genre] = 1
        else:
            cls.genre_count[genre] += 1

    @classmethod
    def add_to_artist_count(cls, artist):
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1


song1 = Song("Song 1", "Jay-Z", "Rap")
song2 = Song("Song 2", "Drake", "Rap")

print(Song.count)
print(Song.artists)
print(Song.genres)
print(Song.genre_count)
print(Song.artist_count)
