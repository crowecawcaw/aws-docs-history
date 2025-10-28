Amazon CodeCatalyst will no longer be open to new customers starting on November
7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For
more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Associating an AWS account with an

environment

Use the following instructions to associate an AWS account with an environment. When you
associate an AWS account with an environment, workflow actions that are assigned the
environment will be able to connect to the AWS account.

For more information about account connections, see [Allowing access to AWS resources with connected
AWS accounts](ipa-connect-account.md "ipa-connect-account.md").

###### Before you begin

You need the following:

- An AWS account connection that includes the IAM roles your workflow action will
  need to access AWS. For information about creating an account connection, see [Allowing access to AWS resources with connected
  AWS accounts](ipa-connect-account.md "ipa-connect-account.md"). You can use a
  maximum of one account connection per environment.
- One of the following CodeCatalyst roles: **Space administrator** or
  **Project administrator**. For more information, see [Granting users project permissions](projects-members.md "projects-members.md").

###### To associate an AWS account with an environment

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. Choose your project.
3. In the navigation pane, choose **CI/CD**, and then choose **Environments**.
4. Choose your environment (for example, `Production`).
5. Choose **Edit environment**.
6. Under **Environment properties**, in the **AWS account
   connection - optional** drop-down list, choose your desired
   AWS account.

If the AWS account connection that you want to use is not listed, it might be
because it's not allowed in your project. For more information, see [Configuring
project-restricted account connections](../adminguide/managing-accounts-restriction.md "../adminguide/managing-accounts-restriction.md") in the _Amazon CodeCatalyst Administrator
Guide_. 7. In **Default IAM role**, choose the IAM role you want to
associate with this environment. Workflow actions that are assigned this environment will
inherit this IAM role, and will be able to use it to connect to services and resources
in your AWS account.

If the IAM role that you want to use as the default is not listed, it might be
because you have not added it to your AWS account connection yet. To add an IAM role
to an account connection, see [Adding IAM roles to account
connections](ipa-connect-account-addroles.md "ipa-connect-account-addroles.md").
