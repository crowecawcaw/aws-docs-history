Amazon CodeCatalyst will no longer be open to new customers starting on November
7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For
more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Grouping actions into action groups

An _action group_ contains one or more actions. Grouping
actions into action groups helps you keep your workflow organized, and also allows you
to configure dependencies between different groups.

###### Note

You cannot nest action groups within other action groups or actions.

###### Topics

- [Defining an action group](#workflows-define-action-group "#workflows-define-action-group")
- [Example: Defining two action
  groups](workflows-group-actions-example.md "workflows-group-actions-example.md")

## Defining an action group

Use the following instructions to define an CodeCatalyst action group.

Visual
_Not available. Choose YAML to view the YAML
instructions._

YAML

###### To define a group

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. Choose your project.
3. In the navigation pane, choose **CI/CD**, and then choose **Workflows**.
4. Choose the name of your workflow. You can filter by the source
   repository or branch name where the workflow is defined, or filter
   by workflow name or status.
5. Choose **Edit**.
6. Choose **YAML**.
7. In `Actions`, add code similar to the
   following:

```
Actions:
  `action-group-name`:
    Actions:
      action-1:
        Identifier: aws/build@v1
        Configuration:
          ...
      action-2:
        Identifier: aws/build@v1
        Configuration:
          ...
```

For another example, see [Example: Defining two action
groups](workflows-group-actions-example.md "workflows-group-actions-example.md"). For more
information, see the description of the
`action-group-name` property in the [Actions](workflow-reference.md#actions-reference "workflow-reference.md#actions-reference") of the [Workflow YAML definition](workflow-reference.md "workflow-reference.md"). 8. (Optional) Choose **Validate** to validate
the workflow's YAML code before committing. 9. Choose **Commit**, enter a commit message,
and choose **Commit** again.
