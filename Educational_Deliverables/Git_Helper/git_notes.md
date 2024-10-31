Keep commits short and frequent

Frequent fetches or pulls

# CLI:

#Make a folder a git repository
git init

#We get up to date on what the remote repository looks like without affecting our actual working directory
git fetch

#Get up to date with main
git pull

#Add specific file to stage (stage a specific file)
git add filename.txt

#Add all files that changed to stage (stage all the changed files)
git add .

#Commit
git commit -m "Stefano 09/10/2024: Changes made"

#Full log of commits
git log

#Log of commits formatted in "oneline"
git log --oneline

#Log of all commits (even ones the were resetted)
git reflog

#Changes the version of all updates
git reset --hard [commit id]

#Surgically remove the changes made in a commit (while still keeping the future and previous changes)
git revert [commit id]

#Opposite of revert, will add the changes made in a commit
git cherry-pick [commit id]

#Create a branch
git branch [branch name]

#Puts you on branch
git switch [branch name]

#While working on a branch, this can put our local version on the main branch, so we "pause" the branch we were working on
git switch main

#Show the repository structure nicely
git log --all --decorate --oneline --graph

#Merge the branch onto the main (type it from the main branch)
git merge [branch name]

#Merge main onto the branch we're working on
git merge main

#Any changes made after the last pull/fetch to the branch will be added on top of the branches commits. This means
#the branch is "becoming" the main and it's adding any changes on top of it. (same result as merge but it doesn't
#use a commit, it just gives a linear history of the changes)
git rebase [branch name]

#To resolve merge conflicts
Open the file with the conflict, git will show everything

#Pushes your branch commits to the server so the branch is visible to everybody
git push origing HEAD:[branch name]

#If I need to do a commit, but what I'm working on isn't ready yet. I can stash the changes that are staged. (So I don't include them in the commit)
git stash

#Bring back to stage the changes made (maybe after the commit has happend)
git stash pop

#Bring all commits to remote repository. (Done after the merge(merge is local))
git push origin
