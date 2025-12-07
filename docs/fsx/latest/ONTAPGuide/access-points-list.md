# Listing S3 access point attachments

This section explains how to list S3 access point using the AWS Management Console, AWS Command Line Interface, or REST API.

1. Open the Amazon FSx console at [https://console.aws.amazon.com/fsx/](https://console.aws.amazon.com/fsx/ "https://console.aws.amazon.com/fsx/").
2. In the navigation pane on the left side of the console, choose
   **Volumes**.
3. On the **Volumes** page, choose the **ONTAP** volume that you want to view
   the access point attachments for.
4. On the Volume details page, choose **S3** to view a list of
   all the S3 access points attached to the volume.
   The following
   [`describe-s3-access-point-attachments`](../APIReference/API_DescribeS3AccessPointAttachments.md "../APIReference/API_DescribeS3AccessPointAttachments.md")
   example command shows how you can use the AWS CLI to list S3 access point attachments.

The following command lists all the S3 access points attached to volumes on the FSx for ONTAP file system fs-0abcdef123456789.

```
aws fsx describe-s3-access-point-attachments --filter {[Name: file-system-id, Values:{[fs-0abcdef123456789]}}
```

The following command lists S3 access points attached to an FSx for ONTAP volume vol-9abcdef123456789].

```
aws fsx describe-s3-access-point-attachments --filter {[Name: volume-id, Values:{[vol-9abcdef123456789]}}
```

For more information and examples, see [list-access-points](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/list-access-points.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/list-access-points.html") in the
_AWS CLI Command Reference_.
