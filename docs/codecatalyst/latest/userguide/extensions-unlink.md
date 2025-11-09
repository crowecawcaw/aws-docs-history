Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Unlinking GitHub repositories, Bitbucket repositories, GitLab project repositories,

and Jira projects in CodeCatalyst

If you no longer want to use a GitHub repository, Bitbucket repository, or GitLab project repository, or manage a
Jira project in CodeCatalyst, you can unlink the repository or project from your CodeCatalyst project.

Unlinking a GitHub repository, Bitbucket repository, or GitLab project repository doesn't delete the repository or make any
changes to it. It doesn't delete any workflow configuration files stored in that linked repository. However, once you unlink a
GitHub repository, Bitbucket repository, or GitLab project repository, events in that repository will no longer start workflow runs,
and you can't use the repository with Dev Environments. You can unlink a GitHub repository, Bitbucket repository, or GitLab project
repository from a CodeCatalyst project from either the details page of the **GitHub repositories**, **Bitbucket repositories**, or **GitLab repositories** extension, or from the
**Source repositories** view in **Code** in the project itself.

Unlinking a Jira project doesn't delete the project, including planning items or development information, or make any changes
to it. However, once you unlink a Jira project, the project's Jira issues will no longer be available to link to the CodeCatalyst project,
and CodeCatalyst **Issues** will be the issue provider again.

###### Important

To unlink your GitHub repository, Bitbucket repository, or Gitlab project repository from your CodeCatalyst project, you
must be the **Space administrator** or the **Project administrator**.

###### To unlink a GitHub repository, Bitbucket repository, GitLab project repository, or Jira project in a CodeCatalyst project from the

extension details page

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. Navigate to your CodeCatalyst space.
3. Do one of the following to view a list of the installed extensions for your space:
   1. Choose **Settings**, and then choose **Installed extensions**.
   2. Choose the **Catalog** icon

   ![The CodeCatalyst catalog icon in the top navigation bar in CodeCatalyst.](images/integrations/marketplace-icon.png)
   in the top menu.

4. Choose **Configure** for one of the following extensions you want to configure: **GitHub repositories**, **Bitbucket repositories**,
   **GitLab repositories**, or **Jira Software**.
5. Do one of the following depending on the third-party extension you chose to configure:
   - **GitHub repositories**: Unlink a GitHub repository.

   In the **GitHub repositories** tab, choose the GitHub repository you want to unlink, and then
   choose **Unlink GitHub repository**.
   - **Bitbucket repositories**: Unlink a Bitbucket repository.

   In the **Bitbucket repositories** tab, choose the Bitbucket repository you want to unlink, and then
   choose **Unlink Bitbucket repository**.
   - **GitLab repositories**: Unlink a GitLab project repository.

   In the **GitLab project repositories** tab, choose the GitLab project repository you want to unlink, and then
   choose **Unlink GitLab project repository**.
   - **Jira Software**: Unlink a Jira project.

   In the **Jira projects** tab, choose the Jira project you want to unlink, and then
   choose **Unlink Jira project**.

6. In the **Unlink** dialog box, review the effects of unlinking the repository.
7. Enter **unlink** into the text input field and choose
   **Unlink**.

###### To unlink a GitHub repository, Bitbucket repository, or GitLab project repository in a CodeCatalyst project from the source repositories page

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. Navigate to your CodeCatalyst project.
3. In the navigation pane, choose **Code**, and then choose **Source repositories**.
4. Choose the radio button of the repository you want to unlink, and then choose **Unlink repository**.
5. Review the information in the dialog box. Follow the instructions, and then choose **Unlink** to unlink the
   repository.
