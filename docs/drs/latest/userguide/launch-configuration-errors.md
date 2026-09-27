

# Launch configuration errors
<a name="launch-configuration-errors"></a>

The following errors occur when launch configuration settings, IAM permissions, or resource limits prevent AWS Elastic Disaster Recovery from launching recovery instances.

**Topics**
+ [Error: Instance not launched due to lifecycle state](#error-launch-lifecycle-state)
+ [Error: OS BYOL requires Dedicated Hosts](#error-byol-conflict)
+ [Error: EBS encryption key not found](#error-ebs-encryption-key)
+ [Error: Missing IAM permissions for launch](#error-launch-iam-permissions)
+ [Error: Instance store volume device name conflict](#Replicating-Instance-Stores)
+ [Error: Basic right-sizing is not supported for arm64](#error-arm64-basic-right-sizing)
+ [Error: In-AWS right-sizing cannot describe the source instance](#error-arm64-in-aws-right-sizing-access-denied)
+ [Error: Source instance not found for in-AWS right-sizing](#error-arm64-in-aws-right-sizing-source-not-found)
+ [Error: Source instance type is unavailable in the recovery Region](#error-arm64-in-aws-right-sizing-type-unavailable)
+ [Error: Launch template specifies an x86\_64 instance type for arm64](#error-arm64-instance-type-not-supported)
+ [Error: Instance requirements exclude arm64 instance types](#error-arm64-instance-requirements-conflict)
+ [Error: AMI architecture does not match the arm64 source](#error-arm64-ami-architecture-mismatch)
+ [Error: Invalid arm64 recovery settings](#error-invalid-arm64-recovery-settings)
+ [Error: Launch-into instance architecture does not match](#error-launch-into-architecture-mismatch)

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

## Error: Basic right-sizing is not supported for arm64
<a name="error-arm64-basic-right-sizing"></a>

**Error message**

Cannot set BASIC right sizing on source server {{source-server-id}}. BASIC right sizing is not supported for arm64/Graviton source servers. Use IN\_AWS or NONE instead.

**Cause**

You explicitly set **Active (basic)** right-sizing on an `arm64` source server.

**Resolution**

Set right-sizing to **Active (in-aws)** or **Inactive**. If the account default launch settings specify **Active (basic)** right-sizing, AWS Elastic Disaster Recovery applies **Active (in-aws)** right-sizing when it creates an `arm64` source server.

## Error: In-AWS right-sizing cannot describe the source instance
<a name="error-arm64-in-aws-right-sizing-access-denied"></a>

**Error message**

Could not apply in-AWS right sizing for source server {{source-server-id}} because AWS Elastic Disaster Recovery is unable to successfully make the DescribeInstances API call against the source EC2 instance {{instance-id}}.

**Cause**

AWS Elastic Disaster Recovery does not have permission to call `DescribeInstances` for the source Amazon EC2 instance. This error appears only when you change the right-sizing method for an `arm64` source server. Otherwise Elastic Disaster Recovery uses its recommended AWS Graviton instance type.

**Resolution**

Restore permission to describe the source instance, then retry the launch-settings update. For source servers replicated from another account, create the failback and in-AWS right-sizing roles in the source account. See [Creating the Failback and in-AWS right-sizing roles](adding-trusted-account.md#trusted-accounts-failback-role).

## Error: Source instance not found for in-AWS right-sizing
<a name="error-arm64-in-aws-right-sizing-source-not-found"></a>

**Error message**

Could not apply in-AWS right sizing for source server {{source-server-id}} because source instance {{instance-id}} was not found in its reported account and region.

**Cause**

The source Amazon EC2 instance no longer exists in the reported account and Region, or the recorded instance identity is incorrect. For when Elastic Disaster Recovery checks the source instance, see [Error: In-AWS right-sizing cannot describe the source instance](#error-arm64-in-aws-right-sizing-access-denied).

**Resolution**

Verify the source account, Region, and instance ID. Restore the source instance or reinstall the agent on the correct instance, then retry.

## Error: Source instance type is unavailable in the recovery Region
<a name="error-arm64-in-aws-right-sizing-type-unavailable"></a>

**Error message**

Could not apply in-AWS right sizing for source server {{source-server-id}} because source instance type {{instance-type}} is not available in the recovery region.

**Cause**

The source Graviton instance type is not offered in the recovery Region. Elastic Disaster Recovery runs this check only in the situations described in [Error: In-AWS right-sizing cannot describe the source instance](#error-arm64-in-aws-right-sizing-access-denied).

**Resolution**

Use **Inactive** right-sizing and configure a compatible Graviton type, or keep the right-sizing method unchanged so that Elastic Disaster Recovery selects a Graviton recommendation that is offered in the recovery Region.

## Error: Launch template specifies an x86\_64 instance type for arm64
<a name="error-arm64-instance-type-not-supported"></a>

**Error message**

Source server {{source-server-id}} is an arm64 (Graviton) source, but the launch template specifies instance type '{{instance-type}}', which is not an arm64 instance type. An aarch64 root volume cannot boot on an x86\_64 instance. Use a Graviton instance type (such as c6g, m6g, r6g, c7g, or t4g) in your launch template.

**Cause**

The launch template pins an `x86_64` instance type for an `arm64` source server.

**Resolution**

Select a Graviton instance type that is offered in the recovery location.

## Error: Instance requirements exclude arm64 instance types
<a name="error-arm64-instance-requirements-conflict"></a>

**Error message**

Source server {{source-server-id}} is an arm64 (Graviton) source, but the launch template's InstanceRequirements cannot be satisfied by any arm64 instance type. An aarch64 root volume cannot boot on an x86\_64 instance. Widen AllowedInstanceTypes to include a Graviton family (for example c6g.\*, m6g.\*, r6g.\*, c7g.\*, or t4g.\*), or relax the attribute constraints so at least one arm64 instance type qualifies.

**Cause**

The allowed, excluded, or attribute requirements match no `arm64` instance type offered in the recovery Region.

**Resolution**

Widen the allowed instance types or relax the requirements so that they match at least one Graviton type offered in the recovery Region.

## Error: AMI architecture does not match the arm64 source
<a name="error-arm64-ami-architecture-mismatch"></a>

**Error message**

Source server {{source-server-id}} is an arm64 (Graviton) source, but the AMI '{{ami-id}}' specified for launch has architecture '{{ami-architecture}}'. An aarch64 root volume cannot boot from an x86\_64 AMI. Use an arm64 AMI, or remove the AMI override to let DRS create an architecture-matched AMI.

**Cause**

The launch template or usage operation specifies an `x86_64` Amazon Machine Image (AMI) for an `arm64` source server.

**Resolution**

Use an `arm64` AMI, or remove the AMI override so that AWS Elastic Disaster Recovery creates an architecture-matched AMI.

## Error: Invalid arm64 recovery settings
<a name="error-invalid-arm64-recovery-settings"></a>

**Error message**

Action could not be completed. Invalid ARM64 recovery settings: {{violations}} in the launch configuration template.

**Cause**

The launch template contains one or more of these violations:
+ one of InstanceType or InstanceRequirements is required
+ instance type '{{instance-type}}' is not an arm64 (Graviton) type

At launch time, the messages described in [Error: AMI architecture does not match the arm64 source](#error-arm64-ami-architecture-mismatch) and [Error: Instance requirements exclude arm64 instance types](#error-arm64-instance-requirements-conflict) can also appear inside this error.

**Resolution**

Specify a Graviton instance type or satisfiable instance requirements in the launch template.

## Error: Launch-into instance architecture does not match
<a name="error-launch-into-architecture-mismatch"></a>

**Error message**

You cannot define the EC2 instance {{ec2-instance-id}} as a launch into instance ID as is has conflicting instance settings to those of the source server ({{source-server-id}}). The following fields have a configuration mismatch: Architecture.

**Cause**

The target instance does not use the same architecture as the protected server.

**Resolution**

Select a stopped target Amazon EC2 instance that uses the same architecture as the protected server and meets the other launch-into requirements.