Amazon CodeCatalyst will no longer be open to new customers starting on November
7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For
more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Using user-defined variables

_User-defined variables_ are key-value pairs that you define. There
are two types:

- **Plaintext variables**, or simply **variables** – These are key-value pairs that you
  define in plaintext within the workflow definition file.
- **Secrets** – These are key-value pairs
  that you define on a separate **Secrets** page of the
  Amazon CodeCatalyst console. The _key_ (name) is a public label, and
  the _value_ contains the information you want to keep
  private. You only specify the key in the workflow definition file. Use secrets
  in place of passwords and other sensitive information in the workflow definition
  file.

###### Note

For brevity, this guide uses the term _variable_ to mean
_plaintext variable_.

For more information about variables, see [Using variables in workflows](workflows-working-with-variables.md "workflows-working-with-variables.md").

###### Topics

- [Examples of
  variables](workflows-working-with-variables-ex.md "workflows-working-with-variables-ex.md")
- [Defining a
  variable](workflows-working-with-variables-define-input.md "workflows-working-with-variables-define-input.md")
- [Defining a secret](workflows-working-with-variables-define-secret.md "workflows-working-with-variables-define-secret.md")
- [Exporting a variable
  so that other actions can use it](workflows-working-with-variables-export-input.md "workflows-working-with-variables-export-input.md")
- [Referencing a
  variable in the action that defines it](workflows-working-with-variables-reference-input.md "workflows-working-with-variables-reference-input.md")
- [Referencing a
  variable output by another action](workflows-working-with-variables-reference-action.md "workflows-working-with-variables-reference-action.md")
- [Referencing a
  secret](workflows-working-with-variables-reference-secret.md "workflows-working-with-variables-reference-secret.md")
