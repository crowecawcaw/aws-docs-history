

# Prerequisites for S3 Files
<a name="s3-files-prereq-policies"></a>

Before you begin using S3 Files, make sure that you have completed the following prerequisites.

## AWS account and compute setup
<a name="s3-files-prereq-account-setup"></a>
+ You have an AWS account.
+ You have a compute resource and an S3 general purpose bucket in your desired AWS Region where you want to create your file system. For more information, see [Creating a general purpose bucket](create-bucket-overview.md).
+ Your S3 bucket has versioning enabled. S3 Files requires S3 Versioning to synchronize changes between your file system and your S3 bucket. For more information, see [Enabling versioning on buckets](manage-versioning-examples.md).
+ Your S3 bucket must use one of the following encryption types: Server-side encryption with Amazon S3 managed keys (SSE-S3) or Server-side encryption with AWS Key Management Service (AWS KMS) keys (SSE-KMS).

## S3 Files client
<a name="s3-files-prereq-client"></a>

To use S3 Files with Amazon EC2, you must install the client `amazon-efs-utils`, a shared open-source collection of tools for Amazon EFS and Amazon S3 Files. To work with S3 Files, you need `amazon-efs-utils` version 3.0.0 or above. The client includes a mount helper program that simplifies mounting S3 file systems and enables Amazon CloudWatch metrics for monitoring your file system's mount status.

### Step 1: Install the client
<a name="s3-files-prereq-client-install"></a>
+ Access the terminal for your Amazon EC2 instance through Secure Shell (SSH), and log in with the appropriate user name. For more information, see [Connect to your EC2 instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/connect-to-linux-instance.html) in the *Amazon Elastic Compute Cloud User Guide*.
+ For those using Amazon Linux, do the following to install efs-utils from Amazon's repositories:

  ```
  sudo yum -y install amazon-efs-utils
  ```
+ If you use other supported Linux distributions, you can do the following:

  ```
  curl https://amazon-efs-utils.aws.com/efs-utils-installer.sh | sudo sh -s -- --install
  ```
+ For other Linux distributions, see [On other Linux distributions](https://github.com/aws/efs-utils/?tab=readme-ov-file#on-other-linux-distributions) in the amazon-efs-utils README on GitHub.

### Step 2: Install botocore
<a name="s3-files-prereq-client-botocore"></a>

The `amazon-efs-utils` client uses botocore to interact with other AWS services. For example, you need to install botocore to use Amazon CloudWatch to monitor your file system. For instructions on installing and upgrading botocore, see [Installing botocore](https://github.com/aws/efs-utils#install-botocore) in the amazon-efs-utils README on GitHub.

### Enabling FIPS mode for S3 Files
<a name="s3-files-prereq-client-fips"></a>

If you need to comply with Federal Information Processing Standards (FIPS), then you must enable FIPS mode in the client. Enabling the FIPS mode involves modifying the `s3files-utils.conf` file on the operating system.

Follow these steps to enable FIPS mode in the client for S3 Files:

1. Using your text editor of choice, open the `/etc/amazon/efs/s3files-utils.conf` file.

1. Find the line containing the following text:

   ```
   fips_mode_enabled = false
   ```

1. Change the text to the following:

   ```
   fips_mode_enabled = true
   ```

1. Save your changes.

## IAM roles and policies
<a name="s3-files-prereq-iam"></a>

To use S3 Files, you must configure IAM roles and attached policies for two purposes:
+ Accessing your bucket from the file system
+ Attaching your file system to AWS compute resources

### IAM role for accessing your bucket from the file system
<a name="s3-files-prereq-iam-creation-role"></a>

When you create an S3 Files file system, you specify an IAM role that S3 Files assumes to read from and write to your S3 bucket. This role grants S3 Files permission to synchronize changes between your file system and your bucket, including Amazon EventBridge rules that trigger synchronization. You must also make sure that your S3 bucket policy does not deny access to your compute resources.

S3 Files requires S3 Versioning on your bucket. It uses version-specific API operations such as `s3:GetObjectVersion` and `s3:GetObjectVersionTagging` in addition to `s3:GetObject`. The following policy uses wildcards (for example, `s3:GetObject*` rather than `s3:GetObject`) to cover both versioned and non-versioned actions.

**Note**  
When you create a file system using the AWS Management Console, S3 Files automatically creates this IAM role with the required permissions.

This IAM role requires the following:
+ An inline policy as follows:

  ```
  {
      "Version": "2012-10-17",		 	 	 
      "Statement": [
          {
              "Sid": "S3BucketPermissions",
              "Effect": "Allow",
              "Action": [
                  "s3:ListBucket",
                  "s3:ListBucketVersions"
              ],
              "Resource": "arn:aws:s3:::{{bucket}}",
              "Condition": {
                  "StringEquals": {
                      "aws:ResourceAccount": "{{accountId}}"
                  }
              }
          },
          {
              "Sid": "S3ObjectPermissions",
              "Effect": "Allow",
              "Action": [
                  "s3:AbortMultipartUpload",
                  "s3:DeleteObject*",
                  "s3:GetObject*",
                  "s3:List*",
                  "s3:PutObject*"
              ],
              "Resource": "arn:aws:s3:::{{bucket}}/*",
              "Condition": {
                  "StringEquals": {
                      "aws:ResourceAccount": "{{accountId}}"
                  }
              }
          },
          {
              "Sid": "UseKmsKeyWithS3Files",
              "Effect": "Allow",
              "Action": [
                  "kms:GenerateDataKey",
                  "kms:Encrypt",
                  "kms:Decrypt",
                  "kms:ReEncryptFrom",
                  "kms:ReEncryptTo"
              ],
              "Condition": {
                  "StringLike": {
                      "kms:ViaService": "s3.{{region}}.amazonaws.com",
                      "kms:EncryptionContext:aws:s3:arn": [
                          "arn:aws:s3:::{{bucket}}",
                          "arn:aws:s3:::{{bucket}}/*"
                      ]
                  }
              },
              "Resource": "arn:aws:kms:{{region}}:{{accountId}}:*"
          },
          {
              "Sid": "EventBridgeManage",
              "Effect": "Allow",
              "Action": [
                  "events:DeleteRule",
                  "events:DisableRule",
                  "events:EnableRule",
                  "events:PutRule",
                  "events:PutTargets",
                  "events:RemoveTargets"
              ],
              "Condition": {
                  "StringEquals": {
                      "events:ManagedBy": "elasticfilesystem.amazonaws.com"
                  }
              },
              "Resource": [
                  "arn:aws:events:*:*:rule/DO-NOT-DELETE-S3-Files*"
              ]
          },
          {
              "Sid": "EventBridgeRead",
              "Effect": "Allow",
              "Action": [
                  "events:DescribeRule",
                  "events:ListRuleNamesByTarget",
                  "events:ListRules",
                  "events:ListTargetsByRule"
              ],
              "Resource": [
                  "arn:aws:events:*:*:rule/*"
              ]
          }
      ]
  }
  ```

  Replace the placeholder values with your own values.    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-files-prereq-policies.html)
+ A trust policy that allows S3 Files to assume the IAM role. Add the following trust policy to the IAM role to allow the S3 Files service to assume it. Replace {{accountId}} and {{region}} with your values.

  ```
  {
      "Version": "2012-10-17",		 	 	 
      "Statement": [
          {
              "Sid": "AllowS3FilesAssumeRole",
              "Effect": "Allow",
              "Principal": {
                  "Service": "elasticfilesystem.amazonaws.com"
              },
              "Action": "sts:AssumeRole",
              "Condition": {
                  "StringEquals": {
                      "aws:SourceAccount": "{{accountId}}"
                  },
                  "ArnLike": {
                      "aws:SourceArn": "arn:aws:s3files:{{region}}:{{accountId}}:file-system/*"
                  }
              }
          }
      ]
  }
  ```

### IAM role for attaching your file system to AWS compute resources
<a name="s3-files-prereq-iam-compute-role"></a>

Your compute resources on which you mount an S3 file system must have an IAM role attached (for example, an EC2 instance profile) with policies that allow your compute resource to interact with your S3 file system and your source S3 bucket. You must also make sure that the bucket policies of your source bucket don't deny access from your compute resource.

Add the following two policies to the IAM role attached to your compute resource:
+ **Permissions for the compute resource to connect to and interact with S3 file systems**

  The IAM role must include permissions for the mount helper to connect to and interact with S3 file systems. You can attach an AWS managed policy such as `AmazonS3FilesClientFullAccess` managed policy if you want to grant the compute resource full read and write access to your S3 file system or the `AmazonS3FilesClientReadOnlyAccess` for read-only access. You can also attach the `AmazonElasticFileSystemsUtils` managed policy if you want to enable Amazon CloudWatch monitoring. For more information and a complete list of available managed policies for S3 Files, see [AWS managed policies for Amazon S3 Files](s3-files-security-iam-awsmanpol.md). You can also provide these permissions by adding individual IAM permissions such as `s3files:ClientMount` or `s3files:ClientWrite` (not required for read-only connections) to the IAM role of your compute resource.
+ **An inline policy that grants the compute resource read access to S3 objects**

  Add the following inline policy to the IAM role. This policy grants the compute resource permissions to directly read objects from the linked S3 bucket in the same account to optimize read performance. Replace {{bucket}} with your S3 bucket name or bucket name with prefix.

  ```
  {
      "Version": "2012-10-17",		 	 	 
      "Statement": [
          {
              "Sid": "S3ObjectReadAccess",
              "Effect": "Allow",
              "Action": [
                  "s3:GetObject",
                  "s3:GetObjectVersion"
              ],
              "Resource": "arn:aws:s3:::{{bucket}}/*"
          },
          {
              "Sid": "S3BucketListAccess",
              "Effect": "Allow",
              "Action": "s3:ListBucket",
              "Resource": "arn:aws:s3:::{{bucket}}"
          }
      ]
  }
  ```

## Security groups
<a name="s3-files-prereq-security-groups"></a>

Once your file system and mount targets are created, you must configure the right security groups to start using your file system. Security groups on both the compute resource and the mount target must allow the required traffic as shown in the table below:


| Security group | Rule type | Protocol | Port | Source/destination | 
| --- | --- | --- | --- | --- | 
| EC2 Instance | Outbound | TCP | 2049 | Mount target security group | 
| Mount Target | Inbound | TCP | 2049 | EC2 instance security group | 