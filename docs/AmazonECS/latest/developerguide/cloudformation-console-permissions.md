# Permissions required for the Amazon ECS console with AWS CloudFormation

Before using the AWS Management Console to create your resources, you'll need to make sure to have the correct
IAM permissions. For information on how to set up permissions for the Amazon ECS console in general first,
see [Permissions required for the Amazon ECS console](console-permissions.md "console-permissions.md").

The Amazon ECS console is powered by AWS CloudFormation and requires additional IAM permissions in
the following cases:

- Creating a cluster
- Creating a service
- Creating a capacity provider
  You can create a policy for the additional permissions, and then attach them to the IAM
  role you use to access the console. For more information, see [Creating
  IAM policies](../../../IAM/latest/UserGuide/access_policies_create.md#access_policies_create-start "../../../IAM/latest/UserGuide/access_policies_create.md#access_policies_create-start") in the _IAM User Guide_.

## Permissions required for creating a cluster

When you create a cluster in the console, you need additional permissions that grant
you permissions to manage AWS CloudFormation stacks.

The following additional permissions are required:

- `cloudformation` – Allows principals to create and manage
  AWS CloudFormation stacks. This is required when creating Amazon ECS clusters using the AWS Management Console
  and the subsequent managing of those clusters.
- `ssm` – Allows AWS CloudFormation to reference latest Amazon ECS-optimized AMI.
  This is required when creating Amazon ECS clusters using the AWS Management Console.

The following policy contains the required AWS CloudFormation permissions, and limits the actions to
resources created in the Amazon ECS console.

JSON

```
`{
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "cloudformation:CreateStack",
 "cloudformation:DeleteStack",
 "cloudformation:DescribeStack*",
 "cloudformation:UpdateStack"
 ],
 "Resource": [
 "arn:*:cloudformation:*:*:stack/Infra-ECS-Cluster-*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": "ssm:GetParameters",
 "Resource": [
 "arn:aws:ssm:*:*:parameter/aws/service/ecs/optimized-ami/amazon-linux-2*/*",
 "arn:aws:ssm:*:*:parameter/aws/service/ecs/optimized-ami/amazon-linux-2023*/*"
 ]
 }
 ]
}`

```

If you have not created the Amazon ECS container instance role
(`ecsInstanceRole`), and you are creating a cluster that uses Amazon EC2
instances, then the console will create the role on your behalf.

In addition, if you use Auto Scaling groups, then you need additional permissions so that the
console can add tags to the auto scaling groups when using the cluster auto scaling
feature.

The following additional permissions are required:

- `autoscaling` – Allows the console to tag Amazon EC2 Auto Scaling group.
  This is required when managing Amazon EC2 auto scaling groups when using the cluster
  auto scaling feature. The tag is the ECS-managed tag that the console
  automatically adds to the group to indicate is was created in the
  console.
- `iam`– Allows principals to list IAM roles and their
  attached policies. Principals can also list instance profiles available to your
  Amazon EC2 instances.

The following policy contains the required IAM permissions, and limits the actions
to the `ecsInstanceRole` role.

The Auto Scaling permissions are not limited.

JSON

```
`{
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "iam:AttachRolePolicy",
 "iam:CreateRole",
 "iam:CreateInstanceProfile",
 "iam:AddRoleToInstanceProfile",
 "iam:ListInstanceProfilesForRole",
 "iam:GetRole"
 ],
 "Resource": "arn:aws:iam::*:role/ecsInstanceRole"
 },
 {
 "Effect": "Allow",
 "Action": "autoscaling:CreateOrUpdateTags",
 "Resource": "*"
 }
 ]
}`

```

## Permissions required for creating a

service

When you create a service in the console, you need additional permissions that grant
you permissions to manage AWS CloudFormation stacks. The following additional permissions are
required:

- `cloudformation` – Allows principals to create and manage
  AWS CloudFormation stacks. This is required when creating Amazon ECS services using the AWS Management Console
  and the subsequent managing of those services.

The following policy contains the required permissions, and limits the actions to
resources created in the Amazon ECS console.

JSON

```
`{
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "cloudformation:CreateStack",
 "cloudformation:DeleteStack",
 "cloudformation:DescribeStack*",
 "cloudformation:UpdateStack"
 ],
 "Resource": [
 "arn:*:cloudformation:*:*:stack/ECS-Console-V2-Service-*"
 ]
 }
 ]
}`

```
