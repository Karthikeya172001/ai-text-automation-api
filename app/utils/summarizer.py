def generate_summary(text: str):
    sentences = [s.strip() for s in text.split(".") if s.strip()]
    
    if len(sentences) <= 2:
        return text  # Not enough to summarize

    mid = len(sentences) // 2
    summary = f"{sentences[0]}. {sentences[mid]}. {sentences[-1]}."
    return summary
