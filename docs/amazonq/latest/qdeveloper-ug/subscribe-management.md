# Subscribe users to Amazon Q Developer Pro in a management account

A _management account_ is an AWS account that is part of an organization
managed by [AWS Organizations](../../../organizations/latest/userguide/orgs_introduction.md "../../../organizations/latest/userguide/orgs_introduction.md"). It is the ultimate owner of the organization, and is responsible for paying all
charges accrued by the accounts in its organization.

If you are the owner of a management account, use the following instructions to subscribe users to
Amazon Q Developer Pro in your account.

###### Note

If possible, subscribe users in member accounts instead of your management account. For more
information, see [Step 1: Choose a deployment option](deployment-options.md "deployment-options.md").

For more information about organizations and management accounts, see [Terminology and concepts
for AWS Organizations](../../../organizations/latest/userguide/orgs_getting-started_concepts.md "../../../organizations/latest/userguide/orgs_getting-started_concepts.md") in the _AWS Organizations User Guide_.

## Prerequisites

Before you begin, make sure that:

- You have a **management** AWS account.
- You have the minimum permissions required to subscribe users and manage Amazon Q Developer
  settings. For more information, see [Allow administrators to use the Amazon Q console](id-based-policy-examples-admins.md#q-admin-setup-admin-users-sub "id-based-policy-examples-admins.md#q-admin-setup-admin-users-sub"), and [Allow administrators to use the Amazon Q Developer console](id-based-policy-examples-admins.md#q-admin-setup-admin-users "id-based-policy-examples-admins.md#q-admin-setup-admin-users").
- You have an organization instance of IAM Identity Center set up in your management account. This IAM Identity Center
  contains the identities of the users you want to subscribe to Amazon Q Developer Pro, and must be
  deployed in a supported AWS Region, as described in [IAM Identity Center Regions supported by Amazon Q Developer](q-admin-setup-subscribe-regions.md#pro-subscription-regions "q-admin-setup-subscribe-regions.md#pro-subscription-regions"). For
  more information about IAM Identity Center, see [Organization instances of IAM Identity Center](../../../singlesignon/latest/userguide/organization-instances-identity-center.md "../../../singlesignon/latest/userguide/organization-instances-identity-center.md") in the
  _AWS IAM Identity Center User Guide_.

## Step 1: Create the Amazon Q Developer

profile

1. Sign in to the AWS Management Console using your AWS management account.
2. Switch to the **Amazon Q Developer** console.
3. Make sure you're in the AWS Region where you want to create the [Amazon Q Developer profile](subscribe-understanding-profile.md "subscribe-understanding-profile.md") and where you want
   to store user data. For supported Regions, see [Supported Regions for the Q Developer
   console and Q Developer profile](q-admin-setup-subscribe-regions.md#qdev-console-and-profile-regions "q-admin-setup-subscribe-regions.md#qdev-console-and-profile-regions").
4. Choose **Get started**.

The **Create Amazon Q Developer profile** dialog box appears. 5. Review the contents of the dialog box and provide a name for your profile in
**Profile name**. For help with:

    * Cross-region inferencing, see [Cross-region processing in Amazon Q Developer](cross-region-processing.md "cross-region-processing.md").
    * The **Share Amazon Q Developer settings with member account** check
     box, see [Enabling profile sharing in Amazon Q Developer](q-admin-profile-sharing.md "q-admin-profile-sharing.md") and [Step 1: Choose a deployment option](deployment-options.md "deployment-options.md").
    * Disabling dashboard metrics, see [Disabling the Amazon Q Developer dashboard](dashboard-disabling.md "dashboard-disabling.md").

Choose **Create application**.

The Amazon Q Developer profile and managed application are created.

## Step 2: Subscribe users

1. In the Amazon Q Developer console, from the navigation pane, choose
   **Subscriptions**.
2. Choose **Subscribe**.

The **Assign users and groups** dialog box appears. 3. Start typing the group or user you want to subscribe. The group or user will
auto-populate with the ones available in the IAM Identity Center set up in your management
account.

###### Note

The dialog box only matches on user names or group names. It does not match on email
addresses. 4. Choose **Assign**. 5. Have users check their email. They should receive an email titled **Activate
Your Amazon Q Developer Pro Subscription** within 24 hours with instructions on how to
begin using their Amazon Q Developer Pro license.

## Step 3: Enable identity-enhanced console sessions

If you want to allow users to use their Amazon Q Developer Pro subscription [in the
AWS Management Console, and on AWS apps and websites](q-on-aws.md "q-on-aws.md"), enable identity-enhanced console sessions.
For more information, see [Enabling identity-enhanced
console sessions](../../../singlesignon/latest/userguide/identity-aware-sessions.md "../../../singlesignon/latest/userguide/identity-aware-sessions.md") in the _AWS IAM Identity Center User Guide_.

###### Note

If you don't enable identity-enhanced console sessions, users can still use Amazon Q in the
AWS Management Console, and on AWS apps and websites, but they'll be limited to the Free tier.

## What resources were created?

When you created the Amazon Q Developer profile and subscribed users in your management account, Amazon Q
created the following resources on your behalf:

- **Pro tier subscriptions** for users, in Amazon Q Developer.
- **An Amazon Q Developer profile**, in the Amazon Q Developer console, under
  **Settings**.
- **A managed application** called
  **QDevProfile-`region`**, in the IAM Identity Center
  that is set up in your management account. The application is associated with the
  Amazon Q Developer profile. Like the Amazon Q Developer profile, the application is created once and
  shared between all Amazon Q subscribers in your management account.

###### Note

Amazon Q can create the
**QDevProfile-`region`** managed
application in a maximum of 10 AWS accounts per AWS Region within an
organization.
