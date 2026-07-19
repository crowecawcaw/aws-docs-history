# Creating file systems

You can create file systems by using the AWS Console, the AWS Command Line Interface
(AWS CLI), or the Amazon S3 API for any existing or new S3 general purpose bucket. For
information on creating a new bucket, see [Creating a general purpose bucket](create-bucket-overview.md "create-bucket-overview.md").

## Required IAM permissions for creating file systems

When you create an S3 file system, you must specify an IAM role that S3 Files assumes
to read from and write to your S3 bucket. This role allows S3 Files to synchronize
changes between your file system and your S3 bucket. When you create a file system using
the AWS Console, S3 Files automatically creates this IAM role with the required
permissions. If you are using the AWS CLI or S3 API, see [IAM role for accessing your bucket from the file system](s3-files-prereq-policies.md#s3-files-prereq-iam-creation-role "s3-files-prereq-policies.md#s3-files-prereq-iam-creation-role").

For more information about managing permissions for API operations, see [How S3 Files works with IAM](s3-files-security-iam.md "s3-files-security-iam.md").

## Status of a file system

A file system can have one of the status values described in the following table that
you can get using the `get-file-system` command.

| File system state | Description                                                                                                                                                                                                                   |
| ----------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| AVAILABLE         | The file system is in a healthy state, and is reachable and available<br>for use.                                                                                                                                             |
| CREATING          | S3 Files is in the process of creating the new file<br>system.                                                                                                                                                                |
| DELETING          | S3 Files is deleting the file system in response to a user-initiated<br>delete request.                                                                                                                                       |
| DELETED           | S3 Files has deleted the file system in response to a user-initiated<br>delete request.                                                                                                                                       |
| ERROR             | The file system is in a failed state and is unrecoverable. To access<br>the file system data, restore a backup of this file system to a new file<br>system. Check the StatusMessage field for information about the<br>error. |

###### Note

S3 Files returns an error when you attempt to create a file system scoped to a
prefix with a large number of objects. This error alerts you that large recursive
rename or move operations may impact file system performance and increase S3 request
costs, as every file requires separate copy and delete requests to your S3 bucket. If
you still want to create a file system scoped to that prefix, you can add the
`--AcceptBucketWarning` parameter.

This section explains how to use the Amazon S3 console to create a file system for
S3 Files.

- Open the Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
- In the navigation bar, verify you are in your
  desired AWS Region.
- In the left navigation pane, choose **File
  systems**.
- Select **Create file
  system**.
- On the create page, choose the S3 bucket or prefix to create your
  file system from. You can enter the S3 URI directly (for example,
  `s3://bucket-name/prefix`) or choose **Browse S3** to navigate to and select your bucket or
  prefix.
- Select a VPC for your file system. S3 Files selects your default VPC
  automatically. This is the VPC where your compute resources connect to your
  file system. To use a different VPC, choose one from the
  dropdown.
- Select **Create** and wait for the
  status of your file system to become
  `Available`.
  **Default settings on AWS Management
  Console**

S3 Files will create your file system with the following configuration:

- **Encryption** — S3 Files sets the
  encryption configuration from the source S3 bucket and applies it to data at
  rest in your file system.
- **IAM role** — S3 Files creates a new
  IAM role that it assumes to manage the data synchronization between your file
  system and bucket.
- **Mount targets** — S3 Files
  automatically creates one mount target in every Availability Zone in the VPC
  you choose.
- **Access point** — S3 Files creates one
  access point for the file system.
  When you're using the AWS CLI, you create these resources in order. First, you
  create a file system. Then, you can create mount targets and any additional optional
  tags for the file system by using corresponding AWS CLI commands.

The following `create-file-system` example command shows how you can use
the AWS CLI to create a file system for S3 Files.

```
aws s3files create-file-system --region `aws-region` --bucket `s3-bucket-arn` --client-token `idempotency-token` --role-arn `iam-role`
```

Replace the following with your desired values:

- `aws-region` : The AWS Region of your
  bucket. For example, `us-east-1`.
- `bucket-arn` : The ARN of your S3
  bucket.
- `idempotency-token` : An idempotency token.
  This is optional.
- `iam-role` : ARN of the IAM role that S3
  Files assumes to read from and write to your S3 bucket. Make sure you have
  added the right permissions to this IAM role. For more information, see [IAM role for accessing your bucket from the file system](s3-files-prereq-policies.md#s3-files-prereq-iam-creation-role "s3-files-prereq-policies.md#s3-files-prereq-iam-creation-role").
  After successfully creating the file system, S3 Files returns the file system
  description as JSON.
