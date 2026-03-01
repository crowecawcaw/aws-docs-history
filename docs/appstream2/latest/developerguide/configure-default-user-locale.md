# Specify a Default User Locale

To specify a default user locale for your users’ streaming sessions, perform the
following steps.

###### Note

If you plan to configure the display language and you want the user locale and
display language to match, you do not need to change the user locale. Changing the
display language automatically changes the user locale to match.

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
5. In the **Format** list, choose a language and region.

###### Note

Currently, WorkSpaces Applications supports only **English (United States)** and **Japanese (Japan)**. 6. Choose **OK** to close the **Region** dialog
box. 7. If required, configure additional default regional or language settings.
Otherwise, on the image builder desktop, open Image Assistant and install and
configure applications for streaming. 8. In Step 2 of the Image Assistant process, choose **Save
settings**. 9. Follow the necessary steps in Image Assistant to finish creating your image.
For information about how to create an image, see [Tutorial: Create a Custom WorkSpaces Applications Image by Using the WorkSpaces Applications Console](tutorial-image-builder.md "tutorial-image-builder.md"). 10. Do one of the following:

    * Create a new fleet and choose your new image for the fleet. For more
     information, see [Create an Amazon WorkSpaces Applications Fleet and Stack](set-up-stacks-fleets.md "set-up-stacks-fleets.md").
    * Update an existing fleet to use the new image.

11. Associate your fleet with the stack that is assigned to the users for whom you
    are configuring the default settings.

The default user locale setting that you configured is applied to the fleet
instances and user streaming sessions that are launched from those
instances.

###### Note

Your users can change their user locale from the default setting that you
configured to any one of 11 different supported locales. To do so, they can
configure their regional settings during application streaming sessions, as
described in [Enable Your WorkSpaces Applications Users to Configure Their Regional Settings](regional-settings.md "regional-settings.md").
Also, if a user previously selected a user locale when streaming from any fleet
instance in the same Region, that user-specified setting automatically overrides any
default user locale setting that you specify through your image builder.
