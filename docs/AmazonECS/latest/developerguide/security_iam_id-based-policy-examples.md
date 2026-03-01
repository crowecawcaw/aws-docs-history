# Identity-based policy examples for Amazon Elastic Container Service

By default, users and roles don't have permission to create or modify Amazon ECS
resources. To grant users permission to perform actions on the
resources that they need, an IAM administrator can create IAM policies.

To learn how to create an IAM identity-based policy by using these example JSON policy
documents, see [Create IAM policies (console)](../../../IAM/latest/UserGuide/access_policies_create-console.md "../../../IAM/latest/UserGuide/access_policies_create-console.md") in the
_IAM User Guide_.

For details about actions and resource types defined by Amazon ECS, including the format of the ARNs for each of the resource types, see [Actions, resources, and condition keys for Amazon Elastic Container Service](../../../service-authorization/latest/reference/list_amazonelasticcontainerservice.md "../../../service-authorization/latest/reference/list_amazonelasticcontainerservice.md") in the _Service Authorization Reference_.

###### Topics

- [Amazon ECS policy best practices](#security_iam_service-with-iam-policy-best-practices "#security_iam_service-with-iam-policy-best-practices")
- [Allow Amazon ECS users to view their own permissions](#security_iam_id-based-policy-examples-view-own-permissions "#security_iam_id-based-policy-examples-view-own-permissions")
- [Amazon ECS cluster examples](#IAM_cluster_policies "#IAM_cluster_policies")
- [Amazon ECS container instance examples](#IAM_container_instance_policies "#IAM_container_instance_policies")
- [Amazon ECS task definition examples](#IAM_task_definition_policies "#IAM_task_definition_policies")
- [Run Amazon ECS Task Example](#IAM_run_policies "#IAM_run_policies")
- [Start Amazon ECS task example](#IAM_start_policies "#IAM_start_policies")
- [List and describe Amazon ECS task examples](#IAM_task_policies "#IAM_task_policies")
- [Create Amazon ECS service example](#IAM_create_service_policies "#IAM_create_service_policies")
- [Describing Amazon ECS services based on tags](#security_iam_id-based-policy-examples-view-cluster-tags "#security_iam_id-based-policy-examples-view-cluster-tags")
- [Deny Amazon ECS Service Connect Namespace Override Example](#IAM_disable_namespace_override_policies "#IAM_disable_namespace_override_policies")

## Amazon ECS policy best practices

Identity-based policies determine whether someone can create, access, or delete Amazon ECS resources in your
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
  if they are used through a specific AWS service, such as CloudFormation. For more information, see
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

## Allow Amazon ECS users to view their own permissions

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

## Amazon ECS cluster examples

The following IAM policy allows permission to create and list clusters. The `CreateCluster` and `ListClusters` actions do not accept any resources, so the resource definition is set to `*` for all resources.

JSON

```
`{
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "ecs:CreateCluster",
 "ecs:ListClusters"
 ],
 "Resource": "*"
 }
 ]
}`

```

JSON

```
`{
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "ecs:DescribeClusters",
 "ecs:DeleteCluster"
 ],
 "Resource": ["arn:aws:ecs:us-east-1:123456789012:cluster/`cluster-name`"]
 }
 ]
}`

```

The following IAM policy allows permission to describe and delete a specific cluster. The `DescribeClusters` and `DeleteCluster` actions accept cluster ARNs as resources.

JSON

```
`{
 "Statement": [
 {
 "Action": [
 "ecs:Describe*",
 "ecs:List*"
 ],
 "Effect": "Allow",
 "Resource": "*"
 },
 {
 "Action": [
 "ecs:DeleteCluster",
 "ecs:DeregisterContainerInstance",
 "ecs:ListContainerInstances",
 "ecs:RegisterContainerInstance",
 "ecs:SubmitContainerStateChange",
 "ecs:SubmitTaskStateChange"
 ],
 "Effect": "Allow",
 "Resource": "arn:aws:ecs:us-east-1:`123456789012`:cluster/default"
 },
 {
 "Action": [
 "ecs:DescribeContainerInstances",
 "ecs:DescribeTasks",
 "ecs:ListTasks",
 "ecs:UpdateContainerAgent",
 "ecs:StartTask",
 "ecs:StopTask",
 "ecs:RunTask"
 ],
 "Effect": "Allow",
 "Resource": "*",
 "Condition": {
 "ArnEquals": {"ecs:cluster": "arn:aws:ecs:us-east-1:123456789012:cluster/default"}
 }
 }
 ]
}`

```

The following IAM policy can be attached to a user or group that would only allow
that user or group to perform operations on a specific cluster.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "ecs:Describe*",
 "ecs:List*"
 ],
 "Effect": "Allow",
 "Resource": "*"
 },
 {
 "Action": [
 "ecs:DeleteCluster",
 "ecs:DeregisterContainerInstance",
 "ecs:ListContainerInstances",
 "ecs:RegisterContainerInstance",
 "ecs:SubmitContainerStateChange",
 "ecs:SubmitTaskStateChange"
 ],
 "Effect": "Allow",
 "Resource": "arn:aws:ecs:us-east-1:111122223333:cluster/default"
 },
 {
 "Action": [
 "ecs:DescribeContainerInstances",
 "ecs:DescribeTasks",
 "ecs:ListTasks",
 "ecs:UpdateContainerAgent",
 "ecs:StartTask",
 "ecs:StopTask",
 "ecs:RunTask"
 ],
 "Effect": "Allow",
 "Resource": "*",
 "Condition": {
 "ArnEquals": {"ecs:cluster": "arn:aws:ecs:us-east-1:111122223333:cluster/default"}
 }
 }
 ]
}`

```

## Amazon ECS container instance examples

Container instance registration is handled by the Amazon ECS agent, but there may be times
where you want to allow a user to deregister an instance manually from a cluster.
Perhaps the container instance was accidentally registered to the wrong cluster, or the
instance was terminated with tasks still running on it.

The following IAM policy allows a user to list and deregister container instances
in a specified cluster:

JSON

```
`{
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "ecs:DeregisterContainerInstance",
 "ecs:ListContainerInstances"
 ],
 "Resource": "arn:aws:ecs:us-east-1:123456789012:cluster/`cluster_name`"
 }
 ]
}`

```

## Amazon ECS task definition examples

Task definition IAM policies do not support resource-level permissions, but the
following IAM policy allows a user to register, list, and describe task
definitions:

If you use the console, you must add `CloudFormation: CreateStack` as an `Action`.

JSON

```
`{
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "ecs:RegisterTaskDefinition",
 "ecs:ListTaskDefinitions",
 "ecs:DescribeTaskDefinition"
 ],
 "Resource": "*"
 }
 ]
}`

```

## Run Amazon ECS Task Example

The resources for `RunTask` are task definitions. To limit which clusters a user can run task definitions on, you can specify them in the `Condition` block. The advantage is that you don't have to list both task definitions and clusters in your resources to allow the appropriate access. You can apply one, the other, or both.

The following IAM policy allows permission to run any revision of a specific task
definition on a specific cluster:

JSON

```
`{
 "Statement": [
 {
 "Effect": "Allow",
 "Action": ["ecs:RunTask"],
 "Condition": {
 "ArnEquals": {"ecs:cluster": "arn:aws:ecs:us-east-1:123456789012:cluster/cluster_name"}
 },
 "Resource": ["arn:aws:ecs:us-east-1:123456789012:task-definition/task_family:*"]
 }
 ]
}`

```

## Start Amazon ECS task example

The resources for `StartTask` are task definitions. To limit which clusters and container instances a user can start task definitions on, you can specify them in the `Condition` block. The advantage is that you don't have to list both task definitions and clusters in your resources to allow the appropriate access. You can apply one, the other, or both.

The following IAM policy allows permission to start any revision of a specific task
definition on a specific cluster and specific container instance.

###### Note

For this example, when you call the `StartTask` API with the AWS CLI or another AWS SDK, you must specify the task definition revision so that the `Resource` mapping matches.

JSON

```
`{
 "Statement": [
 {
 "Effect": "Allow",
 "Action": ["ecs:StartTask"],
 "Condition": {
 "ArnEquals": {
 "ecs:cluster": "arn:aws:ecs:us-east-1:123456789012:cluster/`cluster_name`",
 "ecs:container-instances": ["arn:aws:ecs:us-east-1:123456789012:container-instance/`cluster_name`/`container_instance_UUID`"]
 }
 },
 "Resource": ["arn:aws:ecs:us-east-1:123456789012:task-definition/`task_family`:*"]
 }
 ]
}`

```

## List and describe Amazon ECS task examples

The following IAM policy allows a user to describe a specified task in a specified
cluster:

JSON

```
`{
 "Statement": [
 {
 "Effect": "Allow",
 "Action": ["ecs:DescribeTasks"],
 "Condition": {
 "ArnEquals": {"ecs:cluster": "arn:aws:ecs:us-east-1:123456789012:cluster/`cluster_name`"}
 },
 "Resource": ["arn:aws:ecs:us-east-1:123456789012:task/`cluster_name`/`task_UUID`"]
 }
 ]
}`

```

## Create Amazon ECS service example

The following IAM policy allows a user to create Amazon ECS services in the
AWS Management Console:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "application-autoscaling:Describe*",
 "application-autoscaling:PutScalingPolicy",
 "application-autoscaling:RegisterScalableTarget",
 "cloudwatch:DescribeAlarms",
 "cloudwatch:PutMetricAlarm",
 "ecs:List*",
 "ecs:Describe*",
 "ecs:CreateService",
 "elasticloadbalancing:Describe*",
 "iam:GetPolicy",
 "iam:GetPolicyVersion",
 "iam:GetRole",
 "iam:ListAttachedRolePolicies",
 "iam:ListRoles",
 "iam:ListGroups",
 "iam:ListUsers"
 ],
 "Resource": "*"
 }
 ]
}`

```

## Describing Amazon ECS services based on tags

You can use conditions in your identity-based policy to control access to Amazon ECS resources based on tags. This example shows how you might create a policy that allows describing your services. However, permission is granted only if the service tag `Owner` has the value of that user's user name. This policy also grants the permissions necessary to complete this action on the console.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "DescribeServices",
 "Effect": "Allow",
 "Action": "ecs:DescribeServices",
 "Resource": "*"
 },
 {
 "Sid": "ViewServiceIfOwner",
 "Effect": "Allow",
 "Action": "ecs:DescribeServices",
 "Resource": "arn:aws:ecs:*:*:service/*",
 "Condition": {
 "StringEquals": {"ecs:ResourceTag/Owner": "${aws:username}"}
 }
 }
 ]
}`

```

You can attach this policy to the IAM users in your account. If a user named `richard-roe` attempts to describe an Amazon ECS service, the service must be tagged `Owner=richard-roe` or `owner=richard-roe`. Otherwise he is denied access. The condition tag key `Owner` matches both `Owner` and `owner` because condition key names are not case-sensitive. For more information, see [IAM JSON Policy
Elements: Condition](../../../IAM/latest/UserGuide/reference_policies_elements_condition.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition.md") in the _IAM User Guide_.

## Deny Amazon ECS Service Connect Namespace Override Example

The following IAM policy denies a user from overriding the default Service Connect namespace in a service configuration. The default namespace is set in the cluster. However, you can override it in a service configuration. For consistency, consider setting all your new services to use the same namespace. Use the following context keys to require services to use a specific namespace. Replace the `<region>`, `<aws_account_id>`, `<cluster_name>` and `<namespace_id>` with your own in the following example.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "ecs:CreateService",
 "ecs:UpdateService"
 ],
 "Condition": {
 "ArnEquals": {
 "ecs:cluster": "arn:aws:ecs:us-east-1:123456789012:cluster/`cluster_name`",
 "ecs:namespace": "arn:aws:servicediscovery:us-east-1:123456789012:namespace/`namespace_id`"
 }
 },
 "Resource": "*"
 }
 ]
}`

```
