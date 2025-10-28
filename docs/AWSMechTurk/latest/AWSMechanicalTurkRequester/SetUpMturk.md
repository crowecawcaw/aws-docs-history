# Set up Amazon Mechanical Turk

Use the following topics to learn how to use Amazon Mechanical Turk (Mechanical Turk) with APIs or AWS command line
tools.

If you plan to interact with Mechanical Turk only through the Mechanical Turk requester user interface, you can
skip these steps and instead follow the _Getting Started_
steps described in the [Requester UI Guide](../RequesterUI/GettingStarted.md "../RequesterUI/GettingStarted.md").

###### Topics

- [Step 1: Create a Mechanical Turk account](#set-up-create-account "#set-up-create-account")
- [Step 2: Link your AWS account to your Mechanical Turk requester
  account](#set-up-link "#set-up-link")
- [Step 3: Select a payment option](#set-up-payment.title "#set-up-payment.title")
- [Step 4: Get an AWS access key](#set-up-aws-access-key "#set-up-aws-access-key")
- [Step 5: Configure Your Credentials](#set-up-credentials "#set-up-credentials")
- [Step 6: Set up the developer sandbox](#set-up-sandbox "#set-up-sandbox")

## Step 1: Create a Mechanical Turk account

To create an Amazon Mechanical Turk account, go to the [Amazon Mechanical Turk Requester](https://requester.mturk.com/ "https://requester.mturk.com/") website, choose **Create an account**, and follow the on-screen instructions.

![Account creation options with "Create an Account" and sign-in link for existing users.](images/mturk_create_account.png)

Note that Mechanical Turk accounts use the same login credentials and profiles as Amazon retail
websites such as [Amazon.com](http://amazon.com/ "http://amazon.com/"). Changes in the name
or address on your account, on either Amazon.com or Mechanical Turk, are reflected in both
locations.

To use Mechanical Turk programmatically, you must have an AWS account. If you don't already have
an account, you are prompted to create one when you sign up. You're not charged for any
AWS services that you sign up for unless you use them.

###### To create an AWS account

1. Open [https://portal.aws.amazon.com/billing/signup](https://portal.aws.amazon.com/billing/signup "https://portal.aws.amazon.com/billing/signup").
2. Follow the online instructions.

Part of the sign-up procedure involves receiving a phone call or text message and entering
a verification code on the phone keypad.

When you sign up for an AWS account, an _AWS account root user_ is created. The root user has access to all AWS services
and resources in the account. As a security best practice, assign administrative access to a user, and use only the root user to perform [tasks that require root user access](../../../IAM/latest/UserGuide/id_root-user.md#root-user-tasks "../../../IAM/latest/UserGuide/id_root-user.md#root-user-tasks").

Note your AWS account ID. You need it for the next step.

## Step 2: Link your AWS account to your Mechanical Turk requester

account

You need to link your AWS account to your Mechanical Turk requester account. This operation
grants permission to your AWS account to access your requester account using the Mechanical Turk
APIs.

- Go to [https://requester.mturk.com/developer/](<https://requester.mturk.com/developer\ "https://requester.mturk.com/developer">).
- Choose **Link your AWS Account** and sign in with your AWS
  root user email address and password.

## Step 3: Select a payment option

Before you can post HITs to the Mechanical Turk marketplace, you need to enable AWS Billing for
your account to pay worker rewards and Mechanical Turk fees. These appear on the AWS Anniversary
Bill for your linked AWS account.

Alternatively, you can prepay for the HITs you plan to create using a credit card
payment.

To enable AWS Billing or prepay for HITs, go to the account section of the [Requester website](https://requester.mturk.com/account "https://requester.mturk.com/account").

## Step 4: Get an AWS access key

Before you can access Mechanical Turk programmatically, you must have an AWS access key. Access
keys consist of an access key ID and secret access key, which are used to sign
programmatic requests that you make to AWS. If you don't have access keys, you can
create them from the AWS Management Console. As a best practice, do not use the AWS account root user
access keys for any task where they are not required. Instead, create a new
administrator IAM user with access keys for yourself. To learn how, see [Creating your
first IAM admin user and group](../../../IAM/latest/UserGuide/getting-started_create-admin-group.md "../../../IAM/latest/UserGuide/getting-started_create-admin-group.md") in the IAM User Guide. If you do not wish
to grant administrator access to this account, you can choose either the
`AmazonMechanicalTurkFullAccess` or
`AmazonMechanicalTurkReadOnly` policy rather than
`AdministratorAccess` when you attach a policy to the user.

The only time that you can view or download the secret access key is when you create
the keys. You cannot recover them later. However, you can create new access keys at any
time. You must also have permissions to perform the required IAM actions. For more
information, see [Permissions Required to Access IAM Resources](../../../IAM/latest/UserGuide/access_permissions-required.md "../../../IAM/latest/UserGuide/access_permissions-required.md") in the *IAM User Guide*.

###### To create access keys for an IAM user:

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](<https://console.aws.amazon.com/iam/\ "https://console.aws.amazon.com/iam/">) .
2. In the navigation pane, choose **Users**.
3. Choose the name of the user whose access keys you want to create, and then
   choose the **Security credentials** tab.
4. In the **Access keys** section, choose **Create
   access key**.
5. To view the new access key pair, choose **Show**. You will
   not have access to the secret access key again after this dialog box closes.
   Your credentials should resemble the following example:

Access key ID: AKIAIOSFODNN7EXAMPLE

Secret access key: wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY 6. To download the key pair, choose **Download .csv file**.
Store the keys in a secure location. You will not have access to the secret
access key again after this dialog box closes.

Keep the keys confidential in order to protect your AWS account. Never email them. Do
not share them outside your organization, even if an inquiry appears to come from AWS or
Amazon.com. No one who legitimately represents Amazon will ever ask you for your secret
key.

- After you download the `.csv` file,
  choose **Close**. When you create an access key, the key
  pair is active by default, and you can use the pair right away.

**Related topics**

- [What Is IAM?](../../../IAM/latest/UserGuide/introduction.md "../../../IAM/latest/UserGuide/introduction.md") in the *IAM User
  Guide*
- [AWS Security Credentials](../../../general/latest/gr/aws-security-credentials.md "../../../general/latest/gr/aws-security-credentials.md") in *AWS General
  Reference*

## Step 5: Configure Your Credentials

To access Mechanical Turk programmatically, you must configure your credentials to enable
authorization for your applications.

There are several ways to do this. For example, you can manually create the
credentials file to store your access key ID and secret access key. You also can use the
`aws configure` command of the AWS CLI to automatically create the file.
Alternatively, you can use environment variables. For more information about configuring
your credentials, see the programming language-specific [AWS SDK developer guide](https://aws.amazon.com/tools/ "https://aws.amazon.com/tools/").

The Mechanical Turk API endpoint is only available in the `us-east-1` Region so it is
recommended that you configure your default Region as `us-east-1`. If you
primarily work with a different default AWS Region, you can specify the
`us-east-1` Region and endpoint as part of your CLI or SDK requests to
Mechanical Turk.

To install and configure the AWS CLI, see [Installing, updating, and uninstalling the AWS CLI](../../../cli/latest/userguide/cli-chap-install.md "../../../cli/latest/userguide/cli-chap-install.md") and [Configuring the AWS CLI](../../../cli/latest/userguide/cli-chap-configure.md "../../../cli/latest/userguide/cli-chap-configure.md") in the _IAM User Guide_, respectively.

## Step 6: Set up the developer sandbox

You may wish to test your HITs in the Amazon Mechanical Turk sandbox testing environment to make
sure they work as expected before publishing them in the Mechanical Turk marketplace. The
sandbox is an environment where you can publish and work on HITs at no cost before
publishing them in the _production_ Mechanical Turk marketplace. The sandbox
consists of a [requester sandbox
website](https://requestersandbox.mturk.com/ "https://requestersandbox.mturk.com/") and a [worker sandbox
website](https://workersandbox.mturk.com/ "https://workersandbox.mturk.com/").

Create a requester account on the requester sandbox website, which is located at
[https://requestersandbox.mturk.com](https://requestersandbox.mturk.com "https://requestersandbox.mturk.com"). This follows the same procedure as
creating a Mechanical Turk account described in [Step 1: Create a Mechanical Turk account](#set-up-create-account "#set-up-create-account"). You can use the same email address and
account if you wish.

You also need to create a worker account on the worker sandbox website located at
[https://workersandbox.mturk.com](https://workersandbox.mturk.com "https://workersandbox.mturk.com")
to view your sandbox HITs as a worker. There is no charge for using the Mechanical Turk sandbox
sites.

To create HITs in the sandbox using the Mechanical Turk APIs, you also need to link your AWS
account to your sandbox requester account, as described in [Step 2: Link your AWS account to your Mechanical Turk requester
account](#set-up-link "#set-up-link"), on the [requester sandbox
website](https://requestersandbox.mturk.com/developer "https://requestersandbox.mturk.com/developer").

To configure the AWS CLI or SDKs to access the sandbox instead of the production
environment, you must set the API endpoint to be [https://mturk-requester-sandbox.us-east-1.amazonaws.com](https://mturk-requester-sandbox.us-east-1.amazonaws.com "https://mturk-requester-sandbox.us-east-1.amazonaws.com"). Refer to the
[AWS CLI Command Reference](https://aws.amazon.com/cli/ "https://aws.amazon.com/cli/") or [SDK documentation](https://aws.amazon.com/tools/ "https://aws.amazon.com/tools/") for how best to do
this.
