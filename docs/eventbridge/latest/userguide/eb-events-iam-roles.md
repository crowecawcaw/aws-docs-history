# IAM roles for sending events to targets in Amazon EventBridge

To relay events to targets, EventBridge needs an IAM role.

###### To create an IAM role for sending events to EventBridge

1.  Open the IAM console at
    [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2.  To create an IAM role, follow the steps in [Creating a Role to Delegate
    Permissions to an AWS Service](../../../IAM/latest/UserGuide/id_roles_create_for-service.md "../../../IAM/latest/UserGuide/id_roles_create_for-service.md") in the _IAM User Guide_ .
    As you follow the steps, do the following:

        * In **Role Name**, use a name that is unique within your account.
        * In **Select Role Type**, choose **AWS Service Roles**, and
         then choose **Amazon EventBridge**. This grants EventBridge permissions to assume the role.
        * In **Attach Policy**, choose
         **AmazonEventBridgeFullAccess**.

    You can also create your own custom IAM policies to allow permissions for EventBridge actions and resources.
    You can attach these custom policies to the IAM users or groups that require those permissions. For more
    information about IAM policies, see [Overview of IAM
    Policies](../../../IAM/latest/UserGuide/access_policies.md "../../../IAM/latest/UserGuide/access_policies.md") in the _IAM User Guide_. For more information about managing and
    creating custom IAM policies, see [Managing IAM
    Policies](../../../IAM/latest/UserGuide/ManagingPolicies.md "../../../IAM/latest/UserGuide/ManagingPolicies.md") in the _IAM User Guide_.

## Permissions required for EventBridge to access targets using IAM roles

EventBridge targets typically require IAM roles that grant permission to EventBridge to invoke the target. The following are some examples for various AWS services and targets. For others, use the EventBridge console to create a Rule and create a new Role which will be created with a policy with well-scoped permissions preconfigured.

Amazon SQS, Amazon SNS, Lambda, CloudWatch Logs, and EventBridge bus targets do not use roles, and permissions to EventBridge must be granted via a resource policy. API Gateway targets can use either resource policies or IAM roles.

### API destinations

If the target is an API destination, the role that you specify must include a policy with the following statement:

- **Effect**: `Allow`
- **Action**: `events:InvokeApiDestination`
- **Resource**: `arn:aws:events:*:*:api-destination/*`

### Kinesis streams

If the target is a Kinesis stream, the role used to send event data to that target must include a policy with the following statement:

- **Effect**: `Allow`
- **Action**: `kinesis:PutRecord`
- **Resource**: `*`

### Systems Manager run commands

If the target is Systems Manager run command, and you specify one or more `InstanceIds`
values for the command, the role that you specify must include a policy with the following statement:

- **Effect**: `Allow`
- **Action**: `ssm:SendCommand`
- **Resources**: `arn:aws:ec2:`us-east-1`:`accountId`:instance/`instanceIds``, 
`arn:aws:ssm:`us-east-1`:*:document/`documentName``

If the target is Systems Manager run command, and you specify one or more tags for the command,
the role that you specify must include a policy with the following two actions:

- **Effect**: `Allow`
- **Action**: `ssm:SendCommand`
- **Resources**: `arn:aws:ec2::`accountId`:instance/*`
- **Condition:**

```
"StringEquals": {
  "ec2:ResourceTag/*": [
    "[[tagValues]]"
  ]
}
```

And:

- **Effect**: `Allow`
- **Action**: `ssm:SendCommand`
- **Resources**: `arn:aws:ssm:`us-east-1`:*:document/`documentName``

### Step Functions state machines

If the target is an AWS Step Functions state machine, the role that you specify must include a policy with the following:

- **Effect**: `Allow`
- **Action**: `states:StartExecution`
- **Resource**: `arn:aws:states:*:*:stateMachine:*`

### Amazon ECS tasks

If the target is an Amazon ECS task, the role that you specify must include the following
policy.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "ecs:RunTask"
 ],
 "Resource": [
 "arn:aws:ecs:*:`111122223333`:task-definition/`task-definition-name`"
 ],
 "Condition": {
 "ArnLike": {
 "ecs:cluster": "arn:aws:ecs:*:`111122223333`:cluster/`cluster-name`"
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": "iam:PassRole",
 "Resource": [
 "*"
 ],
 "Condition": {
 "StringLike": {
 "iam:PassedToService": "ecs-tasks.amazonaws.com"
 }
 }
 }
 ]
}`

```

The following policy allows built-in targets in EventBridge to perform Amazon EC2 actions on your
behalf. You need to use the AWS Management Console to create rules with built-in targets.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "TargetInvocationAccess",
 "Effect": "Allow",
 "Action": [
 "ec2:Describe*",
 "ec2:RebootInstances",
 "ec2:StopInstances",
 "ec2:TerminateInstances",
 "ec2:CreateSnapshot"
 ],
 "Resource": "*"
 }
 ]
}`

```

The following policy allows EventBridge to relay events to the Kinesis streams in your account.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "KinesisAccess",
 "Effect": "Allow",
 "Action": [
 "kinesis:PutRecord"
 ],
 "Resource": "*"
 }
 ]
}`

```

## Customer-managed policy example: Using tagging to control access to

rules

The following example shows a user policy that grant permissions for EventBridge actions. This
policy works when you use the EventBridge API, AWS SDKs, or the AWS CLI.

You can grant users access to specific EventBridge rules while preventing them from accessing
other rules. To do so, you tag both sets of rules and then use IAM policies that refer to
those tags. For more information about tagging EventBridge resources, see [Tagging resources in Amazon EventBridge](eb-tagging.md "eb-tagging.md").

You can grant an IAM policy to a user to allow access to only the rules with a
particular tag. You choose which rules to grant access to by tagging them with that
particular tag. For example, the following policy grants a user access to rules with the
value of `Prod` for the tag key `Stack`.

```
{
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "events:*",
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "aws:ResourceTag/Stack": "Prod"
                }
            }
        }
    ]
}
```

For more information about using IAM policy statements, see [Controlling Access Using Policies](../../../IAM/latest/UserGuide/access_controlling.md "../../../IAM/latest/UserGuide/access_controlling.md") in
the _IAM User Guide_.
