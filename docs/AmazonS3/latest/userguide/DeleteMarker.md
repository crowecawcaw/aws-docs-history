# Working with delete markers

A *delete marker* in Amazon S3 is a placeholder (or marker)
 for a versioned object that was specified in a simple `DELETE` request. A simple
 `DELETE` request is a request that doesn't specify a version ID. Because the
 object is in a versioning-enabled bucket, the object is not deleted. But the delete marker
 makes Amazon S3 behave as if the object is deleted. You can use an Amazon S3 API `DELETE`
 call on a delete marker. To do this, you must make the `DELETE` request by using
 an AWS Identity and Access Management (IAM) user or role with the appropriate permissions.

A delete marker has a *key name* (or *key*) and version ID like any other object. However, a delete
 marker differs from other objects in the following ways:


* A delete marker doesn't have data associated with it.
* A delete marker isn't associated with an access control list (ACL) value.
* If you issue a `GET` request for a delete marker, the `GET`
 request doesn't retrieve anything because a delete marker has no data. Specifically,
 when your `GET` request doesn't specify a `versionId`, you get
 a 404 (Not Found) error.
Delete markers accrue a minimal charge for storage in Amazon S3. The storage size of a delete
 marker is equal to the size of the key name of the delete marker. A key name is a sequence
 of Unicode characters. The UTF-8 encoding for the key name adds 1‐4 bytes of storage to
 your bucket for each character in the name. Delete markers are stored in the S3 Standard
 storage class. 

If you want to find out how many delete markers you have and what storage class they're
 stored in, you can use Amazon S3 Storage Lens. For more information, see [Assessing your storage activity and usage with
 Amazon S3 Storage Lens](storage_lens.md "storage_lens.md") and [Amazon S3 Storage Lens metrics glossary](storage_lens_metrics_glossary.md "storage_lens_metrics_glossary.md").

For more information about key names, see [Naming Amazon S3 objects](object-keys.md "object-keys.md"). For information about deleting a delete marker, see [Managing delete markers](ManagingDelMarkers.md "ManagingDelMarkers.md").
 
 

Only Amazon S3 can create a delete marker, and it does so whenever you send a
 `DeleteObject` request on an object in a versioning-enabled or suspended
 bucket. The object specified in the `DELETE` request is not actually deleted.
 Instead, the delete marker becomes the current version of the object. The object's key name
 (or key) becomes the key of the delete marker. 

When you get an object without specifying a `versionId` in your request, if its
 current version is a delete marker, Amazon S3 responds with the following:


* A 404 (Not Found) error
* A response header, `x-amz-delete-marker: true`
When you get an object by specifying a `versionId` in your request, if the
 specified version is a delete marker, Amazon S3 responds with the following:


* A 405 (Method Not Allowed) error
* A response header, `x-amz-delete-marker: true`
* A response header, `Last-Modified: timestamp` (only when using the
 [HeadObject](../API/API_HeadObject.md "../API/API_HeadObject.md") or [GetObject](../API/API_GetObject.md "../API/API_GetObject.md") API
 operations)
The `x-amz-delete-marker: true` response header tells you that the object
 accessed was a delete marker. This response header never returns `false`, because when the value is `false`, the current
 or specified version of the object is not a delete marker.

The `Last-Modified` response header provides the creation time of the delete
 markers.

The following figure shows how a `GetObject` API call on an
 object whose current version is a delete marker responds with a 404 (Not Found) error and
 the response header includes `x-amz-delete-marker: true`.


![Illustration that shows a GetObject call for a delete marker returning a 404 (Not Found) error.](../../../images/AmazonS3/latest/userguide/images/versioning_DELETE_NoObjectFound.png)
If you make a `GetObject` call on an object by specifying a
 `versionId` in your request, and if the specified version is a delete marker,
 Amazon S3 responds with a 405 (Method Not Allowed) error and the response headers include
 `x-amz-delete-marker: true` and `Last-Modified: timestamp`.


![Illustration that shows a GetObject call for a delete marker returning a 405 (Method Not Allowed) error.](../../../images/AmazonS3/latest/userguide/images/versioning_DELETE_NoObjectFound_405.png)
Even if overwritten, delete markers remain in your object versions. The only way to list
 delete markers (and other versions of an object) is by using a [ListObjectVersions](../API/API_ListObjectVersions.md "../API/API_ListObjectVersions.md") request. You can make this request in the
 AWS Management Console by listing your objects in an general purpose bucket and selecting **Show
 versions**. For more information, see [Listing objects in a
 versioning-enabled bucket](list-obj-version-enabled-bucket.md "list-obj-version-enabled-bucket.md").

The following figure shows that a [ListObjectsV2](../API/API_ListObjectsV2.md "../API/API_ListObjectsV2.md") or
 [ListObjects](../API/API_ListObjects.md "../API/API_ListObjects.md") request doesn't return objects whose current
 version is a delete marker.


![Illustration that shows how a ListObjectsV2 or ListObjects call doesn't return any delete markers.](../../../images/AmazonS3/latest/userguide/images/versioning_GETBucketwithDeleteMarkers.png)
