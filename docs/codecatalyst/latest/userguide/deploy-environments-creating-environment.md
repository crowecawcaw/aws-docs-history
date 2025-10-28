Amazon CodeCatalyst will no longer be open to new customers starting on November
7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For
more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Creating an environment

Use the following instructions to create an environment that you can later associate with
a workflow action.

###### Before you begin

You need the following:

- A CodeCatalyst space. For more information, see [Set up and sign in to CodeCatalyst](setting-up-topnode.md "setting-up-topnode.md").
- A CodeCatalyst project. For more information, see [Creating a project with a
  blueprint](projects-create.md#projects-create-console-template "projects-create.md#projects-create-console-template").
- An AWS account connection that includes the IAM roles your workflow action will
  need to access AWS. For information about creating an account connection, see [Allowing access to AWS resources with connected
  AWS accounts](ipa-connect-account.md "ipa-connect-account.md"). You can use a
  maximum of one account connection per environment.

###### Note

You can create an environment without an account connection; however, you will need
to come back and add the connection later.

- One of the following CodeCatalyst roles:
  - **Space administrator**
  - **Project administrator**
  - **Contributor**

  ###### Note

  If you have the **Contributor role**, you'll be able to
  create an environment but you won't be able to associate it with an AWS account
  connection. You'll need to ask someone with the
  **Space administrator** or **Project administrator**
  role to associate the environment with an AWS account connection.
  For more information about permissions and roles, see [Granting users project permissions](projects-members.md "projects-members.md").

###### To create an environment

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. Choose your project.
3. In the navigation pane, choose **CI/CD**, and then choose **Environments**.
4. In **Environment name**, enter a name, such as
   `Production` or `Staging`.
5. In **Environment type**, select one of the following:
   - **Non-production** – An environment where you can test
     your application to make sure it's working as intended before moving it into
     production.
   - **Production** – A 'live' environment that is
     publicly-available and hosts your finalized application.

   If you choose **Production**, a **Production**
   badge appears in the UI next to any actions that the environment is associated with.
   The badge helps you quickly see which actions are deploying to production. Other than
   the appearance of the badge, there are no differences between production and
   non-production environments.

6. (Optional) In **Description**, enter a description such as
   `Production environment for the hello-world app`.
7. In **AWS account connection - optional**, choose the AWS account
   connection you want to associate with this environment. Workflow actions that are assigned
   this environment will be able to connect to the associated AWS account. For more
   information about creating AWS account connections in CodeCatalyst, see [Allowing access to AWS resources with connected
   AWS accounts](ipa-connect-account.md "ipa-connect-account.md").

If the AWS account connection that you want to use is not listed, it might be
because it's not allowed in your project. For more information, see [Configuring
project-restricted account connections](../adminguide/managing-accounts-restriction.md "../adminguide/managing-accounts-restriction.md") in the _Amazon CodeCatalyst Administrator
Guide_. 8. In **Default IAM role**, choose the IAM role you want to
associate with this environment. Workflow actions that are assigned this environment will
inherit this IAM role, and will be able to use it to connect to services and resources
in your AWS account.

If you need to assign the environment to multiple actions, and those actions need
IAM roles that are different from the default one specified here, then you can specify
the different roles on each action's **Configuration** tab, using the
**Switch role** option. For more information, see [Changing the IAM role of an action](deploy-environments-switch-role.md "deploy-environments-switch-role.md").

If the IAM role that you want to use as the default is not listed, it might be
because you have not added it to your AWS account connection yet. To add an IAM role
to an account connection, see [Adding IAM roles to account
connections](ipa-connect-account-addroles.md "ipa-connect-account-addroles.md"). 9. (Optional) In **VPC connection**, choose a VPC connection that you
want to associate with this environment. For more information about creating VPC
connections, see [Managing Amazon Virtual Private Clouds](../adminguide/managing-vpcs.md "../adminguide/managing-vpcs.md") in
the _Amazon CodeCatalyst Administrator Guide_.

If the VPC connection that you want to use is not listed, it might be because it
includes an AWS account connection that's not allowed in your project. For more
information, see [Configuring
project-restricted account connections](../adminguide/managing-accounts-restriction.md "../adminguide/managing-accounts-restriction.md") in the _Amazon CodeCatalyst Administrator
Guide_. 10. Choose **Create environment**. CodeCatalyst creates an empty
environment.

###### Next steps

- Now that you have created an environment, you are ready to associate it with a
  workflow action. For more information, see [Associating an environment with
  an action](deploy-environments-add-app-to-environment.md "deploy-environments-add-app-to-environment.md").
