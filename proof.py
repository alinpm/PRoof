import os
from github import Github, Auth

TOKEN = os.environ.get("GITHUB_TOKEN")
REPO_NAME = "alinpm/PRoof"
PR_NUMBER = 1

auth = Auth.Token(TOKEN)
g = Github(auth=auth)
repo = g.get_repo(REPO_NAME)
pr = repo.get_pull(PR_NUMBER)

print("=" * 40)
print(f"PRoof — анализ PR #{PR_NUMBER}")
print("=" * 40)

if pr.changed_files > 10:
    print("ПЛОХО: Слишком много файлов")
else:
    print("ХОРОШО: Размер нормальный")

if not pr.body or len(pr.body) < 10:
    print("ПЛОХО: Нет описания")
else:
    print("ХОРОШО: Описание есть")

if pr.commits > 10:
    print("ПЛОХО: Слишком много коммитов")
else:
    print("ХОРОШО: Коммитов нормально")

if pr.additions + pr.deletions > 500:
    print("ПЛОХО: Слишком много изменений")
else:
    print("ХОРОШО: Объём изменений нормальный")

print("=" * 40)
print(f"PR: {pr.title}")
print(f"Автор: {pr.user.login}")
print("=" * 40)
