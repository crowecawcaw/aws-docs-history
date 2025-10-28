Amazon CodeCatalyst will no longer be open to new customers starting on November
7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For
more information, see [Migrating from Amazon CodeCatalyst](../userguide/migration.md "../userguide/migration.md").

# Configure an existing CodeCatalyst space

for identity federation

You must have the **Space administrator** role and access to the billing
account for the space in order to view SSO users and groups for your space.

You must have completed the prerequisities in AWS Organizations and IAM Identity Center for a space. The space
can only support members that are managed as federated identities in IAM Identity Center.

You cannot directly add or remove users in your space in CodeCatalyst. You must work with
your Identity federation administrator to manage SSO users and groups in IAM Identity Center. CodeCatalyst syncs
with the IAM Identity Center on a regular basis to update your space members.

###### Important

After a space is updated to SSO and associated with an Identity Center application, it
is an enabled space in CodeCatalyst for SSO. The space will no longer support AWS Builder ID users.
This action cannot be undone, and you can't change the space back to an AWS Builder ID space
later.

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. Choose **Settings**, and then choose **SSO**.
3. On the **SSO not enabled** message, choose **Set up in
   AWS**. The wizard page opens for creating a space. To complete the
   wizard, see the steps in [Creating a space for identity
   federation](setting-up-federation-space-create.md "setting-up-federation-space-create.md").

To view information in IAM Identity Center, choose **IAM Identity Center**. You will be taken to
IAM Identity Center, where you can work with your Identity federation administrator to configure SSO
users and groups for your instance in IAM Identity Center.
