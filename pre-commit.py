# import git
import re
import subprocess

git_branch = subprocess.check_output(["git", "symbolic-ref", "--short", "HEAD"], text=True).strip()
print(git_branch)

# git_branch = git.cmd.Git().execute(["git", "symbolic-ref", "--short", "HEAD"])

search_nxfram = re.search('NXFRAM-\d+',git_branch)

if search_nxfram:
    jira_id = search_nxfram.group(0)


    with open('.git/hooks/prepare-commit-msg', 'r') as file:
        data = file.read()

        data = re.sub(r'NXFRAM-.*', jira_id, data)
        with open('.git/hooks/prepare-commit-msg', 'w') as file:
            file.write(data)
else:
    print("No NXFRAM-xxxx found in branch name. Please use a valid branch name that includes NXFRAM-xxxx format.")
    print("Exiting pre-commit hook.")
    exit(1)

