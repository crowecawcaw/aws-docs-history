# Cross-service confused deputy

prevention

The confused deputy problem is a security issue where an entity that doesn't have
permission to perform an action can coerce a more-privileged entity to perform the
action. In AWS, cross-service impersonation can result in the confused deputy problem.
Cross-service impersonation can occur when one service (the calling service) calls
another service (the called service). The calling service can be manipulated to use its
permissions to act on another customer's resources in a way it should not otherwise have
permission to access. To prevent this, AWS provides tools that help you protect your
data for all services with service principals that have been given access to resources
in your account.

We recommend using the [aws:SourceArn](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourcearn "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourcearn") and [aws:SourceAccount](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourceaccount "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourceaccount") global condition context keys in resource policies to
limit the permissions that CodeDeploy gives another service to the resource. If you use both
global condition context keys and the `aws:SourceArn` value contains the
account ID, the `aws:SourceAccount` value and the account in the
`aws:SourceArn` value must use the same account ID when used in the same
policy statement. Use `aws:SourceArn` if you want only one resource to be
associated with the cross-service access. Use `aws:SourceAccount` if you want
any resource in that account to be associated with the cross-service use.

For EC2/On-Premises, AWS Lambda, and regular
Amazon ECS deployments, the value of `aws:SourceArn` should
include the CodeDeploy deployment group ARN with which CodeDeploy is allowed to assume the IAM
role.

For [Amazon ECS blue/green
deployments created through CloudFormation](deployments-create-ecs-cfn.md "deployments-create-ecs-cfn.md"), the value of `aws:SourceArn`
should include the CloudFormation stack ARN with which CodeDeploy is allowed to assume the IAM
role.

The most effective way to protect against the confused deputy problem is to use the
`aws:SourceArn` key with the full ARN of the resource. If you don't know
the full ARN or if you're specifying multiple resources, use wildcard characters (\*) for
the unknown portions.

For example, you might use the following trust policy with a
EC2/On-Premises, AWS Lambda, or regular Amazon ECS
deployment:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "",
 "Effect": "Allow",
 "Principal": {
 "Service": "codedeploy.amazonaws.com"
 },
 "Action": "sts:AssumeRole",
 "Condition": {
 "StringEquals": {
 "aws:SourceAccount": "`111122223333`"
 },
 "ArnLike": {
 "aws:SourceArn": "arn:aws:codedeploy:`us-east-1`:`111122223333`:deploymentgroup:`myApplication`/*"
 }
 }
 }
 ]
}`

```

For an [Amazon ECS blue/green
deployment created through CloudFormation](deployments-create-ecs-cfn.md "deployments-create-ecs-cfn.md"), you might use:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "",
 "Effect": "Allow",
 "Principal": {
 "Service": "codedeploy.amazonaws.com"
 },
 "Action": "sts:AssumeRole",
 "Condition": {
 "StringEquals": {
 "aws:SourceAccount": "`111122223333`"
 },
 "ArnLike": {
 "aws:SourceArn": "arn:aws:cloudformation:`us-east-1`:`111122223333`:stack/`MyCloudFormationStackName`/*"
 }
 }
 }
 ]
}`

```
