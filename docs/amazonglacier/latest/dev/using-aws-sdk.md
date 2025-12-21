**This page is only for existing customers of the Amazon Glacier service using Vaults and the original REST API from 2012.**

If you're looking for archival storage solutions, we recommend using the Amazon Glacier storage classes in Amazon S3, S3 Glacier Instant Retrieval, S3 Glacier Flexible Retrieval, and S3 Glacier Deep Archive. To learn more about these storage options, see [Amazon Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/ "https://aws.amazon.com/s3/storage-classes/glacier/").

Amazon Glacier (original standalone vault-based service) is no longer accepting new customers. Amazon Glacier is a standalone service with its own APIs that stores data in vaults and is distinct from Amazon S3 and the Amazon S3 Glacier storage classes. Your existing data will remain secure and accessible in Amazon Glacier indefinitely. No migration is required. For low-cost, long-term archival storage, AWS recommends the [Amazon S3 Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/ "https://aws.amazon.com/s3/storage-classes/glacier/"), which deliver a superior customer experience with S3 bucket-based APIs, full AWS Region availability, lower costs, and AWS service integration. If you want enhanced capabilities, consider migrating to Amazon S3 Glacier storage classes by using our [AWS Solutions Guidance for transferring data from Amazon Glacier vaults to Amazon S3 Glacier storage classes](https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/ "https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/").

# Using the AWS SDKs with Amazon Glacier

AWS provides SDKs for you to develop applications for Amazon Glacier. The SDK libraries wrap
the underlying Amazon Glacier API, simplifying your programming tasks. For example, for each
request sent to Amazon Glacier, you must include a signature to authenticate your requests. When
you use the SDK libraries, you need to provide only your AWS security credentials in your
code and the libraries compute the necessary signature and include it in the request sent to
Amazon Glacier. The AWS SDKs provide libraries that map to the underlying REST API and provide
objects that you can use to easily construct requests and process responses.

###### Topics

- [AWS SDK Libraries for Java and .NET](#java-.net-sdk-libraries "#java-.net-sdk-libraries")
- [Using Amazon Glacier with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md")
- [Using the AWS SDK for Java with Amazon Glacier](using-aws-sdk-for-java.md "using-aws-sdk-for-java.md")
- [Using the AWS SDK for .NET with Amazon Glacier](using-aws-sdk-for-dot-net.md "using-aws-sdk-for-dot-net.md")
  The AWS Command Line Interface (AWS CLI) is a unified tool to manage your AWS services, including
  Amazon Glacier. For information about downloading the AWS CLI, see [AWS Command Line Interface](https://aws.amazon.com/cli/ "https://aws.amazon.com/cli/"). For a list of the Amazon Glacier CLI commands,
  see the [AWS CLI Command
  Reference](../../../cli/latest/reference/glacier/index.md "../../../cli/latest/reference/glacier/index.md").

## AWS SDK Libraries for Java and .NET

The AWS SDKs for Java and .NET offer high-level and low-level wrapper libraries.

You can find examples of working with Amazon Glacier by using the AWS SDK for Java and the
AWS SDK for .NET throughout this developer guide.

### What Is the Low-Level API?

The low-level wrapper libraries map closely the underlying REST API ([API Reference for Amazon Glacier](amazon-glacier-api.md "amazon-glacier-api.md")) supported by
Amazon Glacier. For each Amazon Glacier REST operations, the low-level API provides a
corresponding method, a request object for you to provide request information and a
response object for you to process Amazon Glacier response. The low-level wrapper
libraries are the most complete implementation of the underlying Amazon Glacier
operations.

For information about these SDK libraries, see [Using the AWS SDK for Java with Amazon Glacier](using-aws-sdk-for-java.md "using-aws-sdk-for-java.md") and
[Using the AWS SDK for .NET with Amazon Glacier](using-aws-sdk-for-dot-net.md "using-aws-sdk-for-dot-net.md").

### What Is the High-Level API?

To further simplify application development, these libraries offer a higher-level
abstraction for some of the operations. For example:

- Uploading an archive—To upload an archive using the low-level API in
  addition to the file name and the vault name where you want to save the
  archive, You need to provide a checksum (SHA-256 tree hash) of the
  payload. However, the high-level API computes the checksum for you.
- Downloading an archive or vault inventory—To download an archive
  using the low-level API you first initiate a job, wait for the job to
  complete, and then get the job output. You need to write additional
  code to set up an Amazon Simple Notification Service (Amazon SNS) topic for
  Amazon Glacier to notify you when the job is complete. You also need some
  polling mechanism to check if a job completion message was posted to the
  topic. The high-level API provides a method to download an archive that
  takes care of all these steps. You only specify an archive ID and a folder path
  where you want to save the downloaded data.

For information about these SDK libraries, see [Using the AWS SDK for Java with Amazon Glacier](using-aws-sdk-for-java.md "using-aws-sdk-for-java.md") and
[Using the AWS SDK for .NET with Amazon Glacier](using-aws-sdk-for-dot-net.md "using-aws-sdk-for-dot-net.md").

### When to Use the High-Level and Low-Level

API

In general, if the high-level API provides methods you need to perform an operation,
you should use the high-level API because of the simplicity it provides. However, if the
high-level API does not offer the functionality, you can use the low-level API.
Additionally, the low-level API allows granular control of the operation such as retry
logic in the event of a failure. For example, when uploading an archive the high-level
API uses the file size to determine whether to upload the archive in a single operation
or use the multipart upload API. The API also has built-in retry logic in case an upload
fails. However, your application might need granular control over these decisions, in
which case you can use the low-level API.
