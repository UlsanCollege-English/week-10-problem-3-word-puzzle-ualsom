# main.py

def _clean_letters(s):
    """Return lowercase letters from s (a-z)."""
    return "".join(c.lower() for c in s if c.isalpha())

def _signature(s):
    """Return sorted lowercase-letter signature for s, counting duplicates."""
    letters = _clean_letters(s)
    return "".join(sorted(letters))

def group_anagrams(words):
    """Return dict: signature -> list of original words in input order."""
    result = {}
    for word in words:
        key = _signature(word)
        if key not in result:
            result[key] = []
        result[key].append(word)
    return result

if __name__ == "__main__":
    # Optional manual check
    words = ["dusty","study","rat","tar","art","evil","vile","veil","live"]
    print(group_anagrams(words))
