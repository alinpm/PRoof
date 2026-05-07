# PRoof — PR Health Checker

A lightweight Python tool that analyzes GitHub pull requests and checks their quality before code review.

## Problem
Developers often submit pull requests that are too large, poorly described, or have messy commit history — making code review slow and painful.

## Solution
PRoof instantly checks a PR against key quality criteria and gives clear feedback.

## What it checks
- File count — too many files make review hard
- Description — every PR needs context
- Commit count — too many commits create noise
- Lines changed — large PRs take longer to review

## How to use
```bash
export GITHUB_TOKEN="your_token"
python3 proof.py
```

## Tech stack
Python, PyGithub, GitHub API
