

# Deleting file systems
<a name="s3-files-file-systems-deleting"></a>

When you delete a file system, the file system, its data, and its configuration are permanently removed. Make sure no applications are actively using the file system before deletion to avoid service disruption. Before deletion, you must delete all mount targets and access points associated with the file system first. For more information, see [Deleting mount targets](s3-files-mount-targets-deleting.md) and [Deleting access points for an S3 file system](s3-files-access-points-deleting.md).

When you delete a file system, S3 Files checks whether all changes in your file system have been synchronized with your linked S3 bucket. If there are changes that have not yet been synchronized, S3 Files returns an error and the deletion does not proceed. This ensures that all your data is safely stored in your S3 bucket before the file system is deleted. If you want to proceed with deletion and accept that any unsynchronized changes will be lost, you can retry the delete request with the 'force delete' option. In the AWS CLI, add the `--ForceDelete` flag to your delete API call. On the AWS Console, choose **Force** button in the error message that appears when you delete a file system while unsynced changes are present.

## Using the S3 console
<a name="s3-files-file-systems-deleting-console"></a>

This section explains how to use the Amazon S3 console to delete a file system for S3 Files.
+ Open the Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/).
+ In the navigation bar, verify you are in the AWS Region of the file system that you want to delete.
+ In the left navigation pane, choose **General purpose buckets**.
+ Choose a general purpose bucket your file system is attached to.
+ Select the **File systems** tab and select the file system you wish to delete.
+ Choose **Delete**.
+ In the confirmation window, type `confirm`.

## Using the AWS CLI
<a name="s3-files-file-systems-deleting-cli"></a>

The following `delete-file-system` example command shows how you can use the AWS CLI to delete a file system for S3 Files.

```
aws s3files delete-file-system --file-system-id {{file-system-id}}
```