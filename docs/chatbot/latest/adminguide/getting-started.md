

AWS Chatbot is now Amazon Q Developer. [Learn more](service-rename.md)

# Getting started with Amazon Q Developer in chat applications
<a name="getting-started"></a>

To get started using Amazon Q Developer in chat applications to help manage your AWS infrastructure, follow the steps below to set up Amazon Q Developer in chat applications with chat channels and Amazon SNS topic subscriptions.

**Topics**
+ [Setting up Amazon Q Developer in chat applications](#setting-up)
+ [Tutorial: Get started with Amazon Chime](chime-setup.md)
+ [Tutorial: Get started with Microsoft Teams](teams-setup.md)
+ [Tutorial: Get started with Slack](slack-setup.md)
+ [Tutorial: Create or configure an Amazon Simple Notification Service topic as a notification target for Microsoft Teams and AWS CodeStar](teams-codestar.md)
+ [Tutorial: Subscribing an Amazon SNS topic to Amazon Q Developer in chat applications](subscribe-sns-topic.md)
+ [Test notifications from AWS services to chat channels using CloudWatch](test-notifications-cw.md)
+ [Next steps](#next-steps-gettingStarted)

## Setting up Amazon Q Developer in chat applications
<a name="setting-up"></a>

To use Amazon Q Developer in chat applications, you authorize a chat client configuration with Amazon Q Developer in chat applications, and optionally configure Amazon Q Developer in chat applications to use an Amazon Simple Notification Service (Amazon SNS) topic to deliver notifications to the chat channels. Before you can get started, you must complete the following setup tasks.

### Prerequisites
<a name="chatbot-prereqs"></a>

With Amazon Q Developer in chat applications, you can use chat channels to monitor and respond to events in your AWS Cloud.

The following list identifies prerequisites you should have before you begin using Amazon Q Developer in chat applications:
+ You have started using some AWS services. For more information about AWS services you can use with Amazon Q Developer in chat applications, see [Monitoring AWS services using Amazon Q Developer in chat applications](related-services.md).
+ You have administrator privileges with your chosen chat client chat room, tenant, or workspace.
+ You understand Amazon Q Developer in chat applications's permission schemes. For more information about Amazon Q Developer in chat applications's permission schemes, see [Understanding permissions](understanding-permissions.md).

If you have an existing AWS administrator user, you can access the Amazon Q Developer in chat applications console with no additional permissions. AWS recommends that you grant only the permissions required to perform a task for other users. For more information, see [Apply least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#grant-least-privilege) in the *AWS Identity and Access Management User Guide*.

### Sign up for an AWS account
<a name="sign-up-for-aws"></a>

To get started with AWS, you need an AWS account. For information about creating an AWS account, see [Getting started with an AWS account](https://docs.aws.amazon.com/accounts/latest/reference/getting-started.html) in the *AWS Account Management Reference Guide*.

### Setting up IAM permissions for Amazon Q Developer in chat applications
<a name="chatbot-iam"></a>

If you would like to add Amazon Q Developer in chat applications access to an existing user or group, you can choose from allowed Amazon Q Developer in chat applications actions in IAM.

If you need to customize an IAM role to work with Amazon Q Developer in chat applications, [you can use the procedure in this topic](editing-iam-roles-for-chatbot.md).

If you want to chat with Amazon Q Developer in natural language from your chat channels, make sure to add the `AmazonQDeveloperAccess` policy to your IAM role. You must also ensure that your channel guardrail policies allow `AmazonQDeveloperAccess` permissions. For more information, see [Chatting with Amazon Q Developer in chat channels](asking-questions.md).

**To create a policy to configure Amazon Q Developer in chat applications**

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

1. Choose **Policies** from the navigation pane.

1. Choose **Create policy**.

1. Expand **Service** and find **Chatbot**.

1. Under **Actions**, expand the **Read** and **Write** sections to see the available actions.

   **Read** actions include **DescribeChimeWebhookConfigurations**, **DescribeSlackChannelConfigurations**, **DescribeTeamsChannelConfiguration**, and more.

   **Write** actions include **CreateChimeWebhookConfiguration**, **DeleteChimeWebhookConfiguration**, and more.

1. After selecting the actions you want to include, choose **Review policy**.

1. Give your policy a name and description, then choose **Create policy**. You can now add your new policy to any of your users or groups.

For more information on updating the permissions of existing users, see [Adding Permissions to a User (Console)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_change-permissions.html#users_change_permissions-add-console) in the *IAM User Guide*.

**Note**  
 Amazon Q Developer in chat applications requires access to all AWS Regions. If there is a policy in place that prevents access to services in certain Regions, you must change the policy to allow global Amazon Q Developer in chat applications access. For more information about policy types that might limit how IAM roles can be assumed and how to override them, see [Other policy types](security-iam.md#security-iam-other-policies). 

### Setting up Amazon SNS topics
<a name="chatbot-sns"></a>

To use Amazon Q Developer in chat applications, you must have Amazon SNS topics set up. If you don't have any Amazon SNS topics yet, follow the steps to get started in [Getting Started with Amazon SNS](https://docs.aws.amazon.com/sns/latest/dg/sns-getting-started.html) in the *Amazon Simple Notification Service Developer Guide*.

**Note**  
Amazon Q Developer in chat applications doesn't support SNS FIFO topics because these topics can't deliver messages to HTTPS endpoints. For more information, see [Message delivery for FIFO topics](https://docs.aws.amazon.com/sns/latest/dg/fifo-message-delivery.html) in the *Amazon Simple Notification Service Developer Guide*.

If you have server-side encryption enabled for your Amazon SNS topics, you must give permissions to the sending services in your AWS KMS key policy to post events to the encrypted SNS topics. The following policy is an example for Amazon EventBridge.

```
{
  "Sid": "Allow CWE to use the key",
  "Effect": "Allow",
  "Principal": {
    "Service": "events.amazonaws.com"
  },
  "Action": [
    "kms:Decrypt",
    "kms:GenerateDataKey"
  ],
  "Resource": "*"
}
```

In order to successfully test the configuration from the console, your role must also have permission to use the AWS KMS key.

AWS managed service keys don’t allow you to modify access policies, so you will need AWS KMS/CMK for encrypted SNS topics. You can then update the access permissions in the AWS KMS key policy to allow the service that sends messages to publish to your encrypted SNS topics (for example, EventBridge).

## Next steps
<a name="next-steps-gettingStarted"></a>

Once you've taken the necessary steps to set up Amazon Q Developer in chat applications, you can get started configuring the chat client of your choice. For a step-by-step guide on how to do this, choose the appropriate tutorial below:
+ [Tutorial: Get started with Slack](slack-setup.md)
+ [Tutorial: Get started with Amazon Chime](chime-setup.md)
+ [Tutorial: Get started with Microsoft Teams](teams-setup.md)