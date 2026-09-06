

Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md).

# Using user-defined variables
<a name="workflows-using-variables"></a>

*User-defined variables* are key-value pairs that you define. There are two types:
+ **Plaintext variables**, or simply **variables** – These are key-value pairs that you define in plaintext within the workflow definition file.
+ **Secrets** – These are key-value pairs that you define on a separate **Secrets** page of the Amazon CodeCatalyst console. The *key* (name) is a public label, and the *value* contains the information you want to keep private. You only specify the key in the workflow definition file. Use secrets in place of passwords and other sensitive information in the workflow definition file.

**Note**  
For brevity, this guide uses the term *variable* to mean *plaintext variable*.

For more information about variables, see [Using variables in workflows](workflows-working-with-variables.md).

**Topics**
+ [Examples of variables](workflows-working-with-variables-ex.md)
+ [Defining a variable](workflows-working-with-variables-define-input.md)
+ [Defining a secret](workflows-working-with-variables-define-secret.md)
+ [Exporting a variable so that other actions can use it](workflows-working-with-variables-export-input.md)
+ [Referencing a variable in the action that defines it](workflows-working-with-variables-reference-input.md)
+ [Referencing a variable output by another action](workflows-working-with-variables-reference-action.md)
+ [Referencing a secret](workflows-working-with-variables-reference-secret.md)