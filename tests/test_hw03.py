from main import group_anagrams, _signature, _clean_letters

# ---- Normal tests (4) ----

def test_clean_letters_basic():
    assert _clean_letters("Spam!") == "spam"
    assert _clean_letters("E-ggs") == "eggs"

def test_signature_sorted_lowercase():
    assert _signature("Listen") == _signature("Silent") == "eilnst"

def test_group_anagrams_basic_order_preserved():
    words = ["Tea", "Eat", "ate", "now"]
    g = group_anagrams(words)
    assert g["aet"] == ["Tea", "Eat", "ate"]
    assert g["now"] == ["now"]

def test_empty_input_returns_empty_dict():
    assert group_anagrams([]) == {}

# ---- Edge-case tests (3) ----

def test_non_letters_ignored_in_signature():
    # Fixed expectations
    assert _signature("a-b!a") == "aab"  # 2 a's, 1 b
    assert _signature("a!a!a") == "aaa"  # 3 a's

def test_single_char_words():
    g = group_anagrams(["A", "b", "B", "a"])
    assert g["a"] == ["A", "a"]
    assert g["b"] == ["b", "B"]

def test_duplicate_words_kept_in_order():
    g = group_anagrams(["eat", "eat", "tea"])
    assert g["aet"] == ["eat", "eat", "tea"]

# ---- More-complex tests (3) ----

def test_many_words_multiple_groups():
    words = ["dusty","study","rat","tar","art","evil","vile","veil","live"]
    g = group_anagrams(words)
    # Fixed keys
    assert set(g["dstuy"]) == {"dusty","study"}
    assert set(g["art"]) == {"rat","tar","art"}
    assert set(g["eilv"]) == {"evil","vile","veil","live"}

def test_case_and_punctuation_mixed():
    words = ["New!", "Wen", "enw", "w!e!n"]
    assert list(group_anagrams(words).values())[0] == ["New!", "Wen", "enw", "w!e!n"]

def test_large_but_deterministic():
    base = ["abc","bca","cab","xyz","zyx","hello","ohlle"]
    words = base * 10
    g = group_anagrams(words)
    assert len(g["abc"]) == 30
    assert len(g["xyz"]) == 20
    assert len(g["ehllo"]) == 20
