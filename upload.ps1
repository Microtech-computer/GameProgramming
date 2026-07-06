# ============================================
# GITHUB PROJECT UPLOAD SCRIPT (POWERSHELL)
# ============================================
# EDIT THESE VALUES BEFORE RUNNING
# ============================================

$PROJECT_PATH = "C:/GameProgramming"
$GITHUB_USERNAME = "Microtech-computer"
$REPOSITORY_NAME = "GameProgramming"
$COMMIT_MESSAGE = "Initial commit"

# ============================================
# OPEN PROJECT DIRECTORY
# ============================================

cd $PROJECT_PATH

# ============================================
# INITIALIZE GIT
# ============================================

git init

# ============================================
# CREATE .GITIGNORE
# ============================================

@'
node_modules/
.env
dist/
.vscode/
.DS_Store
'@ | Out-File -Encoding utf8 .gitignore

# ============================================
# ADD PROJECT FILES
# ============================================

git add .

# ============================================
# CREATE COMMIT
# ============================================

git commit -m $COMMIT_MESSAGE

# ============================================
# RENAME BRANCH TO MAIN
# ============================================

git branch -M main

# ============================================
# CONNECT TO GITHUB REPOSITORY
# ============================================

git remote remove origin 2>$null

git remote add origin "https://github.com/Microtech-computer/GameProgramming.git"

# ============================================
# PUSH TO GITHUB
# ============================================

git push -u origin main

# ============================================
# FINISHED
# ============================================

Write-Host ""
Write-Host "============================================"
Write-Host "PROJECT SUCCESSFULLY UPLOADED TO GITHUB"
Write-Host "============================================"
Write-Host ""
Write-Host "Repository URL:"
Write-Host "https://github.com/Microtech-computer/GameProgramming.git"
Write-Host ""
