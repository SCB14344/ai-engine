def classify_task(text: str) -> str:
    text = text.lower()
    if "image" in text or "draw" in text:
        return "IMAGE"
    if "video" in text:
        return "VIDEO"
    return "TEXT"