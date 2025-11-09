# Specify a Default System

Locale

To specify a default system locale for your users’ streaming sessions, perform the
following steps.

1. Connect to the image builder that you want to use and sign in with an account
   that has local administrator permissions. To do so, do either of the
   following:
   - [Use the WorkSpaces Applications
     console](managing-image-builders-connect-console.md "managing-image-builders-connect-console.md") (for web connections only)
   - [Create a
     streaming URL](managing-image-builders-connect-streaming-URL.md "managing-image-builders-connect-streaming-URL.md") (for web or WorkSpaces Applications client connections)

   ###### Note

   If the image builder that you want to connect to is joined to an
   Active Directory domain and your organization requires smart card
   sign in, you must create a streaming URL and use the WorkSpaces Applications client
   for the connection. For information about smart card sign in, see
   [Smart Cards](feature-support-USB-devices-qualified.md#feature-support-USB-devices-qualified-smart-cards "feature-support-USB-devices-qualified.md#feature-support-USB-devices-qualified-smart-cards").

2. On the image builder desktop, choose the Windows **Start**
   button, and choose **Control Panel**.
3. Choose **Clock, Language, and Region**, then
   **Region**.
4. In the **Region** dialog box, choose the
   **Formats** tab.
5. Choose **Change system locale**.
6. In the **Region Settings** dialog box, in the
   **Current system locale** list, choose a language and
   region.

###### Note

Currently, WorkSpaces Applications supports only **English (United States)** and **Japanese (Japan)**. 7. Choose **OK** to close the **Region
Settings** dialog box, and choose **OK** again to
close the **Region** dialog box. 8. When prompted to restart your computer, allow Windows to restart. 9. While Windows restarts, the WorkSpaces Applications login prompt displays. Wait for 10 minutes
before you log in to the image builder again. Otherwise, you may receive an
error. After 10 minutes, you can log in as
**Administrator**. 10. If required, configure additional default regional or language settings.
Otherwise, on the image builder desktop, open Image Assistant and install and
configure applications for streaming. After you finish configuring your image
builder, follow the necessary steps in Image Assistant to finish creating your
image. For information about how to create an image, see [Tutorial: Create a Custom WorkSpaces Applications Image by Using the
WorkSpaces Applications Console](tutorial-image-builder.md "tutorial-image-builder.md"). 11. Do one of the following:

    * Create a new fleet and choose your new image for the fleet. For more
     information, see [Create an Amazon WorkSpaces Applications Fleet and Stack](set-up-stacks-fleets.md "set-up-stacks-fleets.md").
    * Update an existing fleet to use the new image.

12. Associate your fleet with the stack that is assigned to the users for whom you
    are configuring the default settings.

The default system locale setting that you configured is applied to the fleet
instances and user streaming sessions that are launched from those
instances.
