# PRoof

> CLI tool to analyze GitHub PRs and score their review-readiness (0–100)

## Why

Large, poorly described, or messy PRs slow down code review.
PRoof checks PR quality before it hits the reviewer's queue.

## What it checks

| Check | Threshold |
|-------|-----------|
| Files changed | ≤ 10 |
| Description | present and meaningful |
| Commits | ≤ 10 |
| Lines changed | ≤ 500 |
| Title | informative, not "fix" / "update" / "wip" |

## Score

| Score | Status |
|-------|--------|
| 75–100 | ✅ Ready for review |
| 50–74 | ⚠️ Needs improvement |
| 0–49 | ❌ Not ready |

## Install

pip install PyGithub colorama

## Usage

export GITHUB_TOKEN="your_token"
python3 proof.py owner/repo PR_number

## Example

python3 proof.py alinpm/PRoof 1

## Stack

Python · PyGithub · GitHub API · colorama
