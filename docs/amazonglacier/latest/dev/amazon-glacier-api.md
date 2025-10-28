**This page is only for existing customers of the Amazon Glacier service using Vaults and the original REST API from 2012.**

If you're looking for archival storage solutions, we recommend using the Amazon Glacier storage classes in Amazon S3, S3 Glacier Instant Retrieval, S3 Glacier Flexible Retrieval, and S3 Glacier Deep Archive. To learn more about these storage options, see [Amazon Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/ "https://aws.amazon.com/s3/storage-classes/glacier/").

Amazon Glacier (original standalone vault-based service) will no longer accept new customers starting December 15, 2025, with no impact to existing customers. Amazon Glacier is a standalone service with its own APIs that stores data in vaults and is distinct from Amazon S3 and the Amazon S3 Glacier storage classes. Your existing data will remain secure and accessible in Amazon Glacier indefinitely. No migration is required. For low-cost, long-term archival storage, AWS recommends the [Amazon S3 Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/ "https://aws.amazon.com/s3/storage-classes/glacier/"), which deliver a superior customer experience with S3 bucket-based APIs, full AWS Region availability, lower costs, and AWS service integration. If you want enhanced capabilities, consider migrating to Amazon S3 Glacier storage classes by using our [AWS Solutions Guidance for transferring data from Amazon Glacier vaults to Amazon S3 Glacier storage classes](https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/ "https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/").

# API Reference for Amazon Glacier

Amazon Glacier supports a set of operations—specifically, a set of RESTful
API calls—that enable you to interact with the service.

You can use any programming library that can send HTTP requests to send your REST requests to
Amazon Glacier. When sending a REST request, Amazon Glacier requires that you authenticate
every request by signing the request. Additionally, when uploading an archive, you must also
compute the checksum of the payload and include it in your request. For more information,
see [Signing Requests](amazon-glacier-signing-requests.md "amazon-glacier-signing-requests.md").

If an error occurs, you need to know what Amazon Glacier sends in an error
response so that you can process it. This section provides all this information, in addition
to documenting the REST operations, so that you can make REST API calls directly.

You can either use the REST API calls directly or use the Amazon SDKs that provide wrapper
libraries. These libraries sign each request you send and
compute the checksum of the payload in your request. Therefore, using the Amazon SDKs
simplifies your coding task. This developer guide provides working examples of basic Amazon Glacier operations using the AWS SDK for Java and .NET. For more information see, [Using the AWS SDKs with Amazon Glacier](using-aws-sdk.md "using-aws-sdk.md").

###### Topics

- [Common Request Headers](api-common-request-headers.md "api-common-request-headers.md")
- [Common Response Headers](api-common-response-headers.md "api-common-response-headers.md")
- [Signing Requests](amazon-glacier-signing-requests.md "amazon-glacier-signing-requests.md")
- [Computing Checksums](checksum-calculations.md "checksum-calculations.md")
- [Error Responses](api-error-responses.md "api-error-responses.md")
- [Vault Operations](vault-operations.md "vault-operations.md")
- [Archive Operations](archive-operations.md "archive-operations.md")
- [Multipart Upload Operations](multipart-archive-operations.md "multipart-archive-operations.md")
- [Job Operations](job-operations.md "job-operations.md")
- [Data Types Used in Job Operations](api-data-types.md "api-data-types.md")
- [Data Retrieval Operations](data-retrieval-policy-operations.md "data-retrieval-policy-operations.md")
