# Update an Image by Using

Managed WorkSpaces Applications Image Updates

WorkSpaces Applications provides an automated way to update your image with the latest Windows
operating system updates, license included application updates, driver updates, and
WorkSpaces Applications agent software. With managed WorkSpaces Applications image updates, you select the image that
you want to update. WorkSpaces Applications creates an image builder in the same AWS account and
Region to install the updates and create the new image. After the new image is
created, you can test it on a pre-production fleet before updating your production
fleets or sharing the image with other AWS accounts.

###### Note

After your new image is created, you're responsible for maintaining updates
for the Windows operating system. To do so, you can continue using managed
WorkSpaces Applications image updates.

You are responsible for maintaining updates for the Amazon EC2 Windows Paravirtual
(PV) driver, ENA driver, and AWS NVMe driver. For more information about how
to update the drivers, see [Manage device
drivers for your EC2 instance](../../../AWSEC2/latest/UserGuide/manage-device-drivers.md "../../../AWSEC2/latest/UserGuide/manage-device-drivers.md").

You're also responsible for maintaining your applications and their
dependencies. To add other applications, update existing applications, or change
image settings, you must start and reconnect to the image builder that you used
to create the image. Or, if you deleted that image builder, launch a new image
builder that is based on your image. Then, make your changes and create a new
image.

## Prerequisites

The following are prerequisites and considerations for working with managed
image updates.

- Make sure that your WorkSpaces Applications account quotas (also referred to as limits)
  are sufficient to support the creation of a new image builder and a new
  image. To request a quota increase, you can use the Service Quotas
  console at [https://console.aws.amazon.com/servicequotas/](https://console.aws.amazon.com/servicequotas/ "https://console.aws.amazon.com/servicequotas/"). For information about
  default WorkSpaces Applications quotas, see [Amazon WorkSpaces Applications Service Quotas](limits.md "limits.md").
- You must own the image that you update. You can't update an image that
  is shared with you.
- When WorkSpaces Applications creates an image builder to install the latest Windows
  operating system updates, driver updates, and WorkSpaces Applications agent software, and
  creates the new image, you're charged for the image builder instance
  while it's updating.
- Supported images must be created from a base image released on
  2017-07-24T00:00:00Z or later.
- English and Japanese are supported display languages. For more
  information, see [Specify a Default Display
  Language](configure-default-display-language.md "configure-default-display-language.md").
- Use the latest version of SSM Agent. For version information, see
  [WorkSpaces Applications Base Image and Managed Image Update
  Release Notes](base-image-version-history.md "base-image-version-history.md"). For installation
  information, see [Manually install SSM Agent on EC2 instances for Windows
  Server](../../../systems-manager/latest/userguide/sysman-install-win.md "../../../systems-manager/latest/userguide/sysman-install-win.md").

## How to Update an Image by Using Managed WorkSpaces Applications Image Updates

To update an WorkSpaces Applications image with the latest patches, driver updates, and WorkSpaces Applications
agent software, perform the following steps.

1. Open the WorkSpaces Applications console at
   [https://console.aws.amazon.com/appstream2](https://console.aws.amazon.com/appstream2 "https://console.aws.amazon.com/appstream2").
2. In the navigation pane, choose **Images**,
   **Image Registry**.
3. In the image list, choose the image that you want to update. Verify
   that the status of the image is **Available**.
4. Choose **Actions**,
   **Update**.
5. In the **Update image** dialog box, do the
   following:
   - For **New image name**, enter an image name
     that is unique within the AWS account and Region. The image
     name can't begin with "Amazon," "AWS," or "AppStream."
   - For **New image display name**, you can
     optionally enter a name to display for the image.
   - For **New image description**, you can
     optionally provide a description for the image.
   - For **Tags**, you can choose **Add
     Tag**, and type the key and value for the tag. To
     add more tags, repeat this step. For more information, see [Tagging Your Amazon WorkSpaces Applications Resources](tagging-basic.md "tagging-basic.md").

6. Choose **Update image**.

If your current image is already up to date, a message notifies
you. 7. In the navigation pane, choose **Images**, and then
choose **Image Builder**. 8. In the list of image builders, verify that a new image builder appears
in the **Updating** state. The name of the image
builder includes a random 10-digit suffix.

The image builder is the smallest size in the instance family that you
chose for the new image in step 5. No subnet is specified because the
image builder is not attached to your virtual private cloud
(VPC). 9. Choose **Image Registry** and verify that your new
image appears in the list.

While your image is being created, the image status in the image
registry of the console appears as
**Creating**. 10. After your image is created, WorkSpaces Applications performs a qualification process
to verify that the image works as expected.

During this time, the image builder, which is also used for this
process, appears in the **Image Builder** list with a
status of **Pending Qualification**. 11. After the qualification process successfully completes, a
**Success** message appears at the top of the
console and the image status in the image registry appears as
**Available**.

In addition, the image builder that WorkSpaces Applications created is deleted
automatically.

###### Note

Depending on the volume of Windows operating system updates, it
might take several hours for an image update to complete. If an
issue prevents the image from being updated, a red icon with an
exclamation point appears next to the image name, and the image
status in the image registry appears as **Failed**.
If this occurs, select the image, choose the
**Notifications** tab, and review any error
notifications. For more information, see the information in the
[Image Internal Service](troubleshooting-notification-codes.md#troubleshooting-notification-codes-image "troubleshooting-notification-codes.md#troubleshooting-notification-codes-image")
section of the documentation for troubleshooting notification
codes.

If the qualification process is not successful, the image builder
that WorkSpaces Applications created is still deleted automatically. 12. After WorkSpaces Applications creates the new image, test the image on a pre-production
fleet. After you verify that your applications work as expected, update
your production fleet with the new image.
