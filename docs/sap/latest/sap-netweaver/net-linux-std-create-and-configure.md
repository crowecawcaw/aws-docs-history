# Creating AWS Resources and Configuring the Operating System for SAP NetWeaver Installation

In this scenario, we will provision an Amazon EC2 instance for installing SAP as a standard system; i.e., ABAP System Central Services (ASCS) and Primary Application Server (PAS) will run on one host.

###### Note

In this section, the syntax shown for the AWS CLI and Linux commands is specific to the scope of this document. Each command supports many additional options. For more information, use the AWS CLI `aws help` command or refer to the documentation.

## Step 1. Check the Region Where You Want to Deploy Your AWS Resources

Display the AWS CLI configuration data.

```
  $ aws configure list
```

In the command output, make sure that the default region that’s listed is the same as the target region where you want to deploy your AWS resources and install SAP NetWeaver.

## Step 2. Create a JSON File for the Amazon EBS Storage

Create a JSON file that contains the storage requirements for SAP Install volumes; for example:

```
  [
   {
      "DeviceName": "/dev/sdh",
      "Ebs": {
        "VolumeSize";: 50,
        "VolumeType";: "gp2",
        "DeleteOnTermination": true
     }
   },
   {
      "DeviceName": "/dev/sdg",
      "Ebs": {
        "VolumeSize": 50,
        "VolumeType": "gp2",
        "DeleteOnTermination": true
     }
   }
  ]
```

## Step 3. Launch the Amazon EC2 Instance

Launch the Amazon EC2 instance for the SAP installation in your target region by using the information that you gathered in the preparation phase. You will also be creating the required storage volumes and attaching them to the Amazon EC2 instance for the SAP installation, based on the JSON file that you created in the previous step.

Use the following syntax:

```
  $ aws ec2 run-instances \
  --image-id <AMI-ID> \
  --count <number-of-EC2-instances> \
  --instance-type <instance-type> \
  --key-name=<name-of-key-pair> \
  --security-group-ids <security-group-ID> \
  --subnet-id <subnet-ID> \
  --block-device-mappings file://C:\Users\file.json \
  --region <region-ID>
```

The JSON file is the storage file that you created in [step 2](#net-linux-step-2-create-json-file "#net-linux-step-2-create-json-file").

When using the command, make sure to place the command and its parameters on a single line; for example:

```
  $ aws ec2 run-instances --image-id ami-123456789abcdefgh --count 1 --instance-type m5.large --key-name=my_key --security-group-ids sg-123456789abcdefgh --subnet-id subnet-1234abcd --block-device-mappings file://C:\Users\storage.json
```

## Step 4. Update the Hostname

Log in to your SAP Instance with Secure Shell (SSH) using the private key pair, and switch to root user to update the hostname along with the domain name according to your requirements. For detailed steps, see the AWS Knowledge Center article for your operating system:

- [Amazon EC2 instance running on SLES](https://aws.amazon.com/premiumsupport/knowledge-center/linux-static-hostname-suse/ "https://aws.amazon.com/premiumsupport/knowledge-center/linux-static-hostname-suse/")
- [Amazon EC2 instance running on RHEL](https://aws.amazon.com/premiumsupport/knowledge-center/linux-static-hostname-rhel7-centos7/ "https://aws.amazon.com/premiumsupport/knowledge-center/linux-static-hostname-rhel7-centos7/")

Alternatively, you can edit the `/etc/hosts` file and manually add this entry. For SAP systems, the hostname should not exceed 13 characters and should comply with SAP standards. See SAP OSS Note [611361](https://launchpad.support.sap.com/#/notes/611361 "https://launchpad.support.sap.com/#/notes/611361") for details (requires access to SAP ONE Support Launchpad).

## Step 5. Install Prerequisite Packages

###### Note

Your Amazon EC2 instance should have access to the internet to read and download required packages from the SUSE or Red Hat repository.

As root user, use the following commands to install the Linux packages that are required for SAP installation.

**SLES syntax:**

To install a package: `zypper install <package-name>`

To remove a package: `zypper remove <package-name>`

**RHEL syntax:**

To install a package: `yum install <package-name>`

To remove a package: `yum remove <package-name>`

1. Install `nfs-utils`, which is required for mounting the Amazon EFS mounts onto the Linux host.
2. Install the `nvme-cli` package to view the NVMe device mapping of Amazon EBS volumes.
3. Install SSM Agent by following the instructions in the [AWS Systems Manager user guide](../../../systems-manager/latest/userguide/sysman-manual-agent-install.md#agent-install-sles "../../../systems-manager/latest/userguide/sysman-manual-agent-install.md#agent-install-sles").
4. Install SAP data provider.

```
  cd /tmp
  wget https://s3.amazonaws.com/aws-data-provider/bin/aws-agent_install.sh
  chmod ugo+x aws-agent_install.sh
  sudo ./aws-agent_install.sh
```

## Step 6. Identify the Amazon EBS Device from NVMe Block Devices

On [Nitro-based](../../../AWSEC2/latest/UserGuide/instance-types.md#ec2-nitro-instances "../../../AWSEC2/latest/UserGuide/instance-types.md#ec2-nitro-instances") instances, device names that are specified in the block device mapping ([step 2](#net-linux-step-2-create-json-file "#net-linux-step-2-create-json-file")) are renamed as `/dev/nvme[0-26]n`. Before you proceed with the next step, ensure that you are using the appropriate device name to create a file system. Refer to the [AWS documentation](../../../AWSEC2/latest/UserGuide/nvme-ebs-volumes.md "../../../AWSEC2/latest/UserGuide/nvme-ebs-volumes.md") to learn how to find the Amazon EBS device on Nitro-based instances.

## Step 7. Format Block Devices for Mounting SAP File Systems

To view the list of volumes attached to your instance and their device names, run the `lsblk` command as root user. The command displays the list of devices that are attached to your instance.

```
  lsblk
  NAME        MAJ:MIN RM SIZE RO TYPE MOUNTPOINT
  nvme1n1     259:0    0  50G  0 disk
  nvme0n1     259:1    0  10G  0 disk
  └nvme0n1p1  259:2    0  10G  0 part /
  nvme2n1     259:3    0  50G  0 disk
```

Format the block device for `/usr/sap`, swap, and other file systems that are needed to install SAP. As root user, format the Amazon EBS volumes attached to your instance to store local SAP files. You need to create a label for the file system as well. This label will be used to mount the file system.

```
  mkfs.xfs -f /dev/nvme1n1 -L USR_SAP
```

###### Tip

NVMe device IDs associated with the volume could change during reboots. To avoid mount errors during instance reboots, you need to create a label for your file systems and mount them by label rather than by the actual NVMe IDs. This will also help in the situation where you need to change your instance type between Nitro-based and non Nitro-based instances.

## Step 8. Create Directories and Mount the File System

As root user, create the directories to mount the file systems required for SAP installation. Start with the `/usr/sap` mount, using the syntax `mkdir <directory-path>`.

```
  mkdir /usr/sap
```

As root user, add entries to the `/etc/fstab` file and mount the file systems. Adding entries to `/etc/fstab` ensures that your file systems are mounted automatically when your Amazon EC2 instance is restarted.

Add the entries for local SAP file systems to the `/etc/fstab` file by using the following commands:

```
  echo "/dev/disk/by-label/USR_SAP /usr/sap xfs noatime,nodiratime,logbsize=256k 0 0" >> /etc/fstab
```

To mount the file system that has been added to `/etc/fstab`, use the syntax `mount -a`.

```
  mount -a
  df -h
  Filesystem      Size  Used Avail Use% Mounted on
  devtmpfs        3.8G  8.0K  3.8G   1% /dev
  tmpfs           3.8G     0  3.8G   0% /dev/shm
  tmpfs           3.8G  9.5M  3.8G   1% /run
  /dev/nvme0n1p1  9.8G  1.4G  7.9G  15% /
  tmpfs           3.8G     0  3.8G   0% /sys/fs/cgroup
  tmpfs           769M     0  769M   0% /run/user/1000
  /dev/nvme1n1     50G   33M   50G   1% /usr/sap
```

Here you can see that `/usr/sap` is mounted on device `/dev/nvme1n1`.

## Step 9. Create Swap for SAP Installation

Linux swap functionality can improve the overall performance of the system and is a mandatory prerequisite for SAP installation. To determine the value for swap, follow the recommendations in the SAP Note [1597355](https://launchpad.support.sap.com/#/notes/1597355 "https://launchpad.support.sap.com/#/notes/1597355").

To allocate swap on device `/dev/nvme2n1`, use the following commands:

```
  lsblk
  NAME        MAJ:MIN RM SIZE RO TYPE MOUNTPOINT
  nvme1n1     259:0    0  50G  0 disk /usr/sap
  nvme0n1     259:1    0  10G  0 disk
  └nvme0n1p1  259:2    0  10G  0 part /
  nvme2n1     259:3    0  50G  0 disk

  mkswap -f /dev/nvme2n1 -L SWAP
  Setting up swapspace version 1, size = 50 GiB (53687087104 bytes)
  LABEL=SWAP, UUID=07291579-afb6-4e5f-8828-4c1441841f9b
  swapon -L SWAP
  swapon -s
  Filename        Type       Size      Used   Priority
  /dev/nvme2n1    partition  52428796  0      -1
```

Device `/dev/nvme2n1` is now allocated to be used as swap by the SAP application that will be installed on this host.

## Step 10. Creating the Amazon EFS Mount for /usr/sap/trans and /sapmnt

To create an Amazon EFS file system and mount it on the Amazon EC2 instance, do the following:

1. Create a security group for Amazon EFS.

```
  $ aws ec2 create-security-group --group-name efs-sap-sg --description "Amazon EFS for SAP, SG for EFS " --vpc-id vpc-123456789abcdefgh
```

Make a note of the security group ID that is displayed in the output.

```
  {
      "GroupId": "sg-abc12def "
  }
```

In the example, the security group ID is `sg-abc12def`. 2. Create an inbound rule for the security group.

```
  $ aws ec2 authorize-security-group-ingress --group-id sg-abc12def --protocol tcp --port 2049 --cidr 0.0.0.0/0
```

3. Create an Amazon EFS file system.

```
  $ aws efs create-file-system --creation-token efsforsap
```

The command should display the following output:

```
  {
    "SizeInBytes": {
        "Value": 0
    },
    "CreationToken": "efsforsap",
    "Encrypted": false,
    "CreationTime": 1523374253.0,
    "PerformanceMode": "generalPurpose",
    "FileSystemId": "fs-abc12def",
    "NumberOfMountTargets": 0,
    "LifeCycleState": "creating",
    "OwnerId": "xxxxxxxxxxxx"
  }
```

Make a note of the `FileSystemId` value. In this example, `FileSystemId` is `fs-abc12def`. 4. Create the tag for `FileSystemId`.

```
  $ aws efs create-tags --file-system-id <FileSystemId> Key=<Name>,Value=<SomeExampleNameValue>
```

In this example, the key is `usrsap` and the value is `ECC`.

```
  $ aws efs create-tags --file-system-id fs-abc12def --tags Key=usrsap,Value=ECC
```

5. Create the mount target.

```
  $ aws efs create-mount-target --file-system-id fs-abc12def --subnet-  id subnet-a98c8386 --security-group sg-abc12def
```

The command should display the following output:

```
  {
    "MountTargetId": "fsmt-123abc45",
    "NetworkInterfaceId": "xxxxxxxxxx",
    "FileSystemId";: "fs-abc12def ",
    "LifeCycleState": "creating",
    "SubnetId": "xxxxxxxxxxx",
    "OwnerId": "xxxxxxxxxxxx",
    "IpAddress": "x.x.x.x"
  }
```

Make a note of the `LifeCycleState` value, which is `creating` in the example. 6. Wait for a few minutes, and then check the status of creation by using the following command:

```
  $ aws efs describe-mount-targets --file-system-id fs-abc12def
```

The mount target `fsmt-061ab24e` is now available.

```
  {
    "MountTargets": [
        {
            "MountTargetId": "fsmt-061ab24e",
            "NetworkInterfaceId": " xxxxxxxxxx ",
            "FileSystemId": "fs-abc12def",
            ";LifeCycleState": "available",
            "SubnetId": " xxxxxxxxxxx ",
            "OwnerId": " xxxxxxxxxxx",
            "IpAddress": "x.x.x.x"
        }
     ]
  }
```

7. The DNS name for your file system on Amazon EFS should use the following naming convention:

```
<file-system-id.efs.aws-region>.amazonaws.com
```

In this example, `us-east-1` is the AWS Region.

```
fs-abc12def.efs.us-east-1.amazonaws.com
```

8. Use SSH to connect to your Amazon EC2 instance and create the mount point.

```
mkdir /usr/sap/trans
```

9. Mount the Amazon EFS file system. Mounting Amazon EFS using a DNS name is by default deactivated on a VPC. Instead, you can use an IP address to the corresponding file system.

```
sudo mount -t nfs -o nfsvers=4.1,rsize=1048576,wsize=1048576,hard,timeo=600,retrans=2 ip-address:/trans </usr/sap/trans>
```

This IP address can be found in step 7; for example:

```
sudo mount -t nfs -o nfsvers=4.1,rsize=1048576,wsize=1048576,hard,timeo=600,retrans=2 fs-abc12def.efs.us-east-1.amazonaws.com:/trans /usr/sap/trans
```

Repeat steps 8-9 to create other Amazon EFS mount points for `/sapmnt` and any other SAP software that needs to be shared between the Amazon EC2 instances.

## Step 11. Installing SAP on Amazon EC2

Amazon EC2 is ready for SAP NetWeaver installation. Download the software from the [SAP Support Portal](https://support.sap.com/en/index.html "https://support.sap.com/en/index.html") and proceed with the installation.

###### Note

SAP Software Provisioning Manager (SWPM) Prerequisites Checker validates your installation host for compliance with most of the prerequisites defined in the installation guide. We recommend using this feature for your installations.
