Amazon CodeCatalyst will no longer be open to new customers starting on November
7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For
more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Viewing a workflow's status

You might want to view the status of a workflow to see if there are any workflow
configuration issues you need to address, or to troubleshoot runs that fail to start. CodeCatalyst
evaluates the workflow status every time you create or update the workflow's underlying
[workflow definition file](workflows-concepts.md#workflows-concepts-workflows-def "workflows-concepts.md#workflows-concepts-workflows-def").

###### Note

You can also view the workflow's _run_ status, which is different
from the workflow status. For more information, see [Viewing workflow run status and details](workflows-view-run.md "workflows-view-run.md").

For a list of possible workflow states, see [Workflow states in CodeCatalyst](workflows-workflow-status.md "workflows-workflow-status.md").

###### To view the status of a workflow

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. Choose your project.
3. In the navigation pane, choose **CI/CD**, and then choose **Workflows**.
4. Choose the name of your workflow. You can filter by the source
   repository or branch name where the workflow is defined, or filter
   by workflow name or status.

The status is displayed with the workflow in the list. 5. (Optional) Choose the name of the workflow, and find the **Workflow
definition** field. It shows the workflow status.
