Amazon CodeCatalyst will no longer be open to new customers starting on November
7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For
more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Deleting a branch

If you no longer need a branch, you can delete it. For example, if you've merged a branch
with a feature change into the default branch and that feature has been released, you
might want to delete the original feature branch, as the changes are already part of the
default branch. Keeping the number of branches low can help users find the branch that
contains the changes they want to work on. When you delete a branch, copies of that
branch remain in the clones of the repository on local computers until users pull and
synchronize those changes.

###### To delete a branch (console)

1. Navigate to the project where your repository resides.
2. Choose the name of the repository from the list of source repositories for the
   project. Alternatively, in the navigation pane, choose
   **Code**, and then choose **Source
   repositories**.

Choose the repository where you want to delete a branch. 3. On the overview page of the repository, choose the drop-down selector next to
the branch name, and then choose **View all**. 4. Choose the branch that you want to delete and then choose **Delete
branch**.

###### Note

You cannot delete the default branch for a repository. 5. A confirmation dialog box appears. It shows the repository, number of open
pull requests, and number of workflows associated with the branch. 6. To confirm deletion of the branch, type **delete** into the
text box, and then choose **Delete**.
You can also use Git to delete branches. For more information, see [Common Git commands for branches](source-branches-git.md#source-branches-git-table "source-branches-git.md#source-branches-git-table").
