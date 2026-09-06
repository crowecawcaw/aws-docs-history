

Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md).

# Using a secret
<a name="workflows-secrets.using"></a>

To use a secret in a workflow action, you must obtain the reference identifier of the secret and use that identifier in the workflow action.

**Topics**
+ [Obtaining the identifier of a secret](#workflows-using-secrets.get-identifier)
+ [Referencing a secret in a workflow](#workflows-using-secrets.using-identifier)

## Obtaining the identifier of a secret
<a name="workflows-using-secrets.get-identifier"></a>

Use the following procedure to obtain the reference identifier of the secret. You'll add this identifier to your workflow.

**To obtain the reference identifier of the secret**

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/).

1. In the navigation pane, choose **CI/CD**, and then choose **Secrets**.

1. In the list of secrets, find the secret that you want to use.

1. In the **Reference ID** column, copy the identifier of the secret. The following is the syntax for the **Reference ID**:

   ```
   ${Secrets.{{<name>}}}
   ```

## Referencing a secret in a workflow
<a name="workflows-using-secrets.using-identifier"></a>

Use the following procedure to reference a secret in a workflow.

**To reference a secret**

1. In the navigation pane, choose **CI/CD**, and then choose **Workflows**.

1. Choose the name of your workflow. You can filter by the source repository or branch name where the workflow is defined, or filter by workflow name or status.

1. Choose **Edit**.

1. Choose **YAML**.

1. Modify the YAML to use the identifier of the secret. For example, to use a user name and password that are stored as secrets with the `curl` command, you would use a `Run` command similar to the following:

   ```
   - Run: curl -u {{<username-secret-identifier>}}:{{<password-secret-identifier>}} https://example.com
   ```

1. (Optional) Choose **Validate** to validate the workflow's YAML code before committing.

1. Choose **Commit**, enter a commit message, and choose **Commit** again.