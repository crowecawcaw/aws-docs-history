# Use Amazon S3 with Amazon EC2 instances

Amazon Simple Storage Service (Amazon S3) is an object storage service that offers industry-leading scalability, data
availability, security, and performance. You can use Amazon S3 to store and retrieve any amount of
data for a range of use cases, such as data lakes, websites, backups, and big data analytics,
from an Amazon EC2 instance or from anywhere over the internet. For more information, see
[What is Amazon S3?](../../../AmazonS3/latest/userguide/Welcome.md "../../../AmazonS3/latest/userguide/Welcome.md")

Objects are the fundamental entities stored in Amazon S3. Every object stored in Amazon S3 is contained
in a bucket. Buckets organize the Amazon S3 namespace at the highest level and identify the account
responsible for that storage. Amazon S3 buckets are similar to internet domain names. Objects stored
in the buckets have a unique key value and are retrieved using a URL. For example, if an object
with a key value `/photos/mygarden.jpg` is stored in the `amzn-s3-demo-bucket1`
bucket, then it is addressable using the URL `https://amzn-s3-demo-bucket1.s3.amazonaws.com/photos/mygarden.jpg`.
For more information, see [How Amazon S3 works](../../../AmazonS3/latest/userguide/Welcome.md#CoreConcepts "../../../AmazonS3/latest/userguide/Welcome.md#CoreConcepts").

## Usage examples

Given the benefits of Amazon S3 for storage, you might decide to use this service to store
files and data sets for use with EC2 instances. There are several ways to move data to
and from Amazon S3 to your instances. In addition to the examples discussed below, there are
a variety of tools that people have written that you can use to access your data in Amazon S3
from your computer or your instance.

If you have permission, you can copy a file to or from Amazon S3 and your instance using
one of the following methods.

wget

###### Note

This method works for public objects only. If the object is not public, you receive
an `ERROR 403: Forbidden` message. If you receive this error, you must use
either the Amazon S3 console, AWS CLI, AWS API, AWS SDK, or AWS Tools for Windows PowerShell, and you must have
the required permissions. For more information, see [Identity and access management
for Amazon S3](../../../AmazonS3/latest/userguide/security-iam.md "../../../AmazonS3/latest/userguide/security-iam.md") and [Downloading an object](../../../AmazonS3/latest/userguide/download-objects.md "../../../AmazonS3/latest/userguide/download-objects.md") in the _Amazon S3 User Guide_.

The **wget** utility is an HTTP and FTP client that allows you to
download public objects from Amazon S3. It is installed by default in Amazon Linux and
most other distributions, and available for download on Windows. To download an Amazon S3
object, use the following command, substituting the URL of the object to
download.

```
`[ec2-user ~]$` wget https://`amzn-s3-demo-bucket`.s3.amazonaws.com/`path-to-file`
```

PowerShell
You can use the [AWS Tools for Windows PowerShell](https://aws.amazon.com/powershell/ "https://aws.amazon.com/powershell/") to move
objects to and from Amazon S3.

Use the [Copy-S3Object](../../../powershell/latest/reference/items/Copy-S3Object.md "../../../powershell/latest/reference/items/Copy-S3Object.md")
cmdlet to copy an Amazon S3 object to your Windows instance as follows.

```
Copy-S3Object `
    -BucketName `amzn-s3-demo-bucket` `
    -Key `path-to-file` `
    -LocalFile `my_copied_file.ext`
```

Alternatively, you can open the Amazon S3 console by using a web browser on the
Windows instance.

AWS CLI
You can use the AWS Command Line Interface (AWS CLI) to download restricted items from Amazon S3 and
also to upload items. For more information, such as how to install and configure the
tools, see the [AWS Command Line Interface detail
page](https://aws.amazon.com/cli/ "https://aws.amazon.com/cli/").

The [aws s3 cp](../../../cli/latest/reference/s3/cp.md "../../../cli/latest/reference/s3/cp.md") command is similar to the Unix
**cp** command. You can copy files from Amazon S3 to your instance, copy
files from your instance to Amazon S3, and copy files from one Amazon S3 location to
another.

Use the following command to copy an object from Amazon S3 to your instance.

```
aws s3 cp s3://`amzn-s3-demo-bucket`/`my_folder`/`my_file.ext` `my_copied_file.ext`
```

Use the following command to copy an object from your instance back into Amazon S3.

```
aws s3 cp `my_copied_file.ext` s3://`amzn-s3-demo-bucket`/`my_folder`/`my_file.ext`
```

The [aws s3 sync](../../../cli/latest/reference/s3/sync.md "../../../cli/latest/reference/s3/sync.md") command can synchronize an entire Amazon S3 bucket to a
local directory location. This can be helpful for downloading a data set and keeping the
local copy up-to-date with the remote set. If you have the proper permissions on the
Amazon S3 bucket, you can push your local directory back up to the cloud when you are
finished by reversing the source and destination locations in the command.

Use the following command to download an entire Amazon S3 bucket to a local directory on
your instance.

```
aws s3 sync s3://`amzn-s3-demo-source-bucket` `local_directory`
```

Amazon S3 API
If you are a developer, you can use an API to access data in Amazon S3. You can use this
API to help develop your application and integrate it with other APIs and SDKs.
For more information, see [Code examples for Amazon S3 using AWS SDKs](../../../AmazonS3/latest/API/service_code_examples.md "../../../AmazonS3/latest/API/service_code_examples.md") in the
_Amazon Simple Storage Service API Reference_.
