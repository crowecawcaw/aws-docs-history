

# Configure FSx for OpenZFS as principal storage for diskless hosts

This page applies to Self-deployed environments that run VCF 9.x on diskless hosts. For how EVS-deployed environments (VCF 5.2.x) differ, see [Differences between deployment modes](deployment-mode-differences.md).

Diskless hosts need external storage for the VMware Cloud Foundation (VCF) management domain. You size and create an Amazon FSx for OpenZFS file system and two Network File System (NFS) volumes, and you set the security group rules that they need. You can grow the capacity later. You mount the volumes on the first host and reference the principal volume in the VCF Installer specification, as described in [Step 4a (diskless): Prepare diskless hosts and the VCF Installer](getting-started-diskless.md) and [Step 4b (diskless): Create the specification and deploy](deploy-diskless-spec.md). For an overview of the storage options, see [External storage options for diskless hosts](external-storage-diskless.md).

## Before you begin
<a name="fsx-openzfs-prereqs"></a>

Make sure that you meet the following prerequisites.
+ You created an Amazon Elastic VMware Service environment in Self-deployed mode in your VPC. For more information, see [Step 1: Create the environment](self-deployed-create-env.md).
+ You know the CIDR block of the host management (`vmkManagement`) VLAN subnet. You use it in the NFS export list and in the security group.
+ You know the ID of the service access subnet that Amazon EVS uses.
+ You or your storage administrator have permissions to create and manage FSx for OpenZFS file systems in your VPC. For more information, see [Identity and access management for Amazon FSx for OpenZFS](https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/security-iam.html) in the *Amazon FSx for OpenZFS User Guide*.

## Size the file system
<a name="fsx-openzfs-sizing"></a>

The VCF Installer checks the capacity of the principal datastore during validation. The datastore size that the ESX host reports depends on the file system and on the volume quota. A volume with no quota appears on the ESX host with the capacity of the file system. Provision enough capacity for the Installer requirement plus the amount that the Installer advises to stay under 80 percent utilization.

For the two-host management domain specification in [Step 4b (diskless): Create the specification and deploy](deploy-diskless-spec.md), the VCF Installer reported the following values.


| Installer check | Value | 
| --- | --- | 
| Required capacity for the management domain | 5,398 GB | 
| Recommended capacity to stay under 80 percent utilization | 6,748 GB | 

The VCF Installer reports capacity in GB. Amazon FSx capacity and the recommendation that follows are in GiB.

For a new deployment of this size, we recommend that you provision at least 7,168 GiB. A file system with 7,168 GiB of SSD storage capacity and no volume quota appears on the ESX host as a 7,168 GiB datastore. At this size, both Installer capacity checks pass and the Installer shows no capacity advisory. If you set a volume quota, keep it above 6,748 GB.

After the two-host management domain is deployed, the principal datastore holds about 284 GiB. The datastores are thin provisioned, so the file system leaves a large amount of free space for workloads. Because both volumes share the file system, the second volume can show a slightly smaller size than the principal volume. Use the size of the principal datastore for capacity planning.

**Important**  
You can increase the SSD storage capacity of a file system later, but you can’t decrease it. Plan the capacity before you deploy VCF. For more information, see [Increase the capacity](#fsx-openzfs-grow).

For prices, see the [Amazon FSx for OpenZFS pricing page](https://aws.amazon.com/fsx/openzfs/pricing).

## Create the file system
<a name="fsx-openzfs-create-fs"></a>

Create a file system in the service access subnet of your environment. You can use the Amazon FSx console or the AWS CLI.

Before you create the file system, create a security group in your VPC with the rules in [Security group rules](#fsx-openzfs-security-group).

Create the file system with the option to copy tags to volumes turned off. If this option is on and the file system has a `Name` tag, creating a volume with a `Name` tag that has a different value fails with a `BadRequest` error.

To create the file system in the Amazon FSx console or with the AWS CLI, use the following steps.

**Example**  

1. Open the [Amazon FSx console](https://console.aws.amazon.com/fsx).

1. Choose **Create file system**, and then choose **Amazon FSx for OpenZFS**.

1. For **Deployment type**, choose **Single-AZ (HA)**, and then choose **Single-AZ 2**.

1. For **Storage class**, choose **SSD (provisioned)**, and for **SSD storage capacity**, enter the capacity from [Size the file system](#fsx-openzfs-sizing).

1. For **Throughput capacity**, choose 640 MBps.

1. For **VPC**, choose the VPC of your environment, and for **Subnet**, choose the Amazon EVS service access subnet.

1. For **Security group**, choose a security group that allows inbound NFS traffic from the host management VLAN subnet. For the rules, see [Security group rules](#fsx-openzfs-security-group).

1. Turn off the option to copy tags to volumes.

1. Under **Root volume configuration**, set the data compression type to **LZ4**.

1. For the NFS exports of the root volume, specify the host management VLAN subnet CIDR block as the client, and set the options to `rw,crossmnt,no_root_squash`.

1. Review the settings, and choose **Create file system**.

1. Run the `aws fsx create-file-system` command. The following example creates a Single-AZ (HA) generation 2 file system. For `--subnet-ids`, specify the Amazon EVS service access subnet. For `Clients`, specify the CIDR block of the host management VLAN subnet. Replace the values in angle brackets with your own values. Replace the example CIDR block with your own value. Replace `<region-code>` with the Region where you created the environment.

   ```bash
   aws fsx create-file-system \
       --file-system-type OPENZFS \
       --storage-capacity 7168 \
       --storage-type SSD \
       --subnet-ids <subnet-id> \
       --security-group-ids <security-group-id> \
       --open-zfs-configuration '{
           "DeploymentType": "SINGLE_AZ_HA_2",
           "ThroughputCapacity": 640,
           "AutomaticBackupRetentionDays": 0,
           "CopyTagsToVolumes": false,
           "RootVolumeConfiguration": {
               "RecordSizeKiB": 128,
               "DataCompressionType": "LZ4",
               "NfsExports": [{
                   "ClientConfigurations": [{
                       "Clients": "10.10.0.0/24",
                       "Options": ["rw", "crossmnt", "no_root_squash"]
                   }]
               }]
           }
       }' \
       --region <region-code>
   ```

Keep the `no_root_squash` option, because ESX mounts NFS datastores as the root user. The example turns off automatic backups. Choose the backup and maintenance settings that match your requirements. For more information, see [Creating FSx for OpenZFS file systems](https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/creating-file-systems.html) in the *Amazon FSx for OpenZFS User Guide*.

A Single-AZ (HA) generation 2 file system with 7,168 GiB of SSD storage and 640 MBps of throughput becomes available in 10 to 25 minutes. Wait until the file system is available before you create the volumes. The endpoint IP address appears when the file system is available.

If you created the file system with the option to copy tags to volumes turned on, turn it off with the following command. The change causes no interruption. Replace `<file-system-id>` with the ID of your file system, and replace `<region-code>` with the Region where you created the environment.

```bash
aws fsx update-file-system \
    --file-system-id <file-system-id> \
    --open-zfs-configuration CopyTagsToVolumes=false \
    --region <region-code>
```

**Note**  
An Amazon EVS environment runs in one Availability Zone. For more information, see [VPC and subnets](plan-network-supported.md#plan-network-supported-vpc). A Multi-AZ file system keeps the storage available if an Availability Zone fails, but it doesn’t keep your Amazon EVS environment running. Choose the deployment type for your availability and cost requirements. For more information, see [Availability and durability](https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/availability-durability.html) in the *Amazon FSx for OpenZFS User Guide*.

### Security group rules
<a name="fsx-openzfs-security-group"></a>

The FSx for OpenZFS file system doesn’t start outbound connections. The NFS datastores mount through the host management VMkernel adapter, so allow the following inbound traffic from the CIDR block of the host management VLAN subnet.


| Purpose | Protocol | Ports | 
| --- | --- | --- | 
| NFS and related services | TCP and UDP | 111, 2049, and 20001 to 20003 | 
| Connectivity checks | Internet Control Message Protocol (ICMP) | All | 

For more information, see [File System Access Control with Amazon VPC](https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/limit-access-security-groups.html) in the *Amazon FSx for OpenZFS User Guide*.

## Create the volumes
<a name="fsx-openzfs-create-volumes"></a>

Create two child volumes of the root volume.

 `vcf-principal`   
The principal datastore for the VCF management domain. The VCF Installer deploys the management appliances onto this volume.

 `installer-staging`   
The temporary datastore for the VCF Installer appliance. You mount it on the first host before you deploy the VCF Installer. During deployment, the VCF Installer moves its appliance to the principal datastore.

Create each volume with the following settings.

 **Parent volume**   
Use the root volume of the file system.

 **NFS exports**   
Use the host management VLAN subnet CIDR block with the options `rw,crossmnt,no_root_squash`.

 **Storage capacity quota**   
Use none (`-1`). The volume is then limited by the quota of the root volume, which equals the file system capacity. The describe output of a volume without a quota shows no quota value. A smaller quota limits the datastore size that ESX reports, so keep any quota above 6,748 GB.

 **Record size**   
The examples on this page use 16 KiB for `vcf-principal` and 128 KiB for `installer-staging`.

 **Tags**   
If you add a `Name` tag, make sure that the option to copy tags to volumes is turned off on the file system.

To create the volumes in the Amazon FSx console or with the AWS CLI, use the following steps.

**Example**  

1. Open the [Amazon FSx console](https://console.aws.amazon.com/fsx).

1. In the navigation pane, choose **File systems**, and then choose your file system.

1. Choose the **Volumes** tab, and then choose **Create volume**.

1. For **Volume name**, enter `vcf-principal`.

1. For **Parent volume**, choose the root volume.

1. Apply the settings in the previous list, and choose **Confirm**.

1. Repeat these steps for `installer-staging`.

1. Get the ID of the root volume. Replace `<file-system-id>` with the ID of your file system, and replace `<region-code>` with the Region where you created the environment.

   ```bash
   aws fsx describe-file-systems \
       --file-system-ids <file-system-id> \
       --query 'FileSystems[0].OpenZFSConfiguration.RootVolumeId' \
       --output text \
       --region <region-code>
   ```

1. Create the principal volume. Replace `<root-volume-id>` with the ID of the root volume from the previous step. Replace the example CIDR block with the CIDR block of your host management VLAN subnet.

   ```bash
   aws fsx create-volume \
       --volume-type OPENZFS \
       --name vcf-principal \
       --open-zfs-configuration '{
           "ParentVolumeId": "<root-volume-id>",
           "StorageCapacityQuotaGiB": -1,
           "RecordSizeKiB": 16,
           "DataCompressionType": "LZ4",
           "NfsExports": [{
               "ClientConfigurations": [{
                   "Clients": "10.10.0.0/24",
                   "Options": ["rw", "crossmnt", "no_root_squash"]
               }]
           }]
       }' \
       --region <region-code>
   ```

1. Repeat the command with `--name installer-staging` and `"RecordSizeKiB": 128`.

You have created the two volumes.

## Get the endpoint IP address
<a name="fsx-openzfs-endpoint"></a>

You use the endpoint IP address of the file system as the NFS server when you mount the volumes on the host and in the VCF Installer specification. To get the endpoint IP address in the Amazon FSx console or with the AWS CLI, use the following steps.

**Example**  

1. Open the [Amazon FSx console](https://console.aws.amazon.com/fsx).

1. In the navigation pane, choose **File systems**, and then choose your file system.

1. Choose the **Network & security** tab.

1. Copy the **Endpoint IP address**.

1. Run the following command. Replace `<file-system-id>` with the ID of your file system, and replace `<region-code>` with the Region where you created the environment.

   ```bash
   aws fsx describe-file-systems \
       --file-system-ids <file-system-id> \
       --query 'FileSystems[0].OpenZFSConfiguration.EndpointIpAddress' \
       --output text \
       --region <region-code>
   ```

The NFS export path of a volume is `/fsx/<volume-name>`. For example, the path of the principal volume is `/fsx/vcf-principal`.

## Increase the capacity
<a name="fsx-openzfs-grow"></a>

If you need more capacity before you deploy VCF, complete the following steps in order. After you deploy VCF, the principal datastore holds your management appliances, and you can’t unmount a datastore while virtual machines use it.

1. Increase the SSD storage capacity of the file system. Each increase must be at least 10 percent of the current capacity. After a change, you must wait six hours before you can change the capacity again. Replace `<file-system-id>` with the ID of your file system, and replace the example capacity with your own value. Replace `<region-code>` with the Region where you created the environment.

   ```bash
   aws fsx update-file-system \
       --file-system-id <file-system-id> \
       --storage-capacity 9216 \
       --region <region-code>
   ```

1. If you set a storage capacity quota on the volume, raise the quota. Each volume has its own quota, and a volume doesn’t use the new capacity until you raise it. Replace `<volume-id>` with the ID of the volume.

   ```bash
   aws fsx update-volume \
       --volume-id <volume-id> \
       --open-zfs-configuration StorageCapacityQuotaGiB=9216 \
       --region <region-code>
   ```

1. Unmount the NFS datastore from the host and mount it again, so that ESX reads the new size. A storage rescan doesn’t update the reported size.

To delete the file system when you no longer need it, see [Clean up a Self-deployed environment](self-deployed-cleanup.md).

Next step: Mount the volumes on the first host, as described in [Prepare the first host](getting-started-diskless.md#getting-started-diskless-prep-host).