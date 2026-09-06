

 **This page is only for existing customers of the Amazon Glacier service using Vaults and the original REST API from 2012.**

If you're looking for archival storage solutions, we recommend using the Amazon Glacier storage classes in Amazon S3, S3 Glacier Instant Retrieval, S3 Glacier Flexible Retrieval, and S3 Glacier Deep Archive. To learn more about these storage options, see [Amazon Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/).

Amazon Glacier (original standalone vault-based service) is no longer accepting new customers. Amazon Glacier is a standalone service with its own APIs that stores data in vaults and is distinct from Amazon S3 and the Amazon S3 Glacier storage classes. Your existing data will remain secure and accessible in Amazon Glacier indefinitely. No migration is required. For low-cost, long-term archival storage, AWS recommends the [Amazon S3 Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/), which deliver a superior customer experience with S3 bucket-based APIs, full AWS Region availability, lower costs, and AWS service integration. If you want enhanced capabilities, consider migrating to Amazon S3 Glacier storage classes by using our [AWS Solutions Guidance for transferring data from Amazon Glacier vaults to Amazon S3 Glacier storage classes](https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/).

# GlacierJobDescription
<a name="api-GlacierJobDescription"></a>

Contains the description of an Amazon Glacier (Amazon Glacier) job.

## Contents
<a name="api-GlacierJobDescription-contents"></a>

**Action**  
The job type. It is either `ArchiveRetrieval`, `InventoryRetrieval`, or `Select`.  
*Type*: String

**ArchiveId**  
The archive ID requested for a select or archive retrieval job. Otherwise, this field is `null`.  
*Type*: String

**ArchiveSHA256TreeHash**  
The SHA256 tree hash of the entire archive for an archive retrieval. For inventory retrieval jobs, this field is `null`.  
*Type*: String

**ArchiveSizeInBytes**  
For an `ArchiveRetrieval` job, this is the size in bytes of the archive being requested for download. For the `InventoryRetrieval` job, the value is `null`.  
*Type*: Number

**Completed**  
`true` if the job is completed; `false` otherwise.  
*Type*: Boolean

**CompletionDate**  
The date when the job completed.  
The Universal Coordinated Time (UTC) time that the job request completed. While the job is in progress, the value is null.  
*Type*: A string representation in the ISO 8601 date format, for example `2013-03-20T17:03:43.221Z`.

**CreationDate**  
The Universal Coordinated Time (UTC) date the job started.  
*Type*: A string representation in the ISO 8601 date format, for example `2013-03-20T17:03:43.221Z`.

**InventoryRetrievalParameters**  
Input parameters used for a range inventory retrieval.  
*Type*: [InventoryRetrievalJobInput](api-InventoryRetrievalJobInput.md) object

**InventorySizeInBytes**  
For an `InventoryRetrieval` job, this is the size in bytes of the inventory requested for download. For the `ArchiveRetrieval` or `Select` job, the value is `null`.  
*Type*: Number

**JobDescription**  
The job description that you provided when you initiated the job.  
*Type*: String

**JobId**  
The ID that identifies the job in Amazon Glacier.  
*Type*: String

**JobOutputPath**  
Contains the job output location.  
*Type*: String

**OutputLocation**  
 An object that contains information about the location where the select job results and errors are stored.   
*Type*: [OutputLocation](api-OutputLocation.md) object

**RetrievalByteRange**  
The retrieved byte range for archive retrieval jobs in the form "{{StartByteValue}}-{{EndByteValue}}." If no range was specified in the archive retrieval, then the whole archive is retrieved and *StartByteValue* equals 0 and *EndByteValue* equals the size of the archive minus 1. For inventory retrieval jobs, this field is `null`.   
*Type*: String

**SelectParameters**  
An object that contains information about the parameters used for a select.  
*Type*: [SelectParameters](api-SelectParameters.md) object

**SHA256TreeHash**  
The SHA256 tree hash value for the requested range of an archive. If the [Initiate Job (POST jobs)](api-initiate-job-post.md) request for an archive specified a tree-hash aligned range, then this field returns a value. For more information about tree-hash alignment for archive range retrievals, see [Receiving Checksums When Downloading Data](checksum-calculations-range.md).  
For the specific case in which the whole archive is retrieved, this value is the same as the `ArchiveSHA256TreeHash` value.   
This field is `null` in the following situations:  
+ Archive retrieval jobs that specify a range that is not tree-hash aligned.
+ Archival jobs that specify a range that is equal to the whole archive and the job status is `InProgress`. 
+ Inventory jobs.
+ Select jobs.
*Type*: String

**SNSTopic**  
The Amazon Resource Name (ARN) that represents an Amazon SNS topic where notification of job completion or failure is sent, if notification was configured in the job initiation ([Initiate Job (POST jobs)](api-initiate-job-post.md)).  
*Type*: String

**StatusCode**  
The code indicating the status of the job.  
*Valid Values*: `InProgress` \| `Succeeded` \| `Failed`  
*Type*: String

**StatusMessage**  
The job status message.  
*Type*: String

**Tier**  
The data access tier to use for the select or archive retrieval.  
*Valid Values*: `Expedited` \| `Standard` \| `Bulk`  
*Type*: String

**VaultARN**  
The ARN of the vault of which the job is a subresource.  
*Type*: String

## More Info
<a name="more-info-api-GlacierJobDescription"></a>
+ [Initiate Job (POST jobs)](api-initiate-job-post.md)