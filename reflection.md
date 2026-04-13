# Profile Comparison Reflection

This reflection compares profile pairs and explains what changed in recommendations and why those shifts make sense.

1. High-Energy Pop vs Low-Energy Pop: Both profiles keep pop/happy, so pop tracks still appear, but low-energy pop shifts toward calmer/acoustic songs like Moonlit Sonata and Spacewalk Thoughts. This makes sense because lowering target energy from 0.9 to 0.2 cuts points for intense tracks and rewards lower-energy songs.

2. Chill Lofi vs High-Energy Lofi: Both profiles keep lofi, so Library Rain/Midnight Coding stay relevant, but high-energy lofi pulls in more energetic non-lofi options near the bottom (like Gym Hero/Electric Sunrise). This makes sense because genre still gives +2.0, but a 0.9 energy target pushes the ranking toward higher-energy songs even if mood/genre fit is weaker.

3. Deep Intense Rock vs Low-Energy Rock: Deep Intense Rock ranks Storm Runner first, while Low-Energy Rock ranks Broken Strings and Shattered Dreams first. This makes sense because the low-energy rock profile asks for sad/low-energy/acoustic preferences, so mood and energy alignment beat pure rock intensity.

4. High-Energy Pop vs Conflict Case (Sad + Very High Energy): The conflict case still returns almost the same high-energy pop leaders (Gym Hero, Sunrise City), but without mood-match bonuses. This makes sense because no songs satisfy both sad mood and very high-energy pop well, so the model prioritizes genre + energy and effectively drops the sad signal.

5. High-Energy Pop vs Out-of-Range Energy: Out-of-range energy (1.4) lowers scores across the board and produces weaker matches overall. This makes sense because every song is far from 1.4, so energy similarity shrinks for all candidates and the ranking depends more on leftover bonuses.

6. Chill Lofi vs Unknown Genre/Mood: Chill Lofi gets strong, coherent lofi recommendations, while Unknown Genre/Mood falls back to generic energy/acoustic matches. This makes sense because unknown labels remove both genre and mood bonuses, so the model cannot personalize around those fields.
