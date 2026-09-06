

# Restoring previous versions
<a name="RestoringPreviousVersions"></a>

You can use versioning to retrieve previous versions of an object. There are two approaches to doing so:
+ Copy a previous version of the object into the same bucket.

  The copied object becomes the current version of that object and all object versions are preserved.
+ Permanently delete the current version of the object.

  When you delete the current object version, you, in effect, turn the previous version into the current version of that object.

Because all object versions are preserved, you can make any earlier version the current version by copying a specific version of the object into the same bucket. In the following figure, the source object (ID = 111111) is copied into the same bucket. Amazon S3 supplies a new ID (88778877) and it becomes the current version of the object. So, the bucket has both the original object version (111111) and its copy (88778877). For more information about getting a previous version and then uploading it to make it the current version, see [Retrieving object versions from a versioning-enabled bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/RetrievingObjectVersions.html) and [Uploading objects](https://docs.aws.amazon.com/AmazonS3/latest/userguide/upload-objects.html).

![Copying a specific version of an object into the same bucket to make it the current version.](http://docs.aws.amazon.com/AmazonS3/latest/userguide/images/versioning_COPY2.png)


A subsequent `GET` retrieves version 88778877.

The following figure shows how deleting the current version (121212) of an object leaves the previous version (111111) as the current object. For more information about deleting an object, see [Deleting a single object](https://docs.aws.amazon.com/AmazonS3/latest/userguide/delete-objects.html).

![Deleting the current version of an object leaves the previous version as the current object.](http://docs.aws.amazon.com/AmazonS3/latest/userguide/images/versioning_COPY_delete2.png)


A subsequent `GET` retrieves version 111111.

**Note**  
To restore object versions in batches, you can [use the `CopyObject` operation](https://docs.aws.amazon.com/AmazonS3/latest/userguide/batch-ops-copy-object.html). The `CopyObject` operation copies each object that is specified in the manifest. However, be aware that objects aren't necessarily copied in the same order as they appear in the manifest. For versioned buckets, if preserving current/non-current version order is important, you should copy all non-current versions first. Then, after the first job is complete, copy the current versions in a subsequent job.

## To restore previous object versions
<a name="restoring-obj-version-version-enabled-bucket-examples"></a>

For more guidance on restoring deleted objects, see [How can I retrieve an Amazon S3 object that was deleted in a versioning-enabled bucket?](https://repost.aws/knowledge-center/s3-undelete-configuration) in the AWS re:Post Knowledge Center.

### Using the S3 console
<a name="retrieving-object-versions"></a>

You can restore a previous version of an object using the Amazon S3 console by deleting the current version. Deleting the current version makes the previous version the new current version.

**To restore a previous version by deleting the current version**

1. Sign in to the AWS Management Console and open the Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/).

1. In the **Buckets** list, choose the name of the bucket that contains the object.

1. In the **Objects** list, choose the name of the object.

1. Choose **Versions**.

   Amazon S3 shows all the versions for the object.

1. Select the check box next to the **Version ID** of the current (latest) version that you want to delete.

1. Choose **Delete**.

1. In the **Delete objects** dialog box, enter **permanently delete**, and then choose **Delete objects**.

   After you delete the current version, the previous version becomes the current version.

**To download a previous version**

1. Sign in to the AWS Management Console and open the Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/).

1. In the **Buckets** list, choose the name of the bucket that contains the object.

1. In the **Objects** list, choose the name of the object.

1. Choose **Versions**.

   Amazon S3 shows all the versions for the object.

1. Select the check box next to the **Version ID** for the versions that you want to retrieve.

1. Choose **Actions**, choose **Download**, and save the object.

You also can view, download, and delete object versions in the object overview panel. For more information, see [Viewing object properties in the Amazon S3 console](view-object-properties.md).

**Note**  
To copy a previous version in place (making it the new current version), use the AWS CLI or AWS SDKs — this approach isn't available in the Amazon S3 console. For an example, see the AWS CLI tab.

**Important**  
You can undelete an object only if it was deleted as the latest (current) version. You can't undelete a previous version of an object that was deleted. For more information, see [Retaining multiple versions of objects with S3 Versioning](Versioning.md).

### Using the AWS CLI
<a name="restoring-obj-version-cli"></a>

To restore a previous version by copying it in place, use the `copy-object` command. For the `--copy-source` parameter, specify the version ID of the previous version that you want to restore:

```
aws s3api copy-object \
    --bucket {{amzn-s3-demo-bucket}} \
    --key {{my-object.jpg}} \
    --copy-source {{amzn-s3-demo-bucket}}/{{my-object.jpg}}?versionId={{previous-version-id}}
```

This creates a new current version of the object with the content from the specified previous version. Amazon S3 preserves all existing versions.

### Using the AWS SDKs
<a name="restoring-obj-version-version-enabled-bucket-sdks"></a>

For information about using other AWS SDKs, see the [AWS Developer Center](https://aws.amazon.com/code/). 

------
#### [ Python ]

The following Python code example restores a versioned object's previous version by deleting all versions that occurred after the specified rollback version.

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

------