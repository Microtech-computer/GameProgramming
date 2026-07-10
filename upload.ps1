# ============================================
# SMART GITHUB SYNC SCRIPT
# Automatically uploads new files/folders
# ============================================

# -------- SETTINGS --------
$PROJECT_PATH = "C:/GameProgramming"
$GITHUB_USERNAME = "Microtech-computer"
$REPOSITORY_NAME = "GameProgramming"

# Commit message with current date/time
$COMMIT_MESSAGE = "Auto update $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')"

# -------- GO TO PROJECT --------
Set-Location $PROJECT_PATH

# -------- INITIALIZE GIT IF NEEDED --------
if (!(Test-Path ".git")) {
    Write-Host "Initializing Git repository..."
    git init
    git branch -M main
}

# -------- CREATE .GITIGNORE IF IT DOESN'T EXIST --------
if (!(Test-Path ".gitignore")) {

@'
# Node
node_modules/

# Python
__pycache__/
*.pyc

# Virtual environments
venv/
.venv/
env/

# Environment variables
.env

# Build folders
dist/
build/

# IDE
.vscode/
.idea/

# Operating System
.DS_Store
Thumbs.db
'@ | Out-File -Encoding utf8 ".gitignore"

}

# -------- CONNECT REMOTE IF MISSING --------
$REMOTE_EXISTS = git remote

if ($REMOTE_EXISTS -notcontains "origin") {
    git remote add origin "https://github.com/$GITHUB_USERNAME/$REPOSITORY_NAME.git"
}

# -------- STAGE EVERYTHING --------
git add -A

# -------- CHECK IF ANYTHING CHANGED --------
$CHANGES = git status --porcelain

if ($CHANGES) {

    git commit -m $COMMIT_MESSAGE

    git push -u origin main

    Write-Host ""
    Write-Host "====================================="
    Write-Host "UPLOAD COMPLETED SUCCESSFULLY"
    Write-Host "====================================="
    Write-Host "Repository:"
    Write-Host "https://github.com/$GITHUB_USERNAME/$REPOSITORY_NAME"

}
else {

    Write-Host ""
    Write-Host "No changes detected."
    Write-Host "Nothing to upload."

}