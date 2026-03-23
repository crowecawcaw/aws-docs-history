Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Deleting a secret

Use the following procedure to delete a secret and the secret reference
identifier.

###### Note

Before deleting a secret, we recommend that you remove the secret's reference
identifier from all workflow actions. If you delete the secret without deleting the
reference identifier, the action will fail the next time it runs.

###### To delete a secret's reference identifier from a workflow

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. In the navigation pane, choose **CI/CD**, and then choose **Workflows**.
3. Choose the name of your workflow. You can filter by the source
   repository or branch name where the workflow is defined, or filter
   by workflow name or status.
4. Choose **Edit**.
5. Choose **YAML**.
6. Search the workflow for the following string:

```
${Secrets.
```

This finds all reference identifiers of all secrets. 7. Delete the reference identifier of the chosen secret, or replace it with a
plaintext value. 8. (Optional) Choose **Validate** to validate the workflow's
YAML code before committing. 9. Choose **Commit**, enter a commit message, and choose
**Commit** again.

###### To delete a secret

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. In the navigation pane, choose **CI/CD**, and then choose
   **Secrets**.
3. In the secrets list, choose the secret you want to delete.
4. Choose **Delete**.
5. Enter `delete` to confirm the deletion.
6. Choose **Delete**.
