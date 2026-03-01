# AWS managed policies for Amazon Q Apps

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

## AWS managed policy: QAppsServiceRolePolicy

Amazon Q Apps uses a `QAppsServiceRolePolicy` to enable an Amazon Q Apps to
access CloudWatch resources and populate CloudWatch metrics. You can't attach
`QAppsServiceRolePolicy` to your IAM entities. This policy is attached to a
service-linked role that allows Amazon Q Apps to perform actions on your behalf. For more
information, see [Using service-linked roles for Amazon Q Apps](using-service-linked-roles-qapps.md "using-service-linked-roles-qapps.md").

**Permissions details**

This policy includes the following permissions.

- `cloudwatch` – Allows Amazon Q Apps to publish metric data points
  to CloudWatch under the AWS/QApps namespace

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "QAppsPutMetricDataPermission",
 "Effect": "Allow",
 "Action": [
 "cloudwatch:PutMetricData"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "cloudwatch:namespace": "AWS/QApps"
 }
 }
 }
 ]
}`

```

## Amazon Q Apps updates to AWS managed policies

View details about updates to AWS managed policies for Amazon Q Apps since this service
began tracking these changes. For automatic alerts about changes to this page, subscribe to
the RSS feed on the [Amazon Q Business Document history page](../business-use-dg/doc-history.md "../business-use-dg/doc-history.md").

| Change                                                                                                                                                  | Description                                                                                      | Date         |
| ------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ | ------------ |
| [QAppsServiceRolePolicy](#security-iam-awsmanpol-amazonq-app-role-policy-qapps "#security-iam-awsmanpol-amazonq-app-role-policy-qapps")<br>• New policy | Amazon Q Apps added a new policy that grants permissions needed for Q Apps<br>to publish metrics | Sep 30, 2024 |
| Amazon Q Apps started tracking changes                                                                                                                  | Amazon Q Apps started tracking changes for its AWS managed<br>policies.                          | Sep 30, 2024 |
