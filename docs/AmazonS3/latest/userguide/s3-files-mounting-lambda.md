

# Mounting S3 file systems on AWS Lambda functions
<a name="s3-files-mounting-lambda"></a>

While AWS Lambda functions provide an ephemeral local storage available during execution, many serverless workloads, such as machine learning inference, data processing, and content management, require access to large reference datasets, shared files, or persistent storage. By attaching an S3 file system to your Lambda function, you can easily share data across function invocations, read large reference data files, and write function output to a persistent and shared store, all through a local mount path.

![The data flow between an S3 bucket, S3 file system, and AWS Lambda function.](http://docs.aws.amazon.com/AmazonS3/latest/userguide/images/S3Files_Lambda_dataflow.png)


## Prerequisites
<a name="s3-files-mounting-lambda-prereqs"></a>

Before you mount an S3 file system on a Lambda function, make sure that you have the following:
+ **File system, mount targets, and access point** — The S3 file system, at least one mount target, and one access point must be available. If you create a file system using the AWS Management Console, S3 Files automatically creates one mount target in every Availability Zone in your default VPC and one access point (UID/GID 1000/1000 and `/Lambda` as the access point scope) for the file system.
+ **Lambda function** — A Lambda function with an execution role that has access to mount the file system. See [Execution role and user permissions](https://docs.aws.amazon.com/lambda/latest/dg/configuration-filesystem-s3files.html#configuration-filesystem-s3files-permissions) in the *AWS Lambda User Guide*.
+ **VPC** — The Lambda function must be in the same VPC as your mount target. The subnets you assign to your Lambda function must be in the Availability Zone that has a mount target.
+ You have configured the required [Security groups](s3-files-prereq-policies.md#s3-files-prereq-security-groups).

## How to mount your S3 file system on a Lambda function
<a name="s3-files-mounting-lambda-steps"></a>
+ On the S3 Console, choose **File systems** in the left navigation pane.
+ Select the file system you want to mount on your Lambda function.
+ In the **Overview** tab, choose **Attach** under **Attach to a Lambda function**.
+ Select an available Lambda function from the drop down. The available list only shows functions within the same VPC and subnets where you have a mount target.
+ Specify the local mount path.
+ If you have more than one access points, select an access point.
+ Choose **Attach**. Your file system will now be attached the next time you invoke your Lambda function.

For more details, see [Configuring Amazon S3 Files access with AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/configuration-filesystem-s3files.html).

You can monitor your file system storage, performance, client connections, and synchronization errors using [Amazon CloudWatch](s3-files-monitoring-cloudwatch.md).