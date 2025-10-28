Amazon CodeCatalyst will no longer be open to new customers starting on November
7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For
more information, see [Migrating from Amazon CodeCatalyst](../userguide/migration.md "../userguide/migration.md").

# Administering spaces that support identity

federation

You can manage your space in CodeCatalyst after you have set up the space for identity
federation.

This guide includes information about administrator tasks for managing spaces in CodeCatalyst
that support identity federation.

For information about the following tasks for managing AWS Builder ID spaces, see the
_CodeCatalyst User Guide_:

- Add other space administrators to the space for an AWS Builder ID
  space
- Change member roles and permissions for an AWS Builder ID space
- Create projects and add members to the project
- View a list of all projects in the space
- View the activity feed for all projects in the space
- Invite users for a AWS Builder ID space
  For the steps to set up a CodeCatalyst space without identity federation, an AWS Builder ID
  space, see [Setting up
  CodeCatalyst](../userguide/setting-up-topnode.md "../userguide/setting-up-topnode.md") in the _Amazon CodeCatalyst User Guide_.

If you have not already connected the AWS account that will be the specified billing
account for your space and set up your identity provider in IAM Identity Center, complete the
prerequisites and create your first space as detailed in [Prerequisite 3: Setting up identity federation in
IAM Identity Center](setting-up-federation.md#setting-up-prereq-identity "setting-up-federation.md#setting-up-prereq-identity") and [Creating a space for identity
federation](setting-up-federation-space-create.md "setting-up-federation-space-create.md"). You work with your Identity federation
administrator and AWS account administrator to configure and enable your identity provider
(IdP). The AWS account that is specified as the billing account for your CodeCatalyst space has
different quotas from other account connections for a space. For more information, see
[Quotas](../userguide/quotas.md "../userguide/quotas.md") in
the _CodeCatalyst User Guide_.

###### Important

Dev Environments aren't available for users in spaces where Active Directory is used as
the identity provider. When planning a space where the identity provider will be Active
Directory, note that users will not be able to use Dev Environments. For more information, see
[I can't create a Dev Environment when I'm signed into CodeCatalyst using a single sign-on
account](../userguide/devenvironments-troubleshooting.md#troubleshoot-create-dev-env-idprovider "../userguide/devenvironments-troubleshooting.md#troubleshoot-create-dev-env-idprovider").
