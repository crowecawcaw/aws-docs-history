Amazon CodeCatalyst will no longer be open to new customers starting on November
7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For
more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Viewing third-party repositories and searching Jira issues in CodeCatalyst

After linking GitHub repositories, Bitbucket repositories, or GitLab project repositories, you can view them in
CodeCatalyst to confirm and configure the resources. You can also search for linked Jira issues in CodeCatalyst.

###### Topics

- [Viewing third-party repositories in CodeCatalyst](#extensions-view-repositories "#extensions-view-repositories")
- [Searching Jira issues in CodeCatalyst](#extensions-search-issues "#extensions-search-issues")

## Viewing third-party repositories in CodeCatalyst

You can view the linked GitHub repositories, Bitbucket repositories, or GitLab project repositories
in the list of source repositories for your project or from the **GitHub repositories**, **Bitbucket repositories**, or **GitLab repositories** extension details page.
Choosing them from the list of repositories doesn't open them in CodeCatalyst. Instead, they open in the
third-party repository provider, where you can view and work on the code in the linked repository.

###### To view linked GitHub repositories, Bitbucket repositories, or GitLab project repositories in CodeCatalyst

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. Navigate to your CodeCatalyst project.
3. In the navigation pane, choose **Code**, and then choose **Source
   repositories**.

###### To view linked GitHub repositories, Bitbucket repositories, or GitLab project repositories from the

extension details page

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. Navigate to your CodeCatalyst space, and then choose the **Installed extensions** tab.
3. Depending on the third-party repositories you want to view, do one of the following:
   - In **GitHub repositories**, choose **Configure**, and then choose **Linked GitHub repositories**
     to view all GitHub repositories connected to CodeCatalyst projects in your CodeCatalyst space.
   - In **Bitbucket repositories**, choose **Configure**, and then choose **Linked Bitbucket repositories**
     to view all Bitbucket repositories connected to CodeCatalyst projects in your CodeCatalyst space.
   - In **GitLab repositories**, choose **Configure**, and then choose **Linked GitLab project repositories**
     to view all GitLab project repositories connected to CodeCatalyst projects in your CodeCatalyst space.

The GitHub repositories, Bitbucket repositories, or GitLab project repositories that are linked to your CodeCatalyst project are
shown in the list. Choose the GitHub repository, Bitbucket repository, or GitLab project repository to view and edit files in
the third-party repository provider.

###### Note

If a workflow uses a GitHub repository, Bitbucket repository, or GitLab project repository in a source action, changes you make to the
workflow YAML in the visual editor or the YAML editor in CodeCatalyst will be automatically committed and pushed to the third-party repository.

## Searching Jira issues in CodeCatalyst

After linking a Jira project, you can search the linked Jira project for issues using the
CodeCatalyst global search bar. You can also search for Jira issues in CodeCatalyst while linking to the
issues from a pull request. For more information about linking Jira issues to a CodeCatalyst pull
request, see [Linking Jira issues to CodeCatalyst pull requests](link-jira-issues-pull-requests.md "link-jira-issues-pull-requests.md").

###### To search for Jira issues in linked Jira projects

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. Navigate to your CodeCatalyst project.
3. In the global search bar, search a linked Jira project for issues or Jira issues you want
   to link to a pull request.
