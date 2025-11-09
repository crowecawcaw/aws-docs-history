Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Removing an action from a workflow

Use the following instructions to remove an action from a workflow.

Visual

###### To remove an action using the visual editor

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. Choose your project.
3. In the navigation pane, choose **CI/CD**, and then choose **Workflows**.
4. Choose the name of your workflow. You can filter by the source
   repository or branch name where the workflow is defined, or filter
   by workflow name or status.
5. Choose **Edit**.
6. Choose **Visual**.
7. In the workflow diagram, in the action you want
   to remove, choose the vertical ellipsis icon (
   ![Ellipsis.](images/flows/elipsis.png)
   ), and choose
   **Remove**.
8. (Optional) Choose **Validate** to validate the
   workflow's YAML code before committing.
9. Choose **Commit**, enter a commit message, and
   choose **Commit** again.

YAML

###### To remove an action using the YAML editor

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. Choose your project.
3. In the navigation pane, choose **CI/CD**, and then choose **Workflows**.
4. Choose the name of your workflow. You can filter by the source
   repository or branch name where the workflow is defined, or filter
   by workflow name or status.
5. Choose **Edit**.
6. Choose **YAML**.
7. Find the section of the YAML that contains the action you want to
   remove.

Select the section and press the delete key on your
keyboard. 8. (Optional) Choose **Validate** to validate the
workflow's YAML code before committing. 9. Choose **Commit**, enter a commit message, and
choose **Commit** again.
