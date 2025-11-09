# Creating Default Application and Windows Settings with the Image Assistant CLI operations

You can create default application and Windows settings so that your users can get
started with their applications quickly. When you create these settings, WorkSpaces Applications
replaces the Windows default user profile with the profile that you configure. The
Windows default user profile is then used to create the initial settings for users in
the fleet instance. If you create these settings by using the Image Assistant CLI
operations, your application installer, or the automation, should modify the Windows
default user profile directly.

To overwrite the Windows default user profile with that of another Windows user, you can also use the Image Assistant `update-default-profile` CLI operation.

For more information about configuring default application and Windows settings, see _Creating Default Application and Windows Settings for Your WorkSpaces Applications Users_ in [Default Application and Windows Settings and Application Launch Performance in Amazon WorkSpaces Applications](customizing-appstream-images.md "customizing-appstream-images.md").
