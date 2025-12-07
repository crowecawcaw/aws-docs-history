# Deleting an S3 access point attachment

This section explains how to delete S3 access points using the AWS Management Console, AWS Command Line Interface, or REST API.

The `fsx:DetatchAndDeleteS3AccessPoint` and `s3control:DeleteAccessPoint` permissions are
required to delete an S3 access point attachment.

1. Open the Amazon FSx console at [https://console.aws.amazon.com/fsx/](https://console.aws.amazon.com/fsx/ "https://console.aws.amazon.com/fsx/").
2. Navigate to the volume that the S3 access point attachment that you want to delete is attached to.
3. Choose **S3** to display the list of S3 access points attached to the volume.
4. Select the S3 access point attachment that you want to delete.
5. Choose **Delete**.
6. Confirm that you want to delete the S3 access point, and choose **Delete**.

- To delete an S3 access point attachments, use the [detach-and-delete-s3-access-point](../../../cli/latest/reference/fsx/detach-and-delete-s3-access-point.md "../../../cli/latest/reference/fsx/detach-and-delete-s3-access-point.md") CLI command (or the equivalent
  [DetachAndDeleteS3AccessPoint](../APIReference/API_DetachAndDeleteS3AccessPoint.md "../APIReference/API_DetachAndDeleteS3AccessPoint.md") API operation), as shown in the
  following example. Use the `--name` property to specify the
  name of the S3 access point attachment that you want to delete.

```
`aws fsx detach-and-delete-s3-access-point \
 --region `us-east-1` \
 --name `my-ontap-ap``
```
