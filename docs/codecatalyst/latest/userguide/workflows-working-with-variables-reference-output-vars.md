Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Referencing a

predefined variable

You can reference predefined variables in any action within an Amazon CodeCatalyst
workflow.

Use the following instructions to reference a predefined variable in a
workflow.

For more information about predefined variables, see [Using predefined variables](workflows-using-predefined-variables.md "workflows-using-predefined-variables.md").

###### Prerequisite

Determine the name of the predefined variable you want to reference, such as
`CommitId`. For more information, see [Determining
which predefined variables your workflow emits](workflows-working-with-variables-determine-output-vars.md "workflows-working-with-variables-determine-output-vars.md").

Visual
_Not available. Choose YAML to view the YAML
instructions._

YAML

###### To reference a predefined variable (YAML editor)

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. Choose your project.
3. In the navigation pane, choose **CI/CD**, and then choose **Workflows**.
4. Choose the name of your workflow. You can filter by the source
   repository or branch name where the workflow is defined, or filter
   by workflow name or status.
5. Choose **Edit**.
6. Choose **YAML**.
7. In a CodeCatalyst action, add the predefined variable reference using
   the following syntax:

```
${`action-group-name`.`action-name-or-WorkflowSource`.`variable-name`}
```

Replace:

    * `action-group-name` with the name
     of the action group.


    ###### Note

    You can omit
     `action-group-name` if
     there is no action group, or if the variable is produced
     by an action in the same action group.
    * `action-name-or-WorkflowSource`
     with:


    The name of the action that outputs the variable.


    or


    `WorkflowSource`, if the variable is the
     `BranchName` or `CommitId`
     variable.
    * `variable-name` with the name of
     the variable.

For example:

```
MySecondAction:
    Configuration:
      Steps:
        - Run: echo ${MyFirstECSAction.cluster}
```

Another example:

```
MySecondAction:
    Configuration:
      Steps:
        - Run: echo ${WorkflowSource.CommitId}
```

For more examples, see [Examples of referencing predefined
variables](workflows-predefined-examples.md "workflows-predefined-examples.md"). For more
information, see the [Workflow YAML definition](workflow-reference.md "workflow-reference.md") for your action. 8. (Optional) Choose **Validate** to validate the
workflow's YAML code before committing. 9. Choose **Commit**, enter a commit message, and
choose **Commit** again.
