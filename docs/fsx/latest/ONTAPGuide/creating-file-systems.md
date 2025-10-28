# Creating file systems

This section describes how to create an FSx for ONTAP file system using the Amazon FSx console, AWS CLI, or the
Amazon FSx API. You can create a file system in a virtual private cloud (VPC) that you own, or in a VPC that
another AWS account has shared with you. There are considerations when creating a Multi-AZ file system in a
VPC in which you are a participant. These considerations are explained in this topic.

By default, when you create a new file system from the Amazon FSx console, Amazon FSx
automatically creates a file system with a single storage virtual machine (SVM) and
one volume, allowing for quick access to data from Linux instances over the Network
File System (NFS) protocol. When creating the file system, you can optionally join
the SVM to an Active Directory to enable access from Windows and macOS clients over
the Server Message Block (SMB) protocol. After your file system is created, you can
create additional SVMs and volumes as needed.

This procedure uses the **Standard create** creation
option to create an FSx for ONTAP file system with a configuration that you
customize for your needs. For information about using the **Quick
create** creation option to rapidly create a file system with a
default set of configuration parameters, see [Create an Amazon FSx for NetApp ONTAP file
system](getting-started.md#getting-started-step1 "getting-started.md#getting-started-step1").

1.  Open the Amazon FSx console at [https://console.aws.amazon.com/fsx/](https://console.aws.amazon.com/fsx/ "https://console.aws.amazon.com/fsx/").
2.  On the dashboard, choose **Create file system**.
3.  On the **Select file system type** page, for
    **File system options**, choose
    **Amazon FSx for NetApp ONTAP**, and then choose
    **Next**.
4.  In the **Creation method** section, choose
    **Standard create**.
5.  In the **File system details** section, provide the
    following information:
    - For **File system name - optional**, enter a name
      for your file system. It's easier to find and manage your file
      systems when you name them. You can use a maximum of 256 Unicode
      letters, white space, and numbers, plus these special characters: +
    * = . \_ : /
    - For **Deployment type** choose
      **Multi-AZ 2**, **Single-AZ 2**,
      **Multi-AZ 1**, or **Single-AZ 1**.
      - **Multi-AZ** file systems replicate your
        data and support failover across multiple Availability Zones
        in the same AWS Region. Multi-AZ 1 is a first-generation FSx for ONTAP file system.
        Multi-AZ 2 is a second-generation file system. They both support one high-availability (HA) pair.
      - **Single-AZ** file systems replicate your
        data and offer automatic failover within a single
        Availability Zone. Single-AZ 1 is a first-generation FSx for ONTAP file system that supports one
        HA pair. Single-AZ 2 is a second-generation file system that supports up to 12 HA pairs.
        For more information, see
        [Managing high-availability (HA) pairs](HA-pairs.md "HA-pairs.md").

      For more information about deployment types, see [Availability, durability, and deployment options](high-availability-AZ.md "high-availability-AZ.md").

      ###### Note

      You can't change your file system's deployment type after creation. If you want to change
      the deployment type (for example, to move from Single-AZ 1 to Single-AZ 2), you can back up your data and restore
      it on a new file system. You can also migrate your data with NetApp SnapMirror, with
      AWS DataSync, or with a third-party data copying tool.
      For more information, see [Migrating to FSx for ONTAP using NetApp SnapMirror](migrating-fsx-ontap-snapmirror.md "migrating-fsx-ontap-snapmirror.md") and
      [Migrating to FSx for ONTAP using
      AWS DataSync](migrate-files-to-fsx-datasync.md "migrate-files-to-fsx-datasync.md").

    - For **SSD storage capacity**, enter the storage
      capacity of your file system, in gibibytes (GiB). Enter any whole
      number in the range of 1,024–1,048,576 GiB (up to 1 pebibyte [PiB]).

    You can increase the amount of storage capacity as needed at any
    time after you create the file system. For more information, see
    [Managing storage capacity](managing-storage-capacity.md "managing-storage-capacity.md").
    - For **Provisioned SSD IOPS**, you have two
      options to provision the number of IOPS for your file system:
      - Choose **Automatic** (the default) if you
        want Amazon FSx to automatically provision 3 IOPS per GiB of SSD
        storage.
      - Choose **User-provisioned** if you want
        to specify the number of IOPS. You can provision a maximum
        of 200,000 SSD IOPS per file system.

    ###### Note

    You can increase your provisioned SSD IOPS after you create the file system.
    Keep in mind that the maximum level of SSD IOPS your file system can achieve is also
    dictated by your file system's throughput capacity even when provisioning additional
    SSD IOPS. For more information, see [Impact of throughput capacity on
    performance](performance.md#impact-throughput-cap-performance "performance.md#impact-throughput-cap-performance") and [Managing storage capacity](managing-storage-capacity.md "managing-storage-capacity.md").
    - For **Throughput capacity**, you have two
      options for determining your throughput capacity in
      megabytes per second (MBps):

          + Choose **Recommended throughput capacity** if you want Amazon FSx
           to automatically choose the throughput capacity based on the amount of storage capacity
           that you chose.
          + Choose **Specify throughput capacity** if you want to specify the amount of
           throughput capacity. If you choose this option, a **Throughput capacity** dropdown
           appears and is populated based on the deployment type that you chose. You can also choose the number of HA
           pairs (up to 12). For more information, see
           [Managing high-availability (HA) pairs](HA-pairs.md "HA-pairs.md").

      Throughput capacity is the sustained speed at which the file server that hosts your file system can serve data. For more information, see [Amazon FSx for NetApp ONTAP performance](performance.md "performance.md").

6.  In the **Networking** section, provide the following information:
    - For **Virtual Private Cloud (VPC)**, choose the VPC
      that you want to associate with your file system.
    - For **VPC Security Groups**, you can choose a security group to
      associate with your file system's network interface. If you don't specify one, Amazon FSx
      will associate the VPC's default security group with your file system.
    - (Multi-AZ only) For **Preferred subnet**, choose any value from the
      list of available subnets. Also choose a **Standby subnet** for the standby
      file server.
    - (Single-AZ only) For **Subnet**, choose any value from the
      list of available subnets.
    - (Multi-AZ only) For **VPC route tables**,
      specify the VPC route tables to create your file system's
      endpoints. Select all VPC route tables associated with the subnets
      in which your clients are located. By default, Amazon FSx selects your
      VPC's default route table. For more information, see
      [Accessing data from outside the
      deployment VPC](supported-fsx-clients.md#access-from-outside-deployment-vpc "supported-fsx-clients.md#access-from-outside-deployment-vpc").

    ###### Note

    Amazon FSx manages these route tables for Multi-AZ file systems using tag-based authentication.
    These route tables are tagged with `Key: AmazonFSx; Value: ManagedByAmazonFSx`.
    When creating FSx for ONTAP Multi-AZ file systems using AWS CloudFormation we recommend that you add the
    `Key: AmazonFSx; Value: ManagedByAmazonFSx` tag manually.
    - For **Network type**, select either **IPv4**
      (for only IPv4 support) or **Dual-stack** (for both IPv4
      and IPv6 support). You can change the network type of an existing file system
      at any time. For more information, see [Changing network type](manage-network-type.md#change-network-type "manage-network-type.md#change-network-type").

    ###### Note

    If you intend to create an FSx for ONTAP file system that uses dual-stack mode, you must first assign an
    Amazon-provided IPv6 CIDR block to your VPC and subnets. For more information, see [Add IPv6 support for your VPC](../../../vpc/latest/userguide/vpc-migrate-ipv6-add.md "../../../vpc/latest/userguide/vpc-migrate-ipv6-add.md") in the
    _Amazon Virtual Private Cloud User Guide_.
    - (Multi-AZ only) **Endpoint IPv4 address range**
      specifies the IPv4 address range in which the endpoints to access your
      file system are created.

    You have three options for the endpoint IPv4 address range:

        + **Unallocated IPv4 address range from your
         VPC** – Amazon FSx chooses the last 64 IP
         addresses from the VPC’s primary CIDR range to use as the
         endpoint IPv4 address range for the file system. This range is
         shared across multiple file systems if you choose this
         option multiple times.


        ###### Note

        This option is grayed out if any of the last 64 IP addresses
         in a VPC's primary CIDR range are in use by a subnet. In this case,
         you can still choose an in-VPC address range (that is, a range that's
         not at the end of your primary CIDR range or a range that's in a secondary
         CIDR of your VPC) by choosing the **Enter an IP address range**
         option.
        + **Floating IPv4 address range outside your VPC** – Amazon FSx
         chooses a 198.19.x.0/24 address range that isn't already used by any other
         file systems with the same VPC and route tables.
        + **Enter an IPv4 address range** – You can provide
         a CIDR range of your own choosing. The IPv4 address range that you choose can
         either be inside or outside the VPC’s IP address range, as long as it doesn't
         overlap with any subnet.


        ###### Note

        Do not choose any range that falls within the
         following CIDR ranges, as they are incompatible with
         FSx for ONTAP:



        	- 0.0.0.0/8
        	- 127.0.0.0/8
        	- 198.19.0.0/20
        	- 224.0.0.0/4
        	- 240.0.0.0/4
        	- 255.255.255.255/32

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

7.  In the **Encryption** section, for
    **Encryption key**, choose the AWS Key Management Service
    (AWS KMS) encryption key that protects your file system's data at
    rest.
8.  For **File system administrative password**,
    enter a secure password for the `fsxadmin` user. Confirm
    the password.

You can use the `fsxadmin` user to administer your file
system using the ONTAP CLI and REST API. For more information about
the `fsxadmin` user, see [Managing file systems with the ONTAP CLI](managing-resources-ontap-apps.md#fsxadmin-ontap-cli "managing-resources-ontap-apps.md#fsxadmin-ontap-cli"). 9. In the **Default storage virtual machine
configuration** section, provide the following
information:

    * In the **Storage virtual machine name**
     field, provide a name for the storage virtual machine. You
     can use a maximum of 47 alphanumeric characters, plus the
     underscore (\_) special character.
    * For **SVM administrative password**, you
     can optionally choose **Specify a
     password** and provide a password for the
     SVM's `vsadmin` user. You can use the
     `vsadmin` user to administer the SVM using
     the ONTAP CLI or REST API. For more information about the
     `vsadmin` user, see [Managing SVMs with the ONTAP CLI](managing-resources-ontap-apps.md#vsadmin-ontap-cli "managing-resources-ontap-apps.md#vsadmin-ontap-cli").


    If you choose **Don't specify a
     password** (the default), you can still use the
     file system's `fsxadmin` user to manage your
     file system using the ONTAP CLI or REST API, but you can't
     use your SVM's `vsadmin` user to do the
     same.
    * For **Volume security style**, choose between
     **Unix (Linux)** and  **NTFS** for
     the volume. For more information, see [Volume security style](managing-volumes.md#volume-security-style "managing-volumes.md#volume-security-style").
    * In the **Active Directory** section, you
     can join an Active Directory to the SVM. For more information,
     see [Working with Microsoft Active Directory
     in FSx for ONTAP](ad-integration-ontap.md "ad-integration-ontap.md").


    If you don't want to join your SVM to an Active
     Directory, choose **Do not join an Active
     Directory**.


    If you want to join your SVM to a self-managed Active
     Directory domain, choose **Join an Active
     Directory**, and provide the following details
     for your Active Directory:




    	+ The NetBIOS name of the Active Directory computer
    	 object to create for your SVM. The NetBIOS name
    	 cannot exceed 15 characters.
    	+ The fully qualified domain name of your Active
    	 Directory. The domain name cannot exceed 255
    	 characters.
    	+ **DNS server IP addresses**
    	 – The IPv4 or IPv6 addresses of the Domain Name
    	 System (DNS) servers for your domain.
    	+ **Service account username**
    	 – The user name of the service account in
    	 your existing Active Directory. Do not include a
    	 domain prefix or suffix.
    	+ **Service account password**
    	 – The password for the service
    	 account.
    	+ **Confirm password** – The
    	 password for the service account.
    	+ (Optional) **Organizational Unit
    	 (OU)** – The distinguished path
    	 name of the organizational unit to which you want to
    	 join your file system.
    	+ **Delegated file system
    	 administrators group** – The name of the group
    	 in your Active Directory that can administer your file system.


    	If you are using AWS Managed Microsoft AD, you need to specify a group such as AWS Delegated FSx Administrators, AWS
    	 Delegated Administrators, or a custom group with delegated permissions to the OU.


    	If you are joining to a self-managed AD,
    	 use the name of the group in your AD. The default group is
    	 `Domain Admins`.

10. In the **Default volume configuration** section, provide the following information
    for the default volume that is created with your file system:
    - In the **Volume name** field, provide a name for
      the volume. You can use up to 203 alphanumeric or underscore (\_)
      characters.
    - (File systems with one HA pair only) For **Volume style**,
      choose either **FlexVol** or **FlexGroup**.
      FlexVol volumes are general-purpose volumes that can be up to 300 tebibytes (TiB) in size. FlexGroup
      volumes are intended for high-performance workloads and can be up to 20 PiB in size.
    - For **Volume size**, enter any whole number
      in the range of 20–314,572,800 mebibytes (MiB) for FlexVol volumes or
      800 gibibytes (GiB)–2,400 TiB per HA pair for FlexGroup volumes. For example, a file system with 12 HA pairs
      would have a minimum volume size of 9,600 GiB
      and a maximum size of 20,480 TiB.
    - For **Volume type**, choose **Read-Write (RW)**
      to create a volume that is readable and writable
      or **Data Protection (DP)** to create a volume that
      is read-only and can be used as the destination of a NetApp SnapMirror
      or SnapVault relationship. For more information,
      see [Volume types](managing-volumes.md#volume-types "managing-volumes.md#volume-types").
    - For **Junction path**, enter a location within
      the file system to mount the volume. The name must have a leading
      forward slash, for example `/vol3`.
    - For **Storage efficiency**, choose
      **Enabled** to enable the ONTAP
      storage-efficiency features (deduplication, compression, and
      compaction). For more information,
      see [Storage efficiency](managing-storage-capacity.md#storage-efficiency "managing-storage-capacity.md#storage-efficiency").
    - For **Snapshot policy**, choose a snapshot policy for the volume.
      For more information about snapshot policies, see [Snapshot policies](snapshots-ontap.md#snapshot-policies "snapshots-ontap.md#snapshot-policies").

    If you choose **Custom policy**, you must specify the policy's name in the
    **custom-policy** field. The custom policy must already exist on the SVM or in the file system. You can create
    a custom snapshot policy with the ONTAP CLI or REST API. For more information, see
    [Create a Snapshot Policy](https://docs.netapp.com/us-en/ontap/data-protection/create-snapshot-policy-task.html "https://docs.netapp.com/us-en/ontap/data-protection/create-snapshot-policy-task.html")
    in the NetApp ONTAP Product Documentation.

11. In the **Default volume storage tiering** section, for **Capacity pool tiering policy**,
    choose the storage pool tiering policy for the volume, which can be **Auto** (the default),
    **Snapshot Only**, **All**, or **None**.
    For more information about capacity pool tiering policies, see
    [Volume tiering policies](volume-storage-capacity.md#data-tiering-policy "volume-storage-capacity.md#data-tiering-policy").

For **Tiering policy cooling period**, if you have set storage tiering to
either `Auto` and `Snapshot-only` policies.valid values are 2-183 days. A volume's tiering policy cooling period
defines the number of days before data that has not been accessed is marked cold and moved to capacity pool storage. 12. In the **Default Volume SnapLock Configuration**
section, for **SnapLock Configuration**,
choose between **Enabled** and
**Disabled**. For more information about configuring a
SnapLock Compliance volume or a SnapLock Enterprise volume, see [Understanding SnapLock Compliance](snaplock-compliance.md "snaplock-compliance.md")
and [Understanding SnapLock Enterprise](snaplock-enterprise.md "snaplock-enterprise.md"). For more information about SnapLock, see
[Protecting your data with SnapLock](snaplock.md "snaplock.md"). 13. In **Backup and maintenance -
_optional_**, you can set the
following options:

    * For **Daily automatic backup**, choose
     **Enabled** for automatic daily
     backups. This option is enabled by default.
    * For **Daily automatic backup window**,
     set the time of the day in Coordinated Universal Time (UTC)
     that you want the daily automatic backup window to start.
     The window is 30 minutes starting from this specified time.
     This window can't overlap with the weekly maintenance backup
     window.
    * For **Automatic backup retention
     period**, set a period from 1–90 days that
     you want to retain automatic backups.
    * For **Weekly maintenance window**, you
     can set the time of the week that you want the maintenance
     window to start. Day 1 is Monday, 2 is Tuesday, and so on.
     The window is 30 minutes starting from this specified time.
     This window can't overlap with the daily automatic backup
     window.

14. For **Tags - _optional_**, you can enter a key and value
    to add tags to your file system. A tag is a case-sensitive key-value
    pair that helps you manage, filter, and search for your file
    system.

Choose **Next**. 15. Review the file system configuration shown on the **Create
file system** page. For your reference, note which file
system settings you can modify after the file system is
created. 16. Choose **Create file system**.

- To create an FSx for ONTAP file system, use the [create-file-system](../../../cli/latest/reference/fsx/create-file-system.md "../../../cli/latest/reference/fsx/create-file-system.md") CLI command (or the equivalent
  [CreateFileSystem](../APIReference/API_CreateFileSystem.md "../APIReference/API_CreateFileSystem.md") API operation), as shown in the
  following example.

###### Note

You can't change your file system's deployment type after creation. If you want to change
the deployment type (for example, to move from Single-AZ 1 to Single-AZ 2), you can back up your data and restore
it on a new file system. You can also migrate your data with NetApp SnapMirror, with
AWS DataSync, or with a third-party data copying tool.
For more information, see [Migrating to FSx for ONTAP using NetApp SnapMirror](migrating-fsx-ontap-snapmirror.md "migrating-fsx-ontap-snapmirror.md") and
[Migrating to FSx for ONTAP using
AWS DataSync](migrate-files-to-fsx-datasync.md "migrate-files-to-fsx-datasync.md").

```
`aws fsx create-file-system \
 --file-system-type ONTAP \
 --storage-capacity 1024 \
 --storage-type SSD \
 --security-group-ids `security-group-id` \

 --subnet-ids subnet-abcdef1234567890b subnet-abcdef1234567890c \
 --ontap-configuration DeploymentType=MULTI_AZ_1,
 ThroughputCapacity=512,PreferredSubnetId=subnet-abcdef1234567890b`
```

After successfully creating the file system, Amazon FSx returns the file
system's description in JSON format as shown in the following example.

```
`{
 "FileSystem": {
 "OwnerId": "111122223333",
 "CreationTime": 1625066825.306,
 "FileSystemId": "fs-0123456789abcdef0",
 "FileSystemType": "ONTAP",
 "Lifecycle": "CREATING",
 "StorageCapacity": 1024,
 "StorageType": "SSD",
 "VpcId": "vpc-11223344556677aab",
 "SubnetIds": [
 "subnet-abcdef1234567890b",
 "subnet-abcdef1234567890c"
 ],
 "KmsKeyId": "arn:aws:kms:us-east-1:111122223333:key/wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
 "ResourceARN": "arn:aws:fsx:us-east-1:111122223333:file-system/fs-0123456789abcdef0",
 "Tags": [],
 "OntapConfiguration": {
 "DeploymentType": "MULTI_AZ_HA_1",
 "EndpointIpAddressRange": "198.19.0.0/24",
 "Endpoints": {
 "Management": {
 "DnsName": "management.fs-0123456789abcdef0.fsx.us-east-1.amazonaws.com"
 },
 "Intercluster": {
 "DnsName": "intercluster.fs-0123456789abcdef0.fsx.us-east-1.amazonaws.com"
 }
 },
 "DiskIopsConfiguration": {
 "Mode": "AUTOMATIC",
 "Iops": 3072
 },
 "PreferredSubnetId": "subnet-abcdef1234567890b",
 "RouteTableIds": [
 "rtb-abcdef1234567890e",
 "rtb-abcd1234ef567890b"
 ],
 "ThroughputCapacity": 512,
 "WeeklyMaintenanceStartTime": "4:10:00"
 }
 }
}`
```

###### Note

Unlike the process of creating a file system in the console, the
`create-file-system` CLI command and the
`CreateFileSystem` API operation don't create a default SVM
or volume. To create an SVM, see [Creating storage virtual machines (SVM)](creating-svms.md "creating-svms.md"); to create a volume, see [Creating volumes](creating-volumes.md "creating-volumes.md").

## Creating FSx for ONTAP file systems in shared subnets

VPC sharing enables multiple AWS accounts to create resources into shared, centrally-managed virtual private clouds (VPCs).
In this model, the account that owns the VPC (owner) shares one or more subnets with other accounts (participants) that
belong to the same organization from AWS Organizations.

Participant accounts can create FSx for ONTAP Single-AZ and Multi-AZ file systems in a VPC subnet
that the owner account has shared with them. For a participant account to create a Multi-AZ file system,
the owner account also needs to grant Amazon FSx permission to modify
route tables in the shared subnets on behalf of the participant account. For more information, see
[Managing shared VPC support for Multi-AZ file systems](#maz-shared-vpc "#maz-shared-vpc").

###### Note

It is the participant account’s responsibility to coordinate with the VPC owner to prevent the creation of
any subsequent VPC subnets that will overlap with the in-VPC CIDR of the participant's file systems.
If subnets do overlap, traffic to the file system can get interrupted.

### Shared subnet requirements and considerations

When creating FSx for ONTAP file systems into shared subnets, note the following:

- The owner of the VPC subnet must share a subnet with a participant account before that
  account can create an FSx for ONTAP file system in it.
- You can't launch resources using the default security group for the VPC because it
  belongs to the owner. Additionally, participant accounts can't launch resources using security groups that
  are owned by other participants or the owner.
- In a shared subnet, the participant and the owner separately controls the security groups
  within each respective account. The owner account can see security groups that are created by the participants,
  but cannot perform any actions on them. If the owner account wants to remove or modify these security groups,
  the participant that created the security group must take the action.
- Participant accounts can view, create, modify, and delete Single-AZ file
  systems and their associated resources in subnets that the owner account has shared with them.
- Participant accounts can create, view, modify, and delete Multi-AZ file
  systems and their associated resources in subnets that the owner account has shared with them. Additionally,
  the owner account must also grant the Amazon FSx service permissions to modify route tables in the
  shared subnets on behalf of the participants account. For more information, see
  [Managing shared VPC support for Multi-AZ file systems](#maz-shared-vpc "#maz-shared-vpc")
- The shared VPC owner cannot view, modify, or delete resources
  that a participant creates in the shared subnet. This is in addition to the VPC resources that each
  account has different access to. For more information, see
  [Responsibilities and permissions for owners and participants](../../../vpc/latest/userguide/vpc-sharing.md#vpc-share-limitations "../../../vpc/latest/userguide/vpc-sharing.md#vpc-share-limitations")
  in the Amazon VPC User Guide.

For more information, see [Share your VPC with other accounts](../../../vpc/latest/userguide/vpc-sharing.md "../../../vpc/latest/userguide/vpc-sharing.md")
in the Amazon VPC User Guide.

#### When sharing a VPC subnet

When sharing your subnets with participant accounts that will be creating FSx for ONTAP file systems in the shared subnets,
you will need to do the following:

- The VPC owner needs to use AWS Resource Access Manager to securely share VPCs and subnets with other AWS accounts. For more information, see
  [Sharing your AWS resources](../../../ram/latest/userguide/getting-started-sharing.md#getting-started-sharing-orgs "../../../ram/latest/userguide/getting-started-sharing.md#getting-started-sharing-orgs") in the AWS Resource Access Manager User Guide.
- The VPC owner needs to share one or more VPCs with a participant account. For more information, see
  [Share your VPC with other accounts](../../../vpc/latest/userguide/vpc-sharing.md "../../../vpc/latest/userguide/vpc-sharing.md")
  in the Amazon Virtual Private Cloud User Guide.
- For participant accounts to create FSx for ONTAP Multi-AZ file systems, the VPC owner must also grant the Amazon FSx
  service permissions to create and modify route tables in the shared subnets on behalf of the participant accounts.
  This is because FSx for ONTAP Multi-AZ file systems use floating IP addresses so that connected clients can
  seamlessly transition between the preferred and standby file servers during a failover event.
  When a failover event occurs, Amazon FSx updates all routes in all route tables associated with
  the file system to point to the currently active file server.

#### Managing shared VPC support for Multi-AZ file systems

Owner accounts can manage whether or not participant accounts can create Multi-AZ FSx for ONTAP file systems in VPC subnets that
the owner has shared with participants using the AWS Management Console, AWS CLI, and API, as described in the following sections.

###### To manage VPC sharing for Multi-AZ file systems (console)

Open the Amazon FSx console at [https://console.aws.amazon.com/fsx/](https://console.aws.amazon.com/fsx/ "https://console.aws.amazon.com/fsx/").

1. In the navigation pane, choose **Settings**.
2. Locate the **Multi-AZ shared VPC settings** on the **Settings** page.
   - To enable VPC sharing for Multi-AZ file systems in VPC subnets that you share, choose
     **Enable route table updates from participant accounts**.
   - To disable VPC sharing for Multi-AZ file systems in all VPCs that you own, choose
     **Disable route table updates from participant accounts**. The confirmation screen is
     displayed.

###### Important

We strongly recommend that participant-created Multi-AZ file systems in the shared VPC
are deleted before you disable this feature. Once the feature is disabled, these file systems will enter
a `MISCONFIGURED` state and will be at risk of becoming unavailable. 3. Enter `confirm` and choose **Confirm** to disable the
feature.

###### To manage VPC sharing for Multi-AZ file systems (AWS CLI)

1. To view the current setting for Multi-AZ VPC sharing, use the
   [describe-shared-vpc-configuration](../../../cli/latest/reference/fsx/describe-shared-vpc-configuration.md "../../../cli/latest/reference/fsx/describe-shared-vpc-configuration.md")
   CLI command, or the equivalent
   [DescribeSharedVpcConfiguration](../APIReference/API_DescribeSharedVpcConfiguration.md "../APIReference/API_DescribeSharedVpcConfiguration.md") API command,
   shown as follows:

```
`$` `aws fsx describe-shared-vpc-configuration`
```

The service responds to a successful request as follows:

```
`{
 "EnableFsxRouteTableUpdatesFromParticipantAccounts": "false"
}`
```

2. To manage the Multi-AZ shared VPC configuration, use the
   [update-shared-vpc-configuration](../../../cli/latest/reference/fsx/update-shared-vpc-configuration.md "../../../cli/latest/reference/fsx/update-shared-vpc-configuration.md")
   CLI command, or the equivalent
   [UpdateSharedVpcConfiguration](../APIReference/API_UpdateSharedVpcConfiguration.md "../APIReference/API_UpdateSharedVpcConfiguration.md") API command.
   The following example enables VPC sharing for Multi-AZ file systems.

```
`$` `aws fsx update-shared-vpc-configuration --enable-fsx-route-table-updates-from-participant-accounts true`
```

The service responds to a successful request as follows:

```
`{
 "EnableFsxRouteTableUpdatesFromParticipantAccounts": "true"
}`
```

3. To disable the feature, set `EnableFsxRouteTableUpdatesFromParticipantAccounts` to `false`, as shown in the following example.

```
`$` `aws fsx update-shared-vpc-configuration --enable-fsx-route-table-updates-from-participant-accounts false`
```

The service responds to a successful request as follows:

```
`{
 "EnableFsxRouteTableUpdatesFromParticipantAccounts": "false"
}`
```
