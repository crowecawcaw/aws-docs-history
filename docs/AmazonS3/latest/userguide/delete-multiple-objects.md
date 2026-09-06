

# Deleting multiple objects
<a name="delete-multiple-objects"></a>

Because all objects in your S3 bucket incur storage costs, you should delete objects that you no longer need. For example, if you are collecting log files, it's a good idea to delete them when they're no longer needed. You can set up a lifecycle rule to automatically delete objects such as log files. For more information, see [Setting an S3 Lifecycle configuration on a bucket](how-to-set-lifecycle-configuration-intro.md).

For information about Amazon S3 features and pricing, see [Amazon S3 pricing](https://aws.amazon.com/s3/pricing).

You can use the Amazon S3 console, AWS SDKs, or the REST API to delete multiple objects simultaneously from an S3 bucket.

## Using the S3 console
<a name="delete-objects-console"></a>

Follow these steps to use the Amazon S3 console to delete multiple objects from a bucket.

**Warning**  
Deleting a specified object cannot be undone.
This action deletes all specified objects. When deleting folders, wait for the delete action to finish before adding new objects to the folder. Otherwise, new objects might be deleted as well.
When deleting objects in a bucket without versioning enabled, including directory buckets, Amazon S3 will permanently delete the objects.
When deleting objects in a bucket with bucket versioning **enabled** or **suspended**, Amazon S3 creates delete markers. For more information, see [Working with delete markers](https://docs.aws.amazon.com/AmazonS3/latest/userguide/DeleteMarker.html).

**To delete objects that have versioning enabled or suspended**
**Note**  
 If the version IDs for the object in a versioning-suspended bucket are marked as `NULL`, S3 permanently deletes the objects since no previous versions exist. However, if a valid version ID is listed for the objects in a versioning-suspended bucket, then S3 creates delete markers for the deleted objects, while retaining the previous versions of the objects. 

1. Sign in to the AWS Management Console and open the Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/).

1. In the left navigation pane, choose **General purpose buckets**.

1. In the bucket list, choose the name of the bucket that you want to delete the objects from.

1. Select the objects and then choose **Delete**.

1. To confirm deletion of the objects list under **Specified objects** in the **Delete objects?** text box, enter **delete**.

**To permanently delete specific object versions in a versioning-enabled bucket**
**Warning**  
When you permanently delete specific object versions in Amazon S3, the deletion can't be undone.

1. Sign in to the AWS Management Console and open the Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/).

1. In the left navigation pane, choose **General purpose buckets**.

1. In the bucket list, choose the name of the bucket that you want to delete the objects from.

1. Select the objects that you want to delete.

1. Choose the **Show versions** toggle.

1. Select the object versions and then choose **Delete**.

1. To confirm permanent deletion of the specific object versions listed under **Specified objects**, in the **Delete objects?** text box, enter **Permanently delete**. Amazon S3 permanently deletes the specific object versions.

**To permanently delete the objects in an Amazon S3 bucket that *don't* have versioning enabled**
**Warning**  
When you permanently delete an object in Amazon S3, the deletion can't be undone. Also, for any buckets without versioning enabled, including directory buckets, deletions are permanent.

1. Sign in to the AWS Management Console and open the Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/).

1. In the left navigation pane, choose **General purpose buckets** or **Directory buckets**.

1. In the bucket list, choose the name of the bucket that you want to delete the objects from.

1. Select the objects and then choose **Delete**.

1. To confirm permanent deletion of the objects listed under **Specified objects**, in the **Delete objects?** text box, enter **permanently delete**.

**Note**  
If you're experiencing any issues with deleting your objects, see [I want to permanently delete versioned objects](troubleshooting-versioning.md#delete-objects-permanent).

## Using the AWS SDKs
<a name="DeletingMultipleObjects"></a>

For examples of how to delete multiple objects with the AWS SDKs, see [Delete multiple objects](https://docs.aws.amazon.com/code-library/latest/ug/s3_example_s3_DeleteObjects_section.html) in the *AWS SDK Code Examples*.

For general information about using different AWS SDKs, see [Developing with Amazon S3 using the AWS SDKs](https://docs.aws.amazon.com/code-library/latest/ug/sdk-general-information-section.html) in the *AWS SDK Code Examples*.