

# Chatting with Amazon Q Developer in chat applications
<a name="q-in-chat-applications"></a>

You can chat with Amazon Q Developer in Microsoft Teams and Slack chat applications. In configured channels, Amazon Q can answer questions about best practices for building solutions, troubleshooting issues, and identifying next steps. The following Amazon Q chat features are available in configured chat applications: 
+ [Chatting about AWS](chat-with-q.md)
+ [Chatting about your resources with Amazon Q Developer](chat-actions.md)
+  [Troubleshooting resource issues](chat-actions-troubleshooting.md)
+ [Chatting about your costs](chat-costs.md)
+ [Chatting about your telemetry and operations](chat-ops.md)
+  [Amazon Q network troubleshooting for Reachability Analyzer](https://docs.aws.amazon.com/vpc/latest/reachability/amazon-q-network-reachability-analysis.html)

For more information about the complete set of features available when you use Amazon Q in chat applications, see [What is Amazon Q Developer in chat applications? ](https://docs.aws.amazon.com/chatbot/latest/adminguide/what-is.html) in the *Amazon Q Developer in chat applications Administrator Guide*.

**Note**  
When you use Amazon Q Developer in chat applications, access is limited to the Amazon Q Developer Free tier. 

## Enable Amazon Q chat in your channels
<a name="add-q"></a>

To add chat capabilities to a Microsoft Teams or Slack channel that is already configured with Amazon Q Developer, complete the following steps. To set up Amazon Q Developer in your chat applications for the first time and allow users to chat with Amazon Q, see [Get started with Microsoft Teams](https://docs.aws.amazon.com/chatbot/latest/adminguide/teams-setup.html) and [Get started with Slack](https://docs.aws.amazon.com/chatbot/latest/adminguide/slack-setup.html) in the *Amazon Q Developer in chat applications Administrator Guide*.

Before you can ask Amazon Q questions from a Microsoft Teams or Slack channel, you need to add Amazon Q to the channel. First, update your AWS Identity and Access Management (IAM) role settings to include the [AmazonQDeveloperAccess](managed-policy.md#amazonq-policy-developeraccess) managed policy, and then add the policy as a channel guardrail. If you need administrator access, add the [AmazonQFullAccess](managed-policy.md#amazonq-policy-fullaccess) policy instead. 

1. Add the `AmazonQDeveloperAccess` managed policy to your IAM role:

   1. Sign in to the AWS Management Console and open the [IAM console](https://console.aws.amazon.com/iam).

   1. In the navigation pane of the IAM console, choose **Roles**.

   1. Choose the name of the role that you want to modify.

   1. In **Permissions policies**, choose **Add permissions** and **Attach policies**.

   1. Enter `AmazonQDeveloperAccess` in the search.

   1. Select **AmazonQDeveloperAccess**.

   1. Choose **Add permissions**.

1. Add the `AmazonQDeveloperAccess` managed policy to your channel guardrails:

   1. Open the [Amazon Q Developer in chat applications console](https://console.aws.amazon.com/chatbot).

   1. Choose a configured client.

   1. Select a configured channel.

   1. Choose **Set guardrails**.

   1. Enter `AmazonQDeveloperAccess` in the search.

   1. Select **AmazonQDeveloperAccess**.

   1. Choose **Save**.

## Ask Amazon Q questions in your channel
<a name="ask-questions"></a>

To check that your configuration was successful, ask Amazon Q a question. Enter `@Amazon Q` followed by your question. 

Following are some examples of questions that you can ask Amazon Q from your configured channel:
+ `@Amazon Q how do I troubleshoot lambda concurrency issues?`
+ `@Amazon Q what are the best practices for securing S3 buckets?`
+ `@Amazon Q what is the maximum zipped file size for a lambda?`
+  `@Amazon Q get the configuration for my lambda function {{name}}? ` 
+  `@Amazon Q what is the size of the auto scaling group {{name}} in us-east-2?` 
+  `@Amazon Q can you show ec2 instances running in us-east-1?` 