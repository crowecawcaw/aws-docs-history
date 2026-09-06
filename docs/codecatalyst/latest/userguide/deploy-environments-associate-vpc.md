

Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md).

# Associating a VPC with an environment
<a name="deploy-environments-associate-vpc"></a>

When an action is configured with an environment that has a VPC connection, the action will run connected to the VPC, adhering to the network rules and access resources specified by the associated VPC. The same VPC connection can be used by one or more environments.

Use the following instructions to associate a VPC connection with an environment.

**To associate a VPC connection with an environment**

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/).

1. Choose your project.

1. In the navigation pane, choose **CI/CD**, and then choose **Environments**.

1. Choose your environment (for example, `Production`).

1. Choose the **Environment properties** tab.

1. Choose **Manage VPC connection**, choose your desired VPC connection, and choose **Confirm**. This associates your selected VPC connection with this environment.
**Note**  
If the VPC connection that you want to use is not listed, it might be because it includes an AWS account connection that's not allowed in your project. For more information, see [Configuring project-restricted account connections](https://docs.aws.amazon.com/codecatalyst/latest/adminguide/managing-accounts-restriction.html) in the *Amazon CodeCatalyst Administrator Guide*.

For more information, see [ Managing Amazon Virtual Private Clouds](https://docs.aws.amazon.com/codecatalyst/latest/adminguide/managing-vpcs.html) in the *CodeCatalyst Administrator Guide*.