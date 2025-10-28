# Delete a custom bundle or image in WorkSpaces Personal

You can delete unused custom bundles or custom images as needed.

## Delete a bundle

To delete a bundle, you must first delete all of the WorkSpaces that are based on
the bundle.

###### To delete a bundle using the console

1. Open the WorkSpaces console at [https://console.aws.amazon.com/workspaces/v2/home](https://console.aws.amazon.com/workspaces/v2/home "https://console.aws.amazon.com/workspaces/v2/home").
2. In the navigation pane, choose **Bundles**.
3. Select the bundle and choose **Delete**.
4. When prompted for confirmation, choose **Delete**.

###### To delete a bundle programmatically

To delete a bundle programmatically, use the
**DeleteWorkspaceBundle** API action. For more information,
see [DeleteWorkspaceBundle](../api/API_DeleteWorkspaceBundle.md "../api/API_DeleteWorkspaceBundle.md") in the
_Amazon WorkSpaces API Reference_.

###### Note

Ensure you wait at least 2 hours after deleting a bundle before creating a new bundle with the same name.

## Delete an image

After you delete a custom bundle, you can delete the image that you used to create
or update the bundle.

To delete an image, you must first either delete any bundles that are associated
with the image, or you must update those bundles to use another source image. You
must also unshare the image if it is shared with other accounts. The image also
can't be in the **Pending** or **Validating**
state.

###### To delete an image using the console

1. Open the WorkSpaces console at [https://console.aws.amazon.com/workspaces/v2/home](https://console.aws.amazon.com/workspaces/v2/home "https://console.aws.amazon.com/workspaces/v2/home").
2. In the navigation pane, choose **Images**.
3. Select the image and choose **Delete**.
4. When prompted for confirmation, choose **Delete**.

###### To delete an image programmatically

To delete an image programmatically, use the
**DeleteWorkspaceImage** API action. For more information,
see [DeleteWorkspaceImage](../api/API_DeleteWorkspaceImage.md "../api/API_DeleteWorkspaceImage.md") in the
_Amazon WorkSpaces API Reference_.
