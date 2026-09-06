

# Use the WorkSpaces Applications Template User Account to Change the Default Internet Explorer Home Page
<a name="customize-fleets-change-ie-homepage-template-user"></a>

Follow these steps to use the **Template User** account to change the default Internet Explorer home page. 

**To change the default Internet Explorer Home page by using the Template User account**

1. Connect to the image builder on which to change the default Internet Explorer home page and sign in with the **Template User** account. To do so, do either of the following: 
   + [Use the WorkSpaces Applications console](managing-image-builders-connect-console.md) (for web connections only)
   + [Create a streaming URL](managing-image-builders-connect-streaming-URL.md) (for web or WorkSpaces Applications client connections)
**Note**  
If the image builder that you want to connect to is joined to an Active Directory domain and your organization requires smart card sign in, you must create a streaming URL and use the WorkSpaces Applications client for the connection. For information about smart card sign in, see [Smart Cards](feature-support-USB-devices-qualified.md#feature-support-USB-devices-qualified-smart-cards).

   **Template User** lets you create default application and Windows settings for your users. For more information, see "Creating Default Application and Windows Settings for Your WorkSpaces Applications Users" in [Default Application and Windows Settings and Application Launch Performance in Amazon WorkSpaces Applications](customizing-appstream-images.md).

1. Open Internet Explorer and complete the necessary steps to change the default home page.

1. In the upper right area of the image builder desktop, choose **Admin Commands**, **Switch User**.   
![Admin Commands menu with Switch User option highlighted.](http://docs.aws.amazon.com/appstream2/latest/developerguide/images/admin-commands-switch-user.png)

1. This disconnects your current session and opens the login menu. Log in to the image builder by doing either of the following:
   + If your image builder is not joined to an Active Directory domain, on the **Local User** tab, choose **Administrator**.
   + If your image builder is joined to an Active Directory domain, choose the **Directory User** tab, and log in as a domain user who has local administrator permissions on the image builder.

1. On the image builder desktop, open Image Assistant.

1. Follow the necessary steps in Image Assistant to finish creating your image. For more information, see [Tutorial: Create a Custom WorkSpaces Applications Image by Using the WorkSpaces Applications Console](tutorial-image-builder.md).