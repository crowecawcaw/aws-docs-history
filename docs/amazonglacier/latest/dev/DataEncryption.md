**This page is only for existing customers of the Amazon Glacier service using Vaults and the original REST API from 2012.**

If you're looking for archival storage solutions, we recommend using the Amazon Glacier storage classes in Amazon S3, S3 Glacier Instant Retrieval, S3 Glacier Flexible Retrieval, and S3 Glacier Deep Archive. To learn more about these storage options, see [Amazon Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/ "https://aws.amazon.com/s3/storage-classes/glacier/").

Amazon Glacier (original standalone vault-based service) is no longer accepting new customers. Amazon Glacier is a standalone service with its own APIs that stores data in vaults and is distinct from Amazon S3 and the Amazon S3 Glacier storage classes. Your existing data will remain secure and accessible in Amazon Glacier indefinitely. No migration is required. For low-cost, long-term archival storage, AWS recommends the [Amazon S3 Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/ "https://aws.amazon.com/s3/storage-classes/glacier/"), which deliver a superior customer experience with S3 bucket-based APIs, full AWS Region availability, lower costs, and AWS service integration. If you want enhanced capabilities, consider migrating to Amazon S3 Glacier storage classes by using our [AWS Solutions Guidance for transferring data from Amazon Glacier vaults to Amazon S3 Glacier storage classes](https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/ "https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/").

# Data Encryption

Data protection refers to protecting data while in-transit (as it travels to and from
Amazon Glacier) and at rest (while it is stored in AWS data centers). You can protect data
in transit that is uploaded directly to Amazon Glacier using Secure Sockets Layer (SSL) or
client-side encryption.

You can also access Amazon Glacier through Amazon S3. Amazon S3 supports lifecycle configuration on
an Amazon S3 bucket, which enables you to transition objects to the Amazon Glacier storage class
for archival. Data in transit between Amazon S3 and Amazon Glacier via lifecycle policies is
encrypted using SSL.

Data at rest stored in Amazon Glacier is automatically server-side encrypted using 256-bit
Advanced Encryption Standard (AES-256) with keys maintained by AWS. If you prefer to
manage your own keys, you can also use client-side encryption before storing data in
Amazon Glacier. For more information about how to setup default encryption for Amazon S3, see
[Amazon S3 Default Encryption](../../../AmazonS3/latest/userguide/bucket-encryption.md "../../../AmazonS3/latest/userguide/bucket-encryption.md") in
the _Amazon Simple Storage Service User Guide_.
