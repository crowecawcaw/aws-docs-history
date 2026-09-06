

# Launch configuration errors
<a name="launch-configuration-errors"></a>

The following errors occur when launch configuration settings, IAM permissions, or resource limits prevent AWS Elastic Disaster Recovery from launching recovery instances.

**Topics**
+ [Error: Instance not launched due to lifecycle state](#error-launch-lifecycle-state)
+ [Error: OS BYOL requires Dedicated Hosts](#error-byol-conflict)
+ [Error: EBS encryption key not found](#error-ebs-encryption-key)
+ [Error: Missing IAM permissions for launch](#error-launch-iam-permissions)
+ [Error: Instance store volume device name conflict](#Replicating-Instance-Stores)

## Error: Instance not launched due to lifecycle state
<a name="error-launch-lifecycle-state"></a>

**Error message**

instance not launched because server lifecycle state is not READY\_FOR\_TEST

**Cause**

The source server has not completed initial sync or is not in the correct lifecycle state for the requested operation.

**Resolution**

To resolve this error, complete the following steps:

1. Verify that the source server is in the *Ready for recovery* state. For recovery drills, the server must have completed initial sync.

1. Check the data replication status in the AWS Elastic Disaster Recovery console.

1. If the server is in a *Stalled* or *Disconnected* state, resolve the replication issue before attempting to launch.

## Error: OS BYOL requires Dedicated Hosts
<a name="error-byol-conflict"></a>

**Error message**

OS BYOL can only be used with EC2 Dedicated Hosts

**Cause**

Bring Your Own License (BYOL) is enabled in the launch settings, but the Amazon EC2 Launch Template is not configured to use a Dedicated Host.

**Resolution**

Use one of the following options to resolve this error:
+ Configure the Amazon EC2 Launch Template to use a Dedicated Host.
+ Disable BYOL in the AWS Elastic Disaster Recovery launch settings for the source server.

## Error: EBS encryption key not found
<a name="error-ebs-encryption-key"></a>

**Error message**

The EBS encryption key could not be found in this account

**Cause**

The AWS KMS key specified in the replication settings does not exist or is not accessible from the target account.

**Resolution**

To resolve this error, verify the following:
+ The KMS key ARN in the replication settings is correct.
+ The key has not been deleted or disabled.
+ The AWS Elastic Disaster Recovery service roles have `kms:CreateGrant` and `kms:DescribeKey` permissions on the key.

## Error: Missing IAM permissions for launch
<a name="error-launch-iam-permissions"></a>

**Error message**

Your IAM user do not have permission for ec2:CreateSecurityGroup

**Cause**

The IAM credentials used for the launch operation lack required permissions.

**Resolution**

Verify that the required AWS Elastic Disaster Recovery IAM policies are attached to your user or role. For more information, see [Identity-based policies for AWS Elastic Disaster Recovery](https://docs.aws.amazon.com/drs/latest/userguide/using-identity-based-policies.html).

## Error: Instance store volume device name conflict
<a name="Replicating-Instance-Stores"></a>

**Error message**

Launch fails with device name conflicts when the source server has instance store volumes.

**Cause**

The Amazon EC2 Launch Template specifies instance store volumes that collide with device names used by AWS Elastic Disaster Recovery for replicated EBS volumes.

**Resolution**

Use one of the following options to resolve this error:
+ **If you need the instance store data** – Change the device name in the Amazon EC2 Launch Template to avoid the collision. For example, use `/dev/xvdc1`.
+ **If you don't need instance store data** – Exclude instance store volumes from replication by using the `--devices` installation parameter. AWS Elastic Disaster Recovery does not populate excluded volumes in the Launch Template. For more information, see [installation parameters](installer-parameters.md).