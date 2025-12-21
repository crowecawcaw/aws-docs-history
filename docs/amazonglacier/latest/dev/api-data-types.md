**This page is only for existing customers of the Amazon Glacier service using Vaults and the original REST API from 2012.**

If you're looking for archival storage solutions, we recommend using the Amazon Glacier storage classes in Amazon S3, S3 Glacier Instant Retrieval, S3 Glacier Flexible Retrieval, and S3 Glacier Deep Archive. To learn more about these storage options, see [Amazon Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/ "https://aws.amazon.com/s3/storage-classes/glacier/").

Amazon Glacier (original standalone vault-based service) is no longer accepting new customers. Amazon Glacier is a standalone service with its own APIs that stores data in vaults and is distinct from Amazon S3 and the Amazon S3 Glacier storage classes. Your existing data will remain secure and accessible in Amazon Glacier indefinitely. No migration is required. For low-cost, long-term archival storage, AWS recommends the [Amazon S3 Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/ "https://aws.amazon.com/s3/storage-classes/glacier/"), which deliver a superior customer experience with S3 bucket-based APIs, full AWS Region availability, lower costs, and AWS service integration. If you want enhanced capabilities, consider migrating to Amazon S3 Glacier storage classes by using our [AWS Solutions Guidance for transferring data from Amazon Glacier vaults to Amazon S3 Glacier storage classes](https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/ "https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/").

# Data Types Used in Job Operations

The following are data types used with the job operations in Amazon Glacier.

###### Topics

- [CSVInput](api-CSVInput.md "api-CSVInput.md")
- [CSVOutput](api-CSVOutput.md "api-CSVOutput.md")
- [Encryption](api-Encryption.md "api-Encryption.md")
- [GlacierJobDescription](api-GlacierJobDescription.md "api-GlacierJobDescription.md")
- [Grant](api-Grant.md "api-Grant.md")
- [Grantee](api-Grantee.md "api-Grantee.md")
- [InputSerialization](api-InputSerialization.md "api-InputSerialization.md")
- [InventoryRetrievalJobInput](api-InventoryRetrievalJobInput.md "api-InventoryRetrievalJobInput.md")
- [jobParameters](api-jobParameters.md "api-jobParameters.md")
- [OutputLocation](api-OutputLocation.md "api-OutputLocation.md")
- [OutputSerialization](api-OutputSerialization.md "api-OutputSerialization.md")
- [S3Location](api-S3Location.md "api-S3Location.md")
- [SelectParameters](api-SelectParameters.md "api-SelectParameters.md")
