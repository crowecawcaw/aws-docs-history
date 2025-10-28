# AppStream 2.0 Console (Web Connection)

To use the AppStream 2.0 console to connect to an image builder through a web browser, complete the following steps.

1. Open the AppStream 2.0 console at
   [https://console.aws.amazon.com/appstream2](https://console.aws.amazon.com/appstream2 "https://console.aws.amazon.com/appstream2").
2. In the left navigation pane, choose **Images**,
   **Image Builder**.
3. In the list of image builders, choose the image builder to which you want to connect. Verify that the status of
   the image builder is **Running**, and choose
   **Connect**.

For this step to work, you might need to configure your browser to allow pop-ups
from https://stream.<aws-region>.amazonappstream.com/. 4. Log in to the image builder by doing either of the following:

    * If your image builder is powered by Windows, Red Hat Enterprise Linux, or Rocky Linux, on the
     **Local User** tab, choose one of the
     following:




    	+ **Administrator** — Choose **Administrator** to install your applications on the image builder and create an image, or to perform any other tasks that require local administrator permissions.
    	+ **Template User (Windows only)**  — Choose **Template
    	 User** to create default application and
    	 Windows settings.
    	+ **Test User** — Choose **Test User** to open your applications and verify their settings.
    * If your image builder is powered by Windows, Red Hat Enterprise Linux, or Rocky Linux, it's
     joined to an Active Directory domain, and you require access to
     resources that are managed by Active Directory to install your
     applications, choose the **Directory User** tab.
     Then, enter the credentials for a domain account that has local
     administrator permissions on the image builder.


    ###### Note

    Smart card sign in isn't supported for connections through a web browser. Instead, you must create a streaming URL and use the AppStream 2.0 client. For information about smart card sign in, see [Smart Cards](feature-support-USB-devices-qualified.md#feature-support-USB-devices-qualified-smart-cards "feature-support-USB-devices-qualified.md#feature-support-USB-devices-qualified-smart-cards").
    * If your image builder is powered by Amazon Linux 2, you are
     automatically logged in as


    the **ImageBuilderAdmin** user in the Amazon
     Linux GNOME desktop and have root admin privileges.
