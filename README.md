# SECB3203 Lab 1 - Python fundamentals and a reproducible project

Student: <TAN HUI SHAN, A24CS0197>

## Setup
Windows (PowerShell)

- Create virtual environment: 
python -m venv .venv

- Activate virtual environment (PowerShell): 
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
.\.venv\Scripts\activate

- Install required packages: 
pip install -r requirements.txt

## Run
- Run unit tests: 
python -m pytest

- Run code style linter: 
ruff check src

- Generate environment report output: 
python src/env_check.py > results/environment_report.txt

## What is in this repository
1 src/: Directory containing core Python source code modules.

2 src/env_check.py: Script to inspect system environment, OS platform, and package dependency versions.

3 src/basics.py: Module implementing GC percentage calculation, report formatting, and sequence count parsing logic.

4 tests/: Directory containing all unit test files run via pytest.

5 tests/test_visible.py: Visible test suite provided in starter kit to verify core task functions.

6 tests/test_lab01_own.py: Custom test suite covering boundary cases, zero base totals, and invalid inputs.

7 data/: Folder reserved for input sequence files and raw datasets.

8 results/: Folder reserved for generated script output files and logs.

9 results/environment_report.txt: Captured output recording verified system architecture and installed packages.

10 requirements.txt: Specified package dependencies required to run the project.

11 requirements-frozen.txt: Exact version snapshot of all packages installed in the virtual environment.

12 AI_USE_LOG.md: Log documenting AI tool usage, prompts, verifications, and UTM APA 7th citations.

13 README.md: Project documentation covering setup, execution commands, repository structure, and Git policies.

## What is not committed, and why
We ignore .venv/ and results/ using .gitignore to ensure the repository remains small and portable across different operating systems. Uploading Windows-bound virtual environment files causes errors on Mac or Linux machines where users should instead build a fresh environment using requirements.txt. Besides, tracking dynamic output files clutters commit logs and causes merge conflicts when generated results vary.
