AWS Chatbot is now Amazon Q Developer. [Learn more](service-rename.md "service-rename.md")

# Amazon Q Developer in chat applications Service-linked role for performing operations on Amazon SNS topics and CloudWatch Logs

Amazon Q Developer uses the service-linked role named **AWSServiceRoleForAWSChatbot**. This is a managed IAM policy with scoped permissions that Amazon Q Developer in chat applications needs to run in customers’ accounts.

## Service-Linked Role Permissions for

Amazon Q Developer

The Amazon Q Developer in chat applications service-linked role gives permissions for the following services and
resources:

- Amazon SNS notifications
- CloudWatch Logs

These permissions allow Amazon Q Developer in chat applications to perform operations on Amazon SNS topics and CloudWatch Logs.

Administrators can view, but can't edit, the permissions for the Amazon Q Developer in chat applications
service-linked role.

The **AWSServiceRoleForAWSChatbot** service-linked role provides trust
permissions to the following service to assume its role:

- `management.chatbot.amazonaws.com`

You must configure permissions to allow an IAM entity (such as a user, group, or role)
to create, edit, or delete a service-linked role. For more information, see [Service-Linked Role Permissions](../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions "../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions") in the
_IAM User Guide_.

When you create an Amazon Q Developer in chat applications configuration, it creates the following policy for
the service-linked role:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "sns:ListSubscriptionsByTopic",
 "sns:ListTopics",
 "sns:Unsubscribe",
 "sns:Subscribe",
 "sns:ListSubscriptions"
 ],
 "Effect": "Allow",
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "logs:PutLogEvents",
 "logs:CreateLogStream",
 "logs:DescribeLogStreams",
 "logs:CreateLogGroup",
 "logs:DescribeLogGroups"
 ],
 "Resource": "arn:aws:logs:*:*:log-group:/aws/chatbot/*"
 }
 ]
}`

```

You don't need to take any action to support this role beyond using the Amazon Q Developer in chat applications service.

## Enabling the service-linked role for Amazon Q Developer

When you configure Amazon Q Developer in chat applications for the first time, you configure a Microsoft Teams channel, a Slack channel, or Amazon Chime
webhook to work with Amazon Simple Notification Service (Amazon SNS) topics for forwarding notifications to chat rooms. When
you create the first resource, Amazon Q Developer in chat applications automatically creates the IAM service-linked role,
which can be seen in the IAM console. You don't need to manually create or configure this
role.

## Editing a service-linked role for Amazon Q Developer

You can't edit the **AWSServiceRoleForAWSChatbot** service-linked role. You also can't change its
name, because other entities might reference it. You can edit the role's description using the
IAM console. For more information, see [Editing
a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role") in the _IAM User Guide_.

## Manually deleting the AWSServiceRoleForAWSChatbot service-linked role

Under specific circumstances, you can manually delete the **AWSServiceRoleForAWSChatbot** service-linked role.
If you no longer need to use any feature or service that requires a service-linked role, we
recommend that you delete that role. Doing so prevents having an unused entity that is not
actively maintained in your account.

To delete the Amazon Q Developer in chat applications service-linked role, you must delete all Amazon Q Developer in chat applications resources in your AWS
account, including all Slack channels and Amazon Chime webhooks. You can delete all Amazon Q Developer in chat applications resources
using the Amazon Q Developer in chat applications console, and then use the IAM console or AWS Command Line Interface (AWS CLI) to delete the
service-linked role.

###### Note

If Amazon Q Developer is using the **AWSServiceRoleForAWSChatbot** service-linked role when you try
to delete its resources, the deletion might fail. If that happens, wait a few minutes and
try deleting it again.

###### To delete Amazon Q Developer in chat applications resources

1. [Open the Amazon Q Developer in chat applications console](https://us-east-2.console.aws.amazon.com/chatbot/home?region=us-east-2#/chat-clients "https://us-east-2.console.aws.amazon.com/chatbot/home?region=us-east-2#/chat-clients").
2. To remove Amazon Chime webhook configurations, do the following:
   1. Choose **Amazon Chime**.
   2. Choose each webhook that you need to delete and choose **Delete
      webhook**. You can delete one at a time.
   3. Choose **Delete** to confirm the deletion.
   4. Repeat these steps to delete all webhook configurations.

3. To remove Slack channel configurations, do the following:
   1. Choose **Slack**.
   2. Choose the channel that you need to delete and choose **Delete
      channel**.
   3. Choose **Delete** to confirm the deletion.
   4. Repeat these steps to delete all Slack channel configurations.###### Note

If you delete the Amazon Q Developer in chat applications service-linked role, and then need to use it again, simply
open the Amazon Q Developer in chat applications console and create a new Slack channel or Amazon Chime webhook resource to recreate
the role in your account. When you create the first new resource in Amazon Q Developer, it
creates the service-linked role for you again. 4. To delete the **AWSServiceRoleForAWSChatbot** service-linked role, use the IAM console or
the AWS Command Line Interface (AWS CLI) . For information, see [Deleting
a Service-Linked Role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role") in the _IAM User Guide_.

## Supported regions for Amazon Q Developer service-linked roles

AWSServiceRoleForAWSChatbot doesn't support using service-linked roles in every AWS Region where the
service is available. The following table shows the Regions where you can use the
**AWSServiceRoleForAWSChatbot**.

| Region Name               | Region Identity | Supported in Amazon Q Developer |
| ------------------------- | --------------- | ------------------------------- |
| US East (N. Virginia)     | us-east-1       | Yes                             |
| US East (Ohio)            | us-east-2       | Yes                             |
| US West (N. California)   | us-west-1       | Yes                             |
| US West (Oregon)          | us-west-2       | Yes                             |
| Asia Pacific (Mumbai)     | ap-south-1      | Yes                             |
| Asia Pacific (Osaka)      | ap-northeast-3  | Yes                             |
| Asia Pacific (Seoul)      | ap-northeast-2  | Yes                             |
| Asia Pacific (Singapore)  | ap-southeast-1  | Yes                             |
| Asia Pacific (Sydney)     | ap-southeast-2  | Yes                             |
| Asia Pacific (Tokyo)      | ap-northeast-1  | Yes                             |
| Canada (Central)          | ca-central-1    | Yes                             |
| Europe (Frankfurt)        | eu-central-1    | Yes                             |
| Europe (Ireland)          | eu-west-1       | Yes                             |
| Europe (London)           | eu-west-2       | Yes                             |
| Europe (Paris)            | eu-west-3       | Yes                             |
| South America (São Paulo) | sa-east-1       | Yes                             |
| AWS GovCloud (US)         | us-gov-west-1   | No                              |
