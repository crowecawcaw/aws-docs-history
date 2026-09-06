

Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md).

# Adding an 'Approval' gate
<a name="workflows-approval-add"></a>

To configure your workflow to require an approval, you must add the **Approval** gate to the workflow. Use the following instructions to add an **Approval** gate to your workflow.

For more information about this gate, see [Requiring approvals on workflow runs](workflows-approval.md).

------
#### [ Visual ]<a name="workflows-add-trigger-add-console"></a>

**To add an 'Approval' gate to a workflow (visual editor)**

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/).

1. Choose your project.

1. In the navigation pane, choose **CI/CD**, and then choose **Workflows**.

1. Choose the name of your workflow. You can filter by the source repository or branch name where the workflow is defined, or filter by workflow name or status.

1. Choose **Edit**.

1. At the top-left, choose **Gates**.

1. In the **Gates** catalog, in **Approval**, choose the plus sign (**\+**).

1. Choose **Inputs**, and in the **Depends on** field, do the following.

   Specify an action, action group, or gate that must run successfully in order for this gate to run. By default, when you add a gate to a workflow, the gate is set to depend on the last action in your workflow. If you remove this property, the gate will not depend on anything, and will run first, before other actions.
**Note**  
A gate must be configured to run before or after an action, action group, or gate. It cannot be set up to run in parallel with other actions, action groups, and gates.

   For more information about the **Depends on** functionality, see [Sequencing gates and actions](workflows-gates-depends-on.md).

1. Choose the **Configuration** tab.

1. In the **Gate name** field, do the following.

   Specify the name you want to give the gate. All gate names must be unique within the workflow. Gate names are limited to alphanumeric characters (a-z, A-Z, 0-9), hyphens (-), and underscores (\_). Spaces are not allowed. You cannot use quotation marks to enable special characters and spaces in gate names.

1. (Optional) In the **Number of approvals** field, do the following.

   Specify the minimum number of approvals required to unlock the **Approval** gate. The minimum is `1`. The maximum is `2`. If omitted, the default is `1`.
**Note**  
If you want to omit the `ApprovalsRequired` property, remove the gate's `Configuration` section from the workflow definition file.

1. (Optional) Choose **Validate** to validate the workflow's YAML code before committing.

1. Choose **Commit**, enter a commit message, and choose **Commit** again.

------
#### [ YAML ]

**To add an 'Approval' gate to a workflow (YAML editor)**

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/).

1. Choose your project.

1. In the navigation pane, choose **CI/CD**, and then choose **Workflows**.

1. Choose the name of your workflow. You can filter by the source repository or branch name where the workflow is defined, or filter by workflow name or status.

1. Choose **Edit**.

1. Choose **YAML**.

1. Add an `Approval` section and underlying properties using the following example as a guide. For more information, see the ['Approval' gate YAML](approval-ref.md) in the [Workflow YAML definition](workflow-reference.md).

   ```
   Actions:
     MyApproval_01:
       Identifier: aws/approval@v1
       DependsOn:
         - PreviousAction
       Configuration:
         ApprovalsRequired: 2
   ```

   For another example, see [Example: An 'Approval' gate](workflows-approval-example.md).

1. (Optional) Choose **Validate** to validate the workflow's YAML code before committing.

1. Choose **Commit**, enter a commit message, and choose **Commit** again.

------