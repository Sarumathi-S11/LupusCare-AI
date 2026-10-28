import re

SYMPTOM_DICTIONARY = {
    "Fatigue": [
        "very tired",
        "feeling tired",
        "feel tired",
        "exhausted",
        "low energy",
        "fatigue",
    ],
    "Joint pain": [
        "joint pain",
        "joints hurt",
        "pain in my joints",
        "aching joints",
    ],
    "Headache": [
        "headache",
        "head hurts",
        "head pain",
    ],
    "Skin rash": [
        "skin rash",
        "rash",
        "skin rashes",
    ],
    "Fever": [
        "fever",
        "high temperature",
    ],
    "Muscle pain": [
        "muscle pain",
        "muscles hurt",
        "muscle aches",
    ],
    "Hair loss": [
        "hair loss",
        "losing hair",
    ],
    "Swelling": [
        "swelling",
        "swollen",
    ],
    "Dizziness": [
        "dizziness",
        "dizzy",
    ],
}


def find_symptoms(text):
    if not isinstance(text, str) or not text.strip():
        return [], []

    text = text.lower()
    found = []
    negated = []

    for symptom, phrases in SYMPTOM_DICTIONARY.items():
        positive = False
        negative = False

        for phrase in phrases:
            pattern = r"(?<!\w)" + re.escape(phrase) + r"(?!\w)"

            for match in re.finditer(pattern, text):
                before = text[max(0, match.start() - 50):match.start()]
                before = re.split(
                    r"[.!?;]|\bbut\b|\bhowever\b",
                    before
                )[-1]

                if re.search(
                    r"\b(no|not|without|never|don't|do not|"
                    r"doesn't|does not|denies|denied)\b"
                    r"(?:\s+\w+){0,4}\s*$",
                    before
                ):
                    negative = True
                else:
                    positive = True

        if positive:
            found.append(symptom)
        elif negative:
            negated.append(symptom)

    return found, negated