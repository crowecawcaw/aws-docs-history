Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Linking Jira issues to CodeCatalyst pull requests

You can link pull requests that are created in a CodeCatalyst source repository to Jira issues. After linking a Jira issue,
the issue is displayed as a property of the pull request. As a result, pull request events, workflow events, and deployment
events are sent to Jira and added to the Jira issue. Pull requests can be linked to one or more Jira issues. You can
only link pull requests that are in a CodeCatalyst source repository, not those in a third-party repository like GitHub. Before
you can link Jira issues to a pull request, your Jira project must be linked to the CodeCatalyst project. For more information
about linking a Jira project to a CodeCatalyst project, see [Linking GitHub repositories, Bitbucket repositories, GitLab project repositories,
and Jira projects in CodeCatalyst](extensions-link.md "extensions-link.md").

###### Note

You can't create a pull request without a source repository with two branches in your
CodeCatalyst project. For more information on pull requests, see [Working with pull requests in CodeCatalyst](source-pull-requests.md "source-pull-requests.md").

###### To link Jira issues to a CodeCatalyst pull request

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. Navigate to your CodeCatalyst project.
3. In the navigation pane, choose **Code**, and then choose **Pull
   requests**.
4. Choose **Create pull request** to enter the pull request details.
5. From the **Source repository** drop-down menu, choose the source repository
   in which you want to link a pull request.
6. From the **Source branch** drop-down menu, choose the branch that contains
   the changes you want reviewed.
7. From the **Destination branch** drop-down menu, choose the branch where you
   want to merge reviewed changes.
8. In the **Pull request title** text input field, enter the title of your pull
   requests.
9. Choose **Link issues** for the **Jira issues - _optional_**
   field, choose the drop-down, and search the Jira issues you want to add from the linked Jira
   project.
10. Select the Jira issues you want to add to the pull request.
11. Choose **Create** to create the pull request.
    Once you link Jira issues to a CodeCatalyst pull request, a summary of the pull request is
    available. The summary includes workflow runs, linked issues, required reviewers, optional reviewers,
    and the author.

###### Note

**Assignee** and **Created by** information associated
with the Jira issue is not available in CodeCatalyst.

After linking a pull request, the synced CodeCatalyst project and Jira project allow
updates from CodeCatalyst to be reflected in your Jira project. The status of the linked pull
request and any workflow events related to the pull request will show up in the Jira issue
when viewing it in Jira. For more information on viewing CodeCatalyst events in Jira, see [Viewing CodeCatalyst events in Jira issues](view-codecatalyst-events-jira.md "view-codecatalyst-events-jira.md").
