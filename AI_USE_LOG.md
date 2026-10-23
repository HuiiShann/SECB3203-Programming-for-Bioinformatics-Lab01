# AI USE LOG

<!-- SECB3203 prompt log. Policy: PROPOSED - for approval by the SECB3203 course team before circulation to students. Fill in, then run: python tools/check_ai_log.py AI_USE_LOG.md --assessment <key> -->

- Course: SECB3203
- Assessment: Lab 01
- Student name: Tan Hui Shan
- Matric no: A24CS0197
- Group ID: n/a
- AI level: 1
- Tools cited: Google. (2026). Gemini (Version 1.5 / 2.0) [Large language model]. Retrieved 23 October from https://gemini.google.com , 
Anthropic (2026). Claude (Claude Sonnet 5.5). Retrieved 23 October 2026 from https://claude.ai

## Declaration (tick exactly one)

- [ ] NIL RETURN: I did not use any generative AI tool for this assessment.
- [x] I used AI. Every interaction that influenced my work is logged below. The log is true and complete.

## Entry 1

- Date: 23 October 2026, 2:30 PM
- Tool: Anthropic (2026). Claude (Claude Sonnet 5.5). Retrieved 23 October 2026 from https://claude.ai
- Purpose: debug
- Prompt: "I having problem when installing -r requirements.txt. Preparing metadata (pyproject.toml) ... error
    error: subprocess-exited-with-error

    × Preparing metadata (pyproject.toml) did not run successfully."
- Output: Claude diagnosed the failure as 32-bit Python, because pip fell back to building numpy from source (numpy-2.4.4.tar.gz) and Meson reported "cpu family: x86". It told me to confirm with struct.calcsize('P')*8, install 64-bit Python, delete .venv, recreate it and reinstall. 
- Verified by: Ran python -c "import struct; print(struct.calcsize('P')*8)", which printed 64. This showed my Python was already 64-bit, so the 32-bit explanation did not match my system.
- My change: Rejected the 32-bit diagnosis and the advice to install 64-bit Python, because my own check contradicted it. Kept only the suggestion to recreate the venv. 
- Used in: Environment setup (T1). Not used as code in src/ or tests/.

## Entry 2 
- Date: 23 October 2026, 2:45 PM
- Tool: Anthropic (2026). Claude (Claude Sonnet 5.5). Retrieved 23 October 2026 from https://claude.ai
- Purpose: debug
- Prompt: "How if I using python 3.15?"
- Output: Claude explained that using an unreleased or experimental Python version (like Python 3.15) causes pip installation failures because pre-compiled binary wheels (.whl) for packages like numpy and pandas do not yet exist on PyPI, forcing pip into a failed source build. Claude advised uninstalling the existing Python installation and downloading/installing Python 3.14 64-bit directly from https://www.python.org.
- Verified by: Navigated to the official Python downloads page, verified the Windows installer architecture details, and confirmed package support.
- My change: Followed the advice directly: uninstalled the previous Python version, downloaded and installed Python 3.14 64-bit from python.org, recreated .venv, and successfully installed all project dependencies.
- Used in: Environment setup and interpreter configuration (Task 1). Not used directly as code in src/ or tests/.

## Entry 3
- Date: 23 October 2026, 3:10 PM
- Tool: Google. (2026). Gemini (Version 2.0) Accessed 23 October 2026 from https://gemini.google.com
- Purpose: explain
- Prompt: can I replace return None with this line : raise NotImplementedError("TODO: implement package_version")?
- Output: Explained that package_version must explicitly return None when an installed package is missing to satisfy automated grading Criterion R1, whereas NotImplementedError is merely a starter stub meant to be removed. Also clarified that Python handles exceptions via try...except blocks rather than catch statements.
- Verified by: Executed python src/env_check.py and ran python -m pytest to confirm that the single passed test (.FFF) verified src/env_check.py returning None for missing packages without raising unhandled exceptions.
- My change: Retained the try...except importlib.metadata.PackageNotFoundError: block, added import importlib.metadata to resolve the NameError, and returned None as required.
- Used in: src/env_check.py inside function package_version().

## Entry 4
- Date: 23 October 2026, 3:25 PM
- Tool: Google. (2026). Gemini (Version 2.0) Accessed 23 October 2026 from https://gemini.google.com
- Purpose: explain
- Prompt: How should I complete the main execution block to let my code successfully run with the function? Prints the report and exits with code 0.
- Output: Explained how to use the if __name__ == "__main__": guard clause so functions execute directly when called from the command line while remaining importable for pytest, providing the following code snippet:
if __name__ == "__main__":
    report = check_environment()
    print("=== Environment Report ===")
    print(f"Python Version : {report['python']}")
    print(f"Platform       : {report['platform']}")
    print("Packages       :")
    for pkg, ver in report["packages"].items():
        print(f"  {pkg}: {ver}")

    sys.exit(0)
- Verified by: Executed python src/env_check.py directly in the terminal to verify formatted output, and ran python -m pytest to confirm that importing the module did not trigger main block side effects.
- My change: Adopted and implemented the if __name__ == "__main__": block with sys.exit(0) in src/env_check.py to print the environment report cleanly.
- Used in: src/env_check.py main execution block.

## Entry 5
- Date: 23 October 2026, 3:45 PM
- Tool: Google. (2026). Gemini (Version 2.0) Accessed 23 October 2026 from https://gemini.google.com
- Purpose: hint
- Prompt: How to implement gc_percent, format_report, and parse_counts in src/basics.py? What validation checks and formatting should I use?
- Output: Summarized the necessary validation checks (negative values, zero totals, token length verification), the :.1f f-string precision specifier for single-decimal rounding, and using .replace(',', ' ').split() for multi-delimiter string parsing.
- Verified by: Saved src/basics.py and executed python -m pytest in the active environment, confirming all 4 visible test cases passed (....).
- My change: Accepted the suggested architectural structure for guard clauses and implemented the functions directly in Python.
- Used in: src/basics.py inside functions gc_percent(), format_report(), and parse_counts().

## Entry 6
- Date: 23 October 2026, 4:10 PM
- Tool: Google. (2026). Gemini (Version 2.0) Accessed 23 October 2026 from https://gemini.google.com
- Purpose: explain
- Prompt: how do I push this repository to GitHub?
- Output: Provided step-by-step guidance on creating a clean remote GitHub repository, configuring git remote add origin, renaming the default branch to main, and executing git push -u origin main.
- Verified by: Executed the Git CLI commands in VS Code PowerShell, authenticated via GitHub, and refreshed the web interface to verify that all commits and project files uploaded successfully.
- My change: Created the remote repository on GitHub and executed the remote link and push commands in Git.
- Used in: Version control and submission setup (Git repository lifecycle).

