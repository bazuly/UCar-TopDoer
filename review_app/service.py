from review_app.config import get_settings

settings = get_settings()


def analyze_sentiment(text: str) -> str:
    text = text.lower()
    positive_words = settings.POSITIVE_WORDS
    negative_words = settings.NEGATIVE_WORDS

    if any(word in text for word in positive_words):
        return 'positive'
    elif any(word in text for word in negative_words):
        return 'negative'
    return 'neutral'
