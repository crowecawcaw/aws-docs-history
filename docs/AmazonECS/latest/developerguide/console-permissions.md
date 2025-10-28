# Permissions required for the Amazon ECS console

Following the best practice of granting least privilege, you can use the
`AmazonECS_FullAccess` managed policy as a template for creating you own
custom policy. That way, you can take away or add permissions to and from the managed policy
based on your specific requirements. For more information, see [AmazonECS_FullAccess](../../../aws-managed-policy/latest/reference/AmazonECS_FullAccess.md "../../../aws-managed-policy/latest/reference/AmazonECS_FullAccess.md") in the _AWS Managed Policy Reference_.

## Permissions for creating IAM roles

The following actions require additional permissions in order to complete the
operation:

- Registering an external instance - for more information, see [Amazon ECS Anywhere IAM role](iam-role-ecsanywhere.md "iam-role-ecsanywhere.md")
- Registering a task definition - for more information, see [Amazon ECS task execution IAM role](task_execution_IAM_role.md "task_execution_IAM_role.md")
- Creating an EventBridge rule to use for scheduling tasks - for more information, see [Amazon ECS EventBridge IAM Role](CWE_IAM_role.md "CWE_IAM_role.md")

You can add these permissions by creating a role in IAM before you use them in the Amazon ECS
console. If you do not create the roles, the Amazon ECS console creates then on your behalf.

## Permissions required for registering an

external instance to a cluster

You need additional permissions when you register an external instance to a cluster
and you want to create a new external instance
(`ecsExternalInstanceRole`) role.

The following additional permissions are required:

- `iam`– Allows principals to create and list IAM roles and
  their attached policies.
  - iam:AttachRolePolicy
  - iam:CreateRole
  - am:CreateInstanceProfile
  - iam:AddRoleToInstanceProfile
  - iam:ListInstanceProfilesForRole
  - iam:GetRole

- `ssm` – Allows principals to register the external
  instance with Systems Manager.

###### Note

In order to choose an existing `ecsExternalInstanceRole`, you must have the
`iam:GetRole` and `iam:PassRole` permissions.

The following policy contains the required permissions, and limits the actions to the
`ecsExternalInstanceRole` role.

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
 "Resource": "arn:aws:iam::*:role/ecsExternalInstanceRole"
 },
 {
 "Effect": "Allow",
 "Action": ["iam:PassRole","ssm:CreateActivation"],
 "Resource": "arn:aws:iam::*:role/ecsExternalInstanceRole"
 }
 ]
}`

```

## Permissions required for registering a task

definition

You need additional permissions when you register a task definition and you want to
create a new task execution (`ecsTaskExecutionRole`) role.

The following additional permissions are required:

- `iam`– Allows principals to create and list IAM roles and
  their attached policies.
  - iam:AttachRolePolicy
  - iam:CreateRole
  - iam:GetRole

###### Note

In order to choose an existing `ecsTaskExecutionRole`, you must have the
`iam:GetRole` permission.

The following policy contains the required permissions, and limits the actions to the
`ecsTaskExecutionRole` role.

JSON

```
`{
"Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "iam:AttachRolePolicy",
 "iam:CreateRole",
 "iam:GetRole"
 ],
 "Resource": "arn:aws:iam::*:role/ecsTaskExecutionRole"
 }
 ]
}`

```

## Permissions required for using Amazon Q Developer to provide

recommendations in the console

For Amazon Q Developer to provide recommendations in the Amazon ECS; console, you must enable the
correct IAM permissions for either your IAM user or role. You must add the
`codewhisperer:GenerateRecommendations` permission.

JSON

```
`{
"Statement": [
 {
 "Sid": "AmazonQDeveloperPermissions",
 "Effect": "Allow",
 "Action": ["codewhisperer:GenerateRecommendations"],
 "Resource": "*"
 }
 ]
}`

```

To use inline chat in the Amazon ECS; console, you must enable the correct IAM permissions
for either your IAM user or role. You must add the `q:SendMessage` permission.:

JSON

```
`{
"Statement": [
 {
 "Sid": "AmazonQDeveloperInlineChatPermissions",
 "Effect": "Allow",
 "Action": ["q:SendMessage"],
 "Resource": "*"
 }
 ]
}`

```

## Permissions required for creating an EventBridge rule for

scheduled tasks

You need additional permissions when you schedule a task and you want to create a new
CloudWatch Events role (`ecsEventsRole`) role.

The following additional permissions are required:

- `iam`– Allows principals to create and list IAM roles and
  their attached policies, and to allow Amazon ECS to pass the role to other services to
  assume the role.

###### Note

In order to choose an existing `ecsEventsRole`, you must have the
`iam:GetRole` and `iam:PassRole` permissions.

The following policy contains the required permissions, and limits the actions to the
`ecsEventsRole` role.

JSON

```
`{
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "iam:AttachRolePolicy",
 "iam:CreateRole",
 "iam:GetRole",
 "iam:PassRole"
 ],
 "Resource": "arn:aws:iam::*:role/ecsEventsRole"
 }
 ]
}`

```

## Permissions required for viewing service deployments

When you follow the best practice of granting least privilege, you need to add additional
permissions in order to view service deployments in the console.

You need access to the following actions:

- ListServiceDeployments
- DescribeServiceDeployments
- DescribeServiceRevisions

You need access to the following resources:

- Service
- Service deployment
- Service revision

The following example policy contains the required permissions, and limits the actions to a
specified service.

Replace the `account`, `cluster-name`, and `service-name`
with your values.

JSON

```
`{
"Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "ecs:ListServiceDeployments",
 "ecs:DescribeServiceDeployments",
 "ecs:DescribeServiceRevisions"
 ],
 "Resource": [
 "arn:aws:ecs:us-east-1:123456789012:service/cluster-name/service-name",
 "arn:aws:ecs:us-east-1:123456789012:service-deployment/cluster-name/service-name/*",
 "arn:aws:ecs:us-east-1:123456789012:service-revision/cluster-name/service-name/*"
 ]
 }
 ]
}`

```

## Permissions required to view Amazon ECS

lifecycle events in Container Insights

The following permissions are required to view the lifecycle events. Add the following
permissions as an inline policy to the role. For more information, see [Adding and Removing
IAM Policies](../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md "../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md")

- events:DescribeRule
- events:ListTargetsByRule
- logs:DescribeLogGroups

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "events:DescribeRule",
 "events:ListTargetsByRule",
 "logs:DescribeLogGroups"
 ],
 "Resource": "*"
 }
 ]
}`

```

## Permissions required for enabling Amazon ECS lifecycle events in Container Insights

The following permissions are required to configure the lifecycle events:

- events:PutRule
- events:PutTargets
- logs:CreateLogGroup

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "events:PutRule",
 "events:PutTargets",
 "logs:CreateLogGroup"
 ],
 "Resource": "*"
 }
 ]
}`

```
