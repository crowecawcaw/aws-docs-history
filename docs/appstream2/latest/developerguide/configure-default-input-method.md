# Specify a Default Input Method

To specify a default input method to be used in your users’ streaming sessions,
perform the following steps.

###### Note

If you plan to configure the display language, and you want the input method and
display language to match, you do not need to change the input method. Changing the
display language in Windows also automatically changes the user locale and input
method to match the language and region of the display language. If you want all
three settings to match, you do not need to separately change the user locale or
input method.

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
   **Language**, **Add a language**.
4. Choose a language, and choose **Add**.

###### Note

Currently, WorkSpaces Applications supports only **English (United
States)** and **Japanese**. 5. The language that you chose appears in the list of languages you added to
Windows. 6. Choose **Advanced Settings**. Under **Override for
default input method**, choose the input method for the language
you added. 7. Choose **Save**. 8. Log off and log in again. To do so, choose the Windows
**Start** button on the image builder desktop. Choose
**ImageBuilderAdmin**, **Sign out**. When
prompted, log in as Administrator. 9. If required, configure additional default regional or language settings.
Otherwise, on the image builder desktop, open Image Assistant and install and
configure applications for streaming. 10. In Step 2 of the Image Assistant process, choose **Save
settings**. 11. Follow the necessary steps in Image Assistant to finish creating your image.
For information about how to create an image, see [Tutorial: Create a Custom WorkSpaces Applications Image by Using the WorkSpaces Applications Console](tutorial-image-builder.md "tutorial-image-builder.md"). 12. Do one of the following:

    * Create a new fleet and choose your new image for the fleet. For
     information, see [Create an Amazon WorkSpaces Applications Fleet and Stack](set-up-stacks-fleets.md "set-up-stacks-fleets.md").
    * Update an existing fleet to use the new image.

13. Associate your fleet with the stack that is assigned to the users for whom you
    are configuring the default settings.

The default input method that you configured is applied to the fleet instances
and user streaming sessions that are launched from those instances.

###### Note

Your users can change their input method from the default setting that you
configured to any one of nine different supported input methods. They can configure
this setting by configuring their regional settings during application streaming
sessions, as described in [Enable Your WorkSpaces Applications Users to Configure Their Regional Settings](regional-settings.md "regional-settings.md"). Also, if a user previously selected an input
method when streaming from any fleet instance in the same Region, that
user-specified setting automatically overrides any default input method that you
specify through your image builder.
