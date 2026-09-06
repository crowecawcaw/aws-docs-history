

# Update a Fleet with a New Image in Amazon WorkSpaces Applications
<a name="update-fleets"></a>

To apply operating system updates or make new applications available to users, create a new image that has these changes. Then, update the fleet with the new image. 

**To update an WorkSpaces Applications fleet with a new image**

1. Connect to the image builder that you want to use and sign in with an account that has local administrator permissions on the image builder. To do so, do either of the following: 
   + [Use the WorkSpaces Applications console](managing-image-builders-connect-console.md) (for web connections only)
   + [Create a streaming URL](managing-image-builders-connect-streaming-URL.md) (for web or WorkSpaces Applications client connections)
**Note**  
If your organization requires smart card sign in, you must create a streaming URL and use the WorkSpaces Applications client for the connection. For information about smart card sign in, see [Smart Cards](feature-support-USB-devices-qualified.md#feature-support-USB-devices-qualified-smart-cards).

1. Do either or both of the following as required: 
   + Install updates to the operating system.
   + Install applications.

     If an application requires the Windows operating system to restart, let it do so. Before the operating system restarts, you are disconnected from your image builder. After the restart is complete, connect to the image builder again, then finish installing the application.

1. On the image builder desktop, open Image Assistant. 

1. Follow the necessary steps in Image Assistant to finish creating your image. For more information, see [Tutorial: Create a Custom WorkSpaces Applications Image by Using the WorkSpaces Applications Console](tutorial-image-builder.md).

   After the image status changes to **Available**, you can update the fleet with your new image.

1. In the left navigation pane, choose **Fleets**.

1. Select the fleet that you want to update with the new image. 

1. On the **Fleet Details** tab, choose **Edit**.

1. In the **Edit Fleet** dialog box, the list of available images displays in the **Name** list. Select the new image from the list. 

1. Choose **Update**.

**Note**  
All existing instances and user sessions will continue to run with the old image, but all new instance launches will spin up from the new image. For multi-session fleets, it is possible that instances keep running with the older image for a longer duration of time because the service will not terminate an instance if there is an active session on the instance, and if user sessions keep getting provisioned on these instances, it is possible the instance will continue to run with the old image. To get rid of long-running instances on multi-session fleets, evaluate the option of putting them in drain mode. To learn more, refer to [Manage Multi-Session Fleet Instances](manage-multi-session-instances.md).