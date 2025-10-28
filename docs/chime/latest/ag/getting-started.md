**End of support notice**: On February
20, 2026, AWS will end support for the Amazon Chime service. After February 20, 2026, you will
no longer be able to access the Amazon Chime console or Amazon Chime application resources. For more
information, visit the [blog post](https://aws.amazon.com/blogs/messaging-and-targeting/update-on-support-for-amazon-chime/ "https://aws.amazon.com/blogs/messaging-and-targeting/update-on-support-for-amazon-chime/"). **Note:** This does not impact the
availability of the [Amazon Chime SDK
service](https://aws.amazon.com/chime/chime-sdk/ "https://aws.amazon.com/chime/chime-sdk/").

# Getting started

The easiest way for your users to get started with Amazon Chime is to download and use the
Amazon Chime Pro version for free for 30 days. For more information, see [Download Amazon Chime](https://aws.amazon.com/chime/trial "https://aws.amazon.com/chime/trial").

###### Purchasing Amazon Chime

To continue using the Amazon Chime Pro version after the 30-day free trial period, you must
create an Amazon Chime administrator account and add your users to it. To get started, you must
first complete the [Prerequisites for Amazon Chime system administrators](prereqs.md "prereqs.md"), which include
creating an AWS account. Then, you can create and configure an Amazon Chime administrator
account and add users to it by completing the following tasks.

###### Tasks

- [Step 1: Creating an Amazon Chime administrator account](#create-account "#create-account")
- [Step 2 (optional): Configuring account settings](#acct-settings "#acct-settings")
- [Step 3: Adding users to your account](#add-users "#add-users")
- [(Optional) Setting up phone numbers for your Amazon Chime account](#add-phone-options "#add-phone-options")

## Step 1: Creating an Amazon Chime administrator account

After you complete the [Prerequisites for Amazon Chime system administrators](prereqs.md "prereqs.md"), you can
create an Amazon Chime administrator account.

###### To create an Amazon Chime administrator account

1. Open the Amazon Chime console at [https://chime.aws.amazon.com/](https://chime.aws.amazon.com "https://chime.aws.amazon.com").
2. On the **Accounts** page, choose **New
   account**.
3. For **Account Name**, enter a name for the account and choose
   **Create account**.
4. (Optional) Choose whether to let Amazon Chime select the optimal AWS Region for your meetings from all available Regions, or to use only the Regions that you select. For more information, see [Managing meeting settings](mtg-settings.md "mtg-settings.md").

## Step 2 (optional): Configuring account settings

By default, new accounts are created as Team accounts. If you
prefer to claim a domain and connect to your own identity provider, or Okta SSO, you can
convert to an Enterprise account. For more
information about Team and Enterprise account types, see [Choosing between an Amazon Chime Team account
or Enterprise account](choose-team-enterprise-account.md "choose-team-enterprise-account.md").

###### To convert a Team account to an Enterprise account

1. Open the Amazon Chime console at [https://chime.aws.amazon.com/](https://chime.aws.amazon.com "https://chime.aws.amazon.com").
2. For **Accounts**, choose the name of the
   account.
3. For **Identity**, choose **Getting Started**.
4. Follow the steps in the console to claim your domain.
5. (Optional) Follow the steps in the console to set up your identity
   provider and configure your directory group.

For more information about claiming domains, see [Claiming a domain](claim-domain.md "claim-domain.md"). For more information about setting up identity
providers, see [Connecting to your Active Directory](active_directory.md "active_directory.md") and [Connecting to Okta SSO](okta_sso.md "okta_sso.md").

You can also allow or stop allowing account policies for options, such as remote
control of shared screens and the Amazon Chime call me feature.

###### To configure account policies

1. Open the Amazon Chime console at [https://chime.aws.amazon.com/](https://chime.aws.amazon.com "https://chime.aws.amazon.com").
2. On the **Accounts** page, choose the name of the
   account to configure.
3. For **Settings**, choose **Meetings**.
4. For **Policies**, select or clear the account policy options you want to
   allow or stop allowing.
5. Choose **Change**.

For more information, see [Managing meeting settings](mtg-settings.md "mtg-settings.md").

## Step 3: Adding users to your account

After your Amazon Chime Team account is created, invite yourself and
your users to join it. If you are upgrading your account to an
Enterprise account, you do not need to invite your users.
Instead, upgrade to an Enterprise account and
claim your domain. For more information, see [Step 2 (optional): Configuring account settings](#acct-settings "#acct-settings").

###### To add users to your Amazon Chime account

1. Open the Amazon Chime console at [https://chime.aws.amazon.com/](https://chime.aws.amazon.com "https://chime.aws.amazon.com").
2. On the **Accounts** page, choose the name of your
   account.
3. On the **Users** page, choose
   **Invite users**.
4. Enter the email addresses of the users to invite, including yourself, and choose **Invite
   users**.

The invited users receive email invitations to join the Amazon Chime Team account that you created.
When they register their Amazon Chime user accounts, they receive Pro permissions by default,
and their 30-day trial ends. If they have already signed up for an Amazon Chime user account
with their work email address, they can continue to use that account. They can also
download the Amazon Chime client app at any time by choosing **Download Amazon Chime** and
signing in to their user account.

You are only charged for a user with Pro permissions when they host a meeting. There
is no charge for users with Basic permissions. Basic users cannot host meetings, but
they can attend meetings and use chat. For more information about pricing and the
features that users with Pro and Basic permissions can access, see [Plans and pricing](https://aws.amazon.com/chime/pricing "https://aws.amazon.com/chime/pricing").

###### To change user permissions

1. Open the Amazon Chime console at [https://chime.aws.amazon.com/](https://chime.aws.amazon.com "https://chime.aws.amazon.com").
2. On the **Accounts** page, choose the name of your
   account.
3. On the **Users** page, select
   the user or users to change permissions for.
4. Choose **User actions**, **Assign user
   permission**.
5. For **Permissions**, select **Pro** or
   **Basic**.
6. Choose **Assign**.

You can provide other users with administrator permissions, and also control their
access to the Amazon Chime console for your account. For more information, see [Identity and access management for Amazon Chime](security-iam.md "security-iam.md").

## (Optional) Setting up phone numbers for your Amazon Chime account

The following phone options are available for Amazon Chime administrative accounts:

**Amazon Chime Business Calling**

Lets your users send and receive phone calls and text messages directly from Amazon Chime. Provision your phone numbers in the Amazon Chime console or port in existing phone numbers. Assign the phone numbers to your Amazon Chime users and grant them permissions to send and receive phone calls and text messages using Amazon Chime. For more information, see [Managing phone numbers in Amazon Chime](phone-numbers.md "phone-numbers.md") and [Porting existing phone numbers](porting.md "porting.md").

**Amazon Chime Voice Connector**

Provides SIP trunking service for an existing phone system. Port in existing phone numbers or provision new phone numbers in the Amazon Chime console. For more information, see [Managing Amazon Chime Voice Connectors](../../../chime-sdk/latest/ag/voice-connectors.md "../../../chime-sdk/latest/ag/voice-connectors.md") in the _Amazon Chime SDK Administration Guide_.
