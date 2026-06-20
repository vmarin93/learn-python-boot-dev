import io
from contextlib import redirect_stdout

from incomplete_main import display_damage_meter


def run_and_capture(players):
    buffer = io.StringIO()
    with redirect_stdout(buffer):
        display_damage_meter(players)
    return buffer.getvalue()


run_cases = [
    (
        [
            {"name": "Arannis", "dps": 4820},
            {"name": "Calyssa", "dps": 3190},
            {"name": "Borin", "dps": 2750},
        ],
        "1. Arannis - 4820 dps\n2. Calyssa - 3190 dps\n3. Borin - 2750 dps\n",
    ),
    (
        [{"name": "Drathos", "dps": 1200}, {"name": "Krakos", "dps": 800}],
        "1. Drathos - 1200 dps\n2. Krakos - 800 dps\n",
    ),
]

submit_cases = run_cases + [
    (
        [
            {"name": "Lyra", "dps": 9999},
            {"name": "Voss", "dps": 5000},
            {"name": "Eska", "dps": 4200},
            {"name": "Pell", "dps": 100},
        ],
        "1. Lyra - 9999 dps\n2. Voss - 5000 dps\n3. Eska - 4200 dps\n4. Pell - 100 dps\n",
    ),
]

test_cases = submit_cases


def test(input, expected_output):
    print("---------------------------------")
    print(f"Input: {input}")
    print(f"Expected:\n{expected_output}")
    result = run_and_capture(input)
    print(f"Actual:\n{result}")
    if result == expected_output:
        print("Pass")
        return True
    print("Fail")
    return False


def main():
    passed = 0
    failed = 0
    skipped = len(submit_cases) - len(test_cases)
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
        else:
            failed += 1
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    if skipped > 0:
        print(f"{passed} passed, {failed} failed, {skipped} skipped")
    else:
        print(f"{passed} passed, {failed} failed")


main()
