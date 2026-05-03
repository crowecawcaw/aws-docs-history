# Setting up and signing into Amazon Quick

Amazon Quick offers two ways to get started, depending on your needs:

- **Get started quickly** – If you're an
  individual or small team and don't have an AWS account, see [Signing up at quick.aws.com](../../../quicksuite/latest/userguide/standalone-signup.md "../../../quicksuite/latest/userguide/standalone-signup.md").
- **Use Quick with your organization's AWS
  account** – If your organization already uses AWS services, see
  [Signing up through the AWS Console](../../../quicksuite/latest/userguide/signing-up.md "../../../quicksuite/latest/userguide/signing-up.md").
  **Free and Plus accounts (quick.aws.com):** Sign up at [https://quick.aws.com](https://quick.aws.com "https://quick.aws.com") using an email address.
  Amazon Quick creates an account for you automatically using your email or social login
  credentials. Choose from Free, Free Trial Plus, or Paid Plus plan tiers. No
  AWS account or technical configuration is required.

**AWS Console accounts:** If your organization uses AWS,
you can provision Amazon Quick through the AWS Management Console. This path uses IAM Identity Center for
authentication and integrates with your existing AWS billing and governance.

For a comparison of features available with each account type, see [Pricing
and availability](../../../quicksuite/latest/userguide/what-is.md#pricing "../../../quicksuite/latest/userguide/what-is.md#pricing").

For more information on administering your account after setup, see [Administering Amazon Quick (Free/Plus)](../../../quicksuite/latest/userguide/standalone-admin-guide.md "../../../quicksuite/latest/userguide/standalone-admin-guide.md") or [Administering Amazon Quick](../../../quicksuite/latest/userguide/qsysadmin.md "../../../quicksuite/latest/userguide/qsysadmin.md") for accounts provisioned through the
AWS Management Console.

###### Topics

- [Complete initial configuration tasks](#setting-up-create-iam-user "#setting-up-create-iam-user")
- [Signing up at quick.aws.com](standalone-signup.md "standalone-signup.md")
- [Signing up through the AWS Console](signing-up.md "signing-up.md")
- [Signing in to Amazon Quick](signing-in.md "signing-in.md")

## Complete initial configuration tasks

###### Note

The following configuration tasks apply to AWS Console accounts only. If you
are signing up at [quick.aws.com](https://quick.aws.com "https://quick.aws.com"), these
steps are handled automatically. See [Signing up at quick.aws.com](../../../quicksuite/latest/userguide/standalone-signup.md "../../../quicksuite/latest/userguide/standalone-signup.md") instead.

To use Amazon Quick you must first complete the following tasks:

###### Topics

- [Sign up for an AWS account](#sign-up-for-aws "#sign-up-for-aws")
- [Create a user with administrative access](#create-an-admin "#create-an-admin")

### Sign up for an AWS account

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

### Create a user with administrative access

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
