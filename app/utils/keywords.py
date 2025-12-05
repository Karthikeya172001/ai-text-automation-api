def extract_keywords(text: str):
    words = text.lower().split()
    freq = {}

    for w in words:
        if len(w) > 3:
            freq[w] = freq.get(w, 0) + 1

    sorted_keys = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    return sorted_keys[:5]
