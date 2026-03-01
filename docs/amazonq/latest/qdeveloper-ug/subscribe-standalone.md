# Subscribe users to Amazon Q Developer Pro in a standalone account

A _standalone_ account is one that is _not_ part of an
organization managed by [AWS Organizations](../../../organizations/latest/userguide/orgs_introduction.md "../../../organizations/latest/userguide/orgs_introduction.md").

If you are the owner of a standalone AWS account, use the following instructions to subscribe
yourself (and a few others) to Amazon Q Developer Pro to evaluate the service’s features and functionality.

After completing the steps on this page, read [What resources were created?](#subscribe-standalone-resources "#subscribe-standalone-resources") at the end to understand which resources were
installed and configured on your behalf when you subscribed. This will help you cleanly remove
everything when you're finished testing.

## Prerequisites

Before you begin, make sure that:

- You have a **standalone** AWS account.
- You have the minimum permissions required to subscribe users and manage Amazon Q Developer
  settings. For more information, see [Allow administrators to use the Amazon Q console](id-based-policy-examples-admins.md#q-admin-setup-admin-users-sub "id-based-policy-examples-admins.md#q-admin-setup-admin-users-sub"), and [Allow administrators to use the Amazon Q Developer console](id-based-policy-examples-admins.md#q-admin-setup-admin-users "id-based-policy-examples-admins.md#q-admin-setup-admin-users").
- (Optional) You have an account instance of IAM Identity Center set up in your standalone account. This
  IAM Identity Center contains the identities of the users you want to subscribe to Amazon Q Developer Pro, and must be
  deployed in a supported AWS Region, as described in [IAM Identity Center Regions supported by Amazon Q Developer](q-admin-setup-subscribe-regions.md#pro-subscription-regions "q-admin-setup-subscribe-regions.md#pro-subscription-regions"). If you
  don't have an IAM Identity Center instance installed, that's ok. One will be installed when you
  subscribe the first user (yourself). The IAM Identity Center instance will be installed in the AWS Region where you subscribed the first user. For more information about IAM Identity Center, see [Organization and
  account instances of IAM Identity Center](../../../singlesignon/latest/userguide/identity-center-instances.md "../../../singlesignon/latest/userguide/identity-center-instances.md") in the
  _AWS IAM Identity Center User Guide_.

###### Note

The instructions on this page assume you have not already installed an IAM Identity Center
instance in your standalone account.

## Step 1: Create the Amazon Q Developer Pro profile and subscribe yourself

1. Sign in to the AWS Management Console using your standalone AWS account. Sign in as the root user,
   or as an IAM user with the permissions described in [Prerequisites](#subscribe-standalone-prereqs "#subscribe-standalone-prereqs").
2. Switch to the **Amazon Q Developer** console.
3. Make sure you're in the AWS Region where you want to create the [Amazon Q Developer profile](subscribe-understanding-profile.md "subscribe-understanding-profile.md") and where you want
   to store user data. For supported Regions, see [Supported Regions for the Q Developer console and Q Developer profile](q-admin-setup-subscribe-regions.md#qdev-console-and-profile-regions "q-admin-setup-subscribe-regions.md#qdev-console-and-profile-regions").
4. Choose the **Get started** button.

###### Note

If you see a **Settings** button instead of **Get
started** button, it means that you've already run through the 'Get
started' workflow and can skip to [Step 2: Subscribe team members](#subscribe-standalone-sub-team "#subscribe-standalone-sub-team").

A **Create your user** dialog box appears. 5. Enter your information. The email address can be the same or different from the one you
used to sign up for your AWS account.

Choose **Continue**.

The **Create Amazon Q Developer profile** dialog box appears. 6. Review the contents of the dialog box and provide a name for your profile in
**Profile name**. For help with cross-region inferencing, see [Cross-region processing in Amazon Q Developer](cross-region-processing.md "cross-region-processing.md"). For help
with disabling dashboard metrics, see [Disabling the Amazon Q Developer dashboard](dashboard-disabling.md "dashboard-disabling.md").

Choose **Create application**.

The Amazon Q Developer profile and managed application are created, and your subscription is
created. 7. (Optional) Verify that your subscription was created:

    1. In the Amazon Q Developer console, in the navigation pane, choose
     **Subscriptions**.
    2. In the main pane, choose the **Users** tab.

Your subscription should appear in the list in the **Pending** state.
If not, refresh your browser tab.

###### Note

Your subscription will change to the **Active** state after your
first use of Amazon Q Developer features.

Now that you are subscribed, you must activate your subscription. You can do this now,
or after you've subscribed team members, as described in the next section. To activate
your subscription, check your inbox for emails titled **Invitation to join
AWS IAM Identity Center** and **Activate Your Amazon Q Developer Pro Subscription**.
Follow the instructions in these emails to activate your Amazon Q Developer Pro subscription and set up
Amazon Q Developer Pro in your IDE. You should receive these emails within 24 hours.

## Step 2: Subscribe team members

You might want to subscribe other team members so that they can try out Amazon Q Developer Pro with you. To
subscribe them, use the following instructions.

###### To add team members

1. Switch to the IAM Identity Center console (not the IAM console).

###### Note

IAM Identity Center was set up on your behalf when you subscribed yourself. For more information
about the IAM Identity Center that was set up, see [What resources were created?](#subscribe-standalone-resources "#subscribe-standalone-resources"). 2. Add users and groups. For instructions, see [Add users to your IAM Identity Center
directory](../../../singlesignon/latest/userguide/addusers.md "../../../singlesignon/latest/userguide/addusers.md") in the _AWS IAM Identity Center User Guide_.

![The IAM Identity Center page showing two users.](images/subscribe/Sub-8.png) 3. Go to the next procedure to subscribe team members.

###### To subscribe team members

1. Return to the Amazon Q Developer console.
2. In the navigation pane, choose **Subscriptions**, and then choose
   **Subscribe**.

The **Assign users and groups** dialog box appears. 3. Start typing the name of a team member or group that you added. The name should
auto-populate.

###### Note

The dialog box only matches on user names or group names. It does not match on email
addresses. 4. Choose **Assign**. 5. Have users check their email. They should receive an email titled **Activate
Your Amazon Q Developer Pro Subscription** within 24 hours. In this email, users will find
guidance on how to begin using their Amazon Q Developer Pro license in the AWS Management Console and their
Integrated Development Environment (IDE). The email includes users' unique Start URL and
AWS Region for authentication, and provides quickstart steps for using Amazon Q Developer in
their IDE. This email streamlines the onboarding process and saves you valuable time by
eliminating the need for you to manually notify each new user.

## What resources were created?

When you subscribed yourself (and optionally, team members), Amazon Q created the following AWS
resources on your behalf:

- **An account instance of IAM Identity Center**. For more information
  about account instances of IAM Identity Center, see [Account
  instances of IAM Identity Center](../../../singlesignon/latest/userguide/account-instances-identity-center.md "../../../singlesignon/latest/userguide/account-instances-identity-center.md") in the _AWS IAM Identity Center User Guide_.

###### Note

Account instances of IAM Identity Center have [limitations](../../../singlesignon/latest/userguide/account-instances-identity-center.md#about-account-instance "../../../singlesignon/latest/userguide/account-instances-identity-center.md#about-account-instance"). For example, account instances don't support console access.
(Users can still use Amazon Q in the console, it's just that they'll be subject to the Free
tier monthly limits.) If you want to use Amazon Q Developer Pro in the console and other AWS
websites, you must be a user in an _organization instance_ of
IAM Identity Center, in a management account. For more information, see [Subscribe users to Amazon Q Developer Pro in a management account](subscribe-management.md "subscribe-management.md").

###### Note

You can't convert or merge an account instance of IAM Identity Center into an organization
instance.

- **The first user**, in IAM Identity Center. You might have manually added
  team members too.
- **Pro tier subscriptions** for the first user and team
  members, in Amazon Q Developer.
- **An Amazon Q Developer profile**, in the Amazon Q Developer console, under
  **Settings**.
- **A managed application** called
  **QDevProfile-`region`**, in the IAM Identity Center
  that is set up in your standalone account. The application is associated with the
  Amazon Q Developer profile. Like the Amazon Q Developer profile, the application is created once and
  shared between all Amazon Q subscribers in your standalone account.
