

Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md).

# Configuring manual-only triggers
<a name="workflows-manual-only"></a>

You can limit a workflow so that it can only be started manually by your team using the **Run** button in the CodeCatalyst console. To configure this functionality, you must remove the `Triggers` section in the workflow definition file. The `Triggers` section is included by default when you create a workflow, but the section is optional and can be removed.

Use the following instructions to remove the `Triggers` section in the workflow definition file so that the workflow can only be started manually.

For more information about triggers, see [Starting a workflow run automatically using triggers](workflows-add-trigger.md).

For more information about running workflows, see [Running a workflow](workflows-working-runs.md).

------
#### [ Visual ]

**To remove the 'Triggers' section (visual editor)**

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/).

1. Choose your project.

1. In the navigation pane, choose **CI/CD**, and then choose **Workflows**.

1. Choose the name of your workflow. You can filter by the source repository or branch name where the workflow is defined, or filter by workflow name or status.

1. Choose **Edit**.

1. Choose **Visual**.

1. Choose the **Source** box in the workflow diagram.

1. Under **Triggers**, choose the trash can icon to remove the `Triggers` section from the workflow.

1. (Optional) Choose **Validate** to validate the workflow's YAML code before committing.

1. Choose **Commit**, enter a commit message, and choose **Commit** again.

------
#### [ YAML ]

**To remove the 'Triggers' section (YAML editor)**

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/).

1. Choose your project.

1. In the navigation pane, choose **CI/CD**, and then choose **Workflows**.

1. Choose the name of your workflow. You can filter by the source repository or branch name where the workflow is defined, or filter by workflow name or status.

1. Choose **Edit**.

1. Choose **YAML**.

1. Find the `Triggers` section and remove it.

1. (Optional) Choose **Validate** to validate the workflow's YAML code before committing.

1. Choose **Commit**, enter a commit message, and choose **Commit** again.

------