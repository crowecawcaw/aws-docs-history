

Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md).

# Creating a secret
<a name="workflows-secrets.creating"></a>

Use the following procedure to create a secret. The secret contains the sensitive information that you want to hide from view.

**Note**  
Secrets are visible to actions and are not masked when written to a file.

**To create a secret**

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/).

1. In the navigation pane, choose **CI/CD**, and then choose **Secrets**.

1. Choose **Create secret**.

1. Enter the following information:  
**Name**  
Enter a name for your secret.  
**Value**  
Enter the value for the secret. This is the sensitive information that you want to hide from view. By default, the value is not displayed. To display the value, choose **Show value**.  
**Description**  
(Optional) Enter a description for your secret.

1. Choose **Create**.