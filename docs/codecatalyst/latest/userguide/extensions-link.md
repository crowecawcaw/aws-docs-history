Amazon CodeCatalyst will no longer be open to new customers starting on November
7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For
more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Linking GitHub repositories, Bitbucket repositories, GitLab project repositories,

and Jira projects in CodeCatalyst

Before you can use a GitHub repository, Bitbucket repository, or GitLab project repository, or manage a Jira project,
you must connect the third-party source that the repository or project belongs to with your CodeCatalyst space. For more
information, see [Connecting GitHub accounts, Bitbucket workspaces, GitLab users, and Jira sites CodeCatalyst](extensions-connect.md "extensions-connect.md").

You can use linked GitHub repositories, Bitbucket repositories, or GitLab project repositories in workflows, where
events in the linked repositories start workflows that might build, test, or deploy code, depending on the workflow
configuration. Workflow configuration files for workflows that use linked GitHub or Bitbucket repositories are stored in
the linked repositories. Linked repositories can also be used with Dev Environments to create, update, and delete files in the
linked repositories. You can link a GitHub repository, Bitbucket repository, or GitLab project repository to a CodeCatalyst
project from either the details page of the **GitHub repositories**, **Bitbucket repositories**, or **GitLab repositories** extension, or from the **Source
repositories** view in **Code** in the project itself.

###### Important

While you can link a GitHub or Bitbucket repository as a **Contributor**, you can only
unlink a third-party repository as the **Space administrator** or the **Project administrator**.
For more information, see [Unlinking GitHub repositories, Bitbucket repositories, GitLab project repositories,
and Jira projects in CodeCatalyst](extensions-unlink.md "extensions-unlink.md").

###### Important

After you install a repository extension, any repositories you link to CodeCatalyst will have
their code indexed and stored in CodeCatalyst. This will make the code searchable in
CodeCatalyst. To better understand the data protection for your code when using linked
repositories in CodeCatalyst, see [Data protection](data-protection.md "data-protection.md")
in the _Amazon CodeCatalyst User Guide_.

###### Important

CodeCatalyst doesn't support detecting changes in the default branch for linked repositories. To change the
default branch for a linked repository, you must first unlink it from CodeCatalyst, change the default branch, and then
link it again.

As a best practice, always make sure you have the latest version of the extension before you link a repository.

You can use linked Jira projects to manage issues and to link CodeCatalyst pull requests to a Jira issue. Summary status
of a pull request and the status of associated CodeCatalyst workflow events are reflected in your Jira issue.

###### Important

To link your Jira project to your CodeCatalyst project, you must be the CodeCatalyst
**Space administrator** or CodeCatalyst **Project administrator**.

###### Note

- A GitHub repository, Bitbucket repository, or GitLab project repository can only be linked to one CodeCatalyst
  project in a space.
- You can't use empty or archived GitHub repositories, Bitbucket repositories, or GitLab project
  repositories with CodeCatalyst projects.
- You can't link a GitHub repository, Bitbucket repository, or GitLab repository that has the same
  name as a repository in a CodeCatalyst project.
- The **GitHub repositories** extension isn't compatible with GitHub Enterprise Server repositories.
- The **Bitbucket repositories** extension isn't compatible with Bitbucket Data Center repositories.
- The **GitLab repositories** extension isn't compatible with GitLab self-managed project repositories.
- You can't use the **Write description for me** or
  **Summarize comments** features with linked repositories.
  These features are only available in pull requests in CodeCatalyst.
- A CodeCatalyst project can only be linked to one Jira project. A Jira project can be linked to multiple CodeCatalyst
  projects.

###### Topics

- [Linking resources from connected third-party providers](#extensions-link-resources "#extensions-link-resources")
- [Linking a third-party repository to during CodeCatalyst project creation](#extensions-link-repositories-creation "#extensions-link-repositories-creation")

## Linking resources from connected third-party providers

###### To link a GitHub repository, Bitbucket repository, GitLab project repository, or Jira project to a CodeCatalyst project from

the extension details page

1.  Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2.  Navigate to your CodeCatalyst space.
3.  Do one of the following to view a list of the installed extensions for your space space:
    1. Choose **Settings**, and then choose **Installed extensions**.
    2. Choose the **Catalog** icon

    ![The CodeCatalyst catalog icon in the top navigation bar in CodeCatalyst.](images/integrations/marketplace-icon.png)
    in the top menu.

4.  Choose **Configure** for one of the following extensions: **GitHub repositories**, **Bitbucket repositories**, **GitLab repositories**,
    or **Jira Software**.
5.  Do one of the following depending on the third-party extension you chose to configure:
    - **GitHub repositories**: Link a GitHub repository.

          1. In the **Linked GitHub repositories** tab, choose **Link GitHub repository**.
          2. From the **GitHub account** dropdown, choose the GitHub account that contains the repository that you want to link.
          3. From the **GitHub repository** dropdown, choose the repository you want to link to a CodeCatalyst project.


          ###### Tip

          If the name of the repository is greyed out, you can't link that repository because it has already been linked to another project in the space.
          4. (Optional) If you don't see a GitHub repository in the list of repositories, it might not have been configured for repository access in the Amazon CodeCatalyst
           application in GitHub. You can configure which GitHub repositories can be used in CodeCatalyst in the connected account.


          	1. Navigate to your [GitHub](https://github.com/ "https://github.com/") account, choose **Settings**, and then choose **Applications**.
          	2. In the **Installed GitHub Apps** tab, choose **Configure** for the Amazon CodeCatalyst application.
          	3. Do one of the following to configure access of GitHub repositories you want to link in CodeCatalyst:




          		+ To provide access to all current and future repositories, choose **All repositories**.
          		+ To provide access to specific repositories, choose **Only select repositories**, choose the **Select
          		 repositories** dropdown, and then choose a repository you want to allow to link in CodeCatalyst.
          5. From the **CodeCatalyst project** dropdown menu, choose the CodeCatalyst project you want to link the GitHub repository to.
          6. Choose **Link**.

      If you no longer want to use a GitHub repository in CodeCatalyst, you can unlink it from a CodeCatalyst
      project. When a repository is unlinked, events in that repository will not start workflow
      runs, and you will not be able to use that repository with CodeCatalyst Dev Environments. For more information, see
      [Unlinking GitHub repositories, Bitbucket repositories, GitLab project repositories,
      and Jira projects in CodeCatalyst](extensions-unlink.md "extensions-unlink.md").

    - **Bitbucket repositories**: Link a Bitbucket repository.

          1. In the **Linked Bitbucket repositories** tab, choose **Link Bitbucket repository**.
          2. From the **Bitbucket workspace** dropdown, choose the Bitbucket workspace that contains the repository that you want to link.
          3. From the **Bitbucket repository** dropdown, choose the repository you want to link to a CodeCatalyst project.


          ###### Tip

          If the name of the repository is greyed out, you can't link that repository because it has already been linked to another project in the space.
          4. From the **CodeCatalyst project** dropdown menu, choose the CodeCatalyst project you want to link the Bitbucket repository to.
          5. Choose **Link**.

      If you no longer want to use a Bitbucket repository in CodeCatalyst, you can unlink it from a CodeCatalyst
      project. When a repository is unlinked, events in that repository will not start workflow
      runs, and you will not be able to use that repository with CodeCatalyst Dev Environments. For more information, see
      [Unlinking GitHub repositories, Bitbucket repositories, GitLab project repositories,
      and Jira projects in CodeCatalyst](extensions-unlink.md "extensions-unlink.md").

    - **GitLab repositories**: Link a GitLab project repository.

          1. In the **Linked GitLab project repositories** tab, choose **Link GitLab project repository**.
          2. From the **GitLab user** dropdown, choose the GitLab user that contains the project repository that you want to link.
          3. From the **GitLab project repository** dropdown, choose the repository you want to link to a CodeCatalyst project.


          ###### Tip

          If the name of the repository is greyed out, you can't link that repository because it has already been linked to another project in the space.
          4. From the **CodeCatalyst project** dropdown menu, choose the CodeCatalyst project you want to link the GitLab project repository to.
          5. Choose **Link**.

      If you no longer want to use a GitLab project repository in CodeCatalyst, you can unlink it from a CodeCatalyst
      project. When a project repository is unlinked, events in that project repository will not start workflow
      runs, and you will not be able to use that project repository with CodeCatalyst Dev Environments. For more information, see
      [Unlinking GitHub repositories, Bitbucket repositories, GitLab project repositories,
      and Jira projects in CodeCatalyst](extensions-unlink.md "extensions-unlink.md").

    - **Jira Software**: Link a Jira project.

          1. In the **Linked Jira projects** tab, choose **Link Jira project**.
          2. From the **Jira site** dropdown menu, choose the Jira site that contains the project that you want to link.
          3. From the **Jira project** dropdown menu, choose the project you want to link to a CodeCatalyst project.
          4. From the **CodeCatalyst project** dropdown menu, choose the CodeCatalyst project you want to link to a Jira project.
          5. Choose **Link**.

      Once a Jira project is linked to a CodeCatalyst project, access to CodeCatalyst issues is disabled entirely,
      and **Issues** in the CodeCatalyst navigation pane will be replaced with a
      **Jira issues** item that links to the Jira project.

    ![CodeCatalyst issues replaced with linked Jira issues in navigation pane.](images/integrations/jira-issues-nav.png)

    If you no longer want to use a Jira project in CodeCatalyst, you can unlink it from your CodeCatalyst
    project. When a Jira project is unlinked, Jira issues will not be available in the CodeCatalyst
    project, and CodeCatalyst **Issues** will be the issue provider again. For more information,
    see [Unlinking GitHub repositories, Bitbucket repositories, GitLab project repositories,
    and Jira projects in CodeCatalyst](extensions-unlink.md "extensions-unlink.md").

###### To link a GitHub repository, Bitbucket repository, or GitLab project repository to a CodeCatalyst project from the source repositories page in a project

1.  Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2.  Navigate to your CodeCatalyst project.
3.  In the navigation pane, choose **Code**, and then choose **Source repositories**.
4.  Choose **Add repository**, and then choose **Link repository**.
5.  From the **Repository provider** dropdown menu, choose one of the following third-party repository providers:
    **GitHub**, **Bitbucket**, **GitLab**.
6.  Do one of the following depending on the third-party repository provider you chose to link:
    - **GitHub repositories**: Link a GitHub repository.
      1. From the **GitHub account** dropdown menu, choose the GitHub account that contains the repository that you want to link.
      2. From the **GitHub repository** dropdown menu, choose the GitHub repository you want to link your CodeCatalyst project.

      ###### Tip

      If the name of the repository is greyed out, you can't link that repository because it has already been linked to another project in the Amazon CodeCatalyst. 3. (Optional) If you don't see a GitHub repository in the list of repositories, it might not have been configured for repository access in the Amazon CodeCatalyst
      application in GitHub. You can configure which GitHub repositories can be used in CodeCatalyst in the connected account.

          1. Navigate to your [GitHub](https://github.com/ "https://github.com/") account, choose **Settings**, and then choose **Applications**.
          2. In the **Installed GitHub Apps** tab, choose **Configure** for the Amazon CodeCatalyst application.
          3. Do one of the following to configure access of GitHub repositories you want to link in CodeCatalyst:




          	+ To provide access to all current and future repositories, choose **All repositories**.
          	+ To provide access to specific repositories, choose **Only select repositories**, choose the **Select
          	 repositories** dropdown, and then choose a repository you want to allow to link in CodeCatalyst.

    - **Bitbucket repositories**: Link a Bitbucket repository.
      1. From the **Bitbucket workspace** dropdown menu, choose the Bitbucket workspace that contains the repository that you want to link.
      2. From the **Bitbucket repository** dropdown menu, choose the Bitbucket repository you want to link your CodeCatalyst project.

      ###### Tip

      If the name of the repository is greyed out, you can't link that repository because it has already been linked to another project in the Amazon CodeCatalyst.

    - **GitLab repositories**: Link a GitLab project repository.
      1. From the **GitLab user** dropdown menu, choose the GitLab user that contains the project repository that you want to link.
      2. From the **GitLab project repository** dropdown menu, choose the GitLab project repository you want to link your CodeCatalyst project.

      ###### Tip

      If the name of the project repository is greyed out, you can't link that project repository because it has already been linked to another project in
      the Amazon CodeCatalyst.

7.  Choose **Link**.

If you no longer want to use a GitHub repository, Bitbucket repository, or GitLab project repository in CodeCatalyst, you can unlink it from a CodeCatalyst
project. When a repository is unlinked, events in that repository will not start workflow
runs, and you will not be able to use that repository with CodeCatalyst Dev Environments. For more information, see
[Unlinking GitHub repositories, Bitbucket repositories, GitLab project repositories,
and Jira projects in CodeCatalyst](extensions-unlink.md "extensions-unlink.md").

After linking your GitHub repository, Bitbucket repository, or GitLab project repository to your CodeCatalyst project, you can use it in CodeCatalyst
workflows and Dev Environments. You can also use the linked repositories with Amazon Q Developer, blueprints, and more. For more information,
see [Automatically starting a workflow run after third-party repository events](extensions-workflow-repositories.md "extensions-workflow-repositories.md") and [Creating a Dev Environment](devenvironment-create.md "devenvironment-create.md").

After linking your Jira project to your CodeCatalyst project, and linking a pull request, updates from CodeCatalyst are reflected in your Jira project.
For more information about linking pull requests to Jira issues, see
[Linking Jira issues to CodeCatalyst pull requests](link-jira-issues-pull-requests.md "link-jira-issues-pull-requests.md"). For more information on viewing CodeCatalyst events in Jira,
see [Viewing CodeCatalyst events in Jira issues](view-codecatalyst-events-jira.md "view-codecatalyst-events-jira.md").

## Linking a third-party repository to during CodeCatalyst project creation

You can link a GitHub repository, Bitbucket repository, or GitLab project respository to a new CodeCatalyst project when creating
the new CodeCatalyst project. For more information, see [Creating a project with a linked third-party
repository](projects-create.md#projects-create-3p-repo "projects-create.md#projects-create-3p-repo").
