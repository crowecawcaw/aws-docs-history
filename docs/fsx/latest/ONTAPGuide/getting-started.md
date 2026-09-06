

# Getting started with Amazon FSx for NetApp ONTAP
<a name="getting-started"></a>

Learn how to get started using Amazon FSx for NetApp ONTAP. This getting started exercise includes the following steps.

1. Sign up for an AWS account and create an administrative user in the account.

1. Create an Amazon FSx for NetApp ONTAP file system using the Amazon FSx console.

1. Mount your file system from an Amazon EC2 Linux instance.

1. Clean up the resources you created.

**Topics**
+ [Setting up FSx for ONTAP](#setting-up)
+ [Create an Amazon FSx for NetApp ONTAP file system](#getting-started-step1)
+ [Mounting your file system from an Amazon EC2 Linux instance](#getting-started-step2)
+ [Cleaning up resources](#getting-started-step3)

## Setting up FSx for ONTAP
<a name="setting-up"></a>

Before you use Amazon FSx for the first time, complete the following tasks.

**Topics**
+ [Sign up for an AWS account](#sign-up-for-aws)
+ [Next step](#setting-up-next-step)

### Sign up for an AWS account
<a name="sign-up-for-aws"></a>

To get started with AWS, you need an AWS account. For information about creating an AWS account, see [Getting started with an AWS account](https://docs.aws.amazon.com/accounts/latest/reference/getting-started.html) in the *AWS Account Management Reference Guide*.

### Next step
<a name="setting-up-next-step"></a>

To get started using FSx for ONTAP see [Getting started with Amazon FSx for NetApp ONTAP](#getting-started) for instructions to create your Amazon FSx resources.

## Create an Amazon FSx for NetApp ONTAP file system
<a name="getting-started-step1"></a>

The Amazon FSx console has two options for creating a file system – a **Quick create** option and a **Standard create** option. To rapidly and easily create an Amazon FSx for NetApp ONTAP file system with the service recommended configuration, use the **Quick create** option.

The **Quick create** option configures this file system to allow data access from Linux instances over the Network File System (NFS) protocol. After your file system is created, you can create additional SVMs and volumes as needed, including an SVM joined to an Active Directory to allow access from Windows and macOS clients over the Server Message Block (SMB) protocol. You can also add additional high-availability (HA) pairs depending on the deployment type that you choose and how many HA pairs you add at creation.

**Note**  
FSx for ONTAP file systems created with the **Quick create** option use a **Network type** of `IPv4`. To create a file system with a **Network type** of `Dual-stack` (which supports both IPv4 and IPv6), use the **Standard create** option.

For information about using the **Standard create** option to create a file system with a customized configuration, and for using the AWS CLI and API, see [Creating file systems](creating-file-systems.md).

**To create your file system**

1. Open the Amazon FSx console at [https://console.aws.amazon.com/fsx/](https://console.aws.amazon.com/fsx/).

1. On the dashboard, choose **Create file system** to start the file system creation wizard.

1. On the **Select file system type** page, choose **Amazon FSx for NetApp ONTAP**, and then choose **Next**. The **Create ONTAP file system** page appears.

1. For **Creation method**, choose **Quick create**.

1. In the **Quick configuration** section, for **File system name - optional**, enter a name for your file system. It's easier to find and manage your file systems when you name them. You can use a maximum of 256 Unicode letters, white space, and numbers, plus these special characters: **\+** **-** (hyphen) **=** **.** **\_** (underscore) **:** **/**

1. For **Deployment type** choose **Multi-AZ** or **Single-AZ**.
   +  **Multi-AZ** file systems replicate your data and support failover across multiple Availability Zones in the same AWS Region. 
   + **Single-AZ** file systems replicate your data and offer automatic failover within a single Availability Zone.

    For more information, see [Availability, durability, and deployment options](high-availability-AZ.md).
**Note**  
The latest generation FSx for ONTAP file system that is available for your AWS Region is chosen by default. You can specify the generation of your file system (in available AWS Regions) with the **Standard create** option. For more information, see [Creating file systems](creating-file-systems.md).

1. For **SSD storage capacity**, specify the storage capacity of your file system, in gibibytes (GiB). Enter any whole number in the range of 1,024–1,048,576. For more information, see [To create a file system (console)](creating-file-systems.md#create-MAZ-file-system-console). 

   You can increase the amount of storage capacity as needed at any time after you create the file system. For more information, see [Managing storage capacity](managing-storage-capacity.md).

1. For **Throughput capacity**, Amazon FSx automatically provides a recommended throughput capacity based on your SSD storage. You can also choose your file system's throughput (up to 73,728 MBps depending on the deployment type and amount of HA pairs). 

1. For **Virtual Private Cloud (VPC)**, choose the Amazon VPC that you want to associate with your file system.

1. (Multi-AZ only) **Endpoint IP address range** specifies the IP address range in which the endpoints to access your file system are created.

   Choose a **Quick create** option for the endpoint IP address range:
   + **Unallocated IPv4 address range from your VPC** – Choose this option to have Amazon FSx use the last 64 IP addresses from the VPC’s primary CIDR range as the endpoint IPv4 address range for the file system. Note that this range is shared across multiple file systems if you choose this option multiple times.
**Note**  
Each file system that you create consumes two IP addresses from this range—one for the cluster, and one for the first SVM. The first and last IP addresses are also reserved. For every additional SVM, the file system consumes another IP address. For example, a file system that hosts 10 SVMs uses 11 IP addresses. Additional file systems work in the same way. They consume the two initial IP addresses, plus one for each additional SVM. The maximum number of file systems using the same IP address range, each with a single SVM, is 31.
This option is grayed out if any of the last 64 IP addresses in a VPC's primary CIDR range are in use by a subnet.
   + **Floating IPv4 address range outside your VPC** – Choose this option to have Amazon FSx use a 198.19.x.0/24 address range that isn't already used by any other file systems with the same VPC and route tables.

   You can also specify your own IP address range in the **Standard create** option. The IP address range that you choose can either be inside or outside the VPC’s IPv4 address range, as long as it doesn't overlap with any subnet, and as long as it isn't already used by another file system with the same VPC and route tables. We recommend using a range that is inside the VPC's IP address range.
**Note**  
Ensure that all of the route tables you're using are associated with your Multi-AZ file system. Doing so helps prevent unavailability during a failover. For information about associating your Amazon VPC route tables with your file system, see [Updating file systems](updating-file-system.md).

1. For **Storage efficiency**, choose **Enabled** to turn on the ONTAP storage efficiency features (compression, deduplication, and compaction) or **Disabled** to turn them off.

1. Choose **Next**, and review the file system configuration on the **Create ONTAP file system** page. Note which file system settings you can modify after the file system is created.

1. Choose **Create file system**.

**Quick create** creates a file system with one SVM (named `fsx`) and one volume (named `vol1`). The volume has a junction path of `/vol1` and a capacity pool tiering policy of **Auto** (which will automatically tier any data that hasn't been accessed for 31 days to lower-cost capacity pool storage). The default snapshot policy gets assigned to the default volume. The file system data is encrypted at rest using your default service managed AWS KMS key.

### Creating a Microsoft Active Directory-joined SVM
<a name="getting-started-create-ad-svm"></a>

After creating your file system, you can create additional SVMs joined to Microsoft Active Directory to enable SMB access from Windows and macOS clients. FSx for ONTAP integrates with AWS Secrets Manager to securely manage your Microsoft Active Directory domain join service account credentials.

**To create a Microsoft Active Directory-joined SVM**

1. In the Amazon FSx console, choose **Storage virtual machines** from the left navigation pane.

1. Choose **Create storage virtual machine**.

1. For **File system**, select the file system you created.

1. For **Storage virtual machine name**, enter a name for your SVM.

1. For **Microsoft Active Directory configuration**, choose **Join a Microsoft Active Directory**.

1. For **Domain join service account credentials**, choose **Managed in Secrets Manager** (default) to use Secrets Manager for secure credential management.
**Note**  
Using Secrets Manager eliminates the need to store plaintext credentials and provides centralized credential management. For more information, see [Storing Active Directory credentials using AWS Secrets Manager](self-managed-AD-best-practices.md#bp-store-ad-creds-using-secret-manager).

1. For **Secret**, choose an existing secret from Secrets Manager that contains your domain join service account credentials, or choose **Create new secret** to create one.

1. Complete the remaining Microsoft Active Directory configuration fields as needed for your environment.

1. Choose **Create storage virtual machine**.

Your SVM will be created and joined to Microsoft Active Directory using the credentials stored in Secrets Manager. You can now create SMB shares and volumes on this SVM for Windows and macOS client access.

## Mounting your file system from an Amazon EC2 Linux instance
<a name="getting-started-step2"></a>

You can mount your file system from an Amazon Elastic Compute Cloud (Amazon EC2) instance. This procedure uses an instance running Amazon Linux 2.

**To mount your file system from Amazon EC2**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. Create or select an Amazon EC2 instance running Amazon Linux 2 that is in the same virtual private cloud (VPC) as your file system. For more information about launching an instance, see [ Step 1: Launch an instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EC2_GetStarted.html#ec2-launch-instance) in the *Amazon EC2 User Guide*.

1. Connect to your Amazon EC2 Linux instance. For more information, see [Connect to your Linux instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AccessingInstances.html) in the *Amazon EC2 User Guide*.

1. Open a terminal on your Amazon EC2 instance using secure shell (SSH), and log in with the appropriate credentials.

1. Create a directory on your Amazon EC2 instance to use as the volume's mount point with the following command. In the following example, replace {{mount-point}} with your own information.

   ```
   $ sudo mkdir /{{mount-point}}
   ```

1. Mount your Amazon FSx for NetApp ONTAP file system to the directory that you created. Use a `mount` command similar to the example that follows. In the following example, replace the following placeholder values with your own information.
   + `{{nfs_version}}` – The NFS version you are using; FSx for ONTAP supports versions 3, 4.0, 4.1, and 4.2.
   + `{{nfs-dns-name}}` – The NFS DNS name of the storage virtual machine (SVM) in which the volume you are mounting exists. You can find the NFS DNS name in the Amazon FSx console by choosing **Storage virtual machines**, then choosing the SVM on which the volume you are mounting exists. The NFS DNS name is found on the **Endpoints** panel.
   + `{{volume-junction-path}}` – The junction path of the volume that you're mounting. You can find a volume's junction path in the Amazon FSx console on the **Summary** panel of the Volume details page.
   + `{{mount-point}}` – The name of the directory that you created on your EC2 instance for the volume's mount point.

   ```
   sudo mount -t nfs -o nfsvers={{nfs_version}} {{nfs-dns-name}}:/{{volume-junction-path}} /{{mount-point}}
   ```

   The following command uses example values.

   ```
   sudo mount -t nfs -o nfsvers=4.1 svm-abcdef1234567890c.fs-012345abcdef6789b.fsx.us-east-2.amazonaws.com:/vol1 /fsxN
   ```

If you have issues with your Amazon EC2 instance (such as connections timing out), see [Troubleshoot EC2 instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-troubleshoot.html) in the *Amazon EC2 User Guide*.

## Cleaning up resources
<a name="getting-started-step3"></a>

After you have finished this exercise, you should follow these steps to clean up your resources and protect your AWS account.

**To clean up resources**

1. On the Amazon EC2 console, terminate your instance. For more information, see [Terminate Your Instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/terminating-instances.html) in the *Amazon EC2 User Guide.*

1. Open the Amazon FSx console at [https://console.aws.amazon.com/fsx/](https://console.aws.amazon.com/fsx/).

1. On the Amazon FSx console, delete all of your FSx for ONTAP volumes that are not root volumes of your SVM. For more information, see [Deleting volumes](deleting-volumes.md).

1. Delete all of your FSx for ONTAP SVMs. For more information, see [Deleting storage virtual machines (SVM)](deleting-svms.md).

1. On the Amazon FSx console, delete your file system. When you delete a file system, all automatic backups are deleted automatically. However, you still must delete any manually created backups. The following steps outline this process.

   1. From the console dashboard, choose the name of the file system that you created for this exercise.

   1. For **Actions**, choose **Delete file system**.

   1. In the **Delete file system** dialog box, enter the ID of the file system that you want to delete in the **File system ID** box.

   1. Choose **Delete file system**.

   1. While Amazon FSx deletes the file system, its status in the dashboard changes to **DELETING**. Once the file system is deleted, it no longer appears in the dashboard. Any automatic backups are deleted along with the file system.

   1. Now you can delete any manually created backups for your file system. From the left-side navigation, choose **Backups**.

   1. From the dashboard, choose any backups that have the same **File system ID** as the file system that you deleted, and choose **Delete backup**. Be sure to retain the final backup, if you created one.

   1. The **Delete backups** dialog box opens. Keep the check box selected for the IDs of the backups that you want to delete, and then choose **Delete backups**.

   Your Amazon FSx file system and any related automatic backups are now deleted, along with any manual backups that you chose to delete as well.