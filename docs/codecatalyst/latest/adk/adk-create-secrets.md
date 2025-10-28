# Creating secrets

As a developer, you might have API keys, secrets, or tokens. You can create secrets to use sensitive data in your workflows. The action is the
main building block of a CodeCatalyst workflow and used by the workflow to integrate the action within the workflow itself. values shouldn't be used
directly in any workflow definitions because they will be visible as files in your repository. With CodeCatalyst, you can protect these values by
adding a secret to your project, and then referencing the secret in your workflow definition file. For more
information, see [Creating a secret](../userguide/workflows-secrets.md#workflows-secrets.creating "../userguide/workflows-secrets.md#workflows-secrets.creating"). To
learn more about workflows and actions, see [Working with workflows](../userguide/working-with-workflows.md "../userguide/working-with-workflows.md") and [Working with actions](../userguide/workflows-actions.md "../userguide/workflows-actions.md").

## Example: Creating AWS access key and ID

In this example, two secrets are created: AWS access key ID and an AWS secret access key that will be passed to the action.

**To create secrets**

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. In the navigation pane, choose **CI/CD**, and then choose **Secrets**.
3. Choose **Create secret**.
4. Enter the following information:

For **Name**, enter _AWS_ACCESS_KEY_ID_. This is the name for your secret.

For **Value**, enter _AWS Access Key ID_. Enter the value for the secret. This is the
sensitive information that you want to hide from view. By default, the value is not displayed. To display the value, choose
**Show value**.

(Optional) For **Description**, enter a description for your secret. 5. Choose **Create**. The secret can later be accessed using the reference ID
(`$(Secrets.AWS_SECRET_ACCESS_KEY)`). 6. Choose **Create secret** to create a second secret. 7. Enter the following information:

For **Name**, enter _AWS_ACCESS_KEY_. This is the name for your secret.

For **Value**, enter _AWS Secrets Access Key_. Enter the value for the secret. This is
the sensitive information that you want to hide from view. By default, the value is not displayed. To display the value, choose
**Show value**.

(Optional) For **Description**, enter a description for your secret. 8. Choose **Create**. The secret can later be accessed using the reference ID
(`$(Secrets.AWS_SECRET_ACCESS_KEY)`).
