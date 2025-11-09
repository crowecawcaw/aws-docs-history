# Local File Access

WorkSpaces Applications file redirection lets you access files on your local computer from your
WorkSpaces Applications streaming session. To use file redirection, open the WorkSpaces Applications client,
connect to a streaming session, and choose the drives and folders that you want
to share. After you share a local drive or folder, you can access all files in
the shared drive or folder from your streaming session. You can stop sharing
local drives and folders at any time.

###### Important

To use WorkSpaces Applications file redirection, you must have the WorkSpaces Applications client installed on your local
computer. File redirection is not available when you connect to WorkSpaces Applications by using a web browser.

###### To share local drives and folders

1. Open the WorkSpaces Applications client and connect to a streaming session.
2. In your WorkSpaces Applications session, in the top left area, choose the **Settings** icon, and then choose **Local Resources**, **Local Drives and Folders**.

![Settings menu with Local Resources option and submenu showing Local Drives and Folders.](images/AppStream2-Client-Local-Drives-Folders-MenuOptions.png)

The **Share your local drives and folders** dialog box
displays the drives and folders that your administrator has made
available for you to share. You can share all or specific drives and
folders, or just one. You can also add your own drives and folders. To
share drives and folders, do one of the following:

    * To share all local drives and folders displayed in the **Share your local drives and
     folders** dialog box, choose **Share
     All**. To apply your changes to future streaming
     sessions, choose **Save my configuration**.



    ![Dialog box for sharing local drives and folders with options to share all or save configuration.](images/AppStream2-Client-Local-Drives-Folders-ShareAll.png)
    * To share a specific local drive or folder, select the drive or folder that you want to access,
     and choose **Share**, **Save my
     configuration**. To share another local drive or
     folder, repeat these steps as needed.



    ![Dialog for sharing local drives and folders, with options to share specific items.](images/AppStream2-Client-Local-Drives-Folders-Share-Specific.png)
    * If the local drive or folder that you want to share is not displayed, you can add it. For
     example, your administrator might make your entire local C Drive
     available for you to share. However, you might only need to
     access a specific folder on that drive. In this case, you can
     add the folder that you need and share only that folder. To
     choose a folder, do the following:




    	+ In the **Share your local drives and folders** dialog box, choose
    	 **Add Folder**.



    	![Dialog box for sharing local drives and folders, with an "Add Folder" button highlighted.](images/AppStream2-Client-Local-Drives-Folders-Add-Specific-Folder.png)
    	+ Browse to the folder that
    	 you want to share, and choose **OK**.
    	+ The folder that you selected is now available to share. Select the folder, and choose
    	 **Share**, **Save my
    	 configuration**. To add another local drive or
    	 folder, repeat these steps as needed.



    	![Dialog for sharing local drives and folders, with options to share specific drives and folders.](images/AppStream2-Client-Local-Drive-Folders-SpecificFolderAdded.PNG)

After you share a local drive or folder, perform the following steps to access
files in the shared drive or folder from your streaming session.

###### To access files in a shared local drive or folder

1. Open the WorkSpaces Applications client and connect to a streaming session.
2. In your WorkSpaces Applications session, open the application that you want to use.
3. From your application interface, choose **File Open**, and browse to the file
   that you want to access. The following screenshot shows how shared local
   drives and folders appear in the Notepad++ browse dialog box for Jane
   Doe when she browses for a file.

![File browser showing shared local drives and folders for a user, including mapped network drives.](images/AppStream2-Client-Local-Drives-Folders-Access-Shared-Drives-Folders.png)

In the browse dialog box, the corresponding paths for her shared drives and folders are shown in the red box. The paths appear with backslashes replaced by
underscores. At the end of each path is the name of Jane's computer, ExampleCorp-123456, and a drive letter. 4. When you're done working with the file, use the **File Save** or **File Save As** command to save it to the location that you want.
If you want to stop sharing a local drive or folder, perform the following steps.

###### To stop sharing local drives and folders

1. Open the WorkSpaces Applications client and connect to a streaming session.
2. In your WorkSpaces Applications session, in the top left area, choose the **Settings** icon, and then choose **Local Resources**, **Local Drives and Folders**.

The **Share your local drives and folders** dialog box displays the drives and folders that your administrator has made available for you to share, and any that you added, if applicable. To stop sharing one or more local drives and folders, do either of the following:

    * To stop sharing all shared local drives and folders, choose **Unshare All**, **Save my configuration**.



    ![Interface for sharing local drives and folders with options to unshare and save configuration.](images/AppStream2-Client-Local-Drives-Folders-UnshareAll.png)
    * To stop sharing a specific shared local drive or folder, select the drive or folder, and choose
     **Unshare**, **Save my
     configuration**. To stop sharing another local drive or
     folder, repeat these steps as needed.



    ![Interface for sharing local drives and folders with options to unshare and save configuration.](images/AppStream2-Client-Local-Drives-Folders-UnshareAll.png)

You can delete local drives and folders that you add to the **Share your
local drives and folders** dialog box. However, you can't delete local
drives or folders that your administrator has made available for you to share. Also,
if you have already shared a local drive or folder, you must stop sharing it before you
can delete it.

###### To delete local drives and folders

1. Open the WorkSpaces Applications client and connect to a streaming session.
2. In your WorkSpaces Applications session, in the top left area, choose the **Settings** icon, and then choose **Local Resources**, **Local Drives and Folders**.

The **Share your local drives and folders** dialog box
displays the drives and folders that your administrator has made
available for you to share. If you added any drives or folders, they are
also displayed. 3. Select the local drive or folder that you want to delete, and then choose **Delete**, **Save my configuration**.

![Dialog for sharing local drives and folders, with options to delete and save configuration.](images/AppStream2-Client-Local-Drive-Folders-SpecificFolderAdded-Delete.png)
