# Using the local Administrators group on the image builder

To grant Active Directory users or groups local administrator rights on your
image builder, you can manually add these users or groups to the local
Administrators group on the image builder. Image builders that are created from
images with these rights maintain the same rights.

The Active Directory users or groups to which to grant local administrator
rights must already exist.

###### To add Active Directory users or groups to the local Administrators group

on the image builder

1. Open the WorkSpaces Applications console at
   [https://console.aws.amazon.com/appstream2](https://console.aws.amazon.com/appstream2 "https://console.aws.amazon.com/appstream2").
2. Connect to the image builder in Administrator mode. The image builder
   must be running and domain-joined. For more information, see [Tutorial: Setting Up Active
   Directory](active-directory-directory-setup.md "active-directory-directory-setup.md").
3. Choose **Start**, **Administrative
   Tools**, and then double-click **Computer
   Management**.
4. In the left navigation pane, choose **Local Users and
   Groups** and open the **Groups**
   folder.
5. Open the **Administrators** group and choose
   **Add...**.
6. Select all Active Directory users or groups to which to assign local
   administrator rights and choose **OK**. Choose
   **OK** again to close the **Administrator
   Properties** dialog box.
7. Close Computer Management.
8. To log in as an Active Directory user and test whether that user has
   local administrator rights on the image builder, choose **Admin
   Commands**, **Switch user**, and then
   enter the credentials of the relevant user.
