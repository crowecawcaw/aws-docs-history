**This page is only for existing customers of the Amazon Glacier service using Vaults and the original REST API from 2012.**

If you're looking for archival storage solutions, we recommend using the Amazon Glacier storage classes in Amazon S3, S3 Glacier Instant Retrieval, S3 Glacier Flexible Retrieval, and S3 Glacier Deep Archive. To learn more about these storage options, see [Amazon Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/ "https://aws.amazon.com/s3/storage-classes/glacier/").

Amazon Glacier (original standalone vault-based service) is no longer accepting new customers. Amazon Glacier is a standalone service with its own APIs that stores data in vaults and is distinct from Amazon S3 and the Amazon S3 Glacier storage classes. Your existing data will remain secure and accessible in Amazon Glacier indefinitely. No migration is required. For low-cost, long-term archival storage, AWS recommends the [Amazon S3 Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/ "https://aws.amazon.com/s3/storage-classes/glacier/"), which deliver a superior customer experience with S3 bucket-based APIs, full AWS Region availability, lower costs, and AWS service integration. If you want enhanced capabilities, consider migrating to Amazon S3 Glacier storage classes by using our [AWS Solutions Guidance for transferring data from Amazon Glacier vaults to Amazon S3 Glacier storage classes](https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/ "https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/").

# Uploading an Archive in a Single Operation

As described in [Uploading an Archive in Amazon Glacier](uploading-an-archive.md "uploading-an-archive.md"),
you can upload smaller archives in a single operation. However, we encourage Amazon Glacier (Amazon Glacier) customers to use Multipart Upload to upload archives greater than 100 MB.

###### Topics

- [Uploading an Archive in a Single Operation Using the AWS Command Line Interface](uploading-an-archive-single-op-using-cli.md "uploading-an-archive-single-op-using-cli.md")
- [Uploading an Archive in a Single Operation Using the AWS SDK for Java](uploading-an-archive-single-op-using-java.md "uploading-an-archive-single-op-using-java.md")
- [Uploading an Archive in a Single Operation Using the AWS SDK for .NET in Amazon Glacier](uploading-an-archive-single-op-using-dotnet.md "uploading-an-archive-single-op-using-dotnet.md")
- [Uploading an Archive in a Single Operation Using the REST API](uploading-an-archive-single-op-using-rest.md "uploading-an-archive-single-op-using-rest.md")
