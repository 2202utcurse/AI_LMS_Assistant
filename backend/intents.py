def detect_intent(text):
    if "summary" in text or "summarize" in text:
        return "summary"
    elif "important questions" in text or "file" in text:
        return "lms_file"
    else:
        return "doubt"