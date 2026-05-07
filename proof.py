import os
from github import Github, Auth
from colorama import Fore, Style, init

init(autoreset=True)

TOKEN = os.environ.get("GITHUB_TOKEN")
REPO_NAME = "alinpm/PRoof"
PR_NUMBER = 1

auth = Auth.Token(TOKEN)
g = Github(auth=auth)
repo = g.get_repo(REPO_NAME)
pr = repo.get_pull(PR_NUMBER)

score = 0
BAD_TITLES = ["fix", "update", "wip", "test", "patch", "changes"]

print("=" * 40)
print(f"PRoof — PR Health Check #{PR_NUMBER}")
print("=" * 40)

if pr.changed_files <= 10:
    print(Fore.GREEN + "✓ Size: OK")
    score += 20
else:
    print(Fore.RED + "✗ Size: Too many files changed")

if pr.body and len(pr.body) >= 10:
    print(Fore.GREEN + "✓ Description: OK")
    score += 20
else:
    print(Fore.RED + "✗ Description: Missing or too short")

if pr.commits <= 10:
    print(Fore.GREEN + "✓ Commits: OK")
    score += 20
else:
    print(Fore.RED + "✗ Commits: Too many commits")

if pr.additions + pr.deletions <= 500:
    print(Fore.GREEN + "✓ Lines changed: OK")
    score += 20
else:
    print(Fore.RED + "✗ Lines changed: Too large")

title = pr.title.lower()
if len(pr.title) >= 10 and not any(word == title for word in BAD_TITLES):
    print(Fore.GREEN + "✓ Title: OK")
    score += 20
else:
    print(Fore.RED + f"✗ Title: Too short or uninformative (avoid: {', '.join(BAD_TITLES)})")

print("=" * 40)
if score >= 75:
    print(Fore.GREEN + f"Score: {score}/100 — Ready for review ✓")
elif score >= 50:
    print(Fore.YELLOW + f"Score: {score}/100 — Needs improvement ⚠")
else:
    print(Fore.RED + f"Score: {score}/100 — Not ready ✗")
print("=" * 40)
print(f"PR: {pr.title}")
print(f"Author: {pr.user.login}")
print("=" * 40)
