**This page is only for existing customers of the Amazon Glacier service using Vaults and the original REST API from 2012.**

If you're looking for archival storage solutions, we recommend using the Amazon Glacier storage classes in Amazon S3, S3 Glacier Instant Retrieval, S3 Glacier Flexible Retrieval, and S3 Glacier Deep Archive. To learn more about these storage options, see [Amazon Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/ "https://aws.amazon.com/s3/storage-classes/glacier/").

Amazon Glacier (original standalone vault-based service) is no longer accepting new customers. Amazon Glacier is a standalone service with its own APIs that stores data in vaults and is distinct from Amazon S3 and the Amazon S3 Glacier storage classes. Your existing data will remain secure and accessible in Amazon Glacier indefinitely. No migration is required. For low-cost, long-term archival storage, AWS recommends the [Amazon S3 Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/ "https://aws.amazon.com/s3/storage-classes/glacier/"), which deliver a superior customer experience with S3 bucket-based APIs, full AWS Region availability, lower costs, and AWS service integration. If you want enhanced capabilities, consider migrating to Amazon S3 Glacier storage classes by using our [AWS Solutions Guidance for transferring data from Amazon Glacier vaults to Amazon S3 Glacier storage classes](https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/ "https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/").

# Uploading an Archive in Amazon Glacier

Amazon Glacier (Amazon Glacier) provides a management console, which you can use to create and delete vaults. However,
you cannot upload archives to Amazon Glacier by using the management console. To upload data, such
as photos, videos, and other documents, you must either use the AWS CLI or write code to
make requests, by using either the REST API directly or by using the Amazon SDKs.

For information about using Amazon Glacier with the AWS CLI, go to [AWS CLI Reference
for Amazon Glacier](../../../cli/latest/reference/glacier/index.md "../../../cli/latest/reference/glacier/index.md"). To install the AWS CLI, go to [AWS Command Line Interface](http://aws.amazon.com/cli/ "http://aws.amazon.com/cli/"). The following **Uploading**
topics describe how to upload archives to Amazon Glacier by using the Amazon SDK for Java,
the Amazon SDK for .NET, and the REST API.

###### Topics

- [Options for Uploading an Archive to Amazon Glacier](#uploading-an-archive-overview "#uploading-an-archive-overview")
- [Uploading an Archive in a Single Operation](uploading-archive-single-operation.md "uploading-archive-single-operation.md")
- [Uploading Large Archives in Parts (Multipart Upload)](uploading-archive-mpu.md "uploading-archive-mpu.md")

## Options for Uploading an Archive to Amazon Glacier

Depending on the size of the data you are uploading, Amazon Glacier offers the following
options:

- Upload archives in a single operation –
  In a single operation, you can upload archives from 1 byte to up to 4 GB in
  size. However, we encourage Amazon Glacier customers to use multipart upload to upload
  archives greater than 100 MB. For more information, see [Uploading an Archive in a Single Operation](uploading-archive-single-operation.md "uploading-archive-single-operation.md").
- Upload archives in parts – Using the
  multipart upload API, you can upload large archives, up to about 40,000 GB
  (10,000 \* 4 GB).

The multipart upload API call is designed to improve the upload experience
for larger archives. You can upload archives in parts. These parts can be
uploaded independently, in any order, and in parallel. If a part upload fails,
you only need to upload that part again and not the entire archive. You can use
multipart upload for archives from 1 byte to about 40,000 GB in size. For more
information, see [Uploading Large Archives in Parts (Multipart Upload)](uploading-archive-mpu.md "uploading-archive-mpu.md").

###### Important

The Amazon Glacier vault inventory is only updated once a day. When you upload an archive,
you will not immediately see the new archive added to your vault (in the console or
in your downloaded vault inventory list) until the vault inventory has been
updated.

### Using the AWS Snowball Edge

Service

AWS Snowball Edge accelerates moving large amounts of data into and out of AWS using
Amazon-owned devices, bypassing the internet. For more information, see [AWS Snowball Edge](http://aws.amazon.com/snowball "http://aws.amazon.com/snowball") detail page.

To upload existing data to Amazon Glacier (Amazon Glacier), you might consider using one of the
AWS Snowball Edge device types to import data into Amazon S3, and then move it to the
Amazon Glacier storage class for archival using lifecycle rules. When you transition Amazon S3
objects to the Amazon Glacier storage class, Amazon S3 internally uses Amazon Glacier for durable
storage at lower cost. Although the objects are stored in Amazon Glacier, they remain
Amazon S3 objects that you manage in Amazon S3, and you cannot access them directly
through Amazon Glacier.

For more information about Amazon S3 lifecycle configuration and transitioning objects
to the Amazon Glacier storage class, see [Object Lifecycle Management](../../../AmazonS3/latest/userguide/object-lifecycle-mgmt.md "../../../AmazonS3/latest/userguide/object-lifecycle-mgmt.md")
and [Transitioning Objects](../../../AmazonS3/latest/userguide/lifecycle-transition-general-considerations.md "../../../AmazonS3/latest/userguide/lifecycle-transition-general-considerations.md") in the
_Amazon Simple Storage Service User Guide_.
