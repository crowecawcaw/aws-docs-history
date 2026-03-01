# Restore an Amazon EC2 instance

When you restore an EC2 instance, AWS Backup creates an Amazon Machine Image (AMI), an
instance, the Amazon EBS root volume, Amazon EBS data volumes (if the protected resource had data
volumes), and Amazon EBS snapshots. You can customize some instance settings using the AWS Backup
console, or a larger number of settings using the AWS CLI or an AWS SDK.

The following considerations apply to restoring EC2 instances:

- AWS Backup configures the restored instance to use the same key pair that the protected
  resource used originally. You can't specify a different key pair for the restored
  instance during the restore process.
- AWS Backup does not back up and restore user-data that is used while launching an Amazon EC2
  instance.
- When configuring the restored instance, you can choose between using the same
  instance profile that the protected resource used originally or launching without an
  instance profile. This is to prevent the possibility of privilege escalations. You can
  update the instance profile for the restored instance using the Amazon EC2 console.

If you use the original instance profile, you must grant AWS Backup the following
permissions, where the resource ARN is the ARN of the IAM role associated with the
instance profile.

```
{
      "Effect": "Allow",
      "Action": "iam:PassRole",
      "Resource": "arn:aws:iam::`account-id`:role/`role-name`"
},
```

Replace `role-name` with the name of the EC2 instance profile role that will be attached to the restored EC2 instance. This is not the AWS Backup service role, but rather the IAM role that provides permissions to applications running on the EC2 instance.

- During a restore, all Amazon EC2 quotas and configuration restrictions apply.
- If the vault containing your Amazon EC2 recovery points has a vault lock, see [Additional security considerations](vault-lock.md#using-vault-lock-with-backup "vault-lock.md#using-vault-lock-with-backup")
  for more information.

## Use the AWS Backup console to restore Amazon EC2 recovery points

You can restore an entire Amazon EC2 instance from a single recovery point, including the
root volume, data volumes, and some instance configuration settings, such as the instance
type and key pair.

###### To restore Amazon EC2 resources using the AWS Backup console

1. Open the AWS Backup console at [https://console.aws.amazon.com/backup](https://console.aws.amazon.com/backup "https://console.aws.amazon.com/backup").
2. In the navigation pane, choose **Protected resources**, then
   choose the ID of the Amazon EC2 resource to open the resource details page.
3. In the **Recovery points** pane, choose the radio button next to
   the ID of the recovery point to restore. In the upper-right corner of the pane, choose
   **Restore**.
4. In the **Network settings** pane, we use the settings from the
   protected instance to select the default values for the instance type, VPC, subnet,
   security group, and instance IAM role. You can use these default values or change
   them as needed.
5. In the **Restore role** pane, use the **Default
   role** or use **Choose an IAM role** to specify an IAM
   role that grants AWS Backup permission to restore the backup.
6. In the **Protected resource tags** pane, we select **Copy
   tags from the protected resource to the restored resource** by default. If
   you do not want to copy these tags, clear the check box.
7. In the **Advanced settings** pane, accept the default values for
   the instance settings or change them as needed. For information about these settings,
   choose **Info** for the setting to open its help pane.
8. When you are finishing configuring the instance, choose **Restore
   backup**.

## Restore Amazon EC2 with AWS CLI

In the command line interface, [`start-restore-job`](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/start-restore-job.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/start-restore-job.html") allows you to restore with up to 32 parameters
(including some parameters that are not customizable through the AWS Backup console).

The following list is the accepted metadata you can pass to restore an Amazon EC2 recovery
point.

```
InstanceType
KeyName
SubnetId
Architecture
EnaSupport
SecurityGroupIds
IamInstanceProfileName
CpuOptions
InstanceInitiatedShutdownBehavior
HibernationOptions
DisableApiTermination
CreditSpecification
Placement
RootDeviceType
RamdiskId
KernelId
UserData
Monitoring
NetworkInterfaces
ElasticGpuSpecification
CapacityReservationSpecification
InstanceMarketOptions
LicenseSpecifications
EbsOptimized
VirtualizationType
Platform
RequireIMDSv2
BlockDeviceMappings
aws:backup:request-id
```

AWS Backup accepts the following information-only attributes. However, including them will
not affect the restore:

```
vpcId
```

[`BlockDeviceMappings`](../../../AWSEC2/latest/UserGuide/ami-block-device-mapping.md#create-ami-bdm "../../../AWSEC2/latest/UserGuide/ami-block-device-mapping.md#create-ami-bdm") is an optional parameter you can include. AWS Backup supports the following
`BlockDeviceMappings` attributes.

###### Note

`SnapshotId` and `OutpostArn` are not supported.

```
{
  "BlockDeviceMappings": [
    {
        "DeviceName" : string,
        "NoDevice" : string,
        "VirtualName" : string,
        "Ebs": {
            "DeleteOnTermination": boolean,
            "Iops": number,
            "VolumeSize": number,
            "VolumeType": string,
            "Throughput": number,
            "Encrypted": boolean,
            "KmsKeyId": string
        }
    }
 }
```

For example:

```
{
  "BlockDeviceMappings": [
    {
      "DeviceName": "/def/tuvw",
      "Ebs": {
        "DeleteOnTermination": true,
        "Iops": 3000,
        "VolumeSize": 16,
        "VolumeType": "gp3",
        "Throughput": 125,
        "Encrypted": true,
        "KmsKeyId": "arn:aws:kms:us-west-2:123456789012:key/ab3cde45-67f8-9g01-hi2j-3456klmno7p8"
      }
    },
    {
      "DeviceName": "/abc/xyz",
      "Ebs": {
        "DeleteOnTermination": false,
        "Iops": 3000,
        "VolumeSize": 16,
        "VolumeType": "gp3",
        "Throughput": 125,
        "Encrypted": false
      }
    }
  ]
}
```

You can also restore an Amazon EC2 instance without including any stored parameters. This
option is available on the **Protected resource** tab on the AWS Backup console.

###### Important

If you do not override the AWS KMS key in the `BlockDeviceMappings` when
restoring from cross-account or cross-Region backups, your restore might fail. For
more information, see [Troubleshoot Amazon EC2 instance restore issues](#restoring-ec2-troubleshooting "#restoring-ec2-troubleshooting").

## Troubleshoot Amazon EC2 instance restore issues

###### Troubleshooting issues

- [Cross-account restore failures](#cross-account-kms-issue "#cross-account-kms-issue")
- [Cross-Region restore failures](#cross-region-kms-issue "#cross-region-kms-issue")

### Cross-account restore failures

**Description:** Amazon EC2 instance restore fails when
attempting to restore from a backup that is shared with your account.

**Possible issues:** Your account might not have access
to the AWS KMS keys used to encrypt the source volumes in the sharing account. The KMS keys
might not be shared with your account.

Or, the volumes attached to the source instance are unencrypted.

**Solution:** To resolve this issue, set the
`encrypted` attribute to `true`, and do one of the following:

- Override the KMS keys in the `BlockDeviceMappings` and specify a KMS key
  that you own in your account.
- Request the owning account to grant you access to the KMS keys used to encrypt the
  volumes by updating the KMS key policy. For more information, see [Allow users
  in other accounts to use a KMS key](../../../kms/latest/developerguide/key-policy-modifying-external-accounts.md "../../../kms/latest/developerguide/key-policy-modifying-external-accounts.md").

### Cross-Region restore failures

**Description:** Amazon EC2 instance restore fails when
attempting to restore from a cross-Region backup.

**Issue:** The volumes in the backup might be encrypted
with single-Region AWS KMS keys that are not available in the destination Region. Or, the
volumes attached to the source instance are unencrypted.

**Solution:** To resolve this issue, set the
`encrypted` attribute to `true`, and override the KMS key
in the `BlockDeviceMappings` with a KMS key in the destination Region.
