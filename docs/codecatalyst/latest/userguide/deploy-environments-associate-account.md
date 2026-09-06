

Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md).

# Associating an AWS account with an environment
<a name="deploy-environments-associate-account"></a>

Use the following instructions to associate an AWS account with an environment. When you associate an AWS account with an environment, workflow actions that are assigned the environment will be able to connect to the AWS account.

For more information about account connections, see [Allowing access to AWS resources with connected AWS accounts](ipa-connect-account.md).

**Before you begin**

You need the following:
+ An AWS account connection that includes the IAM roles your workflow action will need to access AWS. For information about creating an account connection, see [Allowing access to AWS resources with connected AWS accounts](ipa-connect-account.md). You can use a maximum of one account connection per environment.
+ One of the following CodeCatalyst roles: **Space administrator** or **Project administrator**. For more information, see [Granting users project permissions](projects-members.md).

**To associate an AWS account with an environment**

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/).

1. Choose your project.

1. In the navigation pane, choose **CI/CD**, and then choose **Environments**.

1. Choose your environment (for example, `Production`).

1. Choose **Edit environment**.

1. Under **Environment properties**, in the **AWS account connection - optional** drop-down list, choose your desired AWS account.

   If the AWS account connection that you want to use is not listed, it might be because it's not allowed in your project. For more information, see [Configuring project-restricted account connections](https://docs.aws.amazon.com/codecatalyst/latest/adminguide/managing-accounts-restriction.html) in the *Amazon CodeCatalyst Administrator Guide*.

1. In **Default IAM role**, choose the IAM role you want to associate with this environment. Workflow actions that are assigned this environment will inherit this IAM role, and will be able to use it to connect to services and resources in your AWS account.

   If the IAM role that you want to use as the default is not listed, it might be because you have not added it to your AWS account connection yet. To add an IAM role to an account connection, see [Adding IAM roles to account connections](ipa-connect-account-addroles.md).