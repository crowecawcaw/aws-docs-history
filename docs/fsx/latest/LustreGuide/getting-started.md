# Getting started with Amazon FSx for Lustre

Following, you can learn how to get started using Amazon FSx for Lustre. These steps walk you through
creating an Amazon FSx for Lustre file system and accessing it from your compute instances. Optionally, they
show how to use your Amazon FSx for Lustre file system to process the data in your Amazon S3 bucket with your
file-based applications.

This getting started exercise includes the following steps.

###### Topics

- [Prerequisites](#prerequisites "#prerequisites")
- [Step 1: Create your FSx for Lustre file system](#getting-started-step1 "#getting-started-step1")
- [Step 2: Install and configure the Lustre client](#getting-started-step2 "#getting-started-step2")
- [Step 3: Mount the file system](#getting-started-mount-fs "#getting-started-mount-fs")
- [Step 4: Run your workflow](#getting-started-step3 "#getting-started-step3")
- [Step 5: Clean up resources](#getting-started-step4 "#getting-started-step4")

## Prerequisites

To perform this getting started exercise, you need the following:

- An AWS account with the permissions necessary to create an Amazon FSx for Lustre file system and an
  Amazon EC2 instance. For more information, see [Setting up Amazon FSx for Lustre](setting-up.md "setting-up.md").
- Create a Amazon VPC security group to be associated with your FSx for Lustre file system, and
  do not change it after file system creation. For more information, see
  [To create a security group for your Amazon FSx file system](limit-access-security-groups.md#create-security-group "limit-access-security-groups.md#create-security-group").
- An Amazon EC2 instance running a supported Linux release in your virtual private cloud
  (VPC) based on the Amazon VPC service. For this getting started exercise,
  we recommend using Amazon Linux 2023. You will install the Lustre client on this EC2 instance,
  and then mount your FSx for Lustre file system on the EC2 instance. For more information on creating an EC2 instance, see
  [Getting started: Launch an instance](../../../AWSEC2/latest/UserGuide/EC2_GetStarted.md "../../../AWSEC2/latest/UserGuide/EC2_GetStarted.md") or
  [Launch your instance](../../../AWSEC2/latest/UserGuide/LaunchingAndUsingInstances.md "../../../AWSEC2/latest/UserGuide/LaunchingAndUsingInstances.md")
  in the _Amazon EC2 User Guide_.

Besides Amazon Linux 2023, the Lustre client supports the Amazon Linux 2, Red Hat Enterprise Linux (RHEL),
CentOS, Rocky Linux, SUSE Linux Enterprise Server, and Ubuntu operating systems. For more information,
see [Lustre file system and client kernel compatibility](lustre-client-matrix.md "lustre-client-matrix.md").

- When creating your Amazon EC2 instance for this getting started exercise, keep the
  following in mind:
  - We recommend that you create your instance in your default VPC.
  - We recommend that you use the default security group when creating your EC2 instance.

- Determine which type of Amazon FSx for Lustre file system you want to create,
  _scratch_ or _persistent_. For more information,
  see [Deployment and storage class options for FSx for Lustre file systems](using-fsx-lustre.md "using-fsx-lustre.md").
- Each FSx for Lustre file system requires one IP address for each metadata server (MDS) and
  one IP address for each storage server (OSS). For more information,
  see [IP addresses for file systems](using-fsx-lustre.md#ip-addesses-for-fs "using-fsx-lustre.md#ip-addesses-for-fs").
- An Amazon S3 bucket storing the data for your workload to process. The S3 bucket
  will be the linked durable data repository for your FSx for Lustre file system.

## Step 1: Create your FSx for Lustre file system

You create your file system in the Amazon FSx console. Note that all FSx for Lustre file systems
are built on Lustre version 2.15 when created using the Amazon FSx console.

###### To create your file system

1. Open the Amazon FSx console at [https://console.aws.amazon.com/fsx/](https://console.aws.amazon.com/fsx/ "https://console.aws.amazon.com/fsx/").
2. From the dashboard, choose **Create file system** to start the file
   system creation wizard.
3. Choose **FSx for Lustre** and then choose **Next**
   to display the **Create File System** page.

Begin your configuration with the **File system details** section. 4. For **File system name-optional**, provide a name for your file system. You can
use up to 256 Unicode letters, white space, and numbers plus the special characters **+ - = . \_ : /**. 5. For **Deployment and storage class**, choose one of the options:

    * Choose **Persistent, SSD**
     for longer-term storage and for latency-sensitive workloads. With SSD storage, you are
     billed for the amount of storage that you provision.


    Optionally, choose **with EFA enabled** to enable
     Elastic Fabric Adapter (EFA) support for the file system. For more information
     about EFA, see [Working with EFA-enabled file systems](efa-file-systems.md "efa-file-systems.md").
    * Choose **Persistent, Intelligent-Tiering**
     for longer-term storage. The Intelligent-Tiering storage class provides fully elastic, cost-effective
     storage that is suitable for most workloads, as well as an optional SSD read cache that provides SSD
     latencies for reads of frequently accessed data. With Intelligent-Tiering, you are billed for the data
     you store, depending on the size of your dataset, and do not need to specify a file system size.


    Optionally, choose **with EFA enabled** to enable
     Elastic Fabric Adapter (EFA) support for the file system.
    * Choose **Scratch, SSD** deployment for temporary storage and
     shorter-term processing of data. With SSD storage, you are billed for the amount of storage
     that you provision.

6.  Choose the amount of throughput for your file system. You pay for the amount of throughput
    that you provision.
    - For Persistent SSD storage, choose a
      **Throughput per unit of storage** value.
      _Throughput per unit of storage_ is the amount of read and write
      throughput for each 1 tebibyte (TiB) of storage provisioned.
    - For Scratch SSD storage, choose a
      **Throughput per unit of storage** value.
    - For Intelligent-Tiering storage, choose
      a **Throughput capacity** value.

7.  For **Storage capacity** (SSD storage class only), set the amount of storage capacity
    for your file system, in TB:

        * For a *Persistent, SSD* deployment type, set this to a
         value of 1.2 TiB, 2.4 TiB, or increments of 2.4 TiB.
        * For an *EFA-enabled, Persistent, SSD* deployment type,
         set this value in increments of 4.8 TiB, 9.6 TiB, 19.2 TiB, and 38.4 TiB for 1000, 500, 250, and
         125 MBps/TiB throughput tiers, respectively.

    You can increase the amount of storage capacity as needed after you create the file system. For more
    information, see [Managing storage capacity](managing-storage-capacity.md "managing-storage-capacity.md").

8.  For the metadata configuration, choose one of the following options to provision
    the number of Metadata IOPS for your file system:

        * Choose **Automatic** (SSD storage class only) if you want
         Amazon FSx for Lustre to automatically provision and scale the metadata IOPS on your file system
         based on your file system's storage capacity.
        * Choose **User-provisioned** if you want to specify the
         number of Metadata IOPS to provision for your file system with SSD or
         Intelligent-Tiering storage class. Valid values are as follows:




        	+ For SSD file systems, valid values are `1500`,
        	 `3000`, `6000`, `12000`, and
        	 multiples of `12000` up to a maximum of `192000`.
        	+ For Intelligent-Tiering file systems, valid values are `6000`
        	 and `12000`.

    For more information about Metadata IOPS, see
    [Lustre metadata performance configuration](managing-metadata-performance.md#metadata-configuration "managing-metadata-performance.md#metadata-configuration").

9.  For **SSD read cache** (Intelligent-Tiering only),
    select either **Automatic (proportional to throughput capacity)** or
    **Custom (user-provisioned)**. With the Automatic option, Amazon FSx for Lustre automatically
    chooses a read cache size based on your provisioned throughput. If you know the approximate
    size of your active working dataset, you can select Custom to customize the size of the SSD
    read cache. For more information, see [Managing provisioned SSD read cache](managing-ssd-read-cache.md "managing-ssd-read-cache.md").
10. For **Data compression type**, choose **NONE** to turn off
    data compression or choose **LZ4** to turn on data compression with the LZ4 algorithm.
    For more information, see [Lustre data compression](data-compression.md "data-compression.md").
11. In the **Network & security** section, provide the following networking and
    security group information:
    - For **Virtual Private Cloud (VPC)**, choose the VPC that you want to
      associate with your file system. For this getting started exercise, choose the same VPC that you chose
      for your Amazon EC2 instance.
    - For **VPC security groups**, the ID for the default security group
      for your VPC should be already added.

    If you're not using the default security group, make sure that the following
    inbound rule is added to the security group you're using for this getting started exercise.

    | Type    | Protocol | Port range | Source                                 | Description                 |
    | ------- | -------- | ---------- | -------------------------------------- | --------------------------- |
    | All TCP | TCP      | 0-65535    | Custom `the_ID_of_this_security_group` | Inbound Lustre traffic rule |

    ###### Important

        + Make sure that the security group you are using follows the
         configuration instructions provided in [File system access control with Amazon VPC](limit-access-security-groups.md "limit-access-security-groups.md"). You must set up the security
         group to allow inbound traffic on ports 988 and 1018-1023 from the security
         group itself or the full subnet CIDR, which is required to allow the file system
         hosts to communicate with each other.
        + If you are creating an EFA-enabled file system, make sure you
         specify an [EFA-enabled security group](limit-access-security-groups.md#efa-security-groups "limit-access-security-groups.md#efa-security-groups").

    - For **Subnet**, choose any value from the list of available subnets.

12. For the **Encryption** section, the options available vary
    depending upon which file system type you're creating:
    - For a persistent file system, you can choose an AWS Key Management Service (AWS KMS) encryption key to
      encrypt the data on your file system at rest.
    - For a scratch file system, data at rest is encrypted using keys managed by AWS.
    - For scratch 2 and persistent file systems, data in transit is encrypted
      automatically when the file system is accessed from a supported Amazon EC2 instance type.
      For more information, see [Encrypting data in transit](encryption-in-transit-fsxl.md "encryption-in-transit-fsxl.md").

13. For **Data Repository Import/Export _optional_** section,
    linking your file system to Amazon S3 data repositories is disabled by default. For information
    about enabling this option and creating a data repository association to an existing S3 bucket, see
    [To link an S3 bucket while
    creating a file system (console)](create-linked-dra.md#export-path-lustre-console-dra-new "create-linked-dra.md#export-path-lustre-console-dra-new").

###### Important

    * Selecting this option also disables backups and you won't be able to enable
     backups while creating the file system.
    * If you link one or more Amazon FSx for Lustre file systems to an Amazon S3 bucket, don't delete the
     Amazon S3 bucket until all linked file systems have been deleted.
    * Intelligent-Tiering file systems don't support linking to Amazon S3 data
     repositories.

14. For **Logging _optional_**, logging is enabled by default.
    When enabled, failures and warnings for data repository activity on your file system are logged to Amazon CloudWatch Logs.
    For information about configuring logging, see [Managing logging](cw-event-logging.md#manage-logging "cw-event-logging.md#manage-logging").
15. In **Backup and maintenance _optional_**, you
    can do the following.

        * Disable the **Daily automatic backup**. This option is enabled
         by default, unless you enabled **Data Repository Import/Export**.
        * Set the start time for **Daily automatic backup window**.
        * Set the **Automatic backup retention period**, from 1 - 35 days.
        * Set the **Weekly maintenance window** start time, or keep it set to
         the default **No preference**.

    For more information, see [Protecting your data with backups](using-backups-fsx.md "using-backups-fsx.md")
    and [Amazon FSx for Lustre maintenance windows](maintenance-windows.md "maintenance-windows.md").

16. For **Root Squash _optional_**, root squash
    is disabled by default. For information about enabling and configuring root squash,
    see [To enable root squash when creating a file system (console)](root-squash.md#create-root-squash-console "root-squash.md#create-root-squash-console").
17. Create any tags that you want to apply to your file system.
18. Choose **Next** to display the **Create file system summary** page.
19. Review the settings for your Amazon FSx for Lustre file system, and choose **Create file
    system**.

Now that you've created your file system, note its fully qualified domain name and mount
name for a later step. You can find the fully qualified domain name and mount name for a file
system by choosing the name of the file system in the **File systems**
dashboard, and then choosing **Attach**.

## Step 2: Install and configure the Lustre client

Before you can access your Amazon FSx for Lustre file system from your Amazon EC2 instance, you have to do the following:

- Verify your EC2 instance meets the minimum kernel requirements.
- Update the kernel if needed.
- Download and install the Lustre client.

###### To check the kernel version and download the Lustre client

1. Open a terminal window on your EC2 instance.
2. Determine which kernel is currently running on your compute instance by running
   the following command.

```
uname -r
```

3.  Do one of the following:

        * If the command returns `6.1.79-99.167.amzn2023.x86_64` for x86-based EC2 instances,
         or `6.1.79-99.167.amzn2023.aarch64` or higher for Graviton2-based EC2 instances,
         download and install the Lustre client with the following command.



        ```
        sudo dnf install -y lustre-client
        ```
        * If the command returns a result less than `6.1.79-99.167.amzn2023.x86_64` for x86-based EC2 instances,
         or less than `6.1.79-99.167.amzn2023.aarch64` for Graviton2-based EC2 instances, update the kernel and
         reboot your Amazon EC2 instance by running the following command.



        ```
        sudo dnf -y update kernel && sudo reboot
        ```

        Confirm that the kernel has been updated using the **uname -r** command.
         Then download and install the Lustre client as described above.

    For information about installing the Lustre client on other Linux distributions,
    see [Installing the Lustre client](install-lustre-client.md "install-lustre-client.md").

## Step 3: Mount the file system

To mount your file system, you will create a mounting directory, or mount point, and then mount the file system on to your client,
and verify that your client can access the file system.

###### To mount your file system

1. Make a directory for the mount point with the following command.

```
sudo mkdir -p /mnt/fsx
```

2. Mount the Amazon FSx for Lustre file system to the directory that you created. Use the following
   command and replace the following items:
   - Replace `file_system_dns_name` with the actual file
     system's Domain Name System (DNS) name.
   - Replace `mountname` with the file system's mount name,
     which you can get by running the **describe-file-systems** AWS CLI command
     or the [DescribeFileSystems](../APIReference/API_DescribeFileSystems.md "../APIReference/API_DescribeFileSystems.md") API operation.

```
sudo mount -t lustre -o relatime,flock `file_system_dns_name`@tcp:/`mountname` /mnt/fsx
```

This command mounts your file system with two options, `-o relatime` and
`flock`:

    * `relatime` – While the `atime` option maintains
     `atime` (inode access times) data for each time a file is accessed, the
     `relatime` option also maintains `atime` data, but not for
     each time that a file is accessed. With the `relatime` option enabled,
     `atime` data is written to disk only if the file has been modified since
     the `atime` data was last updated (`mtime`), or if the file was
     last accessed more than a certain amount of time ago (6 hours by default).
     Using either the `relatime` or `atime` option will optimize the
     [file release](file-release.md "file-release.md") processes.


    ###### Note

    If your workload requires precise access time accuracy, you can mount with the
     `atime` mount option. However, doing so can impact workload performance
     by increasing the network traffic required to maintain precise access time values.

    If your workload does not require metadata access time, using the `noatime`
     mount option to disable updates to access time can provide a performance gain. Be aware that
     `atime` focused processes like file release or releasing data validity will be
     inaccurate in their release.
    * `flock` – Enables file locking for your file system. If you
     don't want file locking enabled, use the `mount` command without
     `flock`.

3. Verify that the mount command was successful by listing the contents of the directory
   to which you mounted the file system `/mnt/fsx`, by using the following
   command.

```
`ls /mnt/fsx`
import-path  lustre
$
```

You can also use the `df` command, following.

```
df
Filesystem                      1K-blocks    Used  Available Use% Mounted on
devtmpf                          1001808       0    1001808   0% /dev
tmpfs                            1019760       0    1019760   0% /dev/shm
tmpfs                            1019760     392    1019368   1% /run
tmpfs                            1019760       0    1019760   0% /sys/fs/cgroup
/dev/xvda1                       8376300 1263180    7113120  16% /
123.456.789.0@tcp:/`mountname`  3547698816   13824 3547678848   1% /mnt/fsx
tmpfs                             203956       0     203956   0% /run/user/1000

```

The results show the Amazon FSx file system mounted on /mnt/fsx.

## Step 4: Run your workflow

Now that your file system has been created and mounted to a compute instance, you can use
it to run your high-performance compute workload.

You can create a data repository association to link your file system to an Amazon S3 data
repository, For more information,
see [Linking your file system to an Amazon S3 bucket](create-dra-linked-data-repo.md "create-dra-linked-data-repo.md").

After you've linked your file system to an Amazon S3 data repository, you can export data that you've
written to your file system back to your Amazon S3 bucket at any time. From a terminal on one of
your compute instances, run the following command to export a file to your Amazon S3 bucket.

```
sudo lfs hsm_archive `file_name`
```

For more information on how to run this command on a folder or large collection of files
quickly, see [Exporting files using HSM
commands](exporting-files-hsm.md "exporting-files-hsm.md").

## Step 5: Clean up resources

After you have finished this exercise, you should follow these steps to clean up your
resources and protect your AWS account.

###### To clean up resources

1. If you want to do a final export, run the following command.

```
nohup find /mnt/fsx -type f -print0 | xargs -0 -n 1 sudo lfs hsm_archive &
```

2. On the Amazon EC2 console, terminate your instance. For more information, see [Terminate Your Instance](../../../AWSEC2/latest/UserGuide/terminating-instances.md "../../../AWSEC2/latest/UserGuide/terminating-instances.md") in the
   _Amazon EC2 User Guide._
3. On the Amazon FSx for Lustre console, delete your file system with the following procedure:
   1. In the navigation pane, choose **File systems**.
   2. Choose the file system that you want to delete from list of file systems on the
      dashboard.
   3. For **Actions**, choose **Delete file
      system**.
   4. In the dialog box that appears, choose if you want to take a final backup
      of the file system. Then provide the file system ID to confirm the deletion. Choose
      **Delete file system**.

4. If you created an Amazon S3 bucket for this exercise, and if you don't want to preserve the
   data you exported, you can now delete it. For more information, see [Deleting a bucket](../../../AmazonS3/latest/userguide/delete-bucket.md "../../../AmazonS3/latest/userguide/delete-bucket.md") in the
   _Amazon Simple Storage Service User Guide._
