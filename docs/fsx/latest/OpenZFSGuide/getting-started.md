# Setting up an Amazon FSx for OpenZFS file system

If you are getting started with FSx for OpenZFS for the first time, follow these steps to learn how to create your file system, mount it from an Amazon EC2 instance, and clean up your resources once you are done.

###### Topics

- [Prerequisites](#getting-started-prerequisites "#getting-started-prerequisites")
- [Step 1: Create a file system](#getting-started-step1 "#getting-started-step1")
- [Step 2: Mount your file system from an Amazon EC2 instance](#getting-started-step2 "#getting-started-step2")
- [Step 3: Clean up your resources](#getting-started-step3 "#getting-started-step3")

## Prerequisites

Before you use Amazon FSx for the first time, make sure that you have completed the following tasks:

1. [Sign up for an AWS account](#sign-up-for-aws "#sign-up-for-aws")
2. [Create a user with administrative access](#create-an-admin "#create-an-admin")

###

#### Sign up for an AWS account

If you do not have an AWS account, complete the following steps to create one.

###### To sign up for an AWS account

1. Open [https://portal.aws.amazon.com/billing/signup](https://portal.aws.amazon.com/billing/signup "https://portal.aws.amazon.com/billing/signup").
2. Follow the online instructions.

Part of the sign-up procedure involves receiving a phone call or text message and entering
a verification code on the phone keypad.

When you sign up for an AWS account, an _AWS account root user_ is created. The root user has access to all AWS services
and resources in the account. As a security best practice, assign administrative access to a user, and use only the root user to perform [tasks that require root user access](../../../IAM/latest/UserGuide/id_root-user.md#root-user-tasks "../../../IAM/latest/UserGuide/id_root-user.md#root-user-tasks").

AWS sends you a confirmation email after the sign-up process is
complete. At any time, you can view your current account activity and manage your account by
going to [https://aws.amazon.com/](https://aws.amazon.com/ "https://aws.amazon.com/") and choosing **My
Account**.

#### Create a user with administrative access

After you sign up for an AWS account, secure your AWS account root user, enable AWS IAM Identity Center, and create an administrative user so that you
don't use the root user for everyday tasks.

###### Secure your AWS account root user

1. Sign in to the [AWS Management Console](https://console.aws.amazon.com/ "https://console.aws.amazon.com/") as the account owner by choosing **Root user** and entering your AWS account email address. On the next page, enter your password.

For help signing in by using root user, see [Signing in as the root user](../../../signin/latest/userguide/console-sign-in-tutorials.md#introduction-to-root-user-sign-in-tutorial "../../../signin/latest/userguide/console-sign-in-tutorials.md#introduction-to-root-user-sign-in-tutorial") in the _AWS Sign-In User Guide_. 2. Turn on multi-factor authentication (MFA) for your root user.

For instructions, see [Enable a virtual MFA device for your AWS account root user (console)](../../../IAM/latest/UserGuide/enable-virt-mfa-for-root.md "../../../IAM/latest/UserGuide/enable-virt-mfa-for-root.md") in the _IAM User Guide_.

###### Create a user with administrative access

1. Enable IAM Identity Center.

For instructions, see [Enabling
AWS IAM Identity Center](../../../singlesignon/latest/userguide/get-set-up-for-idc.md "../../../singlesignon/latest/userguide/get-set-up-for-idc.md") in the
_AWS IAM Identity Center User Guide_. 2. In IAM Identity Center, grant administrative access to a user.

For a tutorial about using the IAM Identity Center directory as your identity source, see [Configure user access with the default IAM Identity Center directory](../../../singlesignon/latest/userguide/quick-start-default-idc.md "../../../singlesignon/latest/userguide/quick-start-default-idc.md") in the
_AWS IAM Identity Center User Guide_.

###### Sign in as the user with administrative access

- To sign in with your IAM Identity Center user, use the sign-in URL that was sent to your email address when you created the IAM Identity Center user.

For help signing in using an IAM Identity Center user, see [Signing in to the AWS access portal](../../../signin/latest/userguide/iam-id-center-sign-in-tutorial.md "../../../signin/latest/userguide/iam-id-center-sign-in-tutorial.md") in the _AWS Sign-In User Guide_.

###### Assign access to additional users

1. In IAM Identity Center, create a permission set that follows the best practice of applying least-privilege permissions.

For instructions, see [Create a permission set](../../../singlesignon/latest/userguide/get-started-create-a-permission-set.md "../../../singlesignon/latest/userguide/get-started-create-a-permission-set.md") in the _AWS IAM Identity Center User Guide_. 2. Assign users to a group, and then assign single sign-on access to the group.

For instructions, see [Add groups](../../../singlesignon/latest/userguide/addgroups.md "../../../singlesignon/latest/userguide/addgroups.md") in the _AWS IAM Identity Center User Guide_.

## Step 1: Create a file system

The following procedures detail how to create a file system using the **Quick create** and **Standard create**
options on the Amazon FSx console. For instructions on how to create a file system using the AWS CLI instead of the AWS Management Console,
see [Creating an Amazon FSx for OpenZFS file system](creating-file-systems.md "creating-file-systems.md").

Use the **Quick create** option to rapidly and easily create a file system with the default root volume
configuration and a **Network type** of `IPv4`. This configuration automatically creates one root volume
named `fsx` with a path of `/fsx`, a record size of 128 KiB, an `NFS exports` setting in
which **Client addresses** is an asterisk (`*`) and **NFS options** is `rw,crossmnt`.
With these settings, any clients permitted by your VPC and security group settings can access the volume with read and write
permissions. The file system data is encrypted at rest using your default service manages AWS KMS key, named `aws/fsx/(default)`.

Use the **Standard create** option to create a file system with a customized root volume configuration and
a **Network type** of `IPv4` (which only supports IPv4) or `Dual-stack` (which supports
both IPv4 and IPv6). For a list of the file system properties that you can customize,
see [Configurable file system properties](creating-file-systems.md#fsx-openzfs-file-system-properties "creating-file-systems.md#fsx-openzfs-file-system-properties"). We recommend using
**Standard create** only when you are familiar with FSx for OpenZFS file systems and volumes.

###### Note

If you intend to create an FSx for OpenZFS file system that uses dual-stack mode, you must first assign an
Amazon-provided IPv6 CIDR block to your VPC and subnets. For more information, see [Add IPv6 support for your VPC](../../../vpc/latest/userguide/vpc-migrate-ipv6-add.md "../../../vpc/latest/userguide/vpc-migrate-ipv6-add.md") in the
_Amazon Virtual Private Cloud User Guide_.

Quick create (recommended)
**To create a file system using Quick create**

1.  Open the Amazon FSx console at [https://console.aws.amazon.com/fsx/](https://console.aws.amazon.com/fsx/ "https://console.aws.amazon.com/fsx/").
2.  On the dashboard, choose **Create file system** to start
    the file system creation wizard.
3.  On the **Select file system type** page, choose
    **Amazon FSx for OpenZFS**, and then choose **Next**. The
    **Create OpenZFS file system** page appears. For **Creation
    method**, choose **Quick create**. To create a file system
    using the **Standard create** method, see [Creating an Amazon FSx for OpenZFS file system](creating-file-systems.md "creating-file-systems.md").
4.  In the **Quick configuration** section, for **File system name -
    optional**, enter a name for your file system. It's easier to find and manage your
    file systems when you name them. You can use a maximum of 256 Unicode letters, white space, and
    numbers, plus these special characters: **+**
    **-** (hyphen) **=**
    **.**
    **\_** (underscore) **:**
    **/**.
5.  For **Storage class**, select **Intelligent-Tiering (elastic)**
    or **SSD (provisioned)**.
    - **Intelligent-Tiering (elastic)** offers fully elastic storage that is
      suitable for most workloads, as well as an optional SSD read cache that provides SSD latencies for
      reads of frequently accessed data. With Intelligent-Tiering, you are billed for the data you store,
      depending on the size of your dataset, and do not need to specify a file system size.
      Intelligent-Tiering is only supported for Multi-AZ (HA) file systems.
    - **SSD (provisioned)** provides low-latency access to your data.
      With SSD storage, you are billed for the amount of storage that you provision.

6.  For **Deployment type**, select **Multi-AZ (HA)** or **Single-AZ (HA)**.

        * **Multi-AZ (HA)** file systems offer high availability and high durability by replicating
         your data and supporting failover across multiple Availability Zones in the same AWS Region, with a separate copy
         of your data in each availability zone. Failover typically completes within 60 seconds.
        * **Single-AZ (HA)** file systems offer high availability by deploying a primary and
         standby file system within the same Availability Zone to deliver continuous availability in the event of failover
         and failback. Failover typically completes within 60 seconds. Single-AZ (HA) is only available for file systems
         using the SSD (provisioned) storage class.

    We recommend using Multi-AZ (HA) for most production workloads. We recommend using Single-AZ (HA) for workloads
    that require consistent single-AZ latencies and as a cost-effective solution for workloads that do not require the
    high levels of durability that Multi-AZ (HA) provides. For more information on how to choose between deployment types,
    see [Availability by AWS Region](available-aws-regions.md "available-aws-regions.md") and
    [File system performance](performance.md#zfs-fs-performance "performance.md#zfs-fs-performance").

7.  For **Throughput capacity** (Intelligent-Tiering only), select the desired throughput capacity of your file
    system, in MBps. For file systems using the Intelligent-Tiering storage class, the minimum throughput capacity is 160 MBps.
    To specify throughput capacity for a file system using the SSD (provisioned) storage class, create a file system using
    **Standard Create**.
8.  For **SSD read cache sizing mode** (Intelligent-Tiering only), select either **Automatic**,
    **Custom**, or **None**. Automatic is selected by default. With this option, Amazon FSx automatically chooses a read cache size based on your provisioned throughput.
    If you know the approximate size of your active working dataset, you can select
    Custom to customize the size of the SSD read cache. If your workload is not latency-sensitive, you can also choose None to create an elastic file system without an SSD cache and reduce costs.
9.  For **SSD storage capacity** (SSD (provisioned) only), specify the storage capacity of your file
    system, in gibibytes (GiBs). Enter any whole number in the range of 64–524,288.
10. For **Virtual Private Cloud (VPC)**, choose the Amazon VPC that you want to
    associate with your file system.
11. Choose **Next**.
12. Review the file system configuration shown on the **Create OpenZFS file system** page.
    For your reference, note which file system settings you can modify after the file system is created.
13. Choose **Create file system**.

Standard create
**To create a file system using Standard create**

1. Open the Amazon FSx console at [https://console.aws.amazon.com/fsx/](https://console.aws.amazon.com/fsx/ "https://console.aws.amazon.com/fsx/").
2. On the dashboard, choose **Create file system**
   to start the file system creation wizard.
3. On the **Select file system type** page, choose
   **FSx for OpenZFS** , and then choose
   **Next**. The **Create file
   system** page appears.
4. For **Creation method**, choose
   **Standard create**.

Begin your configuration with the **File system
details** section. 5. For **File system name - optional**, enter a name
for your file system. It's easier to find and manage your file
systems when you name them. You can use a maximum of 256 Unicode
letters, white space, and numbers, plus these special characters: +

- = . \_ : /

6.  For **Storage class**, select **Intelligent-Tiering (elastic)**
    or **SSD (provisioned)**.
    - **Intelligent-Tiering (elastic)** offers fully elastic, cost-effective storage
      that is suitable for most workloads, as well as an optional SSD read cache that provides SSD latencies for
      reads of frequently accessed data. With Intelligent-Tiering, you are billed for the data you store, depending
      on the size of your dataset, and do not need to specify a file system size. Intelligent-Tiering is only supported
      for Multi-AZ (HA) file systems.
    - **SSD (provisioned)** provides high performance with low-latency access to your data.
      With SSD storage, you are billed for the amount of storage that you provision.

7.  For **Deployment type**, select **Multi-AZ (HA)**, **Single-AZ (HA)**, or **Single-AZ (non-HA)**.

        * **Multi-AZ (HA)** file systems offer high availability and high durability by replicating your data and supporting failover across multiple Availability Zones in the same AWS Region, with a separate copy of your data in each Availability Zone. Failover typically completes within 60 seconds.
        * **Single-AZ (HA)** file systems offer high availability by deploying a primary and standby file system within the same Availability Zone to
         deliver continuous availability in the event of failover and failback. Failover typically completes within 60 seconds. Single-AZ (HA) is only available on file systems using the SSD (provisioned) storage class.
        * **Single-AZ (non-HA)** file systems ensure self-healing recovery within a single Availability Zone by automatically
         detecting and addressing component failures. Recovery typically completes within 30 minutes. Single-AZ (non-HA) is only available on file systems using the SSD (provisioned) storage class.

    We recommend using Multi-AZ (HA) for most production workloads. We recommend using Single-AZ (HA) for
    workloads that require consistent single-AZ latencies and as a cost-effective solution for workloads that do not require the
    high levels of durability that Multi-AZ (HA) provides. For more information on how to choose between deployment types,
    see [Availability by AWS Region](available-aws-regions.md "available-aws-regions.md") and [File system performance](performance.md#zfs-fs-performance "performance.md#zfs-fs-performance").

8.  For **SSD storage capacity** (SSD (provisioned) only), specify the storage capacity of your file
    system, in gibibytes (GiBs). Enter any whole number in the range of 64–524,288.
9.  For **Provisioned SSD IOPS** (SSD (provisioned) only), you have two
    options to provision the number of IOPS for your file system:
    - Choose **Automatic** (the default) if you
      want Amazon FSx to automatically provision 3 IOPS per GB of SSD
      storage.
    - Choose **User-provisioned** if you want
      to specify the number of IOPS, up to the maximum for your file system.
      You pay for SSD IOPS that you provision above 3 IOPS per GB
      of SSD storage.

10. **Throughput capacity** is the sustained speed at
    which the file server that hosts your file system can serve data.
    For **Throughput capacity**, choose from two
    options to provide your desired throughput capacity in megabytes per second
    (MBps).

        * Choose the default **Recommended throughput
         capacity** if you want Amazon FSx to automatically
         choose the throughput capacity. The recommended value is
         based on the storage capacity that you choose.
        * Choose **Specify throughput capacity** if
         you want to specify the throughput capacity value.




        	+ For Multi-AZ and SINGLE\_AZ\_2 file systems,
        	 valid values are 160, 320, 640, 1280, 2560, 3840, 5120,
        	 7680, or 10240 MBps.
        	+ For SINGLE\_AZ\_1 file systems, valid values
        	 are 64, 128, 256, 512, 1024, 2048, 3072, or 4096 MBps.
        You pay for throughput capacity that you provision that
         exceeds the recommended amount.

    You can increase the amount of throughput capacity as needed at
    any time after you create the file system. For more information, see
    [Modifying throughput capacity](managing-throughput-capacity.md "managing-throughput-capacity.md").

11. For **SSD read cache sizing mode** (Intelligent-Tiering only), select either **Automatic**,
    **Custom**, or **None**. Automatic is selected by default. With this option, Amazon FSx automatically chooses a read cache size based on your provisioned throughput.
    If you know the approximate size of your active working dataset, you can select
    Custom to customize the size of the SSD read cache. If your workload is not latency-sensitive, you can also choose None to create an elastic file system without an SSD cache and reduce costs.
12. In the **Network & security** section,
    provide networking and security group information:
    - For **Virtual Private Cloud (VPC)**,
      choose the Amazon VPC that you want to associate with your
      file system.
    - For **VPC Security Groups**, the ID for
      the default security group for your VPC should already be
      populated.
    - (Multi-AZ only) For **Preferred subnet**, choose any value from the
      list of available subnets. Also choose a **Standby subnet** for the standby
      file server.
    - (Single-AZ only) For **Subnet**, choose any value from the
      list of available subnets.
    - For **Network type**, select either **IPv4**
      (for only IPv4 support) or **Dual-stack** (for both IPv4
      and IPv6 support).
    - (Multi-AZ only) For **Select route tables**,
      specify the VPC route tables in which rules for routing traffic
      to the correct file server will be created. Select all VPC route
      tables associated with the subnets in which your clients are located.
      By default, Amazon FSx selects your VPC's default route table.
    - (Multi-AZ only) **Endpoint IPv4 address range**
      specifies the IPv4 address range in which the endpoints to access your
      file system are created. You have three options for the endpoint
      IPv4 address range:
      - **Unallocated IPv4 address range from your
        VPC** – Amazon FSx chooses a block of 16 available IPv4 addresses
        from the VPC’s IPv4 CIDR range to use as the endpoint IPv4 address range for the file system.
      - **Floating IPv4 address range outside your VPC** – Amazon FSx
        chooses a 198.19.x.0/24 address range.
      - **Enter an IPv4 address range** – You can provide
        an IPv4 CIDR range of your own choosing. The IPv4 address range that you choose can
        either be inside or outside the VPC’s IPv4 address range, as long as it doesn't
        overlap with any subnet.

    - (Multi-AZ and dual-stack only) **Endpoint IPv6 address range**
      specifies the IPv6 address range in which the endpoints to access your
      file system are created. You have two options for the endpoint
      IPv6 address range:
      - **Unallocated IPv6 address range from your
        VPC** – Amazon FSx chooses a block of 1024 available IPv6 addresses
        from one of the VPC’s IPv6 CIDR ranges to use as the endpoint IPv6 address range
        for the file system.
      - **Enter an IPv6 address range** – You can provide
        an IPv6 CIDR range of your own choosing. The IPv6 address range that you choose can
        either be inside or outside the VPC’s IPv6 address range, as long as it doesn't
        overlap with any subnet.

13. In the **Encryption** section, for
    **Encryption key**, choose the AWS Key Management Service
    (AWS KMS) encryption key that protects your file system's data at
    rest.
14. For **Root volume configuration**, you can set
    the following options for the file system's root volume:
    - For **Data compression type**, choose the
      type of compression to use for your volume—either
      **Zstandard**,
      **LZ4**, or **No
      compression**. Zstandard compression provides
      more data compression and higher read throughput than LZ4
      compression. LZ4 compression provides less compression and
      higher write throughput performance than Zstandard
      compression. For more information about the storage and
      performance benefits of the volume data compression options,
      see [Data compression](performance.md#perf-data-compression "performance.md#perf-data-compression").
    - For **Copy tags to snapshots**, choose
      whether to copy tags to the volume's snapshot.
    - For **NFS exports**, you can modify or
      remove the default client configuration setting. Client
      configurations determine client
      access and permissions for the
      volume.

    To provide additional client configurations:

        1. In the **Client addresses**
         field, specify which clients can access the volume.
         Enter an asterisk (`*`) for
         any
         client, a specific IP address, or a CIDR range of IP
         addresses.
        2. In the **NFS options** field,
         enter a comma-delimited set of
         export options. For example, enter `rw` to allow
         read and write permissions to the volume for the
         specified **Client
         addresses**.
        3. Choose **Add client
         configuration**.
        4. Repeat the procedure to add another client
         configuration.

    For more information, see [NFS exports](creating-volumes.md#nfs-exports "creating-volumes.md#nfs-exports").
    - For **Record size**, choose whether to
      use the default suggested record size of 128 KiB, or to set
      a custom suggested record size for the volume. Workloads
      that write in fixed small or large record sizes might
      benefit from setting a custom record size, such as database
      workloads (small record size) or media streaming workloads
      (large record size). We recommend using the default setting
      in most cases. For more information about setting record
      size, see [Configurable volume properties](creating-volumes.md#volume-properties "creating-volumes.md#volume-properties").
    - For **User and group quotas**, you can
      set a storage quota for a user or group:
      1. For **Quota type**, choose
         `USER` or `GROUP`.
      2. For **User or group ID**, choose
         the ID number for the user or group.
      3. For **Usage quota**, choose the
         storage quota number for the user or group.
      4. Choose **Add quota**.
      5. Repeat the procedure to add a quota for another
         user or group.

15. In **Backup and maintenance -
    _optional_**, you can set the
    following options:
    - For **Daily automatic backup**, choose
      **Enabled** for automatic daily
      backups. This option is enabled by default.
    - For **Daily automatic backup window**,
      set the time of the day in Coordinated Universal Time (UTC)
      that you want the daily automatic backup window to start.
      The window is 30 minutes starting from this specified time.
      This window can't overlap with the weekly maintenance backup
      window.
    - For **Automatic backup retention
      period**, set a period from 1–90 days to
      retain automatic backups.
    - For **Weekly maintenance window**, you
      can set the time of the week that you want the maintenance
      window to start. Day 1 is Monday, 2 is Tuesday, and so on.
      The window is 30 minutes starting from this specified time.
      This window can't overlap with the daily automatic backup
      window.

16. For **Tags - _optional_**, you can enter a key and value
    to add tags to your file system. A tag is a case-sensitive key-value
    pair that helps you manage, filter, and search for your file
    system.

Choose **Next**. 17. Review the file system configuration on the **Create file
system** page. Note which file system settings you can
modify after the file system is created. 18. Choose **Create file system**.

After your file system is created, you can create additional volumes as needed to organize your data.
Any new volumes that you create will be children of the root volume. For more information on how to create additional volumes, see
[Creating an Amazon FSx for OpenZFS volume](creating-volumes.md "creating-volumes.md").

## Step 2: Mount your file system from an Amazon EC2 instance

Once you have created your file system, you can access the data stored within it by mounting individual volumes on your client from an Amazon Elastic Compute Cloud (Amazon EC2) instance.
FSx for OpenZFS supports a wide variety of compute instances and operating systems using the Network File System (NFS) protocol (v3, v4.0, v4.1, and v4.2), including Amazon EC2 instances running Linux, macOS, and Microsoft Windows.

The following instructions detail how to mount a volume from an Amazon EC2 instance on a Linux, macOS, or Windows client. Note that you can also view and copy the exact commands needed to mount any FSx for OpenZFS volume
by choosing **Attach** on the details page for that volume in the Amazon FSx console.

###### Note

The commands to mount a volume require the DNS name of the file system in which the volume is created. To identify a file system's DNS name in the Amazon FSx console, choose **File systems**,
then choose the FSx for OpenZFS file system whose volume you are mounting. The **DNS name** will be displayed in the **Network & security** panel. This information can also be found in the response of the
[DescribeVolumes](../APIReference/API_DescribeVolumes.md "../APIReference/API_DescribeVolumes.md") API operation.

Linux client
**To mount a volume from an Amazon EC2 instance on Linux**

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. Create or select an Amazon EC2 instance running Amazon Linux 2 that is in the same virtual private cloud
   (VPC) as your file system. For more information about launching an instance, see [Step 1: Launch an instance](../../../AWSEC2/latest/UserGuide/EC2_GetStarted.md#ec2-launch-instance "../../../AWSEC2/latest/UserGuide/EC2_GetStarted.md#ec2-launch-instance") in the _Amazon EC2 User Guide_.
3. Connect to your Amazon EC2 Linux instance. For more information, see
   [Connect to your Linux instance](../../../AWSEC2/latest/UserGuide/connect-to-linux-instance.md "../../../AWSEC2/latest/UserGuide/connect-to-linux-instance.md")
   in the _Amazon EC2 User Guide_.
4. Open a terminal on your Amazon EC2 instance using secure shell (SSH), and log in with the
   appropriate credentials.
5. If you are using CentOS, RedHat, or Ubuntu, install the NFS client. This step is not necessary if you are using the latest version of the Amazon Linux 2.
   - For CentOS and RedHat use the following command: **sudo yum –y install nfs-utils**
   - For Ubuntu use this command: **sudo apt-get -y install nfs-common**

6. Create a directory on your Amazon EC2 instance for the volume's local mount path with the following
   command. In the following example, replace `fsx` with your desired location.

```
`sudo mkdir /`fsx``
```

7. Use the following `mount` command to mount your Amazon FSx for OpenZFS file system
   to the directory that you created. Replace the following:
   - Replace `nfs-version` with an NFS protocol version, such as
     `4.2`.
   - Replace `fs-dns-name` with the DNS name or the IP address
     of the file system.
   - Replace `volume-path` with the path of the volume to mount.
     For example, use `/fsx` to mount the root volume or a path such as
     `/fsx/sales` to mount the top-level `fsx/sales` directory.
   - Replace `local-mount-path` with the directory path of your local
     mount path, such as `/fsx` for the directory you created in step 5.

```
`sudo mount -t nfs -o nfsvers=`nfs-version` `fs-dns-name`:`volume-path` `local-mount-path``
```

The following example uses sample values.

```
`sudo mount -t nfs -o nfsvers=4.2 fs01234567.fsx.us-east-1.amazonaws.com:/fsx /fsx`
```

You can also use the IP address of the file system instead of its DNS name.

```
`sudo mount -t nfs -o nfsvers=4.2 198.51.100.5:/fsx /fsx`
```

If you have issues with your Amazon EC2 instance (such as connections timing out), see
[Troubleshoot EC2 instances](../../../AWSEC2/latest/UserGuide/ec2-instance-troubleshoot.md "../../../AWSEC2/latest/UserGuide/ec2-instance-troubleshoot.md")
in the _Amazon EC2 User Guide_.

macOS client

###### To mount a volume from an Amazon EC2 instance on macOS

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. Create or select an Amazon EC2 Mac instance running the macOS that is in the same VPC as the file system.

For more information on
launching an instance, see [Step 1: Launch an instance](../../../AWSEC2/latest/UserGuide/ec2-mac-instances.md#mac-instance-launch "../../../AWSEC2/latest/UserGuide/ec2-mac-instances.md#mac-instance-launch") in the _Amazon EC2 User Guide_. 3. Connect to your Amazon EC2 Mac instance. For more information, see
[Connect to your Linux instance](../../../AWSEC2/latest/UserGuide/AccessingInstances.md "../../../AWSEC2/latest/UserGuide/AccessingInstances.md")
in the _Amazon EC2 User Guide_. 4. Open a terminal on your EC2 Mac instance using secure shell (SSH), and log in with the appropriate credentials. 5. Create a directory on the EC2 instance for mounting the volume as follows:

```
`sudo mkdir /`localpath``
```

6. Mount the volume using the following command.

```
`sudo mount -t nfs -o resvport `file-system-dns-name`:/`vol_path` `mount-point``
```

The following example uses sample values.

```
`sudo mount -t nfs -o resvport fs-01234567890abcde5.fsx.us-east-1.amazonaws.com:/fsx/vol1 /fsx`
```

Windows

###### To mount a volume from an Amazon EC2 instance on Windows

###### Note

Mounting FSx for OpenZFS volumes to Windows clients leverages the NFS v3 protocol. The following instructions
include the necessary steps to install the NFS client on your Windows-based EC2 instance.

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. Create or select an Amazon EC2 instance running Microsoft Windows that is in
   the same VPC as the file system.

For more information on launching an instance, see
[Step 1: Launch an instance](../../../AWSEC2/latest/WindowsGuide/EC2_GetStarted.md#ec2-launch-instance "../../../AWSEC2/latest/WindowsGuide/EC2_GetStarted.md#ec2-launch-instance") in the _Amazon EC2 User Guide_. 3. Connect to your Amazon EC2 Windows instance. For more information, see
[Connecting to your Windows instance](../../../AWSEC2/latest/WindowsGuide/connecting_to_windows_instance.md "../../../AWSEC2/latest/WindowsGuide/connecting_to_windows_instance.md") in the _Amazon EC2 User Guide_. 4. Open PowerShell as an administrator, and install the NFS client.

```
`Install-WindowsFeature -Name NFS-Client`
```

If prompted to do so, restart and reconnect to your Windows instance. 5. Open a command prompt window with standard user privileges. If you run the mount command as Administrator,
the mounted drive will not appear in File Explorer.

###### Note

To ensure this mounted drive appears in File Explorer, please open the Command Prompt window with standard user privileges.
If you run this command as Administrator, it will not appear in File Explorer. 6. You can mount the drive using a command prompt, or using a Powershell path

    1. Mount the volume to any available drive letter by running the following command, replacing Z: with any available drive letter:




    	* Replace `filesystem-dns-name` with the DNS name or the IP address
    	 of the file system.
    	* Replace `vol_path` with the path of the FSx for OpenZFS volume
    	 you are trying to mount.
    	* Replace `Z:` with any available drive letter.

    ```
    `mount \\`filesystem-dns-name`\`vol_path` `Z:``
    ```

    The following example uses sample values.



    ```
    `mount \\fs-01234567890abcdef1.fsx.us-east-1.amazonaws.com\fsx\vol1 Z:`
    ```
    2. You can also mount the file system using the following Powershell path:



    ```
    New-PSDrive -Name "Z" -PSProvider "FileSystem" -Root "\\`filesystem-dns-name`\" -Persist
    ```

    The following example uses a sample file system DNS name.



    ```
    New-PSDrive -Name "Z" -PSProvider "FileSystem" -Root "\\fs-0239c0e31af65bff1.fsx.us-east-1.amazonaws.com\" -Persist
    ```

## Step 3: Clean up your resources

Follow these steps to clean up your
resources, delete your file system as needed, and protect your AWS account.

###### Note

Before deleting a file system, make sure there are no Amazon S3 access points attached to any volume.
For information on how to list S3 access points attached to FSx for OpenZFS volumes,
see [Listing S3 access point attachments](access-points-list.md "access-points-list.md").
For information on how to delete S3 access points,
see [Deleting an S3 access point attachment](delete-access-point.md "delete-access-point.md").

###### To clean up your resources and delete your file system

1. On the Amazon EC2 console, terminate your instance. For more information, see [Terminate Your Instance](../../../AWSEC2/latest/UserGuide/terminating-instances.md "../../../AWSEC2/latest/UserGuide/terminating-instances.md") in
   the _Amazon EC2 User Guide._
2. Open the Amazon FSx console at [https://console.aws.amazon.com/fsx/](https://console.aws.amazon.com/fsx/ "https://console.aws.amazon.com/fsx/").
3. On the Amazon FSx console, delete your file system. When you delete a file system, all
   volumes and automatic backups are deleted automatically. However, you still must delete any manually
   created backups. The following steps outline this process.
   1. From the console dashboard, choose the name of the file system that you created for this
      exercise.
   2. For **Actions**, choose **Delete file
      system**.
   3. In the **Delete file system** dialog box that opens, decide
      whether you want to create a final backup. If you do, provide a name for the final
      backup. Any automatically created backups are also deleted.

   ###### Important

   New file systems can be created from backups. We recommend that you create a
   final backup as a best practice. If you find you don't need it after a certain
   period of time, you can delete this and other manually created backups. 4. Enter the ID of the file system that you want to delete in the **File
   system ID** box. 5. Choose **Delete file system**. 6. The file system is now being deleted, and its status in the dashboard changes to
   **DELETING**. When the file system has been deleted, it no longer appears
   in the dashboard. Any automatic backups are deleted along with the file system. 7. Now you can delete any manually created backups for your file system. From the
   left-side navigation, choose **Backups**. 8. From the dashboard, choose any backups that have the same **File system
   ID** as the file system that you deleted, and choose **Delete
   backup**. Be sure to retain the final backup, if you created one. 9. The **Delete backups** dialog box opens. Keep the check box selected
   for the IDs of the backups that you want to delete, and then choose **Delete
   backups**.Your Amazon FSx file system and any related automatic backups are now deleted, along with any
   manual backups that you chose to delete as well.
