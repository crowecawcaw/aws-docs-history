AWS Chatbot is now Amazon Q Developer. [Learn more](service-rename.md "service-rename.md")

# IAM policies for Amazon Q Developer in chat applications

This section describes the IAM permissions and policies that Amazon Q Developer in chat applications uses to secure its
operations with other AWS services. Amazon Q Developer in chat applications uses these permissions to safely forward Amazon SNS
notifications to chat rooms, support AWS CLI commands sessions in Slack, invoke Lambda
functions, and create AWS support tickets directly in the Slack console. You can also
define your own custom policies for the same purposes, using these policies as
templates.

When you create a new role in the Amazon Q Developer in chat applications console, any of the IAM policies described in
this topic might be assigned to that role. You could apply all of them to a single role, or
choose only a couple of them based on how the users of that role will use the Amazon Q Developer in chat applications. Some
policies contain a superset of permissions of other policies.

###### Topics

- [AWS managed IAM policies in
  Amazon Q Developer in chat applications](#aws-managed-policies-for-chatbot "#aws-managed-policies-for-chatbot")
- [Customer managed IAM policies in
  Amazon Q Developer in chat applications](#user-managed-chatbot-iam-policies "#user-managed-chatbot-iam-policies")

## AWS managed IAM policies in

Amazon Q Developer in chat applications

Amazon Q Developer in chat applications supports the following AWS managed IAM policies:

- [ReadOnlyAccess](#read-only-access-managed-policy "#read-only-access-managed-policy")
- [CloudWatchReadOnlyAccess](#CloudwatchReadOnlyAccess-policy-for-chatbot "#CloudwatchReadOnlyAccess-policy-for-chatbot")
- [AWS Support Command Permissions Policy](#chatbot_support_policy "#chatbot_support_policy")
- [Amazon Q Permissions policy](#chatbot_qdev_policy "#chatbot_qdev_policy")
- [Amazon Q Operations Assistant Permissions policy](#chatbot_ops_policy "#chatbot_ops_policy")
- [Resource Explorer Permissions policy](#resource-explorer_policy "#resource-explorer_policy")
- [Incident Manager Permissions policy](#incident-manager_policy "#incident-manager_policy")

AWS managed policies are available to all Amazon Q Developer in chat applications users, but you can't change or edit
them. You can copy them and use them as templates for your own policies, knowing that
you are using AWS-approved policy language to build your own policies.

Amazon Q Developer in chat applications adheres to standard IAM practices for using admin IAM accounts to activate and
use the Amazon Q Developer in chat applications service.

As a convenience, Amazon Q Developer in chat applications also supports the creation of new IAM roles directly in the
Amazon Q Developer in chat applications console. However, to configure existing IAM entities to use Amazon Q Developer in chat applications, you need to use
the IAM console.

### The IAM ReadOnlyAccess

policy

The **ReadOnlyAccess** policy is an AWS managed
policy that is automatically assigned to roles in the Amazon Q Developer in chat applications service.

This policy does not appear in the Amazon Q Developer in chat applications console. It defines Get, List, and Describe
permissions for the entire suite of AWS services, enabling Amazon Q Developer in chat applications to use this role
to access any of those services on your behalf.

You can attach this policy to new roles in IAM, or use it as a template to
define your own, more restrictive policy.

###### Note

Amazon Q Developer in chat applications must use a role that defines all the read-only permissions necessary
for its usage. You can define a policy to be more restrictive or specify fewer
services than the policy described here, and use that in place of the **ReadOnlyAccess** policy. However, you must ensure that
all CloudWatch and Amazon SNS read-only permissions remain in your policy, or some CloudWatch
features may not work with Amazon Q Developer in chat applications. The policy also must provide Get, List, and
Describe permissions for services supported by Amazon Q Developer in chat applications.

The policy's JSON code is shown following:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "a4b:Get*",
 "a4b:List*",
 "a4b:Search*",
 "acm:Describe*",
 "acm:Get*",
 "acm:List*",
 "acm-pca:Describe*",
 "acm-pca:Get*",
 "acm-pca:List*",
 "amplify:GetApp",
 "amplify:GetBranch",
 "amplify:GetJob",
 "amplify:GetDomainAssociation",
 "amplify:ListApps",
 "amplify:ListBranches",
 "amplify:ListDomainAssociations",
 "amplify:ListJobs",
 "xray:BatchGet*",
 "xray:Get*"
 ],
 "Effect": "Allow",
 "Resource": "*"
 }
 ]
}`

```

### The CloudWatchReadOnlyAccess

policy

You can attach the **CloudWatchReadOnlyAccess** policy to
Amazon Q Developer in chat applications roles when you edit them in the IAM console. This policy does not appear in
the Amazon Q Developer in chat applications console.

It is an AWS managed policy. You can attach this policy to any role for Amazon Q Developer in chat applications
usage. You can define your own policy with greater restrictions, using this policy
as a template.

Amazon Q Developer in chat applications users can use this policy to support Amazon CloudWatch events reporting, alarms, CloudWatch
logs, and CloudWatch trend charts for most of Amazon Q Developer in chat applications's supported AWS services. It allows
read-only operations for CloudWatch Logs and the Amazon Simple Notification Service service, and can be used in place
of the customer managed [Notification permissions
policy](#read-only-notifications-policy "#read-only-notifications-policy"). However, you must use the IAM console to attach
this policy to any IAM role.

The Logs permissions also support the useful **Show Logs**
feature for CloudWatch alarms notifications in Slack. Amazon Q Developer in chat applications also supports actions for
displaying logs for Lambda and Amazon API Gateway.

The policy's JSON code is shown following:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "autoscaling:Describe*",
 "cloudwatch:Describe*",
 "cloudwatch:Get*",
 "cloudwatch:List*",
 "logs:Get*",
 "logs:List*",
 "logs:Describe*",
 "logs:TestMetricFilter",
 "logs:FilterLogEvents",
 "sns:Get*",
 "sns:List*"
 ],
 "Effect": "Allow",
 "Resource": "*"
 }
 ]
}`

```

### The AWS Support Command Permissions

policy

The **AWS Support Command Permissions** policy
appears in the Amazon Q Developer in chat applications console when you configure resources. It's provided in the
Amazon Q Developer in chat applications console to conveniently set up a role, to allow Slack users to create AWS
support tickets through their Slack channels.

In the IAM console, this policy appears as **AWSSupportAccess**.

It is an AWS managed policy. You can also attach this policy in IAM to any
role. You can define your own policy with greater restrictions, using this policy as
a template, for roles in Amazon Q Developer in chat applications.

The **Support Command Permissions** policy applies
only to the Support service.

The policy's JSON code is shown following:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "support:*"
 ],
 "Resource": "*"
 }
 ]
}`

```

### The Amazon Q Permissions

policy

The **Amazon Q Permissions** policy
appears in the Amazon Q Developer in chat applications console when you configure your **Permissions**. This policy provides full access to enable
interactions with Amazon Q, including administrator access. It includes access to log in with IAM Identity Center to access Amazon Q through an Amazon Q Developer Pro subscription. For more information, see [AmazonQFullAccess](../../../aws-managed-policy/latest/reference/AmazonQFullAccess.md "../../../aws-managed-policy/latest/reference/AmazonQFullAccess.md") in the
_AWS Managed Policy Reference Guide_.

In the IAM console, this policy appears as **AmazonQFullAccess**.

It is an AWS managed policy. You can also attach this policy in IAM to any
role. You can define your own policy with greater restrictions, using this policy as
a template, for roles in Amazon Q Developer in chat applications.

The policy's JSON code is shown following:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement" : [
 {
 "Sid" : "AllowAmazonQFullAccess",
 "Effect" : "Allow",
 "Action" : [
 "q:StartConversation",
 "q:SendMessage",
 "q:GetConversation",
 "q:ListConversations",
 "q:PassRequest",
 "q:StartTroubleshootingAnalysis",
 "q:GetTroubleshootingResults",
 "q:StartTroubleshootingResolutionExplanation",
 "q:UpdateTroubleshootingCommandResult",
 "q:GetIdentityMetadata",
 "q:CreateAssignment",
 "q:DeleteAssignment",
 "q:GenerateCodeFromCommands",
 "q:CreatePlugin",
 "q:DeletePlugin",
 "q:GetPlugin",
 "q:UsePlugin",
 "q:ListPlugins",
 "q:ListPluginProviders",
 "q:ListTagsForResource",
 "q:UntagResource",
 "q:TagResource"
 ],
 "Resource" : "*"
 },
 {
 "Sid" : "AllowCloudControlReadAccess",
 "Effect" : "Allow",
 "Action" : [
 "cloudformation:GetResource",
 "cloudformation:ListResources"
 ],
 "Resource" : "*"
 },
 {
 "Sid" : "AllowSetTrustedIdentity",
 "Effect" : "Allow",
 "Action" : [
 "sts:SetContext"
 ],
 "Resource" : "arn:aws:sts::*:self"
 },
 {
 "Sid" : "AllowPassRoleToAmazonQ",
 "Effect" : "Allow",
 "Action" : [
 "iam:PassRole"
 ],
 "Resource" : "arn:aws:iam::*:role/*",
 "Condition" : {
 "StringEquals" : {
 "iam:PassedToService" : [
 "q.amazonaws.com"
 ]
 }
 }
 }
 ]
}`

```

### The Amazon Q Operations Assistant Permissions

policy

The **Amazon Q Operations Assistant Permissions** policy
appears in the Amazon Q Developer in chat applications console when you configure your **Permissions**. This policy enables Amazon Q to analyze your AWS resources during investigations of operational events.
this policy is scoped based on the resources that Amazon Q Developer supports during investigations, and is updated as more resources are supported. For more information, see [AIOpsOperatorAccess](../../../AmazonCloudWatch/latest/monitoring/auth-and-access-control-cw.md#managed-policies-QInvestigations-AIOpsAssistant "../../../AmazonCloudWatch/latest/monitoring/auth-and-access-control-cw.md#managed-policies-QInvestigations-AIOpsAssistant") in the
_Amazon CloudWatch User Guide_.

In the IAM console, this policy appears as **AIOpsOperatorAccess**.

It is an AWS managed policy. You can also attach this policy in IAM to any
role. You can define your own policy with greater restrictions, using this policy as
a template, for roles in Amazon Q Developer in chat applications.

The policy's JSON code is shown following:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AIOpsOperatorAccess",
 "Effect": "Allow",
 "Action": [
 "aiops:CreateInvestigation",
 "aiops:CreateInvestigationEvent",
 "aiops:CreateInvestigationResource",
 "aiops:DeleteInvestigation",
 "aiops:Get*",
 "aiops:List*",
 "aiops:UpdateInvestigation",
 "aiops:UpdateInvestigationEvent"
 ],
 "Resource": "*"
 },
 {
 "Sid": "SSOManagementAccess",
 "Effect": "Allow",
 "Action": [
 "identitystore:DescribeUser",
 "sso:DescribeInstance",
 "sso-directory:DescribeUsers"
 ],
 "Resource": "*"
 },
 {
 "Sid": "AllowSTSContextSetting",
 "Effect": "Allow",
 "Action": [
 "sts:SetContext"
 ],
 "Resource": "arn:aws:sts::*:self"
 },
 {
 "Sid": "SSMSettingServiceIntegration",
 "Effect": "Allow",
 "Action": [
 "ssm:GetServiceSetting"
 ],
 "Resource": "arn:aws:ssm:*:*:servicesetting/integrations/*"
 },
 {
 "Sid": "SSMIntegrationTagAccess",
 "Effect": "Allow",
 "Action": [
 "ssm:AddTagsToResource",
 "ssm:CreateOpsItem"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "aws:RequestTag/Integration": [
 "CloudWatch"
 ]
 },
 "ForAllValues:StringEquals": {
 "aws:TagKeys": "Integration"
 }
 }
 },
 {
 "Sid": "SSMOpsItemIntegration",
 "Effect": "Allow",
 "Action": [
 "ssm:DeleteOpsItem",
 "ssm:UpdateOpsItem"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "aws:ResourceTag/Integration": [
 "CloudWatch"
 ]
 }
 }
 },
 {
 "Sid": "SSMTagOperation",
 "Effect": "Allow",
 "Action": [
 "ssm:AddTagsToResource"
 ],
 "Resource": "arn:aws:ssm:*:*:opsitem/*",
 "Condition": {
 "StringEquals": {
 "aws:ResourceTag/Integration": [
 "CloudWatch"
 ]
 },
 "ForAllValues:StringEquals": {
 "aws:TagKeys": "Integration"
 }
 }
 },
 {
 "Sid": "SSMOpsSummaryIntegration",
 "Effect": "Allow",
 "Action": [
 "ssm:GetOpsSummary"
 ],
 "Resource": "*"
 }
 ]
}`

```

### The Resource Explorer Permissions

policy

The **Resource Explorer Permissions** policy
appears in the Amazon Q Developer in chat applications console when you configure your **Permissions**. This policy grants Amazon Q read-only access to permissions to search for and view Resource Explorer resources.
For more information, see [AWSResourceExplorerReadOnlyAccess](../../../resource-explorer/latest/userguide/security_iam_awsmanpol.md#security_iam_awsmanpol_AWSResourceExplorerReadOnlyAccess "../../../resource-explorer/latest/userguide/security_iam_awsmanpol.md#security_iam_awsmanpol_AWSResourceExplorerReadOnlyAccess") in the
_AWS Resource Explorer User Guide_.

In the IAM console, this policy appears as **AWSResourceExplorerReadOnlyAccess**.

It is an AWS managed policy. You can also attach this policy in IAM to any
role. You can define your own policy with greater restrictions, using this policy as
a template, for roles in Amazon Q Developer in chat applications.

The policy's JSON code is shown following:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement" : [
 {
 "Sid" : "ResourceExplorerReadOnlyAccess",
 "Effect" : "Allow",
 "Action" : [
 "resource-explorer-2:Get*",
 "resource-explorer-2:List*",
 "resource-explorer-2:Search",
 "resource-explorer-2:BatchGetView",
 "ec2:DescribeRegions",
 "ram:ListResources",
 "ram:GetResourceShares",
 "organizations:DescribeOrganization"
 ],
 "Resource" : "*"
 }
 ]
}`

```

### Incident Manager permissions

policy

The **Incident Manager permissions** policy
appears in the Amazon Q Developer in chat applications console when you configure your **Permissions**. This policy enables Amazon Q to start, view, and update incidents.
This also allows Amazon Q Developer to create customer timeline events and related items in the incident dashboard. For more information, see [AWSIncidentManagerResolverAccess](../../../incident-manager/latest/userguide/security-iam-awsmanpol.md#security-iam-awsmanpol-AWSIncidentManagerResolverAccess "../../../incident-manager/latest/userguide/security-iam-awsmanpol.md#security-iam-awsmanpol-AWSIncidentManagerResolverAccess") in the
_Incident Manager User Guide_.

In the IAM console, this policy appears as **AWSIncidentManagerResolverAccess**.

It is an AWS managed policy. You can also attach this policy in IAM to any
role. You can define your own policy with greater restrictions, using this policy as
a template, for roles in Amazon Q Developer in chat applications.

The policy's JSON code is shown following:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "StartIncidentPermissions",
 "Effect": "Allow",
 "Action": [
 "ssm-incidents:StartIncident"
 ],
 "Resource": "*"
 },
 {
 "Sid": "ResponsePlanReadOnlyPermissions",
 "Effect": "Allow",
 "Action": [
 "ssm-incidents:ListResponsePlans",
 "ssm-incidents:GetResponsePlan"
 ],
 "Resource": "*"
 },
 {
 "Sid": "IncidentRecordResolverPermissions",
 "Effect": "Allow",
 "Action": [
 "ssm-incidents:ListIncidentRecords",
 "ssm-incidents:GetIncidentRecord",
 "ssm-incidents:UpdateIncidentRecord",
 "ssm-incidents:ListTimelineEvents",
 "ssm-incidents:CreateTimelineEvent",
 "ssm-incidents:GetTimelineEvent",
 "ssm-incidents:UpdateTimelineEvent",
 "ssm-incidents:DeleteTimelineEvent",
 "ssm-incidents:ListRelatedItems",
 "ssm-incidents:UpdateRelatedItems"
 ],
 "Resource": "*"
 }
 ]
}`

```

## Customer managed IAM policies in

Amazon Q Developer in chat applications

Amazon Q Developer in chat applications also supports three service-provided customer managed IAM policies, that you
can apply to any Amazon Q Developer in chat applications role. They can also be used as templates for defining custom
IAM permissions for your users:

- [ReadOnly Command Permissions policy](#read-only-policy-for-cli "#read-only-policy-for-cli")
- [Lambda-Invoke Command
  Permissions policy](#lambda-invoke-policy-for-chatbot-cli "#lambda-invoke-policy-for-chatbot-cli")
- [Notification permissions
  policy](#read-only-notifications-policy "#read-only-notifications-policy")

### The Amazon Q Developer in chat applications Read-Only Command Permissions

IAM policy

The **Read-Only Command Permissions** policy appears
in the Amazon Q Developer in chat applications console when you configure resources. You use this policy to support
AWS commands and actions in Slack channels.

It is a customer managed policy. It pairs with the [Lambda-Invoke Command Permissions
policy](#lambda-invoke-policy-for-chatbot-cli "#lambda-invoke-policy-for-chatbot-cli") to provide a convenient Amazon Q Developer in chat applications configuration to enable Slack
channel support for sending commands to the AWS CLI.

The **Read-Only Command Permissions** policy denies
permission for Amazon Q Developer in chat applications users to get sensitive information from AWS services through
the Slack channel, such as Amazon EC2 password information, key pairs and login
credentials.

This policy appears in the IAM console as the **AWS-Chatbot-ReadOnly-Commands-Policy**.

You can edit and assign this policy to any role in Amazon Q Developer in chat applications or in IAM. For editing
of roles and policies for Amazon Q Developer in chat applications usage, we recommend using the IAM console.

###### Note

If you want to use this policy as a template, we recommend saving a new copy
of the policy under a different name and making your changes there.

For your team's command usage in Slack channels, you must use a role that defines
the necessary read-only permissions.

The policy's JSON code is shown following:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Deny",
 "Action": [
 "iam:*",
 "s3:GetBucketPolicy",
 "ssm:*",
 "sts:*",
 "kms:*",
 "cognito-idp:GetSigningCertificate",
 "ec2:GetPasswordData",
 "ecr:GetAuthorizationToken",
 "gamelift:RequestUploadCredentials",
 "gamelift:GetInstanceAccess",
 "lightsail:DownloadDefaultKeyPair",
 "lightsail:GetInstanceAccessDetails",
 "lightsail:GetKeyPair",
 "lightsail:GetKeyPairs",
 "redshift:GetClusterCredentials",
 "storagegateway:DescribeChapCredentials"
 ],
 "Resource": [
 "*"
 ]
 }
 ]
}`

```

### The Amazon Q Developer in chat applications Lambda-Invoke

Command Permissions policy

The **Lambda-Invoke Command Permissions** policy
appears in the Amazon Q Developer in chat applications console when you configure resources. It pairs with the [Read-Only Command Permissions policy](#read-only-policy-for-cli "#read-only-policy-for-cli") to
provide a convenient Amazon Q Developer in chat applications configuration to enable Slack channel access to the
AWS CLI, and to features that make sense for CLI use. The policy allows Amazon Q Developer in chat applications users to
invoke Lambda functions in their Slack channels.

It is a customer managed policy. In the IAM console, it appears as **AWS-Chatbot-LambdaInvoke-Policy**.

You can edit and assign this policy to any role in Amazon Q Developer in chat applications or in IAM.

By default, the **Lambda-Invoke** policy is very
permissive, because you can invoke any function for any action.

We recommend using this policy as a template to define your own, more restrictive
policies, such as permissions to invoke functions developed for your DevOps team
that only they should be able to invoke, and deny permissions to invoke Lambda
functions for any other purpose. To edit roles and policies for Amazon Q Developer in chat applications, use the IAM
console.

The policy's JSON code is shown following:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "lambda:invokeAsync",
 "lambda:invokeFunction"
 ],
 "Resource": [
 "*"
 ]
 }
 ]
}`

```

### The Amazon Q Developer in chat applications Notification Permissions

IAM policy

The **Notification Permissions** policy appears in
the Amazon Q Developer in chat applications console when you configure resources. It provides the minimum usable IAM
policy configuration for using the Amazon Q Developer in chat applications in Slack channels and Amazon Chime webhooks. The
**Notification Permissions** policy enables Amazon Q Developer in chat applications
admins to forward CloudWatch Events, CloudWatch alarms, and format charting data for viewing in chat
room messages. Because many of Amazon Q Developer in chat applications's supported services use CloudWatch as their event
and alarm processing layer, Amazon Q Developer in chat applications requires this policy for core functionality. You
can use other policies, such as [CloudWatchReadOnlyAccess](#CloudwatchReadOnlyAccess-policy-for-chatbot "#CloudwatchReadOnlyAccess-policy-for-chatbot"), in place of
this policy, but you must attach that policy to the role in the IAM
console.

It is a customer managed policy. You can edit and assign this policy to any role
for Amazon Q Developer in chat applications usage.

###### Note

If you want to use this policy as a template, we recommend saving a new copy
of the policy under a different name and making your changes there.

In the IAM console, it appears as **AWS-Chatbot-NotificationsOnly-Policy**.

The policy's JSON code is shown following:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "cloudwatch:Describe*",
 "cloudwatch:Get*",
 "cloudwatch:List*"
 ],
 "Effect": "Allow",
 "Resource": "*"
 }
 ]
}`

```
