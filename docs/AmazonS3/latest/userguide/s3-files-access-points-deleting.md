# Deleting access points for an S3 file system

When deleting an access point, make sure no applications are actively using the access
point before deletion to avoid service disruption. Once deleted, the access point and its
configuration are permanently removed.

This section explains how to use the Amazon S3 console to delete an access point
for S3 Files.

1. Sign in to the AWS Management Console and open the Amazon S3
   console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the navigation bar, verify you are in the
   AWS Region of the file system which has the access point that you want to
   delete.
3. In the left navigation pane, choose **General
   purpose buckets**.
4. Choose a general purpose bucket your file system is attached
   to.
5. Select the **File systems** tab and
   select the file system you wish to use.
6. Select the **Access points** tab and
   select the access point you wish to delete.
7. Choose **Delete**.
8. In the confirmation window, type `confirm` and
   choose **Delete**.
   The following `delete-access-point` example command shows how you can
   use the AWS CLI to delete an access point for S3 Files.

```
aws s3files delete-access-point --access-point-id `access-point-id`
```
