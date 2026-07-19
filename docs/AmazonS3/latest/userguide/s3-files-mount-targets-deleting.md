# Deleting mount targets

When you delete a mount target, the operation forcibly breaks any mounts of the file
system, which might disrupt compute resources and applications using those mounts. To avoid
application disruption, stop applications and unmount the file system before deleting the
mount target.

You can delete mount targets for a file system by using the AWS Management Console,
AWS CLI, or programmatically by using the AWS SDKs.

This section explains how to use the Amazon S3 console to delete a mount target
for S3 Files.

1. Sign in to the AWS Management Console and open the Amazon S3
   console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the navigation bar, verify you are in the
   AWS Region of the mount target that you want to
   delete.
3. In the left navigation pane, choose **General
   purpose buckets**.
4. Choose a general purpose bucket your file system is attached
   to.
5. Select the **File systems** tab and
   select your desired file system.
6. Select the **Mount targets** tab and
   select the mount target you wish to delete.
7. Choose **Delete**.
8. In the confirmation window, type `confirm` and
   choose **Delete**.
   The following `delete-mount-target` example command shows how you can
   use the AWS CLI to delete a mount target for S3 Files.

```
aws s3files delete-mount-target --region `aws-region` --mount-target-id `mount-target-id`
```
