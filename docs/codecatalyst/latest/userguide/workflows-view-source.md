Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Viewing an action's source code

You can view an action's source code to make sure it doesn't contain risky code,
security vulnerabilities, or other defects.

Use the following instructions to view the source code of a [CodeCatalyst](workflows-actions.md#workflows-actions-types-cc "workflows-actions.md#workflows-actions-types-cc"), [CodeCatalyst Labs](workflows-actions.md#workflows-actions-types-cc-labs "workflows-actions.md#workflows-actions-types-cc-labs"), or [third-party](workflows-actions.md#workflows-actions-types-3p "workflows-actions.md#workflows-actions-types-3p") action.

###### Note

To view the source code of a [GitHub
Action](workflows-actions.md#workflows-actions-types-github "workflows-actions.md#workflows-actions-types-github"), go to the action's page in the [GitHub Marketplace](https://github.com/marketplace/actions "https://github.com/marketplace/actions").
The page includes a link to the action's repository, where you can find the action's
source code.

###### Note

You cannot view the source code of the following CodeCatalyst actions: [build](build-workflow-actions.md "build-workflow-actions.md"), [test](test-workflow-actions.md "test-workflow-actions.md"), [GitHub Actions](integrations-github-action-add.md "integrations-github-action-add.md").

###### Note

AWS does not support or guarantee the action code of GitHub Actions or
third-party actions.

###### To view an action's source code

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. Choose your project.
3. Find the action whose code you want to view:
   1. In the navigation pane, choose **CI/CD**, and then choose **Workflows**.
   2. Choose the name of any workflow, or create one. For information about
      creating a workflow, see [Creating a workflow](workflows-create-workflow.md "workflows-create-workflow.md").
   3. Choose **Edit**.
   4. At the top-left, choose **+ Actions** to open the
      action catalog.
   5. In the drop-down list, choose **Amazon CodeCatalyst** to view
      CodeCatalyst, CodeCatalyst Labs, and third-party actions.
   6. Search for an action, and choose its name. Do not choose the plus sign
      (**+**).

   Details about the action appear.

4. In the action details dialog box, near the bottom, choose
   **Download**.

A page appears, showing the Amazon S3 bucket where the action's source code
resides. For information about Amazon S3, see [What is Amazon S3?](../../../AmazonS3/latest/userguide/Welcome.md "../../../AmazonS3/latest/userguide/Welcome.md") in the
_Amazon Simple Storage Service User Guide_. 5. Inspect the code to ensure it meets your expectations for quality and
security.
