# Share an Image That You Own With Another AWS

Account in Amazon WorkSpaces Applications

WorkSpaces Applications images are a regional resource, so you can share an image that you own with
other AWS accounts within the same AWS Region. Doing so can be helpful in several
different scenarios. For example, if you separate your development and production
resources by using different AWS accounts, you can create an image by using your
development account. Then you can share the image with your production account. If your
organization is an independent software vendor (ISV), you can share optimized images
with your customers. Optimized images that have the required applications already
installed and configured let your customers get started with your applications quickly,
so that they won't need to install and configure those applications themselves.

When you share an image with another AWS account, you specify whether the
destination account can use the image in a fleet or create new images by creating an
image builder. You continue to own images that you share. This way, you can add, change, or
remove permissions as needed for your shared images.

If you share an image with an account and grant the account fleet permissions, the shared image can be used to create or update fleets in that account. If you remove these permissions later, the account can no longer
use the image. For fleets in the account that use the shared image, the desired capacity is set
to 0, which prevents new fleet instances from being created. Existing sessions continue until
the streaming session ends. For new fleet instances to be created, the fleet in that account must be updated with a valid image.

If you share an image with an account and grant the account image builder permissions, the shared image can be used to create image builders and
images in that account. If you remove these permissions later, image builders
and images that were created from your image are not affected.

###### Important

After you share an image with an account, you can't control image
builders or images in the account that are created from your image. For this reason,
grant image builder permissions to an account only if you want to enable the account to make a copy of your image, and retain access to the copy after you stop sharing your
image.

###### To share an image that you own with another AWS account

1.  Open the WorkSpaces Applications console at
    [https://console.aws.amazon.com/appstream2](https://console.aws.amazon.com/appstream2 "https://console.aws.amazon.com/appstream2").
2.  In the navigation pane, choose **Images**, **Image Registry**.
3.  In the image list, select the image that you want to share.
4.  Choose **Actions**, **Share**.
5.  In the **Share image** dialog box, choose **Add account**.
6.  Type the 12-digit AWS account ID of the account that you want to share the image with, and
    then select whether the account can do one or both of the following:

        * Use the image to launch an image builder, if you want to create a new image.
        * Use the image with a fleet.

    To remove an account from the list of accounts that the image is shared with,
    in the row for the account you want to remove, choose the X icon to the right of
    the **Use for fleet** option.

7.  To share the image with more AWS accounts, repeat step 6 for each account that you want to
    share the image with.
8.  Choose **Share Image**.

###### To add or update image sharing permissions for an image that you own

1.  Open the WorkSpaces Applications console at
    [https://console.aws.amazon.com/appstream2](https://console.aws.amazon.com/appstream2 "https://console.aws.amazon.com/appstream2").
2.  In the navigation pane, choose **Images**, **Image Registry**.
3.  In the image list, select the image that you want to change the permissions for.
4.  Below the image list, choose the **Permissions** tab for the image you selected, then choose **Edit**.
5.  In the **Edit image permissions** dialog box, select or clear one or both of the following image sharing options as needed for one or more AWS accounts. If you clear both options for an account, the image is no longer shared with that account.

        * Use the image to launch an image builder, if you want to create a new image.
        * Use the image with a fleet.

    To remove an account from the list of accounts that the image is shared with,
    in the row for the account you want to remove, choose the X icon to the right of
    the **Use for fleet** option.

6.  To edit image sharing permissions for more AWS accounts, repeat step 5 for each account you
    want to update permissions for.
7.  Choose **Update image sharing permissions**.
