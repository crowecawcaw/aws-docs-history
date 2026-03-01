# Understanding archival storage in S3 Glacier Flexible Retrieval and S3 Glacier Deep Archive

S3 Glacier Flexible Retrieval and S3 Glacier Deep Archive are archival storage classes. This means that when you store an object in these storage classes that object is archived, and cannot be accessed directly. To access an archived object, you submit a restore request for it, and then wait for the service to restore the object. The restore request restores a temporary copy of the object, and that copy is deleted when the duration you specified in the request expires. For more information, see [Working with archived objects](archived-objects.md "archived-objects.md").

The transition of objects to the S3 Glacier Deep Archive
storage class can go only one way.

If you want to change the storage class of an
archived object to another storage class, you must use the restore
operation to make a temporary copy of the object first. Then use the
copy operation to overwrite the object specifying S3 Standard,
S3 Intelligent-Tiering, S3 Standard-IA, S3 One Zone-IA, S3 Glacier Instant Retrieval,
S3 Glacier Flexible Retrieval, or Reduced Redundancy Storage as the storage
class.

###### Note

The Copy operation for restored objects isn't supported in the
Amazon S3 console for objects in the S3 Glacier Flexible Retrieval or
S3 Glacier Deep Archive storage classes. For this type of
Copy operation, use the AWS Command Line Interface (AWS CLI), the AWS SDKs, or the
REST API.

You can restore archived objects in these storage classes with up to 1,000 transactions per second (TPS) of [object restore requests](../API/API_RestoreObject.md "../API/API_RestoreObject.md") per account per AWS Region.

## Cost considerations

If you are planning to archive infrequently accessed data for a period of
months or years, the S3 Glacier Flexible Retrieval and
S3 Glacier Deep Archive storage classes can reduce your storage costs.
However, to ensure that the S3 Glacier Flexible Retrieval or
S3 Glacier Deep Archive storage class is appropriate for you, consider
the following:

- Storage overhead charges –
  Each archived object requires 40 KB of additional metadata. This includes 32 KB of metadata required to identify and retrieve your data, which is charged at the default rate for that storage class. An additional 8 KB data is required to maintain the user-defined name and metadata for archived objects, and is charged at the S3 Standard rate.

If you are archiving small objects, consider these storage charges.
Also consider aggregating many small objects into a smaller number of
large objects to reduce overhead costs.

- Multipart upload pricing –
  Objects in S3-storage-class-glacier; and
  S3 Glacier Deep Archive are billed at S3 Standard storage class rates when you upload them using multipart uploads. For more information, see [Multipart upload and pricing](mpuoverview.md#mpuploadpricing "mpuoverview.md#mpuploadpricing").
- Minimum 30 day storage charges – S3 Glacier Flexible Retrieval and
  S3 Glacier Deep Archive are long-term archival solutions. The
  minimal storage duration period is 90 days for the
  S3 Glacier Flexible Retrieval storage class and 180 days for
  S3 Glacier Deep Archive. Deleting data that is archived to
  these storage classes doesn't incur charges if the objects you delete are archived
  for more than the minimal storage duration period. If you delete or
  overwrite an archived object within the minimal duration period, Amazon S3
  charges for the remainder of that duration.
- Data retrieval charges
  – When you restore an archived objects to S3 Glacier Flexible Retrieval and
  S3 Glacier Deep Archive there are per-request data retrieval charges. These charges vary based on the retrieval tier you choose when you initiate a restore. For pricing information, see [Amazon S3
  pricing](https://aws.amazon.com/s3/pricing/ "https://aws.amazon.com/s3/pricing/").
- S3 Lifecycle
  – When you restore an archived objects to S3 Glacier Flexible Retrieval and
  S3 Glacier Deep Archive there are per-request data retrieval charges. These charges vary based on the retrieval tier you choose when you initiate a restore. For pricing information, see [Amazon S3
  pricing](https://aws.amazon.com/s3/pricing/ "https://aws.amazon.com/s3/pricing/").

## Restoring archived objects

Archived objects aren't accessible in real time. You must first initiate a
restore request and then wait until a temporary copy of the object is available
for the duration that you specify in the request. After you receive a temporary
copy of the restored object, the object's storage class remains
S3 Glacier Flexible Retrieval or S3 Glacier Deep Archive. (A [HeadObject](../API/RESTObjectHEAD.md "../API/RESTObjectHEAD.md") or
[GetObject](../API/RESTObjectGET.md "../API/RESTObjectGET.md")
API operation request will return S3 Glacier Flexible Retrieval or
S3 Glacier Deep Archive as the storage class.)

###### Note

When you restore an archive, you are paying for both the archive
(S3 Glacier Flexible Retrieval or S3 Glacier Deep Archive rate) and a
copy that you restored temporarily (S3 Standard storage rate). For
information about pricing, see [Amazon S3 pricing](https://aws.amazon.com/s3/pricing/ "https://aws.amazon.com/s3/pricing/").

You can restore an object copy programmatically or by using the Amazon S3 console.
Amazon S3 processes only one restore request at a time per object. For more
information, see [Restoring an archived object](restoring-objects.md "restoring-objects.md").
