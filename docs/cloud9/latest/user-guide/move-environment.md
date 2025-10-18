AWS Cloud9 is no longer available to new customers. Existing customers of 
 AWS Cloud9 can continue to use the service as normal. 
 [Learn more](https://aws.amazon.com/blogs/devops/how-to-migrate-from-aws-cloud9-to-aws-ide-toolkits-or-aws-cloudshell/ "https://aws.amazon.com/blogs/devops/how-to-migrate-from-aws-cloud9-to-aws-ide-toolkits-or-aws-cloudshell/")

# Moving an AWS Cloud9 IDE
 from
 Amazon EBS volumes

You can move an AWS Cloud9 development environment from one Amazon EC2 instance to another. For example, you might want
 to do the following actions:


* Transfer an environment from an Amazon EC2 instance that's impaired or performing in unexpected
 ways compared with a healthy instance.
* Transfer an environment from an existing instance to one that has the latest system
 updates.
* Increase or decrease an instance's compute resources because the environment is overused or
 underused on the current instance.
You can upgrade from one AWS Cloud9 supported AMI to another by migrating to a new AWS Cloud9
 EC2 environment, while keeping the project files. You may want to upgrade to another version of the AMI
 because: 


* The AMI of the current environment has reached end-of-life and is no longer
 supported.
* The package that you need is outdated in the current AMI.
You can also resize the Amazon Elastic Block Store (Amazon EBS) volume that's associated with an Amazon EC2 instance
 for an environment. For example, you might want to do one or both of the following actions:


* Increase the size of a volume because you're running out of storage space on the
 instance.
* Decrease the size of a volume because you don't want to pay for extra storage space that
 you aren't using.
Before you move or resize an environment, you can try stopping some running processes in the environment
 or adding a swap file to the environment. For more information about dealing with low memory or high
 CPU usage, see [Troubleshooting](troubleshooting.md#troubleshooting-ide-low-memory "troubleshooting.md#troubleshooting-ide-low-memory").

###### Note

This topic only describes moving an environment from one Amazon EC2 instance to another or resizing
 an Amazon EBS volume. To resize an environment from one of your own servers or to change the storage
 space for one of your own servers, refer to your server's documentation.

Last, you can encrypt Amazon EBS resources to ensure the security of both data-at-rest and
 data-in-transit between an instance and its attached EBS storage.


## Move an environment


Before you start the move process, note the following conditions:



* You can't move an environment to an Amazon EC2 instance of the same type. When you move, you must
 choose a different Amazon EC2 instance type for the new instance.


###### Important

If you move your environment to another Amazon EC2 instance type, that instance type must
 also be supported by AWS Cloud9 in the current AWS Region. To check the instance types that
 are available in each Region, go to the **Configure settings** page
 that's displayed when [creating an EC2 environment
 with the console](create-environment-main.md#create-environment-console "create-environment-main.md#create-environment-console"). Your choice in the **Instance type** section
 is determined by the AWS Region that's selected in the upper right of the console.
* You must stop the Amazon EC2 instance that's associated with an environment before you can change
 the instance type. While the instance is stopped, you and any members can't use the environment
 that's associated with the stopped instance.
* AWS moves the instance to new hardware, however, the instance's ID doesn't
 change.
* If the instance is running in an Amazon VPC and has a public IPv4 address, AWS releases
 the address and gives the instance a new public IPv4 address. The instance retains its
 private IPv4 addresses and any Elastic IP addresses or IPv6 addresses.
* Plan for downtime while your instance is stopped. The process might take several
 minutes.

###### To move an environment

1. (Optional) If the new instance type requires drivers that aren't installed on the
 existing instance, connect to your instance and install those drivers. For more
 information, see [Compatibility for resizing instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-resize.html#resize-limitations "https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-resize.html#resize-limitations") in the
 *Amazon EC2 User Guide*.
2. Close all web browser tabs that are currently displaying the environment.


###### Important

If you don't close all of the web browser tabs that are currently displaying the
 environment, AWS Cloud9 might interfere with completing this procedure. Specifically, AWS Cloud9 might
 try at the wrong time during this procedure to restart the Amazon EC2 instance that's
 associated with the environment. The instance must stay stopped until the very last step in
 this procedure.
3. Sign in to the AWS Management Console, if you're not already signed in, at [https://console.aws.amazon.com](https://console.aws.amazon.com "https://console.aws.amazon.com").


We recommend you sign in using administrator-level credentials in your AWS account.
 If you can't do this, check with your AWS account administrator.
4. Open the Amazon EC2 console. To do this, in the **Services** list, choose
 **EC2**.
5. In the AWS navigation bar, choose the AWS Region that contains the environment that you
 want to move (for example, **US East (Ohio)**).
6. In the service navigation pane, expand **Instances**, and then choose
 **Instances**.
7. In the list of instances, choose the one that's associated with the environment that you
 want to move. For an EC2 environment, the instance name starts with `aws-cloud9-`
 followed by the environment name. For example, if the environment is named `my-demo-environment`,
 the instance name starts with `aws-cloud9-my-demo-environment`.
8. If the **Instance State** is not **Stopped**, choose
 **Actions**, **Instance state**,
 **Stop**. When prompted, choose **Yes, Stop**. It can
 take a few minutes for the instance to stop.
9. After the **Instance State** is **stopped**, with
 the instance still selected, choose **Actions**, **Instance
 Settings**, **Change Instance Type**.
10. In the **Change Instance Type** dialog box, choose the new
 **Instance Type** for the environment to use.


###### Note

If the instance type that you want doesn't appear in the list, it's not compatible
 with the configuration of the instance. For example, the instance might not be
 compatible because of the virtualization type.
11. (Optional) If the instance type that you chose supports EBS–optimization, select
 **EBS-optimized** to enable EBS–optimization, or clear
 **EBS-optimized** to disable EBS–optimization.


###### Note

If the instance type you chose is EBS–optimized by default,
 **EBS-optimized** is selected and you can't clear it.
12. Choose **Apply** to accept the new settings.


###### Note

If you didn't choose a different instance type for **Instance
 Type** earlier in this procedure, nothing happens after you choose
 **Apply**.
13. Reopen the environment. For more information, see [Opening an environment in AWS Cloud9](open-environment.md "open-environment.md").

For more information about the preceding procedure, see [Changing the instance type](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-resize.html "https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-resize.html") in the
 *Amazon EC2 User Guide*.


## Moving an AWS Cloud9 EC2 environment to a different Amazon
 Machine Image (AMI)


 


This topic explains how to migrate an AWS Cloud9 EC2 environment from one Amazon Linux AMI to another AWS Cloud9
 supported AMI. 


###### Note

If you want to move your environment to a new instance without updating the OS version,
 see [Move an environment](#move-environment-move "#move-environment-move").


You can migrate your data between environments using one of the following
 procedures:


###### To move an environment by downloading archive to a local machine

1. Create a new environment in the same Availability Zone with a different base
 image:


	1. Complete the steps in the [Creating an EC2 Environment](create-environment-main.md "create-environment-main.md") section to
	 create a new environment. 
	
	
	###### Note
	
	While choosing the **Platform**, select the platform that you
	 want to migrate your environment to.
	2. By default, environments are created with 10 GiB volume. If you don't have
	 sufficient space to upload or unpack the archive to the new environment, complete the
	 steps in [Resize an Amazon EBS volume that an environment
	 uses](move-environment-resize.md "move-environment-resize.md") procedure to resize Amazon EBS volume
	 size.
2. Open the environment that you want to migrate in the AWS Cloud9 IDE.
3. After the AWS Cloud9 IDE loads, select **File** > **Download
 project** from the menu to download the archive with the contents of the
 environment project directory.
4. Open AWS Cloud9 IDE in the new environment.
5. Choose **File** > **Upload local files...** to
 upload the archive.
6. (Optional) To back up the old `.c9` directory to
 `.c9.backup`, in the environment terminal, run the following command: 


```
cp .c9 .c9.backup
```

You may need these backup files if you want to restore the configuration files
 later.
7. To unpack the archive, run the following command: 



```
tar xzvf <old_environment_name>.tar.gz -C ~/
```
8. To delete the archive from the project directory, run the following command:


```
rm <old_environment_name>.tar.gz
```

Ensure that the new environment works as expected.
9. You can now delete the old environment.

###### To move an environment using Amazon EBS volume

If you are not able to download the archive, or if the resulting archive is too large,
 you can use the Amazon EBS volume to migrate. Also, this method enables you to copy files that
 are located outside the `~/environment` directory.

1. Close all AWS Cloud9 IDE tabs that are open in the existing environment.
2. Complete the following steps to stop the existing instance:


	1. In the AWS Cloud9 console, select the environment to navigate to view its
	 details.
	2. On the **Environment details** page, under the **EC2
	 instance** tab, choose **Manage EC2 instance**.
	3. In the EC2 console, select the instance to navigate to the instance details.
	4. Ensure that the **Instance state** is set to
	 **Stopped**. If not, select **Stop instance** from
	 the **Instance state** dropdown list. When prompted, choose
	 **Stop**. It can take a few minutes for the instance to stop.
3. Create a new environment in the same Availability Zone with a different base
 image:


	1. Complete the steps in the [Creating an EC2 Environment](create-environment-main.md "create-environment-main.md") section to
	 create a new environment. 
	
	
	###### Note
	
	While choosing the **Platform**, select the platform that you
	 want to migrate your environment to.
	2. By default, environments are created with 10 GiB volume. If you don’t have
	 sufficient space to move files from the source volume to the new environment, complete
	 the steps in [Resize an Amazon EBS volume that an environment
	 uses](move-environment-resize.md "move-environment-resize.md") procedure to resize Amazon EBS
	 volume size.
4. Complete the following steps to detach the volume from the existing instance:


	1. On the **Instance summary** page, choose the
	 **Storage** tab and select the volume. The device name of the
	 selected volume must be the same as the one that is specified in the **Root
	 device name** of the **Root device details**
	 section.
	2. On the volume details page, choose **Actions** > **Detach
	 volume**.
	3. After the volume is successfully detached, choose **Actions** >
	 **Attach volume** and then find and select the instance of the new
	 environment from the dropdown list. The name of the Amazon EC2 instance that you select
	 must contain the AWS Cloud9 environment name prefixed with `aws-cloud9`.
5. Open AWS Cloud9 IDE in the new environment.
6. After the environment loads, to identify the device of the newly attached volume, run
 the following command in the terminal: 


```
lsblk
```

In the following sample output, partition `nvme0n1` of root device
 `nvme0n1p1` is already mounted, hence the `nvme1n1p1` partition
 must also be mounted. The full path for its device is `/dev/nvme1n1p1`:



```
Admin:~/environment $ lsblk
NAME          MAJ:MIN RM SIZE RO TYPE MOUNTPOINTS
nvme0n1       259:0    0  10G  0 disk 
├─nvme0n1p1   259:2    0  10G  0 part /
├─nvme0n1p127 259:3    0   1M  0 part 
└─nvme0n1p128 259:4    0  10M  0 part /boot/efi
nvme1n1       259:1    0  10G  0 disk 
├─nvme1n1p1   259:5    0  10G  0 part 
└─nvme1n1p128 259:6    0   1M  0 part 
```

###### Note

The output varies when you run this command in your terminal.
7. Complete the following steps in the environment terminal to mount the existing
 volume:


	1. To create a temporary directory where the volume’s partition will be mounted, run
	 the following command:
	
	
	```
	MOUNT_POINT=$(mktemp -d)
	```
	2. Based on the `lsblk` command's sample output, specify the following
	 path of the device to be mounted:
	
	
	
	```
	MOUNT_DEVICE=/dev/nvme1n1p1
	```
	
	###### Note
	
	The output varies when you run this command in your terminal.
	3. To mount the existing volume, run the following command: 
	
	
	```
	sudo mount $MOUNT_DEVICE $MOUNT_POINT
	```
	4. Complete the following steps to verify if the existing volume is correctly
	 mounted:
	
	
		1. To ensure that the volume is included in the output, run the following
		 command: 
		
		
		```
		df -h
		```
		2. To verify contents of the volume, run the following command:
		
		
		```
		ls $MOUNT_POINT/home/ec2-user/environment/
		```
8. (Optional) To back up the old `.c9` directory to
 `.c9.backup`, in the environment terminal, run the following command: 



```
cp .c9 .c9.backup
```

You may need these backup files if you want to restore the configuration files
 later.
9. To copy the old environment from the existing volume, run the following command:


```
cp -R $MOUNT_POINT/home/ec2-user/environment ~
```

###### Note

If required, you can also copy files or directories outside of the environment
 directory using the preceding command. 


Ensure that the new environment works as expected.
10. To unmount the previous device, run one of the two following commands: 

 
```
sudo umount $MOUNT_DEVICE
```


```
sudo umount $MOUNT_POINT
```
11. Choose **Detach volume** from the **Actions**
 dropdown list to detach the volume that you attached in **Step
 3**.
12. You can now delete the old environment and its volume.


###### Note

Since the volume is no longer attached to the environment’s Amazon EC2 instance, you’ll
 need to remove it manually. You can do this by choosing **Delete** on the **Volume details** page.
