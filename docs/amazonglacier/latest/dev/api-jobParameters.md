**This page is only for existing customers of the Amazon Glacier service using Vaults and the original REST API from 2012.**

If you're looking for archival storage solutions, we recommend using the Amazon Glacier storage classes in Amazon S3, S3 Glacier Instant Retrieval, S3 Glacier Flexible Retrieval, and S3 Glacier Deep Archive. To learn more about these storage options, see [Amazon Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/ "https://aws.amazon.com/s3/storage-classes/glacier/").

Amazon Glacier (original standalone vault-based service) is no longer accepting new customers. Amazon Glacier is a standalone service with its own APIs that stores data in vaults and is distinct from Amazon S3 and the Amazon S3 Glacier storage classes. Your existing data will remain secure and accessible in Amazon Glacier indefinitely. No migration is required. For low-cost, long-term archival storage, AWS recommends the [Amazon S3 Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/ "https://aws.amazon.com/s3/storage-classes/glacier/"), which deliver a superior customer experience with S3 bucket-based APIs, full AWS Region availability, lower costs, and AWS service integration. If you want enhanced capabilities, consider migrating to Amazon S3 Glacier storage classes by using our [AWS Solutions Guidance for transferring data from Amazon Glacier vaults to Amazon S3 Glacier storage classes](https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/ "https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/").

# jobParameters

Provides options for defining a job.

## Contents

**ArchiveId**

The ID of the archive that you want. This field is required if the `Type`
field is set to `select` or `archive-retrieval`. An
error occurs if you specify this field for an inventory retrieval job
request.

_Valid Values_: Must be a valid archive ID that you
obtained from a previous request to Amazon Glacier (Amazon Glacier).

_Type_: String

_Required_: Yes when `Type` is set to
`select` or `archive-retrieval`.

**Description**

The optional description for the job.

_Valid Values_: The description must be less than or equal to 1,024
bytes. The allowable characters are 7-bit ASCII without control
codes—specifically, ASCII values 32–126 decimal or 0x20–0x7E
hexadecimal.

_Type_: String

_Required_: no

**Format**

(Optional) The output format, when initiating a job to retrieve a vault inventory. If you
are initiating an inventory job and don't specify a `Format`
field, JSON is the default format.

_Valid Values_: `CSV` | `JSON`

_Type_: String

_Required_: no

**InventoryRetrievalParameters**

Input parameters used for a range inventory retrieval.

_Type_: [InventoryRetrievalJobInput](api-InventoryRetrievalJobInput.md "api-InventoryRetrievalJobInput.md") object

_Required_: no

**OutputLocation**

An object that contains information about the location where the select job results are
stored.

_Type_: [OutputLocation](api-OutputLocation.md "api-OutputLocation.md") object

_Required_: Yes, for `select` jobs.

**RetrievalByteRange**

The byte range to retrieve for an `archive-retrieval`, in the form
"`StartByteValue`-`EndByteValue`".
If this field isn't specified, the whole archive is retrieved. If this
field is specified, the byte range must be megabyte (1024\*1024) aligned.
Megabyte-aligned means that _StartByteValue_ must be
divisible by 1 MB, and _EndByteValue_ plus 1 must be
divisible by 1 MB or be the end of the archive specified as the archive byte
size value minus 1. If **RetrievalByteRange** is not
megabyte-aligned, this operation returns a `400` response.

An error occurs if you specify this field for an `inventory-retrieval` or
`select` job request.

_Type_: String

_Required_: no

**SelectParameters**

An object that contains information about the parameters used for a select.

_Type_: [SelectParameters](api-SelectParameters.md "api-SelectParameters.md") object

_Required_: no

**SNSTopic**

The Amazon Resource Name (ARN) of the Amazon SNS topic where Amazon Glacier sends a notification when
the job is completed and output is ready for you to download. The specified
topic publishes the notification to its subscribers.

The SNS topic must exist. If it doesn't, Amazon Glacier doesn't create it
for you. Additionally, the SNS topic must have a policy that allows the
account that created the job to publish messages to the topic. For
information about SNS topic names, see [CreateTopic](../../../sns/latest/api/API_CreateTopic.md "../../../sns/latest/api/API_CreateTopic.md") in the
_Amazon Simple Notification Service_
_API Reference_.

_Type_: String

_Required_: no

**Tier**

The tier to use for a select or an archive retrieval job.
`Standard` is the default value used.

_Valid Values_: `Expedited` |
`Standard` | `Bulk`

_Type_: String

_Required_: no

**Type**

The job type. You can initiate a job to perform a select query on an
archive, retrieve an archive, or get an inventory of a vault.

_Valid Values_: `select` |
`archive-retrieval` | `inventory-retrieval`

_Type_: String

_Required_: yes

## More Info

- [Initiate Job (POST jobs)](api-initiate-job-post.md "api-initiate-job-post.md")
