##
## repo-init.sh
##
export REPO="vaic"
export DESC="Vertex AI Client"
gh repo create $REPO -d "$DESC" --public
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin git@github.com:damonreed/${REPO}.git
git push -u origin main