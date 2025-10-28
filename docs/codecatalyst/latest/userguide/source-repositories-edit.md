Amazon CodeCatalyst will no longer be open to new customers starting on November
7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For
more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Editing the settings for a source

repository

You can manage the settings for your repository, including editing the description of
a repository, choosing the default branch, creating and managing branch rules, and
creating and managing approval rules for pull requests in CodeCatalyst. This can help project
members understand what the repository is used for, and help you enforce best practices
and processes used by the team.

###### Note

You can't edit the name of a source repository.

You can't edit the name, description, or other information for a linked repository
in CodeCatalyst. To modify information about a linked repository, you must edit it in the
provider that hosts the linked repository. For more information, see the
documentation for the service that hosts the linked repository.

###### To edit the settings of a

repository

1. In the CodeCatalyst console, navigate to the project that contains the source
   repository whose settings you want to edit.
2. On the summary page for your project, choose the repository you want from the
   list, and then choose **View repository**. Alternatively, in
   the navigation pane, choose **Code**, and then choose
   **Source repositories**. Choose the name of the repository
   from the list of source repositories for the project.
3. On the overview page for the repository, choose **More**, and
   then choose **Manage settings**.
4. Do one or more of the following:
   - Edit the description of the repository and then choose **Save**.
   - To change the default branch for the repository, in **Default branch**, choose **Edit**.
     For more information, see [Managing the default branch for a
     repository](source-branches-default-branch.md "source-branches-default-branch.md").
   - To add, remove, or change a rule for what project roles have permission to perform certain actions in a branch,
     in **Branch rules**, choose **Edit**.
     For more information, see [Manage allowed actions for a branch with
     branch rules](source-branches-branch-rules.md "source-branches-branch-rules.md").
   - To add, remove, or change an approval rule for merging pull reuqests to a branch, in **Approval rules**,
     choose **Edit**. For more information, see [Managing requirements for merging
     a pull request with approval rules](source-pull-requests-approval-rules.md "source-pull-requests-approval-rules.md").
