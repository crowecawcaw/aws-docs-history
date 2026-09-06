

Amazon CodeCatalyst will no longer be open to new customers starting on November 7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For more information, see [Migrating from Amazon CodeCatalyst](https://docs.aws.amazon.com/codecatalyst/latest/userguide/migration.html).

# Administering spaces that support identity federation
<a name="managing-federation-space"></a>

You can manage your space in CodeCatalyst after you have set up the space for identity federation. 

This guide includes information about administrator tasks for managing spaces in CodeCatalyst that support identity federation. 

For information about the following tasks for managing AWS Builder ID spaces, see the *CodeCatalyst User Guide*:
+ Add other space administrators to the space for an AWS Builder ID space
+ Change member roles and permissions for an AWS Builder ID space
+ Create projects and add members to the project
+ View a list of all projects in the space
+ View the activity feed for all projects in the space
+ Invite users for a AWS Builder ID space

For the steps to set up a CodeCatalyst space without identity federation, an AWS Builder ID space, see [Setting up CodeCatalyst](https://docs.aws.amazon.com//codecatalyst/latest/userguide/setting-up-topnode.html) in the * Amazon CodeCatalyst User Guide*.

If you have not already connected the AWS account that will be the specified billing account for your space and set up your identity provider in IAM Identity Center, complete the prerequisites and create your first space as detailed in [Prerequisite 3: Setting up identity federation in IAM Identity Center](setting-up-federation.md#setting-up-prereq-identity) and [Creating a space for identity federation](setting-up-federation-space-create.md). You work with your Identity federation administrator and AWS account administrator to configure and enable your identity provider (IdP). The AWS account that is specified as the billing account for your CodeCatalyst space has different quotas from other account connections for a space. For more information, see [Quotas](https://docs.aws.amazon.com/codecatalyst/latest/userguide/quotas.html) in the *CodeCatalyst User Guide*.

**Important**  
Dev Environments aren't available for users in spaces where Active Directory is used as the identity provider. When planning a space where the identity provider will be Active Directory, note that users will not be able to use Dev Environments. For more information, see [I can't create a Dev Environment when I'm signed into CodeCatalyst using a single sign-on account](https://docs.aws.amazon.com/codecatalyst/latest/userguide/devenvironments-troubleshooting.html#troubleshoot-create-dev-env-idprovider).