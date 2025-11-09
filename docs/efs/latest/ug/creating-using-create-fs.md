# Creating EFS file systems

You can create a file system when you create a new EC2 launch instance, as explained in
the [Getting started exercise](getting-started.md "getting-started.md"). However, you can also create file systems by using the Amazon EFS
console, the AWS Command Line Interface (AWS CLI), or the Amazon EFS API.

When creating the file system using the Amazon EFS console, you have different options,
depending on whether you want the file system to use the recommended settings or if you want
to customize the settings.

- You can use Quick create to quickly create a file system with the following recommended
  settings.
  - Regional availability
  - Lifecycle policies to transition the file system to EFS Infrequent Access
    (IA) storage after 30 days, to EFS Archive storage after 90
    days, and not to transition to EFS Standard storage
  - Encryption of data at rest enabled
  - Elastic throughput mode
  - General Purpose performance mode
  - Mount targets configured in each Availability Zone in the AWS Region in which the file
    system is created using an available IPv4 on the specified subnet

- You can use Customize to create a file system with the settings you choose.
  For a table that lists the file system settings and the recommended values, see [Configuration options for file
  systems](#creating-using-create-fs-part1 "#creating-using-create-fs-part1").

## Required IAM permissions for creating file

systems

To create EFS resources, such as a file system and access points, you must
have AWS Identity and Access Management (IAM) permissions for the corresponding API operation and resource.

Create IAM users and grant them permissions for Amazon EFS actions with user policies. You
can also use roles to grant cross-account permissions. Amazon Elastic File System also uses an IAM
service-linked role that includes permissions required to call other AWS services on
your behalf. For more information about managing permissions for API operations, see [Identity and access management for Amazon EFS](security-iam.md "security-iam.md").

## Configuration options for file

systems

EFS file systems are configured with the settings listed in the following
table.

- If you use Quick create to create the file system, the file system is created with
  the indicated recommended value for the setting.
- If use Customize to create a custom file system, you can change the recommended
  value for the setting.

| EFS file system settings | Setting                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Description |
| ------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| **File system type**     | *Recommended: Regional*The file system type determines the<br>[availability and durability](features.md#availability-durability "features.md#availability-durability") with<br>which an EFS file system stores data within an AWS Region.<br>• **Regional** file systems store data and<br>metadata redundantly across all Availability Zones within an AWS Region. You can<br>also create mount targets in each Availability Zone in the AWS Region.<br>Regional offers the highest levels of availability and<br>durability.<br>• **One Zone** file systems store data and<br>metadata redundantly within a single Availability Zone. One Zone file<br>systems can have only a single mount target. This mount target must be located<br>in the same Availability Zone in which the file system is created.<br>NoteOne Zone file systems are available to only certain<br>Availability Zones.<br>For more information about file system types, see [Availability and durability of EFS file systems](features.md#availability-durability "features.md#availability-durability").                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| **Lifecycle management** | _Recommended: Transition into IA storage after 30 days<br>and into Archive storage after 90 days. Do not transition into<br>Standard storage._<br>Lifecycle management uses lifecycle policies to automatically move files<br>in to and out of the lower-cost Infrequent Access (IA) storage class<br>based on access patterns. When you create a file system by using the AWS Management Console,<br>the file system's lifecycle policy is configured with the following default<br>settings:<br>• **Transition into IA** set to **30 days since last<br>access**.<br>• **Transition into Archive** set to **90<br>days since last access.**<br>• **Transition into Standard** set to<br>**None**.<br>When you create a file system by using the AWS CLI, Amazon EFS API, or AWS SDKs,<br>you cannot set a lifecycle policy at the same time. You must wait until the file<br>system is created, and then use the [PutLifecycleConfiguration](API_PutLifecycleConfiguration.md "API_PutLifecycleConfiguration.md") API operation to update the lifecycle policy.<br>For more information about lifecycle management, see [Managing storage lifecycle](lifecycle-management-efs.md "lifecycle-management-efs.md").                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| **Encryption at rest**   | _Recommended: Enabled_<br>Amazon EFS uses your AWS Key Management Service (AWS KMS) EFS service key<br>(`aws/elasticfilesystem`) to encrypt data at rest by default. With<br>encryption, all data and metadata stored on it are encrypted. After you create an<br>EFS file system, you cannot change its encryption setting. To convert<br>an unencrypted file system to encrypted, you must create a new file system.<br>For more information about encryption in Amazon EFS, see [Data encryption in Amazon EFS](encryption.md "encryption.md").                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| **Throughput mode**      | _Recommended: Elastic_<br>You can choose from the following throughput modes:<br>• **Elastic** – Provides throughput that<br>scales up and down automatically in real time, to meet your workload’s<br>performance needs.<br>• **Provisioned** – Specify the<br>throughput amount that you want, independent of the file system's size.<br>• **Bursting** – Provides throughput<br>that scales with the amount of data in Standard storage.<br>NoteAdditional charges are associated with using Elastic and<br>Provisioned throughput. For more information, see [Amazon EFS pricing](https://aws.amazon.com/efs/pricing/ "https://aws.amazon.com/efs/pricing/").<br>For more information about throughput modes, see [Throughput modes](performance.md#throughput-modes "performance.md#throughput-modes").                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| **Performance mode**     | _Recommended: General Purpose_<br>The **General Purpose\*<br>• performance mode has the lowest<br>per-operation latency and is recommended for all file systems.<br>**Max I/O\*\*<br>is a previous generation performance type that is designed for highly parallelized workloads that can tolerate higher latencies<br>than the General Purpose mode. Max I/O mode is not supported for One Zone file systems or<br>file systems that use Elastic throughput.ImportantDue to the higher per-operation latencies with Max I/O, we recommend using General Purpose performance mode for all file systems. For more<br>information, see [Performance modes](performance.md#performancemodes "performance.md#performancemodes").                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| **Network access**       | _Recommended: Mount target created in each Availability Zone in which the file system is<br>available_<br>The mount target settings are as follows:<br>• **VPC** – You can create mount targets for the file system in<br>one VPC at a time. By default, the EC2 instance's default subnet is<br>selected. Change the VPC if you need to access the file system from a<br>different VPC.<br>If you want to change the VPC after creating the after the file system, you<br>need to first delete the mount targets from the current VPC. For more information,<br>see [Changing the mount target VPC](manage-fs-access-change-vpc.md "manage-fs-access-change-vpc.md").<br>• **Availability Zone** and **Subnet ID** – You can change the Availability Zone or subnet for the mount<br>target.<br>• **IP address type** – By default, Amazon EFS uses<br>an IPv4 address at which to create the mount target. You can alternatively<br>choose **IPv6 only\*<br>• to support IPv6 addresses<br>only, or **Dual-stack\*<br>• to support both IPv4 and<br>IPv6 addresses.<br>NoteThe IP address type must match the IP type of the subnet. Additionally,<br>the IP address type overrides the IP addressing attribute of your subnet.<br>For example, if the IP address type is IPv4-only and the IPv6 addressing<br>attribute is enabled for your subnet, network interfaces created in the<br>subnet receive an IPv4 address from the range of the subnet. For more<br>information, see [Modify the IP addressing<br>attributes of your subnet](../../../vpc/latest/userguide/subnet-public-ip.md "../../../vpc/latest/userguide/subnet-public-ip.md").<br>• **IP address** – By default, Amazon EFS creates the<br>mount target at an available address on the specified subnet. Alternately, you<br>can specify the IP address for the mount target.<br>You can't change the IP address of a mount target after it's created. You need<br>to delete the mount target and create a new one with the new address.<br>• **Security group** – The security group assigned to the<br>VPC target is used by default. You can add or remove security groups. For more<br>information about security groups, see [Changing mount target<br>security groups](manage-fs-access-update-mount-target-config-sg.md "manage-fs-access-update-mount-target-config-sg.md").<br>When you create a file system by using the AWS CLI, Amazon EFS API, or AWS SDKs,<br>you cannot create a mount target at the same time. You must wait until the file<br>system is created, and then use the [CreateMountTarget](API_CreateMountTarget.md "API_CreateMountTarget.md") API operation to create the mount<br>targets.<br>For more information about mount targets, see [Managing mount targets](accessing-fs.md "accessing-fs.md"). |

Use the Amazon EFS console to create an Amazon EFS file system that has the recommended
settings. If you want to create a file system with a customized configuration, see [Custom create using the console](#creating-using-fs-part1-console "#creating-using-fs-part1-console").

###### To quick create an Amazon EFS file system that has the recommended settings

1.  Sign in to the AWS Management Console and open the Amazon EFS console at
    [https://console.aws.amazon.com/efs/](https://console.aws.amazon.com/efs/ "https://console.aws.amazon.com/efs/").
2.  Choose **Create file system** to open the **Create file
    system** dialog box.
3.  (Optional) Enter a **Name** for your file system.
4.  For **Virtual Private Cloud (VPC)**, choose your VPC, or keep it set to your default VPC.
5.  Choose **Create** to create a file system that uses the following
    service recommended settings:

        * Regional availability
        * Lifecycle policies to transition the file system to EFS Infrequent Access
         (IA) storage after 30 days, to EFS Archive storage after
         90 days, and not to transition to EFS Standard storage
        * Encryption of data at rest enabled
        * Elastic throughput mode
        * General Purpose performance mode
        * Mount targets configured in each Availability Zone in the AWS Region in which
         the file system is created, using an available IPv4 on the specified
         subnet

    The **File systems** page appears with a banner across the top
    showing the status of the file system you created. A link to access the file system
    details page appears in the banner when the file system becomes available.

For more information about file system status, see [Understanding file system status](file-system-state.md "file-system-state.md").
This section describes the process of using the Amazon EFS console to create an
EFS file system with customized settings instead of using the
service-recommended settings. For more information about creating a file system by using
the recommended settings, see [Quick create using the console](#gs-step-two-create-efs-resources "#gs-step-two-create-efs-resources").

Creating an EFS file system with custom settings by using the console is a
four-step process:

- Step 1 – Configure general file system settings, including the storage
  class and throughput mode.
- Step 2 – Configure file system network settings, including the virtual
  private cloud (VPC) and mount targets. For each mount target, set the
  Availability Zone, subnet, IP address, and security groups.
- Step 3 – (Optional) Create a file system policy to control NFS client
  access to the file system.
- Step 4 – Review the file system settings, make any changes, and then create the file
  system.

###### Step 1: Configure file system settings

1.  Sign in to the AWS Management Console and open the Amazon EFS console at
    [https://console.aws.amazon.com/efs/](https://console.aws.amazon.com/efs/ "https://console.aws.amazon.com/efs/").
2.  Choose **Create file system** to open the **Create file
    system** dialog box.
3.  Choose **Customize** to create a customized file system instead
    of creating a file system by using the recommended settings. The **File system
    settings** page opens.
4.  For **General** settings, do the following.
    1. (Optional) Enter a **Name** for the file system.
    2. For **File system type**, **Regional** is selected by default.
       Choose **One Zone** if you want to create a file system that
       stores file system data and metadata redundantly within a single Availability Zone. If
       you choose **One Zone**, choose the
       **Availability Zone** that you want the file system created in, or
       keep the default value.
    3. For **Lifecycle management**, change the lifecycle
       policies, if necessary.
       - **Transition into IA** – Select when to transition files
         into the Infrequent Access (IA) storage class, based on the time
         since they were last accessed in Standard storage.
       - **Transition into Archive** – Select when
         to transition files into the Archive storage class, based on the
         time since they were last accessed in Standard storage.
       - **Transition into Standard** – Select whether to transition
         the file system to the storage class.

       For more information about lifecycle policies, see [Managing storage lifecycle](lifecycle-management-efs.md "lifecycle-management-efs.md").

    4. Amazon EFS uses your AWS Key Management Service (AWS KMS) EFS service key
       (`aws/elasticfilesystem`) to encrypt data at rest by default. To
       choose a different KMS key to use for encryption, expand **Customize
       encryption settings** and choose a key from the list. Or, enter a
       KMS key ID or Amazon Resource Name (ARN) for the KMS key that
       you want to use.

    If you need to create a new key, choose **Create an
    AWS KMS key** to launch the AWS KMS console and create a new key.

    You can turn off encryption of data at rest by clearing the check box.

    You cannot change the encryption setting after the file system is created. For
    more information, see [Data encryption in Amazon EFS](encryption.md "encryption.md").

5.  For **Performance** settings, do the following:
    1.  For **Throughput mode**, the **Elastic** mode is selected by
        default.

            * To use provisioned throughput, choose **Provisioned**, and,
             in **Provisioned Throughput (MiB/s)**, enter the amount of
             throughput to provision for file system requests. The amount of
             **Maximum Read Throughput** is displayed at three times the
             amount of the throughput that you enter.
            * To use bursting throughput, choose **Bursting**.

        After you choose the throughput mode, an estimate of the monthly cost for the
        file system is shown. You can change the throughput mode after the file system
        becomes available.

    For more information about choosing the correct throughput mode for your
    performance needs, see [Throughput modes](performance.md#throughput-modes "performance.md#throughput-modes"). 2. For **Performance mode**, the default is **General
    Purpose**. To change the performance mode, expand **Additional
    settings**, and then choose **Max I/O**.

    You cannot change the performance mode after the file system becomes available.
    For more information, see [Performance modes](performance.md#performancemodes "performance.md#performancemodes").

    ###### Important

    Due to the higher per-operation latencies with Max I/O, we recommend using General Purpose performance mode for all file systems.

6.  (Optional) Add tag key-value pairs to your file system.
7.  Choose **Next** to configure network access for the file system.

###### Step 2: Configure network access

In Step 2, you configure the file system's network settings, including the VPC
and mount targets.

1. Choose the **Virtual Private Cloud (VPC)** where you want EC2 instances to connect to your file system.
   For more information, see [Managing mount targets](accessing-fs.md "accessing-fs.md").
2. For **Mount targets**, you create one or more mount targets for
   your file system. For each mount target, set the following properties:
   - **Availability Zone** – By default, a mount target is configured in
     each Availability Zone in an AWS Region. If you don't want a mount target in
     a particular Availability Zone, choose **Remove** to delete the
     mount target for that zone. Create a mount target in every Availability Zone that
     you plan to access your file system from – there is no cost to do so.
   - **Subnet ID** – Choose from the available subnets in an
     Availability Zone. The default subnet is preselected.
   - **IP address type** – Choose **IPv4 only** to support IPv4 addresses only, **IPv6
     only** to support IPv6 addresses only, or **Dual-stack** to support both IPv4 and IPv6 addresses.
   - **IPv4 or IPv6 address** – If you know the IP address
     where you want to place the mount target, then enter it in the IP address box that
     matches the **IP address type**. If you don't specify
     a value, Amazon EFS selects an unused IP address from the specified subnet.
   - **Security groups** – By default, Amazon EFS chooses the default security
     group for the VPC. To change the security group, delete the assigned group and
     then choose the group from the **Choose security groups** list.
     You can specify one or more security groups for the mount target. For more
     information, see [Using VPC security groups](network-access.md "network-access.md").

3. Choose **Add mount target** to create a mount target for an
   Availability Zone that doesn't have one. If a mount target is configured for each
   Availability Zone, this choice is not available.
4. Choose **Next** to set the file system policy.

###### Step 3: Create a file system policy (optional)

Optionally, you can create a file system policy for your file system. An
EFS file system policy is an IAM resource policy that you use to control NFS
client access to the file system. For more information, see [Using IAM to control access to file
systems](iam-access-control-nfs-efs.md "iam-access-control-nfs-efs.md").

1.  In **Policy options**, you can choose any combination of the
    preconfigured file system policies:

        * **Prevent root access by default** – This option
         removes `ClientRootAccess` from the set of allowed EFS actions.
        * **Enforce read-only access by default** – This option
         removes `ClientWriteAccess` from the set of allowed EFS actions.
        * **Prevent anonymous access** – This option removes
         `ClientMount` from the set of allowed EFS actions.
        * **Enforce in-transit encryption for all clients** –
         This option denies access to unencrypted clients.

    When you choose a preconfigured policy, the policy JSON object is displayed in the
    **Policy editor** pane.

2.  Use **Grant additional permissions** to grant file system
    permissions to additional IAM principals, including another AWS account. Choose
    **Add**, and enter the principal ARN of the entity that you are
    granting permissions to. Then choose the **Permissions** that you
    want to grant. The additional permissions are shown in the **Policy
    editor**.
3.  You can use the **Policy editor** to customize a preconfigured
    policy or to create your own file system policy. When you use the editor, the
    preconfigured policy options become unavailable. To clear the current file system
    policy and start creating a new policy, choose **Clear**.
4.  Choose **Next** to review and create the file system.

###### Step 4: Review and create

1. Review each of the file system configuration groups. You can make changes to each group at
   this time by choosing **Edit**.
2. Choose **Create file system** to create your file system and return to the
   **File systems** page.

A banner across the top shows that the new file system is being created. A link to
access the new file system details page appears in the banner when the file system
becomes available.
When you're using the AWS CLI, you create these resources in order. First, you create a
file system. Then, you can create mount targets and any additional optional tags for the
file system by using corresponding AWS CLI commands.

The following examples use `adminuser` for the `--profile`
parameter values. You must use an appropriate user profile to provide your credentials. For
information, see [Prerequisites to use the AWS CLI](../../../cli/latest/userguide/getting-started-prereqs.md "../../../cli/latest/userguide/getting-started-prereqs.md") in the _AWS Command Line Interface User Guide_.

- To create an encrypted file system with automatic backups enabled, use the Amazon EFS
  `create-file-system` CLI command (the corresponding operation is [CreateFileSystem](API_CreateFileSystem.md "API_CreateFileSystem.md")), as shown
  following.

```
aws efs create-file-system \
--creation-token `creation-token` \
--encrypted \
--backup \
--performance-mode `generalPurpose` \
--throughput-mode `elastic` \
--region `aws-region` \
--tags Key=`key`,Value=`value` Key=`key1`,Value=`value1` \
--profile `adminuser`
```

For example, the following `create-file-system` command creates a file
system using Elastic throughput in the
`us-west-2` AWS Region. The command specifies `MyFirstFS`
as the creation token. For a list of the AWS Regions where you can create an Amazon EFS
file system, see [Amazon EFS endpoints and quotas](../../../general/latest/gr/elasticfilesystem.md "../../../general/latest/gr/elasticfilesystem.md") in
the _Amazon Web Services General Reference_.

```
aws efs create-file-system \
--creation-token MyFirstFS \
--backup \
--encrypted \
--performance-mode generalPurpose \
--throughput-mode elastic \
--region us-west-2 \
--tags Key=Name,Value="Test File System" Key=developer,Value=rhoward \
--profile adminuser
```

After successfully creating the file system, Amazon EFS returns the file system
description as JSON, as shown in the following example.

```
{
    "OwnerId": "123456789abcd",
    "CreationToken": "MyFirstFS",
    "Encrypted": true,
    "FileSystemId": "fs-c7a0456e",
    "CreationTime": 1422823614.0,
    "LifeCycleState": "creating",
    "Name": "Test File System",
    "NumberOfMountTargets": 0,
    "SizeInBytes": {
        "Value": 6144,
        "ValueInIA": 0,
        "ValueInStandard": 6144
        "ValueInArchive": 0
    },
    "PerformanceMode": "generalPurpose",
    "ThroughputMode": "elastic",
    "Tags": [
      {
         "Key": "Name",
         "Value": "Test File System"
      }
   ]
}
```

- The following example creates a file system that uses Bursting
  throughput in the `us-west-2a` Availability Zone by using the
  `availability-zone-name` property.

```
aws efs create-file-system \
--creation-token MyFirstFS \
--availability-zone-name us-west-2a \
--backup \
--encrypted \
--performance-mode generalPurpose \
--throughput-mode bursting \
--region us-west-2 \
--tags Key=Name,Value="Test File System" Key=developer,Value=rhoward \
--profile adminuser
```

After successfully creating the file system, Amazon EFS returns the file system
description as JSON, as shown in the following example.

```
{
    "AvailabilityZoneId": "usw-az1",
    "AvailabilityZoneName": "us-west-2a",
    "OwnerId": "123456789abcd",
    "CreationToken": "MyFirstFS",
    "Encrypted": true,
    "FileSystemId": "fs-c7a0456e",
    "CreationTime": 1422823614.0,
    "LifeCycleState": "creating",
    "Name": "Test File System",
    "NumberOfMountTargets": 0,
    "SizeInBytes": {
        "Value": 6144,
        "ValueInIA": 0,
        "ValueInStandard": 6144
        "ValueInArchive": 0
    },
    "PerformanceMode": "generalPurpose",
    "ThroughputMode": "bursting",
    "Tags": [
      {
         "Key": "Name",
         "Value": "Test File System"
      }
   ]
}
```

Amazon EFS also provides the `describe-file-systems` CLI command (the
corresponding API operation is [DescribeFileSystems](API_DescribeFileSystems.md "API_DescribeFileSystems.md")), which you can use to retrieve a list of
file systems in your account, as shown following.

```
aws efs describe-file-systems \
--region `aws-region` \
--profile adminuser
```

Amazon EFS returns a list of the file systems in your AWS account created in the
specified Region.
