

# Deleting mount targets
<a name="s3-files-mount-targets-deleting"></a>

When you delete a mount target, it breaks any mounts of the file system. This might disrupt compute resources and applications using those mounts. To avoid disruption, stop applications and unmount the file system before you delete the mount target.

You can delete mount targets for a file system by using the AWS Management Console, AWS CLI, or programmatically by using the AWS SDKs.

## Using the S3 console
<a name="s3-files-mount-targets-deleting-console"></a>

Use the Amazon S3 console to delete a mount target for S3 Files.

1. Sign in to the AWS Management Console and open the Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/).

1. In the navigation bar, verify you are in the AWS Region of the mount target that you want to delete.

1. In the left navigation pane, choose **General purpose buckets**.

1. Choose a general purpose bucket your file system is attached to.

1. Select the **File systems** tab and select your desired file system.

1. Select the **Mount targets** tab and select the mount target you wish to delete.

1. Choose **Delete**.

1. In the confirmation window, type **confirm** and choose **Delete**.

## Using the AWS CLI
<a name="s3-files-mount-targets-deleting-cli"></a>

The following `delete-mount-target` command deletes a mount target for S3 Files using the AWS CLI.

```
aws s3files delete-mount-target --region {{aws-region}} --mount-target-id {{mount-target-id}}
```