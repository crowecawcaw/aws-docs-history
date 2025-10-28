# Amazon ECS infrastructure IAM role

An Amazon ECS infrastructure IAM role allows Amazon ECS to manage infrastructure resources in your
clusters on your behalf, and is used when:

- You want to attach Amazon EBS volumes to your Fargate or EC2 launch
  type Amazon ECS tasks. The infrastructure role allows Amazon ECS to manage Amazon EBS volumes for
  your tasks.

You can use the `AmazonECSInfrastructureRolePolicyForVolumes` managed policy.

- You want to use Transport Layer Security (TLS) to encrypt traffic between your
  Amazon ECS Service Connect services.

You can use the `AmazonECSInfrastructureRolePolicyForServiceConnectTransportLayerSecurity` managed policy.

- You want to create Amazon VPC Lattice target groups.

You can use the `AmazonECSInfrastructureRolePolicyForVpcLattice` managed policy.

- You want to use Amazon ECS Managed Instances in your Amazon ECS clusters. The infrastructure role allows Amazon ECS to manage the lifecycle of managed instances.

You can use the `AmazonECSInfrastructureRolePolicyForManagedInstances` managed policy.
When Amazon ECS assumes this role to take actions on your behalf, the events will be visible
in AWS CloudTrail. If Amazon ECS uses the role to manage Amazon EBS volumes attached to your tasks, the CloudTrail
log `roleSessionName` will be `ECSTaskVolumesForEBS`. If the role is
used to encrypt traffic between your Service Connect services, the CloudTrail log
`roleSessionName` will be `ECSServiceConnectForTLS`. If the role
is used to create target groups for VPC Lattice, the CloudTrail log
`roleSessionName` will be `ECSNetworkingWithVPCLattice`. If the role
is used to manage Amazon ECS Managed Instances, the CloudTrail log `roleSessionName` will be
`ECSManagedInstancesForCompute`. You can use
this name to search events in the CloudTrail console by filtering for **User
name**.

Amazon ECS provides managed policies which contain the permissions required for volume
attachment, TLS, VPC Lattice, and managed instances. For more information see, [AmazonECSInfrastructureRolePolicyForVolumes](../../../aws-managed-policy/latest/reference/AmazonECSInfrastructureRolePolicyForVolumes.md "../../../aws-managed-policy/latest/reference/AmazonECSInfrastructureRolePolicyForVolumes.md"), [AmazonECSInfrastructureRolePolicyForServiceConnectTransportLayerSecurity](../../../aws-managed-policy/latest/reference/AmazonECSInfrastructureRolePolicyForServiceConnectTransportLayerSecurity.md "../../../aws-managed-policy/latest/reference/AmazonECSInfrastructureRolePolicyForServiceConnectTransportLayerSecurity.md"), [AmazonECSInfrastructureRolePolicyForVpcLattice](../../../aws-managed-policy/latest/reference/AmazonECSInfrastructureRolePolicyForVpcLattice.md "../../../aws-managed-policy/latest/reference/AmazonECSInfrastructureRolePolicyForVpcLattice.md"), and [AmazonECSInfrastructureRolePolicyForManagedInstances](../../../aws-managed-policy/latest/reference/AmazonECSInfrastructureRolePolicyForManagedInstances.md "../../../aws-managed-policy/latest/reference/AmazonECSInfrastructureRolePolicyForManagedInstances.md") in the
_AWS Managed Policy Reference Guide_.

## Creating the Amazon ECS infrastructure role

Replace all `user input` with your own
information.

1. Create a file named `ecs-infrastructure-trust-policy.json` that
   contains the trust policy to use for the IAM role. The file should contain the
   following:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowAccessToECSForInfrastructureManagement",
 "Effect": "Allow",
 "Principal": {
 "Service": "ecs.amazonaws.com"
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```

2. Use the following AWS CLI command to create a role named
   `ecsInfrastructureRole` by using the trust policy that you
   created in the previous step.

```
`aws iam create-role \
 --role-name `ecsInfrastructureRole` \
 --assume-role-policy-document file://`ecs-infrastructure-trust-policy.json``
```

3. Depending on your use case, attach the managed policy to the
   `ecsInfrastructureRole` role.
   - To attach Amazon EBS volumes to your Fargate or EC2 launch
     type Amazon ECS tasks, attach the
     `AmazonECSInfrastructureRolePolicyForVolumes` managed
     policy.
   - To use Transport Layer Security (TLS) to encrypt traffic between your
     Amazon ECS Service Connect services, attach the
     `AmazonECSInfrastructureRolePolicyForServiceConnectTransportLayerSecurity`
     managed policy.
   - To create Amazon VPC Lattice target groups, attach the
     `AmazonECSInfrastructureRolePolicyForVpcLattice` managed
     policy.
   - You want to use Amazon ECS Managed Instances in your Amazon ECS clusters, attach the
     `AmazonECSInfrastructureRolePolicyForManagedInstances`
     managed policy.

```
`aws iam attach-role-policy \
 --role-name `ecsInfrastructureRole` \
 --policy-arn arn:aws:iam::aws:policy/service-role/AmazonECSInfrastructureRolePolicyForVolumes`
```

```
`aws iam attach-role-policy \
 --role-name `ecsInfrastructureRole` \
 --policy-arn arn:aws:iam::aws:policy/service-role/AmazonECSInfrastructureRolePolicyForServiceConnectTransportLayerSecurity`
```

```
`aws iam attach-role-policy \
 --role-name `ecsInfrastructureRole` \
 --policy-arn arn:aws:iam::aws:policy/AmazonECSInfrastructureRolePolicyForManagedInstances`
```

You can also use the IAM console's **Custom trust policy** workflow
to create the role. For more information, see [Creating a role using
custom trust policies (console)](../../../IAM/latest/UserGuide/id_roles_create_for-custom.md "../../../IAM/latest/UserGuide/id_roles_create_for-custom.md") in the _IAM User
Guide_.

###### Important

If the infrastructure role is being used by Amazon ECS to manage Amazon EBS volumes attached
to your tasks, ensure the following before you stop tasks that use Amazon EBS
volumes.

- The role isn't deleted.
- The trust policy for the role isn't modified to remove Amazon ECS access
  (`ecs.amazonaws.com`).
- The managed policy
  `AmazonECSInfrastructureRolePolicyForVolumes` isn't removed.
  If you must modify the role's permissions, retain at least
  `ec2:DetachVolume`, `ec2:DeleteVolume`, and
  `ec2:DescribeVolumes` for volume deletion.
  Deleting or modifying the role before stopping tasks with attached Amazon EBS volumes
  will result in the tasks getting stuck in `DEPROVISIONING` and the
  associated Amazon EBS volumes failing to delete. Amazon ECS will automatically retry at regular intervals
  to stop the task and delete the volume until the necessary permissions are
  restored. You can view a task's volume attachment status and associated status reason by using the [DescribeTasks](../APIReference/API_DescribeTasks.md "../APIReference/API_DescribeTasks.md") API.

After you create the file, you must grant your user permission to pass the role to
Amazon ECS.

## Permission to pass the

infrastructure role to Amazon ECS

To use an ECS infrastructure IAM role, you must grant your user permission to pass
the role to Amazon ECS. Attach the following `iam:PassRole` permission to your
user. Replace `ecsInfrastructureRole` with the name of the
infrastructure role that you created.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [

 {
 "Action": "iam:PassRole",
 "Effect": "Allow",
 "Resource": ["arn:aws:iam::*:role/`ecsInfrastructureRole`"],
 "Condition": {
 "StringEquals": {"iam:PassedToService": "ecs.amazonaws.com"}
 }
 }
 ]
}`

```

For more information about `iam:Passrole` and updating permissions for your
user, see [Granting a user permissions to
pass a role to an AWS service](../../../IAM/latest/UserGuide/id_roles_use_passrole.md "../../../IAM/latest/UserGuide/id_roles_use_passrole.md") and [Changing permissions for
an IAM user](../../../IAM/latest/UserGuide/id_users_change-permissions.md "../../../IAM/latest/UserGuide/id_users_change-permissions.md") in the _AWS Identity and Access Management User
Guide_.
