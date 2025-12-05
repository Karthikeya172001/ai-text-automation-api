def remove_duplicate_lines(text: str):
    lines = [line.strip() for line in text.split("\n") if line.strip()]
    clean = list(dict.fromkeys(lines))
    return "\n".join(clean)

def remove_duplicate_paragraphs(text: str):
    paragraphs = [p.strip() for p in text.split("\n\n") if p.strip()]
    clean = list(dict.fromkeys(paragraphs))
    return "\n\n".join(clean)
