# Deleting object versions from a

versioning-enabled bucket

You can delete object versions from Amazon S3 buckets whenever you want. You can also
define lifecycle configuration rules for objects that have a well-defined lifecycle to
request Amazon S3 to expire current object versions or permanently remove noncurrent object
versions. When your bucket has versioning enabled or the versioning is suspended, the lifecycle
configuration actions work as follows:

- The `Expiration` action applies to the current object version.
  Instead of deleting the current object version, Amazon S3 retains the current version
  as a noncurrent version by adding a _delete
  marker_, which then becomes the current version.
- The `NoncurrentVersionExpiration` action applies to noncurrent
  object versions, and Amazon S3 permanently removes these object versions. You cannot
  recover permanently removed objects.
  For more information about S3 Lifecycle, see [Managing the lifecycle of objects](object-lifecycle-mgmt.md "object-lifecycle-mgmt.md") and [Examples of S3 Lifecycle
  configurations](lifecycle-configuration-examples.md "lifecycle-configuration-examples.md").

To see how many current and noncurrent object versions that your buckets have, you can use
Amazon S3 Storage Lens metrics. S3 Storage Lens is a cloud-storage analytics feature that you can use to gain organization-wide
visibility into object-storage usage and activity. For more information, see [Using S3 Storage Lens to optimize your storage costs](storage-lens-optimize-storage.md "storage-lens-optimize-storage.md"). For a complete list of
metrics, see [S3 Storage Lens metrics glossary](storage_lens_metrics_glossary.md "storage_lens_metrics_glossary.md").

###### Note

Normal Amazon S3 rates apply for every version of an object that is stored and transferred,
including noncurrent object versions. For more information, see [Amazon S3 pricing](https://aws.amazon.com/s3/pricing/ "https://aws.amazon.com/s3/pricing/").

## Delete request use cases

A `DELETE` request has the following use cases:

- When versioning is enabled, a simple `DELETE` cannot
  permanently delete an object. (A simple `DELETE` request is a request that doesn't specify a version ID.) Instead, Amazon S3 inserts a delete marker in the
  bucket, and that marker becomes the current version of the object with a new
  ID.

When you try to `GET` an object whose current version is a
delete marker, Amazon S3 behaves as though the object has been deleted (even
though it has not been erased) and returns a 404 error. For more
information, see [Working with delete markers](DeleteMarker.md "DeleteMarker.md").

The following figure shows that a simple `DELETE` does not
actually remove the specified object. Instead, Amazon S3 inserts a delete
marker.

![Illustration that shows a delete marker insertion.](images/versioning_DELETE_versioningEnabled.png)

- To delete versioned objects permanently, you must use `DELETE Object
versionId`.

The following figure shows that deleting a specified object version
permanently removes that object.

![Diagram that shows how DELETE Object versionId permanently deletes a specific object version.](images/versioning_DELETE_versioningEnabled2.png)

## To delete object versions

You can delete object versions in Amazon S3 using the console, AWS SDKs, the REST
API, or the AWS Command Line Interface.

1. Sign in to the AWS Management Console and open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the **Buckets** list, choose the name of the bucket that
   contains the object.
3. In the **Objects** list, choose the name of the object.
4. Choose **Versions**.

Amazon S3 shows all the versions for the object. 5. Select the check box next to the **Version ID** for the versions
that you want to permanently delete. 6. Choose **Delete**. 7. In **Permanently delete objects?**, enter `permanently
 delete`.

###### Warning

When you permanently delete an object version, the action cannot be
undone. 8. Choose **Delete objects**.

Amazon S3 deletes the object version.
For examples of deleting objects using the AWS SDKs for Java, .NET, and
PHP, see [Deleting Amazon S3 objects](DeletingObjects.md "DeletingObjects.md").
The examples for deleting objects in nonversioned and versioning-enabled
buckets are the same. However, for versioning-enabled buckets, Amazon S3 assigns
a version number. Otherwise, the version number is null.

For information about using other AWS SDKs, see the [AWS Developer Center](https://aws.amazon.com/code/ "https://aws.amazon.com/code/").

Python
The following Python code example permanently deletes a
versioned object by deleting all of its versions.

```
def permanently_delete_object(bucket, object_key):
    """
    Permanently deletes a versioned object by deleting all of its versions.

    Usage is shown in the usage_demo_single_object function at the end of this module.

    :param bucket: The bucket that contains the object.
    :param object_key: The object to delete.
    """
    try:
        bucket.object_versions.filter(Prefix=object_key).delete()
        logger.info("Permanently deleted all versions of object %s.", object_key)
    except ClientError:
        logger.exception("Couldn't delete all versions of %s.", object_key)
        raise



```

###### To delete a specific version of an object

- In a `DELETE`, specify a version ID.

###### Example — Deleting a specific version

The following example deletes version `UIORUnfnd89493jJFJ`
of `photo.gif`.

```
DELETE /photo.gif?versionId=UIORUnfnd89493jJFJ HTTP/1.1
Host: bucket.s3.amazonaws.com
Date: Wed, 12 Oct 2009 17:50:00 GMT
Authorization: AWS AKIAIOSFODNN7EXAMPLE:xQE0diMbLRepdf3YB+FIEXAMPLE=
Content-Type: text/plain
Content-Length: 0
```

The following command deletes an object named test.txt from a bucket named
`amzn-s3-demo-bucket1`. To remove a specific version of an
object, you must be the bucket owner and you must use the version Id
subresource.

```
aws s3api delete-object --bucket `amzn-s3-demo-bucket1` --key test.txt --version-id `versionID`
```

For more information about `delete-object` see [delete-object](../../../cli/latest/reference/s3api/delete-object.md "../../../cli/latest/reference/s3api/delete-object.md") in the
_AWS CLI Command Reference_.

For more information about deleting object versions, see the following
topics:

- [Working with delete markers](DeleteMarker.md "DeleteMarker.md")
- [Removing delete markers to make an older version
  current](ManagingDelMarkers.md#RemDelMarker "ManagingDelMarkers.md#RemDelMarker")
- [Deleting an object from an MFA delete-enabled
  bucket](UsingMFADelete.md "UsingMFADelete.md")
