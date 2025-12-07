# Tutorial: Mounting with on-premises Linux

clients

You can mount your EFS file systems on your on-premises data center servers when
connected to your Amazon VPC with Direct Connect or VPN. The following graphic shows a high-level
schematic diagram of the AWS services required in mounting EFS file systems from
on-premises.

![Mount an EFS file system on an on-premises client when using Direct Connect.](/images/efs/latest/ug/images/efs-directconnect-how-it-works.png)

###### Note

Using Amazon EFS with Microsoft Windows–based clients isn't supported.

###### Topics

- [Prerequisites](#efs-onpremises "#efs-onpremises")
- [Step 1: Create your EFS resources](#wt5-step1-efs "#wt5-step1-efs")
- [Step 2: Install the NFS client](#wt5-step4-install-nfs "#wt5-step4-install-nfs")
- [Step 3: Mount the EFS file system on your
  on-premises client](#wt5-step3-connect "#wt5-step3-connect")
- [Step 4: Clean up resources and protect your AWS
  account](#wt5-step4-cleanup "#wt5-step4-cleanup")
- [Optional: Encrypting data in transit](#wt5-step2-get-efs-utils "#wt5-step2-get-efs-utils")

## Prerequisites

Make sure that you already have an Direct Connect or VPN connection. For more information on
Direct Connect, see the [Direct Connect User Guide](../../../directconnect/latest/UserGuide/Welcome.md "../../../directconnect/latest/UserGuide/Welcome.md"). For more
information on setting up a VPN connection, see [Connect your VPC to remote networks using AWS Virtual Private Network](../../../vpc/latest/userguide/vpn-connections.md "../../../vpc/latest/userguide/vpn-connections.md") in the _Amazon VPC User Guide_.

After you have an Direct Connect or VPN connection, create an EFS file system and a
mount target in your Amazon VPC. After that, you download and install the amazon-efs-utils tools.
Then, you test the file system from your on-premises client. Finally, the clean-up step at the
end of the walkthrough provides information for you to remove these resources.

The walkthrough creates all these resources in the US West (Oregon) Region
(`us-west-2`). Whichever AWS Region you use, be sure to use it consistently.
All of your resources—your VPC, your mount target, and your EFS file
system—must be in the same AWS Region, as shown in the following diagram.

![Mount an EFS file system on an on-premises client when using Direct Connect.](/images/efs/latest/ug/images/efs-directconnect-how-it-works.png)

###### Note

In some cases, your local application might need to know if the EFS file system
is available. In these cases, your application should be able to point to a different mount
point IP address if the first mount point becomes temporarily unavailable. In this scenario,
we recommend that you have two on-premises clients connected to your file system through
different Availability Zones (AZs) for higher availability.

You can use the root credentials of your AWS account to sign in to the console and try
this exercise. However, AWS Identity and Access Management (IAM) best practices recommend that you don't use the
root credentials of your AWS account. Instead, create an administrator user in your account
and use those credentials to manage resources in your account. For more information, see
[Single sign-on access to AWS accounts](../../../singlesignon/latest/userguide/useraccess.md "../../../singlesignon/latest/userguide/useraccess.md") in the _AWS IAM Identity Center User Guide_.

You can use a default VPC or a custom VPC that you have created in your account. For this
walkthrough, the default VPC configuration works. However, if you use a custom VPC, verify the
following:

- The internet gateway is attached to your VPC. For more information, see [Enable internet access for a VPC using an internet gateway](../../../vpc/latest/userguide/VPC_Internet_Gateway.md "../../../vpc/latest/userguide/VPC_Internet_Gateway.md") in the
  _Amazon VPC User Guide_.
- The VPC route table includes a rule to send all internet-bound traffic to the Internet
  gateway.

## Step 1: Create your EFS resources

In this step, you create your EFS file system and mount targets.

###### To create your EFS file system

1. Open the Amazon Elastic File System console at
   [https://console.aws.amazon.com/efs/](https://console.aws.amazon.com/efs/ "https://console.aws.amazon.com/efs/").
2. Choose **Create File System**.
3. Choose your default VPC from the **VPC** list.
4. Select the checkboxes for all of the Availability Zones. Make sure that they all have the
   default subnets, automatic IP addresses, and the default security groups chosen. These are
   your mount targets. For more information, see [Managing mount targets](accessing-fs.md "accessing-fs.md").
5. Choose **Next Step**.
6. Name your file system, keep **general purpose** selected as your
   default performance mode, and choose **Next Step**.
7. Choose **Create File System**.
8. Choose your file system from the list and make a note of the **Security
   group** value. You need this value for the next step.

The file system you just created has mount targets. Each mount target has an associated
security group. The security group acts as a virtual firewall that controls network traffic.
If you didn't provide a security group when creating a mount target, Amazon EFS associates the
default security group of the VPC with it. If you followed the preceding steps exactly, then
your mount targets are using the default security group.

Next, you add a rule to the mount target's security group to allow inbound traffic to the
Network File System (NFS) port (2049). You can use the AWS Management Console to add the rule to your mount
target's security groups in your VPC.

###### To allow inbound traffic to the NFS port

1.  Sign in to the AWS Management Console and open the Amazon EC2 console at
    [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2.  Under **NETWORK & SECURITY**, choose **Security
    Groups**.
3.  Choose the security group associated with your file system. You made a note of this at
    the end of Step 1: Create your EFS resources.
4.  In the tabbed pane that appears below the list of security groups, choose the
    **Inbound** tab.
5.  Choose **Edit**.
6.  Choose **Add Rule**, and choose a rule of the following type:

        * **Type** – **NFS**
        * **Source** –
         **Anywhere**

    We recommend that you only use the **Anywhere** source for testing.
    You can create a custom source set to the IP address of the on-premises client, or use the
    console from the client itself, and choose **My IP**.

###### Note

You don't need to add an outbound rule, because the default outbound rule allows all
traffic to leave. If you don't have this default outbound rule, add an outbound
rule to open a TCP connection on NFS port 2049, identifying the mount target security
group as the destination.

## Step 2: Install the NFS client

In this step, you install the NFS client.

###### To install the NFS client on your on-premises server

###### Note

If you require data to be encrypted in transit, use the Amazon EFS mount helper,
`amazon-efs-utils`, instead of the NFS client. For information on installing
amazon-efs-utils, see the section _Optional: Encrypting Data in
Transit_.

1. Access the terminal for your on-premises client.
2. Install NFS.

If you're using Red Hat Linux, install NFS with the following command.

```
$ sudo yum -y install nfs-utils
```

If you're using Ubuntu, install NFS with the following command.

```
$ sudo apt-get -y install nfs-common
```

## Step 3: Mount the EFS file system on your

on-premises client

###### To create a mount directory

1. Make a directory for the mount point with the following command.

```
mkdir ~/efs
```

2. Choose your preferred IP address of the mount target in the Availability Zone. You can
   measure the latency from your on-premises Linux clients. To do so, use a terminal-based
   tool like `ping` against the IP address of your EC2 instances in different
   Availability Zones to find the one with the lowest latency.

- Run the mount command to mount the file system using the IP address of the mount
  target.

```
$ sudo mount -t nfs -o nfsvers=4.1,rsize=1048576,wsize=1048576,hard,timeo=600,retrans=2,noresvport `mount-target-IP`:/   ~/efs
```

Now that you've mounted your EFS file system, you can test it out with the
following procedure.

###### To test the EFS file system connection

1. Change directories to the new directory that you created with the following
   command.

```
$ cd ~/efs
```

2. Make a subdirectory and change the ownership of that subdirectory to your EC2 instance
   user. Then, navigate to that new directory with the following commands.

```
$ sudo mkdir getting-started
$ sudo chown ec2-user getting-started
$ cd getting-started
```

3. Create a text file with the following command.

```
$ touch test-file.txt
```

4. List the directory contents with the following command.

```
$ ls -al
```

As a result, the following file is created.

```
-rw-rw-r-- 1 `username` `username` 0 Nov 15 15:32 test-file.txt
```

###### Warning

Use the `_netdev` option, used to identify network file systems, when
mounting your file system automatically. If `_netdev` is missing, your EC2
instance might stop responding. This result is because network file systems need to be
initialized after the compute instance starts its networking. For more information, see
[Automatic mounting fails and the instance is
unresponsive](troubleshooting-efs-mounting.md#automount-fails "troubleshooting-efs-mounting.md#automount-fails").

## Step 4: Clean up resources and protect your AWS

account

After you have finished this walkthrough, or if you don't want to explore the
walkthroughs, you should follow these steps to clean up your resources and protect your AWS
account.

###### To clean up resources and protect your AWS account

1. Unmount the EFS file system with the following command.

```
$ sudo umount ~/efs
```

2. Open the Amazon EFS console at [Amazon EFS Console](https://console.aws.amazon.com/efs/ "https://console.aws.amazon.com/efs/").
3. Choose the EFS file system that you want to delete from the list of file
   systems.
4. For **Actions**, choose **Delete file
   system**.
5. In the **Permanently delete file system** dialog box, type the file
   system ID for the EFS file system that you want to delete, and then choose
   **Delete File System**.
6. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
7. In the navigation pane, choose **Security Groups**.
8. Select the name of the security group that you added the rule to for this
   walkthrough.

###### Warning

Don't delete the default security group for your VPC. 9. For **Actions**, choose **Edit inbound
rules**. 10. Choose the X at the end of the inbound rule you added, and choose
**Save**.

## Optional: Encrypting data in transit

To encrypt data in transit, use the Amazon EFS mount helper, amazon-efs-utils, instead of the
NFS client.

The _amazon-efs-utils_ package is an open-source
collection of Amazon EFS tools. The amazon-efs-utils collection comes with a mount helper and
tooling that makes it easier to encrypt data in transit for Amazon EFS. For more information on
this package, see [Installing the Amazon EFS client](using-amazon-efs-utils.md "using-amazon-efs-utils.md"). This package is available as a free download from
GitHub, which you can get by cloning the package's repository.

###### To clone amazon-efs-utils from GitHub

1. Access the terminal for your on-premises client.
2. From the terminal, clone the amazon-efs-utils tool from GitHub to a directory of your
   choice, with the following command.

```
git clone https://github.com/aws/efs-utils
```

Now that you have the package, you can install it. This installation is handled
differently depending on the Linux distribution of your on-premises client. The following
distributions are supported:

- Amazon Linux 2
- Amazon Linux
- Red Hat Enterprise Linux (and derivatives such as CentOS) version 8 and newer
- Ubuntu 16.04 LTS and newer

###### To build and install amazon-efs-utils as an RPM package

1. Open a terminal on your client and navigate to the directory that has the cloned
   amazon-efs-utils package from GitHub.
2. Build the package with the following command.

```
make rpm
```

###### Note

If you haven't already, install the rpm-builder package with the following
command.

```
sudo yum -y install rpm-build
```

3. Install the package with the following command.

```
sudo yum -y install build/amazon-efs-utils*rpm
```

###### To build and install amazon-efs-utils as an deb package

1. Open a terminal on your client and navigate to the directory that has the cloned
   amazon-efs-utils package from GitHub.
2. Build the package with the following command.

```
./build-deb.sh
```

3. Install the package with the following command.

```
sudo apt-get install build/amazon-efs-utils*deb
```

After the package is installed, configure amazon-efs-utils for use in your AWS Region with
Direct Connect or VPN.

###### To configure amazon-efs-utils for use in your AWS Region

1. Access the terminal for your EC2 instance through Secure Shell (SSH), and
   log in with the appropriate user name. For more information, see [Connect to your
   EC2 instance](../../../AWSEC2/latest/UserGuide/connect.md "../../../AWSEC2/latest/UserGuide/connect.md") in the
   _Amazon EC2 User Guide_.
2. Using your text editor of choice, open the
   `/etc/amazon/efs/efs-utils.conf` file.
3. Find the line `“dns_name_format =
{fs_id}.efs.`{region}`.amazonaws.com”`.
4. Change `{region}` with the ID for your AWS
   Region, for example `us-west-2`.

To mount the EFS file system on your on-premises client, first open a terminal on your
on-premises Linux client. To mount the system, you need the file system ID, the mount target
IP address for one of your mount targets, and the file system's AWS Region. If you created
multiple mount targets for your file system, then you can choose any one of these.

When you have that information, you can mount your file system in three steps:

###### To create a mount directory

1. Make a directory for the mount point with the following command.

```
mkdir ~/efs
```

2. Choose your preferred IP address of the mount target in the Availability Zone. You can
   measure the latency from your on-premises Linux clients. To do so, use a terminal-based
   tool like `ping` against the IP address of your EC2 instances in different
   Availability Zones to find the one with the lowest latency.

###### To update `/etc/hosts`

- Add an entry to your local `/etc/hosts` file with the file system ID and
  the mount target IP address, in the following format.

```
`mount-target-IP-Address` `file-system-ID`.efs.`region`.amazonaws.com
```

```
192.0.2.0 fs-12345678.efs.us-west-2.amazonaws.com
```

###### To make a mount directory

1. Make a directory for the mount point with the following command.

```
mkdir ~/efs
```

2. Run the mount command to mount the file system.

```
sudo mount -t efs fs-12345678 ~/efs
```

If you want to use encryption of data in transit, your mount command looks something
like the following.

```
sudo mount -t efs -o tls fs-12345678 ~/efs
```
