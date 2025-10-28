# Managing access to the AWS Support App

widget

You can attach an AWS Identity and Access Management (IAM) policy to grant an IAM user permission to configure
the AWS Support App widget in the AWS Support Center Console.

For more information about how to add a policy to an IAM entity, see [Adding IAM identity permissions (console)](../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md#add-policies-console "../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md#add-policies-console") in the
IAM User Guide.

###### Note

You can also sign in as the root user in your AWS account, but we don't recommend
that you do this. For more information about root user access, see [Safeguard your root user credentials and don't use them for everyday tasks](../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials "../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials") in
the _IAM User Guide_.

## Example IAM

policy

You can attach the following policy to an entity, such as an IAM user or group. This
policy allows a user to authorize a Slack workspace and configure Slack channels in the
Support Center Console.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "supportapp:GetSlackOauthParameters",
 "supportapp:RedeemSlackOauthCode",
 "supportapp:DescribeSlackChannels",
 "supportapp:ListSlackWorkspaceConfigurations",
 "supportapp:ListSlackChannelConfigurations",
 "supportapp:CreateSlackChannelConfiguration",
 "supportapp:DeleteSlackChannelConfiguration",
 "supportapp:DeleteSlackWorkspaceConfiguration",
 "supportapp:GetAccountAlias",
 "supportapp:PutAccountAlias",
 "supportapp:DeleteAccountAlias",
 "supportapp:UpdateSlackChannelConfiguration",
 "iam:ListRoles"
 ],
 "Resource": "*"
 }
 ]
}`

```

## Permissions required to connect the

AWS Support App to Slack

The AWS Support App includes permission-only actions that don't directly correspond to an API
operation. These actions are indicated in the [Service
Authorization Reference](../../../service-authorization/latest/reference/list_awssupportappinslack.md "../../../service-authorization/latest/reference/list_awssupportappinslack.md") with [permission only].

The AWS Support App uses the following API actions to connect to Slack and then lists your
_public_ Slack channels in the
AWS Support Center Console:

- `supportapp:GetSlackOauthParameters`
- `supportapp:RedeemSlackOauthCode`
- `supportapp:DescribeSlackChannels`

These API actions are not intended to be called by your code. Therefore, these API
actions are not included in the AWS CLI and AWS SDKs.
