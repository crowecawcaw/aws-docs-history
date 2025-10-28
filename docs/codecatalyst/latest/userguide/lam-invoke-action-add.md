Amazon CodeCatalyst will no longer be open to new customers starting on November
7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For
more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Adding the 'AWS Lambda invoke' action

Use the following instructions to add the **AWS Lambda invoke** action to
your workflow.

###### Prerequisite

Before you begin, make sure your AWS Lambda function and associated Lambda execution role
are ready and available in AWS. For more information, see the [Lambda execution role](../../../lambda/latest/dg/lambda-intro-execution-role.md "../../../lambda/latest/dg/lambda-intro-execution-role.md") topic
in the _AWS Lambda Developer Guide_.

Visual

###### To add the 'AWS Lambda invoke' action using the visual editor

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. Choose your project.
3. In the navigation pane, choose **CI/CD**, and then choose **Workflows**.
4. Choose the name of your workflow. You can filter by the source
   repository or branch name where the workflow is defined, or filter
   by workflow name or status.
5. Choose **Edit**.
6. Choose **Visual**.
7. At the top-left, choose **+ Actions** to open the action
   catalog.
8. From the drop-down list, choose **Amazon CodeCatalyst**.
9. Search for the **AWS Lambda invoke** action, and do one of the
   following:
   - Choose the plus sign (**+**) to add the action to the
     workflow diagram and open its configuration pane.

   Or
   - Choose **AWS Lambda invoke**. The action details dialog box
     appears. On this dialog box:
     - (Optional) Choose **View source** to [view the action's source
       code](workflows-view-source.md#workflows-view-source.title "workflows-view-source.md#workflows-view-source.title").
     - Choose **Add to workflow** to add the action to the
       workflow diagram and open its configuration pane.

10. In the **Inputs**, **Configuration**, and
    **Outputs** tabs, complete the fields according to your needs.
    For a description of each field, see the ['AWS Lambda invoke' action YAML](lam-invoke-action-ref.md "lam-invoke-action-ref.md"). This reference provides detailed
    information about each field (and corresponding YAML property value) as it appears
    in both the YAML and visual editors.
11. (Optional) Choose **Validate** to validate the workflow's YAML
    code before committing.
12. Choose **Commit**, enter a commit message, and choose
    **Commit** again.

YAML

###### To add the 'AWS Lambda invoke' action using the YAML editor

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. Choose your project.
3. In the navigation pane, choose **CI/CD**, and then choose **Workflows**.
4. Choose the name of your workflow. You can filter by the source
   repository or branch name where the workflow is defined, or filter
   by workflow name or status.
5. Choose **Edit**.
6. Choose **YAML**.
7. At the top-left, choose **+ Actions** to open the action
   catalog.
8. From the drop-down list, choose **Amazon CodeCatalyst**.
9. Search for the **AWS Lambda invoke** action, and do one of the
   following:
   - Choose the plus sign (**+**) to add the action to the
     workflow diagram and open its configuration pane.

   Or
   - Choose **AWS Lambda invoke**. The action details dialog box
     appears. On this dialog box:
     - (Optional) Choose **View source** to [view the action's source
       code](workflows-view-source.md#workflows-view-source.title "workflows-view-source.md#workflows-view-source.title").
     - Choose **Add to workflow** to add the action to the
       workflow diagram and open its configuration pane.

10. Modify the properties in the YAML code according to your needs. An explanation
    of each available property is provided in the ['AWS Lambda invoke' action YAML](lam-invoke-action-ref.md "lam-invoke-action-ref.md").
11. (Optional) Choose **Validate** to validate the workflow's YAML
    code before committing.
12. Choose **Commit**, enter a commit message, and choose
    **Commit** again.
