

# Getting started with Amazon EFS
<a name="getting-started"></a>

If you are using Amazon Elastic File System (Amazon EFS) for the first time, complete the following steps to get started with your first EFS file system. 

1. [Review the prerequisites for getting started](#gs-assumptions)

1. [Create your EFS file system and launch your EC2 instance](#gs-step-one-create-ec2-resources)

1. [Transfer files to your EFS file system using AWS DataSync](#gs-step-four-sync-files)

1. [Clean up resources and protect your AWS account](#gs-step-five-cleanup)

## Prerequisites
<a name="gs-assumptions"></a>

Before completing the getting started steps, make sure you have the following requirements:
+ You are set up with Amazon EC2 and are familiar with launching EC2 instances. You need an AWS account, a user with administrative access, a key pair, and a security group. For more information, see [Get started with Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EC2_GetStarted.html) in the *Amazon EC2 User Guide*. 
+ Your Amazon Virtual Private Cloud (Amazon VPC), EC2, and EFS resources are all in the same AWS Region and that you have a default VPC in the Region. If you don't have a default VPC, or if you want to mount your file system from a new VPC with new or existing security groups, see [Using VPC security groups](network-access.md).
+ You haven't changed the default inbound access rule for the default security group.

You can also perform a similar getting started exercise using AWS Command Line Interface (AWS CLI) commands to make the EFS API calls. For more information, see [Tutorial: Create an EFS file system and mount it on an EC2 instance using the AWS CLI](wt1-getting-started.md).

## Create your EFS file system and launch your EC2 instance
<a name="gs-step-one-create-ec2-resources"></a>

After making sure that you have the prerequisites for this getting started exercise, you can create your EFS file system and launch your EC2 instance. The quickest way to complete all of the necessary steps to get started with your first EFS file system is to use the EC2 new launch wizard during instance launch.

**Note**  
You can't use Amazon EFS with Microsoft Windows–based EC2 instances.

**To create your EFS file system and launch your EC2 instance using the EC2 launch wizard**

For instructions on creating and mounting your EFS file system when creating an EC2 instance launch, see [Use Amazon EFS with Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AmazonEFS.html) in the *Amazon EC2 User Guide*.

The following are the steps that you'll perform when creating an EFS file system during instance launch.

1. Create an EC2 instance running on a Linux operating system using the key pair and network settings you choose. 

1. Create a shared EFS file system that has the recommended settings and is automatically mounted to the EC2 instance.

1. Launch the EC2 instance so that the EFS file system is readily available for file transfers.

Alternatively, in the Amazon EFS console, you can create file systems with recommended settings or custom settings. You can also use the AWS CLI and API to create file systems. For more information about all of your options for creating a file system, see [Creating EFS file systems](creating-using-create-fs.md).

## Transfer files to your EFS file system using AWS DataSync
<a name="gs-step-four-sync-files"></a>

After creating an EFS file system, you can transfer files to it from an existing file system by using AWS DataSync. DataSync is a data transfer service that simplifies, automates, and accelerates moving and replicating data between on-premises storage systems and AWS storage services over the internet or Direct Connect. DataSync can transfer your file data, and also file system metadata such as ownership, timestamps, and access permissions.

For more information about DataSync, see [AWS DataSync](https://aws.amazon.com/datasync).

### Prerequisites
<a name="step4-prereq"></a>

Before transferring files to the EFS file system, make sure you have the following:
+ A source NFS file system that you can transfer files from. This source system needs to be accessible over NFS version 3, version 4, or 4.1. Example file systems include those located in an on-premises data center, self-managed in-cloud file systems, and EFS file systems. 
+ You are set up to use DataSync. To learn more, see [Getting started with AWS DataSync](https://docs.aws.amazon.com/datasync/latest/userguide/setting-up.html) in the *AWS DataSync User Guide*.

**To transfer files to your EFS file system using AWS DataSync**

For instructions on using DataSync to transfer files to an EFS file system, see [ Transferring your data with AWS DataSync](https://docs.aws.amazon.com/datasync/latest/userguide/transferring-data-datasync.html) in the *AWS DataSync User Guide*.

The following are the steps that you'll perform when transferring files to the EFS file system using DataSync.

1. Connect to your EC2 instance. For more information, see [Connect to your EC2 instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/connect.html) in the *Amazon EC2 User Guide*.

1. Download, deploy, and activate an agent in your environment.

1. Create and configure a source and destination location.

1. Create and configure a task.

1. Run the task to transfer files from the source to the destination.

## Clean up resources and protect your AWS account
<a name="gs-step-five-cleanup"></a>

When you're finished with this getting started exercise, perform the following steps to clean up your resources and protect your AWS account.

**To clean up resources and protect your account**

1. Connect to your EC2 instance. For more information, see [Connect to your EC2 instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/connect.html) in the *Amazon EC2 User Guide*. 

1. Unmount the EFS file system with the following command.

   ```
   $ sudo umount efs
   ```

1. Open the Amazon Elastic File System console at [https://console.aws.amazon.com/efs/](https://console.aws.amazon.com/efs/).

1. Delete the EFS file system that you created in the first step of the getting started exercise.

   1. Choose the EFS file system that you want to delete from the list of file systems.

   1. For **Actions**, choose **Delete file system**.

   1. In the **Permanently delete file system** dialog box, type the file system ID for the EFS file system that you want to delete, and then choose **Delete File System**.

1. Terminate the EC2 instance that you launched for this getting started exercise. For instructions, see [Terminate Amazon EC2 instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/terminating-instances.html) in the *AWS IAM Identity Center User Guide*.

1. If you created a security group for this getting started exercise, then delete it. For instructions, see [Delete a security group](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/deleting-security-group.html) in the *AWS IAM Identity Center User Guide*.
**Warning**  
Don't delete the default security group for your VPC.