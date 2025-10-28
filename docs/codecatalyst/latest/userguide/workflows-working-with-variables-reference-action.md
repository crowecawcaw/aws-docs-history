Amazon CodeCatalyst will no longer be open to new customers starting on November
7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For
more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Referencing a

variable output by another action

Use the following instructions to reference variables output by other
actions.

###### Note

To reference a variable output from a GitHub Action, see [Referencing GitHub output
parameters](integrations-github-action-referencing.md "integrations-github-action-referencing.md").

For more information about variables, see [Using variables in workflows](workflows-working-with-variables.md "workflows-working-with-variables.md").

###### Prerequisite

Make sure you have exported the variable you want to reference. For more
information, see [Exporting a variable
so that other actions can use it](workflows-working-with-variables-export-input.md "workflows-working-with-variables-export-input.md").

Visual
_Not available. Choose YAML to view the YAML
instructions._

YAML

###### To reference a variable output by another action (YAML

editor)

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. Choose your project.
3. In the navigation pane, choose **CI/CD**, and then choose **Workflows**.
4. Choose the name of your workflow. You can filter by the source
   repository or branch name where the workflow is defined, or
   filter by workflow name or status.
5. Choose **Edit**.
6. Choose **YAML**.
7. In the CodeCatalyst action, add a reference to the variable using
   the following syntax:

```
${`action-group-name`.`action-name`.`variable-name`}
```

Replace:

    * `action-group-name` with the
     name of the action group that contains the action that
     outputs variable.


    ###### Note

    You can omit
     `action-group-name` if
     there is no action group, or if the variable is
     produced by an action in the same action
     group.
    * `action-name` with the name
     of the action that outputs the variable.
    * `variable-name` with the name
     of the variable.

For example:

```
MySecondAction:
    Configuration:
      Steps:
        - Run: ${MyFirstAction.TIMESTAMP}
```

For more examples, see [Examples of
variables](workflows-working-with-variables-ex.md "workflows-working-with-variables-ex.md"). For
more information, see the [Workflow YAML definition](workflow-reference.md "workflow-reference.md") for your action. 8. (Optional) Choose **Validate** to validate
the workflow's YAML code before committing. 9. Choose **Commit**, enter a commit message,
and choose **Commit** again.
