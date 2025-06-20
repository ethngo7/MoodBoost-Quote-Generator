import json
import random

# Load quotes from JSON file
def load_quotes(filepath="quotes.json"):
    with open(filepath, "r") as f:
        return json.load(f)

# Get quotes based on emotion tags
def get_quotes_for_emotions(emotions, num_quotes=3):
    quotes = load_quotes()
    matching_quotes = []

    for quote in quotes:
        # Check for any overlap between emotion tags and quote tags
        if any(tag in quote["tags"] for tag in emotions):
            matching_quotes.append(quote["quote"])

    # Shuffle to keep variety
    random.shuffle(matching_quotes)

    # Fallback if no matches found
    if not matching_quotes:
        return ["I'm still learning how to help with that feeling, but know this: you're not alone. ❤️"]

    return matching_quotes[:num_quotes]
