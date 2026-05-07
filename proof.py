import os
from github import Github, Auth

TOKEN = os.environ.get("GITHUB_TOKEN")

REPO_NAME = "pypa/pip"
PR_NUMBER = 3

auth = Auth.Token(TOKEN)
g = Github(auth=auth)
repo = g.get_repo(REPO_NAME)
pr = repo.get_pull(PR_NUMBER)

print(f"PR: {pr.title}")
print(f"Автор: {pr.user.login}")
print(f"Изменённых файлов: {pr.changed_files}")
print(f"Добавлено строк: {pr.additions}")
print(f"Удалено строк: {pr.deletions}")
print(f"Коммитов: {pr.commits}")
import os
from github import Github, Auth

TOKEN = os.environ.get("GITHUB_TOKEN")

REPO_NAME = "pypa/pip"
PR_NUMBER = 1

auth = Auth.Token(TOKEN)
g = Github(auth=auth)
repo = g.get_repo(REPO_NAME)
pr = repo.get_pull(PR_NUMBER)

print(f"PR: {pr.title}")
print(f"Автор: {pr.user.login}")
print(f"Изменённых файлов: {pr.changed_files}")
print(f"Добавлено строк: {pr.additions}")
print(f"Удалено строк: {pr.deletions}")
print(f"Коммитов: {pr.commits}")
print(f"Описание: {pr.body}")
