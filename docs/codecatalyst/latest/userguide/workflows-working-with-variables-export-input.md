Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Exporting a variable

so that other actions can use it

Use the following instructions to export a variable from an action so that you can
reference it in other actions.

Before you export a variable, note the following:

- If you only need to reference the variable within the action where it's
  defined, then you don't need to export it.
- Not all actions support exporting variables. To determine whether your
  action supports this feature, run through the visual editor instructions
  that follow, and see if the action includes a **Variables**
  button on the **Outputs** tab. If yes, exporting variables
  is supported.
- To export a variable from a GitHub Action, see [Exporting GitHub output parameters](integrations-github-action-export.md "integrations-github-action-export.md").
  For more information about variables, see [Using variables in workflows](workflows-working-with-variables.md "workflows-working-with-variables.md").

###### Prerequisite

Make sure you have defined the variable you want to export. For more
information, see [Defining a
variable](workflows-working-with-variables-define-input.md "workflows-working-with-variables-define-input.md").

Visual

###### To export a variable (visual editor)

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. Choose your project.
3. In the navigation pane, choose **CI/CD**, and then choose **Workflows**.
4. Choose the name of your workflow. You can filter by the source
   repository or branch name where the workflow is defined, or
   filter by workflow name or status.
5. Choose **Edit**.
6. Choose **Visual**.
7. In the workflow diagram, choose the action that you want to
   export the variable from.
8. Choose **Outputs**.
9. In **Variables - optional**, choose
   **Add variable**, and then do the
   following:

Specify the name of a variable that you want the action to export. This variable must already be
defined in the `Inputs` or `Steps` section of the same action. 10. (Optional) Choose **Validate** to validate
the workflow's YAML code before committing. 11. Choose **Commit**, enter a commit message,
and choose **Commit** again.

YAML

###### To export a variable (YAML editor)

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. Choose your project.
3. In the navigation pane, choose **CI/CD**, and then choose **Workflows**.
4. Choose the name of your workflow. You can filter by the source
   repository or branch name where the workflow is defined, or
   filter by workflow name or status.
5. Choose **Edit**.
6. Choose **YAML**.
7. In the action that you want to export the variable from, add
   code similar to the following:

```
`action-name`:
  Outputs:
    Variables:
      - Name: `variable-name`
```

For more examples, see [Examples of
variables](workflows-working-with-variables-ex.md "workflows-working-with-variables-ex.md"). 8. (Optional) Choose **Validate** to validate
the workflow's YAML code before committing. 9. Choose **Commit**, enter a commit message,
and choose **Commit** again.
