# Streaming URL (WorkSpaces Applications Client or Web Connection)

You can create a streaming URL to connect to an image builder through a web
browser or the WorkSpaces Applications client. Unlike a streaming URL that you create to enable user
access to a fleet instance, which is valid for a maximum of seven days, by default,
a streaming URL that you create to access an image builder expires after one hour.
To set a different expiration time, you must generate the streaming URL by using the
[CreateStreamingURL](../APIReference/API_CreateStreamingURL.md "../APIReference/API_CreateStreamingURL.md") API action.

If the image builder that you want to connect to is
joined to an Active Directory domain and your organization requires smart card sign
in, you must create a streaming URL and use the WorkSpaces Applications client for the connection.

###### Note

The streaming URL provides direct access to the image builder instance. Manage
the streaming URL properly and do not share it with unintended users.

###### Note

Native application mode is not supported for WorkSpaces Applications client connections to image builders. If
you use the WorkSpaces Applications client to connect to an image builder and the **Start in native
application mode** check box is selected, an WorkSpaces Applications error notification displays, stating that your session was switched to classic mode.

You can create a streaming URL in any of the following ways:

- WorkSpaces Applications console
- The [CreateStreamingURL](../APIReference/API_CreateStreamingURL.md "../APIReference/API_CreateStreamingURL.md") API action
- The [create-streaming-url](../../../cli/latest/reference/appstream/create-streaming-url.md "../../../cli/latest/reference/appstream/create-streaming-url.md") AWS CLI command
  To create a streaming URL and connect to the image builder by using the WorkSpaces Applications console, complete the steps in the following procedure.

###### To create a streaming URL and connect to the image builder by using the

WorkSpaces Applications console

1. Open the WorkSpaces Applications console at
   [https://console.aws.amazon.com/appstream2](https://console.aws.amazon.com/appstream2 "https://console.aws.amazon.com/appstream2").
2. In the navigation pane, choose **Images**,
   **Image Builder**.
3. In the list of image builders, choose the image builder to which you want to connect. Verify that the status of
   the image builder is **Running**.
4. Choose **Actions**, **Create streaming
   URL**.
5. Do one of the following:
   - To connect to the image builder through the WorkSpaces Applications client, choose
     **Launch in Client**. When you choose this
     option, the WorkSpaces Applications client sign-in page is prepopulated with the
     streaming URL.
   - To connect to the image builder through a web browser, choose
     **Launch in Browser**. When you choose this
     option, a web browser opens with the address bar prepopulated with
     the streaming URL.

6. After you create the streaming URL and connect to the image builder, log
   in to the image builder by doing either of the following:
   - If your image builder is Windows-based and not joined to an Active
     Directory domain, on the **Local User** tab, choose
     one of the following:
     - **Administrator** — Choose
       **Administrator** to install your
       applications on the image builder and create an image, or to
       perform any other tasks that require local administrator
       permissions.
     - **Template User** — Choose
       **Template User** to create default
       application and Windows settings.
     - **Test User** — Choose
       **Test User** to open your applications
       and verify their settings.

   - If your image builder is Windows-based and joined to an Active
     Directory domain and you require access to resources that are
     managed by Active Directory to install your applications, choose the
     **Directory User** tab, and enter the
     credentials for a domain account that has local administrator
     permissions on the image builder.

   ###### Note

   If you're using the WorkSpaces Applications client, you can enter either your
   Active Directory domain password and choose **Password
   sign in**, or select **Choose a smart
   card** and provide your smart card PIN when
   prompted.

   If you're using a web browser, you must enter your Active
   Directory domain password. Smart card sign in is supported only
   for WorkSpaces Applications client connections to streaming instances.
   - If your image builder is Linux-based, you are automatically logged
     in as

   the **ImageBuilderAdmin** user in the Amazon
   Linux GNOME desktop and have root admin privileges.
