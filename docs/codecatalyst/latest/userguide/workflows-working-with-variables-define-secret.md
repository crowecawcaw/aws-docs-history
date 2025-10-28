Amazon CodeCatalyst will no longer be open to new customers starting on November
7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For
more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Defining a secret

You define a secret on the **Secrets** page of the CodeCatalyst
console. For more information, see [Masking data using secrets](workflows-secrets.md "workflows-secrets.md").

For example, you might define a secret that looks like this:

- Name (key): `my-password`
- Value: `^*H3#!b9`
  After the secret is defined, you can specify the secret's key
  (`my-password`) in the workflow definition file. For an
  example of how to do this, see [Example:
  Referencing a secret](workflows-working-with-variables-ex.md#workflows-working-with-variables-ex-refer-secret "workflows-working-with-variables-ex.md#workflows-working-with-variables-ex-refer-secret").
