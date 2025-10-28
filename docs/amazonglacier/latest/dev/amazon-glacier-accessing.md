**This page is only for existing customers of the Amazon Glacier service using Vaults and the original REST API from 2012.**

If you're looking for archival storage solutions, we recommend using the Amazon Glacier storage classes in Amazon S3, S3 Glacier Instant Retrieval, S3 Glacier Flexible Retrieval, and S3 Glacier Deep Archive. To learn more about these storage options, see [Amazon Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/ "https://aws.amazon.com/s3/storage-classes/glacier/").

Amazon Glacier (original standalone vault-based service) will no longer accept new customers starting December 15, 2025, with no impact to existing customers. Amazon Glacier is a standalone service with its own APIs that stores data in vaults and is distinct from Amazon S3 and the Amazon S3 Glacier storage classes. Your existing data will remain secure and accessible in Amazon Glacier indefinitely. No migration is required. For low-cost, long-term archival storage, AWS recommends the [Amazon S3 Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/ "https://aws.amazon.com/s3/storage-classes/glacier/"), which deliver a superior customer experience with S3 bucket-based APIs, full AWS Region availability, lower costs, and AWS service integration. If you want enhanced capabilities, consider migrating to Amazon S3 Glacier storage classes by using our [AWS Solutions Guidance for transferring data from Amazon Glacier vaults to Amazon S3 Glacier storage classes](https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/ "https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/").

# Accessing Amazon Glacier

Amazon Glacier is a RESTful web service that uses HTTP and HTTPS as a transport protocol and
JavaScript Object Notation (JSON) as a message-serialization format. Your application
code can make requests directly to the Amazon Glacier web service API. When using the REST
API directly, you must write the necessary code to sign and authenticate your requests.
For more information about the API, see [API Reference for Amazon Glacier](amazon-glacier-api.md "amazon-glacier-api.md").

Alternatively, you can simplify application development by using the AWS SDKs that
wrap the Amazon Glacier REST API calls. You provide your credentials, and these libraries
take care of authentication and request signing. For more information about using the
AWS SDKs, see [Using the AWS SDKs with Amazon Glacier](using-aws-sdk.md "using-aws-sdk.md").

Amazon Glacier also provides a console. However, all archive and job operations require you
to write code and make requests by using either the REST API directly or the AWS SDK
wrapper libraries. To access the Amazon Glacier console, go to [Amazon Glacier Console](https://console.aws.amazon.com/glacier/home "https://console.aws.amazon.com/glacier/home").

## Regions and Endpoints

You create a vault in a specific AWS Region. You always send your Amazon Glacier
requests to an endpoint specific to an AWS Region. For a list of the AWS Regions
supported by Amazon Glacier, see [Amazon Glacier endpoints and
quotas](../../../general/latest/gr/glacier-service.md "../../../general/latest/gr/glacier-service.md") in the _AWS General Reference_.
