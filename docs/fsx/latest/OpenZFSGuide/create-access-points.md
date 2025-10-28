# Creating access points

The FSx for OpenZFS volume must already exist in your account when creating an S3 access point for your volume.

To create the S3 access point attached to an FSx for OpenZFS volume, you specify the following properties:

- The access point name. For information about access point naming rules, see
  [Access points naming rules](access-point-restrictions-limitations-naming-rules.md#access-points-naming-rules "access-point-restrictions-limitations-naming-rules.md#access-points-naming-rules").
- The file system user identity to use for authorizing file access requests made using the access point.
  Specify the POSIX user ID and group ID, and any secondary group IDs you want to include. For more information, see
  [File system user identity](s3-ap-manage-access-fsx.md#file-system-user-identity "s3-ap-manage-access-fsx.md#file-system-user-identity").
- The access point's network configuration determines whether the access point is accessible from the internet or if access is
  restricted to a specific virtual private cloud (VPC). For more information, see [Creating access points restricted to a virtual private cloud](access-points-vpc.md "access-points-vpc.md").

1. Open the Amazon FSx console at [https://console.aws.amazon.com/fsx/](https://console.aws.amazon.com/fsx/ "https://console.aws.amazon.com/fsx/").
2. In the navigation bar on the top of the page, choose the AWS Region in which you want to create an access point.
   The access point must be created in the same Region as the associated volume.
3. In the left navigation pane, choose **Volumes**.
4. On the **Volumes** page, choose the FSx for OpenZFS volume that you want to attach the access point to.
5. Display the **Create S3 access point** page by choosing **Create S3 access point** from the **Actions** menu.
6. For **Access point name**, enter the name for the access point.
   For more information about guidelines and restrictions for access point names,
   see [Access points naming rules](access-point-restrictions-limitations-naming-rules.md#access-points-naming-rules "access-point-restrictions-limitations-naming-rules.md#access-points-naming-rules").

The **Data source details** are populated with the information of the volume you chose in Step 3. 7. The file system user identity is used by Amazon FSx for authenticating file access requests
that are made using this access point. Be sure that the file system user you specify has the correct permissions on the
FSx for OpenZFS volume.

For **POSIX user ID**, enter the user's POSIX user ID. 8. For **POSIX group ID** enter the user's POSIX group ID. 9. Enter any **Secondary group IDs** for the file system user identity. 10. In the **Network configuration** panel you choose whether the access point is accessible from the Internet, or access is restricted to a specific
virtual private cloud.

For **Network origin**, choose **Internet** to make the access point
accessible from the internet, or choose **Virtual private cloud (VPC)**, and enter the **VPC ID** that you
want to limit access to the access point from.

For more information about network origins for access points, see [Creating access points restricted to a virtual private cloud](access-points-vpc.md "access-points-vpc.md"). 11. (Optional) Under **Access Point Policy - _optional_**, specify an optional access point policy. Be sure to resolve any policy warnings, errors,
and suggestions. For more information about specifying an access point policy, see
[Configuring IAM policies for using access points](../../../AmazonS3/latest/userguide/access-points-policies.md "../../../AmazonS3/latest/userguide/access-points-policies.md")
in the _Amazon Simple Storage Service User Guide_. 12. Choose **Create access point** to review the access point attachment configuration.
The following example command creates an access point named
`my-openzfs-ap` that is attached to the FSx for OpenZFS volume
`fsvol-0123456789abcdef9`
in the account `111122223333`.

```
`$` `aws fsx create-and-attach-s3-access-point --name `my-openzfs-ap` --type OPENZFS --openzfs-configuration \
 VolumeId=`fsvol-0123456789abcdef9`,FileSystemIdentity='{Type=POSIX,PosixUser={Uid=`1234567`,Gid=`1234567`}}' \
 --s3-access-point VpcConfiguration='{VpcId=`vpc-0123467`},Policy=`access-point-policy-json``
```

For a successful request, the system responds by returning the new S3 access point attachment.

```
`$` `{
 {
 "S3AccessPointAttachment": {
 "CreationTime": 1728935791.8,
 "Lifecycle": "CREATING",
 "LifecycleTransitionReason": {
 "Message": "string"
 },
 "Name": "my-openzfs-ap",
 "OpenZFSConfiguration": {
 "VolumeId": "fsvol-0123456789abcdef9",
 "FileSystemIdentity": {
 "Type": "POSIX",
 "PosixUser": {
 "Uid": "1234567",
 "Gid": "1234567",
 "SecondaryGids": ""
 }
 }
 },
 "S3AccessPoint": {
 "ResourceARN": "arn:aws:s3:us-east-1:111122223333:accesspoint/my-openzfs-ap",
 "Alias": "my-openzfs-ap-aqfqprnstn7aefdfbarligizwgyfouse1a-ext-s3alias",
 "VpcConfiguration": {
 "VpcId": "vpc-0123467"
 }
 }
 }
}`
```
