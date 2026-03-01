# How S3 Intelligent-Tiering works

The Amazon S3 Intelligent-Tiering storage class automatically stores objects in three
access tiers. One tier is optimized for frequent access, one lower-cost tier is optimized
for infrequent access, and another very low-cost tier is optimized for rarely accessed data.
For a low monthly object monitoring and automation charge, S3 Intelligent-Tiering monitors
access patterns and automatically moves objects to the Infrequent Access tier when they haven't
been accessed for 30 consecutive days. After 90 days of no access, the objects are moved to
the Archive Instant Access tier without performance impact or operational overhead.

To get the lowest storage cost for data that can be accessed in minutes to hours, activate
archiving capabilities to add two additional access tiers. You can tier down objects to the
Archive Access tier, the Deep Archive Access tier, or both. With Archive Access,
S3 Intelligent-Tiering moves objects that have not been accessed for a minimum of 90
consecutive days to the Archive Access tier. With Deep Archive Access, S3 Intelligent-Tiering
moves objects to the Deep Archive Access tier after a minimum of 180 consecutive days of no
access. For both tiers, you can configure the number of days of no access based on your
needs.

The following actions constitute access that prevents tiering your objects down to the
Archive Access tier or the Deep Archive Access tier:

- Downloading or copying an object through the Amazon S3 console.
- Invoking [CopyObject](../API/API_CopyObject.md "../API/API_CopyObject.md"), [UploadPartCopy](../API/API_UploadPartCopy.md "../API/API_UploadPartCopy.md"), or replicating objects with
  S3 Batch Replication. In these cases, the source objects of the copy or
  replication operations are tiered up.
- Invoking [GetObject](../API/API_GetObject.md "../API/API_GetObject.md"), [PutObject](../API/API_PutObject.md "../API/API_PutObject.md"),
  [RestoreObject](../API/API_RestoreObject.md "../API/API_RestoreObject.md"), [CompleteMultipartUpload](../API/API_CompleteMultipartUpload.md "../API/API_CompleteMultipartUpload.md"),
  or [SelectObjectContent](../API/API_SelectObjectContent.md "../API/API_SelectObjectContent.md").
  For example, if your objects are accessed through `SelectObjectContent` before
  your specified number of days of no access (for example, 180 days), that action resets the
  timer. Your objects won't move to the Archive Access tier or the Deep Archive Access tier
  until the time after the last `SelectObjectContent` request reaches your
  specified number of days.

If an object in the Infrequent Access tier or Archive Instant Access tier is accessed later, it is
automatically moved back to the Frequent Access tier.

The following actions constitute access that automatically moves objects from the
Infrequent Access tier or the Archive Instant Access tier back to the Frequent Access tier:

- Downloading or copying an object through the Amazon S3 console.
- Invoking [CopyObject](../API/API_CopyObject.md "../API/API_CopyObject.md"), [UploadPartCopy](../API/API_UploadPartCopy.md "../API/API_UploadPartCopy.md"), or replicating objects with
  Batch Replication. In these cases, the source objects of the copy or replication
  operations are tiered up.
- Invoking [GetObject](../API/API_GetObject.md "../API/API_GetObject.md"), [PutObject](../API/API_PutObject.md "../API/API_PutObject.md"),
  [RestoreObject](../API/API_RestoreObject.md "../API/API_RestoreObject.md"), or [CompleteMultipartUpload](../API/API_CompleteMultipartUpload.md "../API/API_CompleteMultipartUpload.md").
  Other actions **don't** constitute access that automatically
  moves objects from the Infrequent Access tier or the Archive Instant Access tier back to the
  Frequent Access tier. The following is a sample, not a definitive list, of such actions:

- Invoking [HeadObject](../API/API_HeadObject.md "../API/API_HeadObject.md"), [GetObjectTagging](../API/API_GetObjectTagging.md "../API/API_GetObjectTagging.md"), [PutObjectTagging](../API/API_PutObjectTagging.md "../API/API_PutObjectTagging.md"), [ListObjects](../API/API_ListObjects.md "../API/API_ListObjects.md"), [ListObjectsV2](../API/API_ListObjectsV2.md "../API/API_ListObjectsV2.md"), [ListObjectVersions](../API/API_ListObjectVersions.md "../API/API_ListObjectVersions.md"), and
  [UpdateObjectEncryption](../API/API_UpdateObjectEncryption.md "../API/API_UpdateObjectEncryption.md").
- Invoking [SelectObjectContent](../API/API_SelectObjectContent.md "../API/API_SelectObjectContent.md") doesn't constitute access that
  tiers objects up to a Frequent Access tier. In addition, it doesn't prevent tiering
  objects down from the Frequent Access tier to the Infrequent Access tier, and then to the
  Archive Instant Access tier.
  You can use S3 Intelligent-Tiering as your default storage class for newly created data by specifying
  `INTELLIGENT-TIERING` in the [x-amz-storage-class request header](../API/API_PutObject.md#AmazonS3-PutObject-request-header-StorageClass "../API/API_PutObject.md#AmazonS3-PutObject-request-header-StorageClass") when calling the `PutObject`,
  `CopyObject`, or `CreateMultipartUpload` operations. S3 Intelligent-Tiering is
  designed for 99.9% availability and 99.999999999% durability.

###### Note

If the size of an object is less than 128 KB, it is not monitored and is not eligible
for automatic tiering. Smaller objects are always stored in the Frequent Access tier.

## S3 Intelligent-Tiering access tiers

The following section explains the different automatic and optional access tiers. When
objects move between access tiers, the storage class remains the same
(S3 Intelligent-Tiering).

_Frequent Access tier (automatic)_

This is the default access tier that any object created or transitioned to
S3 Intelligent-Tiering begins its lifecycle in. An object remains in this
tier as long as it is being accessed. The Frequent Access tier provides low
latency and high-throughput performance.

_Infrequent Access tier (automatic)_

If an object is not accessed for 30 consecutive days, the object moves to
the Infrequent Access tier. The Infrequent Access tier provides low latency and
high-throughput performance.

_Archive Instant Access tier (automatic)_

If an object is not accessed for 90 consecutive days, the object moves to
the Archive Instant Access tier. The Archive Instant Access tier provides low latency and
high-throughput performance.

_Archive Access tier (optional)_

S3 Intelligent-Tiering provides you with the option to activate the
Archive Access tier for data that can be accessed asynchronously. After
activation, the Archive Access tier automatically archives objects that
have not been accessed for a minimum of 90 consecutive days. You can extend
the last access time for archiving to a maximum of 730 days. The
Archive Access tier has the same performance as the [S3 Glacier Flexible Retrieval](storage-class-intro.md#sc-glacier "storage-class-intro.md#sc-glacier") storage class.

Standard retrieval times for this access tier can range from 3–5
hours. If you initiate your restore request by using S3 Batch Operations, your
restore starts within minutes. For more information about retrieval options
and times, see [Restoring objects from the S3 Intelligent-Tiering Archive Access and Deep Archive Access tiers](intelligent-tiering-managing.md#restore-data-from-int-tier-archive "intelligent-tiering-managing.md#restore-data-from-int-tier-archive").

###### Note

Only activate the Archive Access tier for 90 days if you want to
bypass the Archive Instant Access tier. The Archive Access tier delivers slightly
lower storage costs, with minute-to-hour retrieval times. The
Archive Instant Access tier delivers millisecond access and high-throughput
performance.

_Deep Archive Access tier (optional)_

S3 Intelligent-Tiering provides you with the option to activate the
Deep Archive Access tier for data that can be accessed asynchronously. After
activation, the Deep Archive Access tier automatically archives objects that
have not been accessed for a minimum of 180 consecutive days. You can extend
the last access time for archiving to a maximum of 730 days. The
Deep Archive Access tier has the same performance as the [S3 Glacier Deep Archive](storage-class-intro.md#sc-glacier "storage-class-intro.md#sc-glacier") storage class.

Standard retrieval of objects in this access tier occurs within 12 hours.
If you initiate your restore request by using S3 Batch Operations, your restore
starts within 9 hours. For more information about retrieval options and
times, see [Restoring objects from the S3 Intelligent-Tiering Archive Access and Deep Archive Access tiers](intelligent-tiering-managing.md#restore-data-from-int-tier-archive "intelligent-tiering-managing.md#restore-data-from-int-tier-archive").

###### Note

Activate the Archive Access and Deep Archive Access tiers only if your objects can
be accessed asynchronously by your application. If the object that you are
retrieving is stored in the Archive Access or Deep Archive Access tiers, you must
first restore the object by using the `RestoreObject` operation.

You can restore archived objects with up to 1,000 transactions per second (TPS) of object restore requests per account per AWS Region from S3 Intelligent-Tiering Archive Access, and S3 Intelligent-Tiering Deep Archive Access.
