# Subscribe users to Amazon Q Developer Pro in a member account

A _member account_ is an AWS account, other than the management account, that
is part of an organization managed by [AWS Organizations](../../../organizations/latest/userguide/orgs_introduction.md "../../../organizations/latest/userguide/orgs_introduction.md").

If you are the owner of a member account, use the following instructions to subscribe users to
Amazon Q Developer Pro in your account.

Not sure whether to subscribe users in a member or management account? See [Step 1: Choose a deployment option](deployment-options.md "deployment-options.md") for help.

For more information about organizations, member accounts, and management accounts, see [Terminology and concepts for AWS Organizations](../../../organizations/latest/userguide/orgs_getting-started_concepts.md "../../../organizations/latest/userguide/orgs_getting-started_concepts.md") in the _AWS Organizations User Guide_.

## Prerequisites

Before you begin, make sure that:

- You have a **member** AWS account.
- You have the minimum permissions required to subscribe users and manage Amazon Q Developer
  settings. For more information, see [Allow administrators to use the Amazon Q console](id-based-policy-examples-admins.md#q-admin-setup-admin-users-sub "id-based-policy-examples-admins.md#q-admin-setup-admin-users-sub"), and [Allow administrators to use the Amazon Q Developer console](id-based-policy-examples-admins.md#q-admin-setup-admin-users "id-based-policy-examples-admins.md#q-admin-setup-admin-users").
- (Optional) You have an organization instance of IAM Identity Center set up in the _management
  account_ or an account instance of IAM Identity Center set up in your _member
  account_. This IAM Identity Center intance contains the identities of the users you want
  to subscribe to Amazon Q Developer Pro, and must be deployed in a supported AWS Region, as described
  in [IAM Identity Center Regions supported by Amazon Q Developer](q-admin-setup-subscribe-regions.md#pro-subscription-regions "q-admin-setup-subscribe-regions.md#pro-subscription-regions"). If
  you don't have an IAM Identity Center instance installed, that's ok. One will be installed in your
  member account when you subscribe the first user. The IAM Identity Center instance will be installed in the AWS Regionn where you subscribed the first user. For more information about IAM Identity Center, see
  [Organization and
  account instances of IAM Identity Center](../../../singlesignon/latest/userguide/identity-center-instances.md "../../../singlesignon/latest/userguide/identity-center-instances.md") in the
  _AWS IAM Identity Center User Guide_.

## Step 1: Create the Amazon Q Developer Pro profile and subscribe

the first user

1. Sign in to the AWS Management Console using your member AWS account.
2. Switch to the **Amazon Q Developer** console.
3. Make sure you're in the AWS Region where you want to create the [Amazon Q Developer profile](subscribe-understanding-profile.md "subscribe-understanding-profile.md") and where you want
   to store user data. For supported Regions, see [Supported Regions for the Q Developer
   console and Q Developer profile](q-admin-setup-subscribe-regions.md#qdev-console-and-profile-regions "q-admin-setup-subscribe-regions.md#qdev-console-and-profile-regions").
4. Choose the **Get started** button.

###### Note

If you see a **Settings** button instead of **Get
started** button, it means that you've already run through the 'Get
started' workflow and can skip to [Step 2: Subscribe other users](#subscribe-member-new-other "#subscribe-member-new-other"). 5. Follow the on-screen prompts to subscribe your first user.

    * If the first user's email address matches one in an existing IAM Identity Center in either
     your member account or a management account, then Amazon Q connects to that
     IAM Identity Center.
    * If the first user's email address doesn't match one in an existing IAM Identity Center, then
     Amazon Q creates an IAM Identity Center account instance in your member account, and adds the first
     user to it. Note that:




    	+ Amazon Q only creates an IAM Identity Center account instance if there is no IAM Identity Center already
    	 in your member account.
    	+ If there is an IAM Identity Center account instance in your member account,
    	 but the user is not in it, then Amazon Q creates the user in the existing
    	 IAM Identity Center.

The **Create Amazon Q Developer profile** dialog box appears. 6. Review the contents of the dialog box and provide a name for your profile in
**Profile name**. For help with cross-region inferencing, see [Cross-region processing in Amazon Q Developer](cross-region-processing.md "cross-region-processing.md"). For help
with disabling dashboard metrics, see [Disabling the Amazon Q Developer dashboard](dashboard-disabling.md "dashboard-disabling.md").

Choose **Create application**.

The Amazon Q Developer profile and managed application are created, and the first user is
subscribed. 7. (Optional) Verify that the first user's subscription was created:

    1. In the Amazon Q Developer console, in the navigation pane, choose
     **Subscriptions**.
    2. In the main pane, choose the **Users** tab.

The subscription of the first user should appear in the list in the
**Pending** state. If not, refresh your browser tab.

###### Note

The subscription will change to the **Active** state after the
user's first use of Amazon Q Developer features. 8. Have the first user check their email. They should receive an email titled
**Activate Your Amazon Q Developer Pro Subscription** within 24 hours. In this
email, users will find guidance on how to begin using their Amazon Q Developer Pro license in the
AWS Management Console and their Integrated Development Environment (IDE). The email includes users'
unique Start URL and AWS Region for authentication, and provides quickstart steps for
using Amazon Q Developer in their IDE. This email streamlines the onboarding process and saves you
valuable time by eliminating the need for you to manually notify each new user.

## Step 2: Subscribe other users

To subscribe other users, add them to your IAM Identity Center instance if they're not already there, and then
subscribe them to Amazon Q Developer Pro by choosing **Subscribe** in the Amazon Q Developer
console.

For instructions on adding users to IAM Identity Center, see [Add users to your IAM Identity Center directory](../../../singlesignon/latest/userguide/addusers.md "../../../singlesignon/latest/userguide/addusers.md") in
the _AWS IAM Identity Center User Guide_.

## Step 3: Enable identity-enhanced console

sessions

If you want to allow users to use their Amazon Q Developer Pro subscription [in the
AWS Management Console, and on AWS apps and websites](q-on-aws.md "q-on-aws.md"), enable identity-enhanced console sessions.
For more information, see [Enabling identity-enhanced
console sessions](../../../singlesignon/latest/userguide/identity-aware-sessions.md "../../../singlesignon/latest/userguide/identity-aware-sessions.md") in the _AWS IAM Identity Center User Guide_.

If you don't enable identity-enhanced console sessions, users can still use Amazon Q in the
AWS Management Console, and on AWS apps and websites, but they'll be limited to the Free tier.

###### Note

The ability to enable identity-enhanced console sessions—and therefore the ability to
use Amazon Q Developer Pro subscriptions in the AWS Management Console, and on AWS apps and websites—is only
supported with organization instances of IAM Identity Center, not account instances.

## What resources were created?

When you subscribed users in your member account, Amazon Q created the following AWS resources on
your behalf:

- **An account instance of IAM Identity Center**. This instance is only
  created if the first user you subscribed wasn't found in an existing IAM Identity Center in the member
  account or management account. For more information about account instances of IAM Identity Center, see
  [Account
  instances of IAM Identity Center](../../../singlesignon/latest/userguide/account-instances-identity-center.md "../../../singlesignon/latest/userguide/account-instances-identity-center.md") in the _AWS IAM Identity Center User Guide_.

###### Note

Account instances of IAM Identity Center have [limitations](../../../singlesignon/latest/userguide/account-instances-identity-center.md#about-account-instance "../../../singlesignon/latest/userguide/account-instances-identity-center.md#about-account-instance"). For example, account instances don't support console access.
(Users can still use Amazon Q in the console, it's just that they'll be subject to the Free
tier monthly limits.) If you want your users to be able to use Amazon Q Developer Pro in the
console and other AWS websites, they must exist in an _organization
instance_ of IAM Identity Center, in a management account. For more information, see
[Subscribe users to Amazon Q Developer Pro in a management account](subscribe-management.md "subscribe-management.md").

###### Note

You can't convert or merge an account instance of IAM Identity Center into an organization
instance.

- **The first user**, in IAM Identity Center. (You might have added team
  members too.)
- **Pro tier subscriptions** for the first user and other
  users, in Amazon Q Developer.
- **An Amazon Q Developer profile**, in the Amazon Q Developer console, under
  **Settings**.
- **A managed application** called
  **QDevProfile-`region`**, in IAM Identity Center. The application is associated with the
  Amazon Q Developer profile. Like the Amazon Q Developer profile, the application is created once and
  shared between all Amazon Q Developer Pro subscribers in your member account.

###### Note

Amazon Q can create the **QDevProfile-`region`** managed application in a
maximum of 10 AWS accounts per AWS Region within an organization.
