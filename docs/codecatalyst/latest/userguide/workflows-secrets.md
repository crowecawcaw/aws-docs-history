Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Using a secret

To use a secret in a workflow action, you must obtain the reference identifier of the
secret and use that identifier in the workflow action.

###### Topics

- [Obtaining the identifier of
  a secret](#workflows-using-secrets.get-identifier "#workflows-using-secrets.get-identifier")
- [Referencing a secret in a
  workflow](#workflows-using-secrets.using-identifier "#workflows-using-secrets.using-identifier")

## Obtaining the identifier of

a secret

Use the following procedure to obtain the reference identifier of the secret.
You'll add this identifier to your workflow.

###### To obtain the reference identifier of the secret

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. In the navigation pane, choose **CI/CD**, and then choose
   **Secrets**.
3. In the list of secrets, find the secret that you want to use.
4. In the **Reference ID** column, copy the identifier of
   the secret. The following is the syntax for the **Reference
   ID**:

```
${Secrets.`<name>`}
```

## Referencing a secret in a

workflow

Use the following procedure to reference a secret in a workflow.

###### To reference a secret

1. In the navigation pane, choose **CI/CD**, and then choose **Workflows**.
2. Choose the name of your workflow. You can filter by the source
   repository or branch name where the workflow is defined, or filter
   by workflow name or status.
3. Choose **Edit**.
4. Choose **YAML**.
5. Modify the YAML to use the identifier of the secret. For example, to use a
   user name and password that are stored as secrets with the `curl`
   command, you would use a `Run` command similar to the
   following:

```
- Run: curl -u `<username-secret-identifier>`:`<password-secret-identifier>` https://example.com
```

6. (Optional) Choose **Validate** to validate the workflow's
   YAML code before committing.
7. Choose **Commit**, enter a commit message, and choose
   **Commit** again.
