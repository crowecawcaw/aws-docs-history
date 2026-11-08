

# What is the AWS assistant?
<a name="what-is"></a>

**Amazon Q Developer in the AWS Management Console is now the AWS assistant**  
Amazon Q Developer in the AWS Management Console is now the AWS assistant. You can use the AWS assistant in the AWS Management Console and AWS Console Mobile Application.  
Technical names didn't change. The `q` prefix still appears in AWS Identity and Access Management (IAM) actions and managed policies. It also appears in service principals, ARNs, AWS CloudTrail events, and resource names.

Use the AWS assistant, a generative AI-powered assistant, in the AWS Management Console and AWS Console Mobile Application. Ask questions in plain language to learn about AWS services. In the AWS Management Console, you can also ask about your resources and costs, fix problems, and contact AWS Support.

The AWS assistant can help you:
+ Learn about AWS architecture, services, recommended practices, and documentation.
+ Retrieve and analyze information about resources that your identity has permission to access.
+ Analyze historical and forecasted costs, identify optimization opportunities, and understand AWS pricing.
+ Troubleshoot resources, alarms, telemetry, and supported console errors.
+ Review email-delivery information for supported services.
+ Create an AWS Support case and transfer to a support agent when your support offering permits it.
+ Generate short scripts and code snippets for AWS SDKs and the AWS Command Line Interface.

For complex resource questions, the AWS assistant creates a sequence of steps and explains the reasoning behind each one. If the first approach fails, it tries another method or asks you for more information.

For example, you can ask "What SQS queues invoke my AWS Lambda functions?" The AWS assistant makes read-only get, list, and describe calls to AWS Lambda and Amazon Simple Queue Service (Amazon SQS). It explains each step and then summarizes which queues invoke which functions.

To get started, see [Getting started with the AWS assistant](getting-started.md).

To learn about features, see [Using the AWS assistant](using-assistant.md). To control access and protect data, see [Security in the AWS assistant](security.md). For help with problems, see [Troubleshooting access, permission, and response errors in the AWS assistant](troubleshooting.md) and [Contacting AWS Support with the AWS assistant](support.md).

The AWS assistant is available at the Free and Pro tiers. For tier requirements, see [[Optional] Step 3: Review Pro tier access](getting-started.md#subscription-access).

The AWS assistant is constantly updating its capabilities so your questions get the most contextually relevant and actionable answers.

**Note**  
Features vary between the AWS Management Console and the AWS Console Mobile Application. Each topic in this guide says where a feature is available. The AWS assistant name doesn't apply to Amazon Q Developer in the IDE or on the command line, Amazon Q Developer in chat applications, Kiro, Amazon Q Business, Amazon Quick, AWS Transform, or other independently branded products.