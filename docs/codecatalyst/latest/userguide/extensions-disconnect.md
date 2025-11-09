Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Disconnecting GitHub accounts, Bitbucket workspaces, GitLab users, and Jira sites CodeCatalyst

If you no longer want to use GitHub repositories, Bitbucket repositories, or GitLab project repositories, or manage Jira issues in CodeCatalyst,
you can disconnect your third-party source. Once a GitHub account, Bitbucket workspace, or GitLab user is disconnected, events in the
repositories will not start workflow runs, and you will not be able to use those repositories with CodeCatalyst Dev Environments. When a Jira site is
disconnected, Jira issues from the site's projects will not be available in the CodeCatalyst projects, and CodeCatalyst **Issues**
will be the issue provider again.

###### Note

- To disconnect a GitHub account, you must first unlink all linked GitHub repositories from that account.
- To disconnect a Bitbucket workspace, you must first unlink all linked Bitbucket repositories from that workspace.
- To disconnect a GitLab user, you must first unlink all linked GitLab project repositories from that workspace.
- To disconnect a Jira site, you must first unlink all linked Jira projects from that account.
  For more information, see [Unlinking GitHub repositories, Bitbucket repositories, GitLab project repositories,
  and Jira projects in CodeCatalyst](extensions-unlink.md "extensions-unlink.md").

###### To disconnect a GitHub project, Bitbucket workspace, GitLab user, or Jira site

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
   - **GitHub repositories**: Disonnect to a GitHub account.

   In the **Connected GitHub accounts** tab, choose the GitHub account you want to disconnect, and then
   choose **Disconnect GitHub account**.
   - **Bitbucket repositories**: Disonnect to a Bitbucket workspace.

   In the **Connected Bitbucket workspaces** tab, choose the Bitbucket workspace you want to disconnect, and then
   choose **Disconnect Bitbucket workspace**.
   - **GitLab repositories**: Disonnect to a GitLab user.

   In the **Connected GitLab users** tab, choose the GitLab user you want to disconnect, and then
   choose **Disconnect GitLab user**.
   - **Jira Software**: Disonnect to a Jira site.

   In the **Connected Jira sites** tab, choose the Jira site you want to disconnect, and then
   choose **Disconnect Jira site**.

6. In the **Disconnect** dialog box, review the effects of disconnecting the account.
7. Enter **disconnect** into the text input field, and then choose
   **Disconnect**.
