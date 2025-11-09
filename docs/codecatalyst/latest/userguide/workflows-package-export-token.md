Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Using authorization tokens in workflow

actions

You can use a token provided by the workflow action to manually configure a package
manager to authenticate with CodeCatalyst package repositories. CodeCatalyst makes this token
available as an environment variable for you to reference in your actions.

| Environment variable                  | Value                                         |
| ------------------------------------- | --------------------------------------------- |
| CATALYST_MACHINE_RESOURCE_NAME        | The user identity of the authorization token. |
| CATALYST_PACKAGES_AUTHORIZATION_TOKEN | The value of the authorization token.         |

###### Note

Note that these environment variables will only be populated if you have
configured your action to export the authorization token.

Use the following instructions to use an authorization token with a workflow
action.

Visual

###### To use an exported authorization token with an action (visual

editor)

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. Choose your project.
3. In the navigation pane, choose **CI/CD**, and then choose **Workflows**.
4. Choose the name of your workflow. You can filter by the source
   repository or branch name where the workflow is defined, or filter
   by workflow name or status.
5. Choose **Edit**.
6. Choose **Visual**.
7. In the workflow diagram, choose the **Build** or
   **Test** action with which you want to
   configure with a package repository.
8. Choose **Packages**.
9. Turn on **Export authorization token**.

YAML

###### To use an exported authorization token with an action (YAML

editor)

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. Choose your project.
3. In the navigation pane, choose **CI/CD**, and then choose **Workflows**.
4. Choose the name of your workflow. You can filter by the source
   repository or branch name where the workflow is defined, or filter
   by workflow name or status.
5. Choose **Edit**.
6. Choose **YAML**.
7. In a **Build** or **Test**
   action, add code similar to the following:

```
Actions:
  `action-name`:
    Packages:
      ExportAuthorizationToken: true
```

You can reference the `$CATALYST_MACHINE_RESOURCE_NAME`
and `$CATALYST_PACKAGES_AUTHORIZATION_TOKEN` environment
variables in the `Steps` section of your YAML. For more
information, refer to [Example: Manually
configuring pip to authenticate with CodeCatalyst](workflows-working-packages-ex.md#workflows-working-packages-pypi-token "workflows-working-packages-ex.md#workflows-working-packages-pypi-token"). 8. (Optional) Choose **Validate** to validate the
workflow's YAML code before committing. 9. Choose **Commit**, enter a commit message, and
choose **Commit** again.
