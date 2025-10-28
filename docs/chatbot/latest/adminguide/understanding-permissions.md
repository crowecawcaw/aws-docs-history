AWS Chatbot is now Amazon Q Developer. [Learn more](service-rename.md "service-rename.md")

# Understanding Amazon Q Developer in chat applications permissions

Amazon Q Developer in chat applications requires an AWS Identity and Access Management (IAM) role to [perform actions](performing-actions.md "performing-actions.md"). Actions you can perform in
your chat channels include running commands and responding to interactive messages. Amazon Q Developer in chat applications uses
organization policies, service policies, channel roles, user roles, and channel guardrail policies to control the actions channel members can take.
What your users can do is the intersection of your guardrail policies and what is allowed by their roles.

###### Topics

- [Organization policies](#orgs-policy "#orgs-policy")
- [Role setting](#role-settings "#role-settings")
- [Channel guardrail policies](#channel-guardrails "#channel-guardrails")
- [Non-supported operations](#forbidden-permissions "#forbidden-permissions")
- [Securing your AWS organization in Amazon Q Developer in chat applications](securing-orgs.md "securing-orgs.md")
- [Chat client application permissions for Amazon Q Developer in chat applications](app-permissions.md "app-permissions.md")
- [Managing IAM roles for Amazon Q Developer in chat applications](manage-user-roles.md "manage-user-roles.md")
- [Protection policy](#cbt-protection-policy "#cbt-protection-policy")

## Organization policies

### Amazon Q Developer in chat applications organization policies (chat applications policies)

Organization administrators can manage multiple Amazon Q Developer in chat applications settings across all accounts within an organization using an Amazon Q Developer in chat applications chat applications policy (chat applications policy).
Chat applications policies define where Amazon Q Developer in chat applications can deliver notifications and if it can respond to Amazon Q Developer in chat applications mention events. For more information,
see [Securing your AWS organization in Amazon Q Developer in chat applications](securing-orgs.md "securing-orgs.md").

### Service control policies (SCPs)

Service control policies (SCPs) are a type of organization policy that you can use to manage permissions in your organization.
SCPs offer central control over the maximum available permissions for the IAM users and IAM roles in your organization.
For more information, [Service control policies (SCPs)](../../../organizations/latest/userguide/orgs_manage_policies_scps.md "../../../organizations/latest/userguide/orgs_manage_policies_scps.md") in the _AWS Organizations User Guide_.

## Role setting

### Channel role

A channel role gives all channel members the same permissions. This is useful if
your channel members are similar users or they typically perform the same actions. You can use an existing role as your channel role or you can create a new
role using templates. If you use a channel role, your channel members can still
choose their own user roles. Your channel role is restricted by your guardrail
policies. You can set your channel role in channel configurations from the Amazon Q Developer in chat applications
console.

#### Channel role templates

There are eight templates that can be used to create a channel role:

- Notification permissions
- Read-only command permissions
- Lambda-invoke command permissions
- AWS Support command permissions
- Incident Manager permissions
- Resource Explorer permissions
- Amazon Q permissions
- Amazon Q operations assistant permissions

You can use any and all combinations of these templates to suit your needs.
For example, if you want to create a configuration that only delivers
notifications, choose **Notification permissions** as your
policy template. If you want your channel members to run read-only commands
exclusively and you want notifications to be delivered, choose
**Read-only command permissions** and
**Notification permissions** as your policy templates. For more information, see [IAM policies for Amazon Q Developer in chat applications](chatbot-iam-policies.md "chatbot-iam-policies.md").

### User roles

User roles require channel members to choose their own roles. As a result,
different users in your channel can have different permissions. If you have a
diverse set of channel members or you don't want new channel members to perform
actions as soon as they join your channel, user roles are appropriate. Under this
schema, your channel members must have applied a user role to perform
actions. When channel members apply a user role, it is mapped to their chat client ID.
Administrators can unmap user roles from chat client IDs in the Amazon Q Developer in chat applications console. Your channel
member's actions are limited by your guardrail policies, despite what user roles they may have applied. For more information on
managing user roles, see [Managing IAM roles for Amazon Q Developer in chat applications](manage-user-roles.md "manage-user-roles.md").

#### User role requirement

Administrators can require user roles for all current channel members and channels and all channels created in the future by enabling a
user role requirement in the Amazon Q Developer in chat applications console. Individual channels can't override this requirement. This can be done at the account level in
**User permissions**, if you want to require every
workspace and channel to use user roles. It can also be done at the channel
configuration level wherein a channel level administrator can enable the user
role requirement.

###### Note

This feature is enforced at the account level.

## Channel guardrail policies

Guardrail policies provide detailed control over what actions are available to your
channel members and what actions Amazon Q Developer in chat applications can perform on your behalf. They constrain and
take precedence over both user roles and channel roles. For example, if a user has a
user role that allows administrator access, and they belong to a channel where the
channel role or the guardrail policies limit permissions on one or more services,
the user will have less than administrator-level access. You can set, view, and edit
your guardrail policies in the Amazon Q Developer in chat applications console. If you had an Amazon Q Developer in chat applications configuration before
the expansion of available commands on 11/28/2021, you may have a protection policy
applied as one of your guardrail policies.

###### Note

AWS Service Roles IAM policies can't be used as guardrail policies.

## Non-supported operations

Amazon Q Developer in chat applications doesn't support running commands for operations in the following JSON policy:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "appsync:ListApiKeys",
 "chatbot:*",
 "codecommit:GetFile",
 "codecommit:GetCommit",
 "codecommit:GetDifferences",
 "cognito-idp:*",
 "cognito-identity:*",
 "connect:GetFederationToken",
 "dynamodb:BatchGetItem",
 "dynamodb:GetItem",
 "ec2:GetPasswordData",
 "ecr:GetAuthorizationToken",
 "gamelift:RequestUploadCredentials",
 "gamelift:GetInstanceAccess",
 "identitystore:*",
 "lightsail:DownloadDefaultKeyPair",
 "lightsail:GetKeyPair",
 "lightsail:GetKeyPairs",
 "lightsail:UpdateRelationalDatabase",

 "iam:*",
 "kms:*",
 "redshift:GetClusterCredentials",
 "sdb:*",
 "secretsmanager:*",
 "sso:*",
 "storagegateway:DescribeChapCredentials",
 "sts:*",
 "s3:GetObject",
 "s3:PutObject",
 "s3:GetBucketPolicy",
 "snowball:GetJobUnlockCode"
 ],
 "Effect": "Deny",
 "Resource": "*"
 }
 ]
}`

```

##

Protection policy

The expansion of usable CLI commands occurred on 11/28/2021. This expansion can allow channel
members to create, read, update, and delete your AWS resources. To prevent this, a
protection policy is applied as a guardrail policy to existing Amazon Q Developer in chat applications configurations by
default. Specifically, the protection policy restricts permissions and actions to what
was available before all CLI commands were usable. This policy is detachable, but we
strongly recommend it stay in place until you’ve verified that all your guardrails,
channel IAM roles, and user-level roles align with your governance policy or channel
requirements. You can detach this policy from:

- Individual workspaces.
- Individual channels in the channel configurations page.
- A selection of channels using the **Set guardrails** button.
- All channel configurations in the **User permissions** page of the Amazon Q Developer in chat applications console.

The protection policy contains the [ReadOnlyAccess policy](../../../aws-managed-policy/latest/reference/ReadOnlyAccess.md "../../../aws-managed-policy/latest/reference/ReadOnlyAccess.md") and the following JSON code:

```
{
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "lambda:Invoke*",
                "support:*",
                "ssm-incidents:*"
            ],
            "Resource": "*"
        }
    ]
}
```
