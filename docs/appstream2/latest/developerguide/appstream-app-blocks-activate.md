# Activate an App Block

If an app block with WorkSpaces Applications packaging was created, but the application package
(VHD) was not attached to it, then the app block will be in an inactive state,
and it can't be used to associate applications with Elastic fleets. To activate
an app block, an application package (VHD) must be associated with the app
block.

###### To create the application package

1. Open the WorkSpaces Applications console at
   [https://console.aws.amazon.com/appstream2](https://console.aws.amazon.com/appstream2 "https://console.aws.amazon.com/appstream2").
2. From the left-hand navigation menu, choose **Applications
   Manager**, **App blocks**.
3. Select an **Inactive** app block that you want to
   activate, and choose **Activate** from the
   **Actions** menu.
4. Select an app block builder, and choose **Launch app block
   builder**.
   - If the list is empty, then you either don’t have an app block
     builder, or all of your app block builders are associated with
     other app blocks. Either create a new app block builder, or
     disassociate an existing app block builder and test it.
   - If the app block builder is already associated with an app
     block, then you can continue using it for activating the app
     block.
   - If the selected app block builder was not associated with an
     app block builder, then it will be associated with the one you
     select, and the streaming session will launch. The app block
     builder remains associated with this app block after the session
     ends.

5. After the app block builder streaming session starts, follow the steps
   in [Step 2: Create the Application Package](appstream-app-blocks-create.md#appstream-app-blocks-create-step2 "appstream-app-blocks-create.md#appstream-app-blocks-create-step2") to create your
   application package (VHD) and activate the app block.
