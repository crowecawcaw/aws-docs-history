# Disable Internet Explorer Enhanced

Security Configuration in Amazon WorkSpaces Applications

Internet Explorer Enhanced Security Configuration (ESC) places servers and Internet
Explorer in a configuration that limits exposure to the internet. However, this
configuration can impact the WorkSpaces Applications end user experience. Users who are connected to
WorkSpaces Applications streaming sessions may find that websites do not display or perform as
expected when:

- Internet Explorer ESC is enabled on fleet instances from which users'
  streaming sessions are launched
- Users run Internet Explorer during their streaming sessions
- Applications use Internet Explorer to load data

###### Note

The following steps apply to Windows fleets only.

###### To disable Internet Explorer Enhanced Security Configuration

1. Connect to the image builder on which to disable Internet Explorer ESC and
   sign in with an account that has local administrator permissions. To do so, do
   either of the following:
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

2. On the image builder, disable Internet Explorer ESC by doing the
   following:
   1. Open Server Manager. Choose the Windows **Start**
      button, and then choose **Server Manager**.
   2. In the left navigation pane, choose **Local Server**.
   3. In the right properties pane, choose the **On** link
      next to IE Enhanced Security Configuration.
   4. In the **Internet Explorer Enhanced Configuration**
      dialog box, choose the **Off** option under
      **Administrators** and **Users**,
      then choose **OK**.

3. In the upper right area of the image builder desktop, choose **Admin
   Commands**, **Switch User**.

![Admin Commands dropdown menu with Switch User option highlighted.](images/admin-commands-switch-user.png) 4. This disconnects your current session and opens the login menu. Log in to the
image builder by doing either of the following:

    * If your image builder is not joined to an Active Directory domain, on
     the **Local User** tab, choose **Template
     User**.
    * If your image builder is joined to an Active Directory domain, choose
     the **Directory User** tab, and log in as a domain user
     who does not have local administrator permissions on the image
     builder.

5. Open Internet Explorer and reset your settings by doing the following:
   1. In the upper right area of the Internet Explorer browser window,
      choose the **Tools** icon, then choose
      **Internet options**.
   2. Choose the **Advanced** tab, then choose
      **Reset**.
   3. When prompted to confirm your choice, choose
      **Reset** again.
   4. When the **Reset Internet Explorer Settings** message
      displays, choose **Close**.

6. Reboot image builder.
7. Choose **Admin Commands**, **Switch User**,
   and then do either of the following:
   - If your image builder is not joined to an Active Directory domain, on
     the **Local User** tab, choose
     **Administrator**.
   - If your image builder is joined to an Active Directory domain, choose
     the **Directory User** tab, and log in with the same
     domain account that you used in step 4.

8. On the image builder desktop, open Image Assistant.
9. In **Step 2. Configure Apps**, choose **Save
   settings**.
10. Follow the necessary steps in Image Assistant to finish creating your image.
    For more information, see [Tutorial: Create a Custom WorkSpaces Applications Image by Using the
    WorkSpaces Applications Console](tutorial-image-builder.md "tutorial-image-builder.md").
