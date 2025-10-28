# Provisioning NVMe/TCP for Linux

FSx for ONTAP supports the Non-Volatile Memory Express over TCP (NVMe/TCP) block storage protocol. With NVMe/TCP,
you use the ONTAP CLI to provision namespaces and subsystems and then map the namespaces to subsystems,
similar to the way LUNs are provisioned and mapped to initiator groups (igroups) for iSCSI.
The NVMe/TCP protocol is available on second-generation file systems that have 6 or fewer
[high-availability (HA) pairs](HA-pairs.md "HA-pairs.md").

###### Note

FSx for ONTAP file systems use an SVM's iSCSI endpoints for both iSCSI and NVMe/TCP block storage
protocols.

There are three main steps to process of configuring NVMe/TCP on your Amazon FSx for NetApp ONTAP, which are covered in the following procedures:

1. Install and configure the NVMe client on the Linux host.
2. Configure NVMe on the file system's SVM.
   - Create an NVMe namespace.
   - Create an NVMe subsystem.
   - Map the namespace to the subsystem.
   - Add the client NQN to the subsystem.

3. Mount an NVMe device on the Linux client.

## Before you begin

Before you begin the process of configuring your file system for NVMe/TCP, you need to have the
following items completed.

- Create an FSx for ONTAP file system.
  For more information, see [Creating file systems](creating-file-systems.md "creating-file-systems.md").
- Create an EC2 instance running Red Hat Enterprise Linux (RHEL) 9.3 in the same VPC as the file system.
  This is the Linux host on which you will configure NVMe and access your file data using NVMe/TCP for Linux.

Beyond the scope of these procedures, if the host is located in another VPC, you
can use VPC peering or AWS Transit Gateway to grant other VPCs access to the volume's iSCSI
endpoints. For more information, see
[Accessing data from outside the
deployment VPC](supported-fsx-clients.md#access-from-outside-deployment-vpc "supported-fsx-clients.md#access-from-outside-deployment-vpc").

- Configure the Linux host's VPC security groups to allow inbound and
  outbound traffic as described in [File System Access Control with Amazon VPC](limit-access-security-groups.md "limit-access-security-groups.md").
- Obtain the credentials for the ONTAP user with `fsxadmin` privileges
  that you will use to access the ONTAP CLI. For more information, see
  [ONTAP roles and users](roles-and-users.md "roles-and-users.md").
- The Linux host that you will configure for NVMe and use to access the FSx for ONTAP file system are located in
  the same VPC and AWS account.
- We recommend that the EC2 instance be in the same availability zone
  as your file system's preferred subnet.

If your EC2 instance runs a different Linux AMI than RHEL 9.3, some of the utilities used
in these procedures and examples might already be installed, and you might use different commands to
install required packages. Aside from installing packages, the commands used in this section
are valid for other EC2 Linux AMIs.

###### Topics

- [Install and configure NVMe on the Linux host](#configure-nvme-on-rhel93 "#configure-nvme-on-rhel93")
- [Configure NVMe on the FSx for ONTAP file system](#configure-nvme-on-svm "#configure-nvme-on-svm")
- [Mount an NVMe device on your Linux client](#add-nvme-on-rhel93-host "#add-nvme-on-rhel93-host")

## Install and configure NVMe on the Linux host

###### To install the NVMe client

1. Connect to your Linux instance using an SSH client. For more information, see
   [Connect to your Linux instance from Linux or macOS using SSH](../../../AWSEC2/latest/UserGuide/connect-linux-inst-ssh.md "../../../AWSEC2/latest/UserGuide/connect-linux-inst-ssh.md").
2. Install `nvme-cli` using the following command:

```
`~$` sudo yum install -y nvme-cli
```

3. Load the `nvme-tcp` module onto the host:

```
`$` `sudo modprobe nvme-tcp`
```

4. Get the Linux host's NVMe Qualified Name (NQN) by using the following command:

```
`$` `cat /etc/nvme/hostnqn`
`nqn.2014-08.org.nvmexpress:uuid:9ed5b327-b9fc-4cf5-97b3-1b5d986345d1`
```

Record the response for use in a later step.

## Configure NVMe on the FSx for ONTAP file system

###### To configure NVMe on the file system

Connect to the NetApp ONTAP CLI on the FSx for ONTAP file system on which you plan to create the NVMe device(s).

1. To access the ONTAP CLI, establish an SSH session on the management port of the
   Amazon FSx for NetApp ONTAP file system or SVM by running the following command. Replace
   `management_endpoint_ip` with the IP address of the file system's
   management port.

```
`[~]$` `ssh fsxadmin@`management_endpoint_ip``
```

For more information, see [Managing file systems with the ONTAP CLI](managing-resources-ontap-apps.md#fsxadmin-ontap-cli "managing-resources-ontap-apps.md#fsxadmin-ontap-cli"). 2. Create a new volume on the SVM that you are using to access the NVMe interface.

```
`::>` `vol create -vserver fsx -volume nvme_vol1 -aggregate aggr1 -size 1t`
     `[Job 597] Job succeeded: Successful`
```

3. Create the NVMe namespace `ns_1` using the
   [`vserver nvme namespace create`](https://docs.netapp.com/us-en/ontap-cli-9141/vserver-nvme-namespace-create.html "https://docs.netapp.com/us-en/ontap-cli-9141/vserver-nvme-namespace-create.html")
   NetApp ONTAP CLI command. A namespace maps to initiators (clients) and controls which initiators (clients) have access to
   NVMe devices.

```
`::>` `vserver nvme namespace create -vserver fsx -path /vol/nvme_vol1/ns_1 -size 100g -ostype linux`
`Created a namespace of size 100GB (107374182400).`
```

4. Create the NVMe subsystem using the
   [`vserver nvme subsystem create`](https://docs.netapp.com/us-en/ontap-cli-9141/vserver-nvme-subsystem-create.html "https://docs.netapp.com/us-en/ontap-cli-9141/vserver-nvme-subsystem-create.html")
   NetApp ONTAP CLI command.

```
`~$` `vserver nvme subsystem create -vserver fsx -subsystem sub_1 -ostype linux`
```

5. Map the namespace to the subsystem you just created.

```
`::>` `vserver nvme subsystem map add -vserver fsx -subsystem sub_1 -path /vol/nvme_vol1/ns_1`
```

6. Add the client to the subsystem using the NQN that you retrieved previously.

```
`::>` `vserver nvme subsystem host add -subsystem sub_1 -host-nqn nqn.2014-08.org.nvmexpress:uuid:ec21b083-1860-d690-1f29-44528e4f4e0e -vserver fsx`
```

If you want to make the devices mapped to this subsystem available to multiple hosts,
you can specify multiple initiator names in a comma separated list. For more information, see
[vserver nvme subsystem host add](https://docs.netapp.com/us-en/ontap-cli-9141/vserver-nvme-subsystem-host-add.html "https://docs.netapp.com/us-en/ontap-cli-9141/vserver-nvme-subsystem-host-add.html")
in the NetApp ONTAP Docs. 7. Confirm that the namespace exists using the
[**vserver nvme namespace show**](https://docs.netapp.com/us-en/ontap-cli-9141/vserver-nvme-namespace-show.html "https://docs.netapp.com/us-en/ontap-cli-9141/vserver-nvme-namespace-show.html")
command:

```
`::>` `vserver nvme namespace show -vserver fsx -instance`
`Vserver Name: fsx
 Namespace Path: /vol/nvme_vol1/ns_1
 Size: 100GB
 Size Used: 90.59GB
 OS Type: linux
 Comment:
 Block Size: 4KB
 State: online
 Space Reservation: false
Space Reservations Honored: false
 Is Read Only: false
 Creation Time: 5/20/2024 17:03:08
 Namespace UUID: c51793c0-8840-4a77-903a-c869186e74e3
 Vdisk ID: 80d42c6f00000000187cca9
 Restore Inaccessible: false
 Inconsistent Filesystem: false
 Inconsistent Blocks: false
 NVFail: false
Node Hosting the Namespace: FsxId062e9bb6e05143fcb-01
 Volume Name: nvme_vol1
 Qtree Name:
 Mapped Subsystem: sub_1
 Subsystem UUID: db526ec7-16ca-11ef-a612-d320bd5b74a9
 Namespace ID: 00000001h
 ANA Group ID: 00000001h
 Vserver UUID: 656d410a-1460-11ef-a612-d320bd5b74a9
 Vserver ID: 3
 Volume MSID: 2161388655
 Volume DSID: 1029
 Aggregate: aggr1
 Aggregate UUID: cfa8e6ee-145f-11ef-a612-d320bd5b74a9
 Namespace Container State: online
 Autodelete Enabled: false
 Application UUID: -
 Application: -
 Has Metadata Provisioned: true

1 entries were displayed.`
```

8. Use the [**network interface show -vserver**](https://docs.netapp.com/us-en/ontap-cli-9141/network-interface-show.html "https://docs.netapp.com/us-en/ontap-cli-9141/network-interface-show.html") command to retrieve the addresses of the block storage interfaces for the
   SVM in which you've created your NVMe devices.

```
`::>` `network interface show -vserver `svm_name` -data-protocol nvme-tcp`
 `Logical Status Network Current Current Is
Vserver Interface Admin/Oper Address/Mask Node Port Home
----------- ---------- ---------- ------------------ ------------- ------- ----
`svm_name`
 iscsi_1 up/up 172.31.16.19/20 FSxId0123456789abcdef8-01 e0e true
 iscsi_2 up/up 172.31.26.134/20 FSxId0123456789abcdef8-02 e0e true
2 entries were displayed.`
```

###### Note

The `iscsi_1` LIF is used for both iSCSI and NVMe/TCP.

In this example, the IP address of iscsi_1 is 172.31.16.19 and iscsi_2 is 172.31.26.134.

## Mount an NVMe device on your Linux client

The process of mounting the NVMe device on your Linux client involves three steps:

1. Discovering the NVMe nodes
2. Partitioning the NVMe device
3. Mounting the NVMe device on the client

These are covered in the following procedures.

###### To discover the target NVMe nodes

1. On your Linux client, use the following command to discover the target NVMe nodes. Replace
   `iscsi_1_IP` with `iscsi_1`’s IP address, and
   `client_IP` the client's IP address.

###### Note

`iscsi_1` and `iscsi_2` LIFs are used for both iSCSI and NVMe storage.

```
`~$` `sudo nvme discover -t tcp -w `client_IP` -a `iscsi_1_IP``
```

```
`Discovery Log Number of Records 4, Generation counter 11
=====Discovery Log Entry 0======
trtype: tcp
adrfam: ipv4
subtype: current discovery subsystem
treq: not specified
portid: 0
trsvcid: 8009
subnqn: nqn.1992-08.com.netapp:sn.656d410a146011efa612d320bd5b74a9:discovery
traddr: 172.31.26.134
eflags: explicit discovery connections, duplicate discovery information
sectype: none
=====Discovery Log Entry 1======
trtype: tcp
adrfam: ipv4
subtype: current discovery subsystem
treq: not specified
portid: 1
trsvcid: 8009
subnqn: nqn.1992-08.com.netapp:sn.656d410a146011efa612d320bd5b74a9:discovery
traddr: 172.31.16.19
eflags: explicit discovery connections, duplicate discovery information
sectype: none`
```

2. (Optional) To drive higher throughput than the Amazon EC2 single client maximum of 5 Gbps (~625 MBps) to your file NVMe device,
   follow the procedures described in
   [Amazon EC2 instance network bandwidth](../../../AWSEC2/latest/UserGuide/ec2-instance-network-bandwidth.md "../../../AWSEC2/latest/UserGuide/ec2-instance-network-bandwidth.md")
   in the Amazon Elastic Compute Cloud User Guide for Linux Instances to establish additional sessions.
3. Log into the target initiators with a controller loss timeout of at least 1800 seconds, again using
   `iscsi_1`’s IP address for `iscsi_1_IP` and the client's
   IP address for `client_IP`. Your NVMe devices are presented as available disks.

```
`~$` `sudo nvme connect-all -t tcp -w `client_IP` -a `iscsi_1` -l 1800`
```

4. Use the following command to verify that the NVMe stack has identified and merged the multiple sessions and configured multipathing.
   The command returns `Y` if the configuration was successful.

```
`~$` `cat /sys/module/nvme_core/parameters/multipath`
Y
```

5. Use the following commands to verify that the NVMe-oF setting `model` is set to `NetApp ONTAP Controller` and the load balancing
   `iopolicy` is set to `round-robin` for the respective ONTAP namespaces to distribute the I/O on all available paths

```
`~$` `cat /sys/class/nvme-subsystem/nvme-subsys*/model`
`Amazon Elastic Block Store
NetApp ONTAP Controller`
`~$` `cat /sys/class/nvme-subsystem/nvme-subsys*/iopolicy`
`numa
round-robin`
```

6. Use the following command to verify that the namespaces are created and correctly discovered on the host:

```
`~$` `sudo nvme list`
`Node Generic SN Model Namespace Usage Format FW Rev
--------------------- --------------------- -------------------- ---------------------------------------- ---------- -------------------------- ---------------- --------
/dev/nvme0n1 /dev/ng0n1 vol05955547c003f0580 Amazon Elastic Block Store 0x1 25.77 GB / 25.77 GB 512 B + 0 B 1.0
/dev/nvme2n1 /dev/ng2n1 lWB12JWY/XLKAAAAAAAC NetApp ONTAP Controller 0x1 107.37 GB / 107.37 GB 4 KiB + 0 B FFFFFFFF`
```

The new device in the output is `/dev/nvme2n1`. This naming scheme may differ depending on your Linux installation. 7. Verify that the controller state of each path is live and has the correct
Asymmetric Namespace Access (ANA) multipathing status:

```
`~$` `nvme list-subsys /dev/nvme2n1`
`nvme-subsys2 - NQN=nqn.1992-08.com.netapp:sn.656d410a146011efa612d320bd5b74a9:subsystem.rhel
 hostnqn=nqn.2014-08.org.nvmexpress:uuid:ec2a70bf-3ab2-6cb0-f997-8730057ceb24
 iopolicy=round-robin
\
 +- nvme2 tcp traddr=172.31.26.134,trsvcid=4420,host_traddr=172.31.25.143,src_addr=172.31.25.143 live non-optimized
 +- nvme3 tcp traddr=172.31.16.19,trsvcid=4420,host_traddr=172.31.25.143,src_addr=172.31.25.143 live optimized`
```

In this example, the NVMe stack has automatically discovered your file system’s alternate LIF, `iscsi_2`, 172.31.26.134. 8. Verify that the NetApp plug-in displays the correct values for each ONTAP namespace device:

```
`~$` `sudo nvme netapp ontapdevices -o column`
`Device Vserver Namespace Path NSID UUID Size
---------------- ------------------------- -------------------------------------------------- ---- -------------------------------------- ---------
/dev/nvme2n1 fsx /vol/nvme_vol1/ns_1 1 0441c609-3db1-4b0b-aa83-790d0d448ece 107.37GB`
```

###### To partition the device

1. Use the following command to verify that the path to your device_name `nvme2n1` is present.

```
`~$` `ls /dev/mapper/nvme2n1`
`/dev/nvme2n1`
```

2. Partition the disk using `fdisk`. You’ll enter an interactive prompt. Enter the options in the order shown.
   You can make multiple partitions by using a value smaller than the last sector (`20971519` in this example).

###### Note

The `Last sector` value will vary depending on the size of your NVMe device (100 GiB in this example).

```
`~$` `sudo fdisk /dev/mapper/nvme2n1`
```

The `fsdisk` interactive prompt starts.

```
`Welcome to fdisk (util-linux 2.37.4).
Changes will remain in memory only, until you decide to write them.
Be careful before using the write command.

Device does not contain a recognized partition table.
Created a new DOS disklabel with disk identifier 0x66595cb0.

Command (m for help):` `n`
`Partition type
 p primary (0 primary, 0 extended, 4 free)
 e extended (container for logical partitions)
Select (default p):` `p`
`Partition number (1-4, default 1):` `1`
`First sector (256-26214399, default 256):
Last sector, +sectors or +size{K,M,G,T,P} (256-26214399, default 26214399):` `20971519`
 `Created a new partition 1 of type 'Linux' and of size 100 GiB.
Command (m for help):` `w`
`The partition table has been altered.
Calling ioctl() to re-read partition table.
Syncing disks.`
```

After entering `w`, your new partition `/dev/nvme2n1`
becomes available. The `partition_name` has the format `<device_name>``<partition_number>`.
`1` was used as the partition number in the `fdisk` command in the previous step. 3. Create your file system using `/dev/nvme2n1` as the path.

```
`~$` `sudo mkfs.ext4 /dev/nvme2n1`
```

The system responds with the following output:

```
`mke2fs 1.46.5 (30-Dec-2021)
Found a dos partition table in /dev/nvme2n1
Proceed anyway? (y,N)` `y`
`Creating filesystem with 26214400 4k blocks and 6553600 inodes
Filesystem UUID: 372fb2fd-ae0e-4e74-ac06-3eb3eabd55fb
Superblock backups stored on blocks:
 32768, 98304, 163840, 229376, 294912, 819200, 884736, 1605632, 2654208,
 4096000, 7962624, 11239424, 20480000, 23887872

Allocating group tables: done
Writing inode tables: done
Creating journal (131072 blocks): done
Writing superblocks and filesystem accounting information: done`
```

###### To mount the NVMe device on the Linux client

1. Create a directory `directory_path` as the mount point for your file system on the Linux instance.

```
`~$` `sudo mkdir /`directory_path`/`mount_point``
```

2. Mount the file system using the following command.

```
`~$` `sudo mount -t ext4 /dev/nvme2n1 /`directory_path`/`mount_point``
```

3. (Optional) If you want to give a specific user ownership of the mount directory, replace `username`
   with the owner's username.

```
`~$` `sudo chown `username`:`username` /`directory_path`/`mount_point``
```

4. (Optional) Verify that you can read from and write data to the file system.

```
`~$` `echo "Hello world!" > /`directory_path`/`mount_point`/HelloWorld.txt`
`~$` `cat `directory_path`/HelloWorld.txt`
`Hello world!`
```

You have successfully created and mounted an NVMe device on your Linux client.
