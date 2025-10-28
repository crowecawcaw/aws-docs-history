# Setting up Amazon DevOps Guru

Complete the tasks in this section to set up Amazon DevOps Guru for the first time. If you already
have an AWS account, know which AWS account or accounts you want to analyze, and have an
Amazon Simple Notification Service topic to use for insight notifications, you can skip ahead to [Getting started with DevOps Guru](getting-started.md "getting-started.md").

Optionally, you can use Quick Setup, a capability of AWS Systems Manager, to set up DevOps Guru and quickly
configure its options. You can use Quick Setup to set up DevOps Guru for a standalone account or an organization.
To use Quick Setup in Systems Manager to set up DevOps Guru for an organization, you must have the following prerequisites
in place:

- An organization with AWS Organizations. For more information, see [AWS Organizations
  terminology and concepts](../../../organizations/latest/userguide/orgs_getting-started_concepts.md "../../../organizations/latest/userguide/orgs_getting-started_concepts.md") in the _AWS Organizations User
  Guide_.
- Two or more organizational units (OUs).
- One or more target AWS accounts in each OU.
- One administrator account with privileges to manage the target accounts.
  To learn how to set up DevOps Guru using Quick Setup, see [Configure DevOps Guru with
  Quick Setup](../../../systems-manager/latest/userguide/quick-setup-devops.md "../../../systems-manager/latest/userguide/quick-setup-devops.md") in the _AWS Systems Manager User Guide_.

Use the following steps to set up DevOps Guru without Quick Setup.

- [Step 1 – Sign up for AWS](#setting-up-aws-sign-up "#setting-up-aws-sign-up")
- [Step 2 – Determine coverage for
  DevOps Guru](#setting-up-determine-coverage "#setting-up-determine-coverage")
- [Step 3 – Identify your Amazon SNS
  notifications topic](#setting-up-notifications "#setting-up-notifications")

## Step 1 – Sign up for AWS

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

## Step 2 – Determine coverage for

DevOps Guru

Your boundary coverage determines the AWS resources that are analyzed by Amazon DevOps Guru
for anomalous behavior. We recommend that you group your resources into your operational
applications. All the resources in your resource boundary should comprise one or more of
your applications. If you have one operational solution, then your coverage boundary
should include all of its resources. If you have multiple applications, choose the
resources that make up each solution and group them together using AWS CloudFormation stacks or AWS
tags. All of the combined resources you specify, whether they define one or more
applications, are analyzed by DevOps Guru and make up its coverage boundary.

Use one of the following methods to specify the resources in your operational
solutions.

- Choose to have your AWS Region and account define your coverage boundary.
  With this option, DevOps Guru analyzes all resources in your account and
  Region. This is a good option to choose if you use your account for only one
  application.
- Use AWS CloudFormation stacks to define the resources in your operational application.
  AWS CloudFormation templates define and generate your resources for you. Specify the stacks
  that create your application resources when you configure DevOps Guru. You can update
  your stacks at any time. All of the resources in the stacks that you choose
  define your boundary coverage. For more information, see [Using AWS CloudFormation stacks to identify resources in your DevOps Guru applications](working-with-cfn-stacks.md "working-with-cfn-stacks.md").
- Use AWS tags to specify AWS resources in your applications. DevOps Guru analyzes
  only the resources that contain the tags you choose. Those resources make up
  your boundary.

An AWS tag consists of a tag _key_ and a tag _value_. You can
specify one tag _key_ and you can specify one or more _values_ with that
_key_. Use one _value_ for all the resources in one of your
applications. If you have multiple applications, then use a tag with the same
_key_ for all of them, and group the resources into your applications using
the tags' _values_. All of the resources with the tags that you choose make
up the coverage boundary for DevOps Guru. For more information, see [Using tags to identify resources in your DevOps Guru
applications](working-with-resource-tags.md "working-with-resource-tags.md").

If your boundary coverage includes resources that make up more than one application,
you can use tags to filter your insights by to view them by one application at a time.
For more information, see Step 4 in [Viewing DevOps Guru insights](working-with-insights.md#view-insights "working-with-insights.md#view-insights").

For more information, see [Defining applications using AWS
resources](working-with-resource-collections.md "working-with-resource-collections.md").
For more
information about the supported services and resources, see
[Amazon DevOps Guru pricing](https://aws.amazon.com/devops-guru/pricing/ "https://aws.amazon.com/devops-guru/pricing/").

## Step 3 – Identify your Amazon SNS

notifications topic

You use one or two Amazon SNS topics to generate notifications about important DevOps Guru
events, such as when an insight is created. This ensures you know about issues that
DevOps Guru finds as soon as possible. Have your topics ready when you set up DevOps Guru. When you
use the DevOps Guru console to set up DevOps Guru, you specify a notification topic using its name
or its Amazon Resource Name (ARN). For more information, see [Enable
DevOps Guru](getting-started-enable-service.md "getting-started-enable-service.md"). You can use the Amazon SNS console to view the name and ARN for each of
your topics. If you don't have a topic, you can create one when you enable DevOps Guru using
the DevOps Guru console. For more information, see [Creating a topic](../../../sns/latest/dg/sns-tutorial-create-topic.md "../../../sns/latest/dg/sns-tutorial-create-topic.md") in the
_Amazon Simple Notification Service Developer Guide_.

### Permissions added

to your Amazon SNS topic

An Amazon SNS topic is a resource that contains
an AWS Identity and Access Management (IAM) resource policy. When you specify a topic here, DevOps Guru appends the following permissions
to its resource policy.

```
{
    "Sid": "DevOpsGuru-added-SNS-topic-permissions",
    "Effect": "Allow",
    "Principal": {
        "Service": "region-id.devops-guru.amazonaws.com"
    },
    "Action": "sns:Publish",
    "Resource": "arn:aws:sns:`region-id`:`topic-owner-account-id`:`my-topic-name`",
    "Condition" : {
      "StringEquals" : {
        "AWS:SourceArn": "arn:aws:devops-guru:`region-id`:`topic-owner-account-id`:channel/`devops-guru-channel-id`",
        "AWS:SourceAccount": "`topic-owner-account-id`"
    }
  }
}
```

These permissions are required for DevOps Guru to publish notifications using a topic. If you prefer to not have
these permissions on the topic, you can safely remove them and the topic will continue to work as it did
before you chose it. However, if these appended permissions are removed, DevOps Guru cannot use the topic to
generate notifications.
