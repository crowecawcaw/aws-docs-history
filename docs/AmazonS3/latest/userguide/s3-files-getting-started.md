

# Tutorial: Getting started with S3 Files
<a name="s3-files-getting-started"></a>

In this tutorial, you create an S3 file system and mount it on an EC2 instance. You then test basic file operations. You can use either the S3 console or the AWS CLI to get started with S3 Files.

## Getting started with S3 Files using the AWS Console
<a name="s3-files-getting-started-console"></a>

The S3 Files workflow on S3 Console consists of the following steps:
+ Create your S3 file system.
+ Mount the file system on your EC2 instance and run file system operations.

### Prerequisites
<a name="s3-files-getting-started-console-prereqs"></a>

Before getting started, make sure you have the following:
+ You have completed the [AWS account and compute setup](s3-files-prereq-policies.md#s3-files-prereq-account-setup).
+ You are set up with Amazon EC2 and are familiar with launching EC2 instances. For more information, see [Get started with Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EC2_GetStarted.html) in the *Amazon EC2 User Guide*. For this tutorial, use the default VPC for your EC2 instance.
+ You have an [IAM role for attaching your file system to AWS compute resources](s3-files-prereq-policies.md#s3-files-prereq-iam-compute-role) attached to your EC2 instance so that it can interact with your S3 file system and your S3 bucket.

### Step 1: Create your S3 file system
<a name="s3-files-getting-started-console-step1"></a>
+ Open the Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/).
+ In the navigation bar, verify you are in the AWS Region where your EC2 instance and S3 bucket is.
+ In the left navigation pane, choose **General purpose buckets**.
+ Select the bucket for which you want to create a file system.
+ Choose the **File systems** tab.
+ Choose **Create file system**.
+ Review and confirm your VPC. For this tutorial, use your default VPC.
+ Choose **Create**.

When you create a file system using the AWS Management Console, S3 Files automatically creates one mount target in every Availability Zone in your default VPC and one access point for the file system. This can take a few minutes. Your file system will become available for the next step once all the resources are created.

### Step 2: Mount the file system on your EC2 instance
<a name="s3-files-getting-started-console-step2"></a>
+ On the file system **Overview** page, choose **Attach** under **Attach to an EC2 instance**. This will open a new page to mount your file system on an EC2 instance.
+ Select your desired EC2 instance from the dropdown **Available EC2 instances**.
+ Enter a path on your EC2 instance where you want to mount the file system. For example, `/mnt/s3files/`.
+ Make sure you have configured the right [Security groups](s3-files-prereq-policies.md#s3-files-prereq-security-groups) on your EC2 instance and the mount target to allow the required traffic to flow.
+ Make sure you have the right IAM role with required permissions attached to your EC2 instance so that it can interact with your S3 file system and your S3 bucket. For more information, see [IAM role for attaching your file system to AWS compute resources](s3-files-prereq-policies.md#s3-files-prereq-iam-compute-role). For this tutorial, you can consider giving the client full access by adding the managed policy `AmazonS3FilesClientFullAccess` to EC2 instance's IAM role.
+ Follow the attach instructions displayed on the page to open CloudShell, mount your file system, and run basic file system operations.

## Getting started with S3 Files using the AWS CLI
<a name="s3-files-getting-started-cli"></a>

The S3 Files workflow on AWS CLI consists of the following steps:

1. Create your file system.

1. Create mount targets for your file system.

1. Mount the file system on your EC2 instance using a mount target.

1. Test file operations such as listing a directory, writing text to a file, reading a file, and copying a file. Then verify that your changes reflect in your S3 bucket.

### Prerequisites
<a name="s3-files-getting-started-cli-prereqs"></a>

Before getting started, make sure you have the following:
+ You have installed and configured the AWS CLI. For more information, see [Installing or updating to the latest version of the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html).
+ You have completed all the prerequisites described in [Prerequisites for S3 Files](s3-files-prereq-policies.md).
+ You are set up with Amazon EC2 and are familiar with launching EC2 instances. You need an AWS account, a user with administrative access, a key pair, and a security group. For more information, see [Get started with Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EC2_GetStarted.html) in the *Amazon EC2 User Guide*.

### Step 1: Create your S3 file system
<a name="s3-files-getting-started-cli-step1"></a>

[Connect to your EC2 instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/connect.html). Run the `create-file-system` command to create a file system.

```
aws s3files create-file-system --region {{aws-region}} --bucket {{bucket-arn}} --role-arn {{iam-role}}
```

Replace the following with your desired values:
+ {{aws-region}} : The AWS Region of your bucket. For example, `us-east-1`.
+ {{bucket-arn}} : The ARN of your S3 bucket.
+ {{iam-role}} : ARN of the IAM role that S3 Files assumes to read from and write to your S3 bucket. Make sure you have added the right permissions to this IAM role. For more information, see [IAM role for accessing your bucket from the file system](s3-files-prereq-policies.md#s3-files-prereq-iam-creation-role).

After successfully creating the file system, S3 Files returns the file system description as JSON. Note down the file system ID for the next step.

### Step 2: Create mount targets
<a name="s3-files-getting-started-cli-step2"></a>

A mount target provides network access to your file system in your VPC within a single Availability Zone. You need a mount target to access your file system from compute resources. You can create a maximum of one mount target per Availability Zone. We recommend creating a mount target in every Availability Zone you operate in.

Run the following `create-mount-target` command to create a mount target for your file system. You must make sure the {{subnet-id}} is in the same VPC as your EC2 instance. You must create your mount target in the same Availability Zone as your EC2 instance.

```
aws s3files create-mount-target --region {{aws-region}} --file-system-id {{file-system-id}} --subnet-id {{subnet-id}}
```

Here {{file-system-id}} is the file system ID that you received in the response of `create-file-system` command. Mount targets can take up to \~5 minutes to create.

### Step 3: Mount the file system on your EC2 instance
<a name="s3-files-getting-started-cli-step3"></a>

Before mounting your file system, make sure you have configured the right [Security groups](s3-files-prereq-policies.md#s3-files-prereq-security-groups) on your compute resource and the mount target to allow the required traffic to flow. For more details on security groups, visit the [VPC user guide](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-security-groups.html).

Run the following commands to mount your file system:
+ Create a directory `/mnt/s3files` that you will use as the file system mount point using the following command:

  ```
  sudo mkdir /mnt/s3files
  ```
+ Mount the file system:

  ```
  sudo mount -t s3files {{file-system-id}}:/ /mnt/s3files
  ```

If you don't have your file system ID, you can find it by running the following:

```
aws s3files get-file-system --region {{aws-region}} --file-system-id {{file-system-id}}
```

### Step 4: Test file operations
<a name="s3-files-getting-started-cli-step4"></a>

Test basic file operations on your mounted file system as follows:
+ Change to the directory you mounted:

  ```
  cd /mnt/s3files
  ```
+ You can list the contents of your directory to check that the contents of your source bucket or prefix got imported. Synchronization typically occurs within seconds, but may take longer, especially for the first file. If your bucket is empty, the command below will also return an empty result.

  ```
  ls
  ```
+ You can also test other file operations:
  + Create a file:

    ```
    echo "Hello, S3 Files!" > test.txt
    ```
  + Read the file:

    ```
    cat test.txt
    ```
  + Create a directory:

    ```
    mkdir test-directory
    ```
  + Copy the file to the directory:

    ```
    cp /mnt/s3files/test.txt /mnt/s3files/test-directory/
    ```

You can then go to your S3 bucket and check that the directory `test-directory` reflects in your bucket. Note that it may take \~1 minute to synchronize changes back to your S3 bucket.