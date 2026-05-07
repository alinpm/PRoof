# PRoof — PR Health Checker

A lightweight Python tool that checks the quality of GitHub pull requests before code review.

## The Problem

Developers often submit pull requests that are too large, poorly described, or have messy commit history. This slows down code review and frustrates the whole team.

## What PRoof checks

- Files changed — more than 10 files is hard to review
- Description — every PR needs context
- Commits — more than 10 commits creates noise
- Lines changed — more than 500 lines takes too long to review
- Title — avoid uninformative names like fix, update, wip

## Score

PRoof gives every PR a score from 0 to 100:

- 75-100 — Ready for review
- 50-74 — Needs improvement
- 0-49 — Not ready

## Installation

pip install PyGithub colorama

## Usage

# PRoof — PR Health Checker

A lightweight Python tool that checks the quality of GitHub pull requests before code review.

## The Problem

Developers often submit pull requests that are too large, poorly described, or have messy commit history. This slows down code review and frustrates the whole team.

## What PRoof checks

- Files changed — more than 10 files is hard to review
- Description — every PR needs context
- Commits — more than 10 commits creates noise
- Lines changed — more than 500 lines takes too long to review
- Title — avoid uninformative names like fix, update, wip

## Score

PRoof gives every PR a score from 0 to 100:

- 75-100 — Ready for review
- 50-74 — Needs improvement
- 0-49 — Not ready

## Installation

pip install PyGithub colorama

## Usage

export GITHUB_TOKEN="your_token"
python3 proof.py owner/repository PR_number

## Example

python3 proof.py alinpm/PRoof 1

## Tech stack

Python, PyGithub, GitHub API, colorama

## Author

Alina Syso — github.com/alinpm
