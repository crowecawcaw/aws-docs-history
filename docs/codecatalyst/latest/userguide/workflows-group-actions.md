

Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md).

# Grouping actions into action groups
<a name="workflows-group-actions"></a>

An *action group* contains one or more actions. Grouping actions into action groups helps you keep your workflow organized, and also allows you to configure dependencies between different groups.

**Note**  
You cannot nest action groups within other action groups or actions.

**Topics**
+ [Defining an action group](#workflows-define-action-group)
+ [Example: Defining two action groups](workflows-group-actions-example.md)

## Defining an action group
<a name="workflows-define-action-group"></a>

Use the following instructions to define an CodeCatalyst action group.

------
#### [ Visual ]

*Not available. Choose YAML to view the YAML instructions.*

------
#### [ YAML ]

**To define a group**

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/).

1. Choose your project.

1. In the navigation pane, choose **CI/CD**, and then choose **Workflows**.

1. Choose the name of your workflow. You can filter by the source repository or branch name where the workflow is defined, or filter by workflow name or status.

1. Choose **Edit**.

1. Choose **YAML**.

1. In `Actions`, add code similar to the following:

   ```
   Actions:
     {{action-group-name}}: 
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

   For another example, see [Example: Defining two action groups](workflows-group-actions-example.md). For more information, see the description of the `action-group-name` property in the [Actions](workflow-reference.md#actions-reference) of the [Workflow YAML definition](workflow-reference.md).

1. (Optional) Choose **Validate** to validate the workflow's YAML code before committing.

1. Choose **Commit**, enter a commit message, and choose **Commit** again.

------