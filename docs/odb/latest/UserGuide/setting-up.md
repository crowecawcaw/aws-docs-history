# Onboarding to Oracle Database@AWS

Before you can begin using Oracle Database@AWS, make sure you're signed up for AWS and create
necessary users. Then you can purchase Oracle Database@AWS from AWS Marketplace by accepting a private
offer from Oracle.

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

## Request a private offer for Oracle Database@AWS

The AWS Marketplace seller private offer feature enables you to request and receive
Oracle Database@AWS pricing and EULA terms from Oracle. You negotiate pricing and terms with
Oracle, and then Oracle creates a private offer for the AWS account that you designate. You
accept the private offer and receive the negotiated price and terms of use. At this time, you
can use the Oracle Database@AWS dashboard. When the private offer agreement reaches its expiration date,
you're either moved automatically to the product's public pricing or unsubscribed from
Oracle Database@AWS. For more information about private offers, see [Private
offers in AWS Marketplace](../../../marketplace/latest/buyerguide/buyer-private-offers.md "../../../marketplace/latest/buyerguide/buyer-private-offers.md").

###### To request and accept a private offer for Oracle Database@AWS

1. Sign in to the AWS Management Console.
2. Search for and then choose Oracle Database@AWS.
3. Choose **Request private offer**.

###### Note

The Oracle Database@AWS dashboard isn't available until after you have accepted a private
offer. 4. On the Oracle Cloud Infrastructure (OCI) site, specify details such as the region and your contact
information. 5. Wait for an OCI representative to contact you and make a private offer available. 6. In the AWS Management Console, choose **View private offer**. 7. Choose the offer and then choose **View offer**. 8. Choose **Create contract** and respond to the subsequent prompts to
accept the private offer. 9. After accepting the private offer, you'll need to activate your OCI account. You can
access the Oracle activation links directly from AWS Management Console.

    1. In the console, navigate to the **Get started** section.
    2. Click on the Oracle activation link provided in the console. Alternatively, you can also use the activation link sent to you via email.
    3. On the Oracle activation page, choose whether to create a new Oracle cloud account or add to an existing account.
    4. Complete the activation process by following the on-screen instructions.
    5. After submitting your activation request, you'll see an **Activation in progress** status in the AWS Management Console, and the dashboard will be temporarily disabled with a reason displayed.
    6. After activation is complete, the Oracle Database@AWS dashboard becomes available, allowing you to
     manage your resources.

10. In the AWS Management Console, choose **Dashboard**.

## Subscribe to Oracle Database@AWS in multiple Regions

When you subscribe to Oracle Database@AWS through AWS Marketplace and finish onboarding, your AWS account is
linked to your OCI tenancy. This link, along with related resources, is automatically
replicated to all AWS Regions where Oracle Database@AWS is available. You subscribe and onboard once
rather than repeating the process for each Region.

To use Oracle Database@AWS in multiple Regions, perform the following steps:

1. Subscribe to Oracle Database@AWS through AWS Marketplace and complete the onboarding process.

When you first subscribe to Oracle Database@AWS, your account is activated in a home Region. You
specify the home Region in Oracle Cloud Infrastructure (OCI). 2. Enable your preferred Regions through the OCI console.

If you don't enable a Region in OCI, and then you switch to this Region in the
Oracle Database@AWS console, you receive an error stating that you haven't subscribed. In this case,
you must enable this Region in OCI before you can use the Oracle Database@AWS dashboard in this
Region. 3. Access Oracle Database@AWS in any supported AWS Region without repeating the subscription
process.
