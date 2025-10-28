# Resource control policies in AWS KMS

Resource control policies (RCPs) are a type of organization policy that you can use to
enforce preventive controls on AWS resources in your organization. RCPs help you to
centrally restrict external access to your AWS resources at scale. RCPs complement service
control policies (SCPs). While, SCPs can be used to centrally set the maximum permissions on
the IAM roles and users in your organization, RCPs can be used to centrally set the
maximum permissions on AWS resources in your organization.

You can use RCPs to manage permissions to the customer managed KMS keys in your
organization. RCPs alone are not sufficient in granting permissions to your customer managed
keys. No permissions are granted by an RCP. An RCP defines a permissions guardrail, or sets
limits, on the actions that identities can take on resources in the affected accounts. The
administrator must still attach identity-based policies to IAM roles or users, or key
policies to actually grant permissions.

###### Note

Resource control policies in your organization do not apply to [AWS managed keys](concepts.md#aws-managed-key "concepts.md#aws-managed-key").

AWS managed keys are created, managed, and used on your behalf by an AWS service,
you cannot change or manage their permissions.

**Learn more**

- For more general information on RCPs, see [Resource control
  policies](../../../organizations/latest/userguide/orgs_manage_policies_rcps.md "../../../organizations/latest/userguide/orgs_manage_policies_rcps.md") in the _AWS Organizations User Guide_.
- For details on how to define RCPs, including examples, see [RCP syntax](../../../organizations/latest/userguide/orgs_manage_policies_rcps_syntax.md "../../../organizations/latest/userguide/orgs_manage_policies_rcps_syntax.md") in
  the _AWS Organizations User Guide_.
  The following example demonstrates how to use an RCP to prevent external principals from
  accessing customer managed keys in your organization. This policy is just a sample, and you
  should tailor it to meet your unique business and security needs. For example, you might
  want to customize your policy to allow access by your business partners. For more details,
  see the [data perimeter policy examples repository](https://github.com/aws-samples/data-perimeter-policy-examples/tree/main/resource_control_policies "https://github.com/aws-samples/data-perimeter-policy-examples/tree/main/resource_control_policies").

###### Note

The `kms:RetireGrant` permission is not effective in an RCP, even if the
`Action` element specifies an asterisk (\*) as a wildcard.

For more information on how permission to `kms:RetireGrant` is determined,
see [Retiring and revoking grants](grant-delete.md "grant-delete.md").

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "RCPEnforceIdentityPerimeter",
 "Effect": "Deny",
 "Principal": "*",
 "Action": "kms:*",
 "Resource": "*",
 "Condition": {
 "StringNotEqualsIfExists": {
 "aws:PrincipalOrgID": "`my-org-id`"
 },
 "Bool": {
 "aws:PrincipalIsAWSService": "false"
 }
 }
 }
 ]
}`

```

The following example RCP requires that AWS service principals can only access your
customer managed KMS keys when the request originates from your organization. This policy
applies the control only on requests that have `aws:SourceAccount` present. This
ensures that service integrations that don't require the use of
`aws:SourceAccount` aren't affected. If `aws:SourceAccount` is
present in the request context, the `Null` condition evaluates to
`true`, causing the `aws:SourceOrgID` key to be enforced.

For more information about the confused deputy problem, see [The confused deputy problem](../../../IAM/latest/UserGuide/confused-deputy.md "../../../IAM/latest/UserGuide/confused-deputy.md") in the
_IAM User Guide_.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "RCPEnforceConfusedDeputyProtection",
 "Effect": "Deny",
 "Principal": "*",
 "Action": "kms:*",
 "Resource": "*",
 "Condition": {
 "StringNotEqualsIfExists": {
 "aws:SourceOrgID": "`my-org-id`"
 },
 "Bool": {
 "aws:PrincipalIsAWSService": "true"
 },
 "Null": {
 "aws:SourceAccount": "false"
 }
 }
 }
 ]
}`

```
