Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Setting up dependencies between

actions

Use the following instructions to set up dependencies between actions in a
workflow.

When configuring dependencies, follow these guidelines:

- If an action is inside a group, that action can only depend on other
  actions within the same group.
- Actions and action groups can depend on other actions and action groups
  _at the same level_ in the YAML hierarchy, but
  _not_ at a different level.

Visual

###### To set up dependencies using the visual editor

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. Choose your project.
3. In the navigation pane, choose **CI/CD**, and then choose **Workflows**.
4. Choose the name of your workflow. You can filter by the source
   repository or branch name where the workflow is defined, or filter
   by workflow name or status.
5. Choose **Edit**.
6. Choose **Visual**.
7. In the workflow diagram, choose the action that will depend on
   another action.
8. Choose the **Inputs** tab.
9. In **Depends on - optional**, do the
   following:

Specify an action, action group, or gate that must run successfully in order for this action to
run.

For more information about the 'depends on' functionality, see [Sequencing actions](workflows-depends-on.md "workflows-depends-on.md"). 10. (Optional) Choose **Validate** to validate
the workflow's YAML code before committing. 11. Choose **Commit**, enter a commit message,
and choose **Commit** again.

YAML

###### To set up dependencies using the YAML editor

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. Choose your project.
3. In the navigation pane, choose **CI/CD**, and then choose **Workflows**.
4. Choose the name of your workflow. You can filter by the source
   repository or branch name where the workflow is defined, or filter
   by workflow name or status.
5. Choose **Edit**.
6. Choose **YAML**.
7. In an action that will depend on another, add code similar to
   the following:

```
`action-name:`
  DependsOn:
    - action-1
```

For more examples, see [Examples of how to configure
dependencies between actions](workflows-depends-on-examples.md "workflows-depends-on-examples.md"). For general
guidelines, see Setting up dependencies between
actions. For more
information, see the description of the `DependsOn`
property in the [Workflow YAML definition](workflow-reference.md "workflow-reference.md") for your action. 8. (Optional) Choose **Validate** to validate
the workflow's YAML code before committing. 9. Choose **Commit**, enter a commit message,
and choose **Commit** again.
