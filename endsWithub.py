def solution(text, ending):
    return text.endswith(ending)

fixed_tests_True = (
    ("samurai", "ai"),
    ("ninja", "ja"),
    ("sensei", "i"),
    ("abc", "abc"),
    ("abcabc", "bc"),
    ("fails", "ails"),
)

fixed_tests_False = (
    ("sumo", "omo"),
    ("samurai", "ra"),
    ("abc", "abcd"),
    ("ails", "fails"),
    ("this", "fails"),
    ("spam", "eggs"),
)

for text, ending in fixed_tests_True:
    result = solution(text, ending)
    print(f"{text} ends with {ending}: {result}")

for text, ending in fixed_tests_False:
    result = solution(text, ending)
    print(f"{text} ends with {ending}: {result}")