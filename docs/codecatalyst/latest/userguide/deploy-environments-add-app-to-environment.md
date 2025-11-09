Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Associating an environment with

an action

When you associate an environment with a [supported workflow action](deploy-environments.md#deploy-environments-supported "deploy-environments.md#deploy-environments-supported"), the environment's AWS account, default IAM role, and
optional Amazon VPC become assigned to the action. The action can then connect and deploy to the
AWS account using the IAM role, and also connect to the optional Amazon VPC.

Use the following instructions to associate an environment with an action.

## Step 1: Associate the

environment with a workflow action

Use the following procedure to associate an environment with a workflow action.

Visual

###### To associate an

environment with a workflow action using the visual editor

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. Choose your project.
3. In the navigation pane, choose **CI/CD**, and then choose **Workflows**.
4. Choose the name of your workflow. You can filter by the source repository or
   branch name where the workflow is defined, or filter by workflow name or
   status.
5. Choose **Edit**.
6. Choose **Visual**.
7. In the workflow diagram, choose an action that is supported with environments.
   For more information, see [Which actions support having their
   deployment information displayed in CodeCatalyst?](deploy-environments.md#deploy-environments-supported-targets "deploy-environments.md#deploy-environments-supported-targets").
8. Choose the **Configuration** tab, and specify information in
   the **Environment** field, as follows.

**Environment**

Specify the CodeCatalyst environment to use with the action. The action connects to
the AWS account and optional Amazon VPC specified in the chosen environment. The action uses the
default IAM role specified in the environment to connect to the AWS account, and uses the
IAM role specified in the [Amazon VPC connection](../adminguide/managing-vpcs.md "../adminguide/managing-vpcs.md") to
connect to the Amazon VPC.

###### Note

If the default IAM role does not have the permissions required by the action, you can
configure the action to use a different role. For more information, see [Changing the IAM role of an action](deploy-environments-switch-role.md "deploy-environments-switch-role.md").

For more information about environments, see [Deploying into AWS accounts and VPCs](deploy-environments.md "deploy-environments.md") and [Creating an environment](deploy-environments-creating-environment.md "deploy-environments-creating-environment.md"). 9. (Optional) Change the IAM role associated with the action. You might want to
change the role if it contains the wrong set of permissions for the action.

To change the role:

    1. In the **What's in `my-environment`
     ?** box, and choose the vertical ellipsis icon (
    ![Ellipsis.](images/flows/elipsis.png)
    ).
    2. Choose one of the following:




    	* **Switch role**. Choose this option to change the IAM
    	 role used by this action, and only this action. Other actions continue to
    	 use the default IAM role specified in their associated environment. For
    	 more information, see [Changing the IAM role of an action](deploy-environments-switch-role.md "deploy-environments-switch-role.md").
    	* **Edit environment**. Choose this option to change the
    	 default IAM role listed in your environment. When you choose this
    	 option, your action—and any other action associated with the same
    	 environment—begins using the new default IAM role.


    	###### Important

    	Use caution when updating the default IAM role. Changing the role
    	 might lead to action failures if the permissions in the role are not
    	 sufficient for all actions that share the environment.

10. (Optional) Choose **Validate** to validate the workflow's
    YAML code before committing.
11. Choose **Commit**, enter a commit message, and choose
    **Commit** again.

YAML

###### To associate an environment with a workflow action using the YAML

editor

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. Choose your project.
3. In the navigation pane, choose **CI/CD**, and then choose **Workflows**.
4. Choose the name of your workflow. You can filter by the source repository or
   branch name where the workflow is defined, or filter by workflow name or
   status.
5. Choose **Edit**.
6. Choose **YAML**.
7. In the workflow action that you want to associate with an environment, add
   code similar to the following:

```
`action-name`:
  Environment:
    Name: `environment-name`
```

For more information, see the [Action types](workflows-actions.md#workflows-actions-types "workflows-actions.md#workflows-actions-types") topic. This topic has links into the
documentation for each action, including its YAML reference. 8. (Optional) If you want the action to use a different role from the default
IAM role that's listed in the environment, add a `Connections:`
section that includes the role you want to use. For more information, see [Changing the IAM role of an action](deploy-environments-switch-role.md "deploy-environments-switch-role.md"). 9. (Optional) Choose **Validate** to validate the workflow's
YAML code before committing. 10. Choose **Commit**, enter a commit message, and choose
**Commit** again.

## Step 2:

Populate the deployment activity page

After associating an environment with a workflow action, you can populate the
**Deployment activity** and **Deployment target** pages
in the **Environments** section of the CodeCatalyst console with deployment
information. Use the following instructions to populate these pages.

###### Note

Only a few actions support having their deployment information displayed in the CodeCatalyst
console. For more information, see [Which actions support having their
deployment information displayed in CodeCatalyst?](deploy-environments.md#deploy-environments-supported-targets "deploy-environments.md#deploy-environments-supported-targets").

###### To add deployment information to CodeCatalyst

1. If a workflow run did not start automatically when you committed your changes in
   [Step 1: Associate the
   environment with a workflow action](#deploy-environments-add-app-to-environment-assoc "#deploy-environments-add-app-to-environment-assoc"), manually start a
   run as follows:
   1. In the navigation pane, choose **CI/CD**, and then choose **Workflows**.
   2. Choose the name of your workflow. You can filter by the source repository or
      branch name where the workflow is defined, or filter by workflow name or
      status.
   3. Choose **Run**.The workflow run starts a new deployment, which causes CodeCatalyst to add deployment
      information to CodeCatalyst.

2. Verify that deployment activity was added to the CodeCatalyst console:
   1. In the navigation pane, choose **CI/CD**, and then choose
      **Environments**.
   2. Choose your environment (for example, `Production`).
   3. Choose the **Deployment activity** tab, and verify that a
      deployment appears with a **Status** of
      **SUCCEEDED**. This indicates that a workflow run successfully
      deployed your application resources.
   4. Choose the **Deployment targets** tab, and verify that your
      application resources appear.
