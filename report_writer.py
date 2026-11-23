
import sys
import subprocess
import xml.etree.ElementTree as ET
from pathlib import Path


def write_report(filename):
    test_file = Path("tests") / (
        "test_" + Path(filename).stem + ".py"
    )

    if not test_file.exists():
        raise FileNotFoundError(test_file)

    # Run tests and save real results
    result = subprocess.run(
        [
            sys.executable, "-m", "pytest",
            "-q", str(test_file),
            "--junitxml=test_results.xml"
        ],
        capture_output=True,
        text=True
    )

    print(result.stdout)

    root = ET.parse("test_results.xml").getroot()
    cases = root.findall(".//testcase")

    if not cases:
        raise RuntimeError(
            "No tests collected. Check the pytest output."
        )

    def status(case):
        if case.find("failure") is not None:
            return "FAIL"
        if case.find("error") is not None:
            return "ERROR"
        if case.find("skipped") is not None:
            return "SKIP"
        return "PASS"

    results = [
        (case.attrib.get("name", ""), status(case))
        for case in cases
    ]

    functions = [
        ("is_even", "Beginner", "Incorrect even number check"),
        ("is_adult", "Easy", "Age 18 was excluded"),
        ("discounted_price", "Medium", "Wrong discount calculation"),
        ("unique_in_order", "Hard", "Original order was not preserved"),
        ("moving_averages", "Challenging", "Last window was missing")
    ]

    report = [
        "# Homework Report",
        "",
        "## Objective",
        "The objective was to find, test and fix bugs "
        "in five Python functions.",
        "",
        "## Results",
        "",
        "| Function | Difficulty | Problem Found | Result |",
        "|---|---|---|---|"
    ]

    for name, difficulty, problem in functions:
        matches = [
            state for test, state in results
            if name in test
        ]

        if not matches:
            final = "NOT TESTED"
        elif all(s == "PASS" for s in matches):
            final = "PASS"
        else:
            final = "FAIL / ERROR / SKIP"

        report.append(
            f"| {name} | {difficulty} | {problem} | {final} |"
        )

    passed = sum(s == "PASS" for _, s in results)
    failed = sum(s == "FAIL" for _, s in results)
    errors = sum(s == "ERROR" for _, s in results)
    skipped = sum(s == "SKIP" for _, s in results)

    report += [
        "",
        "## Test Summary",
        f"- Total tests: {len(results)}",
        f"- Passed: {passed}",
        f"- Failed: {failed}",
        f"- Errors: {errors}",
        f"- Skipped: {skipped}",
        "",
        "## Conclusion"
    ]

    if passed == len(results) and result.returncode == 0:
        report.append(
            "All tests passed after the corrections."
        )
    else:
        report.append(
            "Some tests did not pass. Further review is needed."
        )

    Path("RESULTS.md").write_text(
        "\n".join(report) + "\n",
        encoding="utf-8"
    )

    print("Report saved to RESULTS.md")
