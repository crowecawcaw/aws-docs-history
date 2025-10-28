# Change User

Environment Variables

Follow these steps to change user environment variables across your fleet
instances.

###### To change user environment variables

1.  Connect to the image builder on which to change system environment
    variables and sign in as a **Template User**. To do so, do
    either of the following:

        * [Use the
         AppStream 2.0 console](managing-image-builders-connect-console.md "managing-image-builders-connect-console.md") (for web connections only)
        * [Create a streaming URL](managing-image-builders-connect-streaming-URL.md "managing-image-builders-connect-streaming-URL.md") (for web or AppStream 2.0 client
         connections)


        ###### Note

        If the image builder that you want to connect to is joined to
         an Active Directory domain and your organization requires smart
         card sign in, you must create a streaming URL and use the AppStream 2.0
         client for the connection. For information about smart card sign
         in, see [Smart Cards](feature-support-USB-devices-qualified.md#feature-support-USB-devices-qualified-smart-cards "feature-support-USB-devices-qualified.md#feature-support-USB-devices-qualified-smart-cards").

    **Template User** lets you create default application and
    Windows settings for your users. For more information, see "Creating Default
    Application and Windows Settings for Your AppStream 2.0 Users" in [Default Application and Windows Settings and Application Launch Performance in Amazon AppStream 2.0](customizing-appstream-images.md "customizing-appstream-images.md").

2.  On the image builder, choose the Windows **Start**
    button, **Control Panel**, **User
    Accounts**.
3.  Choose **User Accounts** again. In the left navigation
    pane, choose **Change my environment variables.**
4.  Under **User environment variables** for
    **DefaultProfileUser**, set or create the user
    environment variables as needed, then choose **OK**.
5.  This disconnects your current session and opens the login menu. Log in to
    the image builder by doing either of the following:
    - If your image builder is not joined to an Active Directory domain,
      on the **Local User** tab, choose
      **Administrator**.
    - If your image builder is joined to an Active Directory domain,
      choose the **Directory User** tab, and log in as a
      domain user who has local administrator permissions on the image
      builder.

6.  On the image builder desktop, open Image Assistant.
7.  Follow the necessary steps in Image Assistant to finish creating your
    image. For more information, see [Tutorial: Create a Custom AppStream 2.0 Image by Using the
    AppStream 2.0 Console](tutorial-image-builder.md "tutorial-image-builder.md").
