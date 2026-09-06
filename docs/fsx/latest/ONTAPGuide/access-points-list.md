

# Listing S3 access point attachments
<a name="access-points-list"></a>

This section explains how to list S3 access point using the AWS Management Console, AWS Command Line Interface, or REST API.

## To list all the S3 access points attached to an FSx for ONTAP volume (Amazon FSx console)
<a name="access-points-list-console"></a>

1. Open the Amazon FSx console at [https://console.aws.amazon.com/fsx/](https://console.aws.amazon.com/fsx/).

1. In the navigation pane on the left side of the console, choose **Volumes**.

1. On the **Volumes** page, choose the **ONTAP** volume that you want to view the access point attachments for.

1. On the Volume details page, choose **S3** to view a list of all the S3 access points attached to the volume.

## To list all the S3 access points attached to an FSx for ONTAP volume (AWS CLI)
<a name="access-points-list-cli"></a>

The following [`describe-s3-access-point-attachments`](https://docs.aws.amazon.com/fsx/latest/APIReference/API_DescribeS3AccessPointAttachments.html) example command shows how you can use the AWS CLI to list S3 access point attachments.

The following command lists all the S3 access points attached to volumes on the FSx for ONTAP file system fs-0abcdef123456789.

```
aws fsx describe-s3-access-point-attachments --filter {[Name: file-system-id, Values:{[fs-0abcdef123456789]}} 
```

The following command lists S3 access points attached to an FSx for ONTAP volume vol-9abcdef123456789].

```
aws fsx describe-s3-access-point-attachments --filter {[Name: volume-id, Values:{[vol-9abcdef123456789]}} 
```

For more information and examples, see [list-access-points](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/list-access-points.html) in the *AWS CLI Command Reference*.