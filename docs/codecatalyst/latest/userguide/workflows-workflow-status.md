Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Workflow states in CodeCatalyst

A workflow can have one of the following states:

- **Valid** – The workflow is runnable and can be activated
  by [triggers](workflows-add-trigger.md#workflows-add-trigger.title "workflows-add-trigger.md#workflows-add-trigger.title").

For a workflow to be marked as valid, both of the following conditions must be
true:

    + The workflow definition file must be valid.
    + The workflow must have no triggers, no push triggers, or a push trigger
     that runs using the files on the current branch. For more information, see
     [Usage guidelines for triggers and
     branches](workflows-add-trigger-considerations.md "workflows-add-trigger-considerations.md").

- **Not valid** – The workflow's definition file
  is not valid. The workflow cannot be run manually, or automatically through
  triggers. Workflows that are not valid appear with a **Workflow definition
  has `n` errors** message (or similar) in the
  CodeCatalyst console.

For a workflow to be marked as not valid, the following condition must be
true:

    + The workflow definition file must be misconfigured.


    To fix a misconfigured workflow definition file, see [How do I fix "Workflow definition
     has n errors" errors?](troubleshooting-workflows.md#troubleshooting-workflows-asterisks "troubleshooting-workflows.md#troubleshooting-workflows-asterisks").

- **Inactive** – The workflow definition is valid but cannot
  be run manually, or automatically through triggers.

For a workflow to be marked as inactive, both of the following conditions must be
true:

    + The workflow definition file must be valid.
    + The workflow definition file must include a push trigger that specifies a
     branch that is different from the one that the workflow definition file is
     currently on. For more information, see [Usage guidelines for triggers and
     branches](workflows-add-trigger-considerations.md "workflows-add-trigger-considerations.md").


    To switch a workflow from **Inactive** to
     **Active**, see [How do I fix "Workflow is inactive"
     messages?](troubleshooting-workflows.md#troubleshooting-workflows-inactive "troubleshooting-workflows.md#troubleshooting-workflows-inactive").


    ###### Note

    If there are a lot of workflows in the **Inactive**
     state, you can filter them from view. To filter out inactive workflows,
     choose the **Filter workflows** field at the top of the
     **Workflows** page, choose
     **Status**, choose **Status != Does not
     equal**, and choose **INACTIVE**.

###### Note

If the workflow specifies a resource that you later remove (for example, a package
repository), CodeCatalyst won't detect this change and will continue to mark the workflow as
valid. These types of issues will be caught when the workflow runs.
