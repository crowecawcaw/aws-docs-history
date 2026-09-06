

# Launch and Setup Instance
<a name="sap-nw-os-setup"></a>

**Topics**
+ [Launch an instance](#sap-nw-os-setup-launch)
+ [Remote Access with AWS Systems Manager Session Manager](#remote-access-with-systems-manager-session-manager)
+ [Configure the hostname](#configure-the-hostname)
+ [Install prerequisite packages](#install-prerequisite-packages)
+ [Configure storage](#configure-storage)

## Launch an instance
<a name="sap-nw-os-setup-launch"></a>

An instance is a virtual server in the AWS Cloud. You launch an instance from an Amazon Machine Image (AMI). The AMI provides the operating system, application server, and applications for your instance.

There are multiple console and code driven methods for launching an EC2 Instance, see the full documentation at [Launch an Amazon EC2 instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/LaunchingAndUsingInstances.html) 

If you are new to AWS, we suggest exploring the options using the launch instance wizard, to understand configuration options including location, instance type, local storage allocation, security options and advanced options such as user data which you can specify operating system commands to run when you launch an EC2 instance. A full list of configurable parameters is available at [Reference for Amazon EC2 instance configuration parameters](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-launch-parameters.html) 

 **CloudFormation example** 

If using AWS CloudFormation for infrastructure as code, the following snippet shows the minimum requirements for a SAP NetWeaver instance. This is not a complete CloudFormation template but demonstrates the key properties:

```
MySAPNetWeaverInstance:
  Type: AWS::EC2::Instance
  Properties:
    ImageId: ami-0f0dcf1e0a0d26ea4  # Choose a marketplace or other AMI
    InstanceType: r7i.xlarge        # Choose a certified instance
    KeyName: my-key-pair
    SubnetId: subnet-1234567        # Distribute your instances in different subnets
    IamInstanceProfile: !Ref EC2InstanceProfile
    SecurityGroups:
      - !Ref InstanceSecurityGroup  # Define or Select Security Group
    BlockDeviceMappings:
      - DeviceName: /dev/xvda       # Root volume
        Ebs:
          VolumeSize: 50            # Root for OS and NetWeaver
          VolumeType: gp3
          DeleteOnTermination: true
      - DeviceName: /dev/sdb        # SAP application volume
        Ebs:
          VolumeSize: 100
          VolumeType: gp3
          DeleteOnTermination: true
      - DeviceName: /dev/sdc        # Swap volume
        Ebs:
          VolumeSize: 50
          VolumeType: gp3
          DeleteOnTermination: true
    UserData:
      Fn::Base64: | # Sample user data
        #!/bin/bash

        # Set hostname
        hostnamectl set-hostname saphost01

        # Install SSM Agent
        # Provide details depending on OS type and whether it is already part of the AMI
```

## Remote Access with AWS Systems Manager Session Manager
<a name="remote-access-with-systems-manager-session-manager"></a>

For secure shell access to your SAP NetWeaver instances, AWS Systems Manager Session Manager provides browser-based or CLI-based shell access without requiring SSH keys, bastion hosts, or open inbound ports. The SSM Agent comes pre-installed on many AMIs, but ensure it’s running and has the necessary IAM permissions during your launch activities. For RHEL-based systems, see [Installing SSM Agent on RHEL](https://docs.aws.amazon.com/systems-manager/latest/userguide/agent-install-rhel.html), and for SLES systems, see [Installing SSM Agent on SLES](https://docs.aws.amazon.com/systems-manager/latest/userguide/agent-install-sles.html). This allows immediate secure access to your instance for SAP installation and configuration tasks. For complete Session Manager documentation, see [AWS Systems Manager Session Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager.html).

## Configure the hostname
<a name="configure-the-hostname"></a>

Configure your instance hostname either during launch using user data or after launch through a shell session.

To configure the hostname after launch:

1. Connect to your SAP instance using AWS Systems Manager Session Manager or SSH with your key pair.

1. Switch to the root user.

1. Update the hostname and domain name according to your requirements.

For detailed steps specific to your operating system, see [How do I assign a static hostname to a private Amazon EC2 instance running RHEL or SLES?](https://repost.aws/knowledge-center/linux-static-hostname) in the AWS Knowledge Center.

For SAP-specific hostname requirements, see [SAP Note 611361 - Hostnames of SAP ABAP Platform servers](https://me.sap.com/notes/611361) and [SAP Note 2718300 - Physical and Virtual hostname length limitations](https://me.sap.com/notes/0002718300).

## Install prerequisite packages
<a name="install-prerequisite-packages"></a>

Your Amazon EC2 instance requires internet access to download packages from the SUSE or Red Hat repositories.

**Important**  
Ensure your instance has outbound internet connectivity or access to a local package repository before proceeding with package installation.

The following packages are required for SAP NetWeaver installation on AWS. Depending on your baseline AMI (for example, RHEL for SAP or SLES for SAP), some packages may already be installed.


| Package | Description | Manual Download | Required | 
| --- | --- | --- | --- | 
|  `nfs-utils`  | Network File System utilities for mounting Amazon EFS |  | Mandatory | 
|  `nvme-cli`  | NVMe command line interface for viewing Amazon EBS volume mapping |  | Recommended | 
|  `aws-cli`  |  AWS Command Line Interface for AWS service management. | See [Installing or updating the latest version of the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) for installation instructions. | Recommended | 
|  `aws-sap-data-provider`  |  AWS Data Provider for SAP - enables SAP systems to retrieve AWS infrastructure information. | Download the appropriate RPM package first from [AWS Data Provider installation guide](https://docs.aws.amazon.com/sap/latest/general/data-provider-installation.html). | Mandatory | 

Use the following commands to install packages on your system:

 **SLES systems:** 

```
$ sudo zypper install <package-name>
```

 **RHEL systems:** 

```
$ sudo dnf install <package-name>
```

## Configure storage
<a name="configure-storage"></a>

This section explains how to configure the Amazon EBS volumes that were attached during instance launch for SAP NetWeaver installation.

**Note**  
This guide uses NVMe device names (for example, /dev/nvme1n1) which are standard on Nitro-based instances. On non-Nitro instances, devices use different naming (for example, /dev/sdb). Adjust commands according to your device names.

**Important**  
While LVM can be used for volume management, it is not recommended for SAP NetWeaver installations due to potential performance overhead and added complexity. Use direct device formatting as shown in this guide.

### Configure local storage
<a name="configure-local-storage"></a>

1.  **Identify attached volumes** 

   Rescan for new or changed block devices, then identify the devices attached to your instance, their sizes, and associated volume IDs.

   ```
   $ sudo partprobe
   $ sudo lsblk -o NAME,SIZE,TYPE,FSTYPE,LABEL,PATH,SERIAL | sed 's/vol0/vol-0/g'
   ```

   Example output:

   ```
   NAME        SIZE TYPE FSTYPE LABEL PATH           SERIAL
   nvme0n1      10G disk              /dev/nvme0n1   vol-0abc123def456789a
   └nvme0n1p1   10G part xfs    ROOT  /dev/nvme0n1p1
   nvme1n1      50G disk              /dev/nvme1n1   vol-0xyz987uvw654321b
   nvme2n1      50G disk              /dev/nvme2n1   vol-0pqr456mno789123c
   ```

1.  **Create filesystems** 

   Create XFS filesystems on the volumes allocated for SAP NetWeaver. Use labels to ensure consistent mounting across instance restarts.

   ```
   $ sudo mkfs.xfs -f /dev/nvme1n1 -L USR_SAP
   ```
**Tip**  
Labels provide consistent device identification across instance restarts and instance type changes. Always use labels in /etc/fstab by referencing `/dev/disk/by-label/LABEL_NAME`.

1.  **Create mount points and configure fstab** 

   Create the required directories and add entries to /etc/fstab for automatic mounting.

   ```
   $ sudo mkdir /usr/sap
   $ echo "/dev/disk/by-label/USR_SAP /usr/sap xfs noatime,nodiratime,logbsize=256k 0 0" | sudo tee -a /etc/fstab
   $ sudo mount -a
   $ df -h
   ```

### Configure swap space
<a name="configure-swap-space"></a>

Configure swap space for SAP NetWeaver installation. For swap sizing recommendations, see [SAP Note 1597355 - Linux swap space requirement](https://me.sap.com/notes/1597355).

1.  **Create swap filesystem** 

   ```
   $ sudo mkswap -f /dev/nvme2n1 -L SWAP
   ```

1.  **Configure swap in fstab and enable** 

   ```
   $ echo "/dev/disk/by-label/SWAP none swap sw 0 0" | sudo tee -a /etc/fstab
   $ sudo swapon -L SWAP
   ```

1.  **Verify swap is active** 

   ```
   $ sudo swapon -s
   ```

### Configure NFS filesystems
<a name="configure-nfs-filesystems"></a>

Configure NFS filesystems for shared SAP directories such as transport directories or shared installation media.

1.  **Test NFS mount and create directory structure** 

   Test the NFS mount temporarily and create the required directory structure on the EFS filesystem.

   ```
   $ sudo mount -t nfs4 -o nfsvers=4.1,rsize=1048576,wsize=1048576,hard,intr,timeo=600 your-efs-mount-target.efs.region.amazonaws.com:/ /mnt/
   $ sudo mkdir -p /mnt/SHARED_SID
   $ sudo mkdir -p /mnt/SHARED_TRANS
   $ ls -la /mnt
   $ sudo umount /mnt
   ```

1.  **Create permanent mount points** 

   Create the required local directories for NFS mounts.

   ```
   $ sudo mkdir -p /sapmnt/SID
   $ sudo mkdir -p /usr/sap/trans
   ```

1.  **Configure NFS mounts in fstab** 

   Add NFS mount entries to /etc/fstab for automatic mounting.

   ```
   $ echo "your-efs-mount-target.efs.region.amazonaws.com:/SHARED_SID /sapmnt/SID nfs4 nfsvers=4.1,rsize=1048576,wsize=1048576,hard,intr,timeo=600 0 0" | sudo tee -a /etc/fstab
   $ echo "your-efs-mount-target.efs.region.amazonaws.com:/SHARED_TRANS /usr/sap/trans nfs4 nfsvers=4.1,rsize=1048576,wsize=1048576,hard,intr,timeo=600 0 0" | sudo tee -a /etc/fstab
   ```

1.  **Mount NFS filesystems** 

   ```
   $ sudo mount -a
   $ df -h
   ```

**Note**  
Replace `SID` with your actual SAP System ID (for example, `PRD` or `DEV`). Replace `your-efs-mount-target.efs.region.amazonaws.com` with your actual Amazon EFS mount target DNS name and region.