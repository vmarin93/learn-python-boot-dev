from incomplete_main import get_buffed_attacks

run_cases = [([50, 60, 70], [100, 120, 140]), ([5, 10, 15, 21], [10, 20, 30, 42])]

submit_cases = run_cases + [
    ([0, 0, 0], [0, 0, 0]),
    ([23684230, 5748823], [47368460, 11497646]),
    ([2.5, 7.3, 6.2], [5, 14.6, 12.4]),
]

test_cases = submit_cases


def test(input, expected_output):
    print("---------------------------------")
    print(f"Input: {input}")
    print(f"Expected: {expected_output}")
    result = get_buffed_attacks(input)
    print(f"Actual:   {result}")
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
