# Create a Stack in Amazon WorkSpaces Applications

Set up and create a stack to control access to your fleet.

###### Note

You can enable Google Drive, OneDrive, and Application Settings Persistence only
for stacks associated with a Windows fleet. Before you associate an existing stack
with a Linux fleet, please make sure these settings are disabled.

###### To set up and create a stack

1. In the left navigation pane, choose **Stacks**, and then
   choose **Create Stack**.
2. For **Step 1: Stack Details**, Under **Stack
   details**, enter a unique name identifier for the stack.
   Optionally, you can do the following:
   - **Display name** — Enter a name to display for
     the stack (maximum of 100 characters).
   - **Description**— Enter a description for the
     stack (maximum of 256 characters).
   - **Redirect URL** — Specify a URL to which users
     are redirected after their streaming sessions end.
   - **Feedback URL** — Specify a URL to which users
     are redirected after they click the **Send Feedback**
     link to submit feedback about their application streaming experience. If
     you do not specify a URL, this link is not displayed.
   - **Fleet** — Select an existing fleet or create
     a new one to associate with your stack.
   - **Streaming
     Protocol Preference** — Specify the streaming
     protocol you’d like your stack to prefer, UDP or TCP. UDP is currently
     only supported in the Windows native client. For more information, see
     [System Requirements and Feature Support (WorkSpaces Applications Client)](client-system-requirements-feature-support.md "client-system-requirements-feature-support.md").
   - **Tags** — Choose **Add Tag**,
     and type the key and value for the tag. To add more tags, repeat this
     step. For more information, see [Tagging Your Amazon WorkSpaces Applications Resources](tagging-basic.md "tagging-basic.md").
   - **VPC Endpoints (Advanced)** — You can create a
     private link, which is an [interface VPC endpoint](../../../vpc/latest/userguide/vpce-interface.md "../../../vpc/latest/userguide/vpce-interface.md") (interface endpoint), in your
     virtual private cloud (VPC). To start creating the interface endpoint,
     select **Create VPC Endpoint**. Selecting this link
     opens the VPC console. To finish creating the endpoint, follow steps 3
     through 6 in _To create an interface endpoint_, in
     [Tutorial: Creating and Streaming from Interface VPC Endpoints](creating-streaming-from-interface-vpc-endpoints.md "creating-streaming-from-interface-vpc-endpoints.md").

   After you create the interface endpoint, you can use it to keep
   streaming traffic within your VPC.
   - **Embed WorkSpaces Applications (Optional)** — To embed an
     WorkSpaces Applications streaming session in a webpage, specify the domain to host the
     embedded streaming session. Embedded streaming sessions are only
     supported over HTTPS [TCP port 443].

   ###### Note

   You must meet prerequisites and perform additional steps to
   configure embedded WorkSpaces Applications streaming sessions. For more information,
   see [Embed Amazon WorkSpaces Applications Streaming Sessions](embed-streaming-sessions.md "embed-streaming-sessions.md").

3. Choose **Next.**
4. For **Step 2: Enable Storage**, you can provide persistent
   storage for your users by choosing one or more of the following:
   - **Home Folders** — Users can save their files
     to their home folder and access existing files in their home folder
     during application streaming sessions. For information about
     requirements for enabling home folders, see [Enable Home Folders for Your WorkSpaces Applications Users](enable-home-folders.md "enable-home-folders.md").
   - **Google Drive for Google Workspace** — Users
     can link their Google Drive for Google Workspace account to WorkSpaces Applications.
     During application streaming sessions, they can sign in to their Google
     Drive account, save files to Google Drive, and access their existing
     files in Google Drive. You can enable Google Drive for accounts in
     Google Workspace domains only, not for personal Gmail accounts.

   ###### Note

   Enabling Google Drive is not supported for Linux-based stacks or
   stacks associated with multi-session fleets.

   ###### Note

   After you select **Enable Google Drive**, type
   the name of at least one organizational domain that is associated
   with your Google Workspace account. Access to Google Drive during
   application streaming sessions is limited to users that are in the
   domains that you specify. You can specify up to 10 domains. For more
   information about requirements for enabling Google Drive, see [Enable Google Drive for Your WorkSpaces Applications Users](enable-google-drive.md "enable-google-drive.md").
   - **OneDrive for Business** — Users can link
     their OneDrive for Business account to WorkSpaces Applications. During application
     streaming sessions, they can sign in to their OneDrive account, save
     files to OneDrive, and access their existing files in OneDrive. You can
     enable OneDrive for accounts in OneDrive domains only, not for personal
     accounts.

   ###### Note

   Enabling OneDrive is not supported for Linux-based stacks or
   stacks associated with multi-session fleets..

   ###### Note

   After you select **Enable OneDrive**, enter the
   name of least one organizational domain that is associated with your
   OneDrive account. Access to OneDrive during application streaming
   sessions is limited to users that are in the domains that you
   specify. You can specify up to 10 domains. For more information
   about requirements for enabling OneDrive, see [Enable OneDrive for Your WorkSpaces Applications Users](enable-onedrive.md "enable-onedrive.md").

5. Choose **Next**.
6. For **Step 3: User Settings**, configure the following
   settings. When you're done, choose **Review**.

**Clipboard, file transfer, print to local device, and
authentication permissions**:

###### Note

**Smart card sign in for Active Directory** is currently
not available for multi-session fleets.

    * **Clipboard** — By default, users can copy and
     paste data between their local device and streaming applications. You
     can limit Clipboard options so that users can paste data to their remote
     streaming session only or copy data to their local device only. You can
     also disable Clipboard options entirely. Users can still copy and paste
     between applications in their streaming session. You can choose
     **Copy to local device character limit** or
     **Paste to remote session character limit** or both
     to limit the amount of data that users can copy or paste when using the
     clipboard, either in or out of their WorkSpaces Applications streaming session. The value
     can be between 1 and 20,971,520 (20 MB), and defaults to the maximum
     value when unspecified.
    * **File transfer** — By default, users can
     upload and download files between their local device and streaming
     session. You can limit file transfer options so that users can upload
     files to their streaming session only or download files to their local
     device only. You can also disable file transfer entirely.


    ###### Important

    If your users require WorkSpaces Applications file system redirection to access
     local drives and folders during their streaming sessions, you must
     enable both file upload and download. To use file system
     redirection, your users must have WorkSpaces Applications client version 1.0.480 or
     later installed. For more information, see [Enable File System Redirection for Your WorkSpaces Applications Users](enable-file-system-redirection.md "enable-file-system-redirection.md").
    * **Print to local device** — By default, users
     can print to their local device from within a streaming application.
     When they choose **Print** in the application, they can
     download a .pdf file that they can print to a local printer. You can
     disable this option to prevent users from printing to a local
     device.
    * **Password sign in for Active Directory** —
     Users can enter their Active Directory domain password to sign in to an
     WorkSpaces Applications streaming instance that is joined to an Active Directory domain.


    You can also enable **Smart card sign in for Active
     Directory**. At least one authentication must be
     enabled.
    * **Smart card sign in for Active Directory** —
     Users can use a smart card reader and smart card connected to their
     local computer to sign in to an WorkSpaces Applications streaming instance that is joined
     to an Active Directory domain.


    You can also enable **Password sign in for Active
     Directory**. At least one authentication method must be
     enabled.

###### Note

**Clipboard, file transfer, and print to local device
settings** — These settings control only whether users
can use WorkSpaces Applications data transfer features. If your image provides access to a
browser, network printer, or other remote resource, your users might be able
to transfer data to or from their streaming session in other ways.

**Authentication settings** — These
settings control only the authentication method that can be used for Windows
sign in to an WorkSpaces Applications streaming instance (fleet or image builder). They do
not control the authentication method that can be used for in-session
authentication, after a user signs in to a streaming instance. For
information about configuration requirements for using smart cards for
Windows sign in and in-session authentication, see [Smart Cards](feature-support-USB-devices-qualified.md#feature-support-USB-devices-qualified-smart-cards "feature-support-USB-devices-qualified.md#feature-support-USB-devices-qualified-smart-cards").
These settings are not supported for Linux-based stacks.

**Time zone**:

    * **Set time zone automatically for remote session**
     — This setting syncs the time zone used for streaming to match the
     time zone set on the user's device. Users can override this and set
     their own preferred time zone.

**Application settings persistence**:

    * **Enable Application Settings Persistence** —
     Users' application customizations and Windows settings are automatically
     saved after each streaming session and applied during the next session.
     These settings are saved to an Amazon Simple Storage Service (Amazon S3) bucket in your account,
     within the AWS Region in which application settings persistence is
     enabled.
    * **Settings Group** — The settings group
     determines which saved application settings are used for a streaming
     session from this stack. If the same settings group is applied to
     another stack, both stacks use the same application settings. By
     default, the settings group value is the name of the stack.

###### Note

For information about requirements for enabling and administering
application settings persistence, see [Enable Application Settings Persistence for Your WorkSpaces Applications Users](app-settings-persistence.md "app-settings-persistence.md"). 7. For **Step 4: Review**, confirm the details for the stack. To
change the configuration for any section, choose **Edit** and
make the needed changes. After you finish reviewing the configuration details,
choose **Create**.
After the service sets up resources, the **Stacks** page appears. The
status of your new stack appears as **Active** when it is ready to use.
