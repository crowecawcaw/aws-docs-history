Amazon CodeCatalyst will no longer be open to new customers starting on November
7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For
more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Viewing the history of changes to a file

You can view the the history of changes to a file in your source repository in the Amazon CodeCatalyst console.
This can help you understand the changes made to the file by various commits to the branch where you choose
to view the history of the file. For example, if you view the history of changes to the `readme.md`
file in the `main` branch of the source repository, you will see a list of commits that included changes
to that file in that branch.

###### Note

You can't view the history of a file in a linked repository in the CodeCatalyst console.

# To view the history of a file in the CodeCatalyst console

1. Navigate to the project where you want to view the history of a file. For more information, see
   [Viewing a source repository](source-repositories-view.md "source-repositories-view.md").
2. Choose the name of the repository from the list of source repositories for the project. Alternatively, in the navigation pane,
   choose **Code**, and then choose **Source repositories**.
3. Choose the repository where you want to view the history of a file. Choose the branch where you want to view the history the file,
   and then choose the file from the list. Choose **View history**.
4. Review the list of commits that included changes to this file in the specified branch. To view the details of the changes included in
   a particular commit, choose the commit message for that commit in the list. The differences between that commit and its parent commit
   are displayed.
5. To review the history of changes to the file in another branch, use the branch selector to change views to that branch, choose the
   file from the file list, and then choose **View history**.

###### Note

You cannot view the history of changes to Git submodules in the CodeCatalyst console. For more information about Git submodules, see the [Git
documentation](https://git-scm.com/book/en/v2/Git-Tools-Submodules "https://git-scm.com/book/en/v2/Git-Tools-Submodules").
