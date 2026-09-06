

# Use Amazon S3 with Amazon EC2 instances
<a name="AmazonS3"></a>

Amazon Simple Storage Service (Amazon S3) is an object storage service that offers industry-leading scalability, data availability, security, and performance. You can use Amazon S3 to store and retrieve any amount of data for a range of use cases, such as data lakes, websites, backups, and big data analytics, from an Amazon EC2 instance or from anywhere over the internet. For more information, see [What is Amazon S3?](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html)

There are two ways to access Amazon S3 data from your Amazon EC2 instances:
+ **File access** – Use [Amazon S3 Files](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-files.html) to mount an S3 bucket as a high performance file system on your instance.
+ **Object access** – Use the [Amazon S3 API](https://docs.aws.amazon.com/AmazonS3/latest/API/), AWS CLI, AWS SDKs, or tools like wget to copy objects to and from S3.

## File access with Amazon S3 Files
<a name="S3FilesAccess"></a>

Amazon S3 Files is a serverless file system that lets you mount your S3 general purpose bucket as a high performance file system on your compute instance. With S3 Files, you can access your S3 objects as files by using standard file system operations such as read and write on the local mount path.

You can mount an S3 file system to an EC2 instance either at launch, or after launch on a running instance.

**Prerequisites**

Before you set up S3 Files with your EC2 instance, make sure you have the following:
+ An S3 file system and at least one mount target in the available state. For information about creating an S3 file system, see [Working with Amazon S3 Files](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-files.html) in the *Amazon S3 User Guide*.
+ An EC2 Linux instance with an instance profile attached to it. For information about the required permissions to mount the file system, see [IAM roles and policies ](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-files-prereq-policies.html#s3-files-prereq-iam) in the *Amazon S3 User Guide*.
+ Security groups that allow NFS traffic (port 2049) between your instance and the file system’s mount targets. For information about the required security group settings, see [Security groups](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-files-prereq-policies.html#s3-files-prereq-security-groups) in the *Amazon S3 User Guide*.

**To mount a file system to an EC2 instance at launch using the EC2 console**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. Choose **Launch instance**. 

1. Under **Network settings**, do the following:

   1. Choose **Edit**.

   1. For **Subnet**, select a subnet.

   1. Select the default security group to make sure that your EC2 instance can access your S3 file system. You can't access your EC2 instance by Secure Shell (SSH) using this security group. For access by SSH, you can later edit the default security group and add a rule to allow SSH, or add a new security group that allows SSH. You can use the following settings:

      1. **Type:** SSH 

      1. **Protocol:** TCP 

      1. **Port Range:** 22 

      1. **Source:** Anywhere 0.0.0.0/0

1. Under **Configure storage**, do the following:

   1. Under **File systems**, choose **S3 Files**.

   1. Choose **Add shared file system**.

   1. For **S3 file system**, your file systems appear in the Availability Zone based on the subnet that you selected in your Network settings. Choose the S3 file system that you want to mount. If you don’t have any file systems, choose **Create a new file system** to create a new one. 

   1. Enter a local mount path on your EC2 instance where you want to mount the file system (for example, `/mnt/s3files`). 

   1. A command will be generated to mount the file system and add it to fstab. You can add this command to the **User data** field under **Advanced details**. Your EC2 instance will then be configured to mount the S3 file system at launch and whenever it's rebooted. You can also run these commands in your EC2 instance after it is launched. 

1. Under **Advanced details**, attach an instance profile to your instance. Your IAM role must have permissions to mount the file system and access the S3 bucket. For more information about the required permissions, see [IAM roles and policies](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-files-prereq-policies.html#s3-files-prereq-iam) in the *Amazon S3 User Guide*. 

1. Choose **Launch instance**.

   After the instance launches, the required software utilities are installed and the file system is mounted. You can view the file system by navigating to your local mount path.

**To mount a file system to an EC2 instance after launch**

1. [Connect to your EC2 instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/connect.html) through Secure Shell (SSH) or by using EC2 Instance Connect in the EC2 console.

1. To mount your S3 file system, use the mount helper utility `amazon-efs-utils`. Depending on your Linux distribution, use one of the following commands to install the `amazon-efs-utils` package:

   1. If you’re using Amazon Linux, run the following command to install efs-utils from Amazon's repositories:

      ```
      sudo yum -y install amazon-efs-utils
      ```

   1. If you are using other [supported Linux distributions](https://github.com/aws/efs-utils/?tab=readme-ov-file#efs-utils), run the following command:

      ```
      curl https://amazon-efs-utils.aws.com/efs-utils-installer.sh | sudo sh -s -- --install
      ```

   1. For other Linux distributions, see the [efs-utils](https://github.com/aws/efs-utils/?tab=readme-ov-file#on-other-linux-distributions) repository on *GitHub*.

1. Create a directory for the file system mount point using the following command:

   ```
   sudo mkdir {path/to/mount}
   ```

1. Mount the S3 file system:

   ```
   FS="{YOUR_FILE_SYSTEM_ID}"
   sudo mount -t s3files $FS:/ {path/to/mount}
   ```

1. Confirm the file system is mounted:

   ```
   df -h {path/to/mount}
   ```

**To view objects in your S3 bucket as files**  
Having completed the preceding procedures, you can now read and write S3 objects as files on your local mount path using standard file system operations. If you have objects in your S3 bucket, you can view them as files by using the following command:

```
ls {path/to/mount}
```

## Object-based access
<a name="objectaccess"></a>

You can copy files to and from Amazon S3 using the S3 API, AWS CLI, AWS SDKs, or standard HTTP tools. If you have the required permissions, you can copy a file to or from Amazon S3 and your instance using one of the following methods. 

------
#### [ wget ]

**Note**  
This method works for public objects only. If the object is not public, you receive an `ERROR 403: Forbidden` message. If you receive this error, you must use either the Amazon S3 console, AWS CLI, AWS API, AWS SDK, or AWS Tools for Windows PowerShell, and you must have the required permissions. For more information, see [Identity and access management for Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/security-iam.html) and [ Downloading an object](https://docs.aws.amazon.com/AmazonS3/latest/userguide/download-objects.html) in the *Amazon S3 User Guide*.

The **wget** utility is an HTTP and FTP client that you can use to download public objects from Amazon S3. It is installed by default in Amazon Linux and most other distributions, and available for download on Windows. To download an Amazon S3 object, use the following command, substituting the URL of the object to download.

```
[ec2-user ~]$ wget https://{{amzn-s3-demo-bucket}}.s3.amazonaws.com/{{path-to-file}}
```

------
#### [ PowerShell ]

You can use the [AWS Tools for Windows PowerShell](https://aws.amazon.com/powershell/) to move objects to and from Amazon S3.

Use the [Copy-S3Object](https://docs.aws.amazon.com/powershell/latest/reference/items/Copy-S3Object.html) cmdlet to copy an Amazon S3 object to your Windows instance as follows.

```
Copy-S3Object `
    -BucketName {{amzn-s3-demo-bucket}} `
    -Key {{path-to-file}} `
    -LocalFile {{my_copied_file.ext}}
```

Alternatively, you can open the Amazon S3 console by using a web browser on the Windows instance.

------
#### [ AWS CLI ]

You can use the AWS Command Line Interface (AWS CLI) to download restricted items from Amazon S3 and to upload items. For more information, such as how to install and configure the tools, see the [AWS Command Line Interface detail page](https://aws.amazon.com/cli/).

The [aws s3 cp](https://docs.aws.amazon.com/cli/latest/reference/s3/cp.html) command is similar to the Unix **cp** command. You can copy files from Amazon S3 to your instance, copy files from your instance to Amazon S3, and copy files from one Amazon S3 location to another.

Use the following command to copy an object from Amazon S3 to your instance:

```
aws s3 cp s3://{{amzn-s3-demo-bucket}}/{{my_folder}}/{{my_file.ext}} {{my_copied_file.ext}}
```

Use the following command to copy an object from your instance back into Amazon S3:

```
aws s3 cp {{my_copied_file.ext}} s3://{{amzn-s3-demo-bucket}}/{{my_folder}}/{{my_file.ext}}
```

The [aws s3 sync](https://docs.aws.amazon.com/cli/latest/reference/s3/sync.html) command can synchronize an entire Amazon S3 bucket to a local directory location. This can be helpful for downloading a data set and keeping the local copy up-to-date with the remote set. If you have the proper permissions on the Amazon S3 bucket, you can push your local directory back up to the cloud when you are finished by reversing the source and destination locations in the command.

Use the following command to download an entire Amazon S3 bucket to a local directory on your instance:

```
aws s3 sync s3://{{amzn-s3-demo-source-bucket}} {{local_directory}}
```

------
#### [ Amazon S3 API ]

You can use an API to access data in Amazon S3. You can use this API to help develop your application and integrate it with other APIs and SDKs. For more information, see [Code examples for Amazon S3 using AWS SDKs](https://docs.aws.amazon.com/AmazonS3/latest/API/service_code_examples.html) in the *Amazon Simple Storage Service API Reference*.

------