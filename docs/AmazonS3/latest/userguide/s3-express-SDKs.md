# Working with directory buckets by using the S3 console, AWS CLI, and AWS SDKs

You can work with the S3 Express One Zone storage class and directory buckets by using the
AWS SDKs, Amazon S3 console, AWS Command Line Interface (AWS CLI), and Amazon S3 REST API.

## S3 Console

To get started using the S3 console, follow these steps:

- [Creating directory buckets in an Availability Zone](directory-bucket-create.md "directory-bucket-create.md")
- [Emptying a directory bucket](directory-bucket-empty.md "directory-bucket-empty.md")
- [Deleting a directory bucket](directory-bucket-delete.md "directory-bucket-delete.md")

For a full tutorial, see [Tutorial: Getting started with S3 Express One Zone](s3-express-getting-started.md "s3-express-getting-started.md").

## AWS SDKs

S3 Express One Zone supports the following AWS SDKs:

- AWS SDK for C++
- AWS SDK for Go v2
- AWS SDK for Java 2.x
- AWS SDK for JavaScript v3
- AWS SDK for .NET
- AWS SDK for PHP
- AWS SDK for Python (Boto3)
- AWS SDK for Ruby
- AWS SDK for Kotlin
- AWS SDK for Rust

When you're working with S3 Express One Zone, we recommend using the latest version of the
AWS SDKs. The supported AWS SDKs for S3 Express One Zone handle session establishment,
refreshment, and termination on your behalf. This means that you can immediately
start using API operations after you download and install the AWS SDKs and
configure the necessary IAM permissions. For more information, see [Authorizing Regional endpoint API operations with IAM](s3-express-security-iam.md "s3-express-security-iam.md").

For information about the AWS SDKs, including how to download and install them,
see [Tools to Build on
AWS](https://aws.amazon.com/developer/tools/ "https://aws.amazon.com/developer/tools/").

For AWS SDK examples, see the following:

- [Creating directory buckets in an Availability Zone](directory-bucket-create.md "directory-bucket-create.md")
- [Emptying a directory bucket](directory-bucket-empty.md "directory-bucket-empty.md")
- [Deleting a directory bucket](directory-bucket-delete.md "directory-bucket-delete.md")

## AWS Command Line Interface (AWS CLI)

You can use the AWS Command Line Interface (AWS CLI) to create directory buckets and use supported
Regional and Zonal endpoint API operations for S3 Express One Zone.

To get started with the AWS CLI, see [Get started with the
AWS CLI](../../../cli/latest/userguide/cli-chap-getting-started.md "../../../cli/latest/userguide/cli-chap-getting-started.md") in the _AWS CLI Command Reference_.

###### Note

To use directory buckets with the [high-level `aws s3` commands](../../../cli/latest/userguide/cli-services-s3-commands.md "../../../cli/latest/userguide/cli-services-s3-commands.md"), update your AWS CLI to the latest version. For more information about how to install and configure the AWS CLI,
see [Install or update the latest version of the AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md") in the _AWS CLI Command Reference_.

For AWS CLI examples, see the following:

- [Creating directory buckets in an Availability Zone](directory-bucket-create.md "directory-bucket-create.md")
- [Emptying a directory bucket](directory-bucket-empty.md "directory-bucket-empty.md")
- [Deleting a directory bucket](directory-bucket-delete.md "directory-bucket-delete.md")
