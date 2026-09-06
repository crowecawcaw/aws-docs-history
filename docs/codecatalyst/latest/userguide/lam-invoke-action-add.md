

Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md).

# Adding the 'AWS Lambda invoke' action
<a name="lam-invoke-action-add"></a>

 Use the following instructions to add the **AWS Lambda invoke** action to your workflow. 

**Prerequisite**  
Before you begin, make sure your AWS Lambda function and associated Lambda execution role are ready and available in AWS. For more information, see the [Lambda execution role](https://docs.aws.amazon.com/lambda/latest/dg/lambda-intro-execution-role.html) topic in the *AWS Lambda Developer Guide*.

------
#### [ Visual ]

**To add the 'AWS Lambda invoke' action using the visual editor**

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/).

1. Choose your project.

1. In the navigation pane, choose **CI/CD**, and then choose **Workflows**.

1. Choose the name of your workflow. You can filter by the source repository or branch name where the workflow is defined, or filter by workflow name or status.

1. Choose **Edit**.

1. Choose **Visual**.

1. At the top-left, choose **\+ Actions** to open the action catalog.

1. From the drop-down list, choose **Amazon CodeCatalyst**.

1. Search for the **AWS Lambda invoke** action, and do one of the following:
   + Choose the plus sign (**\+**) to add the action to the workflow diagram and open its configuration pane.

     Or
   + Choose **AWS Lambda invoke**. The action details dialog box appears. On this dialog box:
     + (Optional) Choose **View source** to [view the action's source code](workflows-view-source.md#workflows-view-source.title).
     + Choose **Add to workflow** to add the action to the workflow diagram and open its configuration pane.

1. In the **Inputs**, **Configuration**, and **Outputs** tabs, complete the fields according to your needs. For a description of each field, see the ['AWS Lambda invoke' action YAML](lam-invoke-action-ref.md). This reference provides detailed information about each field (and corresponding YAML property value) as it appears in both the YAML and visual editors.

1. (Optional) Choose **Validate** to validate the workflow's YAML code before committing.

1. Choose **Commit**, enter a commit message, and choose **Commit** again.

------
#### [ YAML ]

**To add the 'AWS Lambda invoke' action using the YAML editor**

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/).

1. Choose your project.

1. In the navigation pane, choose **CI/CD**, and then choose **Workflows**.

1. Choose the name of your workflow. You can filter by the source repository or branch name where the workflow is defined, or filter by workflow name or status.

1. Choose **Edit**.

1. Choose **YAML**.

1. At the top-left, choose **\+ Actions** to open the action catalog.

1. From the drop-down list, choose **Amazon CodeCatalyst**.

1. Search for the **AWS Lambda invoke** action, and do one of the following:
   + Choose the plus sign (**\+**) to add the action to the workflow diagram and open its configuration pane.

     Or
   + Choose **AWS Lambda invoke**. The action details dialog box appears. On this dialog box:
     + (Optional) Choose **View source** to [view the action's source code](workflows-view-source.md#workflows-view-source.title).
     + Choose **Add to workflow** to add the action to the workflow diagram and open its configuration pane.

1. Modify the properties in the YAML code according to your needs. An explanation of each available property is provided in the ['AWS Lambda invoke' action YAML](lam-invoke-action-ref.md).

1. (Optional) Choose **Validate** to validate the workflow's YAML code before committing.

1. Choose **Commit**, enter a commit message, and choose **Commit** again.

------