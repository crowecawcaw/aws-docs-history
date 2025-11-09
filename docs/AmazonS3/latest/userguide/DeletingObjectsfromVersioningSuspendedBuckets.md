# Deleting objects from

versioning-suspended buckets

You can delete objects from versioning-suspended buckets to remove an object with a
null version ID.

If versioning is suspended for a bucket, a `DELETE` request:

- Can only remove an object whose version ID is `null`.
- Doesn't remove anything if there isn't a null version of the object in the
  bucket.
- Inserts a delete marker into the bucket.
  If bucket versioning is suspended, the operation removes the object that has a null
  `versionId`. If a version ID exists, Amazon S3 inserts a delete marker that
  becomes the current version of the object. The following figure shows how a simple
  `DELETE` removes a null version and Amazon S3 inserts a delete marker in its
  place instead with a `null` version ID.

![Illustration that shows a simple delete to remove an object with a NULL version ID.](images/versioning_DELETE_versioningSuspended.png)
To permanently delete an object that has a `versionId`, you must include
the object’s `versionId` in the request. Since a delete marker doesn't
contain any content, you'll lose the content for the `null` version when a
delete marker replaces it.

The following figure shows a bucket that doesn't have a null version. In this case,
the `DELETE` removes nothing. Instead, Amazon S3 just inserts a delete
marker.

![Illustration that shows a delete marker insertion.](images/versioning_DELETE_versioningSuspendedNoNull.png)
Even in a versioning-suspended bucket, the bucket owner can permanently delete a
specified version by including the version ID in the `DELETE` request, unless
permissions for the `DELETE` request have been explicitly denied. For
example, to deny deletion of any objects that have a `null` version ID, you must
explicitly deny the `s3:DeleteObject` and `s3:DeleteObjectVersions` permissions.

The following figure shows that deleting a specified object version permanently removes that
version of the object. Only the bucket owner can delete a specified object
version.

![Illustration that shows a permanent object deletion using a specified version ID.](images/versioning_DELETE_versioningEnabled2.png)
