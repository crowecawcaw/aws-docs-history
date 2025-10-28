# Enabling automatic mounting on new

EC2 Linux instances

When you create a new EC2 Linux instance using the Amazon EC2 launch instance wizard,
you can configure it to mount your Amazon EFS file system automatically. The EC2 instance
mounts the file system automatically the instance first launched and also whenever it
restarts.

This method uses the EFS mount helper to mount the file system update the
/etc/fstab file on the EC2 instance. The mount helper is part of the [amazon-efs-utils](using-amazon-efs-utils.md "using-amazon-efs-utils.md") set of
tools.

###### Note

EFS file systems do not support mounting on EC2 Mac instances running
macOS Big Sur or Monterey at instance launch.

###### Note

You can't use Amazon EFS with Microsoft Windows–based EC2
instances.

Before you can launch and connect to an EC2 instance, you need to create a key
pair. For more information, see [Amazon EC2 key pairs and Amazon EC2
instances](../../../AWSEC2/latest/UserGuide/ec2-key-pairs.md "../../../AWSEC2/latest/UserGuide/ec2-key-pairs.md") in the _Amazon EC2 User Guide_ to create a key pair.

###### To configure your EC2 instance to mount an EFS file system

automatically at launch

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. Choose **Launch Instance**.
3. In **Step 1: Choose an Amazon Machine Image (AMI)**, find an Amazon Linux
   AMI at the top of the list and choose **Select**.
4. In **Step 2: Choose an Instance Type**, choose **Next:
   Configure Instance Details**.
5. In **Step 3: Configure Instance Details**, provide the following information:
   - For **Network**, choose the entry for the same VPC that the EFS
     file system you're mounting is in.
   - For **Subnet**, choose a default subnet in any Availability Zone.
   - For **File systems**, choose the EFS file system that you want to
     mount. The path shown next the file system ID is the mount point that the
     EC2 instance will use, which you can change.
   - Under **Advanced Details**, the **User data** is
     automatically generated, and includes the commands needed to mount the
     EFS file systems you specified under **File
     systems**.

6. Choose **Next: Add Storage**.
7. Choose **Next: Add Tags**.
8. Name your instance and choose **Next: Configure Security
   Group**.
9. In **Step 6: Configure Security Group**, set **Assign a
   security group** to **Select an existing security
   group**. Choose the default security group to make sure that it can
   access your EFS file system.

You can't access your EC2 instance by Secure Shell (SSH) using this security
group. For access by SSH, later you can edit the default security and add a rule to
allow SSH or a new security group that allows SSH. You can use the following
settings:

    * **Type:** SSH
    * **Protocol:** TCP
    * **Port Range:** 22
    * **Source:** Anywhere 0.0.0.0/0

10. Choose **Review and Launch**.
11. Choose **Launch**.
12. Select the check box for the key pair that you created, and then choose
    **Launch Instances**.
    Your EC2 instance is now configured to mount the EFS file system at
    launch and whenever it's rebooted.
