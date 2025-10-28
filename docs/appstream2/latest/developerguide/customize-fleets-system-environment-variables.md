# Change System

Environment Variables

Follow these steps to change system environment variables across your fleet
instances.

###### To change system environment variables on an image builder

This procedure applies only to system environment variables, not user
environment variables. To change user environment variables that persist across
your fleet instances, perform the steps in the next procedure.

1. Connect to the image builder on which to change system environment
   variables and sign in with an account that has local administrator
   permissions. To do so, do either of the following:
   - [Use the
     AppStream 2.0 console](managing-image-builders-connect-console.md "managing-image-builders-connect-console.md") (for web connections only)
   - [Create a streaming URL](managing-image-builders-connect-streaming-URL.md "managing-image-builders-connect-streaming-URL.md") (for web or AppStream 2.0 client
     connections)

   ###### Note

   If the image builder that you want to connect to is joined to
   an Active Directory domain and your organization requires smart
   card sign in, you must create a streaming URL and use the AppStream 2.0
   client for the connection. For information about smart card sign
   in, see [Smart Cards](feature-support-USB-devices-qualified.md#feature-support-USB-devices-qualified-smart-cards "feature-support-USB-devices-qualified.md#feature-support-USB-devices-qualified-smart-cards").

2. Choose the Windows **Start** button, open the context
   (right-click) menu for **Computer**, and then choose
   **Properties**.
3. In the navigation pane, choose **Advanced system
   settings**.
4. In **System variables**, change the environment variables
   that you want to persist across your fleet instances, and then
   choose **OK**.
5. On the image builder desktop, open Image Assistant.
6. Follow the necessary steps in Image Assistant to finish creating your
   image. For more information, see [Tutorial: Create a Custom AppStream 2.0 Image by Using the
   AppStream 2.0 Console](tutorial-image-builder.md "tutorial-image-builder.md").

The changes to the system environment variables persist across your fleet
instances and are available to streaming sessions launched from those
instances.

###### Note

Setting AWS CLI credentials as system environment variables might
prevent AppStream 2.0 from creating the image.
