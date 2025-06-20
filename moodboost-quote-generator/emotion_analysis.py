from textblob import TextBlob


keywords_to_emotions = {
    # Happiness / Joy
    "happy": ["happiness", "joy"],
    "joyful": ["happiness", "joy"],
    "cheerful": ["happiness"],
    "bliss": ["happiness"],
    "ecstatic": ["happiness"],
    "content": ["happiness", "peace"],
    "cheerful": ["happiness"],
    "delighted": ["happiness"],

    # Sadness
    "sad": ["sadness"],
    "unhappy": ["sadness"],
    "depressed": ["sadness", "depression"],
    "lonely": ["sadness", "loneliness"],
    "grief": ["sadness", "grief"],
    "melancholy": ["sadness"],
    "tearful": ["sadness"],

    # Fear / Anxiety
    "afraid": ["fear"],
    "scared": ["fear"],
    "nervous": ["anxiety"],
    "anxious": ["anxiety"],
    "panic": ["fear", "anxiety"],
    "terrified": ["fear"],
    "worried": ["anxiety"],
    "fearful": ["fear"],

    # Anger / Frustration
    "angry": ["anger"],
    "mad": ["anger"],
    "furious": ["anger"],
    "irritated": ["anger"],
    "annoyed": ["anger"],
    "frustrated": ["frustration"],
    "rage": ["anger"],
    "resentment": ["anger"],

    # Surprise
    "surprised": ["surprise"],
    "amazement": ["surprise"],
    "astonished": ["surprise"],

    # Trust / Love
    "love": ["love"],
    "loving": ["love"],
    "caring": ["love"],
    "compassion": ["love"],
    "trust": ["trust"],
    "affectionate": ["love"],

    # Anticipation / Excitement / Hope
    "excited": ["excitement"],
    "eager": ["anticipation", "excitement"],
    "hopeful": ["hope"],
    "optimistic": ["hope"],
    "anticipate": ["anticipation"],

    # Calm / Peace
    "calm": ["calm"],
    "peaceful": ["peace"],
    "relaxed": ["calm"],

    # Confusion
    "confused": ["confusion"],
    "uncertain": ["confusion"],

    # Pride / Guilt / Shame
    "proud": ["pride"],
    "guilty": ["guilt"],
    "ashamed": ["shame"],

    # Boredom / Loneliness
    "bored": ["boredom"],
    "alone": ["loneliness"],

    # Burnout / Stress
    "tired": ["burnout", "fatigue"],
    "burnt": ["burnout"],
    "overwhelmed": ["stress", "anxiety"],
    "stressed": ["stress"],
    "fatigued": ["fatigue"]
}



def detect_emotions(text):
    text_lower = text.lower()
    detected_emotions = set()

    for keyword, emotions in keywords_to_emotions.items():
        if keyword in text_lower:
            detected_emotions.update(emotions)
    
    if not detected_emotions:
        blob = TextBlob(text)
        polarity = blob.sentiment.polarity

    return list(detected_emotions)

        