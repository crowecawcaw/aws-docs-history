

 **This page is only for existing customers of the Amazon Glacier service using Vaults and the original REST API from 2012.**

If you're looking for archival storage solutions, we recommend using the Amazon Glacier storage classes in Amazon S3, S3 Glacier Instant Retrieval, S3 Glacier Flexible Retrieval, and S3 Glacier Deep Archive. To learn more about these storage options, see [Amazon Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/).

Amazon Glacier (original standalone vault-based service) is no longer accepting new customers. Amazon Glacier is a standalone service with its own APIs that stores data in vaults and is distinct from Amazon S3 and the Amazon S3 Glacier storage classes. Your existing data will remain secure and accessible in Amazon Glacier indefinitely. No migration is required. For low-cost, long-term archival storage, AWS recommends the [Amazon S3 Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/), which deliver a superior customer experience with S3 bucket-based APIs, full AWS Region availability, lower costs, and AWS service integration. If you want enhanced capabilities, consider migrating to Amazon S3 Glacier storage classes by using our [AWS Solutions Guidance for transferring data from Amazon Glacier vaults to Amazon S3 Glacier storage classes](https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/).

# Encryption
<a name="api-Encryption"></a>

Contains information about the encryption used to store the job results in Amazon S3.

## Contents
<a name="api-Encryption-contents"></a>

**Encryption**  
The server-side encryption algorithm used when storing job results in Amazon S3. The default is no encryption.  
*Type*: String  
*Valid Values*: `aws:kms` \| `AES256`  
*Required*: no

**KMSContext**  
Optional. If the encryption type is `aws:kms,` you can use this value to specify the encryption context for the job results.  
*Type*: String  
*Required*: no

**KMSKeyId**  
The AWS Key Management Service (AWS KMS) key ID to use for object encryption.  
*Type*: String  
*Required*: no

## More Info
<a name="more-info-api-Encryption"></a>

 
+ [Initiate Job (POST jobs)](api-initiate-job-post.md)