

AWS Chatbot is now Amazon Q Developer. [Learn more](service-rename.md)

# Managing user roles as a channel member in Amazon Q Developer in chat applications
<a name="cm-container"></a>

Channel members can switch their user roles from their chat channels. Additionally, channel members can unmap user roles from chat client IDs using the Amazon Q Developer in chat applications console.

**Topics**
+ [Adding a user role from a chat channel using Amazon Q Developer in chat applications](#cm-add-role)
+ [Switching user roles from a chat channel using Amazon Q Developer in chat applications](#cm-switch-role)
+ [Unmapping a user role using Amazon Q Developer in chat applications](#cm-unmap-role)

## Adding a user role from a chat channel using Amazon Q Developer in chat applications
<a name="cm-add-role"></a>

If you are a new channel member or your channel permission approach changes, Amazon Q Developer in chat applications will prompt you to add a user role.

**To add a user role from a chat channel**

1. Choose **Let's get started**.

1. Choose an account to add a role.
**Note**  
This link will take you directly to the Amazon Q Developer in chat applications console.

1. In **User role**, choose a role.

1. Choose **Save**.
**Note**  
 Choosing **Save** takes you to an authorization page to fetch your chat client identity. This identity is mapped to your chosen role.

1. Choose **Allow**.

## Switching user roles from a chat channel using Amazon Q Developer in chat applications
<a name="cm-switch-role"></a>

If you find that your current user role doesn’t have the right permissions to achieve your desired task, you can switch roles directly from Microsoft Teams and Slack.

**Note**  
If you are unable to run a particular command after switching roles, contact your administrator regarding the channel guardrails in place.

**To switch a user role from a chat channel**

1. In your chat channel, enter `@Amazon Q switch-role`.

1. Choose the account that you want to switch roles for.
**Note**  
This link will take you directly to the Amazon Q Developer in chat applications console.

1. In the Amazon Q Developer in chat applications console, choose **Choose user role**.

1. In **User role**, choose a user role.

1. Choose **Save**.
**Note**  
Choosing **Save**, takes you to an authorization page. This is so your chat client identity can be retrieved and associated with your chosen role.

1. On the authorization page, choose **Allow**.

## Unmapping a user role using Amazon Q Developer in chat applications
<a name="cm-unmap-role"></a>

If you have a user role applied that you no longer need, you can unmap it.

**To unmap a user role**

1. Open the [Amazon Q Developer in chat applications console](https://console.aws.amazon.com/chatbot/).

1. Choose a configured client.

1. In **User role**, choose **Clear role**.