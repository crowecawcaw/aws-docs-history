AWS Migration Hub will no longer be open to new customers starting November 7, 2025. To continue using the service, sign up prior to November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Transform](https://aws.amazon.com/transform "https://aws.amazon.com/transform").

# IAM roles and permissions for AWS Migration Hub automation

units

###### Note

The AWS Migration Hub Automation feature is in preview release. It is available in
US East (N. Virginia). To use this feature, you must set your AWS Region to
US East (N. Virginia). You must also set the AWS Migration Hub home Region to US East (N. Virginia).
For instructions on how to set the AWS Migration Hub home Region, see [Managing your AWS Migration Hub home Region](home-region.md "home-region.md").

This is pre-release documentation. Both the AWS Migration Hub Automation feature and the
documentation are subject to change.

To run an automation unit, you must associate with it an IAM role with a trust policy
and a permissions policy that depend on the kind of unit (custom or managed) and on the
actions that the unit performs.

###### Warning

This IAM role allows Migration Hub to execute automation units on your behalf. By specifying
a service role, you define the specific actions that can be performed during an
automation run, which may differ from the permissions of the user that creates or runs
the automation unit. A user with the following four permissions can perform any actions
in your AWS account.

- mgh:CreateAutomationUnit
- mgh:AssociateAutomationUnitRole
- mgh:CreateAutomationRun
- iam:PassRole
  To minimize security risks, apply strict least-privilege permissions to service roles,
  and carefully review and audit automation unit roles. For more information, see [Apply
  least-privilege permissions](../../../IAM/latest/UserGuide/best-practices.md#grant-least-privilege "../../../IAM/latest/UserGuide/best-practices.md#grant-least-privilege") in the _IAM User Guide_.

###### Topics

- [IAM role and policies for managed automation
  units](#mha-mgn-rehost-role "#mha-mgn-rehost-role")
- [IAM role and policies for custom
  automation units](#iam-custom-automation-units "#iam-custom-automation-units")

## IAM role and policies for managed automation

units

For managed automation units, create an IAM role and give the role any name that you
want. Attach the following trust policy to the role. For information about how to create
an IAM role with this trust policy, see [Create a role using
custom trust policies](../../../IAM/latest/UserGuide/id_roles_create_for-custom.md "../../../IAM/latest/UserGuide/id_roles_create_for-custom.md").

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": ["ssm.amazonaws.com", "migrationhub.amazonaws.com"]
 },
 "Action": "sts:AssumeRole",
 "Condition": {
 "StringEquals": {
 "aws:SourceAccount": "`account-id`"
 }
 }
 }
 ]
}`

```

Attach the following permissions policy to the role.

## IAM role and policies for custom

automation units

For custom automation units, create an IAM role and give the role any name that you
want. The trust policy and permissions policy that you must attach to the IAM role
depend on your implementation of the unit, as described in the following sections. For
information about how to create an IAM role with one of these trust policies, see
[Create a role using
custom trust policies](../../../IAM/latest/UserGuide/id_roles_create_for-custom.md "../../../IAM/latest/UserGuide/id_roles_create_for-custom.md").

###### Topics

- [IAM policies for custom automation units
  that use an AWS Systems Manager document as their target](#iam-custom-units-ssm "#iam-custom-units-ssm")
- [IAM policies for custom automation units
  that use an AWS Lambda as their target](#iam-custom-units-lambda "#iam-custom-units-lambda")

### IAM policies for custom automation units

that use an AWS Systems Manager document as their target

If your custom unit uses an AWS Systems Manager document as its target, then the IAM role
that you attach to the unit must have the following trust policy.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": ["ssm.amazonaws.com", "migrationhub.amazonaws.com"]
 },
 "Action": "sts:AssumeRole",
 "Condition": {
 "StringEquals": {
 "aws:SourceAccount": "`account-id`"
 }
 }
 }
 ]
}`

```

You must also attach to the IAM role a permissions policy that has at least the
permissions that are in the following policy. Add to this policy any permissions
that the custom unit needs in order to perform its actions.

### IAM policies for custom automation units

that use an AWS Lambda as their target

For a custom automation unit that uses an AWS Lambda function as its target, you
must attach the following trust policy.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": ["migrationhub.amazonaws.com"]
 },
 "Action": "sts:AssumeRole",
 "Condition": {
 "StringEquals": {
 "aws:SourceAccount": "`account-id`"
 }
 }
 }
 ]
}`

```

You must also attach to the IAM role a permissions policy that has at least the
permissions that are in the following policy. Add to this policy any permissions
that the custom unit needs in order to perform its actions.
