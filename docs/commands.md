git add .        → stage changes
git commit -m    → save snapshot
git push         → upload to GitHub
git status       → check changes

Basic LINUX
pwd        → show current folder
ls         → list files
ls -l      → detailed list
cd folder  → move into folder
cd ..      → go back one folder
mkdir name → create folder
touch file → create empty file

FILE OPERATION
cat file        → view file content
nano file       → edit file
rm file         → delete file
rm -r folder    → delete folder
cp a b          → copy file
mv a b          → rename/move

PYTHON BASIC (SCRIPTS)
python3 file.py     → run python script
python3 --version   → check python version

GIT BASIC FLOW
git status          → check changes
git add .           → stage everything
git commit -m "msg" → save snapshot
git push            → send to GitHub
git pull            → get updates from GitHub

GIT SETUP
git config --global user.name "Your Name"
git config --global user.email "you@email.com"

REPO CONNECTION (one time per project)
git init
git remote add origin <repo-url>
git branch -M main
git push -u origin main

NETSHIELD PROJECT FLOW 
cd ~/netshield-phase1
python3 scripts/system_info.py
git status
git add .
git commit -m "update"
git push

DEBUGGING
history        → shows previous commands
clear          → clear terminal
which python3  → locate python

IMPORTANT PATTERN (MEMORIZE)
EDIT → RUN → CHECK → COMMIT → PUSH

PRO TIP (IMPORTANT)
git add .
git commit -m "update commands cheat sheet"
git push

