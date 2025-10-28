Amazon CodeCatalyst will no longer be open to new customers starting on November
7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For
more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Using variables in workflows

A _variable_ is a key-value pair that contains information that you can
reference in your Amazon CodeCatalyst workflow. The value portion of the variable is replaced with an
actual value when the workflow runs.

There are two types of variable that you can use in a workflow:

- **User-defined variables** – These are
  key-value pairs that you define.
- **Predefined variables** – These are key-value
  pairs that are emitted by a workflow automatically. There is no need for you to
  define them.
  For more information about workflows, see [Build, test, and deploy with workflows](workflow.md "workflow.md").

###### Note

CodeCatalyst also supports [GitHub output parameters](https://docs.github.com/en/actions/using-workflows/workflow-commands-for-github-actions#setting-an-output-parameter "https://docs.github.com/en/actions/using-workflows/workflow-commands-for-github-actions#setting-an-output-parameter"), which behave like variables and can be referenced
in other actions. For more information, see [Exporting GitHub output parameters](integrations-github-action-export.md "integrations-github-action-export.md") and [Referencing GitHub output
parameters](integrations-github-action-referencing.md "integrations-github-action-referencing.md")

###### Topics

- [Using user-defined variables](workflows-using-variables.md "workflows-using-variables.md")
- [Using predefined variables](workflows-using-predefined-variables.md "workflows-using-predefined-variables.md")
