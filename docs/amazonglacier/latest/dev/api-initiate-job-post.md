**This page is only for existing customers of the Amazon Glacier service using Vaults and the original REST API from 2012.**

If you're looking for archival storage solutions, we recommend using the Amazon Glacier storage classes in Amazon S3, S3 Glacier Instant Retrieval, S3 Glacier Flexible Retrieval, and S3 Glacier Deep Archive. To learn more about these storage options, see [Amazon Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/ "https://aws.amazon.com/s3/storage-classes/glacier/").

Amazon Glacier (original standalone vault-based service) is no longer accepting new customers. Amazon Glacier is a standalone service with its own APIs that stores data in vaults and is distinct from Amazon S3 and the Amazon S3 Glacier storage classes. Your existing data will remain secure and accessible in Amazon Glacier indefinitely. No migration is required. For low-cost, long-term archival storage, AWS recommends the [Amazon S3 Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/ "https://aws.amazon.com/s3/storage-classes/glacier/"), which deliver a superior customer experience with S3 bucket-based APIs, full AWS Region availability, lower costs, and AWS service integration. If you want enhanced capabilities, consider migrating to Amazon S3 Glacier storage classes by using our [AWS Solutions Guidance for transferring data from Amazon Glacier vaults to Amazon S3 Glacier storage classes](https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/ "https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/").

# Initiate Job (POST jobs)

This operation initiates the following types of Amazon Glacier (Amazon Glacier) jobs:

- `archive-retrieval`— Retrieve an archive
- `inventory-retrieval`— Inventory a vault

###### Topics

- [Initializing an Archive or Vault
  Inventory Retrieval Job](#api-initiate-job-post-description "#api-initiate-job-post-description")
- [Requests](#api-initiate-job-post-requests "#api-initiate-job-post-requests")
- [Responses](#api-initiate-job-post-responses "#api-initiate-job-post-responses")
- [Examples](#api-initiate-job-post-examples "#api-initiate-job-post-examples")
- [Related Sections](#more-info-api-initiate-job-post "#more-info-api-initiate-job-post")

## Initializing an Archive or Vault

Inventory Retrieval Job

Retrieving an archive or a vault inventory are asynchronous operations that require
you to initiate a job. Once started, job cannot be cancelled. Retrieval is a two-step
process:

1. Initiate a retrieval job by using the [Initiate Job (POST jobs)](api-initiate-job-post.md "api-initiate-job-post.md") operation.

###### Important

A data retrieval policy can cause your initiate retrieval job request to
fail with a `PolicyEnforcedException`. For more information about
data retrieval policies, see [Amazon Glacier Data Retrieval Policies](data-retrieval-policy.md "data-retrieval-policy.md"). For more information
about the `PolicyEnforcedException` exception, see [Error Responses](api-error-responses.md "api-error-responses.md"). 2. After the job completes, download the bytes using the [Get Job Output (GET output)](api-job-output-get.md "api-job-output-get.md") operation.

The retrieval request is ran asynchronously. When you initiate a retrieval job,
Amazon Glacier creates a job and returns a job ID in the response. When Amazon Glacier completes
the job, you can get the job output (archive or inventory data). For information about
getting job output, see the [Get Job Output (GET output)](api-job-output-get.md "api-job-output-get.md") operation.

The job must complete before you can get its output. To determine when a job is
complete, you have the following options:

- Use an Amazon SNS notification— You can
  specify an Amazon SNS topic to which Amazon Glacier can post a notification after the job
  is completed. You can specify an SNS topic per job request. The notification is
  sent only after Amazon Glacier completes the job. In addition to specifying an SNS
  topic per job request, you can configure vault notifications for a vault so that
  job notifications are sent for all retrievals. For more information, see [Set Vault Notification Configuration (PUT
  notification-configuration)](api-vault-notifications-put.md "api-vault-notifications-put.md").
- Get job details— You can make a [Describe Job (GET JobID)](api-describe-job-get.md "api-describe-job-get.md")
  request to obtain job status information while a job is in progress. However, it
  is more efficient to use an Amazon SNS notification to determine when a job is
  complete.

###### Note

The information you get via notification is same that you get by calling [Describe Job (GET JobID)](api-describe-job-get.md "api-describe-job-get.md").

If for a specific event, you add both the notification configuration on the vault and
also specify an SNS topic in your initiate job request, Amazon Glacier sends both
notifications. For more information, see [Set Vault Notification Configuration (PUT
notification-configuration)](api-vault-notifications-put.md "api-vault-notifications-put.md").

### The Vault

Inventory

Amazon Glacier updates a vault inventory approximately once a day, starting on the day
you first upload an archive to the vault. If there have been no archive additions or
deletions to the vault since the last inventory, the inventory date is not updated.
When you initiate a job for a vault inventory, Amazon Glacier returns the last inventory
it generated, which is a point-in-time snapshot and not real-time data.

After Amazon Glacier creates the first inventory for the vault, it typically takes half
a day and up to a day before that inventory is available for retrieval.

You might not find it useful to retrieve a vault inventory for each archive
upload. However, suppose that you maintain a database on the client-side associating
metadata about the archives you upload to Amazon Glacier. Then, you might find the vault
inventory useful to reconcile information, as needed, in your database with the
actual vault inventory. For more information about the data fields returned in an
inventory job output, see [Response Body](api-job-output-get.md#api-job-output-get-responses-elements "api-job-output-get.md#api-job-output-get-responses-elements").

### Range

Inventory Retrieval

You can limit the number of inventory items retrieved by filtering on the archive
creation date or by setting a limit.

###### Filtering by Archive Creation Date

You can retrieve inventory items for archives created between
`StartDate` and `EndDate` by specifying values for
these parameters in the **Initiate Job** request.
Archives created on or after the `StartDate` and before the
`EndDate` are returned. If you provide only the
`StartDate` without the `EndDate`, you retrieve the
inventory for all archives created on or after the `StartDate`. If
you provide only the `EndDate` without the `StartDate`,
you get back the inventory for all archives created before the
`EndDate`.

###### Limiting Inventory Items per Retrieval

You can limit the number of inventory items returned by setting the
`Limit` parameter in the **Initiate
Job** request. The inventory job output contains inventory items up
to the specified `Limit`. If there are more inventory items
available, the result is paginated. After a job is complete, you can use the
[Describe Job (GET JobID)](api-describe-job-get.md "api-describe-job-get.md")
operation to get a marker that you use in a subsequent **Initiate Job** request. The marker indicates the starting point to
retrieve the next set of inventory items. You can page through your entire
inventory by repeatedly making **Initiate Job**
requests with the marker from the previous **Describe
Job** output. You do so until you get a marker from **Describe Job** that returns null, indicating that there
are no more inventory items available.

You can use the `Limit` parameter together with the date range
parameters.

### Ranged Archive Retrieval

You can initiate archive retrieval for the whole archive or a range of the
archive. In the case of ranged archive retrieval, you specify a byte range to return
or the whole archive. The range specified must be megabyte (MB) aligned. In other
words, the range start value must be divisible by 1 MB and the range end value plus
1 must be divisible by 1 MB or equal the end of the archive. If the ranged archive
retrieval is not megabyte-aligned, this operation returns a `400`
response. Furthermore, to ensure that you get checksum values for data you download
using **Get Job Output** ([Get Job Output (GET output)](api-job-output-get.md "api-job-output-get.md")), the range
must be tree-hash aligned. For more information about tree-hash aligned ranges, see
[Receiving Checksums When Downloading Data](checksum-calculations-range.md "checksum-calculations-range.md").

### Expedited, Standard, and Bulk

Tiers

When initiating an archive retrieval job, you can specify one of the
following options in the `Tier` field of the request body:

- **`Expedited`** – Expedited
  allows you to quickly access your data when occasional urgent requests for
  restoring archives are required. For all but the largest archives (250 MB+),
  data accessed using the Expedited tier is typically made available within
  1–5 minutes.
- **`Standard`** – Standard
  allows you to access any of your archives within several hours. Data
  accessed using the Standard tier typically made available within 3–5 hours.
  This option is the default one for job requests that don't specify the
  tier option.
- **`Bulk`** – Bulk is the
  lowest-cost tier for Amazon Glacier, enabling you to retrieve large amounts, even
  petabytes, of data inexpensively in a day. Data accessed using the Bulk tier
  is typically made available within 5–12 hours.

For more information about expedited and bulk retrievals, see [Retrieving Amazon Glacier Archives](downloading-an-archive-two-steps.md "downloading-an-archive-two-steps.md").

## Requests

To initiate a job, you use the HTTP `POST` method and scope the request to
the vault's `jobs` subresource. You specify details of the job request in the
JSON document of your request. The job type is specified with the `Type`
field. Optionally, you can specify an `SNSTopic` field to indicate an Amazon SNS
topic to which Amazon Glacier can post notification after it completes the job.

###### Note

To post a notification to Amazon SNS, you must create the topic yourself if it
doesn't already exist. Amazon Glacier doesn't create the topic for you. The topic
must have permissions to receive publications from a Amazon Glacier vault. Amazon Glacier doesn't
verify if the vault has permission to publish to the topic. If the permissions are
not configured appropriately, you might not receive notification even after the job
completes.

### Syntax

The following is the request syntax for initiating a job.

```
POST /`AccountId`/vaults/`VaultName`/jobs HTTP/1.1
Host: glacier.`Region`.amazonaws.com
Date: `Date`
Authorization: `SignatureValue`
x-amz-glacier-version: 2012-06-01

{
   "jobParameters": {
      "ArchiveId": "`string`",
      "Description": "`string`",
      "Format": "`string`",
      "InventoryRetrievalParameters": {
         "EndDate": "`string`",
         "Limit": "`string`",
         "Marker": "`string`",
         "StartDate": "`string`"
      },
      "OutputLocation": {
         "S3": {
            "AccessControlList": [
               {
                  "Grantee": {
                     "DisplayName": "`string`",
                     "EmailAddress": "`string`",
                     "ID": "`string`",
                     "Type": "`string`",
                     "URI": "`string`"
                  },
                  "Permission": "`string`"
               }
            ],
            "BucketName": "`string`",
            "CannedACL": "`string`",
            "Encryption": {
               "EncryptionType": "`string`",
               "KMSContext": "`string`",
               "KMSKeyId": "`string`"
            },
            "Prefix": "`string`",
            "StorageClass": "`string`",
            "Tagging": {
               "`string`" : "`string`"
            },
            "UserMetadata": {
               "`string`" : "`string`"
            }
         }
      },
      "RetrievalByteRange": "`string`",
      "SelectParameters": {
         "Expression": "`string`",
         "ExpressionType": "`string`",
         "InputSerialization": {
            "csv": {
               "Comments": "`string`",
               "FieldDelimiter": "`string`",
               "FileHeaderInfo": "`string`",
               "QuoteCharacter": "`string`",
               "QuoteEscapeCharacter": "`string`",
               "RecordDelimiter": "`string`"
            }
         },
         "OutputSerialization": {
            "csv": {
               "FieldDelimiter": "`string`",
               "QuoteCharacter": "`string`",
               "QuoteEscapeCharacter": "`string`",
               "QuoteFields": "`string`",
               "RecordDelimiter": "`string`"
            }
         }
      },
      "SNSTopic": "`string`",
      "Tier": "`string`",
      "Type": "`string`"
   }
}

```

###### Note

The `AccountId` value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single '`-`' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens ('-') in the ID.

### Request Body

The request accepts the following data in JSON format in the body of the
request.

jobParameters

Provides options for specifying job information.

_Type_: [jobParameters](api-jobParameters.md "api-jobParameters.md") object

_Required_: Yes

## Responses

Amazon Glacier creates the job. In the response, it returns the URI of the job.

### Syntax

```
HTTP/1.1 202 Accepted
x-amzn-RequestId: **x-amzn-RequestId**
Date: **Date**
Location: `location`
x-amz-job-id: `jobId`
x-amz-job-output-path: `jobOutputPath`
```

### Response Headers

| Header                  | Description                                                                                                                                                                                                                      |
| ----------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Location`              | The relative URI path of the job. You can use this URI path to<br>find the job status. For more information, see [Describe Job (GET JobID)](api-describe-job-get.md "api-describe-job-get.md").<br>Type: String<br>Default: None |
| `x-amz-job-id`          | The ID of the job. This value is also included as part of the<br>`Location` header.<br>Type: String<br>Default: None                                                                                                             |
| `x-amz-job-output-path` | The path to the location of where<br>the select results are stored.<br>Type: String<br>Default: None                                                                                                                             |

### Response Body

This operation does not return a response body.

### Errors

This operation includes the following error or errors, in addition to the possible errors common to all Amazon Glacier operations. For information about Amazon Glacier
errors and a list of error codes, see [Error Responses](api-error-responses.md "api-error-responses.md").

| Code                            | Description                                                                                                                                                                 | HTTP Status Code          | Type   |
| ------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------- | ------ |
| `InsufficientCapacityException` | Returned if there is insufficient capacity to process this<br>expedited request. This error only applies to expedited retrievals<br>and not to standard or bulk retrievals. | `503 Service Unavailable` | Server |

## Examples

### Example Request: Initiate an

archive retrieval job

```
POST /-/vaults/examplevault/jobs HTTP/1.1
Host: glacier.us-west-2.amazonaws.com
x-amz-Date: 20170210T120000Z
x-amz-glacier-version: 2012-06-01
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20141123/us-west-2/glacier/aws4_request,SignedHeaders=host;x-amz-date;x-amz-glacier-version,Signature=9257c16da6b25a715ce900a5b45b03da0447acf430195dcb540091b12966f2a2

{
  "Type": "archive-retrieval",
  "ArchiveId": "NkbByEejwEggmBz2fTHgJrg0XBoDfjP4q6iu87-TjhqG6eGoOY9Z8i1_AUyUsuhPAdTqLHy8pTl5nfCFJmDl2yEZONi5L26Omw12vcs01MNGntHEQL8MBfGlqrEXAMPLEArchiveId",
  "Description": "My archive description",
  "SNSTopic": "arn:aws:sns:us-west-2:111111111111:Glacier-ArchiveRetrieval-topic-Example",
  "Tier" : "Bulk"
}
```

The following is an example of the body of a request that specifies a range of the
archive to retrieve using the `RetrievalByteRange` field.

```
{
  "Type": "archive-retrieval",
  "ArchiveId": "NkbByEejwEggmBz2fTHgJrg0XBoDfjP4q6iu87-TjhqG6eGoOY9Z8i1_AUyUsuhPAdTqLHy8pTl5nfCFJmDl2yEZONi5L26Omw12vcs01MNGntHEQL8MBfGlqrEXAMPLEArchiveId",
  "Description": "My archive description",
  "RetrievalByteRange": "2097152-4194303",
  "SNSTopic": "arn:aws:sns:us-west-2:111111111111:Glacier-ArchiveRetrieval-topic-Example",
  "Tier" : "Bulk"
}
```

### Example Response

```
HTTP/1.1 202 Accepted
x-amzn-RequestId: AAABZpJrTyioDC_HsOmHae8EZp_uBSJr6cnGOLKp_XJCl-Q
Date: Wed, 10 Feb 2017 12:00:00 GMT
Location: /111122223333/vaults/examplevault/jobs/HkF9p6o7yjhFx-K3CGl6fuSm6VzW9T7esGQfco8nUXVYwS0jlb5gq1JZ55yHgt5vP54ZShjoQzQVVh7vEXAMPLEjobID
x-amz-job-id: HkF9p6o7yjhFx-K3CGl6fuSm6VzW9T7esGQfco8nUXVYwS0jlb5gq1JZ55yHgt5vP54ZShjoQzQVVh7vEXAMPLEjobID
```

### Example

Request: Initiate an inventory retrieval job

The following request initiates an inventory retrieval job to get a list of
archives from the `examplevault` vault. The `Format` set to
`CSV` in the body of the request indicates that the inventory is
returned in CSV format.

```
POST /-/vaults/examplevault/jobs HTTP/1.1
Host: glacier.us-west-2.amazonaws.com
x-amz-Date: 20170210T120000Z
Content-Type: application/x-www-form-urlencoded
x-amz-glacier-version: 2012-06-01
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20141123/us-west-2/glacier/aws4_request,SignedHeaders=host;x-amz-date;x-amz-glacier-version,Signature=9257c16da6b25a715ce900a5b45b03da0447acf430195dcb540091b12966f2a2

{
  "Type": "inventory-retrieval",
  "Description": "My inventory job",
  "Format": "CSV",
  "SNSTopic": "arn:aws:sns:us-west-2:111111111111:Glacier-InventoryRetrieval-topic-Example"
}
```

### Example

Response

```
HTTP/1.1 202 Accepted
x-amzn-RequestId: AAABZpJrTyioDC_HsOmHae8EZp_uBSJr6cnGOLKp_XJCl-Q
Date: Wed, 10 Feb 2017 12:00:00 GMT
Location: /111122223333/vaults/examplevault/jobs/HkF9p6o7yjhFx-K3CGl6fuSm6VzW9T7esGQfco8nUXVYwS0jlb5gq1JZ55yHgt5vP54ZShjoQzQVVh7vEXAMPLEjobID
x-amz-job-id: HkF9p6o7yjhFx-K3CGl6fuSm6VzW9T7esGQfco8nUXVYwS0jlb5gq1JZ55yHgt5vP54ZShjoQzQVVh7vEXAMPLEjobID
```

### Example

Requests: Initiate an inventory retrieval job by using date filtering with a set
limit, and a subsequent request to retrieve the next page of inventory
items.

The following request initiates a vault inventory retrieval job by using date
filtering and setting a limit.

```

{
    "ArchiveId": null,
    "Description": null,
    "Format": "CSV",
    "RetrievalByteRange": null,
    "SNSTopic": null,
    "Type": "inventory-retrieval",
    "InventoryRetrievalParameters": {
        "StartDate": "2013-12-04T21:25:42Z",
        "EndDate": "2013-12-05T21:25:42Z",
        "Limit" : "10000"
    },
}
```

The following request is an example of a subsequent request to retrieve the next
page of inventory items using a marker obtained from [Describe Job (GET JobID)](api-describe-job-get.md "api-describe-job-get.md").

```
{
    "ArchiveId": null,
    "Description": null,
    "Format": "CSV",
    "RetrievalByteRange": null,
    "SNSTopic": null,
    "Type": "inventory-retrieval",
    "InventoryRetrievalParameters": {
        "StartDate": "2013-12-04T21:25:42Z",
        "EndDate": "2013-12-05T21:25:42Z",
        "Limit": "10000",
        "Marker": "vyS0t2jHQe5qbcDggIeD50chS1SXwYMrkVKo0KHiTUjEYxBGCqRLKaiySzdN7QXGVVV5XZpNVG67pCZ_uykQXFMLaxOSu2hO_-5C0AtWMDrfo7LgVOyfnveDRuOSecUo3Ueq7K0"
    },
}
```

### Example

Response

```
HTTP/1.1 202 Accepted
x-amzn-RequestId: AAABZpJrTyioDC_HsOmHae8EZp_uBSJr6cnGOLKp_XJCl-Q
Date: Wed, 10 Feb 2017 12:00:00 GMT
Location: /111122223333/vaults/examplevault/jobs/HkF9p6o7yjhFx-K3CGl6fuSm6VzW9T7esGQfco8nUXVYwS0jlb5gq1JZ55yHgt5vP54ZShjoQzQVVh7vEXAMPLEjobID
x-amz-job-id: HkF9p6o7yjhFx-K3CGl6fuSm6VzW9T7esGQfco8nUXVYwS0jlb5gq1JZ55yHgt5vP54ZShjoQzQVVh7vEXAMPLEjobID
x-amz-job-output-path: test/HkF9p6o7yjhFx-K3CGl6fuSm6VzW9T7esGQfco8nUXVYwS0jlb5gq1JZ55yHgt5vP54ZShjoQzQVVh7vEXAMPLEjobID/
```

## Related Sections

- [Describe Job (GET JobID)](api-describe-job-get.md "api-describe-job-get.md")
- [Get Job Output (GET output)](api-job-output-get.md "api-job-output-get.md")
- [Identity and Access Management for Amazon Glacier](security-iam.md "security-iam.md")
