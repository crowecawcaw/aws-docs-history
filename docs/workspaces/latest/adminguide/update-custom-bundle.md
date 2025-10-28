# Update a custom bundle for WorkSpaces Personal

You can update an existing custom WorkSpaces bundle by modifying a WorkSpace that is
based on the bundle, creating an image from the WorkSpace, and updating the bundle with
the new image. You can then launch new WorkSpaces using the updated bundle.

###### Important

Existing WorkSpaces aren't automatically updated when you update the bundle that
they're based on. To update existing WorkSpaces that are based on a bundle that
you've updated, you must either rebuild the WorkSpaces or delete and recreate
them.

###### To update a bundle using the console

1. Connect to a WorkSpace that is based on the bundle and make the changes that
   you want. For example, you can apply the latest operating system and application
   patches and install additional applications.

Alternatively, you can create a new WorkSpace with the same base software
package (Plus or Standard) as the image used to create the bundle, and make
changes. 2. If you are still connected to the WorkSpace, disconnect by choosing
**Amazon WorkSpaces** and **Disconnect** in the
WorkSpaces client application. 3. Open the WorkSpaces console at [https://console.aws.amazon.com/workspaces/v2/home](https://console.aws.amazon.com/workspaces/v2/home "https://console.aws.amazon.com/workspaces/v2/home"). 4. In the navigation pane, choose **WorkSpaces**. 5. Select the WorkSpace and choose **Actions**, **Create
Image**. If the status of the WorkSpace is `STOPPED`,
you must start it first (choose **Actions**, **Start
WorkSpaces**) before you can choose **Actions**,
**Create Image**. 6. Enter an image name and a description, and then choose **Create
Image**. The WorkSpace is unavailable while the image is being
created. For detailed information about the image creation process, see [Create a custom WorkSpaces image and bundle for WorkSpaces Personal](create-custom-bundle.md "create-custom-bundle.md"). 7. In the navigation pane, choose **Bundles**. 8. Choose the bundle to open its details page, and then under **Source
image**, choose **Edit**. 9. On the **Update source image** page, select the image that
you created and choose **Update bundle**. 10. As needed, update any existing WorkSpaces that are based on the bundle by
rebuilding the WorkSpaces or deleting and recreating them. For more information,
see [Rebuild a WorkSpace in WorkSpaces Personal](rebuild-workspace.md "rebuild-workspace.md").

###### To update a bundle programmatically

To update a bundle programmatically, use the
**UpdateWorkspaceBundle** API action. For more information, see
[UpdateWorkspaceBundle](../api/API_UpdateWorkspaceBundle.md "../api/API_UpdateWorkspaceBundle.md") in the
_Amazon WorkSpaces API Reference_.
