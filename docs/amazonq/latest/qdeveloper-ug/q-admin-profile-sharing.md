

# Enabling profile sharing in Amazon Q Developer
<a name="q-admin-profile-sharing"></a>

**Note**  
This section does not apply to personal accounts (Builder IDs).

If you are a management account administrator within an organization managed by [AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html), you can enable the *profile sharing* feature. When profile sharing is enabled, the [Amazon Q Developer profile](subscribe-understanding-profile.md) that has been created in a management account will be shared with member accounts. Sharing the profile has one benefit: it allows IAM Identity Center workforce users who are subscribed to Amazon Q Developer Pro in a *management* account to use their Amazon Q Developer Pro subscription [in the AWS Management Console, and on AWS apps and websites](q-on-aws.md) while signed in to a *member* account. When profile sharing is disabled, these users can still use Amazon Q in the AWS Management Console, and on AWS apps and websites, while signed in to a member account, but they'll be subject to Free tier limits and features.

Enabling profile sharing has no effect on users' ability to use [Amazon Q in the integrated development environment (IDE)](q-in-IDE.md) or [on the command line](command-line.md).

Use the following instructions to enable profile sharing.

 **Prerequisites** 

Before you begin, make sure that:
+ You are an administrator of an AWS *management* account.
+ You have an IAM Identity Center instance set up in your management account and connected to Amazon Q. To check, sign in to your management account, go to the Amazon Q Developer console, choose **Settings**, and make sure that a **Start URL** appears. 
+ You have subscribed users to Amazon Q Developer Pro in your management account.
+ You have the minimum permissions required to access the Amazon Q Developer console. For more information, see [Allow administrators to use the Amazon Q Developer console](id-based-policy-examples-admins.md#q-admin-setup-admin-users).

**To enable profile sharing**

1. Sign in to the AWS Management Console using your AWS management account.

1. Switch to the Amazon Q Developer console.

1. Choose **Settings**. 

1. Scroll to the **Member account settings** section and choose **Edit**. 

1. Enable **Q Developer managed application and settings profile**. 

1. Choose **Save**. 

   Users who are subscribed to Amazon Q Developer Pro in your management account will now be able to use their Amazon Q Developer Pro subscription in the AWS Management Console, and on AWS apps and websites while signed in to a member account.