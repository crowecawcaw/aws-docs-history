# Create email addresses

This topic explains how to create email addresses by using the Amazon Connect admin website. You can create
email addresses that customers can reply to, as well as outbound only (no-reply) email
addresses.

For a list of the APIs used to create and manage email addresses programmatically, see
[APIs to create and manage email
addresses](#apis-manage-email-addresses1 "#apis-manage-email-addresses1").

You can create up to 100 email addresses.

###### To create email addresses

1. Log in to the Amazon Connect admin website at https://`instance
name`.my.connect.aws/. Use an admin account, or an account with
   **Channels and Flows** - **Email
   addresses** - **Create** permission in it's
   security profile.
2. On the navigation menu, choose **Channels**, **Email
   addresses**.
3. Choose a domain from the dropdown list. The list contains the auto-generated
   domain that was created when you enabled the email channel for your instance. It
   may also display up to five custom domains if you added them.
4. Under **Additional information**, you can optionally add the
   following:
   - **Friendly sender name**
   - **Description**: This is for your use, not customer
     facing.
   - **Flow**: Choose a published flow for sending emails.
     Leave this blank for the email address to be used only for outbound
     communication. Customers will not be able to reply to it.

   ###### Tip

   To create **No-reply** email
   addresses, that is, addresses that are only used for outbound mail,
   and cannot accept a reply don't select a flow to be used for the
   email address.

5. Under **Tags**, optionally add [tags](tagging.md "tagging.md") to manage who can view and access email addresses in Amazon Connect and
   the agent workspace.
6. Choose **Create**.

## APIs to create and manage email

addresses

For a list of all email address APIs, see [Email actions](../APIReference/email-api.md "../APIReference/email-api.md") in the
_Amazon Connect API Reference Guide_.

Use the following APIs to create addresses programmatically:

- [CreateEmailAddress](../APIReference/API_CreateEmailAddress.md "../APIReference/API_CreateEmailAddress.md")
- [DescribeEmailAddress](../APIReference/API_DescribeEmailAddress.md "../APIReference/API_DescribeEmailAddress.md")
- [UpdateEmailAddressMetadata](../APIReference/API_UpdateEmailAddressMetadata.md "../APIReference/API_UpdateEmailAddressMetadata.md")
