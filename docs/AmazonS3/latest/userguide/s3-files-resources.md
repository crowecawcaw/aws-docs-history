

# Creating and managing S3 Files resources
<a name="s3-files-resources"></a>

This page describes how to create, configure, and manage S3 Files resources. To manage your resources using the AWS CLI, see [S3 Files API reference](https://docs.aws.amazon.com/AmazonS3/latest/API/API_Operations_Amazon_S3_Files.html).

**File systems**  
A shared file system linked to your S3 bucket. It stores a fraction of your actively used S3 data as files and directories so that your applications and users can benefit from low-latency performance. You can access your data using standard file system operations, including reading, writing, and locking files.  
+ [Creating file systems](s3-files-file-systems-creating.md)
+ [Deleting file systems](s3-files-file-systems-deleting.md)

**Mount targets**  
A mount target provides network access to your file system within a single Availability Zone in your VPC. You need at least one mount target to access your file system from compute resources, and you can create a maximum of one mount target per Availability Zone. We recommend creating one mount target in each Availability Zone you operate in so that your compute resources always have a local network path to the file system, improving both availability and latency. When you create a file system using the AWS Management Console, S3 Files automatically creates one mount target in every Availability Zone in your default VPC.  
+ [Creating mount targets](s3-files-mount-targets-creating.md)
+ [Managing mount targets](s3-files-mount-targets-managing.md)
+ [Deleting mount targets](s3-files-mount-targets-deleting.md)

**File system policies**  
A file system policy is an optional IAM resource policy that you can create for your S3 file system to control NFS client access to the file system.  
+ [Creating file system policies](s3-files-file-system-policies-creating.md)
+ [Deleting file system policies](s3-files-file-system-policies-deleting.md)

**Access points**  
Access points are application-specific entry points to a file system that simplify managing data access at scale for shared datasets. You can use access points to enforce user identities and permissions for all file system requests that are made through the access point. Additionally, access points can restrict clients to only access data within a specified root directory and its subdirectories. When you create a file system using the AWS Management Console, S3 Files automatically creates one access point for the file system.  
A file system can have a maximum of 25,000 access points. For more information, see [Unsupported features, limits, and quotas](s3-files-quotas.md).  
+ [Creating access points for an S3 file system](s3-files-access-points-creating.md)
+ [Deleting access points for an S3 file system](s3-files-access-points-deleting.md)

**Tags**  
Tags are key-value pairs that you define and associate with your S3 Files resources to help organize, identify, and manage them.  
+ [Tagging S3 Files resources](s3-files-tagging.md)

## CloudFormation template
<a name="s3-files-resources-cloudformation"></a>

You can also use CloudFormation templates to create and manage S3 Files resources. See [Amazon Simple Storage Service Files (Amazon S3 Files)](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/AWS_S3Files.html) in the *AWS CloudFormation User Guide* for all available S3 Files resource types.

**Topics**
+ [CloudFormation template](#s3-files-resources-cloudformation)
+ [Creating file systems](s3-files-file-systems-creating.md)
+ [Deleting file systems](s3-files-file-systems-deleting.md)
+ [Creating mount targets](s3-files-mount-targets-creating.md)
+ [Managing mount targets](s3-files-mount-targets-managing.md)
+ [Deleting mount targets](s3-files-mount-targets-deleting.md)
+ [Creating file system policies](s3-files-file-system-policies-creating.md)
+ [Deleting file system policies](s3-files-file-system-policies-deleting.md)
+ [Creating access points for an S3 file system](s3-files-access-points-creating.md)
+ [Deleting access points for an S3 file system](s3-files-access-points-deleting.md)
+ [Tagging S3 Files resources](s3-files-tagging.md)