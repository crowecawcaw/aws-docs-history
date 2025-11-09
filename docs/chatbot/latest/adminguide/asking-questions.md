AWS Chatbot is now Amazon Q Developer. [Learn more](service-rename.md "service-rename.md")

# Chatting with Amazon Q Developer in chat channels

|                                                                          |
| ------------------------------------------------------------------------ |
| Chatting about network security is in preview, and is subject to change. |

By [adding Amazon Q Developer permissions](#cbt-awsq "#cbt-awsq") to your role settings and channel guardrails, you can get Artificial Intelligence (AI) powered answers to your natural language questions about:

- AWS services
- Your AWS resources
- Your costs
- Your telemetry and operations
- Network connectivity issues
- Network security
  Amazon Q Developer is available in Microsoft Teams and Slack channels configured with Amazon Q Developer.

###### Topics

- [Adding Amazon Q Developer in chat applications permissions](#cbt-awsq "#cbt-awsq")
- [Chatting about AWS](#service-questions-q "#service-questions-q")
- [Chatting about your AWS resources](#resource-questions-qdev "#resource-questions-qdev")
- [Chatting about your costs](#cost-questions "#cost-questions")
- [Chatting about your telemetry and operations](#telemetry "#telemetry")
- [Troubleshooting network connectivity issues](#troubleshoot-network "#troubleshoot-network")
- [Chatting about your network security](#network-security "#network-security")

## Adding Amazon Q Developer in chat applications permissions

To get AI powered answers to your questions about AWS and your AWS account resources, you must have the requisite permissions.

###### To chat with Amazon Q Developer in chat applications in natural language

1. Add the [AmazonQDeveloperAccess managed policy](../../../amazonq/latest/qdeveloper-ug/managed-policy.md#amazonq-policy-developeraccess "../../../amazonq/latest/qdeveloper-ug/managed-policy.md#amazonq-policy-developeraccess") to your IAM role:

###### Note

If you require administrator access, you can use the [AmazonQFullAccess managed policy](../../../amazonq/latest/qdeveloper-ug/managed-policy.md#amazonq-policy-fullaccess "../../../amazonq/latest/qdeveloper-ug/managed-policy.md#amazonq-policy-fullaccess").

    1. Open the [IAM console](https://console.aws.amazon.com/iam "https://console.aws.amazon.com/iam").
    2. In the navigation pane of the IAM console, choose **Roles**.
    3. Choose the name of the role you want to modify.
    4. In **Permissions policies**, choose **Add permissions** and **Attach policies**.
    5. Enter `AmazonQDeveloperAccess` in the search.
    6. Select **AmazonQDeveloperAccess**.
    7. Choose **Add permissions**.

2. Add the `AmazonQDeveloperAccess` managed policy to your channel guardrails:
   1. Open the [Amazon Q Developer in chat applications console](https://console.aws.amazon.com/chatbot "https://console.aws.amazon.com/chatbot").
   2. Choose a configured client.
   3. Select a configured channel.
   4. Choose **Set guardrails**.
   5. Enter `AmazonQDeveloperAccess` in the search.
   6. Select **AmazonQDeveloperAccess**.
   7. Choose **Save**.

3. In your chat channel, enter `@Amazon Q` and your question.

## Chatting about AWS

You can chat about best practices, recommendations, step-by-step instructions for AWS tasks, and architecting your AWS resources and workflows directly from your chat channels
using Amazon Q Developer.
Additionally, Amazon Q Developer can generate short scripts or code snippets to help you get started using AWS SDKs and AWS CLI.
For more information, see [Chatting with Amazon Q Developer about AWS](../../../amazonq/latest/qdeveloper-ug/chat-with-q.md "../../../amazonq/latest/qdeveloper-ug/chat-with-q.md") in the _Amazon Q Developer User Guide_.

### Commonly asked questions

You can ask Amazon Q Developer these service questions directly from your chat channels.

`@Amazon Q what is fargate?`

`@Amazon Q what’s the maximum runtime for a Lambda function?`

`@Amazon Q what’s the best container service to use to run my workload if I need to keep my costs low?`

`@Amazon Q how do I list my Amazon S3 buckets?`

## Chatting about your AWS resources

You can ask Amazon Q Developer about your AWS account resources. Amazon Q Developer can perform get, list, and describe actions to retrieve your AWS resources.
Amazon Q Developer can’t answer questions about the data stored in your resources, such as listing objects in an Amazon S3 bucket, or questions related to your account security, identity, credentials,
or cryptography. For more information, see [Chatting about your resources](../../../amazonq/latest/qdeveloper-ug/chat-actions.md "../../../amazonq/latest/qdeveloper-ug/chat-actions.md") in the _Amazon Q Developer User Guide_.

###### Note

Amazon Q Developer uses cross-region inference and cross-region calls to provide the service. For more information, see [Cross-region processing](../../../amazonq/latest/qdeveloper-ug/cross-region-processing.md "../../../amazonq/latest/qdeveloper-ug/cross-region-processing.md") in the _Amazon Q Developer User Guide_.

### Commonly asked questions

You can ask Amazon Q Developer these resource questions directly from your chat channels.

`@Amazon Q get the configuration for my lambda function `<name>`?`

`@Amazon Q what is the size of the auto scaling group `<name>` in us-east-2?`

`@Amazon Q can you show ec2 instances running in us-east-1?`

## Chatting about your costs

You can ask Amazon Q Developer about your AWS bill and account costs.
Amazon Q Developer can retrieve your cost data, explain costs, and analyze cost trends, so you can understand your costs without referring to documentation or
interrupting your workflow.
For more information, see [Chatting about your costs](../../../amazonq/latest/qdeveloper-ug/chat-costs.md "../../../amazonq/latest/qdeveloper-ug/chat-costs.md") in the _Amazon Q Developer User Guide_.

### Commonly asked questions

You can ask Amazon Q Developer these cost questions directly from your chat channels.

`@Amazon Q How much did we spend on SageMaker AI in January?`

`@Amazon Q What were my Amazon EC2 costs by instance type last week?`

`@Amazon Q What was my cost breakdown by service for the past three months?`

`@Amazon Q What were my cost trends by region over the last three months?`

## Chatting about your telemetry and operations

Amazon Q Developer analyzes your Amazon CloudWatch telemetry and operational data to help manage your AWS environment.
It retrieves resource health information, monitors alarms, and provides troubleshooting guidance.
When you ask questions, Amazon Q may prompt you for specific details like resource names and time ranges to ensure accurate assistance.
For more information, see [Chatting about your telemetry and operations](../../../amazonq/latest/qdeveloper-ug/chat-ops.md "../../../amazonq/latest/qdeveloper-ug/chat-ops.md") in the _Amazon Q Developer User Guide_.

### Commonly asked questions

You can ask Amazon Q Developer these telemetry and operations questions directly from your chat channels.

`@Amazon Q Is my Lambda function `<name>` healthy?`

`@Amazon Q Is anything wrong with my Amazon ECS clusters?`

`@Amazon Q Why is my alarm with name `<name>` firing?`

`@Amazon Q Is my Service `<name>`in environment`<name>` healthy?`

## Troubleshooting network connectivity issues

You can use Amazon Q Developer to help you diagnose network connectivity issues for applications that run in your virtual private clouds (VPCs).
For more information, see [Amazon Q network troubleshooting for Reachability Analyzer](../../../vpc/latest/reachability/amazon-q-network-reachability-analysis.md "../../../vpc/latest/reachability/amazon-q-network-reachability-analysis.md") in the _Amazon Virtual Private Cloud Reachability Analyzer_.

### Commonly asked questions

You can ask Amazon Q Developer these network connectivity questions directly from your chat channels.

`@Amazon Q Why can't I ssh into my Amazon EC2 instance?`

`@Amazon Q Why am I getting timeout errors when accessing my EC2 Windows instance via RDP?`

`@Amazon Q Why can't I access the internet from EC2 instance?`

`@Amazon Q Are my routes set up correctly to allow internet access?`

## Chatting about your network security

Amazon Q Developer helps you analyze your network security configurations, identify missing or misconfigured AWS network security services, and provides recommendations for a stronger network security posture.
You can understand network security findings, implement remediation steps, and follow security best practices without interrupting your workflow.

When you ask Amazon Q about your network security configurations,
responses include specific information about your resources, related security findings,
and detailed remediation instructions as well as links to learn more in the AWS Management Console.

For more information about network security analysis with Amazon Q, see [Get insights with Amazon Q Developer](../../../waf/latest/developerguide/nsd-security-insights.md "../../../waf/latest/developerguide/nsd-security-insights.md") in the _AWS Shield network security director Developer Guide_.

### Prerequisites

For Amazon Q to answer questions about your network security, you must also enable AWS Shield network security director.

#### Enable AWS Shield network security director

To chat about your network security configurations with Amazon Q, you must enable AWS Shield network security director in your AWS account.

###### To enable AWS Shield network security director

1. Open the [AWS Shield network security director console](https://console.aws.amazon.com/nsd/ "https://console.aws.amazon.com/nsd/").
2. Follow the setup instructions to enable the service.
3. Run a network analysis to collect information about your network security posture.

### Commonly asked questions

You can ask Amazon Q Developer these network security questions directly from your chat channels.

`@Amazon Q Identify my top network security findings`

`@Amazon Q Summarize the network security of my environment`

`@Amazon Q Are my systems at risk of DDoS attacks?`

`@Amazon Q How can I improve my network security?`
