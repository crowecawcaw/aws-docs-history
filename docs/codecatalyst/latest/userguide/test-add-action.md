

Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md).

# Adding the test action
<a name="test-add-action"></a>

Use the following procedure to add a test action to your CodeCatalyst workflow. 

------
#### [ Visual ]

**To add a test action using the visual editor**

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/).

1. In the navigation pane, choose **CI/CD**, and then choose **Workflows**.

1. Choose the name of your workflow. You can filter by the source repository or branch name where the workflow is defined, or filter by workflow name or status.

1. Choose **Edit**.

1. Choose **Visual**.

1. Choose **Actions**.

1. In **Actions**, choose **Test**. 

1. In the **Inputs** and **Configuration** tabs, complete the fields according to your needs. For a description of each field, see the [Build and test actions YAML](build-action-ref.md). This reference provides detailed information on each field (and corresponding YAML property value) as it appears in both the YAML and visual editors.

1. (Optional) Choose **Validate** to validate the workflow's YAML code before committing.

1. Choose **Commit**, enter a commit message, and choose **Commit** again.

------
#### [ YAML ]

**To add a build action using the YAML editor**

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/).

1. In the navigation pane, choose **CI/CD**, and then choose **Workflows**.

1. Choose the name of your workflow. You can filter by the source repository or branch name where the workflow is defined, or filter by workflow name or status.

1. Choose **Edit**.

1. Choose **YAML**.

1. Choose **Actions**.

1. In **Actions**, choose **Test**.

1. Modify the properties in the YAML code according to your needs. An explanation of each available property is provided in the [Build and test actions YAML](build-action-ref.md).

1. (Optional) Choose **Validate** to validate the workflow's YAML code before committing.

1. Choose **Commit**, enter a commit message, and choose **Commit** again.

------

## Test action definition
<a name="test-add-action-definition"></a>

The test action is defined as a set of YAML properties inside your workflow definition file. For information about these properties, see [Build and test actions YAML](build-action-ref.md) in the [Workflow YAML definition](workflow-reference.md).