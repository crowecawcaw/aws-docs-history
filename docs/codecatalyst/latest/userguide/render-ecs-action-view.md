

Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md).

# Viewing the updated task definition file
<a name="render-ecs-action-view"></a>

You can view the name and contents of the updated task definition file.

**To view the name of the updated task definition file, after the **Render Amazon ECS task definition** action has processed it.**

1. Find the run that includes a completed render action:

   1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/).

   1. Choose your project.

   1. In the navigation pane, choose **CI/CD**, and then choose **Workflows**.

   1. Choose the name of your workflow. You can filter by the source repository or branch name where the workflow is defined, or filter by workflow name or status.

   1. Choose a run that includes the completed render action.

1. In the workflow diagram, choose the render action.

1. Choose **Outputs**.

1. Choose **Variables**.

1. The task definition file name is displayed. It looks similar to `task-definition--259-0a2r7gxlTF5X-.json`.

**To view the contents of the updated task definition file**

1. Find the run that includes a completed render action:

   1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/).

   1. Choose your project.

   1. In the navigation pane, choose **CI/CD**, and then choose **Workflows**.

   1. Choose the name of your workflow. You can filter by the source repository or branch name where the workflow is defined, or filter by workflow name or status.

   1. Choose a run that includes the completed render action.

1. In the workflow run, at the top, next to **Visual** and **YAML**, choose **Workflow outputs**.

1. In the **Artifacts** section, choose **Download** next to the artifact that contains the updated task definition file. This artifact will have a **Produced by** column set to the name of your render action.

1. Open the .zip file to view the task definition .json file.