# Restoring previous versions

You can use versioning to retrieve previous versions of an object. There are two
 approaches to doing so:


* Copy a previous version of the object into the same bucket.


The copied object becomes the current version of that object and all
 object versions are preserved.
* Permanently delete the current version of the object.


When you delete the current object version, you, in effect, turn the
 previous version into the current version of that object.
Because all object versions are preserved, you can make any earlier version the
 current version by copying a specific version of the object into the same bucket. In
 the following figure, the source object (ID = 111111) is copied into the same
 bucket. Amazon S3 supplies a new ID (88778877) and it becomes the current version of the
 object. So, the bucket has both the original object version (111111) and its copy
 (88778877). For more information about getting a previous version and then uploading
 it to make it the current version, see [Retrieving object
 versions from a versioning-enabled bucket](RetrievingObjectVersions.md "RetrievingObjectVersions.md") and [Uploading objects](upload-objects.md "upload-objects.md").


![Illustration that shows copying a specific version of an object into the same bucket to make it the current version.](../../../images/AmazonS3/latest/userguide/images/versioning_COPY2.png)
A subsequent `GET` retrieves version 88778877.

The following figure shows how deleting the current version (121212) of an object
 leaves the previous version (111111) as the current object. For more information
 about deleting an object, see [Deleting a single
 object](delete-objects.md "delete-objects.md").


![Illustration that shows deleting the current version of an object leaves the previous version as the current object.](../../../images/AmazonS3/latest/userguide/images/versioning_COPY_delete2.png)
A subsequent `GET` retrieves version 111111.

###### Note

To restore object versions in batches, you can [use the
 `CopyObject` operation](batch-ops-copy-object.md "batch-ops-copy-object.md"). The `CopyObject` operation copies each
 object that is specified in the manifest. However, be aware that objects aren't
 necessarily copied in the same order as they appear in the manifest. For
 versioned buckets, if preserving current/non-current version order is important,
 you should copy all non-current versions first. Then, after the first job is
 complete, copy the current versions in a subsequent job.


##  To
 restore previous object versions


For more guidance on restoring deleted objects, see [How can I retrieve an Amazon S3 object that was deleted in a versioning-enabled bucket?](https://repost.aws/knowledge-center/s3-undelete-configuration "https://repost.aws/knowledge-center/s3-undelete-configuration") in the AWS re:Post Knowledge Center.


1. Sign in to the AWS Management Console and open the Amazon S3 console at
 [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the **Buckets** list, choose the name of the bucket that
 contains the object.
3. In the **Objects** list, choose the name of the object.
4. Choose **Versions**.


Amazon S3 shows all the versions for the object.
5. Select the check box next to the **Version ID** for the versions
 that you want to retrieve.
6. Choose **Actions**, choose **Download**, and
 save the object.
You also can view, download, and delete object versions in the object overview panel. For
 more information, see [Viewing object properties in the Amazon S3 console](view-object-properties.md "view-object-properties.md").

###### Important

You can undelete an object only if it was deleted as the latest (current) version. You
 can't undelete a previous version of an object that was deleted. For more information,
 see [Retaining multiple versions of objects with S3 Versioning](Versioning.md "Versioning.md").

For information about using other AWS SDKs, see the [AWS Developer Center](https://aws.amazon.com/code/ "https://aws.amazon.com/code/"). 


Python
The following Python code example restores a versioned
 object's previous version by deleting all versions that
 occurred after the specified rollback version.



```
def rollback_object(bucket, object_key, version_id):
    """
    Rolls back an object to an earlier version by deleting all versions that
    occurred after the specified rollback version.

    Usage is shown in the usage_demo_single_object function at the end of this module.

    :param bucket: The bucket that holds the object to roll back.
    :param object_key: The object to roll back.
    :param version_id: The version ID to roll back to.
    """
    # Versions must be sorted by last_modified date because delete markers are
    # at the end of the list even when they are interspersed in time.
    versions = sorted(
        bucket.object_versions.filter(Prefix=object_key),
        key=attrgetter("last_modified"),
        reverse=True,
    )

    logger.debug(
        "Got versions:\n%s",
        "\n".join(
            [
                f"\t{version.version_id}, last modified {version.last_modified}"
                for version in versions
            ]
        ),
    )

    if version_id in [ver.version_id for ver in versions]:
        print(f"Rolling back to version {version_id}")
        for version in versions:
            if version.version_id != version_id:
                version.delete()
                print(f"Deleted version {version.version_id}")
            else:
                break

        print(f"Active version is now {bucket.Object(object_key).version_id}")
    else:
        raise KeyError(
            f"{version_id} was not found in the list of versions for " f"{object_key}."
        )



```
