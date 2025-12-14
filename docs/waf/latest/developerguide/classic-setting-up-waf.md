**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the console](working-with-console.md "working-with-console.md").

# Setting up AWS WAF Classic

###### Warning

AWS WAF Classic is is going through a planned end-of-life process. Refer to your AWS Health dashboard for the milestones and dates specific to your Region.

###### Note

This is **AWS WAF Classic** documentation. You should only
use this version if you created AWS WAF
resources, like rules and web ACLs, in AWS WAF prior to November 2019, and you have not
migrated them over to the latest version yet. To migrate your web ACLs, see [Migrating your AWS WAF Classic resources to AWS WAF](waf-migrating-from-classic.md "waf-migrating-from-classic.md").

**For the latest version of AWS WAF**, see [AWS WAF](waf-chapter.md "waf-chapter.md").

This topic describes preliminary steps, such as creating a user account, to prepare you to
use AWS WAF Classic. You aren't charged for these. You are charged only for AWS services that you use.

###### Note

If you're a new user to AWS WAF, don't follow these setup steps for AWS WAF Classic. Instead, follow
the steps for the latest version of AWS WAF, at [Setting up your account to use the services](setting-up-waf.md "setting-up-waf.md").

After you complete these steps, see [Getting started with AWS WAF Classic](classic-getting-started.md "classic-getting-started.md") to continue getting started with AWS WAF Classic.

###### Note

AWS Shield Standard is included with AWS WAF Classic and does not require additional setup. For more
information, see [How AWS Shield and Shield Advanced work](ddos-overview.md "ddos-overview.md").

Before you use AWS WAF Classic or AWS Shield Advanced for the first time, complete the steps in this section.

###### Topics

- [Sign up for an AWS account](#sign-up-for-aws "#sign-up-for-aws")
- [Create a user with administrative access](#create-an-admin "#create-an-admin")
- [Download tools](#classic-setting-up-waf-tools "#classic-setting-up-waf-tools")

## Sign up for an AWS account

If you do not have an AWS account, complete the following steps to create one.

###### To sign up for an AWS account

1. Open [https://portal.aws.amazon.com/billing/signup](https://portal.aws.amazon.com/billing/signup "https://portal.aws.amazon.com/billing/signup").
2. Follow the online instructions.

Part of the sign-up procedure involves receiving a phone call or text message and entering
a verification code on the phone keypad.

When you sign up for an AWS account, an _AWS account root user_ is created. The root user has access to all AWS services
and resources in the account. As a security best practice, assign administrative access to a user, and use only the root user to perform [tasks that require root user access](../../../IAM/latest/UserGuide/id_root-user.md#root-user-tasks "../../../IAM/latest/UserGuide/id_root-user.md#root-user-tasks").

AWS sends you a confirmation email after the sign-up process is
complete. At any time, you can view your current account activity and manage your account by
going to [https://aws.amazon.com/](https://aws.amazon.com/ "https://aws.amazon.com/") and choosing **My
Account**.

## Create a user with administrative access

After you sign up for an AWS account, secure your AWS account root user, enable AWS IAM Identity Center, and create an administrative user so that you
don't use the root user for everyday tasks.

###### Secure your AWS account root user

1. Sign in to the [AWS Management Console](https://console.aws.amazon.com/ "https://console.aws.amazon.com/") as the account owner by choosing **Root user** and entering your AWS account email address. On the next page, enter your password.

For help signing in by using root user, see [Signing in as the root user](../../../signin/latest/userguide/console-sign-in-tutorials.md#introduction-to-root-user-sign-in-tutorial "../../../signin/latest/userguide/console-sign-in-tutorials.md#introduction-to-root-user-sign-in-tutorial") in the _AWS Sign-In User Guide_. 2. Turn on multi-factor authentication (MFA) for your root user.

For instructions, see [Enable a virtual MFA device for your AWS account root user (console)](../../../IAM/latest/UserGuide/enable-virt-mfa-for-root.md "../../../IAM/latest/UserGuide/enable-virt-mfa-for-root.md") in the _IAM User Guide_.

###### Create a user with administrative access

1. Enable IAM Identity Center.

For instructions, see [Enabling
AWS IAM Identity Center](../../../singlesignon/latest/userguide/get-set-up-for-idc.md "../../../singlesignon/latest/userguide/get-set-up-for-idc.md") in the
_AWS IAM Identity Center User Guide_. 2. In IAM Identity Center, grant administrative access to a user.

For a tutorial about using the IAM Identity Center directory as your identity source, see [Configure user access with the default IAM Identity Center directory](../../../singlesignon/latest/userguide/quick-start-default-idc.md "../../../singlesignon/latest/userguide/quick-start-default-idc.md") in the
_AWS IAM Identity Center User Guide_.

###### Sign in as the user with administrative access

- To sign in with your IAM Identity Center user, use the sign-in URL that was sent to your email address when you created the IAM Identity Center user.

For help signing in using an IAM Identity Center user, see [Signing in to the AWS access portal](../../../signin/latest/userguide/iam-id-center-sign-in-tutorial.md "../../../signin/latest/userguide/iam-id-center-sign-in-tutorial.md") in the _AWS Sign-In User Guide_.

###### Assign access to additional users

1. In IAM Identity Center, create a permission set that follows the best practice of applying least-privilege permissions.

For instructions, see [Create a permission set](../../../singlesignon/latest/userguide/get-started-create-a-permission-set.md "../../../singlesignon/latest/userguide/get-started-create-a-permission-set.md") in the _AWS IAM Identity Center User Guide_. 2. Assign users to a group, and then assign single sign-on access to the group.

For instructions, see [Add groups](../../../singlesignon/latest/userguide/addgroups.md "../../../singlesignon/latest/userguide/addgroups.md") in the _AWS IAM Identity Center User Guide_.

## Download tools

The AWS Management Console includes a console for AWS WAF Classic, but if you want to access AWS WAF Classic
programmatically, see the following:

- If you want to call the AWS WAF Classic API without having to handle low-level details like
  assembling raw HTTP requests, you can use an AWS SDK. The AWS SDKs provide
  functions and data types that encapsulate the functionality of AWS WAF Classic and other
  AWS services. To download an AWS SDK, see the applicable page, which also
  includes prerequisites and installation instructions:

      + [Java](https://aws.amazon.com/sdk-for-java/ "https://aws.amazon.com/sdk-for-java/")
      + [JavaScript](http://aws.amazon.com/sdkforbrowser/ "http://aws.amazon.com/sdkforbrowser/")
      + [.NET](https://aws.amazon.com/sdk-for-net/ "https://aws.amazon.com/sdk-for-net/")
      + [Node.js](https://aws.amazon.com/sdk-for-node-js/ "https://aws.amazon.com/sdk-for-node-js/")
      + [PHP](https://aws.amazon.com/sdk-for-php/ "https://aws.amazon.com/sdk-for-php/")
      + [Python](https://github.com/boto/boto "https://github.com/boto/boto")
      + [Ruby](https://aws.amazon.com/sdk-for-ruby/ "https://aws.amazon.com/sdk-for-ruby/")

  For a complete list of AWS SDKs, see [Tools for
  Amazon Web Services](http://aws.amazon.com/tools/ "http://aws.amazon.com/tools/").

- If you're using a programming language for which AWS doesn't provide an SDK,
  the [AWS WAF API Reference](../APIReference.md "../APIReference.md") documents the operations
  that AWS WAF Classic supports.
- The AWS Command Line Interface (AWS CLI) supports AWS WAF Classic. The AWS CLI lets you control multiple AWS services
  from the command line and automate them through scripts. For more information,
  see [AWS Command Line Interface](https://aws.amazon.com/cli/ "https://aws.amazon.com/cli/").
- AWS Tools for Windows PowerShell supports AWS WAF Classic. For more information, see [AWS Tools for PowerShell Cmdlet Reference](http://aws.amazon.com/documentation/powershell/ "http://aws.amazon.com/documentation/powershell/").
