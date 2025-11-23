# Creating an organization

To use Amazon WorkMail, you must first create an organization. One AWS account can have
multiple Amazon WorkMail organizations. When you create an organization, you also select a domain
for the organization and set up user directory and encryption settings.

You can create a new Amazon WorkMail directory for use with your WorkMail organization, or
integrate Amazon WorkMail with an existing directory. You can use Amazon WorkMail with existing directories of
the following types:

- on-premises Microsoft Active Directory
- AWS Managed Active Directory (which is a [Microsoft AD managed by AWS Directory Service](../../../directoryservice/latest/admin-guide/directory_microsoft_ad.md "../../../directoryservice/latest/admin-guide/directory_microsoft_ad.md"))
- Simple AD
  By integrating with your on-premises directory, you can use your existing users and
  groups in Amazon WorkMail and users can sign in with their existing credentials. If you’re using an
  on-premises directory, you must first set up an AD Connector in AWS Directory Service. The
  AD Connector synchronizes your users and groups with the Amazon WorkMail address book and
  performs user authentication requests. For more information, see [Active
  Directory Connector](../../../directoryservice/latest/admin-guide/directory_ad_connector.md "../../../directoryservice/latest/admin-guide/directory_ad_connector.md") in the _Directory Service Administration
  Guide_.

You also have the option of selecting a

AWS KMS key that Amazon WorkMail uses to encrypt the mailbox content. You can
either select the default AWS managed master key for Amazon WorkMail, or use an existing
KMS key in AWS Key Management Service (AWS KMS). For information about creating a new KMS key, see
[Creating keys](../../../kms/latest/developerguide/create-keys.md "../../../kms/latest/developerguide/create-keys.md") in the _AWS Key Management Service Developer Guide_. If you are
signed in as an AWS Identity and Access Management (IAM) user, make yourself a key administrator on the
KMS key. For more information, see [Enabling and disabling
keys](../../../kms/latest/developerguide/enabling-keys.md "../../../kms/latest/developerguide/enabling-keys.md") in the _AWS Key Management Service Developer Guide_.

###### Considerations

Remember the following when creating an Amazon WorkMail organization:

- Amazon WorkMail doesn't currently support managed Microsoft Active Directory services
  that you share with multiple accounts.
- If you have an on-premises Active Directory with Microsoft Exchange and an
  AD Connector, we recommend configuring interoperability settings for your
  organization. This allows you to minimize disruption to your users as you
  migrate mailboxes to Amazon WorkMail, or use Amazon WorkMail for a subset of your corporate mailboxes.
  For more information, see [Interoperability between Amazon WorkMail and Microsoft Exchange](interoperability.md "interoperability.md").
- If you select the **Free test domain** option, you can start
  using your Amazon WorkMail organization with the provided test domain. The test domain uses
  this format: `example`.awsapps.com. You can
  use the test mail domain with Amazon WorkMail and other supported AWS services as long as
  you maintain enabled users in your Amazon WorkMail organization. However, you can't use the
  test domain for other purposes. The test domain might become available for
  registration and use by other customers if your Amazon WorkMail organization does not
  maintain at least one enabled user.
- Amazon WorkMail does not support multi-Region directories.
- Amazon WorkMail synchronizes directory data with AWS Managed Active Directory,
  Simple AD and AD Connector every four hours.

## Important changes for using AWS Managed Active

Directory

Amazon WorkMail is updating its authorization model for organizations that use AWS Managed
Active Directory (Managed AD). This change affects how Amazon WorkMail interacts with directory
data and requires you to take specific actions to ensure continued
functionality.

Previously, when an Amazon WorkMail organization was created with AWS Managed Active
Directory, Amazon WorkMail used service-level permissions to interact with the Managed AD. To
provide additional flexibility for customers to separate directory management and
mailbox administration roles, WorkMail’s APIs and console will now use AWS Directory
Service Data (DS-Data) APIs to create or update users and groups in AWS Managed
Active Directories. An IAM principal executing these operations through the WorkMail
console or APIs will also need authorization to use the equivalent DS-Data actions
against the Managed AD associated with their WorkMail organization, providing more
granular control and better integration with IAM policies.

Whether you create a new organization with Managed AD, or have an existing
organization that uses Managed AD, if you wish to continue being able to create,
update, or delete users and groups through the WorkMail console or APIs, you will
have to complete additional configuration steps to ensure proper functionality with
the updated authorization model. This is explained in [Configuring AWS Managed Active
Directory integration](#configure-managed-ad-integration "#configure-managed-ad-integration").

###### Topics

- [Creating an organization](#create-organization "#create-organization")
- [Configuring AWS Managed Active
  Directory integration](#configure-managed-ad-integration "#configure-managed-ad-integration")
- [Viewing an organization's details](#view-org-details "#view-org-details")
- [Integrating a WorkSpaces directory](#compatible "#compatible")
- [Organization states and descriptions](#org-states "#org-states")

## Creating an organization

Create a new organization in the Amazon WorkMail console.

###### To create an organization

1. Open the Amazon WorkMail console at
   [https://console.aws.amazon.com/workmail/](https://console.aws.amazon.com/workmail/ "https://console.aws.amazon.com/workmail/").

If necessary, change the AWS Region. In the bar at the top of the
console window, open the **Select a
Region** list and choose a
Region. For more information, see [Region and endpoints](../../../general/latest/gr/rande.md "../../../general/latest/gr/rande.md") in
the _Amazon Web Services General Reference_. 2. In the navigation bar, select **Organization**.

The **Organizations** page appears and displays your
organizations, if any. 3. Choose **Create organization**. 4. Under **Email domain**, select the domain to use for the
email addresses in your organization:

    * **Existing Route 53
     domain** – Select an existing domain
     that you manage with an Amazon Route 53 (Route 53) hosted zone.
    * **New Route 53
     domain** – Register a new Route 53 domain
     name to use with Amazon WorkMail.
    * **External
     domain** – Enter an existing domain
     that you manage with an external domain name system (DNS)
     provider.
    * **Free test
     domain** – Use a free test domain
     provided by Amazon WorkMail. You can explore Amazon WorkMail using a test domain, and
     then add a domain to your organization later.

5. (Optional) If your domain is managed through Amazon Route 53, for
   **Route 53 hosted zone**, select your Route 53 domain.
6. For **Alias**, enter a unique alias for your
   organization.
7. Choose **Advanced settings**, and for **User
   directory**, select one of the following options:
   - Create new Amazon WorkMail directory –
     Creates a new directory for adding and managing your users.
   - Use existing directory –
     Uses an existing directory to manage your users, such as an
     on-premises Microsoft Active Directory, AWS Managed Active
     Directory, or Simple AD.

8. For **Encryption**, select one of the following
   options:
   - Use an Amazon WorkMail managed key –
     Creates a new encryption key in your account.
   - Use existing KMS key –
     Uses an existing KMS key that you have already created in
     AWS KMS.

9. Choose **Create organization**.

If you use an external domain, verify it by adding the appropriate text (TXT) and
mail exchanger (MX) records to your DNS service. TXT records allow you to enter
notes about the DNS service. MX records specify the incoming mail server.

Be sure to set your domain as the default for your organization. For more
information, see [Verifying domains](domain_verification.md "domain_verification.md") and [Choosing the default domain](default_domain.md "default_domain.md").

When your organization is **Active**, you can add users to it and
set up their email clients. For more information, see [Adding a user](add_user.md "add_user.md") and [Setting up email clients for
Amazon WorkMail](../userguide/clients.md "../userguide/clients.md").

## Configuring AWS Managed Active

Directory integration

When using AWS Managed Active Directory with your Amazon WorkMail organization, additional
configuration steps ensure proper functionality with the updated authorization
model.

###### To configure Managed AD integration for new organizations

1. In the Directory Service console, navigate to your Managed AD (Microsoft AD), or from
   the Amazon WorkMail console, select **Users** or
   **Groups** in the left navigation panel, and then click
   the directory link in the note box at the top of the page.
2. Choose **Enable** for **User and group
   management**. This setting is disabled by default and must be
   enabled to perform write operations on users and groups.
3. Ensure your IAM principal has the required permissions by attaching a
   policy with these actions:

```
ds:AccessDSData
ds:ResetUserPassword
ds-data:CreateGroup
ds-data:DeleteGroup
ds-data:AddGroupMember
ds-data:RemoveGroupMember
ds-data:CreateUser
ds-data:DeleteUser
ds-data:UpdateUser
```

###### To migrate existing Managed AD organizations

1. Monitor the Users or Groups page in the Amazon WorkMail console for migration
   notifications.
2. When the notification appears, toggle on **Enable updated
   directory operations** to migrate to the new Directory Service
   APIs.
3. Finally, ensure that you have enabled **User and group
   management** in the Directory Service console and have updated your IAM
   policies with the required DS-Data permissions as described in the previous
   section.

The use of AWS Directory Service Data (DS-Data) APIs for creating, updating, and
deleting users will be enabled for any remaining Amazon WorkMail organizations using Managed AD
where this has not previously been enabled.

## Viewing an organization's details

Each of your Amazon WorkMail organizations can display an the organization details page. The
page shows you information about their organization, including IDs that you can use
with the AWS Command Line Interface. Messages on the page can also show you any steps needed to
finish setting up and organization, such as an unverified domain or a lack of users.
The messages also provide the first step that you follow to set up a given email
client.

###### To view organization details

1. In the navigation bar, choose **Organization**.

The **Organizations** page appears and displays your
organizations. 2. Choose the organization that you want to view.

## Integrating a WorkSpaces directory

To use Amazon WorkMail with WorkSpaces, create a compatible directory by using the following
steps.

###### To add a compatible WorkSpaces directory

1. Create a compatible directory using WorkSpaces. For WorkSpaces instructions, see
   [Get started with
   Amazon WorkSpaces Quick Setup](../../../workspaces/latest/adminguide/getting-started.md "../../../workspaces/latest/adminguide/getting-started.md") in the
   _Amazon WorkSpaces Administration Guide_.
2. In the Amazon WorkMail console, create your Amazon WorkMail organization and choose to use your
   existing directory for it. For more information, see [Creating an organization](#create-organization "#create-organization").

## Organization states and descriptions

After you create an organization, it can have one of the following states.

| **State**      | Description                                                                      |
| -------------- | -------------------------------------------------------------------------------- |
| **Active**     | Your organization is healthy and ready for use.                                  |
| **Creating**   | A workflow is running to create your organization.                               |
| **Failed**     | Your organization could not be created.                                          |
| **Impaired**   | Your organization is malfunctioning or an issue has been<br>detected.            |
| **Inactive**   | Your organization is inactive.                                                   |
| **Requested**  | Your organization creation request is in the queue and waiting<br>to be created. |
| **Validating** | All settings for the organization are being<br>health-checked.                   |
