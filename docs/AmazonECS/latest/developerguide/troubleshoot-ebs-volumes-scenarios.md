# Status reasons for Amazon EBS volume attachment to Amazon ECS tasks

Use the following reference to fix issues that you might encounter in the form of
status reasons in the AWS Management Console when you configure Amazon EBS volumes for attachment to Amazon ECS
tasks. For more information on locating these status reasons in the console, see [Check volume attachment
status](troubleshoot-ebs-volumes.md#troubleshoot-ebs-volumes-location "troubleshoot-ebs-volumes.md#troubleshoot-ebs-volumes-location").

**`ECS was unable to assume the configured ECS Infrastructure Role
 'arn:aws:iam::`111122223333`:role/`ecsInfrastructureRole`'.
 Please verify that the role being passed has the proper trust relationship
 with Amazon ECS`**

This status reason appears in the following scenarios.

- You provide an IAM role without the necessary trust policy
  attached. Amazon ECS can't access the Amazon ECS infrastructure IAM role
  that you provide if the role doesn't have the necessary trust
  policy.
  The task can get stuck in the `DEPROVISIONING` state. For
  more information about the necessary trust policy, see [Amazon ECS infrastructure IAM role](infrastructure_IAM_role.md "infrastructure_IAM_role.md").
- Your IAM user doesn't have permission to pass the Amazon ECS
  infrastructure role to Amazon ECS. The task can get stuck in the
  `DEPROVISIONING` state. To avoid this problem, you
  can attach the `PassRole` permission to your user. For
  more information, see [Amazon ECS infrastructure IAM role](infrastructure_IAM_role.md "infrastructure_IAM_role.md").
- Your IAM role doesn't have the necessary permissions for Amazon EBS
  volume attachment. The task can get stuck in the
  `DEPROVISIONING` state. For more information about
  the specific permissions necessary for attaching Amazon EBS volumes to
  tasks, see [Amazon ECS infrastructure IAM role](infrastructure_IAM_role.md "infrastructure_IAM_role.md").

###### Note

You may also see this error message due to a delay in role
propagation. If retrying to use the role after waiting for a few minutes
doesn't fix the issue, you might have misconfigured the trust policy for
the role.

**`ECS failed to set up the EBS volume. Encountered
 IdempotentParameterMismatch"; "The client token you have provided is
 associated with a resource that is already deleted. Please use a different
 client token."`**

The following AWS KMS key scenarios can lead to an
`IdempotentParameterMismatch` message appearing:

- You specify a KMS key ARN, ID, or alias that isn't valid. In
  this scenario, the task might appear to launch successfully, but the
  task eventually fails because AWS authenticates the KMS key
  asynchronously. For more information, see [Amazon EBS
  encryption](../../../ebs/latest/userguide/ebs-encryption.md "../../../ebs/latest/userguide/ebs-encryption.md") in the _Amazon EC2 User
  Guide_.
- You provide a customer managed key that lacks the permissions that allow the
  Amazon ECS infrastructure IAM role to use the key for encryption. To
  avoid key-policy permission issues, see the example AWS KMS key policy
  in [Data encryption for Amazon EBS volumes](ebs-volumes.md#ebs-kms-encryption "ebs-volumes.md#ebs-kms-encryption").

You can set up Amazon EventBridge to send Amazon EBS volume events and Amazon ECS task state
change events to a target, such as Amazon CloudWatch groups. You can then use these
events to identify the specific customer managed key related issue that affected
volume attachment. For more information, see

- [How can I create a CloudWatch log group to use as a target for an
  EventBridge rule?](https://repost.aws/knowledge-center/cloudwatch-log-group-eventbridge "https://repost.aws/knowledge-center/cloudwatch-log-group-eventbridge") on AWS re:Post.
- [Task state change events](ecs_cwe_events.md#ecs_task_events "ecs_cwe_events.md#ecs_task_events").
- [Amazon EventBridge events
  for Amazon EBS](../../../ebs/latest/userguide/ebs-cloud-watch-events.md "../../../ebs/latest/userguide/ebs-cloud-watch-events.md") in the _Amazon EBS User
  Guide_.

**`ECS timed out while configuring the EBS volume attachment to your
 Task`**.

The following file system format scenarios result in this message.

- The file system format that you specify during configuration isn't
  compatible with the [task's operating system](../APIReference/API_RuntimePlatform.md "../APIReference/API_RuntimePlatform.md").
- You configure an Amazon EBS volume to be created from a snapshot, and
  the snapshot's file system format isn't compatible with the task's
  operating system. For volumes created from a snapshot, you must
  specify the same filesystem type that the volume was using when the
  snapshot was created.

You can utilize the Amazon ECS container agent logs to troubleshoot this
message for EC2 tasks. For more information, see [Amazon ECS log file locations](logs.md "logs.md") and [Amazon ECS log
collector](ecs-logs-collector.md "ecs-logs-collector.md").
