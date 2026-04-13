"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from recommender import load_songs, recommend_songs


def print_profile_recommendations(profile_name: str, user_prefs: dict, songs: list) -> None:
    """Run and print top recommendations for a single named profile."""
    recommendations = recommend_songs(user_prefs, songs, k=5)

    print(f"\n=== {profile_name} ===")
    # print(f"Preferences: {user_prefs}\n")

    for idx, rec in enumerate(recommendations, start=1):
        song, score, explanation = rec
        reasons = [part.strip() for part in explanation.split(";") if part.strip()]

        print(f"[{idx}] {song['title']}")
        print(f"  Final score: {score:.2f}")
        print("  Reasons:")
        if reasons:
            for reason in reasons:
                print(f"    - {reason}")
        else:
            print("    - No specific reason provided")
        print()


def main() -> None:
    songs = load_songs("data/songs.csv")

    # Baseline profiles
    profiles = {
        "High-Energy Pop": {
            "genre": "pop",
            "mood": "happy",
            "energy": 0.9,
            "likes_acoustic": False,
        },
        "Low-Energy Pop": {
            "genre": "pop",
            "mood": "happy",
            "energy": 0.2,
            "likes_acoustic": True,
        },
        "Chill Lofi": {
            "genre": "lofi",
            "mood": "calm",
            "energy": 0.2,
            "likes_acoustic": True,
        },
        "Deep Intense Rock": {
            "genre": "rock",
            "mood": "intense",
            "energy": 0.85,
            "likes_acoustic": False,
        },
        "Low-Energy Rock": {
            "genre": "rock",
            "mood": "sad",
            "energy": 0.25,
            "likes_acoustic": True,
        },
        # Adversarial / edge-case profiles (for system evaluation)
        "Conflict Case (Sad + Very High Energy)": {
            "genre": "pop",
            "mood": "sad",
            "energy": 0.9,
            "likes_acoustic": False,
        },
        "Out-of-Range Energy": {
            "genre": "electronic",
            "mood": "happy",
            "energy": 1.4,
            "likes_acoustic": True,
        },
        "Unknown Genre/Mood": {
            "genre": "hyperfolk",
            "mood": "melancholic-ecstatic",
            "energy": 0.5,
            "likes_acoustic": False,
        },
    }

    print("\nTop recommendations by profile")
    for profile_name, user_prefs in profiles.items():
        print_profile_recommendations(profile_name, user_prefs, songs)


if __name__ == "__main__":
    main()
