Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Adding the 'AWS CDK bootstrap' action

Use the following instructions to add the **AWS CDK bootstrap** action to
your workflow.

**Before you begin**

Before you can use the **AWS CDK bootstrap** action, make sure you have an
AWS CDK app ready. The bootstrap action will synthesize the AWS CDK app before bootstrapping. You
can write your app in any programming language supported by the AWS CDK.

Make sure your AWS CDK app files are available in:

- A CodeCatalyst [source repository](source.md "source.md"), or
- A CodeCatalyst [output artifact](workflows-working-artifacts.md "workflows-working-artifacts.md") generated
  by another workflow action

Visual

###### To add the 'AWS CDK bootstrap' action using the visual editor

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
9. Search for the **AWS CDK bootstrap** action, and do one of the
   following:
   - Choose the plus sign (**+**) to add the action to the
     workflow diagram and open its configuration pane.

   Or
   - Choose **AWS CDK bootstrap**. The action details dialog box
     appears. On this dialog box:
     - (Optional) Choose **View source** to [view the action's source
       code](workflows-view-source.md#workflows-view-source.title "workflows-view-source.md#workflows-view-source.title").
     - Choose **Add to workflow** to add the action to the
       workflow diagram and open its configuration pane.

10. In the **Inputs**, **Configuration**, and
    **Outputs** tabs, complete the fields according to your needs.
    For a description of each field, see the ['AWS CDK bootstrap' action YAML](cdk-boot-action-ref.md "cdk-boot-action-ref.md"). This reference provides detailed
    information about each field (and corresponding YAML property value) as it appears
    in both the YAML and visual editors.
11. (Optional) Choose **Validate** to validate the workflow's YAML
    code before committing.
12. Choose **Commit**, enter a commit message, and then choose
    **Commit** again.

###### Note

If your **AWS CDK bootstrap** action fails with an `npm
 install` error, see [How do I fix "npm install"
errors?](troubleshooting-workflows.md#troubleshooting-workflows-npm "troubleshooting-workflows.md#troubleshooting-workflows-npm") for information about how to fix
the error.

YAML

###### To add the 'AWS CDK bootstrap' action using the YAML editor

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
9. Search for the **AWS CDK bootstrap** action, and choose
   **+** to add it to the workflow diagram and open its
   configuration pane.
10. Modify the properties in the YAML code according to your needs. An explanation
    of each available property is provided in the ['AWS CDK bootstrap' action YAML](cdk-boot-action-ref.md "cdk-boot-action-ref.md").
11. (Optional) Choose **Validate** to validate the workflow's YAML
    code before committing.
12. Choose **Commit**, enter a commit message, and then choose
    **Commit** again.

###### Note

If your **AWS CDK bootstrap** action fails with an `npm
 install` error, see [How do I fix "npm install"
errors?](troubleshooting-workflows.md#troubleshooting-workflows-npm "troubleshooting-workflows.md#troubleshooting-workflows-npm") for information about how to fix
the error.
