

# Configuring S3 Files for Amazon ECS
<a name="s3files-volumes"></a>

S3 Files is a shared file system that connects any AWS compute resource directly with your data in Amazon S3. It provides fast, direct access to all of your S3 data as files with full file system semantics and low-latency performance, without your data ever leaving S3. You can read, write, and organize data using file and directory operations, while S3 Files keeps your file system and S3 bucket synchronized automatically. With Amazon ECS, you can define S3 file systems as volumes in your task definitions, giving your containers direct file system access to data stored in S3 buckets. To learn more about Amazon S3 Files and its capabilities, see the [Amazon S3 User Guide](https://docs.aws.amazon.com/AmazonS3/latest/userguide/).

## Availability
<a name="s3files-volume-availability"></a>

S3 Files support in Amazon ECS is available for the following launch types at General Availability:
+ **Fargate** — Fully supported.
+ **Amazon ECS Managed Instances** — Fully supported.

**Important**  
S3 Files are not supported on the Amazon EC2 launch type at this time. If you configure an S3 file system in a task definition and attempt to run it on the Amazon EC2 launch type, the task will fail at launch. Amazon EC2 launch type support is planned for a future release.

## Considerations
<a name="s3files-volume-considerations"></a>
+ S3 file system uses a dedicated `s3filesVolumeConfiguration` parameter in the task definition.
+ S3 file system requires a full Amazon Resource Name (ARN) to identify the file system. The ARN format is:

  ```
  arn:{{{partition}}}:s3files:{{{region}}}:{{{account-id}}}:file-system/{{fs-xxxxx}}
  ```
+ Transit encryption is mandatory for S3 file system volumes and is automatically enforced. There is no option to disable it.
+ Task IAM Role is mandatory for S3 file system volumes and is automatically enforced. There is no option to disable it.

## Prerequisites
<a name="s3files-volume-prerequisites"></a>

Before configuring S3 file system volumes in your Amazon ECS task definitions, ensure the following prerequisites are met:
+ **An S3 file system and mount target** — You must have an S3 file system created and associated with an S3 bucket. For instructions on creating an S3 file system, see the [Amazon S3 Files User Guide](https://docs.aws.amazon.com/AmazonS3/latest/userguide/).
+ **A Task IAM Role** — Your task definition must include a Task IAM Role with the following permissions:
  + Permissions to connect to and interact with S3 file systems from your application code (running in the container).
  + Permissions to read S3 objects from your application code (running in the container).
+ **VPC and security group configuration** — Your S3 file system must be accessible from the VPC and subnets where your Amazon ECS tasks run.
+ **(Optional) S3 Files access points** — If you want to enforce application-specific access controls, create an S3 Files access point and provide the ARN in the task definition.

For more information, refer to [prerequisites for S3 Files](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-files-prereq-policies.html#s3-files-prereq-iam-compute-role).

## S3 Files volume configuration parameters
<a name="s3files-volume-parameters"></a>

The following table describes the parameters available in the `s3filesVolumeConfiguration` object:

`fileSystemArn`  
Type: String  
Required: Yes  
The full ARN of the S3 file system to mount. Format: `arn:{{{partition}}}:s3files:{{{region}}}:{{{account-id}}}:file-system/{{fs-xxxxx}}`

`rootDirectory`  
Type: String  
Required: No  
The directory within the S3 file system to mount as the root of the volume. Defaults to `/` if not specified.

`transitEncryptionPort`  
Type: Integer  
Required: No  
The port to use for sending encrypted data between the Amazon ECS host and the S3 file system. Transit encryption itself is always enabled and cannot be disabled.

`accessPointArn`  
Type: String  
Required: No  
The full ARN of the S3 Files access point to use. Access points provide application-specific entry points into the file system with enforced user identity and root directory settings.