# IAM best practices for Amazon ECS

You can use AWS Identity and Access Management (IAM) to manage and control access to your AWS services and
resources through rule-based policies for authentication and authorization purposes.
More specifically, through this service, you control access to your AWS resources by
using policies that are applied to users, groups, or roles. Among these three, users are
accounts that can have access to your resources. And, an IAM role is a set of
permissions that can be assumed by an authenticated identity, which isn't associated
with a particular identity outside of IAM. For more information, see [Amazon ECS overview of access management: Permissions and policies](../../../IAM/latest/UserGuide/introduction_access-management.md "../../../IAM/latest/UserGuide/introduction_access-management.md").

## Follow the policy of least privileged access

Create policies that are scoped to allow users to perform their prescribed jobs.
For example, if a developer needs to periodically stop a task, create a policy that only
permits that particular action. The following example only allows a user to stop a task
that belongs to a particular `task_family` on a cluster with a specific
Amazon Resource Name (ARN). Referring to an ARN in a condition is also an example of using
resource-level permissions. You can use resource-level permissions to specify the
resource that you want an action to apply to. For more information, see [Policy resources for Amazon ECS](security_iam_service-with-iam.md#security_iam_service-with-iam-id-based-policies-resources "security_iam_service-with-iam.md#security_iam_service-with-iam-id-based-policies-resources").

## Have cluster resources serve as the administrative boundary

Policies that are too narrowly scoped can cause a proliferation of roles and
increase administrative overhead. Rather than creating roles that are scoped to
particular tasks or services only, create roles that are scoped to clusters and use
the cluster as your primary administrative boundary.

## Create automated pipelines to isolate end-users from the API

You can limit the actions that users can use by creating pipelines that
automatically package and deploy applications onto Amazon ECS clusters. This effectively
delegates the job of creating, updating, and deleting tasks to the pipeline. For
more information, see [Tutorial: Amazon ECS
standard deployment with CodePipeline](../../../codepipeline/latest/userguide/ecs-cd-pipeline.md "../../../codepipeline/latest/userguide/ecs-cd-pipeline.md") in the
_AWS CodePipeline User Guide_.

## Use policy conditions for an added layer of security

When you need an added layer of security, add a condition to your policy. This can
be useful if you're performing a privileged operation or when you need to restrict
the set of actions that can be performed against particular resources. The following
example policy requires multi-factor authorization when deleting a cluster.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "ecs:DeleteCluster"
 ],
 "Condition": {
 "Bool": {
 "aws:MultiFactorAuthPresent": "true"
 }
 },
 "Resource": ["*"]
 }
 ]
}`

```

Tags applied to services are propagated to all the tasks that are part of that
service. Because of this, you can create roles that are scoped to Amazon ECS resources with
specific tags. In the following policy, an IAM principal starts and stops all tasks
with a tag-key of `Department` and a tag-value of
`Accounting`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "ecs:StartTask",
 "ecs:StopTask",
 "ecs:RunTask"
 ],
 "Resource": "arn:aws:ecs:us-east-1:123456789012:cluster/my-cluster",
 "Condition": {
 "StringEquals": {"ecs:ResourceTag/Department": "Accounting"}
 }
 }
 ]
}`

```

## Periodically audit access to the APIs

A user might change roles. After they change roles, the permissions that were
previously granted to them might no longer apply. Make sure that you audit who has
access to the Amazon ECS APIs and whether that access is still warranted. Consider
integrating IAM with a user lifecycle management solution that automatically
revokes access when a user leaves the organization. For more information, see [AWS
security audit guidelines](../../../IAM/latest/UserGuide/security-audit-guide.md "../../../IAM/latest/UserGuide/security-audit-guide.md") in the
_AWS Identity and Access Management User Guide_.
