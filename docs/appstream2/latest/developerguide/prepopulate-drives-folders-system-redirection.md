# Make

Default Drives and Folders Available for Your Users to Share

By default, when you enable file direction for users of a stack, the following
drives and folders are made available for those users to share in their
streaming session:

- Drives:
  - All local hard disks (physical drives, such as the C Drive and
    D Drive)
  - All virtual drives (network and virtual drives such as mapped
    drive letters, Google Drive, and OneDrive)
  - All local USB drives

- Folders:

      + %USERPROFILE%\Desktop
      + %USERPROFILE%\Documents
      + %USERPROFILE%\Downloads

  These drive and folder paths prepopulate the **Share your local drives
  and folders** dialog box. This dialog box is displayed when users
  sign in to WorkSpaces Applications, start a streaming session, and choose
  **Settings**, **Local Resources**, and
  **Local Drives and Folders**.

You can change or define your own default drive and folder paths by editing
the registry. You can also use the administrative template file that is provided
in the WorkSpaces Applications client Enterprise Deployment Tool. This template lets you
configure the client by using Group Policy. For more information, see [Install and Configure the WorkSpaces Applications Client](install-configure-client.md "install-configure-client.md").

When users access their shared local drives and folders during a streaming
session, the corresponding paths appear with backslashes replaced by
underscores. They are also suffixed with the name of the local computer and a
drive letter. For example, for a user with the user name janedoe and a computer
name of ExampleCorp-123456, the default Desktop, Documents, and Downloads folder
paths appear as follows:

C_Users_janedoe_Desktop (\\ExampleCorp-123456) (F:)

C_Users_janedoe_Documents (\\ExampleCorp-123456) (G:)

C_Users_janedoe_Downloads (\\ExampleCorp-123456) (H:)
