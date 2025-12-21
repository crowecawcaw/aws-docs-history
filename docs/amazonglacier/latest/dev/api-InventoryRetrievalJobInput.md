**This page is only for existing customers of the Amazon Glacier service using Vaults and the original REST API from 2012.**

If you're looking for archival storage solutions, we recommend using the Amazon Glacier storage classes in Amazon S3, S3 Glacier Instant Retrieval, S3 Glacier Flexible Retrieval, and S3 Glacier Deep Archive. To learn more about these storage options, see [Amazon Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/ "https://aws.amazon.com/s3/storage-classes/glacier/").

Amazon Glacier (original standalone vault-based service) is no longer accepting new customers. Amazon Glacier is a standalone service with its own APIs that stores data in vaults and is distinct from Amazon S3 and the Amazon S3 Glacier storage classes. Your existing data will remain secure and accessible in Amazon Glacier indefinitely. No migration is required. For low-cost, long-term archival storage, AWS recommends the [Amazon S3 Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/ "https://aws.amazon.com/s3/storage-classes/glacier/"), which deliver a superior customer experience with S3 bucket-based APIs, full AWS Region availability, lower costs, and AWS service integration. If you want enhanced capabilities, consider migrating to Amazon S3 Glacier storage classes by using our [AWS Solutions Guidance for transferring data from Amazon Glacier vaults to Amazon S3 Glacier storage classes](https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/ "https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/").

# InventoryRetrievalJobInput

Provides options for specifying a range inventory retrieval job.

## Contents

**EndDate**

The end of the date range, in UTC time, for a vault inventory retrieval that includes
archives created before this date.

_Valid Values_: A string representation in the ISO 8601 date format (`YYYY-MM-DDThh:mm:ssTZD`) in seconds, for example `2013-03-20T17:03:43Z`.

_Type_: String. A string representation in the ISO 8601 date format (`YYYY-MM-DDThh:mm:ssTZD`) in seconds, for example `2013-03-20T17:03:43Z`.

_Required_: no

**Format**

The output format for the vault inventory list, which is set by the
[Initiate Job (POST jobs)](api-initiate-job-post.md "api-initiate-job-post.md") request
when initiating a job to retrieve a vault inventory.

_Valid Values_: `CSV` | `JSON`

_Required_: no

_Type_: String

**Limit**

The maximum number of inventory items that can be returned for each vault inventory
retrieval request.

_Valid Values_: An integer value greater than
or equal to 1.

_Type_: String

_Required_: no

**Marker**

An opaque string that represents where to continue pagination of the vault inventory
retrieval results. You use this marker in a new `Initiate Job`
request to obtain additional inventory items. If there are no more inventory
items, this value is null.

_Type_: String

_Required_: no

**StartDate**

The start of the date range, in UTC time, for a vault inventory retrieval that includes
archives created on or after this date.

_Valid Values_: A string representation in the ISO 8601 date format (`YYYY-MM-DDThh:mm:ssTZD`) in seconds, for example `2013-03-20T17:03:43Z`.

_Type_: String. A string representation in the ISO 8601 date format (`YYYY-MM-DDThh:mm:ssTZD`) in seconds, for example `2013-03-20T17:03:43Z`.

_Required_: no

## More Info

- [Initiate Job (POST jobs)](api-initiate-job-post.md "api-initiate-job-post.md")
