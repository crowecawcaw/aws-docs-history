Amazon CodeCatalyst will no longer be open to new customers starting on November
7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For
more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Understanding

changes in source code with commits in Amazon CodeCatalyst

Commits are snapshots of the contents and changes to the contents of your repository.
Every time a user commits and pushes a change to a branch, that information is saved. Git
commit information includes the commit author, the person who committed the change, the date
and time, and the changes made. Similar information is automatically included when you
create or edit a file in the Amazon CodeCatalyst console, but the author name is your CodeCatalyst user
name. You can also add Git tags to commits to help you identify specific commits.

In Amazon CodeCatalyst, you can:

- View a list of commits for a branch.
- View individual commits, including the changes made in a commit when compared to its parent or
  parents.
  You can also view files and folders. For more information, see [Managing
  source code files in Amazon CodeCatalyst](source-files.md "source-files.md").

###### Topics

- [Viewing commits to a branch](#source-commits-view "#source-commits-view")
- [Changing how commits are displayed (CodeCatalyst
  console)](#source-commits-settings "#source-commits-settings")

## Viewing commits to a branch

You can view the history of changes made to a branch by reviewing the branch's commits
in the CodeCatalyst console. This helps you understand who made changes to the branch and
when. You can also review the changes made in a specific commit.

###### Tip

You can also view the history of commits that made changes to a specific file. For
more information see [Viewing a file](source-files-view-history.md "source-files-view-history.md").

You can also view commits by using your Git client. For more information, see your Git
documentation.

###### To view commits (console)

1. Navigate to the project that contains the source repository where you want to
   view commits.
2. Choose the name of the repository from the list of source repositories for the
   project. Alternatively, in the navigation pane, choose
   **Code**, and then choose **Source
   repositories**.

Choose the repository where you want to view commits to a branch. 3. The default branch of the repository is displayed, including information about
the most recent commit to the branch. Choose **Commits**.
Alternatively, choose **More**, and then choose **View
commits**. 4. To view commits for a different branch, choose the branch selector, and then
choose the name of the branch. 5. To view details about a particular commit, choose its title from
**Commit
title**.
Details of the commit are displayed, including information about its parent
commit and the changes made to the code by comparing the parent commit to the
specified commit.

###### Tip

If a commit has more than one parent, you can choose which parent commit
to view information and display changes for by choosing the drop-down icon
next to the parent commit ID.

## Changing how commits are displayed (CodeCatalyst

console)

You can change what information is displayed in the **Commits** view. You can choose to hide or display columns
such as author and commit ID.

###### To change how commits are displayed

(console)

1. Navigate to the project that contains the source repository where you want to
   view commits.
2. Choose the name of the repository from the list of source repositories for the
   project. Alternatively, in the navigation pane, choose
   **Code**, and then choose **Source
   repositories**.

Choose the repository where you want to change how you view commits. 3. The default branch of the repository is displayed, including information about
the most recent commit to the branch. Choose
**Commits**. 4. Choose the gear icon. 5. In **Preferences**, choose the number of commits to display,
and choose whether to display information about commit author, commit date, and
the commit ID.

###### Note

You can't hide the commit title in the display of information. 6. When you have made your changes, choose **Save** to save
them, or **Cancel** to discard them.
