Amazon CodeCatalyst will no longer be open to new customers starting on November
7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For
more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Changing the IAM role of an action

By default, when you associate an [environment](deploy-environments.md "deploy-environments.md")
with a workflow [action](workflows-actions.md "workflows-actions.md"), the action inherits the
default IAM role specified in the environment. You can change this behavior so that the
action uses a different role. You might want an action to use a different role if the default
IAM role is missing the permissions that the action needs to operate in the AWS
cloud.

To assign a different IAM role to an action, you can use the **Switch
role** option in the visual editor or the `Connections:` property in the
YAML editor. The new role overrides the default IAM role specified in the environment,
allowing you to keep the default IAM role as-is. You might want to keep the default IAM
role as-is if there are other actions that use it.

Use the following instructions to configure an action to use a different IAM role from
the one specified in its environment.

Visual

###### To assign a different IAM role to an action (visual editor)

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. Choose your project.
3. In the navigation pane, choose **CI/CD**, and then choose **Workflows**.
4. Choose the name of your workflow. You can filter by the source repository or
   branch name where the workflow is defined, or filter by workflow name or
   status.
5. Choose **Edit**.
6. Choose the box that represents the action whose IAM role you want to
   update.
7. Choose the **Configuration** tab.
8. In the **What's in `my-environment`
   ?** box, choose the vertical ellipsis icon (
   ![Ellipsis.](images/flows/elipsis.png)
   ).
9. Choose **Switch role**.
10. In the **Switch role** dialog box, in the **IAM
    role** drop-down list, choose the IAM role that you want the action to
    use. This role will override the default IAM role in the environment. If the role
    you want to use is not in the list, make sure you've added it to your space. For
    more information, see [Adding IAM roles to account
    connections](ipa-connect-account-addroles.md "ipa-connect-account-addroles.md").

The chosen role now appears in the **What's in
`my-environment`?** box along with a
**Defined in workflow** badge. The role also appears in the
workflow definition file, in the `Connections:` section. 11. (Optional) Choose **Validate** to validate the workflow's YAML
code before committing. 12. Choose **Commit**, enter a commit message, and choose
**Commit** again.

YAML

###### To assign a different IAM role to an action (YAML editor)

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. Choose your project.
3. In the navigation pane, choose **CI/CD**, and then choose **Workflows**.
4. Choose the name of your workflow. You can filter by the source repository or
   branch name where the workflow is defined, or filter by workflow name or
   status.
5. Choose **Edit**.
6. Choose **YAML**.
7. In the workflow action where you want to use a different IAM role, add a
   `Connections:` section, similar to the following:

```
`action-name`:
  Environment:
    Name: `environment-name`
    **Connections:
 - Name: `account-connection-name`
 Role: `iam-role-name`**
```

In the preceding code, replace
`account-connection-name` with the name of the [account connection](ipa-connect-account.md "ipa-connect-account.md") that contains the IAM
role, and replace `iam-role-name` with the name of the
IAM role that you want the action to use. This role will override the default
IAM role in the environment. Make sure you've added the role to your space. For
more information, see [Adding IAM roles to account
connections](ipa-connect-account-addroles.md "ipa-connect-account-addroles.md").

For more information, see the [Action types](workflows-actions.md#workflows-actions-types "workflows-actions.md#workflows-actions-types") topic. This topic has links into the
documentation for each action, including its YAML reference.
