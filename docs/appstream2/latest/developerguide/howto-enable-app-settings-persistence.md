# How to Enable Application

Settings Persistence

You can enable or disable application settings persistence while creating a stack
or after the stack is created by using the AppStream 2.0 console, AppStream 2.0 API, an AWS SDK,
or the AWS Command Line Interface (CLI). For each AWS Region, persistent
application settings are stored in an S3 bucket in your account.

The first time you enable application settings persistence for a stack in an AWS
Region, AppStream 2.0 creates an S3 bucket in your AWS account in the same Region. The
same bucket stores the application settings VHD file for all users and all stacks in
that AWS Region. For more information, see _Amazon S3 Bucket
Storage_ in [Administer the VHDs for Your Users'
Application Settings](administer-app-settings-vhds.md "administer-app-settings-vhds.md").

###### To enable application settings persistence while creating a stack

- Follow the steps in [Create a Stack in Amazon AppStream 2.0](set-up-stacks-fleets-install.md "set-up-stacks-fleets-install.md"), and make sure that
  **Enable Application Settings Persistence** is
  selected.

###### To enable application settings persistence for an existing stack

1. Open the AppStream 2.0 console at
   [https://console.aws.amazon.com/appstream2](https://console.aws.amazon.com/appstream2 "https://console.aws.amazon.com/appstream2").
2. In the left navigation pane, choose **Stacks**, and
   select the stack for which to enable application settings
   persistence.
3. Below the stacks list, choose **User Settings**,
   **Application Settings Persistence**,
   **Edit**.
4. In the **Application Settings Persistence** dialog box,
   choose **Enable Application Settings Persistence**.
5. Confirm the current settings group or type the name of a new settings
   group. When you're done, choose **Update**.
   New streaming sessions now have application settings persistence enabled.
