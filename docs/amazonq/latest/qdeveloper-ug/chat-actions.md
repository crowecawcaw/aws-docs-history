# Chatting about your resources with Amazon Q Developer

Amazon Q Developer answers questions about your AWS account resources to help you understand your
AWS infrastructure through natural language prompts. Using advanced reasoning capabilities,
Amazon Q analyzes and provides insights about your resources so you can quickly get the
information you need without relying on multiple service consoles, APIs, or complicated
scripts.

The type of resource analysis Amazon Q can perform includes:

- **Resource listing and details** – Ask for lists or
  specific details about resources in your account.
- **Filtered queries** – Request resource information based on criteria such as region or configuration state.
- **Cross-service analysis** – Ask complex questions
  about your infrastructure, configurations, and dependencies across multiple
  AWS resources and services.
- **Troubleshooting assistance** – Get help identifying
  and resolving issues with your resources. For more
  information, see [Asking Amazon Q to troubleshoot your
  resources](chat-actions-troubleshooting.md "chat-actions-troubleshooting.md").
  For examples of questions you can ask, see
  [Ask Amazon Q for resource information](#ask-resource-questions "#ask-resource-questions").

###### Topics

- [How it works](#how-chat-actions-works "#how-chat-actions-works")
- [Prerequisites](#resoure-chat-prereqs "#resoure-chat-prereqs")
- [Ask Amazon Q for resource information](#ask-resource-questions "#ask-resource-questions")
- [Count resources with AWS Resource Explorer](#count-resources "#count-resources")

## How it works

To respond to questions about resources, Amazon Q uses service APIs and AWS Cloud Control API to
retrieve the requested information. To allow Amazon Q to call the APIs required to retrieve
requested resource information, your IAM identity must have permissions to use those APIs.
For more information, see [Prerequisites](#resoure-chat-prereqs "#resoure-chat-prereqs").

Amazon Q can perform get, list, and describe actions to retrieve information about
multiple AWS resources at a time. When asked complex resource questions, Amazon Q
creates dynamic, multi-step plans that explain the reasoning behind the actions it’s
taking to further your understanding of your AWS environment. If the initial plan fails,
Amazon Q attempts alternative methods or prompts you for any additional information
required to continue.

Amazon Q can’t answer questions about the data stored in your resources, such as listing
objects in an Amazon S3 bucket, or questions related to your account security, identity,
credentials, or cryptography.

## Prerequisites

You can chat about your account resources with Amazon Q in the AWS Management Console, AWS Console Mobile Application, and
in [configured chat applications](q-in-chat-applications.md "q-in-chat-applications.md").

To chat about your resources, your IAM identity must have the following permissions:

- Permissions to chat with Amazon Q, to use Cloud Control API, and to allow Amazon Q to access your
  resources. For an IAM policy that grants the required permissions, see
  [Allow users to chat about
  resources with Amazon Q](id-based-policy-examples-users.md#id-based-policy-examples-allow-resource-chat "id-based-policy-examples-users.md#id-based-policy-examples-allow-resource-chat").
- Permissions to access the resources you ask about. For example, if you ask
  Amazon Q to list your Amazon S3 buckets, you must have the
  `s3:ListAllMyBuckets` permission.

Amazon Q will never access resources that your IAM identity doesn't have
access to.

###### Important

Normal fees apply when you ask Amazon Q to perform read, list, or describe
actions. For more information, see the pricing page for the AWS service you
are asking Amazon Q about.

## Ask Amazon Q for resource information

When you ask Amazon Q about your resources, you can specify the AWS Region that Amazon Q
calls to locate your resources. If no Region is specified in a given query, Amazon Q
will use a Region previously specified in your conversation if applicable, and otherwise
uses your current console Region (or the most recent console Region if you are using a
global console Region).

Amazon Q might need additional information to answer to your resource questions. When Amazon Q asks
a follow up, reply with the requested details.

Following are example questions you can ask Amazon Q about your resources:

- Describe the encryption settings for S3 bucket
  `<name>`
- What SQS queues invoke my Lambda functions?
- Do I have any MySQL RDS clusters that need updates?
- List my EC2 instances in `<region>`
- Get the configuration for my lambda function
  `<name>`
- What alarms are configured for instance `<instance
ID>`?

## Count resources with AWS Resource Explorer

When you ask a question that requires resource counting, such as 'How many EC2
resources are running in my account?', Amazon Q uses Cloud Control API by default to return a count
of the requested resources. You also have the option to enable and configure Resource Explorer for
faster resource counting with Amazon Q.

If Resource Explorer is enabled, Amazon Q will attempt to use it when generating a response that
requires counting your resources. Amazon Q can use Resource Explorer to count a single type of
resource across all AWS Regions. Using Resource Explorer enables Amazon Q to count resources faster
by returning the count from the Resource Explorer index, as opposed to calling service APIs to list
resources and count the results.

If you choose to enable Resource Explorer for resource counting, note that resource information
can be out of date. Resource Explorer indexes resources in your account by taking a periodic
inventory, and if resources have been created or deleted after the last inventory, the
resource count will be incorrect. Resource Explorer also doesn't support resource filtering. If
you ask to count resources matching a specific criteria, Amazon Q will fall back to Cloud Control API.

If you don't have Resource Explorer enabled and configured for use, or if Amazon Q can't use Resource Explorer
to answer your question, Amazon Q uses Cloud Control API to count resources. Using Cloud Control API ensures an
accurate resource count and supports resource filtering, however this can also lead to
increased latency compared to counting with Resource Explorer. If you are counting a large number
of resources, Cloud Control API can also time out.

To use Resource Explorer for resource counting, the following configuration is required:

- The user interacting with Amazon Q must be in account where an Resource Explorer default
  view is configured and an aggregator index has been created in the same Region
  as the default view. For more information, see [Setting up Resource Explorer using Advanced setup](../../../resource-explorer/latest/userguide/getting-started-setting-up.md#getting-started-setting-up-advanced "../../../resource-explorer/latest/userguide/getting-started-setting-up.md#getting-started-setting-up-advanced") in the _AWS Resource Explorer
  User Guide_.
- The user's IAM identity must have read permissions for the default view. For
  more information, see
  [Granting access to Resource Explorer views for search](../../../resource-explorer/latest/userguide/configure-views-grant-access.md "../../../resource-explorer/latest/userguide/configure-views-grant-access.md") in the _AWS Resource Explorer User Guide_.
