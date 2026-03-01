# Specify a Default Time Zone

To specify a default time zone to be used in your users’ streaming sessions, perform
the steps in either of the following two procedures.

###### Procedures

- [Specify a Default Time Zone (Windows Server 2012 R2)](#configure-default-time-zone "#configure-default-time-zone")
- [Specify a Default Time Zone (Windows Server 2016, Windows Server 2019, Windows Server 2022, and Windows Server 2025)](#configure-default-time-zone-2016-2019 "#configure-default-time-zone-2016-2019")

###### Note

Currently, WorkSpaces Applications supports only **UTC** and **(UTC+9:00)
Osaka, Sapporo, Tokyo**.

## Specify a Default Time Zone (Windows Server 2012 R2)

1. Connect to the image builder that you want to use and sign in with a user
   that has local administrator permissions. To do so, do either of the
   following:
   - [Use the
     WorkSpaces Applications console](managing-image-builders-connect-console.md "managing-image-builders-connect-console.md") (for web connections only)
   - [Create a streaming URL](managing-image-builders-connect-streaming-URL.md "managing-image-builders-connect-streaming-URL.md") (for web or WorkSpaces Applications client
     connections)

   ###### Note

   If the image builder that you want to connect to is joined to
   an Active Directory domain and your organization requires smart
   card sign in, you must create a streaming URL and use the WorkSpaces Applications
   client for the connection. For information about smart card sign
   in, see [Smart Cards](feature-support-USB-devices-qualified.md#feature-support-USB-devices-qualified-smart-cards "feature-support-USB-devices-qualified.md#feature-support-USB-devices-qualified-smart-cards").

2. On the image builder desktop, choose the Windows
   **Start** button, and choose **Control
   Panel**.
3. Choose **Clock, Language, and Region**, then
   **Date and Time**, then **Change time
   zone**.
4. In the **Time zone** list, choose a time zone, and choose
   **OK**.
5. To apply any change to the time zone setting, restart your image builder.
   To do so, choose the Windows **Start** button, and choose
   **Windows PowerShell**. In PowerShell, use the
   **restart-computer** cmdlet.
6. While Windows restarts, the WorkSpaces Applications login prompt displays. Wait for 10
   minutes before you log in to the image builder again. Otherwise, you may
   receive an error. After 10 minutes, you can log in as
   **Administrator**.
7. If required, configure additional default regional or language settings.
   Otherwise, on the image builder desktop, open Image Assistant and install
   and configure applications for streaming.
8. After you finish configuring your image builder, follow the necessary
   steps in Image Assistant to finish creating your image. For information
   about how to create an image, see [Tutorial: Create a Custom WorkSpaces Applications Image by Using the WorkSpaces Applications Console](tutorial-image-builder.md "tutorial-image-builder.md").
9. Do one of the following:
   - Create a new fleet and choose your new image for the fleet. For
     more information, see [Create an Amazon WorkSpaces Applications Fleet and Stack](set-up-stacks-fleets.md "set-up-stacks-fleets.md").
   - Update an existing fleet to use the new image.

10. Associate your fleet with the stack that is assigned to the users for whom
    you are configuring the default settings.

The default time zone setting that you configured is applied to the fleet
instances and user streaming sessions that are launched from those
instances.

## Specify a Default Time Zone (Windows Server 2016, Windows Server 2019, Windows Server 2022, and Windows Server 2025)

1. Connect to the image builder that you want to use and sign in with an
   account that has local administrator permissions. To do so, do either of the
   following:
   - [Use the
     WorkSpaces Applications console](managing-image-builders-connect-console.md "managing-image-builders-connect-console.md") (for web connections only)
   - [Create a streaming URL](managing-image-builders-connect-streaming-URL.md "managing-image-builders-connect-streaming-URL.md") (for web or WorkSpaces Applications client
     connections)

   ###### Note

   If the image builder that you want to connect to is joined to
   an Active Directory domain and your organization requires smart
   card sign in, you must create a streaming URL and use the WorkSpaces Applications
   client for the connection. For information about smart card sign
   in, see [Smart Cards](feature-support-USB-devices-qualified.md#feature-support-USB-devices-qualified-smart-cards "feature-support-USB-devices-qualified.md#feature-support-USB-devices-qualified-smart-cards").

2. On the image builder desktop, choose the Windows
   **Start** button, and choose **Control
   Panel**.
3. Specify the default time zone by using PowerShell or the Windows user
   interface:
   - **PowerShell**
     - Open PowerShell and run the following command:

     ```
     Run Set-TimeZone -Id "Tokyo Standard Time"
     ```

     ###### Note

     To run this command, you must be logged in to the
     applicable computer as
     **Administrator**.

   - **Windows user interface**
     1. On the image builder desktop, choose the Windows
        **Start** button, and type
        `timedate.cpl` to open the
        **Date and Time** control panel
        item.
     2. Right-click the **Date and Time** icon,
        and choose **Run as administrator**.
     3. When prompted by **User Account Control**
        to choose whether you want to allow the app to make changes
        to your device, choose **Yes**.
     4. Choose **Change time zone**.
     5. In the **Time zone** list, choose a time
        zone, and choose **OK**.

4. If required, configure additional default regional or language settings.
   Otherwise, on the image builder desktop, open Image Assistant and install
   and configure applications for streaming.
5. After you finish configuring your image builder, follow the necessary
   steps in Image Assistant to finish creating your image. For information
   about how to create an image, see [Tutorial: Create a Custom WorkSpaces Applications Image by Using the WorkSpaces Applications Console](tutorial-image-builder.md "tutorial-image-builder.md").
6. Do one of the following:
   - Create a new fleet and choose your new image for the fleet. For
     more information, see [Create an Amazon WorkSpaces Applications Fleet and Stack](set-up-stacks-fleets.md "set-up-stacks-fleets.md").
   - Update an existing fleet to use the new image.

7. Associate your fleet with the stack that is assigned to the users for whom
   you are configuring the default settings.

The default time zone setting that you configured is applied to the fleet
instances and user streaming sessions that are launched from those
instances.

###### Note

Your users can change their time zone from the default setting that you
configured. They can configure their regional settings during an application
streaming session, as described in [Enable Your WorkSpaces Applications Users to Configure Their Regional Settings](regional-settings.md "regional-settings.md"). Also, if a user previously selected a time
zone when streaming from any fleet instance in the same AWS Region, the
user-specified time zone setting automatically overrides any default time zone
setting you specify through your image builder.
