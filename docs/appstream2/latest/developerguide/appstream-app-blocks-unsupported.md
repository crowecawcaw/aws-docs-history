# Unsupported Applications

Applications might encounter failures when installing or running in the following
scenarios:

- **Applications with location-based checks during
  installation**: If an application’s installation process
  verifies the actual location of the installed files, it might result in
  a failure. Because WorkSpaces Applications redirects the files to the app block VHD, only
  links to the actual files are maintained at the original
  location.
  If you are uncertain whether your application falls into any of these
  categories, you can use WorkSpaces Applications packaging to create an app block. This process
  involves installing your application(s) on an app block builder instance. In the
  event that your application(s) fail to install on the app block builder
  instance, you can take the following actions:

- Check the logs. The error log file for your app block builder instance
  can be found at C:\AppStream\AppBlocks\errorLog. This log records all
  installation failures, including RegKeys/File operation processing. If
  you see any of the following logs in the errorLog, it indicates that the
  packaging of your application is currently unsupported by the WorkSpaces Applications app
  block builder:

      + "Unable to create symbolic link"
      + "Service doesn't support file renaming"

  If there is no errorLog file, or if this file is empty, then check
  your application installation logs to identify the reason for failures.

- Report a problem. Select the **Report a problem**
  button, which is available on the application builder assistant in the
  app block builder. Selecting this option will gather all the WorkSpaces Applications logs
  from your app block builder instance, and submit them to the WorkSpaces Applications team
  for assistance.
- Create an app block with custom packaging: If you are unable to
  package your applications using the app block builder, you can try to
  create an app block using custom packaging methods. For more
  information, see [Custom App Blocks](custom-app-blocks.md "custom-app-blocks.md").
- If you need more help, contact AWS Support. For more information, see
  [AWS Support Center](https://console.aws.amazon.com/support/home#/ "https://console.aws.amazon.com/support/home#/").
  It is important to consider these potential limitations, and plan accordingly
  when using WorkSpaces Applications packaging for your applications.
