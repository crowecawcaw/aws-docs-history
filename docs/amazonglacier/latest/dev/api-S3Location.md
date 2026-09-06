

 **This page is only for existing customers of the Amazon Glacier service using Vaults and the original REST API from 2012.**

If you're looking for archival storage solutions, we recommend using the Amazon Glacier storage classes in Amazon S3, S3 Glacier Instant Retrieval, S3 Glacier Flexible Retrieval, and S3 Glacier Deep Archive. To learn more about these storage options, see [Amazon Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/).

Amazon Glacier (original standalone vault-based service) is no longer accepting new customers. Amazon Glacier is a standalone service with its own APIs that stores data in vaults and is distinct from Amazon S3 and the Amazon S3 Glacier storage classes. Your existing data will remain secure and accessible in Amazon Glacier indefinitely. No migration is required. For low-cost, long-term archival storage, AWS recommends the [Amazon S3 Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/), which deliver a superior customer experience with S3 bucket-based APIs, full AWS Region availability, lower costs, and AWS service integration. If you want enhanced capabilities, consider migrating to Amazon S3 Glacier storage classes by using our [AWS Solutions Guidance for transferring data from Amazon Glacier vaults to Amazon S3 Glacier storage classes](https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/).

# S3Location
<a name="api-S3Location"></a>

 Contains information about the location in Amazon S3 where the job results are stored.

## Contents
<a name="api-S3Location-contents"></a>

**AccessControlList**  
A list of grants that control access to the stored results.  
*Type*: Array of [Grant](api-Grant.md) objects  
*Required*: no

**BucketName**  
The name of the Amazon S3 bucket where the job results are stored. The bucket must be in the same AWS Region as the vault that contains the input archive object.  
*Type*: String  
*Required*: yes

**CannedACL**  
The canned access control list (ACL) to apply to the job results.  
*Type*: String  
*Valid Values*: `private` \| `public-read` \| `public-read-write` \| `aws-exec-read` \| `authenticated-read` \| `bucket-owner-read` \| `bucket-owner-full-control`  
*Required*: no

**Encryption**  
An object that contains information about the encryption used to store the job results in Amazon S3.  
*Type*: [Encryption](api-Encryption.md) object  
*Required*: no

**Prefix**  
The prefix that is prepended to the results for this request. The maximum length for the prefix is 512 bytes.  
*Type*: String  
*Required*: yes

**StorageClass**  
The class of storage used to store the job results.  
*Type*: String  
*Valid Values*: `STANDARD` \| `REDUCED_REDUNDANCY` \| `STANDARD_IA`  
*Required*: no

**Tagging**  
The tag set that is applied to the job results.  
*Type*: String to string map  
*Required*: no

**UserMetadata**  
A map of metadata to store with the job results in Amazon S3.  
*Type*: String to string map  
*Required*: no

## More Info
<a name="more-info-api-S3Location"></a>

 
+ [Initiate Job (POST jobs)](api-initiate-job-post.md)