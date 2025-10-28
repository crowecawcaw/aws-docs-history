# Amazon Q Developer Pro Region support

Region information for the Pro tier varies depending on whether you're an end-user with a
personal account (Builder ID), or you're an administrator of IAM Identity Center workforce users.

## Personal account (Builder ID) users

If you're the owner of a personal account (Builder ID), your Pro tier subscription is supported
in the following Region:

- US East (N. Virginia)

## IAM Identity Center workforce users

Read this section if you're an administrator of IAM Identity Center workforce users.

###### Topics

- [IAM Identity Center Regions supported by Amazon Q Developer](#pro-subscription-regions "#pro-subscription-regions")
- [Supported Regions for the Q Developer
  console and Q Developer profile](#qdev-console-and-profile-regions "#qdev-console-and-profile-regions")
- [Subscribing users to Amazon Q Developer Pro across AWS Regions](#subscribe-multi-region "#subscribe-multi-region")

### IAM Identity Center Regions supported by Amazon Q Developer

The workforce users that you want to subscribe to Amazon Q Developer Pro must have identities in an
IAM Identity Center instance (or a connected identity provider) in one of the Regions listed on the
[Supported Regions
page](regions.md#default-regions "regions.md#default-regions"), except for opt-in Regions. If your users have identities in an IAM Identity Center
instance in an opt-in Region, they can't be subscribed, which means they will only have
access to the Free tier [in the AWS Management Console, and on AWS apps and
websites](q-on-aws.md "q-on-aws.md"), and they won’t have access to Amazon Q in the IDE or at the command
line.

Amazon Q stores the subscriptions of IAM Identity Center workforce users in the same Region as your IAM Identity Center
instance.

Regardless of the IAM Identity Center Region, data is stored in the Region where you create the
Amazon Q Developer profile.

For more information about Amazon Q Developer profiles, see [What is the Amazon Q Developer profile?](subscribe-understanding-profile.md "subscribe-understanding-profile.md").

For more information about data protection, see [Data protection in Amazon Q Developer](data-protection.md "data-protection.md").

### Supported Regions for the Q Developer

console and Q Developer profile

The **Amazon Q Developer console** and **Amazon Q Developer profile** are supported in the following Regions:

- US East (N. Virginia)
- Europe (Frankfurt)

For more information about the Amazon Q Developer profile, see [What is the Amazon Q Developer profile?](subscribe-understanding-profile.md "subscribe-understanding-profile.md").

###### Note

The following features aren’t supported for Q Developer profiles created in the
Europe (Frankfurt) Region:

- [Chatting with Support](support-chat.md "support-chat.md")
- [Troubleshooting resources with
  Amazon Q](chat-actions-troubleshooting.md "chat-actions-troubleshooting.md")
- [.NET transformations in the
  IDE](transform-dotnet-IDE.md "transform-dotnet-IDE.md")
- [Amazon Q in chat applications (for
  Slack)](q-in-chat-applications.md "q-in-chat-applications.md")
- Amazon Q in the AWS Console Mobile Application
- [GitLab Duo with Amazon Q](gitlab-with-amazon-q.md "gitlab-with-amazon-q.md")
- [Amazon Q for GitHub](amazon-q-for-github.md "amazon-q-for-github.md")

### Subscribing users to Amazon Q Developer Pro across AWS Regions

When you subscribe an IAM Identity Center workforce user to Amazon Q Developer Pro, you might need to work in two different AWS
Regions:

- One Region for the IAM Identity Center instance (where user identities are managed, and where
  subscriptions are stored)
- Another Region for the Amazon Q Developer console (where the [Amazon Q Developer profile](subscribe-understanding-profile.md "subscribe-understanding-profile.md"), customizations, and
  subscriptions are managed)

The Regions are not always the same because the Amazon Q Developer console is supported in fewer Regions than
IAM Identity Center.

In a scenario where your IAM Identity Center is in a different Region from your Amazon Q Developer console, use the
guidance in the following example to subscribe users.

#### Example subscription process in a multi-Region

scenario

Let's walk through subscribing a user where:

- The IAM Identity Center instance is in **US West (N. California)**.
- The Amazon Q Developer console is in **US East (N. Virginia)**. This
  is the closest Region to the IAM Identity Center instance that the Amazon Q Developer console supports.

###### To subscribe the user

1. Add the user in your IAM Identity Center instance in **US West (N. California)**.
2. Switch to the Amazon Q Developer console in the **US East (N. Virginia)**.
3. Subscribe the user through the Amazon Q Developer console in **US East (N. Virginia)**.

Upon being subscribed:

- The user's subscription is created in **US West (N. California)**.
- The user's subscription is associated with their user entry in **US West (N. California)**.
- The user's subscription is associated with the Amazon Q Developer profile in **US East (N. Virginia)**.

Additionally, any data that Amazon Q Developer needs to store on the user's behalf will be stored in
**US East (N. Virginia)**. For more information about data storage
and security, see [Encryption at rest](data-encryption.md#encryption-rest "data-encryption.md#encryption-rest").

For detailed instructions on subscribing users, see [Getting started with IAM Identity Center](getting-started-idc.md "getting-started-idc.md").
