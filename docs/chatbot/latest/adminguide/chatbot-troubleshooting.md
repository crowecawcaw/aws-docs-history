AWS Chatbot is now Amazon Q Developer. [Learn more](service-rename.md "service-rename.md")

# Troubleshooting Amazon Q Developer in chat applications

Amazon Q Developer in chat applications operates with multiple AWS services, including Amazon CloudWatch, Amazon GuardDuty, and CloudFormation. If
you encounter issues when trying to receive notifications, see the following topic for
troubleshooting help.

If you configured your AWS service to send notifications to the Amazon Simple Notification Service (Amazon SNS)
topics mapped to Amazon Q Developer in chat applications, but the notifications aren't appearing in the chat rooms or
channels, try the steps below.

**Possible causes**

- **There is no connectivity.**

Test your connectivity and your Amazon Q Developer in chat applications configuration by using the **Send
test message button** in the [Amazon Q Developer in chat applications
console](https://console.aws.amazon.com/chatbot/ "https://console.aws.amazon.com/chatbot/"). For more information, see [Test
notifications from AWS services to Amazon Chime](chime-setup.md#test-notifications "chime-setup.md#test-notifications"), [Test
notifications from AWS services to Microsoft Teams](teams-setup.md#test-notifications-teams "teams-setup.md#test-notifications-teams"), or [Test
notifications from AWS services to Slack](slack-setup.md#test-notifications-slack "slack-setup.md#test-notifications-slack").

- **The bot is not invited to the channel.**

Ensure that the Amazon Q Developer in chat applications app ("@Amazon Q") is added to the chat channel. If it hasn't,
in Microsoft Teams or Slack, add the Amazon Q Developer in chat applications app by choosing **Add apps** from the
channel's **Details** screen.

- **The notification's originating service is not supported by
  Amazon Q Developer in chat applications.**

For a list of supported services, see [Using
Amazon Q Developer in chat applications with Other AWS Services](related-services.md "related-services.md").

- **The SNS topic doesn't have a subscription to
  Amazon Q Developer in chat applications.**

In the Amazon SNS console, go to the **Topics** page, choose the
**Subscriptions** tab, and then verify that the topic has a
subscription. If the topic doesn't, open the Amazon Q Developer in chat applications console, open your authorized
client, and then look at the **Configured channels** or
**Configured webhooks** list. Add a new channel or webhook
configuration, and then add the SNS topic. Without this configuration, event
notifications can't reach the chat rooms.

- **The Amazon SNS topic has server-side encryption turned
  on.**

If you have server-side encryption enabled for your Amazon SNS topics, you must give permissions to the sending services in your AWS KMS key policy to post events to the encrypted SNS topics. The following policy is an example for EventBridge.

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

AWS managed service keys don’t allow you to modify access policies, so you will need AWS KMS/CMK for encrypted SNS topics.
You can then update the access permissions in the AWS KMS key policy to allow the service that sends messages to publish to your encrypted SNS topics (for example, EventBridge).

- **Your SNS topic subscription to the Amazon Q Developer in chat applications has the Enable raw
  message delivery setting enabled.**

Don't enable the **Enable raw message delivery**
feature for any SNS topic subscriptions to Amazon Q Developer in chat applications.

- **The event was throttled.**

Events can be throttled for the following reasons:

    + Slack has throttling limits that are applied per workspace. Workspaces can have multiple channels, so it's easy to exceed the limit. For more information, see
     [Rate Limits](https://api.slack.com/apis/rate-limits "https://api.slack.com/apis/rate-limits").
    + Amazon Q Developer in chat applications allows for 10 events per second. If more than 10 events per second are
     received, any event above 10 is throttled.

Even if Amazon Q Developer doesn't throttle the event while posting a message to Slack, Slack might because limits are applied at the workspace level.
To unsubscribe a channel or chat room from all Amazon Q Developer in chat applications notifications, remove the respective configuration from the Amazon Q Developer in chat applications console.
Otherwise, to identify certain service and notification-types to unsubscribe from, see [I don't want to receive notifications from certain services anymore.](#i-dont-want-to-receive-notifications-from-certain-services "#i-dont-want-to-receive-notifications-from-certain-services")

If you want to unsubscribe only some notifications from the channel or chatroom, you can remove specific SNS topics from the Amazon Q Developer in chat applications configuration.
Alternatively, you can remove the specific SNS topics as the event and alarm notification targets from the respective service configurations.
You should also check if you have Amazon EventBridge rules configured for the service event types and remove the specific SNS topics as the rule triggers targets.

**Possible causes**

- **The IAM role doesn’t have CloudWatchRead permissions.**

In the Amazon Q Developer in chat applications console, create a new role. This role requires the Notifications
permissions policy from the Amazon Q Developer in chat applications console when you configure a new webhook or Slack
channel. You can also edit your IAM role to [add the CloudWatchRead permissions](editing-iam-roles-for-chatbot.md "editing-iam-roles-for-chatbot.md") for Amazon Q Developer in chat applications.

- **Amazon Q Developer in chat applications doesn't have access to all AWS Regions.**

Amazon Q Developer in chat applications may execute API calls from any nearby AWS Region. If any Region is disabled,
you may experience problems with CloudWatch metrics graphs, among other issues. For more
information, see [I get AccessDenied or permissions
errors.](#chatbot-troubleshooting-regions "#chatbot-troubleshooting-regions")
If the AWS Billing and Cost Management console displays an error message for the SNS topic you want to use for
notifications, [you can edit the SNS topic's permissions policy so it can forward Budget
notifications.](../../../awsaccountbilling/latest/aboutv2/budgets-sns-policy.md "../../../awsaccountbilling/latest/aboutv2/budgets-sns-policy.md")

Do this if you have already configured an SNS topic that has a subscription to Amazon Q Developer in chat applications
or you've configured a new SNS topic. It is not needed if you want to use an Amazon SNS topic
that is already configured and working with AWS Billing and Cost Management. [You can then set up that topic with a subscription to Amazon Q Developer in chat applications](subscribe-sns-topic.md "subscribe-sns-topic.md").

Configuration names can't be edited. Names must be unique across your account.

**Possible causes**

- **You are missing some IAM permissions or trust
  relationships.**

Make sure you have the correct policies set up by following the instructions found
in [Setting up Amazon Q Developer in chat applications](getting-started.md#setting-up "getting-started.md#setting-up") and [Identity and Access Management for Amazon Q Developer in chat applications](security-iam.md "security-iam.md").

- **Amazon Q Developer in chat applications doesn't have access to all AWS Regions.**

Amazon Q Developer in chat applications is a global service and may execute API calls from any nearby AWS Region. If
any Region is disabled, you may experience errors. Make sure the IAM role you set up
for Amazon Q Developer in chat applications to assume has access to all Regions.

[Other policy types](security-iam.md#security-iam-other-policies "security-iam.md#security-iam-other-policies") can limit how IAM roles can be
assumed. If you have set up your Amazon Q Developer in chat applications IAM role to have global access but you're still
getting errors, one of these policy types may be the culprit:

    + **AWS Organizations service control policies (SCPs)** - SCPs are JSON
     policies that specify the maximum permissions for an organization or organizational
     unit (OU) in AWS Organizations. A service control policy could be overriding the policies you
     put in place for Amazon Q Developer in chat applications. See [How SCPs
     Work](../../../organizations/latest/userguide/orgs_manage_policies_about-scps.md "../../../organizations/latest/userguide/orgs_manage_policies_about-scps.md") in the *AWS Organizations User Guide*.
    + **IAM account settings**


    With IAM, you can use AWS Security Token Service (AWS STS) to create and provide trusted users
     with temporary security credentials that can control access to your AWS resources.
     When you activate STS endpoints for a Region, AWS STS can issue temporary credentials
     to users and roles in your account that make an AWS STS request. Those credentials can
     then be used in any Region that is enabled by default or is manually enabled. You
     must activate the Region in the account where the temporary credentials are
     generated. It does not matter whether a user is signed into the same account or a
     different account when they make the request. For more information, see [Activating and deactivating AWS STS in an AWS Region](../../../IAM/latest/UserGuide/id_credentials_temp_enable-regions.md#sts-regions-activate-deactivate "../../../IAM/latest/UserGuide/id_credentials_temp_enable-regions.md#sts-regions-activate-deactivate") in the
     *IAM User Guide*.

If there is a policy in place that prevents access to services in certain Regions, you
must change the policy to allow global Amazon Q Developer in chat applications access.

For example, the policy below allows Amazon Q Developer in chat applications in **us-east-2** but denies
other services by using a [NotAction](../../../IAM/latest/UserGuide/reference_policies_elements_notaction.md "../../../IAM/latest/UserGuide/reference_policies_elements_notaction.md")
element.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Deny",
 "NotAction": [
 "chatbot:*"
 ],
 "Resource": [
 "*"
 ],
 "Condition": {
 "StringEquals": {
 "aws:RequestedRegion": [
 "us-east-2"
 ]
 }
 }
 }
 ]
}`

```

**Possible causes**

- **The notification's originating service is not supported by
  Amazon Q Developer in chat applications.**

For a list of supported services, see [Monitoring AWS services](related-services.md "related-services.md"). You can also send customized notifications for these services using custom notifications. For more information, see [Custom notifications using Amazon Q Developer in chat applications](custom-notifs.md "custom-notifs.md").

- **The service event is modified.**

Amazon Q Developer in chat applications only supports default service events. If you need to modify a service event or send custom notifications, send the message using the custom notifications event schema. For more information, see [Custom notifications using Amazon Q Developer in chat applications](custom-notifs.md "custom-notifs.md").
**Possible causes**

- **The Amazon Q Developer in chat applications app is not added to the Slack
  workspace.**

Add the Amazon Q Developer in chat applications app to the Slack workspace. For more information, see the [Getting started guide for Amazon Q Developer in chat applications](getting-started.md "getting-started.md").
**Possible causes**

- **A new scope change requires administrator
  approval.**

There may be a new scope added to the Amazon Q Developer in chat applications Slack application that requires approval
by an administrator. If Amazon Q Developer in chat applications has released a new scope, administrators need to
re-approve the Amazon Q Developer in chat applications Slack application. Note that the approval is only required for
Slack workspaces with an app approval policy.

Workspace administrators can check their workspace settings to review and approve

new scopes for Amazon Q Developer in chat applications. For more information about how to approve an app, see [Approve or restrict an app at the org level](https://slack.com/help/articles/360000281563-Manage-apps-on-Enterprise-Grid#approve-or-restrict-an-app "https://slack.com/help/articles/360000281563-Manage-apps-on-Enterprise-Grid#approve-or-restrict-an-app") in the Slack Help Center.

- **Installation of the Amazon Q Developer in chat applications Slack app is restricted for your
  workspace.**

This error may appear if the workspace administrator has explicitly restricted the
installation of the Amazon Q Developer in chat applications Slack app.
Microsoft Teams doesn't currently support Amazon Q Developer in chat applications in private channels.
For more information, see [Private channel limitations](https://learn.microsoft.com/en-us/microsoftteams/private-channels#private-channel-limitations "https://learn.microsoft.com/en-us/microsoftteams/private-channels#private-channel-limitations").

## Provide feedback

You can provide feedback about Amazon Q Developer in chat applications directly from your Amazon Chime chat room, chat
channels, or from the Amazon Q Developer in chat applications console. To leave feedback from your Amazon Chime chat room or
chat channel, type the following command and replace `comments` with
your own information.

```
@Amazon Q feedback `comments`
```

To leave feedback from the Amazon Q Developer in chat applications console, navigate to the [Amazon Q Developer in chat applications console](https://console.aws.amazon.com/chatbot/ "https://console.aws.amazon.com/chatbot/") and choose the **Feedback** link
at the bottom of the console. All feedback is sent directly to and reviewed by the Amazon Q Developer in chat applications
team.
