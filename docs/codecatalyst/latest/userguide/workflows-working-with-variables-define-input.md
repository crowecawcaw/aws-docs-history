

Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md).

# Defining a variable
<a name="workflows-working-with-variables-define-input"></a>

You can define variables in two ways:
+ In the `Inputs` section of a workflow action – see [To define a variable in the 'Inputs' section](#workflows-to-define-variable-input)
+ In the `Steps` section of a workflow action – see [To define a variable in the 'Steps' section](#workflows-to-define-variable-steps)
**Note**  
The `Steps` method only works with the CodeCatalyst build, test, and **GitHub Actions** actions, because these are the only actions that include a `Steps` section.

For examples, see [Examples of variables](workflows-working-with-variables-ex.md).

For more information about variables, see [Using variables in workflows](workflows-working-with-variables.md).

------
#### [ Visual ]

**To define a variable in the 'Inputs' section (visual editor)**

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/).

1. Choose your project.

1. In the navigation pane, choose **CI/CD**, and then choose **Workflows**.

1. Choose the name of your workflow. You can filter by the source repository or branch name where the workflow is defined, or filter by workflow name or status.

1. Choose **Edit**.

1. Choose **Visual**.

1. In the workflow diagram, choose the action where you want to set the variable.

1. Choose **Inputs**.

1. In **Variables - optional**, choose **Add variable**, and then do the following:

   Specify a sequence of name/value pairs that define the input variables that you want to make available to the action. Variable names are limited to alphanumeric characters (a-z, A-Z, 0-9), hyphens (-), and underscores (\_). Spaces are not allowed. You cannot use quotation marks to enable special characters and spaces in variable names.

   For more information about variables, including examples, see [Using variables in workflows](workflows-working-with-variables.md).

1. (Optional) Choose **Validate** to validate the workflow's YAML code before committing.

1. Choose **Commit**, enter a commit message, and choose **Commit** again.

------
#### [ YAML ]

**To define a variable in the 'Inputs' section (YAML editor)**

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/).

1. Choose your project.

1. In the navigation pane, choose **CI/CD**, and then choose **Workflows**.

1. Choose the name of your workflow. You can filter by the source repository or branch name where the workflow is defined, or filter by workflow name or status.

1. Choose **Edit**.

1. Choose **YAML**.

1. In a workflow action, add code similar to the following:

   ```
   {{action-name}}:
     Inputs:
       Variables:
         - Name: {{variable-name}}
           Value: {{variable-value}}
   ```

   For more examples, see [Examples of variables](workflows-working-with-variables-ex.md). For more information, see the [Workflow YAML definition](workflow-reference.md) for your action.

1. (Optional) Choose **Validate** to validate the workflow's YAML code before committing.

1. Choose **Commit**, enter a commit message, and choose **Commit** again.

------

------
#### [ Visual ]

**To define a variable in the 'Steps' section (visual editor)**

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/).

1. Choose your project.

1. In the navigation pane, choose **CI/CD**, and then choose **Workflows**.

1. Choose the name of your workflow. You can filter by the source repository or branch name where the workflow is defined, or filter by workflow name or status.

1. Choose **Edit**.

1. Choose **Visual**.

1. In the workflow diagram, choose the action where you want to set the variable.

1. Choose **Configuration**.

1. In **Shell commands** or **GitHub Actions YAML**, whichever is available, define a variable in the action's `Steps`, either explicitly or implicitly.
   + To define the variable explicitly, include it in a bash command directly to the `Steps` section.
   + To define a variable implicitly, specify it in a file that's referenced in the action's `Steps` section.

     For examples, see [Examples of variables](workflows-working-with-variables-ex.md). For more information, see the [Workflow YAML definition](workflow-reference.md) for the action.

1. (Optional) Choose **Validate** to validate the workflow's YAML code before committing.

1. Choose **Commit**, enter a commit message, and choose **Commit** again.

------
#### [ YAML ]

**To define a variable in the 'Steps' section (YAML editor)**

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/).

1. Choose your project.

1. In the navigation pane, choose **CI/CD**, and then choose **Workflows**.

1. Choose the name of your workflow. You can filter by the source repository or branch name where the workflow is defined, or filter by workflow name or status.

1. Choose **Edit**.

1. Choose **YAML**.

1. In a workflow action, define a variable in the action's `Steps` section, either explicitly or implicitly.
   + To define the variable explicitly, include it in a bash command directly to the `Steps` section.
   + To define a variable implicitly, specify it in a file that's referenced in the action's `Steps` section.

     For examples, see [Examples of variables](workflows-working-with-variables-ex.md). For more information, see the [Workflow YAML definition](workflow-reference.md) for the action.

1. (Optional) Choose **Validate** to validate the workflow's YAML code before committing.

1. Choose **Commit**, enter a commit message, and choose **Commit** again.

------