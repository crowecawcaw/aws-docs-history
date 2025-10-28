# Copy a custom image in WorkSpaces Personal

You can copy a custom WorkSpaces image within or across AWS Regions. Copying an
image results in the creation of an identical image with its own unique
identifier.

You can copy a Bring Your Own License (BYOL) image to another Region as long as the
destination Region is enabled for BYOL. Ensure that BYOL is enabled for all accounts and
Regions involved.

###### Note

In the China (Ningxia) Region, you can copy images only within the same
Region.

In the AWS GovCloud (US) Regions, to copy images to and from other AWS Regions,
contact AWS Support.

In Opt-in Regions, to copy images to other Regions, contact AWS Support. For
more information about Opt-in Regions, see [Available Regions](../../../AWSEC2/latest/UserGuide/using-regions-availability-zones.md#concepts-available-regions "../../../AWSEC2/latest/UserGuide/using-regions-availability-zones.md#concepts-available-regions").

You can also copy an image that has been shared with you by another AWS account. For
more information about shared images, see [Share or unshare a custom image in WorkSpaces Personal](share-custom-image.md "share-custom-image.md").

There are no additional charges for copying an image within or across Regions.
However, the quota for the number of images in the destination Region applies. For more
information about Amazon WorkSpaces quotas, see [Amazon WorkSpaces quotas](workspaces-limits.md "workspaces-limits.md").

###### IAM Permissions to copy an image

If you use an IAM user to copy an image, the user must have permissions for
`workspaces:DescribeWorkspaceImages` and
`workspaces:CopyWorkspaceImage`.

The following example policy allows the user to copy the specified image to the
specified account in the specified Region.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "workspaces:DescribeWorkspaceImages",
 "workspaces:CopyWorkspaceImage"
 ],
 "Resource": [
 "arn:aws:workspaces:`us-east-1`:`123456789012`:workspaceimage/`wsi-a1bcd2efg`"
 ]
 }
 ]
}`

```

###### Important

If you are creating an IAM policy for copying shared images for accounts that
don't own the images, you cannot specify an account ID in the ARN. Instead, you must
use `*` for the account ID, as shown in the following example
policy.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "workspaces:DescribeWorkspaceImages",
 "workspaces:CopyWorkspaceImage"
 ],
 "Resource": [
 "arn:aws:workspaces:`us-east-1`:*:workspaceimage/`wsi-a1bcd2efg`"
 ]
 }
 ]
}`

```

You can specify an account ID in the ARN only when that account owns the images to
be copied.

For more information about working with IAM, see [Identity and access management for WorkSpaces](workspaces-access-control.md "workspaces-access-control.md").

###### Bulk copy images

You can copy images one by one using the console. To bulk copy images, use the
**CopyWorkspaceImage** API operation or the
**copy-workspace-image** command in the AWS Command Line Interface (AWS CLI). For
more information, see [CopyWorkspaceImage](../api/API_CopyWorkspaceImage.md "../api/API_CopyWorkspaceImage.md") in the _Amazon WorkSpaces API Reference_ or see
[copy-workspace-image](../../../cli/latest/reference/workspaces/copy-workspace-image.md "../../../cli/latest/reference/workspaces/copy-workspace-image.md") in the _AWS CLI Command Reference_.

###### Important

Before copying a shared image, be sure to verify that it has been shared from the
correct AWS account. To determine if an image has been shared and to see the AWS
account ID that owns an image, use the [DescribeWorkSpaceImages](../api/API_DescribeWorkspaceImages.md "../api/API_DescribeWorkspaceImages.md") and [DescribeWorkspaceImagePermissions](../api/API_DescribeWorkspaceImagePermissions.md "../api/API_DescribeWorkspaceImagePermissions.md") API operations or the [describe-workspace-images](../../../cli/latest/reference/workspaces/describe-workspace-images.md "../../../cli/latest/reference/workspaces/describe-workspace-images.md") and [describe-workspace-image-permissions](../../../cli/latest/reference/workspaces/describe-workspace-image-permissions.md "../../../cli/latest/reference/workspaces/describe-workspace-image-permissions.md") commands in the AWS CLI.

###### To copy an image using the console

1. Open the WorkSpaces console at [https://console.aws.amazon.com/workspaces/v2/home](https://console.aws.amazon.com/workspaces/v2/home "https://console.aws.amazon.com/workspaces/v2/home").
2. In the navigation pane, choose **Images**.
3. Select the image and choose **Actions**, **Copy
   image**.
4. For **Select destination**, select the AWS Region that you
   want to copy the image to.
5. For **Name of the copy**, enter the new name for the copied
   image, and for **Description**, enter a description for the
   copied image.
6. (Optional) Under **Tags**, enter tags for the copied image.
   For more information, see [Tag resources in WorkSpaces Personal](tag-workspaces-resources.md "tag-workspaces-resources.md").
7. Choose **Copy image**.
