def apply_style(text: str, style: str) -> str:
    if style == 'formal':
        return text + " (Formal style)"
    elif style == 'informal':
        return text + " (Informal style)"
    elif style == 'technical':
        return text + " (Technical style)"
    else:
        return text
