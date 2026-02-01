# Restore a virtual machine using AWS Backup

You can restore a virtual machine to VMware, VMware Cloud on AWS, VMware Cloud on
AWS Outposts, an Amazon EBS volume, or [to an Amazon EC2 instance](restoring-ec2.md "restoring-ec2.md").
Restoring (or migrating) a virtual machine to EC2 requires a license. By default, AWS will
include a license (charges apply). For more information, see [Licensing options](../../../vm-import/latest/userguide/licensing.md "../../../vm-import/latest/userguide/licensing.md") in the
_VM Import/Export User Guide_.

You can restore a VMware virtual machine using the AWS Backup console or through the AWS CLI.
When a virtual machine is restored, the VMware Tools folder is not included. See VMware
documentation to reinstall VMware Tools.

AWS Backup restores of virtual machines are non-destructive, meaning AWS Backup does not overwrite
existing virtual machines during a restore. Instead, the restore job deploys a new virtual
machine.

###### Tasks

- [Considerations when restoring a VM to an Amazon EC2
  instance](#vm-restore-ec2 "#vm-restore-ec2")
- [Use the AWS Backup console to restore virtual machine
  recovery points](#vm-restore-console "#vm-restore-console")
- [Use AWS CLI to restore virtual machine recovery
  points](#vm-restore-cli "#vm-restore-cli")

## Considerations when restoring a VM to an Amazon EC2

instance

- Restoring (or migrating) a virtual machine to EC2 requires a license. By default,
  an AWS will include a license (charges apply). For more information, see [Licensing
  options](../../../vm-import/latest/userguide/licensing.md "../../../vm-import/latest/userguide/licensing.md") in the _VM Import/Export User Guide_.
- There is a maximum limit of 5 TB (terabytes) for each virtual machine disk.
- You can't specify a key pair when you restore the virtual machine to an instance.
  You can add a key pair to `authorized_keys` during launch (through instance
  user data) or after launch (as described in [this troubleshooting section](../../../AWSEC2/latest/UserGuide/TroubleshootingInstancesConnecting.md#replacing-lost-key-pair "../../../AWSEC2/latest/UserGuide/TroubleshootingInstancesConnecting.md#replacing-lost-key-pair") in the Amazon EC2 User Guide).
- Confirm your [operating system is supported](../../../vm-import/latest/userguide/prerequisites.md#vmimport-operating-systems "../../../vm-import/latest/userguide/prerequisites.md#vmimport-operating-systems") for import to and export from Amazon EC2 in the
  _VM Import/Export User Guide_.
- Review limitations involved with [Importing VMs
  to Amazon EC2](../../../vm-import/latest/userguide/prerequisites.md#limitations-image "../../../vm-import/latest/userguide/prerequisites.md#limitations-image") in the _VM Import/Export User Guide_.
- When you restore to an Amazon EC2 instance using AWS CLI, you must specify
  `"RestoreTo":"EC2Instance"`. All other attributes have default
  values.
- Amazon EC2 offers [EC2 Allowed AMIs](../../../AWSEC2/latest/UserGuide/ec2-allowed-amis.md "../../../AWSEC2/latest/UserGuide/ec2-allowed-amis.md"). If
  this setting is enabled in your account, add the alias `aws-backup-vault`
  to your allowlist. Otherwise, restore operations of VM recovery points to EC2
  instances will fail with an error message, such as "Source AMI not found in
  Region".
- For VMware restores involving more than 21 disks, you must limit the initial
  VMware restore to no more than 21 disks, then use [VMware Restores to EBS](restoring-vm.md#restore-vm-ebs "restoring-vm.md#restore-vm-ebs") for
  the remaining disks, and after all restore operations complete, attach the
  EBS volumes to the restored instance.

## Use the AWS Backup console to restore virtual machine

recovery points

You can restore a virtual machine from multiple locations in the left navigation pane
of the AWS Backup console:

- Choose **Hypervisors** to view recovery points for virtual
  machines managed by a hypervisor that is connected to AWS Backup.
- Choose **Virtual machines** to view recovery points for virtual
  machines across all your hypervisors that are connected to AWS Backup.
- Choose **Backup vaults** to view recovery points stored in a
  specific AWS Backup vault.
- Choose **Protected resources** to view recovery points across all
  your AWS Backup protected resources.

If you need to restore a virtual machine that no longer has a connection with Backup
gateway, choose **Backup vaults** or **Protected
resources** to locate your recovery point.

###### Options

- [Restore to VMware](#restore-vm-vmware "#restore-vm-vmware")
- [Restore to an Amazon EBS volume](#restore-vm-ebs "#restore-vm-ebs")
- [Restore to an Amazon EC2 instance](#restore-vm-ec2 "#restore-vm-ec2")

###### To restore a virtual machine to VMware, VMware Cloud on AWS, and VMware Cloud on

AWS Outposts

1. In the **Hypervisors** or **Virtual machines**
   views, choose the **VM name** to restore. In the **Protected
   resources** view, choose the virtual machine **Resource
   ID** to restore.
2. Choose the radial button next to the **Recovery point ID** to
   restore.
3. Choose **Restore**.
4. Choose the **Restore type**.
   1. **Full restore** restores all the virtual machine's
      disks.
   2. **Disk-level restore** restores a user-defined selection of
      one or more disks. Use the drop-down menu to select which disks to restore.

5. Choose the **Restore location**. The options are
   **VMware**, **VMware Cloud on AWS**, and
   **VMware Cloud on AWS Outposts**.
6. If you are doing a full restore, skip to the next step. If you are performing a
   disk-level restore, there will be a drop-down menu under **VM
   disks**. Choose one or more bootable volumes to restore.
7. Select a **Hypervisor** from the dropdown menu to manage the
   restored virtual machine
8. For the restored virtual machine, use your organization’s virtual machine best
   practices to specify its:
   1. **Name**
   2. **Path** (such as `/datacenter/vm`)
   3. **Compute resource name** (such as VMHost or Cluster)

   If a host is part of a cluster then you cannot restore to the host but only to
   the given cluster. 4. **Datastore**

9. For **Restore role,** select either the **Default
   role** (recommended) or **Choose an IAM role** using the
   dropdown menu.
10. Choose **Restore backup**.
11. _Optional_: Check when your restore job has the status
    `Completed`. In the left navigation menu, choose
    **Jobs**.

###### To restore a virtual machine to an Amazon EBS volume

1. In the **Hypervisors** or **Virtual machines**
   views, choose the **VM name** to restore. In the **Protected
   resources** view, choose the virtual machine **Resource
   ID** to restore.
2. Choose the radial button next to the **Recovery point ID** to
   restore.
3. Choose **Restore**.
4. Choose the **Restore type**.
   1. **Disk restore** restores a user-defined selection of one
      disk. Use the drop-down menu to select which disk to restore.

5. Choose the **Restore location** as
   **Amazon EBS**.
6. Under the **VM disk** dropdown menu, choose bootable volume to
   restore.
7. Under **EBS Volume type**, choose the volume type.
8. Choose your Availability Zone.
9. Encryption (optional). Check the box if you choose to encrypt the EBS
   volume.
10. Select your KMS key from the menu.
11. For **Restore role,** select either the **Default
    role** (recommended) or **Choose an IAM role**.
12. Choose **Restore backup**.
13. _Optional_: Check when your restore job has the status
    `Completed`. In the left navigation menu, choose
    **Jobs**.
14. _Optional_: Visit [How do I use LVM to
    create a logical volume on an Amazon EBS volume's partition?](https://repost.aws/knowledge-center/create-lv-on-ebs-partition "https://repost.aws/knowledge-center/create-lv-on-ebs-partition") to learn more on how
    to mount managed volumes and access data on the restored Amazon EBS volume.

###### To restore a virtual machine to an Amazon EC2 instance

1. In the **Hypervisors** or **Virtual machines**
   views, choose the **VM name** to restore. In the **Protected
   resources** view, choose the virtual machine **Resource
   ID** to restore.
2. Choose the radial button next to the **Recovery point ID** to
   restore.
3. Choose **Restore**.
4. Choose the **Restore type**.
   1. **Full restore** restores the file system completely,
      including the root-level folder and files.

5. Choose the **Restore location** as
   **Amazon EC2**.
6. For **Instance type**, choose the combination of compute and
   memory required to run your application on your new instance.

###### Tip

Choose an instance type that matches or exceeds the specifications of the
original virtual machine. For more information, see the [Amazon EC2 Instance Types Guide](../../../ec2/latest/instancetypes.md "../../../ec2/latest/instancetypes.md"). 7. For **Virtual Private Cloud (VPC)**, choose a virtual private
cloud (VPC), which defines the networking environment for the instance. 8. For **Subnet**, choose one of the subnets in the VPC. Your
instance receives a private IP address from the subnet address range. 9. For **security groups**, choose a security group, which acts as a
firewall for traffic to your instance. 10. For **Restore role,** select either the **Default
role** (recommended) or **Choose an IAM role**. 11. _Optional_: To run a script on your instance at launch, expand
**Advanced settings** and enter the script in **User
data**. 12. Choose **Restore backup**. 13. _Optional_: Check when your restore job has the status
`Completed`. In the left navigation menu, choose
**Jobs**.

## Use AWS CLI to restore virtual machine recovery

points

Use `StartRestoreJob`.

You can specify the following metadata for a virtual machine restore to Amazon EC2 and
Amazon EBS:

```
RestoreTo
InstanceType
VpcId
SubnetId
SecurityGroupIds
IamInstanceProfileName
InstanceInitiatedShutdownBehavior
HibernationOptions
DisableApiTermination
Placement
CreditSpecification
RamdiskId
KernelId
UserData
EbsOptimized
LicenseSpecifications
KmsKeyId
AvailabilityZone
EbsVolumeType
IsEncrypted
ItemsToRestore
RequireIMDSv2
NetworkInterfaces
```

You can specify the following metadata for a virtual machine restore to VMware, VMware
Cloud on AWS, and VMware cloud on AWS Outpost:

```
RestoreTo
HypervisorArn
VMName
VMPath
ComputeResourceName
VMDatastore
DisksToRestore
ItemsToRestore
```

This example shows how to conduct a full restore to VMware:

```
'{"RestoreTo":"VMware","HypervisorArn":"arn:aws:backup-gateway:us-east-1:209870788375:hypervisor/hype-9B1AB1F1","VMName":"name","VMPath":"/Labster/vm","ComputeResourceName":"Cluster","VMDatastore":"vsanDatastore","DisksToRestore":"[{\"DiskId\":\"2000\",\"Label\":\"Hard disk 1\"}]","vmId":"vm-101"}'
```
