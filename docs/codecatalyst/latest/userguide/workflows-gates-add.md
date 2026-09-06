

Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md).

# Adding a gate to a workflow
<a name="workflows-gates-add"></a>

In Amazon CodeCatalyst, you can add a gate to a workflow to prevent it from proceeding unless certain conditions are met. Use the following instructions to add a gate to a workflow.

For more information about gates, see [Gating a workflow run](workflows-gates.md).

**To add and configure a gate**

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/).

1. Choose your project.

1. In the navigation pane, choose **CI/CD**, and then choose **Workflows**.

1. Choose the name of your workflow. You can filter by the source repository or branch name where the workflow is defined, or filter by workflow name or status.

1. Choose **Edit**.

1. Choose **Visual**.

1. On the left, choose **Gates**.

1. In the gate catalog, search for a gate, and then choose the plus sign (**\+**) to add the gate to your workflow.

1. Configure the gate. Choose **Visual** to use the visual editor, or **YAML** to use the YAML editor. For detailed instructions, see:
   + [Adding an 'Approval' gate](workflows-approval-add.md)

1. (Optional) Choose **Validate** to make sure the YAML code is valid.

1. Choose **Commit** to commit your changes.