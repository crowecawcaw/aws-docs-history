**This page is only for existing customers of the Amazon Glacier service using Vaults and the original REST API from 2012.**

If you're looking for archival storage solutions, we recommend using the Amazon Glacier storage classes in Amazon S3, S3 Glacier Instant Retrieval, S3 Glacier Flexible Retrieval, and S3 Glacier Deep Archive. To learn more about these storage options, see [Amazon Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/ "https://aws.amazon.com/s3/storage-classes/glacier/").

Amazon Glacier (original standalone vault-based service) is no longer accepting new customers. Amazon Glacier is a standalone service with its own APIs that stores data in vaults and is distinct from Amazon S3 and the Amazon S3 Glacier storage classes. Your existing data will remain secure and accessible in Amazon Glacier indefinitely. No migration is required. For low-cost, long-term archival storage, AWS recommends the [Amazon S3 Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/ "https://aws.amazon.com/s3/storage-classes/glacier/"), which deliver a superior customer experience with S3 bucket-based APIs, full AWS Region availability, lower costs, and AWS service integration. If you want enhanced capabilities, consider migrating to Amazon S3 Glacier storage classes by using our [AWS Solutions Guidance for transferring data from Amazon Glacier vaults to Amazon S3 Glacier storage classes](https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/ "https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/").

# S3Location

Contains information about the location in Amazon S3 where the job results are stored.

## Contents

**AccessControlList**

A list of grants that control access to the stored results.

_Type_: Array of [Grant](api-Grant.md "api-Grant.md") objects

_Required_: no

**BucketName**

The name of the Amazon S3 bucket where the job results are stored. The bucket must be in the
same AWS Region as the vault that contains the input archive object.

_Type_: String

_Required_: yes

**CannedACL**

The canned access control list (ACL) to apply to the job results.

_Type_: String

_Valid Values_: `private` |
`public-read` | `public-read-write` |
`aws-exec-read` | `authenticated-read` |
`bucket-owner-read` | `bucket-owner-full-control`

_Required_: no

**Encryption**

An object that contains information about the encryption used to store the job results in
Amazon S3.

_Type_: [Encryption](api-Encryption.md "api-Encryption.md") object

_Required_: no

**Prefix**

The prefix that is prepended to the results for this request. The maximum length for the
prefix is 512 bytes.

_Type_: String

_Required_: yes

**StorageClass**

The class of storage used to store the job results.

_Type_: String

_Valid Values_: `STANDARD` |
`REDUCED_REDUNDANCY` | `STANDARD_IA`

_Required_: no

**Tagging**

The tag set that is applied to the job results.

_Type_: String to string map

_Required_: no

**UserMetadata**

A map of metadata to store with the job results in Amazon S3.

_Type_: String to string map

_Required_: no

## More Info

- [Initiate Job (POST jobs)](api-initiate-job-post.md "api-initiate-job-post.md")
