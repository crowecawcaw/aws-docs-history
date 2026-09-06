

# Mounting S3 file systems on Amazon EC2
<a name="s3-files-mounting"></a>

To mount S3 file systems on an EC2 instance, you must use the S3 Files mount helper. The mount helper helps you mount your S3 file systems on EC2 instances running the supported distributions. When mounting a file system, the mount helper defines a new network file system type, called `s3files`, which is fully compatible with the standard `mount` command in Linux. The mount helper also supports mounting an S3 file system at instance boot time automatically by using entries in the `/etc/fstab` configuration file on EC2 Linux instances. The mount helper is part of the open-source collection of tools that is installed when you install the S3 Files client (amazon-efs-utils).

![The data flow between an S3 bucket, S3 file system, and Amazon EC2 instance.](http://docs.aws.amazon.com/AmazonS3/latest/userguide/images/S3Files_EC2_dataflow.png)


## Prerequisites to mount on EC2 instances
<a name="s3-files-mounting-prereqs"></a>
+ Your EC2 instance runs one of the following supported Linux distributions. Windows and macOS are not supported.
  + Amazon Linux 2
  + Amazon Linux 2023
  + Red Hat Enterprise Linux (RHEL) 8
  + Red Hat Enterprise Linux (RHEL) 9
  + Ubuntu 20.04
  + Ubuntu 22.04
  + Ubuntu 24.04
  + openSUSE Leap
  + SUSE Linux Enterprise Server (SLES) 15
+ You have an S3 file system with at least one mount target available.
+ Your EC2 instance is in the same Availability Zone as the mount target that you will use to mount your file system.
+ An IAM instance profile is attached to the EC2 instance with the required permissions for S3 Files. For details, see [IAM role for attaching your file system to AWS compute resources](s3-files-prereq-policies.md#s3-files-prereq-iam-compute-role).
+ You have configured the required [Security groups](s3-files-prereq-policies.md#s3-files-prereq-security-groups).
+ You have installed the amazon-efs-utils package on the EC2 instance. For more information, see [S3 Files client](s3-files-prereq-policies.md#s3-files-prereq-client).

## How does the mount helper work?
<a name="s3-files-mounting-how-it-works"></a>

When you issue a mount command, the mount helper performs the following actions:
+ Retrieves IAM credentials from the EC2 instance profile.
+ Initializes the efs-proxy process to establish a TLS-encrypted connection to the mount target.
+ Starts the amazon-efs-mount-watchdog supervisor process, which monitors the health of TLS mounts. This process is started automatically the first time an S3 file system is mounted.
+ Mounts the file system at the specified mount point.

The mount helper uses TLS version 1.2 to communicate with your file system. Using TLS requires certificates, and these certificates are signed by a trusted Amazon Certificate Authority. For more information on how encryption works, see [Security for S3 Files](s3-files-security.md).

The mount helper uses the following mount options that are optimized for S3 Files:


| Option | Value | Description | 
| --- | --- | --- | 
| nfsvers | 4.2 | NFS protocol version. | 
| rsize | 1048576 | Sets the maximum number of bytes of data that the NFS client can receive for each network READ request to 1048576 (1 MB), the largest available, to avoid diminished performance. | 
| wsize | 1048576 | Sets the maximum number of bytes of data that the NFS client can send for each network WRITE request to 1048576 (1 MB), the largest available, to avoid diminished performance. | 
| hard | — | Sets the recovery behavior of the NFS client after an NFS request times out, so that NFS requests are retried indefinitely until the server replies, to ensure data integrity. | 
| timeo | 600 | Sets the timeout value that the NFS client uses to wait for a response before it retries an NFS request to 600 deciseconds (60 seconds) to avoid diminished performance. | 
| retrans | 2 | Sets the number of times the NFS client retries a request before it attempts further recovery action to 2. | 
| noresvport | — | Tells the NFS client to use a new non-privileged TCP source port when a network connection is reestablished. Using noresvport helps ensure that your file system has uninterrupted availability after a reconnection or network recovery event. | 

In addition, the mount helper automatically uses `tls` and `iam` mount options when mounting an S3 file system as S3 Files requires these options to establish a connection. This is because S3 Files always mounts a file system using TLS encryption and IAM authentication and these cannot be disabled.

## How to mount your S3 file system on an EC2 instance?
<a name="s3-files-mounting-steps"></a>
+ Connect to your EC2 instance through Secure Shell (SSH) or EC2 Instance Connect on EC2 Console. For more information, see [Connect to your EC2 instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/connect.html).
+ Create a directory `/mnt/s3files` that you will use as the file system mount point using the following command:

  ```
  sudo mkdir /mnt/s3files
  ```
+ Mount your S3 file system:

  ```
  FS="{{{YOUR_FILE_SYSTEM_ID}}}"
  sudo mount -t s3files $FS:/ /mnt/s3files
  ```
+ Confirm the file system is mounted.

  ```
  df -h /mnt/s3files
  ```

  You should see a response similar to the following:

  ```
  Filesystem      Size  Used Avail Use% Mounted on
  {{{s3files-dns}}}    8.0E  129M  8.0E   1% {{{path/to/mount}}}
  ```

  You can also verify file system mount and inspect mount options by listing the contents of the local mount point. If the mount is successful, this command shows the mount details, including your mount options, for the specific directory.

  ```
  findmnt -T /mnt/s3files
  ```

For detailed information on mount commands, visit the [GitHub documentation](https://github.com/aws/efs-utils/blob/master/README.md#mountefs).

You can now read and write S3 objects as files on your local mount path using standard file system operations. If you have objects in your S3 bucket then you can view them as files using the following commands.

```
ls /mnt/s3files
```

You can monitor your file system storage, performance, client connections, and synchronization errors using [CloudWatch metrics](s3-files-monitoring-cloudwatch.md).

## How to mount your S3 file system on an EC2 instance using access points
<a name="s3-files-mounting-access-points-inline"></a>

When you mount a file system using an access point, the mount command includes the `access-point-id` mount option.

```
sudo mount -t s3files -o accesspoint={{access-point-id}} {{file-system-id}} /mnt/s3files
```

where:
+ {{access-point-id}} is the ID of your access point.
+ {{file-system-id}} is the ID of your S3 file system.

## Automatically mounting S3 file systems when your EC2 instance starts
<a name="s3-files-mounting-auto"></a>

You can configure your EC2 instance to automatically mount an S3 file system when the instance starts or restarts by updating the `/etc/fstab` file. The `/etc/fstab` file contains information about file systems and is used by the operating system to determine which file systems to mount at boot time.

**Warning**  
Use the `_netdev` option, used to identify network file systems, when mounting your file system automatically. If `_netdev` is missing, your EC2 instance might stop responding. This result is because network file systems need to be initialized after the compute instance starts its networking. For more information, see [Automatic mounting fails and the instance is unresponsive](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/builtInFS-fstab-issues.html).

You can use the mount helper to configure an Amazon EC2 instance to automatically mount an S3 file system when the instance starts:
+ Update the EC2 `/etc/fstab` file with an entry for the S3 file system.
+ Attach an S3 file system when you create a new EC2 instance using the EC2 launch instance wizard.

### Updating the /etc/fstab file
<a name="s3-files-mounting-auto-fstab"></a>

Perform the following steps to update the `/etc/fstab` on an EC2 Linux instance so that the instance uses the mount helper to automatically remount an S3 file system when the instance restarts.
+ [Connect to your EC2 instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/connect.html).
+ Open the `/etc/fstab` file in an editor and add the following line to the file:

  ```
  {{file-system-id}}:/ {{mount-directory}} s3files _netdev 0 0
  ```

  Where:
  + {{file-system-id}} is the ID of your S3 file system (for example, `fs-0123456789abcdef0`).
  + {{mount-directory}} is the mount point directory on your EC2 instance (for example, `/mnt/s3files`).
  + `_netdev` specifies that the file system is a network file system, ensuring the instance waits for network availability before attempting the mount.
+ Save the file and close the editor.
+ Test the fstab entry by mounting all file systems in fstab:

  ```
  sudo mount -a
  ```
+ Verify the file system is mounted:

  ```
  findmnt -T {{mount-directory}}
  ```

**Using the nofail option**

We recommend adding the `nofail` option to your fstab entry in production environments. This option allows the instance to boot even if the file system fails to mount:

```
{{file-system-id}}:/ {{mount-directory}} s3files _netdev,nofail 0 0
```

**Automatic mounting with an access point**

To automatically mount using an S3 Files access point, include the `accesspoint` option:

```
{{file-system-id}}:/ {{mount-directory}} s3files _netdev,accesspoint={{access-point-id}} 0 0
```

**Automatic mounting with a subdirectory**

To automatically mount a specific subdirectory of your file system, specify the path:

```
{{file-system-id}}:/path/to/directory {{mount-directory}} s3files _netdev 0 0
```

### Using the EC2 launch instance wizard
<a name="s3-files-mounting-auto-wizard"></a>
+ Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).
+ Choose **Launch Instance**.
+ Follow this documentation to launch an EC2 instance using the launch instance wizard in the AWS console. Before choosing **Launch Instance**, configure your network and add your S3 file system as shown in following steps.
+ Make sure you select a subnet in your **Network settings**.
+ Select the default security group to make sure that your EC2 instance can access your S3 file system. You can't access your EC2 instance by Secure Shell (SSH) using this security group. For access by SSH, later you can edit the default security and add a rule to allow SSH or a new security group that allows SSH. You can use the following settings:
  + Type: SSH
  + Protocol: TCP
  + Port Range: 22
  + Source: Anywhere 0.0.0.0/0
+ Under **Storage** section, choose **File systems** and choose **S3 Files**.
+ Under the file system drop down, you will see your file systems in the Availability Zone based on the subnet you selected previously in your Network settings. Choose the S3 file system that you want to mount. If you don't have any file systems, choose create a new file system to create a new one.
+ Enter a local mount path on your EC2 instance where you want to mount the file system (for example, `/mnt/s3files`).
+ A command will be generated to mount the file system and add it to fstab. You can choose to add the command to User data or run it manually on your EC2 instance after it is launched. Your EC2 instance will then be configured to mount the S3 file system at launch and whenever it's rebooted.
+ Choose **Launch Instance**.

## Mounting S3 file systems from another VPC
<a name="s3-files-mounting-cross-vpc"></a>

When you use a VPC peering connection or transit gateway to connect VPCs, Amazon EC2 instances that are in one VPC can access S3 file systems in another VPC.

A transit gateway is a network transit hub that you can use to interconnect your VPCs and on-premises networks. For more information about using VPC transit gateways, see [Getting Started with transit gateways](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-getting-started.html) in the *Amazon VPC Transit Gateways Guide*. A VPC peering connection is a networking connection between two VPCs. This type of connection enables you to route traffic between them using private Internet Protocol version 4 (IPv4) or Internet Protocol version 6 (IPv6) addresses. You can use VPC peering to connect VPCs within the same AWS Region or between AWS Regions. For more information on VPC peering, see [What is VPC Peering?](https://docs.aws.amazon.com/vpc/latest/peering/what-is-vpc-peering.html) in the *Amazon VPC User Guide*.

When mounting a file system from a different VPC, you need to resolve the mount target manually. You should use the IP address of the mount targets in the corresponding Availability Zone as follows and replace the {{mount-target-ip-address}}, {{file-system-id}}, and {{mount-directory}} with your values.

```
sudo mount -t s3files -o mounttargetip={{mount-target-ip-address}} {{file-system-id}} {{mount-directory}}
```

To ensure high availability of your file system, we recommend that you always use a mount target IP address that is in the same Availability Zone as your NFS client.

Alternatively, you can use Amazon Route 53 as your DNS service. In Route 53, you can resolve the mount target IP addresses from another VPC by creating a private hosted zone and resource record set. For more information on how to do so, see [Working with private hosted zones](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/hosted-zones-private.html) in the *Amazon Route 53 Developer Guide*.

For more details on mounting from another VPC, visit the [GitHub ReadMe](https://github.com/aws/efs-utils/blob/master/README.md).

## Mounting S3 file systems from a different AWS Region
<a name="s3-files-mounting-cross-region"></a>

If you are mounting your S3 file system from another VPC that is in a different AWS Region than the file system, you will need to edit the `s3files-utils.conf` file. In `/etc/amazon/efs/s3files-utils.conf`, locate the following lines:

```
#region = us-east-1
```

Uncomment the line, and replace the value for the ID of the region in which the file system is located, if it is not in us-east-1.

Then, you need to specify the mount target IP in the mount command after changing the region in the config:

```
sudo mount -t s3files -o mounttargetip={{mount-target-ip-address}} {{file-system-id}} {{mount-directory}}
```

## Unmounting your S3 file system
<a name="s3-files-mounting-unmount"></a>

To unmount an S3 file system connected to an EC2 instance running Linux, use the `umount` command as follows:

```
umount {{mount-directory}}
```

We recommend that you do not specify any other `umount` options. Avoid setting any other `umount` options that are different from the defaults. You can verify that your S3 file system has been unmounted by running the `findmnt` command. If the unmount was successful, the `findmnt` command on your mount directory will yield no output.