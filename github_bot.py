import os
import github3
from dotenv import load_dotenv
from reviewer import analyze_code_with_ai

load_dotenv()

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
REPO_NAME = os.getenv("GITHUB_REPO")  
PR_NUMBER = int(os.getenv("PR_NUMBER"))

def fetch_pr_files():
    gh = github3.login(token=GITHUB_TOKEN)
    repo = gh.repository(*REPO_NAME.split("/"))
    pr = repo.pull_request(PR_NUMBER)

    files = [f.filename for f in pr.files()]
    return files

def fetch_pr_file_content(file_path):
    gh = github3.login(token=GITHUB_TOKEN)
    repo = gh.repository(*REPO_NAME.split("/"))
    pr = repo.pull_request(PR_NUMBER)

    for file in pr.files():
        if file.filename == file_path:
            return file.patch, file 

    return None, None

def comment_on_pr(file_path, code_snippet, file_obj):
    suggestion = analyze_code_with_ai(code_snippet)

    gh = github3.login(token=GITHUB_TOKEN)
    repo = gh.repository(*REPO_NAME.split("/"))
    pr = repo.pull_request(PR_NUMBER)

    
    commit_id = pr.head.sha
    position = file_obj.patch.count("\n")

    comment = f"🚀 AI Code Review Suggestion for `{file_path}`:\n\n{suggestion}"


    pr.create_review_comment(comment, commit_id, file_path, position)

if __name__ == "__main__":
    pr_files = fetch_pr_files()
    for file in pr_files:
        code_snippet, file_obj = fetch_pr_file_content(file)
        if code_snippet and file_obj:
            comment_on_pr(file, code_snippet, file_obj)
            print(f"✅ AI Review posted for {file}")

