Amazon CodeCatalyst will no longer be open to new customers starting on November
7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For
more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Linking a source repository

When linking a source repository to a project, you can include repositories that have
a CodeCatalyst extension for the service that hosts the repository, if that extension is
installed for your space. Only users with the Space administrator role can install
extensions. Once the extension is installed, you can link to repositories configured for
access by that extension. For more information, see [Installing an extension in a space](install-extension.md "install-extension.md") or
follow [Linking GitHub repositories, Bitbucket repositories, GitLab project repositories,
and Jira projects in CodeCatalyst](extensions-link.md "extensions-link.md").

###### Important

After you install a repository extension, any repositories you link to CodeCatalyst will have
their code indexed and stored in CodeCatalyst. This will make the code searchable in
CodeCatalyst. To better understand the data protection for your code when using linked
repositories in CodeCatalyst, see [Data protection](data-protection.md "data-protection.md")
in the _Amazon CodeCatalyst User Guide_.

You can link a repository to only one project in a space. You cannot link an
archived repository. While you can link an empty repository, you can't use it in
CodeCatalyst until you have initialized it with an initial commit that creates a default
branch. Additionally:

- A GitHub repository, Bitbucket repository, or GitLab project repository can only be linked to one CodeCatalyst
  project in a space.
- You can't use empty or archived GitHub repositories, Bitbucket repositories, or GitLab project
  repositories with CodeCatalyst projects.
- You can't link a GitHub repository, Bitbucket repository, or GitLab project repository that has the
  same name as a repository in a CodeCatalyst project.
- The **GitHub repositories** extension isn't compatible with GitHub Enterprise Server repositories.
- The **Bitbucket repositories** extension isn't compatible with Bitbucket Data Center repositories.
- The **GitLab repositories** extension isn't compatible with GitLab self-managed project repositories.
- You can't use the **Write description for me** or
  **Summarize comments** features with linked repositories.
  These features are only available in pull requests in CodeCatalyst.
  While you can link a GitHub repository, Bitbucket repository, or GitLab project repository as a **Contributor**, you can only
  unlink a third-party repository as the **Space administrator** or the **Project administrator**.
  For more information, see [Unlinking GitHub repositories, Bitbucket repositories, GitLab project repositories,
  and Jira projects in CodeCatalyst](extensions-unlink.md "extensions-unlink.md").

###### Important

CodeCatalyst doesn't support detecting changes in the default branch for linked
repositories. To change the default branch for a linked repository, you must first unlink it
from CodeCatalyst, change the default branch, and then link it again. For more information,
see [Linking GitHub repositories, Bitbucket repositories, GitLab project repositories,
and Jira projects in CodeCatalyst](extensions-link.md "extensions-link.md").

As a best practice, always make sure you have the latest version of the extension
before you link a repository.

###### To link a source repository

1. Navigate to the project where you want to link a repository.

###### Note

Before you can link a repository, a user with the Space administrator role must first install the extension for the provider that
hosts the repository. For more information, see [Installing an extension in a space](install-extension.md "install-extension.md"). 2. In the navigation pane, choose **Code**, and then choose **Source repositories**. 3. Choose **Add repository**, and then choose **Link repository**. 4. From the **Repository provider** dropdown menu, choose one of the following third-party repository providers:
**GitHub** or **Bitbucket**. 5. Do one of the following depending on the third-party repository provider you chose to link:

    * **GitHub repositories**: Link a GitHub repository.



    	1. From the **GitHub account** dropdown menu, choose the GitHub account that contains the repository that you want to link.
    	2. From the **GitHub repository** dropdown menu, choose the GitHub account you want to link your CodeCatalyst project.
    	3. (Optional) If you don't see a GitHub repository in the list of repositories, it might not have been configured for repository access in the Amazon CodeCatalyst
    	 application in GitHub. You can configure which GitHub repositories can be used in CodeCatalyst in the connected account.


    		1. Navigate to your [GitHub](https://github.com/ "https://github.com/") account, choose **Settings**, and then choose **Applications**.
    		2. In the **Installed GitHub Apps** tab, choose **Configure** for the Amazon CodeCatalyst application.
    		3. Do one of the following to configure access of GitHub repositories you want to link in CodeCatalyst:




    			+ To provide access to all current and future repositories, choose **All repositories**.
    			+ To provide access to specific repositories, choose **Only select repositories**, choose the **Select
    			 repositories** dropdown, and then choose a repository you want to allow to link in CodeCatalyst.
    * **Bitbucket repositories**: Link a Bitbucket repository.



    	1. From the **Bitbucket workspace** dropdown menu, choose the Bitbucket workspace that contains the repository that you want to link.
    	2. From the **Bitbucket repository** dropdown menu, choose the Bitbucket repository you want to link your CodeCatalyst project.

###### Tip

If the name of the repository is greyed out, you can't link that repository because it has already been linked to another project in the Amazon CodeCatalyst. 6. Choose **Link**.
If you no longer want to use a GitHub repository, Bitbucket repository, or GitLab project repository in CodeCatalyst,
you can unlink it from a CodeCatalyst project. When a repository is unlinked, events in that repository will not start
workflow runs, and you will not be able to use that repository with CodeCatalyst Dev Environments. For more information, see
[Unlinking GitHub repositories, Bitbucket repositories, GitLab project repositories,
and Jira projects in CodeCatalyst](extensions-unlink.md "extensions-unlink.md").
