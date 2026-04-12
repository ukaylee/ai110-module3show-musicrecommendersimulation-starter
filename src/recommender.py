from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass
import csv

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """Load songs from a CSV file into a list of typed dictionaries."""
    songs: List[Dict] = []

    with open(csv_path, mode="r", newline="", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            songs.append(
                {
                    "id": int(row["id"]),
                    "title": row["title"],
                    "artist": row["artist"],
                    "genre": row["genre"],
                    "mood": row["mood"],
                    "energy": float(row["energy"]),
                    "tempo_bpm": float(row["tempo_bpm"]),
                    "valence": float(row["valence"]),
                    "danceability": float(row["danceability"]),
                    "acousticness": float(row["acousticness"]),
                }
            )
        print(f"Loaded songs: {len(songs)}")

    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Compute a weighted compatibility score and explanation reasons for one song."""
    score = 0.0
    reasons: List[str] = []

    favorite_genre = str(user_prefs.get("genre", "")).strip().lower()
    favorite_mood = str(user_prefs.get("mood", "")).strip().lower()
    target_energy = float(user_prefs.get("energy", 0.5))
    likes_acoustic = bool(user_prefs.get("likes_acoustic", False))

    song_genre = str(song.get("genre", "")).strip().lower()
    song_mood = str(song.get("mood", "")).strip().lower()
    song_energy = float(song.get("energy", 0.0))
    song_acousticness = float(song.get("acousticness", 0.0))
    song_valence = float(song.get("valence", 0.0))

    if song_genre == favorite_genre and favorite_genre:
        genre_points = 2.0
        score += genre_points
        reasons.append(f"genre match (+{genre_points:.1f})")

    if song_mood == favorite_mood and favorite_mood:
        mood_points = 1.0
        score += mood_points
        reasons.append(f"mood match (+{mood_points:.1f})")

    energy_diff = abs(song_energy - target_energy)
    energy_points = max(0.0, 2.0 * (1.0 - energy_diff))
    score += energy_points
    if energy_points > 0:
        reasons.append(f"energy similarity (+{energy_points:.2f})")

    acoustic_points = song_acousticness if likes_acoustic else (1.0 - song_acousticness)
    acoustic_points = max(0.0, min(1.0, acoustic_points))
    score += acoustic_points
    if acoustic_points > 0:
        reasons.append(f"acoustic preference match (+{acoustic_points:.2f})")

    valence_bonus = max(0.0, min(0.5, song_valence * 0.5))
    score += valence_bonus
    if valence_bonus > 0:
        reasons.append(f"valence bonus (+{valence_bonus:.2f})")

    return score, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Return the top-k highest scoring songs with scores and joined explanations."""
    scored_songs: List[Tuple[Dict, float, str]] = [
        (song, score, "; ".join(reasons))
        for song in songs
        for score, reasons in [score_song(user_prefs, song)]
    ]

    ranked_songs = sorted(scored_songs, key=lambda item: item[1], reverse=True)
    return ranked_songs[:k]
