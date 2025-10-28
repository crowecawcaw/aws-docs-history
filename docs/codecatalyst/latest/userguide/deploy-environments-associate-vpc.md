Amazon CodeCatalyst will no longer be open to new customers starting on November
7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For
more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Associating a VPC with an

environment

When an action is configured with an environment that has a VPC connection, the action
will run connected to the VPC, adhering to the network rules and access resources specified by
the associated VPC. The same VPC connection can be used by one or more environments.

Use the following instructions to associate a VPC connection with an environment.

###### To associate a VPC connection with an environment

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. Choose your project.
3. In the navigation pane, choose **CI/CD**, and then choose **Environments**.
4. Choose your environment (for example, `Production`).
5. Choose the **Environment properties** tab.
6. Choose **Manage VPC connection**, choose your desired VPC connection,
   and choose **Confirm**. This associates your selected VPC connection with
   this environment.

###### Note

If the VPC connection that you want to use is not listed, it might be because it
includes an AWS account connection that's not allowed in your project. For more
information, see [Configuring
project-restricted account connections](../adminguide/managing-accounts-restriction.md "../adminguide/managing-accounts-restriction.md") in the _Amazon CodeCatalyst
Administrator Guide_.
For more information, see [Managing Amazon Virtual Private Clouds](../adminguide/managing-vpcs.md "../adminguide/managing-vpcs.md") in the
_CodeCatalyst Administrator Guide_.
