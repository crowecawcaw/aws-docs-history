Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Masking data using secrets

There may be times when you need to use sensitive data, such as authentication
credentials, in your workflows. Storing these values in plaintext anywhere in your
repository should be avoided because anyone with access to the repository which contains the
secret can see them. Similarly, these values shouldn't be used directly in any workflow
definitions because they will be visible as files in your repository. With CodeCatalyst, you can
protect these values by adding a secret to your project, and then referencing the secret in
your workflow definition file. Note that you can have a maximum of five secrets per
action.

###### Note

Secrets can only be used to replace passwords and sensitive information in the
workflow definition file.

###### Topics

- [Creating a secret](workflows-secrets.md "workflows-secrets.md")
- [Editing a secret](workflows-secrets.md "workflows-secrets.md")
- [Using a secret](workflows-secrets.md "workflows-secrets.md")
- [Deleting a secret](workflows-secrets.md "workflows-secrets.md")
