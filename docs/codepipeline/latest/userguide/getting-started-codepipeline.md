# Getting started with CodePipeline

If you are new to CodePipeline, you can follow the tutorials in this guide after following the
steps in this chapter to get set up.

The CodePipeline console includes helpful information in a collapsible panel that you can open from
the information icon or any **Info** link on the page. (
![Image showing the lower-case letter i that is used as the console info icon](images/console-info-icon.png)
). You can close this panel at any time.

The CodePipeline console also provides a way to quickly search for your resources, such as
repositories, build projects, deployment applications, and pipelines. Choose **Go to
resource** or press the `/` key, and then type the name of the resource.
Any matches appear in the list. Searches are case insensitive. You only see resources that you
have permissions to view. For more information, see [Viewing resources in the
console](security-iam-resources-console.md "security-iam-resources-console.md").

Before you can use AWS CodePipeline for the first time, you must create your AWS account and
create your first administrative user.

###### Topics

- [Step 1: Create an AWS account and administrative
  user](#create-iam-user "#create-iam-user")
- [Step 2: Apply a managed policy for administrative access
  to CodePipeline](#assign-permissions "#assign-permissions")
- [Step 3: Install the AWS CLI](#install-cli "#install-cli")
- [Step 4: Open the console for CodePipeline](#open-codepipeline-console "#open-codepipeline-console")
- [Next steps](#next-steps "#next-steps")

## Step 1: Create an AWS account and administrative

user

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

## Step 2: Apply a managed policy for administrative access

to CodePipeline

You must grant permissions to interact with CodePipeline. The quickest way to do this is to apply
the `AWSCodePipeline_FullAccess` managed policy to the administrative user.

###### Note

The `AWSCodePipeline_FullAccess` policy includes permissions that allow the console user to pass an
IAM role to CodePipeline or other AWS services. This allows the service to assume the role and
perform actions on your behalf. When you attach the policy to a user, role, or group, the
`iam:PassRole` permissions are applied. Make sure the policy is only applied to
trusted users. When users with these permissions use the console to create or edit a
pipeline, the following choices are available:

- Create a CodePipeline service role or choose an existing one and pass the role to
  CodePipeline
- Might choose to create a CloudWatch Events rule for change detection and pass the CloudWatch Events service
  role to CloudWatch Events
  For more information, see [Granting
  a user permissions to pass a role to an AWS service](../../../IAM/latest/UserGuide/id_roles_use_passrole.md "../../../IAM/latest/UserGuide/id_roles_use_passrole.md").

###### Note

The `AWSCodePipeline_FullAccess` policy provides access to all CodePipeline actions and resources that the
IAM user has access to, as well as all possible actions when creating stages in a
pipeline, such as creating stages that include CodeDeploy, Elastic Beanstalk, or Amazon S3. As a best practice,
you should grant individuals only the permissions they need to perform their duties. For
more information about how to restrict IAM users to a limited set of CodePipeline actions and
resources, see [Remove permissions from the CodePipeline
service role](how-to-custom-role.md#remove-permissions-from-policy "how-to-custom-role.md#remove-permissions-from-policy").

To provide access, add permissions to your users, groups, or roles:

- Users and groups in AWS IAM Identity Center:

Create a permission set. Follow the instructions in [Create a permission set](../../../singlesignon/latest/userguide/howtocreatepermissionset.md "../../../singlesignon/latest/userguide/howtocreatepermissionset.md") in the _AWS IAM Identity Center User Guide_.

- Users managed in IAM through an identity provider:

Create a role for identity federation. Follow the instructions in [Create a role for a third-party identity provider (federation)](../../../IAM/latest/UserGuide/id_roles_create_for-idp.md "../../../IAM/latest/UserGuide/id_roles_create_for-idp.md")
in the _IAM User Guide_.

- IAM users:
  - Create a role that your user can assume. Follow the instructions in [Create a role for an IAM user](../../../IAM/latest/UserGuide/id_roles_create_for-user.md "../../../IAM/latest/UserGuide/id_roles_create_for-user.md") in the _IAM User Guide_.
  - (Not recommended) Attach a policy directly to a user or add a user to a user group. Follow the instructions in [Adding permissions to a user (console)](../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console "../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console") in the _IAM User Guide_.

## Step 3: Install the AWS CLI

To call CodePipeline commands from the AWS CLI on a local development machine, you must install
the AWS CLI. This step is optional if you intend to get started using only the steps in this
guide for the CodePipeline console.

###### To install and configure the AWS CLI

1. On your local machine, download and install the AWS CLI. This will enable you to
   interact with CodePipeline from the command line. For more information, see [Getting Set Up with the AWS Command
   Line Interface](../../../cli/latest/userguide/cli-chap-getting-set-up.md "../../../cli/latest/userguide/cli-chap-getting-set-up.md").

###### Note

CodePipeline works only with AWS CLI versions 1.7.38 and later. To determine which version of the AWS CLI that you may have installed, run the command **aws --version**. To upgrade an older version of the AWS CLI to the latest version,
follow the instructions in [Uninstalling the
AWS CLI](../../../cli/latest/userguide/cli-uninstall.md "../../../cli/latest/userguide/cli-uninstall.md"), and then follow the instructions in [Installing the AWS Command Line Interface](../../../cli/latest/userguide/installing.md "../../../cli/latest/userguide/installing.md"). 2. Configure the AWS CLI with the **configure** command, as follows:

```
aws configure
```

When prompted, specify the AWS access key and AWS secret access key of the IAM
user that you will use with CodePipeline. When prompted for the default region name, specify the
region where you will create the pipeline, such as `us-east-2`. When prompted
for the default output format, specify `json`. For example:

```
AWS Access Key ID [None]: `Type your target AWS access key ID here, and then press Enter`
AWS Secret Access Key [None]: `Type your target AWS secret access key here, and then press Enter`
Default region name [None]: `Type` us-east-2 `here, and then press Enter`
Default output format [None]: `Type` json `here, and then press Enter`
```

###### Note

For more information about IAM, access keys, and secret keys, see [Managing Access Keys for IAM
Users](../../../IAM/latest/UserGuide/ManagingCredentials.md "../../../IAM/latest/UserGuide/ManagingCredentials.md") and [How Do I Get
Credentials?](../../../IAM/latest/UserGuide/IAM_Introduction.md#IAM_SecurityCredentials "../../../IAM/latest/UserGuide/IAM_Introduction.md#IAM_SecurityCredentials").

For more information about the Regions and endpoints available for CodePipeline, see [AWS CodePipeline endpoints and quotas](../../../general/latest/gr/codepipeline.md "../../../general/latest/gr/codepipeline.md").

## Step 4: Open the console for CodePipeline

- Sign in to the AWS Management Console and open the CodePipeline console at [http://console.aws.amazon.com/codesuite/codepipeline/home](http://console.aws.amazon.com/codesuite/codepipeline/home "http://console.aws.amazon.com/codesuite/codepipeline/home").

## Next steps

You have completed the prerequisites. You can begin using CodePipeline. To start working with
CodePipeline, see the [CodePipeline tutorials](tutorials.md "tutorials.md").
