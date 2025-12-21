**This page is only for existing customers of the Amazon Glacier service using Vaults and the original REST API from 2012.**

If you're looking for archival storage solutions, we recommend using the Amazon Glacier storage classes in Amazon S3, S3 Glacier Instant Retrieval, S3 Glacier Flexible Retrieval, and S3 Glacier Deep Archive. To learn more about these storage options, see [Amazon Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/ "https://aws.amazon.com/s3/storage-classes/glacier/").

Amazon Glacier (original standalone vault-based service) is no longer accepting new customers. Amazon Glacier is a standalone service with its own APIs that stores data in vaults and is distinct from Amazon S3 and the Amazon S3 Glacier storage classes. Your existing data will remain secure and accessible in Amazon Glacier indefinitely. No migration is required. For low-cost, long-term archival storage, AWS recommends the [Amazon S3 Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/ "https://aws.amazon.com/s3/storage-classes/glacier/"), which deliver a superior customer experience with S3 bucket-based APIs, full AWS Region availability, lower costs, and AWS service integration. If you want enhanced capabilities, consider migrating to Amazon S3 Glacier storage classes by using our [AWS Solutions Guidance for transferring data from Amazon Glacier vaults to Amazon S3 Glacier storage classes](https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/ "https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/").

# CSVInput

Contains information about the comma-separated values (CSV) file.

## Contents

**Comments**

A single character used to indicate that a row should be ignored when the
character is present at the start of that row.

_Type_: String

_Required_: no

**FieldDelimiter**

A single character used to separate individual fields from each other within a record.
The character must be a `\n`, `\r`, or an ASCII
character in the range 32–126. The default is a comma
(`,`).

_Type_: String

_Default_: ,

_Required_: no

**FileHeaderInfo**

A value that describes what to do with the first line of the input.

_Type_: String

_Valid Values_: `Use` | `Ignore`
| `None`

_Required_: no

**QuoteCharacter**

A single character used as an escape character where the field delimiter is part of the
value.

_Type_: String

_Required_: no

**QuoteEscapeCharacter**

A single character used for escaping the quotation-mark character inside an already escaped value.

_Type_: String

_Required_: no

**RecordDelimiter**

A single character used to separate individual records from each other.

_Type_: String

_Required_: no

## More Info

- [Initiate Job (POST jobs)](api-initiate-job-post.md "api-initiate-job-post.md")
