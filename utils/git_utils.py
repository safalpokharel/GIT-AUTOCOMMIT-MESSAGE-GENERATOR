import subprocess
from rich import print as rprint
from rich.panel import Panel
from rich.console import Console
def is_git_repo():
    try:
        response = subprocess.run(["git", "rev-parse", "--is-inside-work-tree"], capture_output=True, text=True)
        if response.returncode == 0 and response.stdout.strip() == "true":
            return True
        else:
            print('❌ Not a Git repository. Please navigate into a Git repo and try again.')
            return False
    except Exception as e:
        print(e)


def has_staged_changes():
    try:
        result = subprocess.run(["git", "diff", "--cached"], capture_output=True, text=True)
        if not result.stdout.strip():
            print('⚠️ No staged changes found. Please stage your changes using: git add <file> and try again.')
            return False
        return True
    except Exception as e:
        print(e)


def get_git_diff():
    try:
        diff = subprocess.run(["git", "diff", "--cached"], capture_output=True, text=True)
        return diff.stdout
    except Exception as e:
        print(e)
