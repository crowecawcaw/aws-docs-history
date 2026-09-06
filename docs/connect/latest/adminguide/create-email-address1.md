

# Create email addresses
<a name="create-email-address1"></a>

This topic explains how to create email addresses by using the Connect Customer admin website. You can create email addresses that customers can reply to, as well as outbound only (no-reply) email addresses.

For a list of the APIs used to create and manage email addresses programmatically, see [APIs to create and manage email addresses](#apis-manage-email-addresses1). 

You can create up to 100 email addresses. 

**To create email addresses**

1. Log in to the Connect Customer admin website at https://{{instance name}}.my.connect.aws/. Use an admin account, or an account with **Channels and Flows** - **Email addresses** - **Create** permission in it's security profile.

1. On the navigation menu, choose **Channels**, **Email addresses**.

1. Choose a domain from the dropdown list. The list contains the auto-generated domain that was created when you enabled the email channel for your instance. It might also display up to five custom domains if you added them. 

1. Under **Additional information**, you can optionally add the following: 
   + **Friendly sender name**
   + **Description**: This is for your use, not customer facing.
   + **Flow**: Choose a published flow for sending emails. Leave this blank for the email address to be used only for outbound communication. Customers will not be able to reply to it.
**Tip**  
To create **No-reply** email addresses, that is, addresses that are only used for outbound mail, and cannot accept a reply don't select a flow to be used for the email address.

1. Under **Tags**, optionally add [tags](tagging.md) to manage who can view and access email addresses in Connect Customer and the agent workspace.

1. Choose **Create**.

## APIs to create and manage email addresses
<a name="apis-manage-email-addresses1"></a>

For a list of all email address APIs, see [Email actions](https://docs.aws.amazon.com/connect/latest/APIReference/email-api.html) in the *Connect Customer API Reference Guide*.

Use the following APIs to create addresses programmatically:
+ [CreateEmailAddress](https://docs.aws.amazon.com/connect/latest/APIReference/API_CreateEmailAddress.html)
+ [DescribeEmailAddress](https://docs.aws.amazon.com/connect/latest/APIReference/API_DescribeEmailAddress.html)
+ [UpdateEmailAddressMetadata](https://docs.aws.amazon.com/connect/latest/APIReference/API_UpdateEmailAddressMetadata.html)