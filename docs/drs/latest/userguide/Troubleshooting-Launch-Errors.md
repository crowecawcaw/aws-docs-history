# Troubleshooting launch and post-launch errors

This section describes common errors that occur during or after launching drill
or recovery instances, including conversion errors, Windows-specific issues, and
instance store volume conflicts.

###### Topics

- [Windows License activation – AWS](#Windows-License-Activation "#Windows-License-Activation")
- [Replicating Instance Store Volumes](#Replicating-Instance-Stores "#Replicating-Instance-Stores")
- [Windows Drive changes](#Windows-Drive-Changes "#Windows-Drive-Changes")
- [Error: Failed to connect using HTTP channel](#Error-Failed-to-connect-using-HTTP-channel "#Error-Failed-to-connect-using-HTTP-channel")
- [Windows Dynamic Disk troubleshooting](#Windows-Dynamic-Disk "#Windows-Dynamic-Disk")
- [Error: Conversion server launch failed](#error-conversion-server-launch-failed "#error-conversion-server-launch-failed")
- [Error: Conversion failed](#error-conversion-failed "#error-conversion-failed")
- [Error: Failed to take snapshot](#error-snapshot-failed "#error-snapshot-failed")
- [Error: Instance not launched due to lifecycle state](#error-launch-lifecycle-state "#error-launch-lifecycle-state")
- [Error: OS BYOL can only be used with EC2 Dedicated Hosts](#error-byol-conflict "#error-byol-conflict")
- [Error: EBS encryption key not found](#error-ebs-encryption-key "#error-ebs-encryption-key")
- [Error: Missing IAM permissions for launch](#error-launch-iam-permissions "#error-launch-iam-permissions")

## Windows License activation – AWS

AWS Elastic Disaster Recovery converts the Windows OS licenses to AWS Windows licenses and
activates them against the AWS KMS.

If license activation failed, follow [this AWS guide](https://aws.amazon.com/premiumsupport/knowledge-center/windows-activation-fails/ "https://aws.amazon.com/premiumsupport/knowledge-center/windows-activation-fails/") to resolve the issue.

###### Important

When performing a failback, AWS DRS does not have access to the Customer licenses
and therefore cannot activate the licenses. After failback is complete, you can
activate the licenses manually or using post-launch scripts.

## Replicating Instance Store Volumes

When installing the DRS agent on an EC2 Instance with Instance Store volumes attached, device name conflicts can arise in the Recovery Instance's EC2 Launch Template
if the template also specifies Instance Store volumes.

![Storage configuration interface showing EBS volumes and instance store volumes with device name conflict warning.](images/troubleshooting-4.png)

You can resolve this error in one of two ways:

- If you require protection of the data on the Source Server's Instance Store Volume, ensure the Recovery Instance's EC2 Launch Template is reconfigured
  to provide a unique Device Name that will not collide with the default Instance Store mappings.
  For example, the "Device Name" for the EBS volume can be changed to /dev/xvdc1.
- If you do not require protection of the data on the Source Server's Instance Store volume,
  ensure instance store volumes are excluded from replication via the --devices
  [installation parameter](installer-parameters.md "installer-parameters.md").
  The DRS agent will not populate any volumes excluded from replication in the EC2 Launch Template.

## Windows Drive changes

Users may see changes in Windows drive letter assignments (for example, Drive D changed to E) on
Target machines launched by AWS Elastic Disaster Recovery.

This happens because Windows sometimes reconfigures the drive letters when a
machine comes up on a new infrastructure, for example, if the source server had a
drive letter mapped to a disk that was not replicated (such as a network drive). You
can solve this issue by remapping the drive letters on the drill or recovery
instance correctly after it has been launched.

## Error: Failed to connect using HTTP channel

This error occurs when the Conversion server is unable to communicate with
the necessary AWS endpoints on TCP port 443. Although the replication server
operates in the same staging area subnet, the Conversion server is a separate
instance that may be affected by changes made after replication was established.

Check if any network changes were made to the staging area since replication
was set up (security group rules, network ACL changes, route table modifications,
or DNS configuration changes) that could affect the Conversion server reaching
the [required
AWS endpoints](Network-Requirements.md#TCP-443 "Network-Requirements.md#TCP-443").

Console

###### Verify Conversion server connectivity

1. In the VPC Console, check the staging area subnet's route
   table, security group, and network ACL to ensure outbound TCP
   443 is allowed to the AWS Elastic Disaster Recovery and S3 endpoints.
2. Check if any recent network changes were made (firewall
   settings, DNS settings, route table changes).
3. Launch a test instance in the staging area subnet and verify
   it can reach the [required
   endpoints](Network-Requirements.md#TCP-443 "Network-Requirements.md#TCP-443") on TCP port 443.

CLI

###### Verify Conversion server connectivity

1. From a test instance in the staging area subnet, test
   connectivity to the required endpoints:
   - **Linux:**

   ```
   # DRS endpoint
   curl -v https://drs.`region`.amazonaws.com 2>&1 | head -20

   # S3 endpoint
   curl -v https://s3.`region`.amazonaws.com 2>&1 | head -20

   # EC2 endpoint
   curl -v https://ec2.`region`.amazonaws.com 2>&1 | head -20
   ```

   - **Windows (PowerShell):**

   ```
   # DRS endpoint
   Test-NetConnection -ComputerName drs.`region`.amazonaws.com -Port 443

   # S3 endpoint
   Test-NetConnection -ComputerName s3.`region`.amazonaws.com -Port 443

   # EC2 endpoint
   Test-NetConnection -ComputerName ec2.`region`.amazonaws.com -Port 443
   ```

2. Check the staging area subnet's route table:

```
aws ec2 describe-route-tables \
  --filters Name=association.subnet-id,Values=`subnet-1234567890abcdefg` \
  --query 'RouteTables[0].Routes[*].{Dest:DestinationCidrBlock,Target:GatewayId||NatGatewayId}'
```

If the issue persists after confirming network connectivity, [create
a case](../../../awssupport/latest/user/case-management.md "../../../awssupport/latest/user/case-management.md") with AWS Premium Support.

## Windows Dynamic Disk troubleshooting

Moving a Windows Dynamic Disk from a local computer to another computer may change the disk
status to "Foreign", resulting in a disruption in replication. The solution is to import the
foreign disk, as discussed in [this Microsoft troubleshooting article](https://docs.microsoft.com/en-us/windows-server/storage/disk-management/troubleshooting-disk-management#a-dynamic-disks-status-is-foreign "https://docs.microsoft.com/en-us/windows-server/storage/disk-management/troubleshooting-disk-management#a-dynamic-disks-status-is-foreign").

## Error: Conversion server launch failed

If you see `Conversion server launch failed`, the conversion server
could not be launched or did not become available within the expected time.

Retry the launch. If the issue persists, [create
a case](../../../awssupport/latest/user/case-management.md "../../../awssupport/latest/user/case-management.md") with AWS Support and include the recovery job ID from the
AWS Elastic Disaster Recovery Console.

## Error: Conversion failed

If you see `Conversion failed` in the recovery job history, the
volume conversion process did not complete successfully.

Retry the launch. If the issue persists, [create
a case](../../../awssupport/latest/user/case-management.md "../../../awssupport/latest/user/case-management.md") with AWS Support and include the recovery job ID from the
AWS Elastic Disaster Recovery Console.

## Error: Failed to take snapshot

If you see `Failed to take snapshot` in the recovery job history,
AWS Elastic Disaster Recovery was unable to create a point-in-time snapshot for the launch.

If you are using a custom KMS key for EBS encryption, verify that the key
exists, is enabled, and that the AWS Elastic Disaster Recovery service roles have the required
permissions to use it.

Retry the launch. If the issue persists, [create
a case](../../../awssupport/latest/user/case-management.md "../../../awssupport/latest/user/case-management.md") with AWS Support and include the recovery job ID.

## Error: Instance not launched due to lifecycle state

If you see `instance not launched because server lifecycle state is not
 READY_FOR_TEST` or a similar lifecycle state error, the source server has
not completed initial sync or is not in the correct state for the requested
action.

- For recovery drills, the source server must be in
  **Ready for recovery** state (initial sync
  completed).
- Check the source server's data replication status in the AWS Elastic Disaster Recovery
  Console to verify that initial sync has completed.
- If the source server is in **Stalled**
  or **Disconnected** state, resolve the replication
  issue first.

## Error: OS BYOL can only be used with EC2 Dedicated Hosts

If you see `OS BYOL can only be used with EC2 Dedicated Hosts`,
the launch configuration has Bring Your Own License (BYOL) enabled but the
target instance is not configured to launch on a Dedicated Host.

To resolve, either:

- Configure the EC2 Launch Template to use a Dedicated Host.
- Disable the BYOL option in the AWS Elastic Disaster Recovery launch settings for the
  source server.

## Error: EBS encryption key not found

If you see `The EBS encryption key could not be found in this account`,
the KMS key specified in the replication settings does not exist or is not
accessible.

- Verify that the KMS key ARN in the replication settings is
  correct.
- Ensure the KMS key has not been deleted or disabled.
- Verify that the AWS Elastic Disaster Recovery service roles have
  `kms:CreateGrant` and `kms:DescribeKey` permissions
  on the key.

## Error: Missing IAM permissions for launch

If you see errors such as `Your IAM user do not have permission for
 ec2:CreateSecurityGroup` or similar permission errors during launch,
the IAM credentials lack the required permissions.

Verify that the required AWS Elastic Disaster Recovery IAM policies are attached. See
[Identity-based
policies for Elastic Disaster Recovery](using-identity-based-policies.md "using-identity-based-policies.md") for the full list of required permissions.
