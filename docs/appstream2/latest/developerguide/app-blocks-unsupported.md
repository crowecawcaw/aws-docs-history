# Unsupported Applications

Applications might encounter failures when installing or running in the following
scenarios:

- **Applications requiring reboots after
  installation**: If an application needs to perform additional
  changes or configurations after installation that require a reboot, it
  might fail. Currently, app block builder does not support restart, which
  can prevent the application from completing its required
  post-installation steps.
- **Applications relying on user-specific details**:
  Applications that are intended to be installed only for the currently
  logged-in user on app block builder, or that rely on the logged-in user
  details on app block builder, such as security identifiers (SIDs) during
  installation, might not function correctly on Elastic fleets. This is
  due to the logged-in user changes within the elastic fleet environment.
  Additionally, application redirection does not record all directories
  under %USERPROFILE%. However, you have the option to configure post
  setup scripts to dynamically change your application configuration based
  on environment.
- **Applications relying on machine-specific details**:
  Applications that rely on machine-specific details on app block builder
  during installation, such as network adaptor GUID, might encounter
  issues on Eastic fleets. This is because the machine details, including
  network adaptor GUIDs, can change within the elastic fleet environment.
  To address this, you can configure the post setup scripts to handle the
  configuration of those machine-specific details.
  If you are uncertain whether your application falls into any of these
  categories, you can use AppStream 2.0 packaging to create an app block. This process
  involves installing your application(s) on an app block builder instance. In the
  event that your application(s) fail to install on the app block builder
  instance, you can take the following actions:

- Check the logs. The error log file for your app block builder instance can be
  found at C:\AppStream\AppBlocks\errorLog. This log records all installation
  failures, including registry keys and file operation processing. If you see
  any of the following logs in the errorLog, it indicates that the packaging
  of your application is currently unsupported by the AppStream 2.0 app block
  builder:

      + "Unable to create symbolic link"
      + "Service doesn't support file renaming"

  If there is no errorLog file, or if this file is empty, then check
  your application installation logs to identify the reason for failures.

- Report a problem. Select the **Report a problem** button,
  which is available on the application builder assistant in the app block
  builder. Selecting this option will gather all the AppStream 2.0 logs from your app
  block builder instance, and submit them to the AppStream 2.0 team.
- Create an app block with custom packaging: If you are unable to package your
  applications using the app block builder, you can try to create an app block
  using custom packaging methods. For more information, see [Custom App Blocks](custom-app-blocks.md "custom-app-blocks.md").
- If you need more help, contact AWS Support. For more information, see [AWS Support Center](https://console.aws.amazon.com/support/home#/ "https://console.aws.amazon.com/support/home#/").
  It is important to consider these potential limitations, and plan accordingly
  when using AppStream 2.0 packaging for your applications.
