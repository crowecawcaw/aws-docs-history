

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

1. On the fleet detail page, choose the **Image** tab.

1. In the **Image details** panel, choose **Edit**. This opens the **Edit: Fleet image** page.

1. Select the new image from the **Images** list. You can use the **Filter by attribute or keyword** box to search; the list is paginated.

1. Choose **Save** to apply the change.

**Note**  
The fleet does not need to be in the **Stopped** state to change its image. Optionally, stop the fleet first if you prefer.

**Note**  
All existing instances and user sessions will continue to run with the old image, but all new instance launches will spin up from the new image. For multi-session fleets, it is possible that instances keep running with the older image for a longer duration of time because the service will not terminate an instance if there is an active session on the instance, and if user sessions keep getting provisioned on these instances, it is possible the instance will continue to run with the old image. To get rid of long-running instances on multi-session fleets, evaluate the option of putting them in drain mode. To learn more, refer to [Manage Multi-Session Fleet Instances](manage-multi-session-instances.md).

You can also change the instance type of an existing fleet. By default, you can change a fleet's instance type only within the same instance family. If the fleet uses a unified graphics image, you can change the instance type across supported graphics families by using the `UpdateFleet` operation when the fleet is stopped. For more information, see [Unified graphics images](unified-graphics-images.md).

**To change the instance type of a fleet that uses a unified graphics image**

1. In the left navigation pane, choose **Fleets**.

1. Select the fleet that you want to change.

1. Choose **Actions**, **Stop** to stop the fleet. You must stop the fleet before you can change its instance type across graphics families.

1. After the fleet is in the **Stopped** state, choose **Actions**, **Edit**.

1. For **Instance Type**, select the new instance type (for example, stream.graphics.g7.4xlarge).

1. Choose **Save**.

1. Choose **Actions**, **Start** to start the fleet. New instances launch on the selected graphics family.

For example, suppose that the fleet my-cad-fleet uses a unified graphics image and runs on stream.graphics.g6.4xlarge. To move the fleet to the Graphics G7 family, stop my-cad-fleet, edit the fleet, select stream.graphics.g7.4xlarge for the instance type, save the change, and start the fleet. New instances then launch on the Graphics G7 family. You can also change the instance type by using the [UpdateFleet](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_UpdateFleet.html) API operation or the [update-fleet](https://docs.aws.amazon.com/cli/latest/reference/appstream/update-fleet.html) AWS CLI command.