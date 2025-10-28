Amazon CodeCatalyst will no longer be open to new customers starting on November
7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For
more information, see [Migrating from Amazon CodeCatalyst](../userguide/migration.md "../userguide/migration.md").

# Administering connected accounts

To access resources in AWS related to your projects in CodeCatalyst, you must connect an
AWS account to your space. The connected account can also be used as the billing account for
the space if you choose to use a paid tier.

To do so, you must set up a connection between the AWS accounts and your space in
CodeCatalyst. Creating a connection like this means that projects and workflows within your CodeCatalyst
space can interact with resources in your AWS accounts. You must create one connection
for each AWS account you want to use with your CodeCatalyst space.

After you create a connection, you can choose to associate AWS IAM roles with it.

Here is one possible flow for adding an AWS account in CodeCatalyst:

Li Juan has the Project administrator role in a CodeCatalyst project with a workflow that
builds and deploys the application to AWS infrastructure in the cloud. To deploy to the AWS
infrastructure, CodeCatalyst must use an authorized AWS account to access the AWS resources for
the build action in the workflow. Li Juan works with Mary Major, who has
the **Space administrator** role, and Mateo Jackson, who has AWS
administrator permissions in the AWS account to create a connection between the space and
the AWS account. Before creating the connection, Mateo Jackson creates an IAM role in
that account called `codecatalyst-build-role` with the IAM permissions policy for
the AWS Cloud Development Kit (AWS CDK) stack he wants to use to build the application in the AWS account.

As the next step, Mary Major edits the CodeCatalyst space settings, completes an
authorization flow with Mateo Jackson, and adds the AWS account and role to the list of
AWS accounts and roles available for the CodeCatalyst space. Li Juan uses the CodeCatalyst
environments page to add the account and role to the environment for his CodeCatalyst project.
Li Juan also adds the role Amazon Resource Name (ARN) to the `Role` field
for the CodeCatalyst workflow YAML.

For steps for managing accounts in the CodeCatalyst console, see [Account
connections](../userguide/ipa-connect-account.md "../userguide/ipa-connect-account.md") in the CodeCatalyst User Guide.

###### Topics

- [Adding an account connection for a space (in AWS)](#w6aac29c21 "#w6aac29c21")
- [Removing an account from a space (in
  AWS)](managing-accounts-remove.md "managing-accounts-remove.md")
- [Tagging account connections](managing-accounts-tag.md "managing-accounts-tag.md")
- [Enabling or disabling project-restricted account
  connections](managing-accounts-restriction.md "managing-accounts-restriction.md")

## Adding an account connection for a space (in AWS)

For steps for managing accounts in the CodeCatalyst console, see [Account
connections](../userguide/ipa-connect-account.md "../userguide/ipa-connect-account.md") in the CodeCatalyst User Guide.

For a space that supports AWS Builder ID users, the space requires that you specify a
connected account to the be the billing account for the space. For a space that supports
identity federation, the space billing account will default to the management account
associated with the organization in AWS Organizations.
