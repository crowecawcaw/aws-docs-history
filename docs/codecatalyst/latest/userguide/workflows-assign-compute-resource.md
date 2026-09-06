

Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md).

# Assigning a fleet or compute to an action
<a name="workflows-assign-compute-resource"></a>

By default, workflow actions use the `Linux.x86-64.Large` on-demand fleet with an Amazon EC2 compute type. To use a provisioned fleet instead, or to use a different on-demand fleet, such as `Linux.x86-64.2XLarge`, use the following instructions.

------
#### [ Visual ]

**Before you begin**
+ If you want to assign a provisioned fleet, you must first create the provisioned fleet. For more information, see [Creating a provisioned fleet](projects-create-compute-resource.md).

**To assign a provisioned fleet or different fleet type to an action**

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/).

1. Choose your project.

1. In the navigation pane, choose **CI/CD**, and then choose **Workflows**.

1. Choose the name of your workflow. You can filter by the source repository or branch name where the workflow is defined, or filter by workflow name or status.

1. Choose **Edit**.

1. Choose **Visual**.

1. In the workflow diagram, choose the action that you want to assign your provisioned fleet or new fleet type to.

1. Choose the **Configuration** tab.

1. In **Compute fleet**, do the following:

   Specify the machine or fleet that will run your workflow or workflow actions. With on-demand fleets, when an action starts, the workflow provisions the resources it needs, and the machines are destroyed when the action finishes. Examples of on-demand fleets: `Linux.x86-64.Large`, `Linux.x86-64.XLarge`. For more information about on-demand fleets, see [On-demand fleet properties](workflows-working-compute.md#compute.on-demand).

   With provisioned fleets, you configure a set of dedicated machines to run your workflow actions. These machines remain idle, ready to process actions immediately. For more information about provisioned fleets, see [Provisioned fleet properties](workflows-working-compute.md#compute.provisioned-fleets).

   If `Fleet` is omitted, the default is `Linux.x86-64.Large`.

1. (Optional) Choose **Validate** to validate the workflow's YAML code before committing.

1. Choose **Commit**, enter a commit message, and choose **Commit** again.

------
#### [ YAML ]

**Before you begin**
+ If you want to assign a provisioned fleet, you must first create the provisioned fleet. For more information, see [Creating a provisioned fleet](projects-create-compute-resource.md).

**To assign a provisioned fleet or different fleet type to an action**

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/).

1. Choose your project.

1. In the navigation pane, choose **CI/CD**, and then choose **Workflows**.

1. Choose the name of your workflow. You can filter by the source repository or branch name where the workflow is defined, or filter by workflow name or status.

1. Choose **Edit**.

1. Choose **YAML**.

1. Find the action that you want to assign your provisioned fleet or new fleet type to.

1. In the action, add a `Compute` property and set `Fleet` to the name of your fleet or on-demand fleet type. For more information, see the description of the `Fleet` property in the [Build and test actions YAML](build-action-ref.md) for your action.

1. (Optional) Choose **Validate** to validate the workflow's YAML code before committing.

1. Choose **Commit**, enter a commit message, and choose **Commit** again.

------