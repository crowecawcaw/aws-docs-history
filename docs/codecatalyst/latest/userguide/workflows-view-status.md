

Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md).

# Viewing a workflow's status
<a name="workflows-view-status"></a>

You might want to view the status of a workflow to see if there are any workflow configuration issues you need to address, or to troubleshoot runs that fail to start. CodeCatalyst evaluates the workflow status every time you create or update the workflow's underlying [workflow definition file](workflows-concepts.md#workflows-concepts-workflows-def). 

**Note**  
You can also view the workflow's *run* status, which is different from the workflow status. For more information, see [Viewing workflow run status and details](workflows-view-run.md).

For a list of possible workflow states, see [Workflow states in CodeCatalyst](workflows-workflow-status.md).

**To view the status of a workflow**

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/).

1. Choose your project.

1. In the navigation pane, choose **CI/CD**, and then choose **Workflows**.

1. Choose the name of your workflow. You can filter by the source repository or branch name where the workflow is defined, or filter by workflow name or status.

   The status is displayed with the workflow in the list.

1. (Optional) Choose the name of the workflow, and find the **Workflow definition** field. It shows the workflow status.