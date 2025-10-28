Amazon CodeCatalyst will no longer be open to new customers starting on November
7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For
more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Determining

which predefined variables your workflow emits

Use the following procedure to determine which predefined variables a workflow emits
when it runs. You can then reference these variables within the same workflow.

For more information about predefined variables, see [Using predefined variables](workflows-using-predefined-variables.md "workflows-using-predefined-variables.md").

###### To determine the predefined variables that your workflow emits

- Do one of the following:
  - **Run the workflow once**. After the run
    finishes, the variables emitted by the workflow are displayed on the
    **Variables** tab of the run details page. For more
    information, see [Viewing workflow run status and details](workflows-view-run.md "workflows-view-run.md").
  - **Consult the [List of predefined variables](workflow-ref-action-variables.md "workflow-ref-action-variables.md")**. This
    reference lists the variable name (key) and value for each predefined
    variable.

###### Note

The maximum total size of a workflow's variables is listed in [Quotas for workflows in CodeCatalyst](workflows-quotas.md "workflows-quotas.md"). If the total size
exceeds the maximum, the action that occurs after the maximum is reached may
fail.
