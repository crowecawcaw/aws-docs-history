# AWS managed policies for AWS Health

An AWS managed policy is a standalone policy that is created and administered by AWS. AWS managed policies are designed
to provide permissions for many common use cases so that you can start assigning permissions to users, groups, and roles.

Keep in mind that AWS managed policies might not grant least-privilege permissions for your specific use cases because
they're available for all AWS customers to use. We recommend that you reduce permissions further by defining
[customer managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#customer-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#customer-managed-policies") that are specific to your use cases.

You cannot change the permissions defined in AWS managed policies. If AWS updates the permissions defined in an AWS
managed policy, the update affects all principal identities (users, groups, and roles) that the policy is attached to. AWS is
most likely to update an AWS managed policy when a new AWS service is launched or new API operations become available for
existing services.

For more information, see [AWS managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies") in the
_IAM User Guide_.

AWS Health has the following managed policies.

###### Contents

- [AWS
  managed policy: AWSHealth_EventProcessorServiceRolePolicy](security-iam-awsmanpol.md#security-iam-awsmanpol-Health_EventProcessorServiceRolePolicy "security-iam-awsmanpol.md#security-iam-awsmanpol-Health_EventProcessorServiceRolePolicy")
- [AWS
  managed policy: Health_OrganizationsServiceRolePolicy](security-iam-awsmanpol.md#security-iam-awsmanpol-Health_OrganizationsServiceRolePolicy "security-iam-awsmanpol.md#security-iam-awsmanpol-Health_OrganizationsServiceRolePolicy")
- [AWS managed policy:
  AWSHealthFullAccess](security-iam-awsmanpol.md#security-iam-awsmanpol-AWSHealthFullAccess "security-iam-awsmanpol.md#security-iam-awsmanpol-AWSHealthFullAccess")
- [AWS Health updates to AWS managed
  policies](security-iam-awsmanpol.md#security-iam-awsmanpol-updates "security-iam-awsmanpol.md#security-iam-awsmanpol-updates")

## AWS

managed policy: AWSHealth_EventProcessorServiceRolePolicy

AWS Health uses the [AWSHealth_EventProcessorServiceRolePolicy](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/aws-service-role/Health_EventProcessorServiceRolePolicy$jsonEditor "https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/aws-service-role/Health_EventProcessorServiceRolePolicy$jsonEditor") AWS managed policy. This
managed policy is attached to the `AWSServiceRoleForHealth_EventProcessor` service-linked
role. The policy allows the service-linked role to complete actions for you. You can't
attach this policy to your IAM entities. For more information, see [Using service-linked roles for
AWS Health](using-service-linked-roles.md "using-service-linked-roles.md").

The managed policy has the following permissions to allow AWS Health to access the
Amazon EventBridge rule for AWS Incident Detection and Response.

**Permissions details**

This policy includes the following permissions.

- `events` – Describes and deletes EventBridge rules, and describes
  and updates the targets for those rules.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Condition": {
 "StringEquals": {"events:ManagedBy": "event-processor.health.amazonaws.com"}
 },
 "Action": [
 "events:DeleteRule",
 "events:RemoveTargets",
 "events:PutTargets",
 "events:PutRule"
 ],
 "Resource": "*",
 "Effect": "Allow"
 },
 {
 "Action": [
 "events:ListTargetsByRule",
 "events:DescribeRule"
 ],
 "Resource": "*",
 "Effect": "Allow"
 }
 ]
}`

```

For a list of changes to the policy, see [AWS Health updates to AWS managed
policies](#security-iam-awsmanpol-updates "#security-iam-awsmanpol-updates").

## AWS

managed policy: Health_OrganizationsServiceRolePolicy

AWS Health uses the [Health_OrganizationsServiceRolePolicy](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/aws-service-role/Health_OrganizationsServiceRolePolicy$jsonEditor "https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/aws-service-role/Health_OrganizationsServiceRolePolicy$jsonEditor") AWS managed
policy. This managed policy is attached to the
`AWSServiceRoleForHealth_Organizations` service-linked role. The policy
allows the service-linked role to complete actions for you. You can't attach this policy
to your IAM entities. For more information, see [Using service-linked roles for
AWS Health](using-service-linked-roles.md "using-service-linked-roles.md").

This policy grants permissions that allow AWS Health to access required AWS Organizations
details for the Health Organizational view.

**Permissions details**

This policy includes the following permissions.

- `organizations` – Describes the accounts in AWS Organizations and the
  AWS services that can be used with Organizations.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "organizations:ListAccounts",
 "organizations:ListAWSServiceAccessForOrganization",
 "organizations:ListDelegatedAdministrators",
 "organizations:DescribeOrganization",
 "organizations:DescribeAccount"
 ],
 "Resource": "*"
 }
 ]
}`

```

For a list of changes to the policy, see [AWS Health updates to AWS managed
policies](#security-iam-awsmanpol-updates "#security-iam-awsmanpol-updates").

## AWS managed policy:

AWSHealthFullAccess

AWS Health uses the [AWSHealthFullAccess](https://console.aws.amazon.com//iam/home?#/policies/arn:aws:iam::aws:policy/AWSHealthFullAccess$jsonEditor "https://console.aws.amazon.com//iam/home?#/policies/arn:aws:iam::aws:policy/AWSHealthFullAccess$jsonEditor") AWS managed policy. The policy
grants entities (IAM users or roles) access to the AWS Health console. For more
information, see [Using the
AWS Health console](security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-console "security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-console").

**Permissions details**

This policy includes the following permissions.

- `organizations` – Enable or disable the AWS Health
  organizational view feature for all accounts in an AWS organization, and view
  the organizational units (OU) of the management account
- `health` – Access to the AWS Health API operations and
  notifications
- `iam` – Creates an IAM role that is linked the AWS Health
  service

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "OrganizationWriteAccess",
 "Effect": "Allow",
 "Action": [
 "organizations:EnableAWSServiceAccess",
 "organizations:DisableAWSServiceAccess"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "organizations:ServicePrincipal": "health.amazonaws.com"
 }
 }
 },
 {
 "Sid": "HealthFullAccess",
 "Effect": "Allow",
 "Action": [
 "health:*",
 "organizations:DescribeAccount",
 "organizations:ListAccounts",
 "organizations:ListDelegatedAdministrators",
 "organizations:ListParents"
 ],
 "Resource": "*"
 },
 {
 "Sid": "ServiceLinkAccess",
 "Effect": "Allow",
 "Action": "iam:CreateServiceLinkedRole",
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "iam:AWSServiceName": "health.amazonaws.com"
 }
 }
 }
 ]
}`

```

For a list of changes to the policy, see [AWS Health updates to AWS managed
policies](#security-iam-awsmanpol-updates "#security-iam-awsmanpol-updates").

## AWS Health updates to AWS managed

policies

View details about updates to AWS managed policies for AWS Health since this
service began tracking these changes. For automatic alerts about changes to this page,
subscribe to the RSS feed on the [Document history for AWS Health](doc-history.md "doc-history.md") page.

The following table describes important updates to the AWS Health managed policies
since January 13, 2022.

| AWS Health                                                                                                                                                                                                                      | Change                                                                                                                                                               | Description      | Date |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- | ---- |
| [AWS managed policy:<br>AWSHealthFullAccess](#security-iam-awsmanpol-AWSHealthFullAccess "#security-iam-awsmanpol-AWSHealthFullAccess")<br>• Update<br>to an existing policy                                                    | AWS Health has expanded the AWSHealthFullAccess policy to<br>AWS GovCloud (US) Regions and China Regions.                                                            | October 16, 2023 |
| [AWS<br>managed policy: Health_OrganizationsServiceRolePolicy](#security-iam-awsmanpol-Health_OrganizationsServiceRolePolicy "#security-iam-awsmanpol-Health_OrganizationsServiceRolePolicy")<br>• Update to an existing policy | AWS Health added new AWS Organizations actions to allow service-linked<br>role to describe the accounts and AWS services that can be used<br>with AWS Organizations. | July 19, 2023    |
| Change log published                                                                                                                                                                                                            | Change log for the AWS Health managed policies.                                                                                                                      | January 13, 2023 |
