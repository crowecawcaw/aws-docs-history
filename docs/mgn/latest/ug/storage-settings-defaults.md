

# Storage settings defaults

The **Storage settings defaults** section of the **Launch settings** tab defines the default Amazon EBS settings that MGN stores for the source server. MGN uses these defaults when it builds a volume entry in the server's EC2 launch template itself:
+ When MGN creates the server's EC2 launch template.
+ When a new disk appears on the source server.
+ When a disk on the source server grows.

All volume entries that MGN builds for the server use the same defaults. The storage settings defaults are stored in MGN and don't change the EC2 launch template directly.

The storage settings defaults include:
+ **EBS volume type** – The Amazon EBS volume type, for example gp2, gp3, io1, io2, st1, or sc1.
+ **IOPS** – The provisioned IOPS for the volumes. The allowed range depends on the volume type.
+ **Throughput** – The provisioned throughput, in MiB/s. Applies to gp3 volumes only.
+ **Volume initialization rate** – The rate, in MiB/s, at which snapshot data is downloaded to the volume. Specifying an initialization rate ensures that volumes are fully initialized in a predictable amount of time. Additional costs apply. For more information, see [Amazon EBS volume initialization rate](https://docs.aws.amazon.com/ebs/latest/userguide/initalize-volume.html#volume-initialization-rate) in the *Amazon EBS User Guide*.
+ **Delete on termination** – Whether the volumes are automatically deleted when the instance is terminated. If you disable this setting, the volumes remain provisioned in your account after the instance is terminated, and you must delete them manually if you no longer need them. For more information, see [How instance termination affects root and data volumes](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/preserving-volumes-on-termination.html#how-instance-termination-affects-root-and-data-volumes) in the *Amazon EC2 User Guide*.

For the limits that apply to each volume type, including IOPS and throughput, see [Amazon EBS volume types](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-volume-types.html) in the *Amazon EBS User Guide*.

**Note**  
MGN sets the volume size automatically for each volume, based on the size of the corresponding disk on the source server. You can't set the volume size in the storage settings defaults.

When MGN adds a source server, it copies the Amazon EBS settings of the [account launch template](launch-template.md#default-ec2-launch-template) into the server's storage settings defaults. Later changes to the account launch template don't affect them. If you disconnect the source server, MGN copies the account launch template's settings again, replacing the storage settings defaults that you set for the server.

If a setting has no value, MGN uses its own default when it creates a volume:
+ No Amazon EBS volume type: gp3, with 3,000 IOPS and 125 MiB/s throughput.
+ An Amazon EBS volume type without IOPS or throughput: the highest IOPS and throughput that the volume type and size allow.
+ No volume initialization rate or delete on termination: MGN doesn't set it, and the Amazon EC2 default applies.

If the volume type doesn't support a volume's size (for example, st1 and sc1 volumes must be at least 125 GiB), MGN uses gp3 with 3,000 IOPS and 125 MiB/s for that volume.

You can edit the storage settings defaults in any of these ways:
+ In the MGN console, on the **Launch settings** tab of the source server.
+ Through the MGN API, with the `UpdateLaunchConfigurationDefaults` operation. `GetLaunchConfigurationDefaults` returns the current values.
+ By [exporting](export-main.md) your inventory, editing the `mgn:launch:default:ebs:*` fields, and [importing](import-main.md) it again. This lets you change the defaults for many source servers at once.

**Important**  
Changes to the storage settings defaults apply only to volume entries that MGN builds after the change. They don't update volumes that already exist in the server's EC2 launch template. To change an existing volume, edit the [EC2 launch template](ec2-launch.md) directly. The exception is a source disk that grows. MGN then updates the size of its volume and applies the current storage settings defaults to it, replacing the volume type, IOPS, throughput, volume initialization rate and delete on termination set for that volume in the EC2 launch template.

Encryption settings for the volumes aren't part of the storage settings defaults. You set the encryption type and KMS key in the server's [replication settings](replication-settings.md).

**Note**  
Viewing and editing the storage settings defaults requires the `mgn:GetLaunchConfigurationDefaults` and `mgn:UpdateLaunchConfigurationDefaults` actions. These actions are separate from `mgn:GetLaunchConfiguration` and `mgn:UpdateLaunchConfiguration`, so a policy that denies `mgn:UpdateLaunchConfiguration` doesn't deny `mgn:UpdateLaunchConfigurationDefaults`. To prevent changes to the storage settings defaults, deny `mgn:UpdateLaunchConfigurationDefaults` as well. The [AWSApplicationMigrationFullAccess](security-iam-awsmanpol-AWSApplicationMigrationFullAccess.md) managed policy includes both actions. If you use your own policies or roles that allow MGN actions individually, such as an `AWSApplicationMigrationSharingRole_<MANAGEMENT_ACCOUNT_ID>` role that you created manually for global view, add both actions to them.