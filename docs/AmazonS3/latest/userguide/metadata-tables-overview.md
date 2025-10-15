# Discovering your data with S3 Metadata tables

Amazon S3 Metadata accelerates data discovery by automatically capturing metadata for objects in your
 general purpose buckets and storing it in read-only, fully managed Apache Iceberg tables
 that you can query. These read-only tables are called *metadata tables*.
 As objects are added to, updated, or removed from your general purpose buckets, S3 Metadata automatically
 refreshes the corresponding metadata tables to reflect the latest changes.

By default, S3 Metadata provides three types of metadata: 


* [System-defined metadata](UsingMetadata.md#SysMetadata "UsingMetadata.md#SysMetadata"), such as an object's creation
 time and storage class
* Custom metadata, such as tags and [user-defined
 metadata](UsingMetadata.md#UserMetadata "UsingMetadata.md#UserMetadata") that was included during object upload
* Event metadata, such as when an object is updated or deleted, and the AWS account that
 made the request
With S3 Metadata, you can easily find, store, and query metadata for your S3 objects, so that you can
 quickly prepare data for use in business analytics, content retrieval, artificial intelligence and machine
 learning (AI/ML) model training, and more. 

For each general purpose bucket, you can create a metadata table configuration that contains two
 complementary metadata tables:


* **Journal table** – By default, your metadata table
 configuration contains a *journal table*, which captures events that
 occur for the objects in your bucket. The journal table records changes made to your data in near real
 time, helping you to identify new data uploaded to your bucket, track recently deleted objects,
 monitor lifecycle transitions, and more. The journal table records new objects and updates to your
 objects and their metadata (those updates that require either a `PUT` or a
 `DELETE` operation). 


The journal table captures metadata only for change events (such as uploads, updates, and deletes)
 that happen after you create your metadata table configuration. Because this table is queryable, you
 can audit the changes to your bucket through simple SQL queries. 


The journal table is required for each metadata table configuration. (In the initial release of S3
 Metadata, the journal table was referred to as "the metadata table.")


For more information about what data is stored in journal tables, see [S3 Metadata journal tables schema](metadata-tables-schema.md "metadata-tables-schema.md").


To help minimize your storage costs, you can choose to enable journal table record expiration. For
 more information, see [Expiring journal table records](metadata-tables-expire-journal-table-records.md "metadata-tables-expire-journal-table-records.md").
* **Live inventory table** – Optionally, you can add a *live inventory table* to your metadata table configuration. The live
 inventory table provides a simple, queryable inventory of all the objects and their versions in your
 bucket so that you can determine the latest state of your data. 


You can use the live inventory table to simplify and speed up business workflows and big data jobs
 by identifying objects that you want to process for various workloads. For example, you can query the
 live inventory table to find all objects stored in a particular storage class, all objects with
 certain tags, all objects that aren't encrypted with server-side encryption using AWS Key Management Service (AWS KMS)
 keys (SSE-KMS), and more. 


When you enable the live inventory table for your metadata table configuration, the table goes
 through a process known as *backfilling*, during which Amazon S3 scans
 your general purpose bucket to retrieve the initial metadata for all objects that exist in the bucket.
 Depending on the number of objects in your bucket, this process can take minutes (minimum 15 minutes) to hours. When the
 backfilling process is finished, the status of your live inventory table changes from
 **Backfilling** to **Active**. After backfilling is completed,
 updates to your objects are typically reflected in the live inventory table within one hour.


You're charged for backfilling your inventory table. If your general purpose bucket has more than
 one billion objects, you're also charged a monthly fee for your live inventory table. For more
 information, see [Amazon S3 Pricing](https://aws.amazon.com/s3/pricing/ "https://aws.amazon.com/s3/pricing/").


For more information about what data is stored in live inventory tables, see [S3 Metadata live inventory tables schema](metadata-tables-inventory-schema.md "metadata-tables-inventory-schema.md").
Your metadata tables are stored in an AWS managed S3 table bucket, which provides storage that's
 optimized for tabular data. To query your metadata, you can integrate your table bucket with Amazon SageMaker Lakehouse.
 This integration, which uses the AWS Glue Data Catalog and AWS Lake Formation, allows AWS analytics services to
 automatically discover and access your table data. 

After your table bucket is integrated with the AWS Glue Data Catalog, you can directly query your metadata
 tables with AWS analytics services such as Amazon Athena, Amazon EMR, and Amazon Redshift. You can also create
 interactive dashboards with your query data by using Amazon QuickSight. For more information about integrating your
 AWS managed S3 table bucket with Amazon SageMaker Lakehouse, see [Integrating Amazon S3 Tables with AWS analytics
 services](s3-tables-integrating-aws.md "s3-tables-integrating-aws.md").

You can also query your metadata tables with Apache Spark, Apache Trino,
 and any other application that supports the Apache Iceberg format by using the AWS Glue
 Iceberg REST endpoint, the Amazon S3 Tables Iceberg REST endpoint, or the Amazon S3
 Tables Catalog for Apache Iceberg client catalog. For more information about accessing your
 metadata tables, see [Accessing table data](s3-tables-access.md "s3-tables-access.md").

For S3 Metadata pricing, see [Amazon S3 Pricing](https://aws.amazon.com/s3/pricing/ "https://aws.amazon.com/s3/pricing/"). 


## How metadata tables work


Metadata tables are managed by Amazon S3, and can't be modified by any IAM principal outside of Amazon S3
 itself. You can, however, delete your metadata tables. As a result, metadata tables are read-only, which
 helps ensure that they correctly reflect the contents of your general purpose bucket.


To generate and store object metadata in AWS managed metadata tables, you create a metadata table
 configuration for your general purpose bucket. Amazon S3 is designed to continuously update the metadata
 tables to reflect the latest changes to your data as long as the configuration is active on the general
 purpose bucket. 


Before you create a metadata table configuration, make sure that you have the necessary AWS Identity and Access Management
 (IAM) permissions to create and manage metadata tables. For more information, see [Setting up permissions for configuring metadata
 tables](metadata-tables-permissions.md "metadata-tables-permissions.md").


###### Metadata table storage, organization, and encryption


When you create your metadata table configuration, your metadata tables are stored in an AWS
 managed table bucket. All metadata table configurations in your account and in the same Region are
 stored in a single AWS managed table bucket. These AWS managed table buckets are named
 `aws-s3` and have the following Amazon Resource Name (ARN) format: 


`arn:aws:s3tables:`region`:`account_id`:bucket/aws-s3`


For example, if your account ID is 123456789012 and your general purpose bucket is in
 US East (N. Virginia) (`us-east-1`), your AWS managed table bucket is also created
 in US East (N. Virginia) (`us-east-1`) and has the following ARN:


`arn:aws:s3tables:`us-east-1`:123456789012:bucket/aws-s3`


By default, AWS managed table buckets are encrypted with server-side encryption using Amazon S3 managed
 keys (SSE-S3). After you create your first metadata configuration, you can set the default encryption
 setting for the AWS managed table bucket to use server-side encryption with AWS Key Management Service (AWS KMS) keys
 (SSE-KMS). For more information, see [Encryption for AWS managed table buckets](s3-tables-aws-managed-buckets.md#aws-managed-buckets-encryption "s3-tables-aws-managed-buckets.md#aws-managed-buckets-encryption") and [Specifying server-side encryption with AWS KMS keys
 (SSE-KMS) in table buckets](s3-tables-kms-specify.md "s3-tables-kms-specify.md").


Within your AWS managed table bucket, the metadata tables for your configuration are typically
 stored in a namespace with the following naming format: 


`b_`general-purpose-bucket-name``


###### Note


* If your general purpose bucket name contains any periods, the periods are converted to underscores
 (`_`) in the namespace name.
* If your general purpose bucket was created before March 1, 2018, its name might contain
 uppercase letters and underscores, and it might also be up to 255 characters long. If your bucket
 name has these characteristics, your metadata table namespace will have a different format. The
 general purpose bucket name will be prefixed with `b_`, truncated to 63 characters,
 converted to all lowercase, and suffixed with a hash.

Metadata tables have the following Amazon Resource Name (ARN) format, which includes the table ID of
 the metadata table: 


`arn:aws:s3tables:`region-code`:`account-id`:bucket/aws-s3/table/`table-id``


For example, a metadata table in the US East (N. Virginia) Region would have an ARN like the
 following:


`arn:aws:s3tables:us-east-1:111122223333:bucket/aws-s3/table/a12bc345-67d8-912e-3456-7f89123g4h56`


Journal tables have the name `journal`, and live inventory tables have the name
 `inventory`.


When you create your metadata table configuration, you can choose to encrypt your AWS managed
 metadata tables with server-side encryption using AWS Key Management Service (AWS KMS) keys (SSE-KMS). If you choose to use
 SSE-KMS, you must provide a customer managed KMS key in the same Region as your general purpose
 bucket. You can set the encryption type for your tables only during table creation. After an AWS
 managed table is created, you can't change its encryption setting. To specify SSE-KMS for your metadata
 tables, you must have certain permissions. For more information, see  [Permissions for SSE-KMS](metadata-tables-permissions.md#metadata-kms-permissions "metadata-tables-permissions.md#metadata-kms-permissions").


The encryption setting for a metadata table takes precedence over the default bucket-level
 encryption setting. If you don't specify encryption for a table, it will inherit the default encryption
 setting from the bucket.


AWS managed table buckets don't count toward your S3 Tables quotas. For more information about
 working with AWS managed table buckets and AWS managed tables, see [Working with AWS managed table
 buckets](s3-tables-aws-managed-buckets.md "s3-tables-aws-managed-buckets.md").


To monitor updates to your metadata table configuration, you can use AWS CloudTrail. For more information,
 see [Amazon S3 bucket-level actions
 that are tracked by CloudTrail logging](cloudtrail-logging-s3-info.md#cloudtrail-bucket-level-tracking "cloudtrail-logging-s3-info.md#cloudtrail-bucket-level-tracking"). 


###### Metadata table maintenance and record expiration


To keep your metadata tables performing at their best, Amazon S3 performs periodic maintenance activities
 on your tables, such as compaction and unreferenced file removal. These maintenance activities help to
 both minimize the cost of storing your metadata tables and optimize query performance. This table
 maintenance happens automatically, requiring no opt-in or ongoing management by you.


###### Note


* You can't control the expiration of journal table or inventory table snapshots. For each
 table, Amazon S3 stores a minimum of 1 snapshot for a maximum of 24 hours.
* To help minimize your costs, you can configure journal table record expiration. By default,
 journal table records don't expire, and journal table records must be retained for a minimum of 7
 days. For more information, see [Expiring journal table records](metadata-tables-expire-journal-table-records.md "metadata-tables-expire-journal-table-records.md").

###### Topics

* [Metadata table limitations and
 restrictions](metadata-tables-restrictions.md "metadata-tables-restrictions.md")
* [S3 Metadata journal tables schema](metadata-tables-schema.md "metadata-tables-schema.md")
* [S3 Metadata live inventory tables schema](metadata-tables-inventory-schema.md "metadata-tables-inventory-schema.md")
* [Configuring metadata tables](metadata-tables-configuring.md "metadata-tables-configuring.md")
* [Querying metadata tables](metadata-tables-querying.md "metadata-tables-querying.md")
* [Troubleshooting S3 Metadata](metadata-tables-troubleshooting.md "metadata-tables-troubleshooting.md")
