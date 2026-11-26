"""Lithuanian Language Toolkit."""

import random

CASES = (
    "vardininkas",
    "kilmininkas",
    "naudininkas",
    "galininkas",
    "inagininkas",
    "vietininkas",
    "sauksmininkas",
)

NOUNS = {
    "namas": {
        "singular": (
            "namas", "namo", "namui", "namą",
            "namu", "name", "name"
        ),
        "plural": (
            "namai", "namų", "namams", "namus",
            "namais", "namuose", "namai"
        ),
    },
    "mokykla": {
        "singular": (
            "mokykla", "mokyklos", "mokyklai",
            "mokyklą", "mokykla", "mokykloje", "mokykla"
        ),
        "plural": (
            "mokyklos", "mokyklų", "mokykloms",
            "mokyklas", "mokyklomis", "mokyklose", "mokyklos"
        ),
    },
    "miestas": {
        "singular": (
            "miestas", "miesto", "miestui",
            "miestą", "miestu", "mieste", "mieste"
        ),
        "plural": (
            "miestai", "miestų", "miestams",
            "miestus", "miestais", "miestuose", "miestai"
        ),
    },
}


def decline(word, case, number="singular"):
    """Return a supported Lithuanian noun form."""
    return NOUNS[word][number][CASES.index(case)]


def generate_exercise():
    """Generate a Lithuanian grammar exercise."""
    word = random.choice(list(NOUNS))
    case = random.choice(CASES)
    number = random.choice(("singular", "plural"))

    return {
        "word": word,
        "case": case,
        "number": number,
        "answer": decline(word, case, number),
    }


if __name__ == "__main__":
    print(generate_exercise())
