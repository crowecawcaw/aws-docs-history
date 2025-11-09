Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Viewing CodeCatalyst events in Jira issues

If your CodeCatalyst projects and Jira projects are linked, the summary status of the pull request
and the status of associated CodeCatalyst workflow events are reflected in your Jira issue. For example,
if you close or merge a pull request in CodeCatalyst, the status update is reflected in the Jira issue. CodeCatalyst
workflow CI/CD events related to a CodeCatalyst pull request are synchronized, so a successful workflow
run would be sent to the Jira issue as well.

###### To view CodeCatalyst events in a Jira issue

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. Navigate to your CodeCatalyst project.
3. In the CodeCatalyst navigation pane, choose **Code**, choose **Pull
   requests**, and then choose the pull request with the Jira issue that you want
   to view in your Jira project.
4. In the **Additional info** pane, choose the Jira issue that you want to
   view in your Jira project.
5. From the **Details** pane in the Jira project, choose **pull
   request** listed for **Development** to see details of the pull
   request.
6. (Optional) To see the latest builds, choose the **Builds** tab.
7. (Optional) To see the development status, choose the **Deployments**
   tab.
