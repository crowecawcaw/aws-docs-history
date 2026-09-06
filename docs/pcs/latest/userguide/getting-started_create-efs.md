

# Create shared storage for AWS PCS in Amazon Elastic File System
<a name="getting-started_create-efs"></a>

Amazon Elastic File System (Amazon EFS) is an AWS service that provides serverless, fully elastic file storage so that you can share file data without provisioning or managing storage capacity and performance. For more information, see [What is Amazon Elastic File System?](https://docs.aws.amazon.com/efs/latest/ug/whatisefs.html) in the *Amazon Elastic File System User Guide*. 

 The AWS PCS demonstration cluster uses an EFS file system to provide a shared home directory between the cluster nodes. Create an EFS file system in the same VPC as your cluster. 

**To create your Amazon EFS file system**

1. Go to the [Amazon EFS console](https://console.aws.amazon.com/efs).

1. Make sure it's set to the same AWS Region where you will try AWS PCS.

1. Choose **Create file system**.

1. On the **Create file system** page, set the following parameters:
   + For **Name**, enter `getstarted-efs`
   + Under **Virtual Private Cloud (VPC)**, choose the VPC named `hpc-networking:Large-Scale-HPC`
   + Choose **Create**. This returns you to the **File systems** page.

1. Make a note of the **File system ID** for the `getstarted-efs` file system. You use this information later.