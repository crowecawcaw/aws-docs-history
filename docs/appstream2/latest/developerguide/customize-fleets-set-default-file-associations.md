# Set Default File

Associations for Your Users in Amazon WorkSpaces Applications

The associations for application file extensions are set on a per-user basis and so
are not automatically applied to all users who launch WorkSpaces Applications streaming sessions. For
example, if you set Adobe Reader as the default application for .pdf files on your image
builder, this change is not applied to your users.

###### Note

The following steps apply to Windows fleets only.

###### Note

The following steps must be performed on an image builder that is joined to an
Active Directory domain. In addition, your fleet must be joined to an Active
Directory domain. Otherwise, the default file associations that you set are not
applied.

###### To set default file associations for your users

1. Connect to the image builder on which to set default file associations and
   sign in with a domain account that has local administrator permissions on the
   image builder. To do so, do either of the following:
   - [Use the WorkSpaces Applications
     console](managing-image-builders-connect-console.md "managing-image-builders-connect-console.md") (for web connections only)
   - [Create a
     streaming URL](managing-image-builders-connect-streaming-URL.md "managing-image-builders-connect-streaming-URL.md") (for web or WorkSpaces Applications client connections)

   ###### Note

   If your organization requires smart card sign in, you must create
   a streaming URL and use the WorkSpaces Applications client for the connection. For
   information about smart card sign in, see [Smart Cards](feature-support-USB-devices-qualified.md#feature-support-USB-devices-qualified-smart-cards "feature-support-USB-devices-qualified.md#feature-support-USB-devices-qualified-smart-cards").

2. Set default file associations as needed.
3. Open the Windows command prompt as an administrator.
4. At the command prompt, type the following command to export the image builder
   file associations as an XML file, and then press ENTER:

`dism.exe /online
 /export-DefaultAppAssociations:c:\default_associations.xml`

If you receive an error message stating that you cannot service a running
64-bit operating system with a 32-bit version of DISM, close the command prompt
window. Open File Explorer, browse to C:\Windows\System32, right-click cmd.exe,
choose **Run as Administrator**, and run the command
again. 5. You can use either Local Group Policy Editor or the GPMC to set a default
associations configuration file:

    * Local Group Policy Editor:


    On your image builder, open the command prompt as an administrator,
     type `gpedit.msc`, and then press ENTER.


    In the console tree, under **Computer
     Configuration**, expand **Administrative
     Templates**, **Windows Components**, and
     then choose **File Explorer**.
    * GPMC:


    In your directory or on a domain controller, open the command prompt
     as an administrator, type `gpmc.msc`, and then press
     ENTER.


    In the left console tree, select the OU in which you want to create a
     new GPO, or use an existing GPO, and then do either of the
     following:




    	+ Create a new GPO by opening the context (right-click) menu and
    	 choosing **Create a GPO in this domain, Link it
    	 here**. For **Name**, provide a
    	 descriptive name for this GPO.
    	+ Select an existing GPO.
    Open the context menu for the GPO, and choose
     **Edit**.


    Under **User Configuration**, expand
     **Policies**, **Administrative
     Templates**, **Windows Components**, and
     then choose **File Explorer**.

6. Double-click **Set a default associations configuration
   file**.
7. In the **Set a default associations configuration file
   properties** dialog box, choose **Enabled**, and
   do one of the following:
   - If you are using Local Group Policy Editor, enter this path:
     `c:\default_associations.xml`.
   - If you are using the GPMC, enter a network path. For example,
     `\\networkshare\default_associations.xml`.

8. Choose **Apply**, **OK**.
9. Close Local Group Policy Editor or the GPMC.
10. On the image builder desktop, open Image Assistant.
11. Follow the necessary steps in Image Assistant to finish creating your image.
    For more information, see [Tutorial: Create a Custom WorkSpaces Applications Image by Using the
    WorkSpaces Applications Console](tutorial-image-builder.md "tutorial-image-builder.md").

The file associations that you configured are applied to the fleet instances
and user streaming sessions that are launched from those instances.
