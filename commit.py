import os
import random
import datetime

# Generate a random commit message
commit_messages = ["Random commit", "Another commit", "Daily update", "Automated commit", "Code magic"]
message = random.choice(commit_messages)

# Modify a dummy file
with open("dummy.txt", "a") as file:
    file.write(f"{datetime.datetime.now()}\n")

# Git commands to commit and push
os.system("git add .")
os.system(f'git commit -m "{message}"')
os.system("git push")
