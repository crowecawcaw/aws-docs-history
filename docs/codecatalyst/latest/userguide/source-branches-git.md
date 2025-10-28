Amazon CodeCatalyst will no longer be open to new customers starting on November
7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For
more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Git commands for branches

You can use Git to create, manage, and delete branches in the clone of the source
repository you have on your computer (your local repo) or in your Dev Environments, and then
commit and push your changes to your CodeCatalyst source repository (the remote repository).
For example:

Common Git commands for branches| Lists all branches in the local repo with an asterisk
(`*`) displayed next to your current branch. | `git branch` |
| Pulls information about all existing branches in the remote repository to the local repo. | `git fetch` |
| Lists all branches in the local repo and remote tracking branches in the local repo. | `git branch -a` |
| Lists only remote tracking branches in the local repo. | `git branch -r` |
| Creates a branch in the local repo using the specified branch name. This branch will not appear in the remote repository until you commit and push the change. | `git branch `branch-name`` |
| Creates a branch in the local repo using the specified branch name, and then switches to it. | `git checkout -b `branch-name`` |
| Switches to another branch in the local repo using the specified branch name. | `git checkout `other-branch-name`` |
| Pushes a branch from the local repo to the remote repository using the local repo's specified nickname for the remote repository and the specified branch name. Also sets up upstream tracking information for the branch in the local repo. | `git push -u `remote-name` `branch-name`` |
| Merges changes from another branch in the local repo to the current branch in the local repo. | `git merge `from-other-branch-name`` |
| Deletes a branch in the local repo unless it contains work that has not been merged.  | `git branch -d `branch-name`` |
| Deletes a branch in the remote repository using the specified nickname the local repo has for the remote repository and the specified branch name. (Note the use of the colon (`:`).) Alternatively, specify `--delete` as part of the command. | `git push `remote-name` :`branch-name`` `git push `remote-name` --delete `branch-name`` | For more information, see your Git documentation.
