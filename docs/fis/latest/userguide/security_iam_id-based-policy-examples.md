# AWS Fault Injection Service policy examples

By default, users and roles don't have permission to create or modify AWS FIS
resources. To grant users permission to perform actions on the
resources that they need, an IAM administrator can create IAM policies.

To learn how to create an IAM identity-based policy by using these example JSON policy
documents, see [Create IAM policies (console)](../../../IAM/latest/UserGuide/access_policies_create-console.md "../../../IAM/latest/UserGuide/access_policies_create-console.md") in the
_IAM User Guide_.

For details about actions and resource types defined by AWS FIS, including the format of the ARNs for each of the resource types, see [Actions, resources, and condition keys for AWS Fault Injection Service](../../../service-authorization/latest/reference/list_awsfaultinjectionservice.md "../../../service-authorization/latest/reference/list_awsfaultinjectionservice.md") in the _Service Authorization Reference_.

###### Contents

- [Policy best
  practices](#security_iam_service-with-iam-policy-best-practices "#security_iam_service-with-iam-policy-best-practices")
- [Example: Use the AWS FIS
  console](#security-iam-policy-examples-console "#security-iam-policy-examples-console")
- [Example: List available AWS FIS actions](#security-iam-policy-examples-list-actions "#security-iam-policy-examples-list-actions")
- [Example: Create an experiment template for a specific action](#security-iam-policy-examples-create-template "#security-iam-policy-examples-create-template")
- [Example: Start an experiment](#security-iam-policy-examples-start-experiment "#security-iam-policy-examples-start-experiment")
- [Example: Use tags to control resource usage](#security-iam-policy-examples-tagging "#security-iam-policy-examples-tagging")
- [Example: Delete an experiment template with a specific tag](#security-iam-policy-examples-delete-tagged-template "#security-iam-policy-examples-delete-tagged-template")
- [Example: Allow
  users to view their own permissions](#security_iam_id-based-policy-examples-view-own-permissions "#security_iam_id-based-policy-examples-view-own-permissions")
- [Example: Use condition keys for
  ec2:InjectApiError](#security-iam-policy-examples-ec2 "#security-iam-policy-examples-ec2")
- [Example: Use condition keys for
  aws:s3:bucket-pause-replication](#security-iam-policy-examples-s3 "#security-iam-policy-examples-s3")

## Policy best

practices

Identity-based policies determine whether someone can create, access, or delete AWS FIS resources in your
account. These actions can incur costs for your AWS account. When you create or edit identity-based policies, follow these guidelines and
recommendations:

- **Get started with AWS managed policies and move toward least-privilege permissions**
  – To get started granting permissions to your users and workloads, use the _AWS
  managed policies_ that grant permissions for many common use cases. They are
  available in your AWS account. We recommend that you reduce permissions further by
  defining AWS customer managed policies that are specific to your use cases. For more information, see
  [AWS managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies") or [AWS managed policies for job functions](../../../IAM/latest/UserGuide/access_policies_job-functions.md "../../../IAM/latest/UserGuide/access_policies_job-functions.md") in the _IAM User Guide_.
- **Apply least-privilege permissions** –
  When you set permissions with IAM policies, grant only the permissions required to
  perform a task. You do this by defining the actions that can be taken on specific resources
  under specific conditions, also known as _least-privilege permissions_.
  For more information about using IAM to apply permissions, see [Policies and permissions in IAM](../../../IAM/latest/UserGuide/access_policies.md "../../../IAM/latest/UserGuide/access_policies.md") in the _IAM User Guide_.
- **Use conditions in IAM policies to further restrict access**
  – You can add a condition to your policies to limit access to actions and resources. For example, you can write a policy condition to specify that all requests must
  be sent using SSL. You can also use conditions to grant access to service actions
  if they are used through a specific AWS service, such as AWS CloudFormation. For more information, see
  [IAM JSON policy elements: Condition](../../../IAM/latest/UserGuide/reference_policies_elements_condition.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition.md") in the _IAM User Guide_.
- **Use IAM Access Analyzer to validate your IAM policies to ensure secure and functional permissions**
  – IAM Access Analyzer validates new and existing policies so that the policies adhere to the IAM policy language (JSON) and IAM best practices.
  IAM Access Analyzer provides more than 100 policy checks and actionable recommendations to help
  you author secure and functional policies. For more information, see [Validate policies with IAM Access Analyzer](../../../IAM/latest/UserGuide/access-analyzer-policy-validation.md "../../../IAM/latest/UserGuide/access-analyzer-policy-validation.md") in the _IAM User Guide_.
- **Require multi-factor authentication (MFA)** –
  If you have a scenario that requires IAM users or a root user in your AWS account, turn on MFA for additional security. To require
  MFA when API operations are called, add MFA conditions to your policies. For
  more information, see [Secure API access with MFA](../../../IAM/latest/UserGuide/id_credentials_mfa_configure-api-require.md "../../../IAM/latest/UserGuide/id_credentials_mfa_configure-api-require.md") in the _IAM User Guide_.

For more information about best practices in IAM, see [Security best practices in IAM](../../../IAM/latest/UserGuide/best-practices.md "../../../IAM/latest/UserGuide/best-practices.md") in the _IAM User Guide_.

## Example: Use the AWS FIS

console

To access the AWS Fault Injection Service console, you must have a minimum set of permissions.
These permissions must allow you to list and view details about the AWS FIS resources
in your AWS account. If you create an identity-based policy that is more restrictive
than the minimum required permissions, the console won't function as intended for
entities (users or roles) with that policy.

You don't need to allow minimum console permissions for users that are making calls
only to the AWS CLI or the AWS API. Instead, allow access to only the actions that match
the API operation that they're trying to perform.

The following example policy grants permission to list and view all AWS FIS
resources using AWS FIS console, but not to create, update, or delete them. It also
grants permissions to view the available resources used by all AWS FIS actions that
you could specify in an experiment template.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "FISReadOnlyActions",
 "Effect": "Allow",
 "Action": [
 "fis:List*",
 "fis:Get*"
 ],
 "Resource": "*"
 },
 {
 "Sid": "AdditionalReadOnlyActions",
 "Effect": "Allow",
 "Action": [
 "ssm:Describe*",
 "ssm:Get*",
 "ssm:List*",
 "ec2:DescribeInstances",
 "rds:DescribeDBClusters",
 "ecs:DescribeClusters",
 "ecs:ListContainerInstances",
 "eks:DescribeNodegroup",
 "cloudwatch:DescribeAlarms",
 "iam:ListRoles"
 ],
 "Resource": "*"
 },
 {
 "Sid": "PermissionsToCreateServiceLinkedRole",
 "Effect": "Allow",
 "Action": "iam:CreateServiceLinkedRole",
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "iam:AWSServiceName": "fis.amazonaws.com"
 }
 }
 }
 ]
}`

```

## Example: List available AWS FIS actions

The following policy grants permission to list the available AWS FIS actions.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "fis:ListActions"
 ],
 "Resource": "arn:aws:fis:*:*:action/*"
 }
 ]
}`

```

## Example: Create an experiment template for a specific action

The following policy grants permission to create an experiment template for the
action `aws:ec2:stop-instances`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "PolicyExample",
 "Effect": "Allow",
 "Action": [
 "fis:CreateExperimentTemplate"
 ],
 "Resource": [
 "arn:aws:fis:*:*:action/aws:ec2:stop-instances",
 "arn:aws:fis:*:*:experiment-template/*"
 ]
 },
 {
 "Sid": "PolicyPassRoleExample",
 "Effect": "Allow",
 "Action": [
 "iam:PassRole"
 ],
 "Resource": [
 "arn:aws:iam::`111122223333`:role/`role-name`"
 ]
 }
 ]
}`

```

## Example: Start an experiment

The following policy grants permission to start an experiment using the specified
IAM role and experiment template. It also allows AWS FIS to create a service-linked
role on the user's behalf. For more information, see [Use service-linked roles for AWS Fault Injection Service](using-service-linked-roles.md "using-service-linked-roles.md").

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "PolicyExample",
 "Effect": "Allow",
 "Action": [
 "fis:StartExperiment"
 ],
 "Resource": [
 "arn:aws:fis:*:*:experiment-template/`experiment-template-id`",
 "arn:aws:fis:*:*:experiment/*"
 ]
 },
 {
 "Sid": "PolicyExampleforServiceLinkedRole",
 "Effect": "Allow",
 "Action": "iam:CreateServiceLinkedRole",
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "iam:AWSServiceName": "fis.amazonaws.com"
 }
 }
 }
 ]
}`

```

## Example: Use tags to control resource usage

The following policy grants permission to run experiments from experiment
templates that have the tag `Purpose=Test`. It does not grant permission
to create or modify experiment templates, or run experiments using templates that do
not have the specified tag.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "fis:StartExperiment",
 "Resource": "arn:aws:fis:*:*:experiment-template/*",
 "Condition": {
 "StringEquals": {
 "aws:ResourceTag/`Purpose`": "`Test`"
 }
 }
 }
 ]
}`

```

## Example: Delete an experiment template with a specific tag

The following policy grants permission to delete an experiment template with tag
`Purpose=Test`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "fis:DeleteExperimentTemplate"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "aws:ResourceTag/`Purpose`": "`Test`"
 }
 }
 }
 ]
}`

```

## Example: Allow

users to view their own permissions

This example shows how you might create a policy that allows IAM users to view the inline and managed policies that are attached to their user
identity. This policy includes permissions to complete this action on the console or programmatically using the AWS CLI or AWS API.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "ViewOwnUserInfo",
            "Effect": "Allow",
            "Action": [
                "iam:GetUserPolicy",
                "iam:ListGroupsForUser",
                "iam:ListAttachedUserPolicies",
                "iam:ListUserPolicies",
                "iam:GetUser"
            ],
            "Resource": ["arn:aws:iam::*:user/${aws:username}"]
        },
        {
            "Sid": "NavigateInConsole",
            "Effect": "Allow",
            "Action": [
                "iam:GetGroupPolicy",
                "iam:GetPolicyVersion",
                "iam:GetPolicy",
                "iam:ListAttachedGroupPolicies",
                "iam:ListGroupPolicies",
                "iam:ListPolicyVersions",
                "iam:ListPolicies",
                "iam:ListUsers"
            ],
            "Resource": "*"
        }
    ]
}
```

## Example: Use condition keys for

`ec2:InjectApiError`

The following example policy uses the `ec2:FisTargetArns` condition key
to scope target resources. This policy allows the AWS FIS actions `aws:ec2:api-insufficient-instance-capacity-error`
and `aws:ec2:asg-insufficient-instance-capacity-error`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "ec2:InjectApiError",
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "ec2:FisActionId": [
 "aws:ec2:api-insufficient-instance-capacity-error",
 "aws:ec2:asg-insufficient-instance-capacity-error"
 ]
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": "ec2:InjectApiError",
 "Resource": "*",
 "Condition": {
 "ForAllValues:ArnLike": {
 "ec2:FisTargetArns": [
 "arn:aws:autoscaling:*:*:autoScalingGroup:uuid:`autoScalingGroupName`/`asg-name`"
 ]
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": "autoscaling:DescribeAutoScalingGroups",
 "Resource": "*"
 }
 ]
}`

```

## Example: Use condition keys for

`aws:s3:bucket-pause-replication`

The following example policy uses the `S3:IsReplicationPauseRequest` condition key
to allow `PutReplicationConfiguration` and `GetReplicationConfiguration`
only when used by AWS FIS in the context of the AWS FIS action `aws:s3:bucket-pause-replication`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "S3:PauseReplication"
 ],
 "Resource": "arn:aws:s3:::mybucket",
 "Condition": {
 "StringEquals": {
 "s3:DestinationRegion": "`region`"
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "S3:PutReplicationConfiguration",
 "S3:GetReplicationConfiguration"
 ],
 "Resource": "arn:aws:s3:::mybucket",
 "Condition": {
 "BoolIfExists": {
 "s3:IsReplicationPauseRequest": "true"
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "S3:ListBucket"
 ],
 "Resource": "arn:aws:s3:::*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "tag:GetResources"
 ],
 "Resource": "*"
 }
 ]
 }`

```
