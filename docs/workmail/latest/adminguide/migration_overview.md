# Migrating to Amazon WorkMail

You can migrate to Amazon WorkMail from Microsoft Exchange, Microsoft Office 365, G Suite
Basic (formerly Google Apps for Work), and other platforms by working with one of our
partners.
For more information about our partners, see [Amazon WorkMail Features](https://aws.amazon.com/workmail/features/ "https://aws.amazon.com/workmail/features/").

###### Topics

- [Step 1: Create or enable users in Amazon WorkMail](#create_enable_users "#create_enable_users")
- [Step 2: Migrate to Amazon WorkMail](#prepare_mail_server "#prepare_mail_server")
- [Step 3: Complete the migration to Amazon WorkMail](#complete_migration "#complete_migration")

## Step 1: Create or enable users in Amazon WorkMail

Before you migrate your users, you must add those users in Amazon WorkMail to provision their
mailbox. For more information, see [Adding a user](add_user.md "add_user.md").

## Step 2: Migrate to Amazon WorkMail

You can work with any AWS migration partners to migrate to Amazon WorkMail. For information
about these providers, see [Amazon WorkMail
features](https://aws.amazon.com/workmail/features/ "https://aws.amazon.com/workmail/features/").

To migrate your mailboxes, create a dedicated Amazon WorkMail user to act as a migration
administrator. The following procedure grants permission to that user to access all
of the mailboxes in your organization.

###### To create a migration administrator

1. Do one of the following:
   - In the Amazon WorkMail console, create a new user to act as migration administrator. For more information, see
     [Adding a user](add_user.md "add_user.md").
   - In your Active Directory, create a new user to act as migration administrator, and then enable the user for Amazon WorkMail. For more information,
     see [Enabling users](enable_user.md "enable_user.md").

2. In the Amazon WorkMail console navigation pane, choose **Organizations**, and then choose the name of your organization.
3. Choose **Organization settings**, choose **Migration**, and then **Edit**.
4. Move the **Migration enabled** slider to the on position.
5. Open the **Migration administrator** and select a user.
6. Choose **Save**.

## Step 3: Complete the migration to Amazon WorkMail

After you migrate your email accounts to Amazon WorkMail, you can verify your DNS records and
configure your desktop and mobile clients.

###### To complete migration to Amazon WorkMail

1. Verify that all DNS records are updated and that they point to Amazon WorkMail. For more
   information about the required DNS records, see [Adding a domain](add_domain.md "add_domain.md").

###### Note

The DNS record update process can take several hours. If any new items
appear in a source mailbox while the MX records are being changed, run
the migration tool again to migrate new items after the DNS records are
updated. 2. For more information about configuring your desktop or mobile clients to
use Amazon WorkMail, see [Connect
Microsoft Outlook to your Amazon WorkMail account](../userguide/connect_mail_client.md "../userguide/connect_mail_client.md") in the
_Amazon WorkMail User Guide_.
