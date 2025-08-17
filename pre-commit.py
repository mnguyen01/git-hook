import git
import re

git_branch = git.cmd.Git().execute(["git", "symbolic-ref", "--short", "HEAD"])

search_nxfram = re.search('NXFRAM-\d+',git_branch)

if search_nxfram:
    jira_id = search_nxfram.group(0)
    print(jira_id)

    with open('msg-template.txt', 'r') as file:
        data = file.read()
        data = data.replace('NXFRAM-xxxx', jira_id)
        with open('msg-template.txt', 'w') as file:
            file.write(data)
else:
    print("NXFRAM-xxxx")

