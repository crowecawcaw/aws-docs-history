# Cataloging and analyzing your data with S3 Inventory

You can use Amazon S3 Inventory to help manage your storage. For example, you can use it to audit
and report on the replication and encryption status of your objects for business, compliance,
and regulatory needs. You can also simplify and speed up business workflows and big data jobs by
using Amazon S3 Inventory, which provides a scheduled alternative to the Amazon S3 synchronous
`List` API operations. Amazon S3 Inventory does not use the `List` API
operations to audit your objects and does not affect the request rate of your bucket.

Amazon S3 Inventory provides comma-separated values (CSV), [Apache optimized row columnar (ORC)](https://orc.apache.org/ "https://orc.apache.org/") or [Apache Parquet](https://parquet.apache.org/ "https://parquet.apache.org/") output files that list
your objects and their corresponding metadata on a daily or weekly basis for an S3 bucket or
objects with a shared prefix (that is, objects that have names that begin with a common string).
If you set up a weekly inventory, a report is generated every Sunday (UTC time zone) after the
initial report. For information about Amazon S3 Inventory pricing, see [Amazon S3 pricing](https://aws.amazon.com/s3/pricing/ "https://aws.amazon.com/s3/pricing/").

You can configure multiple inventory lists for a bucket. When you're configuring an
inventory list, you can specify the following:

- What object metadata to include in the inventory
- Whether to list all object versions or only current versions
- Where to store the inventory list file output
- Whether to generate the inventory on a daily or weekly basis
- Whether to encrypt the inventory list file
  You can query Amazon S3 Inventory with standard SQL queries by using [Amazon Athena](../../../athena/latest/ug/what-is.md "../../../athena/latest/ug/what-is.md"), [Amazon Redshift Spectrum](../../../redshift/latest/dg/c-getting-started-using-spectrum.md "../../../redshift/latest/dg/c-getting-started-using-spectrum.md"), and other
  tools, such as [Presto](https://prestodb.io/ "https://prestodb.io/"), [Apache Hive](https://hive.apache.org/ "https://hive.apache.org/"), and [Apache Spark](https://databricks.com/spark/about/ "https://databricks.com/spark/about/"). For more
  information about using Athena to query your inventory files, see [Querying Amazon S3 Inventory with Amazon Athena](storage-inventory-athena-query.md "storage-inventory-athena-query.md").

###### Note

It might take up to 48 hours for Amazon S3 to deliver the first inventory report.

## Source and destination buckets

The bucket that the inventory lists objects for is called the _source
bucket_. The bucket where the inventory list file is stored is called the
_destination bucket_.

**Source bucket**

The inventory lists the objects that are stored in the source bucket. You can get an
inventory list for an entire bucket, or you can filter the list by object key name
prefix.

The source bucket:

- Contains the objects that are listed in the inventory
- Contains the configuration for the inventory

**Destination bucket**

Amazon S3 Inventory list files are written to the destination bucket. To group all the
inventory list files in a common location in the destination bucket, you can specify a
destination prefix in the inventory configuration.

The destination bucket:

- Contains the inventory file lists.
- Contains the manifest files that list all the inventory list files that are stored in
  the destination bucket. For more information, see [Inventory manifest](storage-inventory-location.md#storage-inventory-location-manifest "storage-inventory-location.md#storage-inventory-location-manifest").
- Must have a bucket policy to give Amazon S3 permission to verify ownership of the bucket
  and permission to write files to the bucket.
- Must be in the same AWS Region as the source bucket.
- Can be the same as the source bucket.
- Can be owned by a different AWS account than the account that owns the source
  bucket.

## Amazon S3 Inventory list

An inventory list file contains a list of the objects in the source bucket and metadata for each object. An inventory list file is stored in the destination bucket with one of the following formats:

- As a CSV file compressed with GZIP
- As an Apache optimized row columnar (ORC) file
  compressed with ZLIB
- As an Apache Parquet file compressed with Snappy

###### Note

Objects in Amazon S3 Inventory reports aren't guaranteed to be sorted in any order.

An inventory list file contains a list of the objects in the source bucket and metadata
for each listed object. These default fields are always included:

- **Bucket name** – The name of the bucket that the
  inventory is for.
- **ETag** – The entity tag (ETag) is a hash of the
  object. The ETag reflects changes only to the contents of an object, not to its metadata.
  The ETag can be an MD5 digest of the object data. Whether it is depends on how the object
  was created and how it is encrypted. For more information, see [Object](../API/API_Object.md "../API/API_Object.md") in the _Amazon Simple Storage Service API Reference_.
- **Key name** – The object key name (or key) that
  uniquely identifies the object in the bucket. When you're using the CSV file format, the
  key name is URL-encoded and must be decoded before you can use it.
- **Last modified date** – The object creation date
  or the last modified date, whichever is the latest.
- **Size** – The object size in bytes, not including
  the size of incomplete multipart uploads, object metadata, and delete markers.
- **Storage class** – The storage class that's used
  for storing the object. Set to
  `STANDARD`, `REDUCED_REDUNDANCY`, `STANDARD_IA`,
  `ONEZONE_IA`, `INTELLIGENT_TIERING`, `GLACIER`, `DEEP_ARCHIVE`, `OUTPOSTS`,
  `GLACIER_IR`, or `SNOW`. For more information, see [Understanding and managing Amazon S3 storage classes](storage-class-intro.md "storage-class-intro.md").

###### Note

S3 Inventory does not support S3 Express One Zone.

You can choose to include the following additional metadata fields in the report:

- **Checksum algorithm** – Indicates the algorithm
  that's used to create the checksum for the object. For more information, see [Using supported checksum algorithms](checking-object-integrity-upload.md#using-additional-checksums "checking-object-integrity-upload.md#using-additional-checksums").
- **Encryption status** – The server-side encryption
  status, depending on what kind of encryption key is used— server-side encryption
  with Amazon S3 managed keys (SSE-S3), server-side encryption with AWS Key Management Service (AWS KMS) keys
  (SSE-KMS), dual-layer server-side encryption with AWS KMS keys (DSSE-KMS), or server-side
  encryption with customer-provided keys (SSE-C). Set to `SSE-S3`,
  `SSE-KMS`, `DSSE-KMS`, `SSE-C`, or
  `NOT-SSE`. A status of `NOT-SSE` means that the object is not
  encrypted with server-side encryption. For more information, see [Protecting data with encryption](UsingEncryption.md "UsingEncryption.md").
- **S3 Intelligent-Tiering access tier** – Access
  tier (frequent or infrequent) of the object if it is stored in the S3 Intelligent-Tiering
  storage class. Set to
  `FREQUENT`, `INFREQUENT`, `ARCHIVE_INSTANT_ACCESS`, `ARCHIVE`, or `DEEP_ARCHIVE`.
  For more information, see [Storage class for automatically optimizing data with changing or unknown access patterns](storage-class-intro.md#sc-dynamic-data-access "storage-class-intro.md#sc-dynamic-data-access").
- **S3 Object Lock retain until date** – The date
  until which the locked object cannot be deleted. For more information, see [Locking objects with Object Lock](object-lock.md "object-lock.md").
- **S3 Object Lock retention mode** – Set to
  `Governance` or `Compliance` for objects that are locked. For more
  information, see [Locking objects with Object Lock](object-lock.md "object-lock.md").
- **S3 Object Lock legal hold status** – Set to
  `On` if a legal hold has been applied to an object. Otherwise, it is set to
  `Off`. For more information, see [Locking objects with Object Lock](object-lock.md "object-lock.md").
- **Version ID** – The object version ID. When you
  enable versioning on a bucket, Amazon S3 assigns a version number to objects that are added to
  the bucket. For more information, see [Retaining multiple versions of objects with S3 Versioning](Versioning.md "Versioning.md"). (This field is not included if the list is configured only for
  the current version of the objects.)
- **IsLatest** – Set to `True` if the
  object is the current version of the object. (This field is not included if the list is
  configured only for the current version of the objects.)
- **Delete marker** – Set to `True` if
  the object is a delete marker. For more information, see [Retaining multiple versions of objects with S3 Versioning](Versioning.md "Versioning.md"). (This field is automatically added to your report if you've
  configured the report to include all versions of your objects).
- **Multipart upload flag** – Set to
  `True` if the object was uploaded as a multipart upload. For more
  information, see [Uploading and copying objects using multipart upload in Amazon S3](mpuoverview.md "mpuoverview.md").
- **Object owner** – The canonical user ID of the owner of the object. For more information, see [Find the canonical user ID for your AWS account](../../../accounts/latest/reference/manage-acct-identifiers.md#FindCanonicalId "../../../accounts/latest/reference/manage-acct-identifiers.md#FindCanonicalId") in the
  _AWS Account Management Reference Guide_.
- **Replication status** – Set to
  `PENDING`, `COMPLETED`, `FAILED`, or
  `REPLICA`. For more information, see [Getting replication status information](replication-status.md "replication-status.md").
- **S3 Bucket Key status** – Set to
  `ENABLED` or `DISABLED`. Indicates whether the object uses an
  S3 Bucket Key for SSE-KMS. For more information, see [Using Amazon S3 Bucket Keys](bucket-key.md "bucket-key.md").
- **Object access control list** – An access control
  list (ACL) for each object that defines which AWS accounts or groups are granted access
  to this object and the type of access that is granted. The Object ACL field is defined in
  JSON format. An S3 Inventory report includes ACLs that are associated with objects in your source bucket, even when ACLs are disabled for the bucket.
  For more information, see [Working with the Object ACL field](objectacl.md "objectacl.md") and [Access control list (ACL) overview](acl-overview.md "acl-overview.md").

###### Note

The Object ACL field is defined in JSON format. An inventory report displays the
value for the Object ACL field as a base64-encoded string.

For example, suppose that you have the following Object ACL field in JSON
format:

```
{
        "version": "2022-11-10",
        "status": "AVAILABLE",
        "grants": [{
            "canonicalId": "example-canonical-user-ID",
            "type": "CanonicalUser",
            "permission": "READ"
        }]
}
```

The Object ACL field is encoded and shown as the following base64-encoded
string:

```
eyJ2ZXJzaW9uIjoiMjAyMi0xMS0xMCIsInN0YXR1cyI6IkFWQUlMQUJMRSIsImdyYW50cyI6W3siY2Fub25pY2FsSWQiOiJleGFtcGxlLWNhbm9uaWNhbC11c2VyLUlEIiwidHlwZSI6IkNhbm9uaWNhbFVzZXIiLCJwZXJtaXNzaW9uIjoiUkVBRCJ9XX0=
```

To get the decoded value in JSON for the Object ACL field, you can query this field
in Amazon Athena. For query examples, see [Querying Amazon S3 Inventory with Amazon Athena](storage-inventory-athena-query.md "storage-inventory-athena-query.md").

- **Lifecycle Expiration Date** – Set to the lifecycle expiration
  timestamp of the object. This field will only be populated, if the object is to be expired by
  an applicable lifecycle rule. In other cases, the field will be empty. For more information,
  see [Expiring objects](lifecycle-expire-general-considerations.md "lifecycle-expire-general-considerations.md").

###### Note

When an object reaches the end of its lifetime based on its lifecycle configuration,
Amazon S3 queues the object for removal and removes it asynchronously. Therefore, there might be
a delay between the expiration date and the date when Amazon S3 removes an object. The inventory
report includes the objects that have expired but haven't been removed yet. For more
information about expiration actions in S3 Lifecycle, see [Expiring objects](lifecycle-expire-general-considerations.md "lifecycle-expire-general-considerations.md").

The following is an example inventory report with additional metadata fields consisting of four records.

```
amzn-s3-demo-bucket1    example-object-1    EXAMPLEDC8l.XJCENlF7LePaNIIvs001    TRUE        1500    2024-08-15T15:28:26.0004    EXAMPLE21e1518b92f3d92773570f600    STANDARD    FALSE    COMPLETED    SSE-KMS    2025-01-25T15:28:26.000Z    COMPLIANCE    Off        ENABLED        eyJ2ZXJzaW9uIjoiMjAyMi0xMS0xMCIsInN0YXR1cyI6IkFWQUlMQUJMRSIsImdyYW50cyI6W3sicGVybWlzc2lvbiI6IkZVTExfQ09OVFJPTCIsInR5cGUiOiJDYW5vbmljYWxVc2VyIiwiY2Fub25pY2FsSWQiOiJFWEFNUExFNzY2ZThmNmIxMTVkOTNkNDFkZjJlYWM0MjBhYTRhNDY1ZDE3N2MxMzk4YmM2YTA4OGM3NmI3MDAwIn1dfQ==    EXAMPLE766e8f6b115d93d41df2eac420aa4a465d177c1398bc6a088c76b7000
amzn-s3-demo-bucket1    example-object-2    EXAMPLEDC8l.XJCENlF7LePaNIIvs002    TRUE        200    2024-08-21T15:28:26.000Z    EXAMPLE21e1518b92f3d92773570f601    INTELLIGENT_TIERING    FALSE    COMPLETED    SSE-KMS    2025-01-25T15:28:26.000Z    COMPLIANCE    Off    INFREQUENT    ENABLED    SHA-256    eyJ2ZXJzaW9uIjoiMjAyMi0xMS0xMCIsInN0YXR1cyI6IkFWQUlMQUJMRSIsImdyYW50cyI6W3sicGVybWlzc2lvbiI6IkZVTExfQ09OVFJPTCIsInR5cGUiOiJDYW5vbmljYWxVc2VyIiwiY2Fub25pY2FsSWQiOiJFWEFNUExFNzY2ZThmNmIxMTVkOTNkNDFkZjJlYWM0MjBhYTRhNDY1ZDE3N2MxMzk4YmM2YTA4OGM3NmI3MDAwIn1dfQ==    EXAMPLE766e8f6b115d93d41df2eac420aa4a465d177c1398bc6a088c76b7001
amzn-s3-demo-bucket1    example-object-3    EXAMPLEDC8l.XJCENlF7LePaNIIvs003    TRUE        12500    2023-01-15T15:28:30.000Z    EXAMPLE21e1518b92f3d92773570f602    STANDARD    FALSE    REPLICA    SSE-KMS    2025-01-25T15:28:26.000Z    GOVERNANCE    On        ENABLED        eyJ2ZXJzaW9uIjoiMjAyMi0xMS0xMCIsInN0YXR1cyI6IkFWQUlMQUJMRSIsImdyYW50cyI6W3sicGVybWlzc2lvbiI6IkZVTExfQ09OVFJPTCIsInR5cGUiOiJDYW5vbmljYWxVc2VyIiwiY2Fub25pY2FsSWQiOiJFWEFNUExFNzY2ZThmNmIxMTVkOTNkNDFkZjJlYWM0MjBhYTRhNDY1ZDE3N2MxMzk4YmM2YTA4OGM3NmI3MDAwIn1dfQ==    EXAMPLE766e8f6b115d93d41df2eac420aa4a465d177c1398bc6a088c76b7002
amzn-s3-demo-bucket1    example-object-4    EXAMPLEDC8l.XJCENlF7LePaNIIvs004    TRUE        100    2021-02-15T15:28:27.000Z    EXAMPLE21e1518b92f3d92773570f603    STANDARD    FALSE    COMPLETED    SSE-KMS    2025-01-25T15:28:26.000Z    COMPLIANCE    Off        ENABLED        eyJ2ZXJzaW9uIjoiMjAyMi0xMS0xMCIsInN0YXR1cyI6IkFWQUlMQUJMRSIsImdyYW50cyI6W3sicGVybWlzc2lvbiI6IkZVTExfQ09OVFJPTCIsInR5cGUiOiJDYW5vbmljYWxVc2VyIiwiY2Fub25pY2FsSWQiOiJFWEFNUExFNzY2ZThmNmIxMTVkOTNkNDFkZjJlYWM0MjBhYTRhNDY1ZDE3N2MxMzk4YmM2YTA4OGM3NmI3MDAwIn1dfQ==    EXAMPLE766e8f6b115d93d41df2eac420aa4a465d177c1398bc6a088c76b7003
```

We recommend that you create a lifecycle policy that deletes old inventory lists. For more
information, see [Managing the lifecycle of objects](object-lifecycle-mgmt.md "object-lifecycle-mgmt.md").

The `s3:PutInventoryConfiguration` permission allows a user to both select all
the metadata fields that are listed earlier for each object when configuring an inventory list
and to specify the destination bucket to store the inventory. A user with read access to
objects in the destination bucket can access all object metadata fields that are available in
the inventory list. To restrict access to an inventory report, see [Grant permissions for S3 Inventory and S3 analytics](example-bucket-policies.md#example-bucket-policies-s3-inventory-1 "example-bucket-policies.md#example-bucket-policies-s3-inventory-1").

### Inventory consistency

All of your objects might not appear in each inventory list. The inventory list provides
eventual consistency for `PUT` requests (of both new objects and overwrites) and
for `DELETE` requests. Each inventory list for a bucket is a snapshot of bucket
items. These lists are eventually consistent (that is, a list might not include recently
added or deleted objects).

To validate the state of an object before you take action on the object, we recommend
that you perform a `HeadObject` REST API request to retrieve metadata for the
object, or to check the object's properties in the Amazon S3 console. You can also check object
metadata with the AWS CLI or the AWS SDKS. For more information, see [`HeadObject`](../API/RESTObjectHEAD.md "../API/RESTObjectHEAD.md") in the
_Amazon Simple Storage Service API Reference_.

For more information about working with Amazon S3 Inventory, see the following topics.

###### Topics

- [Configuring Amazon S3 Inventory](configure-inventory.md "configure-inventory.md")
- [Locating your inventory list](storage-inventory-location.md "storage-inventory-location.md")
- [Setting up Amazon S3 Event Notifications for inventory completion](storage-inventory-notification.md "storage-inventory-notification.md")
- [Querying Amazon S3 Inventory with Amazon Athena](storage-inventory-athena-query.md "storage-inventory-athena-query.md")
- [Converting empty version ID strings in Amazon S3 Inventory reports to null strings](inventory-configure-bops.md "inventory-configure-bops.md")
- [Working with the Object ACL field](objectacl.md "objectacl.md")
