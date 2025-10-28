# Tutorial: Create an EFS file system and mount it on an

EC2 instance using the AWS CLI

Create an encrypted EFS file system, mount it on an EC2 instance in your
VPC, and test the setup using the AWS CLI.

###### Note

In the [Getting started](getting-started.md "getting-started.md") tutorial,
you use the console to create Amazon EC2 and EFS resources. In this tutorial, you use
the AWS CLI to do the same—primarily to familiarize yourself with the Amazon EFS API.

In this tutorial, you create the following AWS resources in your account:

- Amazon EC2 resources:
  - Two security groups (for your EC2 instance and EFS file
    system).

  You add rules to these security groups to authorize appropriate inbound/outbound
  access. Doing this allows your EC2instance to connect to the file system through
  the mount target by using a standard NFSv4.1 TCP port.
  - An EC2 instance in your VPC.

- Amazon EFS resources:

      + A file system.
      + A mount target for your file system.


      To mount your file system on an EC2 instance you need to create a mount
       target in your VPC. You can create one mount target in each of the Availability Zones in your
       VPC. For more information, see [How Amazon EFS works](how-it-works.md "how-it-works.md").

  Then, you test the file system on your EC2 instance. The cleanup step at the end of
  the tutorial provides information for you to remove these resources.

The tutorial creates all these resources in the US West (Oregon) Region
(`us-west-2`). Whichever AWS Region you use, be sure to use it consistently. All
of your resources—your VPC, EC2 resources, and EFS
resources—must be in the same AWS Region.

###### Topics

- [Prerequisites](#wt1-prepare "#wt1-prepare")
- [Setting up the AWS CLI](#wt1-setup-awscli "#wt1-setup-awscli")
- [Step 1: Create EC2 resources](#wt1-create-ec2-resources "#wt1-create-ec2-resources")
- [Step 2: Create EFS resources](#wt1-create-efs-resources "#wt1-create-efs-resources")
- [Step 3: Mount the file system on the EC2 instance and
  test](#wt1-test "#wt1-test")
- [Step 4: Clean up](#wt1-clean-up "#wt1-clean-up")

## Prerequisites

- You can use the root credentials of your AWS account to sign in to the console and
  try the getting started exercise. However, AWS Identity and Access Management (IAM) recommends that you do not
  use the root credentials of your AWS account. Instead, create an administrator user in
  your account and use those credentials to manage resources in your account. For more information, see
  [Assign AWS account access for an IAM Identity Center user](../../../singlesignon/latest/userguide/get-started-assign-account-access-user.md "../../../singlesignon/latest/userguide/get-started-assign-account-access-user.md") in the _AWS IAM Identity Center User Guide_.
- You can use a default VPC or a custom VPC that you have created in your account. For
  this walkthrough, the default VPC configuration works. However, if you use a custom VPC,
  verify the following:
  - DNS hostnames are enabled. For more information, see [DNS attributes in your
    VPC](../../../vpc/latest/userguide/vpc-dns.md#vpc-dns-support "../../../vpc/latest/userguide/vpc-dns.md#vpc-dns-support") in the _Amazon VPC User Guide_.
  - The internet gateway is attached to your VPC. For more information, see [Connect to the internet using an internet
    gateway](../../../vpc/latest/userguide/VPC_Internet_Gateway.md "../../../vpc/latest/userguide/VPC_Internet_Gateway.md") in the
    _Amazon VPC User Guide_.
  - The VPC subnets are configured to request public IP addresses for instances
    launched in the VPC subnets. For more information, see [IP addressing for your VPCs and subnets](../../../vpc/latest/userguide/vpc-ip-addressing.md "../../../vpc/latest/userguide/vpc-ip-addressing.md") in the
    _Amazon VPC User Guide_.
  - The VPC route table includes a rule to send all Internet-bound traffic to the
    Internet gateway.

- You need to set up the AWS CLI and add the adminuser profile.

## Setting up the AWS CLI

Use the following instructions to set up the AWS CLI and user profile.

###### To set up the AWS CLI

1. Download and configure the AWS CLI. For instructions, see
   [Get started with the AWS CLI](../../../cli/latest/userguide/cli-chap-getting-started.md "../../../cli/latest/userguide/cli-chap-getting-started.md") in the
   _AWS Command Line Interface User Guide_.
2. Set profiles.

You store user credentials in the AWS CLI `config` file. The example
CLI commands in this tutorial specify the adminuser profile. Create the adminuser profile
in the `config` file. You can also set the administrator user profile
as the default in the `config` file as shown.

```
[profile adminuser]
aws_access_key_id = `admin user access key ID`
aws_secret_access_key = `admin user secret access key`
region = us-west-2

[default]
aws_access_key_id = `admin user access key ID`
aws_secret_access_key = `admin user secret access key`
region = us-west-2
```

The preceding profile also sets the default AWS Region. If you don't specify a
Region in the CLI command, the us-west-2 region is assumed. 3. Verify the setup by entering the following command at the command prompt. Both of
these commands don't provide credentials explicitly, so the credentials of the default
profile are used.

    * Try the help command


    You can also specify the user profile explicitly by adding the
     `--profile` parameter.



    ```
    aws help
    ```


    ```
    aws help \
    --profile adminuser
    ```

## Step 1: Create EC2 resources

In this step, you do the following:

- Create two security groups.
- Add rules to the security groups to authorize additional access.
- Launch an EC2 instance. You create and mount an EFS file system on
  this instance in the next step.

### Step 1.1: Create two security groups

In this section, you create security groups in your VPC for your EC2 instance and
EFS mount target. Later in the tutorial, you assign these security groups to an
EC2 instance and an EFS mount target. For information about security
groups, see [Amazon EC2 security
groups for Linux instances](../../../AWSEC2/latest/UserGuide/ec2-security-groups.md#vpc-security-groups "../../../AWSEC2/latest/UserGuide/ec2-security-groups.md#vpc-security-groups") .

###### To create security groups

1. Create two security groups using the `create-security-group` CLI
   command:
   1. Create a security group (`efs-walkthrough1-ec2-sg`) for your
      EC2 instance, and provide your VPC ID.

   ```
   $ aws ec2 create-security-group \
   --region us-west-2 \
   --group-name efs-walkthrough1-ec2-sg \
   --description "Amazon EFS walkthrough 1, SG for EC2 instance" \
   --vpc-id `vpc-id-in-us-west-2` \
   --profile adminuser
   ```

   Write down the security group ID. The following is an example response.

   ```
   {
       "GroupId": "sg-aexample"
   }
   ```

   You can find the VPC ID using the following command.

   ```
   $ aws  ec2 describe-vpcs
   ```

   2. Create a security group (`efs-walkthrough1-mt-sg`) for your
      EFS mount target. You need to provide your VPC ID.

   ```
   $ aws ec2 create-security-group \
   --region us-west-2 \
   --group-name efs-walkthrough1-mt-sg \
   --description "Amazon EFS walkthrough 1, SG for mount target" \
   --vpc-id `vpc-id-in-us-west-2` \
   --profile adminuser
   ```

   Write down the security group ID. The following is an example response.

   ```
   {
       "GroupId": "sg-aexample"
   }
   ```

2. Verify the security groups.

```
aws ec2 describe-security-groups \
--group-ids `list of security group IDs separated by space` \
--profile `adminuser` \
--region us-west-2
```

Both should have only one outbound rule that allows all traffic to leave.

In the next section, you authorize additional access that enables the following:

    * Enable you to connect to your EC2 instance.
    * Enable traffic between an EC2 instance and an EFS mount target
     (with which you associate these security groups later in this tutorial).

### Step 1.2: Add rules to the security groups to authorize

inbound/outbound access

In this step, you add rules to the security groups to authorize inbound/outbound
access.

###### To add rules

1. Authorize incoming Secure Shell (SSH) connections to the security group for your
   EC2 instance (`efs-walkthrough1-ec2-sg`) so you can connect to your
   EC2 instance using SSH from any host.

```
$ aws ec2 authorize-security-group-ingress \
--group-id `id of the security group created for EC2 instance` \
--protocol tcp \
--port 22 \
--cidr 0.0.0.0/0 \
--profile adminuser \
--region us-west-2
```

Verify that the security group has the inbound and outbound rule you added.

```
aws ec2 describe-security-groups \
--region us-west-2 \
--profile adminuser \
--group-id `security-group-id`
```

2. Authorize inbound access to the security group for the EFS mount target
   (`efs-walkthrough1-mt-sg`).

At the command prompt, run the following AWS CLI
`authorize-security-group-ingress` command using the adminuser profile to
add the inbound rule.

```
$ aws ec2 authorize-security-group-ingress \
--group-id `ID of the security group created for Amazon EFS mount target` \
--protocol tcp \
--port 2049 \
--source-group `ID of the security group created for EC2 instance` \
--profile adminuser \
--region us-west-2
```

3. Verify that both security groups now authorize inbound access.

```
aws ec2 describe-security-groups \
--group-names efs-walkthrough1-ec2-sg   efs-walkthrough1-mt-sg \
--profile adminuser \
--region us-west-2
```

### Step 1.3: Launch an EC2 instance

In this step, you launch an EC2 instance.

###### To launch an EC2 instance

1.  Gather the following information that you need to provide when launching an
    EC2 instance:
    - Key pair name. For instructions to create a key pair, see [Create a key
      pair for your Amazon EC2 instance](../../../AWSEC2/latest/UserGuide/create-key-pairs.md "../../../AWSEC2/latest/UserGuide/create-key-pairs.md") in the _Amazon EC2 User Guide_.
    - The ID of the Amazon Machine Image (AMI) you want to launch.

    The AWS CLI command that you use to launch an EC2 instance requires the ID
    of the Amazon Machine Image (AMI) that you want to deploy as a parameter. The
    exercise uses the Amazon Linux HVM AMI.

    ###### Note

    You can use most general purpose Linux-based AMIs. If you use another Linux
    AMI, make sure that you use your distribution's package manager to install
    the NFS client on the instance. Also, you might need to add software packages as
    you need them.

    For the Amazon Linux HVM AMI, you can find the latest IDs at [Amazon Linux AMI](https://aws.amazon.com/amazon-linux-ami/ "https://aws.amazon.com/amazon-linux-ami/"). You choose the
    ID value from the Amazon Linux AMI IDs table as follows:

        + Choose the **US West Oregon** region. This walkthrough
         assumes you are creating all resources in the US West (Oregon) Region
         (us-west-2).
        + Choose the **EBS-backed HVM 64-bit** type (because in the
         CLI command you specify the `t2.micro` instance type, which does not
         support instance store).

    - ID of the security group you created for an EC2 instance.
    - AWS Region. This walkthrough uses the us-west-2 region.
    - Your VPC subnet ID where you want to launch the instance. You can get list of
      subnets using the `describe-subnets` command.

    ```
    $ aws ec2 describe-subnets \
    --region us-west-2 \
    --filters "Name=vpc-id,Values=`vpc-id`" \
    --profile adminuser
    ```

    After you choose the subnet ID, write down the following values from the
    `describe-subnets` result:

        + Subnet ID – You need this value when
         you create a mount target. In this exercise, you create a mount target in the
         same subnet where you launch an EC2 instance.
        + Availability Zone of the subnet – You need
         this value to construct your mount target DNS name, which you use to mount a
         file system on the EC2 instance.

2.  Run the following AWS CLI `run-instances` command to launch an EC2
    instance.

```
$ aws ec2 run-instances \
--image-id `AMI ID` \
--count 1 \
--instance-type t2.micro \
--associate-public-ip-address \
--key-name `key-pair-name` \
--security-group-ids `ID of the security group created for EC2 instance` \
--subnet-id `VPC subnet ID` \
--region us-west-2 \
--profile adminuser
```

3. Write down the instance ID returned by the `run-instances`
   command.
4. The EC2 instance you created must have a public DNS name that you use to
   connect to the EC2 instance and mount the file system on it. The public DNS name
   is of the form:

```
ec2-xx-xx-xx-xxx.compute-1.amazonaws.com
```

Run the following CLI command and write down the public DNS name.

```
aws ec2 describe-instances \
--instance-ids `EC2 instance ID` \
--region us-west-2 \
--profile adminuser
```

If you don't find the public DNS name, check the configuration of the VPC in which
you launched the EC2 instance. For more information, see [Prerequisites](#wt1-prepare "#wt1-prepare"). 5. (Optional) Assign a name to the EC2 instance that you created. To do so, add
a tag with the key name and value set to the name that you want to assign to the
instance. You do this by running the following AWS CLI `create-tags` command.

```
$  aws ec2 create-tags \
--resources  `EC2-instance-ID` \
--tags Key=Name,Value=`Provide-instance-name`  \
--region us-west-2 \
--profile adminuser
```

## Step 2: Create EFS resources

In this step, you do the following:

- Create an encrypted EFS file system.
- Enable lifecycle management.
- Create a mount target in the Availability Zone where you have your EFS instance
  launched.

### Step 2.1: Create an EFS file

system

In this step, you create an EFS file system. Write down the
`FileSystemId` to use later when you create mount targets for the file system
in the next step.

###### To create a file system

- Create a file system with the optional `Name` tag.
  1.  At the command prompt, run the following AWS CLI `create-file-system`
      command.

  ```
  `$` aws efs create-file-system \
  --encrypted \
  --creation-token FileSystemForWalkthrough1 \
  --tags Key=Name,Value=SomeExampleNameValue \
  --region us-west-2 \
  --profile adminuser
  ```

  You get the following response.

  ```
  `{
   "OwnerId": "111122223333",
   "CreationToken": "FileSystemForWalkthrough1",
   "FileSystemId": "fs-c657c8bf",
   "CreationTime": 1548950706.0,
   "LifeCycleState": "creating",
   "NumberOfMountTargets": 0,
   "SizeInBytes": {
   "Value": 0,
   "ValueInIA": 0,
   "ValueInStandard": 0
   },
   "PerformanceMode": "generalPurpose",
   "Encrypted": true,
   "KmsKeyId": "arn:aws:kms:us-west-2:111122223333:a5c11222-7a99-43c8-9dcc-abcdef123456",
   "ThroughputMode": "bursting",
   "Tags": [
   {
   "Key": "Name",
   "Value": "SomeExampleNameValue"
   }
   ]
  }`
  ```

  2.  Note the `FileSystemId` value. You need this value when you create a
      mount target for this file system in [Step 2.3: Create a mount target](#wt1-create-mount-target "#wt1-create-mount-target").

### Step 2.2: Enable lifecycle management

In this step, you enable lifecycle management on your ﬁle system in order to use the
EFS Infrequent Access (IA) storage class. To learn more, see [Managing storage lifecycle](lifecycle-management-efs.md "lifecycle-management-efs.md") and [EFS storage classes](features.md#storage-classes "features.md#storage-classes").

###### To enable lifecycle management

- At the command prompt, run the following AWS CLI `put-lifecycle-configuration`
  command.

```
`$` `aws efs put-lifecycle-configuration \
--file-system-id fs-c657c8bf \
--lifecycle-policies TransitionToIA=AFTER_30_DAYS \
--region us-west-2 \
--profile adminuser`

```

You get the following response.

```
{
  "LifecyclePolicies": [
    {
        "TransitionToIA": "AFTER_30_DAYS"
    }
  ]
}

```

### Step 2.3: Create a mount target

In this step, you create a mount target for your file system in the Availability Zone where
you have your EC2 instance launched.

1. Make sure you have the following information:
   - ID of the file system (for example, `fs-example`) for which you are
     creating the mount target.
   - VPC subnet ID where you launched the EC2 instance in
     [Step 1: Create EC2 resources](#wt1-create-ec2-resources "#wt1-create-ec2-resources").

   For this tutorial, you create the mount target in the same subnet in which you
   launched the EC2 instance, so you need the subnet ID (for example,
   `subnet-example`).
   - ID of the security group you created for the mount target in the preceding
     step.

2. At the command prompt, run the following AWS CLI `create-mount-target`
   command.

```
$ aws efs create-mount-target \
--file-system-id `file-system-id` \
--subnet-id  `subnet-id` \
--security-group `ID-of-the security-group-created-for-mount-target` \
--region us-west-2 \
--profile adminuser
```

You get the following response.

```
{
    "MountTargetId": "fsmt-example",
    "NetworkInterfaceId": "eni-example",
    "FileSystemId": "fs-example",
    "PerformanceMode" : "generalPurpose",
    "LifeCycleState": "available",
    "SubnetId": "fs-subnet-example",
    "OwnerId": "account-id",
    "IpAddress": "xxx.xx.xx.xxx"
}
```

3. You can also use the `describe-mount-targets` command to get descriptions
   of mount targets you created on a file system.

```
$ aws efs describe-mount-targets \
--file-system-id `file-system-id` \
--region us-west-2 \
--profile adminuser
```

## Step 3: Mount the file system on the EC2 instance and

test

In this step, you do the following:

- Gather required information.
- Install the NFS client on your EC2 instance.
- Mount the file system on your EC2 instance and test.

###### Topics

- [Step 3.1: Gather Information](#wt1-connect-test-gather-info "#wt1-connect-test-gather-info")
- [Step 3.2: Install the NFS client on your
  EC2 instance](#wt1-connect-install-nfs-client "#wt1-connect-install-nfs-client")
- [Step 3.3: Mount the file system on your EC2
  instance and test](#wt1-mount-fs-and-test "#wt1-mount-fs-and-test")

### Step 3.1: Gather Information

Make sure you have the following information as you follow the steps in this
section:

- Public DNS name of your EC2 instance in the following format:

```
ec2-xx-xxx-xxx-xx.`aws-region`.compute.amazonaws.com
```

- DNS name of your file system. You can construct this DNS name using the following
  generic form:

```
`file-system-id`.efs.`aws-region`.amazonaws.com
```

The EC2 instance on which you mount the file system by using the mount target
can resolve the file system's DNS name to the mount target's IP address.

###### Note

Amazon EFS doesn't require that your EC2 instance have either a public IP address or
public DNS name. The requirements listed preceding are just for this walkthrough example
to ensure that you can connect by using SSH into the instance from outside the VPC.

### Step 3.2: Install the NFS client on your

EC2 instance

You can connect to your EC2 instance from Windows or from a computer running
Linux, or macOS X, or any other Unix variant.

###### To install an NFS client

1. Connect to your EC2 instance. For more information, see [Connect to your
   EC2 instance](../../../AWSEC2/latest/UserGuide/connect.md "../../../AWSEC2/latest/UserGuide/connect.md") in the
   _Amazon EC2 User Guide_.
2. Execute the following commands on the EC2 instance by using the SSH
   session:
   1. (Optional) Get updates and reboot.

   ```
   `$` `sudo yum -y update`
   $  sudo reboot
   ```

   After the reboot, reconnect to your EC2 instance. 2. Install the NFS client.

   ```
   `$` `sudo yum -y install nfs-utils`
   ```

   ###### Note

   If you choose the **Amazon Linux AMI 2016.03.0** Amazon Linux
   AMI when launching your EC2 instance, you don't need to install
   `nfs-utils` because it is already included in the AMI by
   default.

### Step 3.3: Mount the file system on your EC2

instance and test

Now you mount the file system on your EC2 instance.

1. Make a directory ("efs-mount-point").

```
`$` `mkdir ~/efs-mount-point`
```

2. Mount the EFS file system.

```
`$` `sudo mount -t nfs -o nfsvers=4.1,rsize=1048576,wsize=1048576,hard,timeo=600,retrans=2,noresvport `mount-target-DNS`:/ ~/efs-mount-point`
```

The EC2 instance can resolve the mount target DNS name to the IP address. You can
optionally specify the IP address of the mount target directly.

```
`$` `sudo mount -t nfs -o nfsvers=4.1,rsize=1048576,wsize=1048576,hard,timeo=600,retrans=2,noresvport `mount-target-ip`:/  ~/efs-mount-point`
```

3. Now that you have the EFS file system mounted on your EC2 instance, you
   can create files.
   1. Change the directory.

   ```
   `$` `cd ~/efs-mount-point`
   ```

   2. List the directory contents.

   ```
   `$` `ls -al`
   ```

   It should be empty.

   ```
   drwxr-xr-x 2 root     root     4096 Dec 29 22:33 .
   drwx------ 4 ec2-user ec2-user 4096 Dec 29 22:54 ..
   ```

   3. The root directory of a file system, upon creation, is owned by and is writable
      by the root user, so you need to change permissions to add files.

   ```
   `$` `sudo chmod go+rw .`
   ```

   Now, if you try the `ls -al` command you see that the permissions
   have changed.

   ```
   drwxrwxrwx 2 root     root     4096 Dec 29 22:33 .
   drwx------ 4 ec2-user ec2-user 4096 Dec 29 22:54 ..
   ```

   4. Create a text file.

   ```
   `$` `touch test-file.txt`
   ```

   5. List directory content.

   ```
   `$` `ls -l`
   ```

You now have successfully created and mounted an EFS file system on your
EC2 instance in your VPC.

The file system you mounted doesn't persist across reboots. To automatically
remount the directory, you can use the `fstab` file. If
you are using an Auto Scaling group to launch EC2 instances, you can also set scripts
in a launch configuration.

## Step 4: Clean up

If you no longer need the resources you created, you should remove them. You can do this
with the CLI.

- Remove EC2 resources (the EC2 instance and the two security groups).
  Amazon EFS deletes the network interface when you delete the mount target.
- Remove EFS resources (file system, mount target).

###### To delete AWS resources created in this walkthrough

1. Terminate the EC2 instance you created for this tutorial.

```
$ aws ec2 terminate-instances \
--instance-ids `instance-id` \
--profile adminuser
```

You can also delete EC2 resources using the console. For instructions, see
[Terminate an instance](../../../AWSEC2/latest/UserGuide/terminating-instances.md#terminating-instances-console "../../../AWSEC2/latest/UserGuide/terminating-instances.md#terminating-instances-console"). 2. Delete the mount target.

You must delete the mount targets created for the file system before deleting the file
system. You can get a list of mount targets by using the
`describe-mount-targets` CLI command.

```
$  aws efs describe-mount-targets \
--file-system-id `file-system-ID` \
--profile adminuser \
--region `aws-region`
```

Then delete the mount target by using the `delete-mount-target` CLI
command.

```
$ aws efs delete-mount-target \
--mount-target-id `ID-of-mount-target-to-delete` \
--profile adminuser \
--region `aws-region`
```

3. (Optional) Delete the two security groups you created. You don't pay for creating
   security groups.

You must delete the mount target's security group first, before deleting the
EC2 instance's security group. The mount target's security group has a rule that
references the EC2 security group. Therefore, you cannot first delete the
EC2 instance's security group.

For instructions, see [Delete your security
group](../../../cli/latest/userguide/cli-services-ec2-sg.md#deleting-a-security-group "../../../cli/latest/userguide/cli-services-ec2-sg.md#deleting-a-security-group") in the _Amazon EC2 User Guide_. 4. Delete the file system by using the `delete-file-system` CLI command. You
can get a list of your file systems by using the `describe-file-systems` CLI
command. You can get the file system ID from the response.

```
aws efs describe-file-systems \
--profile adminuser \
--region `aws-region`
```

Delete the file system by providing the file system ID.

```
$ aws efs delete-file-system \
--file-system-id `ID-of-file-system-to-delete` \
--region `aws-region` \
--profile adminuser
```
