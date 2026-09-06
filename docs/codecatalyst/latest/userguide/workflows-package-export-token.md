

Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md).

# Using authorization tokens in workflow actions
<a name="workflows-package-export-token"></a>

You can use a token provided by the workflow action to manually configure a package manager to authenticate with CodeCatalyst package repositories. CodeCatalyst makes this token available as an environment variable for you to reference in your actions.


| Environment variable | Value | 
| --- | --- | 
| CATALYST\_MACHINE\_RESOURCE\_NAME | The user identity of the authorization token. | 
| CATALYST\_PACKAGES\_AUTHORIZATION\_TOKEN | The value of the authorization token. | 

**Note**  
Note that these environment variables will only be populated if you have configured your action to export the authorization token.

Use the following instructions to use an authorization token with a workflow action.

------
#### [ Visual ]

**To use an exported authorization token with an action (visual editor)**

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/).

1. Choose your project.

1. In the navigation pane, choose **CI/CD**, and then choose **Workflows**.

1. Choose the name of your workflow. You can filter by the source repository or branch name where the workflow is defined, or filter by workflow name or status.

1. Choose **Edit**.

1. Choose **Visual**.

1. In the workflow diagram, choose the **Build** or **Test** action with which you want to configure with a package repository.

1. Choose **Packages**.

1. Turn on **Export authorization token**.

------
#### [ YAML ]

**To use an exported authorization token with an action (YAML editor)**

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/).

1. Choose your project.

1. In the navigation pane, choose **CI/CD**, and then choose **Workflows**.

1. Choose the name of your workflow. You can filter by the source repository or branch name where the workflow is defined, or filter by workflow name or status.

1. Choose **Edit**.

1. Choose **YAML**.

1. In a **Build** or **Test** action, add code similar to the following:

   ```
   Actions:
     {{action-name}}:
       Packages:
         ExportAuthorizationToken: true
   ```

   You can reference the `$CATALYST_MACHINE_RESOURCE_NAME` and `$CATALYST_PACKAGES_AUTHORIZATION_TOKEN` environment variables in the `Steps` section of your YAML. For more information, refer to [Example: Manually configuring `pip` to authenticate with CodeCatalyst](workflows-working-packages-ex.md#workflows-working-packages-pypi-token).

1. (Optional) Choose **Validate** to validate the workflow's YAML code before committing.

1. Choose **Commit**, enter a commit message, and choose **Commit** again.

------