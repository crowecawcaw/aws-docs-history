Amazon CodeCatalyst will no longer be open to new customers starting on November
7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For
more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Configuring manual-only triggers

You can limit a workflow so that it can only be started manually by your team using
the **Run** button in the CodeCatalyst console. To configure this
functionality, you must remove the `Triggers` section in the workflow
definition file. The `Triggers` section is included by default when you
create a workflow, but the section is optional and can be removed.

Use the following instructions to remove the `Triggers` section in the
workflow definition file so that the workflow can only be started manually.

For more information about triggers, see [Starting a workflow run automatically using
triggers](workflows-add-trigger.md "workflows-add-trigger.md").

For more information about running workflows, see [Running a workflow](workflows-working-runs.md "workflows-working-runs.md").

Visual

###### To remove the 'Triggers' section (visual editor)

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. Choose your project.
3. In the navigation pane, choose **CI/CD**, and then choose **Workflows**.
4. Choose the name of your workflow. You can filter by the source
   repository or branch name where the workflow is defined, or filter
   by workflow name or status.
5. Choose **Edit**.
6. Choose **Visual**.
7. Choose the **Source** box in the workflow
   diagram.
8. Under **Triggers**, choose the trash can icon to
   remove the `Triggers` section from the workflow.
9. (Optional) Choose **Validate** to validate the
   workflow's YAML code before committing.
10. Choose **Commit**, enter a commit message, and
    choose **Commit** again.

YAML

###### To remove the 'Triggers' section (YAML editor)

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. Choose your project.
3. In the navigation pane, choose **CI/CD**, and then choose **Workflows**.
4. Choose the name of your workflow. You can filter by the source
   repository or branch name where the workflow is defined, or filter
   by workflow name or status.
5. Choose **Edit**.
6. Choose **YAML**.
7. Find the `Triggers` section and remove it.
8. (Optional) Choose **Validate** to validate the
   workflow's YAML code before committing.
9. Choose **Commit**, enter a commit message, and
   choose **Commit** again.
