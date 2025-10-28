Amazon CodeCatalyst will no longer be open to new customers starting on November
7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For
more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Assigning a fleet or compute to an

action

By default, workflow actions use the `Linux.x86-64.Large` on-demand fleet
with an Amazon EC2 compute type. To use a provisioned fleet instead, or to use a different
on-demand fleet, such as `Linux.x86-64.2XLarge`, use the following
instructions.

Visual

###### Before you begin

- If you want to assign a provisioned fleet, you must first create
  the provisioned fleet. For more information, see [Creating a provisioned fleet](projects-create-compute-resource.md "projects-create-compute-resource.md").

###### To assign a provisioned fleet or different fleet type to an

action

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. Choose your project.
3. In the navigation pane, choose **CI/CD**, and then choose **Workflows**.
4. Choose the name of your workflow. You can filter by the source
   repository or branch name where the workflow is defined, or filter
   by workflow name or status.
5. Choose **Edit**.
6. Choose **Visual**.
7. In the workflow diagram, choose the action that you want to assign
   your provisioned fleet or new fleet type to.
8. Choose the **Configuration** tab.
9. In **Compute fleet**, do the following:

Specify the machine or fleet that will run your workflow or workflow actions. With on-demand fleets, when an action starts, the workflow provisions the resources it needs, and the machines are destroyed when the action finishes. Examples of on-demand fleets: `Linux.x86-64.Large`, `Linux.x86-64.XLarge`. For more information about on-demand fleets, see [On-demand fleet properties](workflows-working-compute.md#compute.on-demand "workflows-working-compute.md#compute.on-demand").

With provisioned fleets, you configure a set of dedicated machines to run your workflow actions. These machines remain idle, ready to process actions immediately. For more information about provisioned fleets, see [Provisioned fleet properties](workflows-working-compute.md#compute.provisioned-fleets "workflows-working-compute.md#compute.provisioned-fleets").

If `Fleet` is omitted, the default is `Linux.x86-64.Large`. 10. (Optional) Choose **Validate** to validate the
workflow's YAML code before committing. 11. Choose **Commit**, enter a commit message, and
choose **Commit** again.

YAML

###### Before you begin

- If you want to assign a provisioned fleet, you must first create
  the provisioned fleet. For more information, see [Creating a provisioned fleet](projects-create-compute-resource.md "projects-create-compute-resource.md").

###### To assign a provisioned fleet or different fleet type to an

action

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. Choose your project.
3. In the navigation pane, choose **CI/CD**, and then choose **Workflows**.
4. Choose the name of your workflow. You can filter by the source
   repository or branch name where the workflow is defined, or filter
   by workflow name or status.
5. Choose **Edit**.
6. Choose **YAML**.
7. Find the action that you want to assign your provisioned fleet or
   new fleet type to.
8. In the action, add a `Compute` property and set
   `Fleet` to the name of your fleet or on-demand fleet
   type. For more information, see the description of the
   `Fleet` property in the [Build and test actions YAML](build-action-ref.md "build-action-ref.md")
   for your action.
9. (Optional) Choose **Validate** to validate the
   workflow's YAML code before committing.
10. Choose **Commit**, enter a commit message, and
    choose **Commit** again.
