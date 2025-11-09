# Test an App Block

You can use an app block builder to test your app block and verify your
application functionalities. You don’t need to launch an Elastic fleet for this
option. You can also create multiple app block builders with different instance
types or sizes, and test the performance of your application with different
compute options.

###### Note

The test app block option is supported only for app blocks with WorkSpaces Applications
packaging.

###### To test an app block

1. Open the WorkSpaces Applications console at
   [https://console.aws.amazon.com/appstream2](https://console.aws.amazon.com/appstream2 "https://console.aws.amazon.com/appstream2").
2. From the left-hand navigation menu, choose **Applications
   Manager**, **App blocks**.
3. Select an app block that you want to test, and choose
   **Test** from the **Actions**
   menu.
4. Select an app block builder, and choose **Launch and test app
   block**.
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

5. App block builder launches in a separate browser window in a Desktop
   streaming mode. The service downloads the app block from the
   Amazon S3 bucket and installs it on the app block builder
   instance.
6. Your applications can now be streamed and tested. You can open your
   application by either browsing it in File Explorer or using the Start
   menu.
7. When you are done testing, end the streaming session.
