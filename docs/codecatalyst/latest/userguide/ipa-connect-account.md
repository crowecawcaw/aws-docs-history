Amazon CodeCatalyst will no longer be open to new customers starting on November
7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For
more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Allowing access to AWS resources with connected

AWS accounts

You
can use resources from your AWS accounts in Amazon CodeCatalyst
spaces. To do so, you must set up a connection between the
AWS accounts and your space in CodeCatalyst. Creating a connection like this means that
projects and workflows within your CodeCatalyst space can interact with resources in your
AWS accounts. You must create one connection for each AWS account you want
to use with your CodeCatalyst space.

After you create a connection, you can choose to associate AWS IAM roles with
it.

###### Topics

- [Adding an AWS account to a
  space](ipa-connect-account-create.md "ipa-connect-account-create.md")
- [Adding IAM roles to account
  connections](ipa-connect-account-addroles.md "ipa-connect-account-addroles.md")
- [Adding the account connection and
  IAM roles to your deploy environment](ipa-connect-account-addroles-env.md "ipa-connect-account-addroles-env.md")
- [Viewing account connections](ipa-connect-account-list.md "ipa-connect-account-list.md")
- [Deleting account connections (in
  CodeCatalyst)](ipa-connect-account-delete.md "ipa-connect-account-delete.md")
- [Configuring a billing account for a
  space](connect-account-billing-ref.md "connect-account-billing-ref.md")
  You can set up CodeCatalyst to use authorized AWS accounts by adding the accounts to your
  space. By adding AWS accounts to your CodeCatalyst space, you can give your project
  workflows access to AWS account resources and your billing configuration.

Adding an AWS account creates a connection that authorizes CodeCatalyst to use this account.
You can use added AWS accounts to do the following:

- Set up billing for a CodeCatalyst space. See [Managing billing](../adminguide/managing-billing.md "../adminguide/managing-billing.md") in the Amazon CodeCatalyst Administrator Guide. The
  AWS account that is specified as the billing account for your CodeCatalyst space
  has different quotas from other account connections for a space. For more
  information, see [Quotas for CodeCatalyst](quotas.md "quotas.md").
- Allow CodeCatalyst to assume IAM roles to access AWS resources and deploy to
  AWS services in the account. See [Configuring IAM roles for connected accounts](spaces-manage-roles.md "spaces-manage-roles.md").
  Account connections are created by completing authorization with the AWS account. After the connection is created, you further configure the
  connection for workflows and projects to use by adding IAM roles.

For the steps to configure account connections in the AWS Management Console page for CodeCatalyst as the
administrator for the AWS account and the space, see [Managing connected
accounts](../adminguide/managing-billing.md "../adminguide/managing-billing.md") in the _CodeCatalyst Administrator Guide_.
Account connections can be configured for restriction to specific projects. You can only
associate workflows or VPC connections with an AWS account that has access to your
project. For more information, see [Configuring project-restricted account connections](../adminguide/managing-accounts.md#managing-accounts-restriction "../adminguide/managing-accounts.md#managing-accounts-restriction").
