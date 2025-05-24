from dotenv import load_dotenv
from google import genai
from rich import print as rprint
from rich.panel import Panel
from rich.console import Console
import os
import subprocess
from utils.git_utils import is_git_repo, has_staged_changes, get_git_diff

load_dotenv()


rprint("🎉 WELCOME TO AUTO COMMIT MESSAGE GENERATOR")

def main():
    if is_git_repo():
        if has_staged_changes():
            diff = get_git_diff()

            with open('./prompts/commit.txt', 'r') as file:
                print("FILE OPENEDE")
                content = file.read()
                final_prompt = content.replace('{git_diff}', diff)
               

                try:
                    

                    client = genai.Client(api_key=os.getenv("GOOGLE_GEMINI_API_KEY"))

                    response = client.models.generate_content(
                        model="gemini-2.0-flash",
                        contents=final_prompt,
                    )

                    print(response.text)





                    print("\n✅ Suggested Commit Message:\n")
                    commit_msg = response.text
                    print(Panel(commit_msg, style="green"))
                    edit_msg = input("Do you want to edit the message? Type Y or N:  ").strip().upper()
                    if edit_msg == "Y":
                        with open("edit_commit.txt", "w") as file:
                            file.write(commit_msg)
                        subprocess.run(["nano", "edit_commit.txt"])
                        with open("edit_commit.txt", "r") as file:
                            commit_msg = file.read().strip()

                    subprocess.run(["git", "commit", "-m", commit_msg])
                    if os.path.exists("edit_commit.txt"):
                        os.remove("edit_commit.txt")

                except Exception as e :
                    print(e)
                



if __name__ == "__main__":
    main()
