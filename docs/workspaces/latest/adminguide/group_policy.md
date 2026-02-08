# Manage your Windows WorkSpaces in WorkSpaces Personal

You can use Group Policy Objects (GPOs) to apply settings to manage Windows WorkSpaces or users
that are part of your Windows WorkSpaces directory.

###### Note

- If you use Microsoft Entra ID or Custom WorkSpaces directory, you can manage
  users and groups with Microsoft Entra ID or your Identity Providers. For more inforamtion,
  see [Create a dedicated Microsoft Entra ID directory with WorkSpaces Personal](launch-entra-id.md "launch-entra-id.md").
- Linux instances do not adhere to Group Policy. For information about managing Amazon Linux
  WorkSpaces, see [Manage your Amazon Linux 2 WorkSpaces in WorkSpaces Personal](manage_linux_workspace.md "manage_linux_workspace.md").
  Amazon recommends that you create an organizational unit for your WorkSpaces Computer Objects and an
  organizational unit for your WorkSpaces User Objects.

To use the Group Policy settings that are specific to Amazon WorkSpaces, you must install the
Group Policy administrative template for the protocol or protocols that you are using,
either PCoIP or DCV.

###### Warning

Group Policy settings can affect the experience of your WorkSpace users as
follows:

- **Implementing an interactive logon message to display a
  logon banner prevents users from being able to access their
  WorkSpaces.** The interactive logon message Group Policy setting is not
  currently supported by PCoIP WorkSpaces. The logon message is supported on DCV WorkSpaces,
  and users have to login again after accepting the logon banner. Logon messages are not
  supported when Certificate-Based Logon is enabled.
- **Disabling removable storage through Group Policy
  settings causes a login failure** that results in users being
  logged in to temporary user profiles with no access to drive D.
- **Removing users from the Remote Desktop Users local group
  through Group Policy settings prevents those users from being able to
  authenticate** through the WorkSpaces client applications. For more
  information about this Group Policy setting, see [Allow log on through Remote Desktop Services](https://docs.microsoft.com/windows/security/threat-protection/security-policy-settings/allow-log-on-through-remote-desktop-services "https://docs.microsoft.com/windows/security/threat-protection/security-policy-settings/allow-log-on-through-remote-desktop-services") in the Microsoft
  documentation.
- **If you remove the built-in Users group from the
  **Allow log on locally** security policy, your PCoIP
  WorkSpaces users won't be able to connect to their WorkSpaces through the WorkSpaces client
  applications.** Your PCoIP WorkSpaces also won't receive updates to the
  PCoIP agent software. PCoIP agent updates might contain security and other
  fixes, or they might enable new features for your WorkSpaces. For more information
  about working with this security policy, see [Allow log on locally](https://docs.microsoft.com/windows/security/threat-protection/security-policy-settings/allow-log-on-locally "https://docs.microsoft.com/windows/security/threat-protection/security-policy-settings/allow-log-on-locally") in the Microsoft documentation.
- Group Policy settings can be used to restrict drive access. **If you configure Group Policy settings to restrict access to
  drive C or to drive D, users can't access their WorkSpaces.** To prevent
  this issue from occurring, make sure that your users can access drive C and
  drive D.
- **The WorkSpaces audio-in feature requires local logon access
  inside the WorkSpace.** The audio-in feature is enabled by default
  for Windows WorkSpaces. However, if you have a Group Policy setting that restricts
  users' local logon in their WorkSpaces, audio-in won't work on your WorkSpaces. If you
  remove that Group Policy setting, the audio-in feature is enabled after the next
  reboot of the WorkSpace. For more information about this Group Policy setting,
  see [Allow log on locally](https://docs.microsoft.com/windows/security/threat-protection/security-policy-settings/allow-log-on-locally "https://docs.microsoft.com/windows/security/threat-protection/security-policy-settings/allow-log-on-locally") in the Microsoft documentation.

For more information about enabling or disabling audio-in redirection, see
[Configure audio-in redirection for
PCoIP](#gp_audio "#gp_audio") or [Configure audio-in redirection for
DCV](#gp_audio_in_wsp "#gp_audio_in_wsp").

- Using Group Policy to set the Windows power plan to
  **Balanced** or **Power saver** might
  cause your WorkSpaces to sleep when they're left idle. We strongly recommend using
  Group Policy to set the Windows power plan to **High
  performance**. For more information, see [My Windows WorkSpace goes to
  sleep when it's left idle](amazon-workspaces-troubleshooting.md#windows_workspace_sleeps_when_idle "amazon-workspaces-troubleshooting.md#windows_workspace_sleeps_when_idle").
- Some Group Policy settings force users to log off when they are disconnected
  from a session. Any applications that users have open on their WorkSpaces are
  closed.
- "Set time limit for active but idle Remote Desktop Services sessions" is
  currently not supported on DCV WorkSpaces. Avoid using it during DCV sessions as it
  causes a disconnect even when there is activity and the session is not
  idle.
  For information about using the Active Directory administration tools to work with GPOs,
  see [Set up Active Directory Administration Tools for WorkSpaces Personal](directory_administration.md "directory_administration.md").

###### Contents

- [Install the Group Policy
  administrative template files for DCV](group_policy.md#gp_install_template_wsp "group_policy.md#gp_install_template_wsp")
- [Manage Group Policy settings for
  DCV](group_policy.md#gp_configurations_dcv "group_policy.md#gp_configurations_dcv")
- [Install the Group Policy administrative template
  for PCoIP](group_policy.md#gp_install_template "group_policy.md#gp_install_template")
- [Manage Group Policy settings for PCoIP](group_policy.md#gp_configurations_pcoip "group_policy.md#gp_configurations_pcoip")
- [Set the maximum lifetime for a Kerberos
  ticket](group_policy.md#gp_kerberos_ticket "group_policy.md#gp_kerberos_ticket")
- [Configure device proxy server settings for internet
  access](group_policy.md#gp_device_proxy "group_policy.md#gp_device_proxy")
  - [Proxying desktop traffic](group_policy.md#w2aac11c29c11c27c15 "group_policy.md#w2aac11c29c11c27c15")
  - [Recommendation on the use of proxy servers](group_policy.md#w2aac11c29c11c27c17 "group_policy.md#w2aac11c29c11c27c17")

- [Enable Zoom Meeting Media Plugin support](group_policy.md#zoom-integration "group_policy.md#zoom-integration")
  - [Enable Zoom Meeting Media Plugin for DCV](group_policy.md#zoom-wsp "group_policy.md#zoom-wsp")
    - [Prerequisites](group_policy.md#zoom-integ-prerequisites-wsp "group_policy.md#zoom-integ-prerequisites-wsp")
    - [Before you begin](group_policy.md#zoom-begin-wsp "group_policy.md#zoom-begin-wsp")
    - [Installing the Zoom components](group_policy.md#installing-zoom-wsp "group_policy.md#installing-zoom-wsp")

  - [Enable Zoom Meeting Media Plugin for PCoIP](group_policy.md#zoom-pcoip "group_policy.md#zoom-pcoip")
    - [Prerequisites](group_policy.md#zoom-integ-prerequisites-pcoip "group_policy.md#zoom-integ-prerequisites-pcoip")
    - [Create the registry key on a
      Windows WorkSpaces host](group_policy.md#zoom-integ-create-registry-key "group_policy.md#zoom-integ-create-registry-key")
    - [Troubleshooting](group_policy.md#zoom-integ-troubleshoot "group_policy.md#zoom-integ-troubleshoot")

## Install the Group Policy administrative

template files for DCV

To use the Group Policy settings that are specific to WorkSpaces when using DCV, you must add the Group Policy administrative template
`wsp.admx` and `wsp.adml` files for DCV
to the Central Store of the domain controller for your WorkSpaces directory. For more
information about `.admx` and `.adml` files, see
[How to create and manage the Central Store for Group Policy Administrative
Templates in Windows](https://support.microsoft.com/help/3087759/how-to-create-and-manage-the-central-store-for-group-policy-administra "https://support.microsoft.com/help/3087759/how-to-create-and-manage-the-central-store-for-group-policy-administra").

The following procedure describes how to create the Central Store and add the
administrative template files to it. Perform the following procedure on a directory
administration WorkSpace or Amazon EC2 instance that is joined to your WorkSpaces
directory.

###### To install the Group Policy administrative template files for DCV

1. From a running Windows WorkSpace, make a copy of the
   `wsp.admx` and `wsp.adml` files in the
   `C:\Program Files\Amazon\WSP` directory.
2. On a directory administration WorkSpace or an Amazon EC2 instance that is joined to
   your WorkSpaces directory, open Windows File Explorer, and in the address bar, enter
   your organization's fully qualified domain name (FQDN), such as
   `\\example.com`.
3. Open the `sysvol` folder.
4. Open the folder with the `FQDN`
   name.
5. Open the `Policies` folder. You should now be in
   `\\`FQDN`\sysvol\`FQDN`\Policies`.
6. If it doesn't already exist, create a folder named
   `PolicyDefinitions`.
7. Open the `PolicyDefinitions` folder.
8. Copy the `wsp.admx` file into the
   `\\`FQDN`\sysvol\`FQDN`\Policies\PolicyDefinitions`
   folder.
9. Create a folder named `en-US` in the
   `PolicyDefinitions` folder.
10. Open the `en-US` folder.
11. Copy the `wsp.adml` file into the
    `\\`FQDN`\sysvol\`FQDN`\Policies\PolicyDefinitions\en-US`
    folder.

###### To verify that the administrative template files are correctly installed

1. On a directory administration WorkSpace or an Amazon EC2 instance that is joined to
   your WorkSpaces directory, open the Group Policy Management tool
   (**gpmc.msc**).
2. Expand the forest
   (**Forest:`FQDN`**).
3. Expand **Domains**.
4. Expand your FQDN (for example, `example.com`).
5. Expand **Group Policy Objects**.
6. Select **Default Domain Policy**, open the context
   (right-click) menu, and choose **Edit**.

###### Note

If the domain backing the WorkSpaces is an AWS Managed Microsoft AD directory, you cannot
use the Default Domain Policy to create your GPO. Instead, you must create
and link the GPO under the domain container that has delegated
privileges.

When you create a directory with AWS Managed Microsoft AD, Directory Service creates a
`yourdomainname` organizational unit (OU) under
the domain root. The name of this OU is based on the NetBIOS name that you
typed when you created your directory. If you didn't specify a NetBIOS name,
it will default to the first part of your Directory DNS name (for example,
in the case of `corp.example.com`, the NetBIOS name is
`corp`).

To create your GPO, instead of selecting **Default Domain
Policy**, select the `yourdomainname`
OU (or any OU under that one), open the context (right-click) menu, and
choose **Create a GPO in this domain, and Link it here**.

For more information about the `yourdomainname`
OU, see [What Gets Created](../../../directoryservice/latest/admin-guide/ms_ad_getting_started_what_gets_created.md "../../../directoryservice/latest/admin-guide/ms_ad_getting_started_what_gets_created.md") in the
_AWS Directory Service Administration Guide_. 7. In the Group Policy Management Editor, choose **Computer
Configuration**, **Policies**,
**Administrative Templates**, **Amazon**,
and **DCV**. 8. You can now use this **DCV** Group Policy object to modify
the Group Policy settings that are specific to WorkSpaces when using
DCV.

## Manage Group Policy settings for

DCV

###### To use Group Policy settings to manage your Windows WorkSpaces that use DCV

1. Make sure that the most recent [WorkSpaces Group Policy administrative template for DCV](#gp_install_template_wsp "#gp_install_template_wsp") is
   installed in the Central Store of the domain controller for your WorkSpaces
   directory.
2. Verify the administrative template files are correctly installed. For more information,
   see [To verify that the administrative template files are correctly installed](#verify-admin-template "#verify-admin-template").

By default, WorkSpaces enables Basic remote printing, which offers limited printing
capabilities because it uses a generic printer driver on the host side to ensure
compatible printing.

Advanced remote printing for Windows clients connecting to Windows WorkSpaces
lets you use specific features of your printer, such as double-sided printing, but
it requires installation of the matching printer drivers on the host side and the
client side.

You can use Group Policy settings to configure printer support as needed.

| Basic vs. Advanced Printing | Aspect                 | Basic Printing                                                        | Advanced Printing |
| --------------------------- | ---------------------- | --------------------------------------------------------------------- | ----------------- |
| **Driver Used**             | Generic XPS driver     | Printer-specific driver                                               |
| **Driver Installation**     | Automatic              | Manual (host and client)                                              |
| **Features**                | Standard printing only | Full printer features (duplex, paper tray selection, finishing, etc.) |

**When to use Advanced Printing:** - Double-sided (duplex) printing

- Specific paper tray selection - Finishing options (stapling, hole-punching) - Label
  printing (e.g., Zebra printers) - Color management and other advanced features of
  a printer.

#### Configure Printer Support

###### To configure printer support

1. In the Group Policy Management Editor, choose **Computer
   Configuration**, **Policies**,
   **Administrative Templates**, **Amazon**,
   and **WSP**.
2. Open the **Configure remote printing**
   setting.
3. In the **Configure remote printing** dialog box, do
   one of the following:
   - **For Basic Printing:** choose
     **Enabled**. To automatically
     use the client computer's current default printer, select
     **Map local default printer to the remote host.**
   - **For Advanced Printing:** Choose
     **Enabled**, then choose **Enable
     Advanced Printing**.To automatically use the client
     computer's current default printer, select **Map local
     default printer to the remote host**. Once the policy
     is enabled, you will need to install matching printer
     drivers on the host and client side.
   - To disable printing, choose
     **Disabled**.

4. Choose **OK**.
5. The Group Policy setting change takes effect after the next Group
   Policy update for the WorkSpace and after the WorkSpace session is
   restarted. To apply the Group Policy changes, do one of the
   following:
   - Reboot the WorkSpace (in the Amazon WorkSpaces console, select the
     WorkSpace, then choose **Actions**,
     **Reboot WorkSpaces**).
   - In an administrative command prompt, enter `gpupdate
/force`.

#### Configure Advanced Printer Redirection

###### Prerequisites

1. **WorkSpaces Host Agent:** Version 2.2.0.2116 or later
2. **Windows Client:** Version 5.31.0 or later
3. **Printer drivers:** Matching printer drivers must be
   installed on both the WorkSpace and the client device

###### Note

Advanced printing is only supported on Windows
clients connecting to Windows WorkSpaces. MacOS, Linux, and Web clients
will use basic printing.

#### Driver Version Matching

When Advanced printing is selected, three driver validation modes
are supported:

| Driver Validation Modes      | Mode                                         | Behavior                                          | Use When |
| ---------------------------- | -------------------------------------------- | ------------------------------------------------- | -------- |
| \*_Name Only_<br>• (Default) | Matches driver name only, ignores version    | Maximum compatibility needed                      |
| **Partial Match**            | Matches Major.Minor version (e.g., 10.6.x.x) | Balancing compatibility and features              |
| **Exact Match**              | Requires exact version match                 | Specialized printers (e.g., Zebra label printers) |

**To configure validation mode**, set name only, partial match,
or exact match in the printer driver validation dropdown in the GPO.

###### Note

When driver validation fails, WorkSpaces automatically
falls back to basic printing.

###### Verify Configuration

1. Connect to the WorkSpace.
2. Open **Settings** > **Devices** >
   **Printers & scanners**.
3. Verify your local printer appears with "Redirected" prefix.
4. Print a test document and click Printer Properties to verify advanced options are available.

#### Troubleshooting

**Advanced features not available**: - Verify “Enable Advanced Printing” is selected in the GPO - Check driver
versions match according to your validation mode - Consider using partial validation mode instead of exact. Make
sure to restart for any changes on the GPO to take effect.

**Printer not appearing**: - Verify **Configure remote printing** is **Enabled**

- Ensure printer is connected to client device - Restart WorkSpace session

**Print jobs fail**: - Check driver versions on both client and WorkSpace -
Review logs at: `C:\ProgramData\Amazon\WSP\Logs\agentsession.log` - Look for
"Advanced print is enabled" in logs

Enable detailed logging: In Group Policy, set Configure log verbosity to debug under **Computer Configuration**

> **Policies** > **Administrative Templates** > **Amazon** > **WSP**.

By default, WorkSpaces supports two-way (copy/paste) clipboard redirection. For
Windows WorkSpaces, you can use Group Policy settings to disable this feature or
configure the direction where clipboard redirection is allowed.

###### To configure clipboard redirection for Windows WorkSpaces

1. In the Group Policy Management Editor, choose **Computer
   Configuration**, **Policies**,
   **Administrative Templates**, **Amazon**,
   and **WSP**.
2. Open the **Configure clipboard redirection**
   setting.
3. In the **Configure clipboard redirection** dialog
   box, choose **Enabled** or
   **Disabled**.

When **Configure clipboard redirection** is
**Enabled**, the following **Clipboard
redirection options** will become available:

    * Choose **Copy and Paste** to allow two-way
     clipboard copy and paste redirection.
    * Choose **Copy Only** to allow copying data
     from the server clipboard to the client clipboard only.
    * Choose **Paste Only** to allow pasting data
     from the client clipboard to the server clipboard only.

4. Choose **OK**.
5. The Group Policy setting change takes effect after the next Group
   Policy update for the WorkSpace and after the WorkSpace session is
   restarted. To apply the Group Policy changes, do one of the
   following:
   - Reboot the WorkSpace (in the Amazon WorkSpaces console, select the
     WorkSpace, then choose **Actions**,
     **Reboot WorkSpaces**).
   - In an administrative command prompt, enter `gpupdate
/force`.

###### Known limitation

With clipboard redirection enabled on the WorkSpace, if you copy content
that is larger than 890 KB from a Microsoft Office application, the
application might become slow or unresponsive for up to 5 seconds.

When you lose network connectivity, your active WorkSpaces client session is
disconnected. WorkSpaces client applications for Windows and macOS attempt to
reconnect the session automatically if network connectivity is restored within a
certain amount of time. The default session resume timeout is 20 minutes (1200
seconds), but you can modify that value for WorkSpaces that are controlled by your
domain's Group Policy settings.

###### To set the automatic session resume timeout value

1.  In the Group Policy Management Editor, choose **Computer
    Configuration**, **Policies**,
    **Administrative Templates**, **Amazon**,
    and **WSP**.
2.  Open the **Enable/disable automatic reconnect**
    setting.
3.  In the **Enable/disable automatic reconnect** dialog
    box, choose **Enabled**, and then set
    **Reconnect timeout (seconds)** to the desired
    timeout in seconds.
4.  Choose **OK**.
5.  The Group Policy setting change takes effect after the next Group
    Policy update for the WorkSpace and after the WorkSpace session is
    restarted. To apply the Group Policy changes, do one of the
    following:

        * Reboot the WorkSpace (in the Amazon WorkSpaces console, select the
         WorkSpace, then choose **Actions**,
         **Reboot WorkSpaces**).
        * In an administrative command prompt, enter `gpupdate
         /force`.

    By default, WorkSpaces supports redirecting data from a local camera. If needed for
    Windows WorkSpaces, you can use Group Policy settings to disable this feature.

###### To configure video-in redirection for Windows WorkSpaces

1.  In the Group Policy Management Editor, choose **Computer
    Configuration**, **Policies**,
    **Administrative Templates**, **Amazon**,
    and **WSP**.
2.  Open the **Enable/disable video-in redirection**
    setting.
3.  In the **Enable/disable video-in redirection** dialog
    box, choose **Enabled** or
    **Disabled**.
4.  Choose **OK**.
5.  The Group Policy setting change takes effect after the next Group
    Policy update for the WorkSpace and after the WorkSpace session is
    restarted. To apply the Group Policy changes, do one of the
    following:

        * Reboot the WorkSpace (in the Amazon WorkSpaces console, select the
         WorkSpace, then choose **Actions**,
         **Reboot WorkSpaces**).
        * In an administrative command prompt, enter `gpupdate
         /force`.

    By default, WorkSpaces supports redirecting data from a local microphone. If needed
    for Windows WorkSpaces, you can use Group Policy settings to disable this feature.

###### To configure audio-in redirection for Windows WorkSpaces

1.  In the Group Policy Management Editor, choose **Computer
    Configuration**, **Policies**,
    **Administrative Templates**, **Amazon**,
    and **WSP**.
2.  Open the **Enable/disable audio-in redirection**
    setting.
3.  In the **Enable/disable audio-in redirection** dialog
    box, choose **Enabled** or
    **Disabled**.
4.  Choose **OK**.
5.  The Group Policy setting change takes effect after the next Group
    Policy update for the WorkSpace and after the WorkSpace session is
    restarted. To apply the Group Policy changes, do one of the
    following:

        * Reboot the WorkSpace (in the Amazon WorkSpaces console, select the
         WorkSpace, then choose **Actions**,
         **Reboot WorkSpaces**).
        * In an administrative command prompt, enter `gpupdate
         /force`.

    By default, WorkSpaces redirects data to a local speaker. If needed for Windows
    WorkSpaces, you can use Group Policy settings to disable this feature.

###### To configure audio-out redirection for Windows WorkSpaces

1.  In the Group Policy Management Editor, choose **Computer
    Configuration**, **Policies**,
    **Administrative Templates**, **Amazon**,
    and **WSP**.
2.  Open the **Enable/disable audio-out redirection**
    setting.
3.  In the **Enable/disable audio-out redirection**
    dialog box, choose **Enabled** or
    **Disabled**.
4.  Choose **OK**.
5.  The Group Policy setting change takes effect after the next Group
    Policy update for the WorkSpace and after the WorkSpace session is
    restarted. To apply the Group Policy changes, do one of the
    following:

        * Reboot the WorkSpace. In the Amazon WorkSpaces console, select the
         WorkSpace, then choose **Actions** >
         **Reboot WorkSpaces**.
        * In an administrative command prompt, enter `gpupdate
         /force`.

    By default, the time within a Workspace is set to mirror the time zone of the
    client that is being used to connect to the WorkSpace. This behavior is
    controlled through time zone redirection. You might want to turn off time zone
    direction for various reasons. For example:

- Your company wants all employees to work in a certain time zone (even
  if some employees are in other time zones).
- You have scheduled tasks in a WorkSpace that are meant to run at a
  certain time in a specific time zone.
- Your users who travel a lot want to keep their WorkSpaces in one time zone
  for consistency and personal preference.
  If needed for Windows WorkSpaces, you can use Group Policy settings to disable this
  feature.

###### To disable time zone redirection for Windows WorkSpaces

1. In the Group Policy Management Editor, choose **Computer
   Configuration**, **Policies**,
   **Administrative Templates**, **Amazon**,
   and **WSP**.
2. Open the **Enable/disable time zone redirection**
   setting.
3. In the **Enable/disable time zone redirection**
   dialog box, choose **Disabled**.
4. Choose **OK**.
5. The Group Policy setting change takes effect after the next Group
   Policy update for the WorkSpace and after the WorkSpace session is
   restarted. To apply the Group Policy changes, do one of the
   following:
   - Reboot the WorkSpace (in the Amazon WorkSpaces console, select the
     WorkSpace, then choose **Actions**,
     **Reboot WorkSpaces**).
   - In an administrative command prompt, enter `gpupdate
/force`.

6. Set the time zone for the WorkSpaces to the desired time zone.
   The time zone of the WorkSpaces is now static and no longer mirrors the time zone
   of the client machines.

For DCV, data in transit is encrypted using TLS 1.2 encryption. By default,
all of the following ciphers are allowed for encryption, and the client and
server negotiate which cipher to use:

- ECDHE-RSA-AES128-GCM-SHA256
- ECDHE-ECDSA-AES128-GCM-SHA256
- ECDHE-RSA-AES256-GCM-SHA384
- ECDHE-ECDSA-AES256-GCM-SHA384
- ECDHE-RSA-AES128-SHA256
- ECDHE-RSA-AES256-SHA384
  For Windows WorkSpaces, you can use Group Policy settings to modify the TLS
  Security Mode and to add new or block certain cipher suites. A detailed
  explanation of these settings and the supported cipher suites is provided in the
  **Configure security settings Group Policy** dialog
  box.

###### To configure DCV security settings

1.  In the Group Policy Management Editor, choose **Computer
    Configuration**, **Policies**,
    **Administrative Templates**, **Amazon**,
    and **WSP**.
2.  Open **Configure security settings**.
3.  In the **Configure security settings** dialog box,
    choose **Enabled**. Add cipher suites that you want to
    allow and remove cipher suites that you want to block. For more
    information about these settings, see the descriptions provided in the
    **Configure security settings** dialog box.
4.  Choose **OK**.
5.  The Group Policy setting change takes effect after the next Group
    Policy update for the WorkSpace, and after you restart the WorkSpace
    session. To apply the Group Policy changes, do one of the
    following:

        * To reboot the WorkSpace, in the Amazon WorkSpaces console, select the
         WorkSpace, then choose **Actions**,
         **Reboot WorkSpaces**.
        * In an administrative command prompt, enter `gpupdate
         /force`.

    By default, support for WorkSpaces extensions is disabled. If needed, you can
    configure your WorkSpace to use extensions in the following ways:

- Server and client – Enable extensions for both server and
  client
- Server only – Enable extensions for server only
- Client only – Enable extensions for client only
  For Windows WorkSpaces, you can use Group Policy settings to configure the use of
  extensions.

###### To configure extensions for DCV

1.  In the Group Policy Management Editor, choose **Computer
    Configuration**, **Policies**,
    **Administrative Templates**, **Amazon**,
    and **WSP**.
2.  Open the **Configure extensions** setting.
3.  In the **Configure extensions** dialog box, choose
    **Enabled** and then set the desired support
    option. Choose **Client Only**, **Server and
    Client**, or **Server only**.
4.  Choose **OK**.
5.  The Group Policy setting change takes effect after the next Group
    Policy update for the WorkSpace and after you restart the WorkSpace
    session. To apply the Group Policy changes, do one of the
    following:

        * Reboot the WorkSpace. In the Amazon WorkSpaces console, select the
         WorkSpace, then choose **Actions**,
         **Reboot WorkSpaces**.
        * In an administrative command prompt, enter `gpupdate
         /force`.

    By default, Amazon WorkSpaces are not enabled to support the use of smart cards for
    either _pre-session authentication_ or _in-session
    authentication_. Pre-session authentication refers to smart card
    authentication that's performed while users are logging in to their WorkSpaces.
    In-session authentication refers to authentication that's performed after
    logging in.

If needed, you can enable pre-session and in-session authentication for
Windows WorkSpaces by using Group Policy settings. Pre-session authentication must
also be enabled through your AD Connector directory settings by using the
**EnableClientAuthentication** API action or the
**enable-client-authentication** AWS CLI command. For more
information, see [Enable Smart Card Authentication for AD Connector](../../../directoryservice/latest/admin-guide/ad_connector_clientauth.md "../../../directoryservice/latest/admin-guide/ad_connector_clientauth.md") in the
_AWS Directory Service Administration Guide_.

###### Note

To enable the use of smart cards with Windows WorkSpaces, additional steps are
required. For more information, see [Use smart cards for authentication in WorkSpaces Personal](smart-cards.md "smart-cards.md").

###### To configure smart card redirection for Windows WorkSpaces

1. In the Group Policy Management Editor, choose **Computer
   Configuration**, **Policies**,
   **Administrative Templates**, **Amazon**,
   and **WSP**.
2. Open the **Enable/disable smart card redirection**
   setting.
3. In the **Enable/disable smart card redirection**
   dialog box, choose **Enabled** or
   **Disabled**.
4. Choose **OK**.
5. The Group Policy setting change takes effect after the WorkSpace
   session is restarted. To apply the Group Policy change, reboot the
   WorkSpace (in the Amazon WorkSpaces console, select the WorkSpace, then choose
   **Actions**, **Reboot
   WorkSpaces**).
   By default, Amazon WorkSpaces enables WebAuthn redirection, allowing users to use their local FIDO2-compatible security keys and biometric authenticators with applications running inside their WorkSpace. This feature securely redirects authentication requests from applications in the WorkSpace to the user's local device, providing seamless access to authentication methods including Yubikeys and Windows Hello.

Amazon WorkSpaces supports two versions of WebAuthn redirection:

- **Standard WebAuthn** - Requires a browser extension, supported on Windows and Linux WorkSpaces, for browser-based apps
- **Enhanced WebAuthn** - No browser extension required, with additional native application support, supported on Windows WorkSpaces only

#### Standard WebAuthn redirection

Standard WebAuthn redirection requires a browser extension to facilitate the redirection of WebAuthn prompts to the client device.

##### Version requirements

- **Windows WorkSpaces**: DCV host agent version 2.0.0.1425 or higher
- **Client versions:**
  - Windows client: 5.19.0 or above
  - Mac client: 5.19.0 or above
  - Linux client: 2024.0 or above

##### Supported browsers on WorkSpaces

- Google Chrome 116+
- Microsoft Edge 116+

#### Enhanced WebAuthn redirection

Enhanced WebAuthn redirection eliminates the need for a browser extension and provides support for WebAuthn authentication in native Windows applications that support WebAuthn authentication.

##### Version requirements

- **Windows WorkSpaces**: DCV host agent version 2.1.0.2000 or higher
- **Client versions:**
  - Windows client: 5.29.0 or above
  - Mac client: 5.29.0 or above

##### Key benefits

- No browser extension required
- Improved performance
- Support for WebAuthn in native Windows applications
- Seamless authentication experience across browsers and desktop applications

##### Supported browsers on WorkSpaces

- Google Chrome 116+
- Microsoft Edge 116+

#### Configure WebAuthn redirection

###### To configure WebAuthn redirection for Windows WorkSpaces

1. In the Group Policy Management Editor, choose **Computer
   Configuration**, **Policies**,
   **Administrative Templates**, **Amazon**,
   and **DCV**.
2. Open the **Configure WebAuthn redirection** setting.
3. In the **Configure WebAuthn redirection** dialog box,
   choose **Enabled** or **Disabled**.
4. Choose **OK**.
5. The Group Policy setting change takes effect after the WorkSpace session is
   restarted. To apply the Group Policy changes, reboot the WorkSpace by going to the
   Amazon WorkSpaces console and selecting the WorkSpace. Then, choose **Actions**,
   **Reboot WorkSpaces**.

###### Note

This Group Policy setting enables WebAuthn redirection. The version used (Standard or Enhanced) depends on your host agent version and operating system support.

#### Configure WebAuthn process compatibility

When WebAuthn redirection is enabled, you can configure which applications and processes are allowed to use WebAuthn redirection through the **WebAuthn Process Compatibility List**.

##### Default process compatibility list

By default, the following processes are enabled for WebAuthn redirection:

```
['chrome.exe','msedge.exe','island.exe','firefox.exe','dcvwebauthnnativemsghost.exe','msedgewebview2.exe','Microsoft.AAD.BrokerPlugin.exe']
```

##### Required process for Standard WebAuthn

- `dcvwebauthnnativemsghost.exe` - This process is **required** for Standard WebAuthn functionality and must remain in the compatibility list when using Standard WebAuthn.

###### To configure the WebAuthn process compatibility list

1. In the Group Policy Management Editor, choose **Computer Configuration**, **Policies**, **Administrative Templates**, **Amazon**, and **DCV**.
2. Open the **Configure WebAuthn Redirection** setting.
3. Choose **Enabled**.
4. In the **WebAuthn process compatibility list** field, specify the list of process names that are compatible with WebAuthn redirection.
   - Use the default list as a starting point
   - Add additional process names as needed for your environment

5. Choose **OK**.
6. The Group Policy setting change takes effect after the WorkSpace session is restarted.

##### Process compatibility list guidelines

- **For Standard WebAuthn**: Always include `dcvwebauthnnativemsghost.exe` in the list
- **Custom Applications**: Add any additional `.exe` process names that need WebAuthn support in your environment
- **Format**: Use comma-separated process names enclosed in square brackets, with each process name in single quotes

##### Example custom process list

```
['chrome.exe','msedge.exe','firefox.exe','dcvwebauthnnativemsghost.exe','msedgewebview2.exe','Microsoft.AAD.BrokerPlugin.exe','myapp.exe','customapplication.exe']
```

#### Transitioning from Standard to Enhanced WebAuthn

When upgrading from Standard WebAuthn to Enhanced WebAuthn, **users will need to uninstall or disable the Amazon DCV WebAuthn Redirection browser extension** they previously installed for Standard WebAuthn before using Enhanced WebAuthn.

##### Why this step is important

- Enhanced WebAuthn handles redirection natively without browser extensions
- Leaving the extension enabled will default to Standard WebAuthn redirection

#### Installing the Amazon DCV WebAuthn Redirection Extension (Standard WebAuthn Only)

###### Note

This section only applies to Standard WebAuthn. Enhanced WebAuthn does not require browser extensions.

Users will need to install the Amazon DCV WebAuthn Redirection Extension to use Standard WebAuthn after the feature is enabled by doing either of the following:

- Users will be prompted to enable the browser extension in their browser.

###### Note

This is a one-time browser prompt. Your users will get the notification when you update the DCV agent version to 2.0.0.1425 or higher.
If your end users don’t need the WebAuthn redirection, they can just remove the extension from the browser. You can also block the WebAuthn Redirection Extension
installation prompt using GPO policy.

- You can force install the redirection extension for your users using GPO policy. If you enable the GPO policy, the extension will
  automatically be installed when your users launch the supported browsers with internet access.
- Users can install the extension manually with [Microsoft Edge Add-ons](https://microsoftedge.microsoft.com/addons/detail/dcv-webauthn-redirection-/ihejeaahjpbegmaaegiikmlphghlfmeh "https://microsoftedge.microsoft.com/addons/detail/dcv-webauthn-redirection-/ihejeaahjpbegmaaegiikmlphghlfmeh") or the
  [Chrome Web Store](https://chromewebstore.google.com/detail/dcv-webauthn-redirection/mmiioagbgnbojdbcjoddlefhmcocfpmn?pli=1 "https://chromewebstore.google.com/detail/dcv-webauthn-redirection/mmiioagbgnbojdbcjoddlefhmcocfpmn?pli=1").

##### Understanding WebAuthn Redirection Extension Native Messaging

WebAuthn redirection in Chrome and Edge browsers utilizes a browser
extension and a native messaging host. The native messaging host is a
component that allows communication between the extension and the host
application. In a typical configuration, all native messaging hosts are
permitted by the browser by default. However, you can choose to use a
native messaging blocklist, where the value of \* means that all native
messaging hosts are denied unless explicitly allowed. In this case, you
need to enable the Amazon DCV WebAuthn Redirection native messaging host
by explicitly specifying the value
`com.dcv.webauthnredirection.nativemessagehost` in the
allow list.

For more information, follow the guidance for your browser:

- For Google Chrome, see [Native Messaging allowed hosts](https://support.google.com/chrome/a/answer/2657289#zippy=%2Cnative-messaging-allowed-hosts "https://support.google.com/chrome/a/answer/2657289#zippy=%2Cnative-messaging-allowed-hosts").
- For Microsoft Edge, see [Native Messaging](https://learn.microsoft.com/en-us/deployedge/microsoft-edge-policies#native-messaging "https://learn.microsoft.com/en-us/deployedge/microsoft-edge-policies#native-messaging").

##### Manage and install the browser extension using Group Policy

You can install the Amazon DCV WebAuthn Redirection Extension using Group Policy, either
centrally from your domain for session hosts that are joined to an Active Directory (AD) domain
or using the Local Group Policy Editor for each session host. This process will change depending on
which browser you're using.

###### For Microsoft Edge

1. Download and install the
   [Microsoft Edge administrative template](https://learn.microsoft.com/en-us/deployedge/configure-microsoft-edge#1-download-and-install-the-microsoft-edge-administrative-template "https://learn.microsoft.com/en-us/deployedge/configure-microsoft-edge#1-download-and-install-the-microsoft-edge-administrative-template").
2. On a directory administration WorkSpace or an Amazon EC2 instance that is
   joined to your WorkSpaces directory, open the Group Policy Management tool
   (**gpmc.msc**).
3. Expand the forest
   (**Forest:`FQDN`**).
4. Expand **Domains**.
5. Expand your FQDN (for example,
   `example.com`).
6. Expand **Group Policy Objects**.
7. Select **Default Domain Policy**, open the context
   (right-click) menu, and choose **Edit**.
8. Choose **Computer Configuration** ,
   **Administrative Templates**, **Microsoft Edge**,
   and **Extensions**
9. Open **Configure extension management settings** and set it
   to **Enabled**.
10. Under **Configure extension management settings**, enter the following:

```
{"ihejeaahjpbegmaaegiikmlphghlfmeh":{"installation_mode":"force_installed","update_url":"https://edge.microsoft.com/extensionwebstorebase/v1/crx"}}
```

11. Choose **OK**.
12. The Group Policy setting change takes effect after the WorkSpace session is
    restarted. To apply the Group Policy changes, reboot the WorkSpace by going to the
    Amazon WorkSpaces console and selecting the WorkSpace. Then, choose **Actions**,
    **Reboot WorkSpaces**).

###### Note

You can block the installation of the extension by applying the following configuration management setting:

```
{"ihejeaahjpbegmaaegiikmlphghlfmeh":{"installation_mode":"blocked","update_url":"https://edge.microsoft.com/extensionwebstorebase/v1/crx"}}
```

###### For Google Chrome

1. Download and install the Google Chrome administrative template. For more information, see
   [Set Chrome Browser policies on managed PCs](https://support.google.com/chrome/a/answer/187202#zippy=%2Cwindows "https://support.google.com/chrome/a/answer/187202#zippy=%2Cwindows").
2. On a directory administration WorkSpace or an Amazon EC2 instance that is
   joined to your WorkSpaces directory, open the Group Policy Management tool
   (**gpmc.msc**).
3. Expand the forest
   (**Forest:`FQDN`**).
4. Expand **Domains**.
5. Expand your FQDN (for example,
   `example.com`).
6. Expand **Group Policy Objects**.
7. Select **Default Domain Policy**, open the context
   (right-click) menu, and choose **Edit**.
8. Choose **Computer Configuration** ,
   **Administrative Templates**, **Google Chrome**,
   and **Extensions**
9. Open **Configure extension management settings** and set it
   to **Enabled**.
10. Under **Configure extension management settings**, enter the following:

```
{"mmiioagbgnbojdbcjoddlefhmcocfpmn":{ "installation_mode":"force_installed","update_url":"https://clients2.google.com/service/update2/crx"}}
```

11. Choose **OK**.
12. The Group Policy setting change takes effect after the WorkSpace session is
    restarted. To apply the Group Policy changes, reboot the WorkSpace by going to the
    Amazon WorkSpaces console and selecting the WorkSpace. Then, choose **Actions**,
    **Reboot WorkSpaces**).

###### Note

You can block the installation of the extension by applying the following configuration management setting:

```
{"mmiioagbgnbojdbcjoddlefhmcocfpmn":{ "installation_mode":"blocked","update_url":"https://clients2.google.com/service/update2/crx"}}
```

WebRTC redirection enhances real-time communication by offloading audio and video processing from WorkSpaces
to your local client, which improves performance and reduces latency. However, WebRTC redirection isn't universal
and requires third-party application vendors to develop specific integrations with WorkSpaces. By default, WebRTC
redirection isn't enabled on WorkSpaces. To use WebRTC redirection, ensure the following:

- Third-party application vendor integration
- WorkSpaces extensions are enabled through Group Policy settings
- WebRTC redirection is enabled
- WebRTC redirection Browser extension is installed and enabled

###### Note

This redirection is implemented as an extension and requires you to enable support for WorkSpaces extensions
using Group Policy settings. If the extensions are disabled, WebRTC redirection will not function.

#### Requirements

WebRTC redirection for DCV requires the following:

- DCV host agent version 2.0.0.1622 or higher
- WorkSpaces clients:
  - Windows 5.21.0 or higher
  - Web client

- Web browsers installed on your WorkSpaces running the Amazon DCV WebRTC Redirection Extension:
  - Google Chrome 116+
  - Microsoft Edge 116+

#### Enabling or disabling WebRTC redirection for Windows WorkSpaces

If needed, you can enable or disable support for WebRTC redirection
for Windows WorkSpaces by using Group Policy settings. If you disable or don't configure this setting, WebRTC
redirection will be disabled.

When feature is enabled, web applications that have integration with Amazon WorkSpaces will be able
to redirect WebRTC API calls to the local client.

###### To configure WebRTC redirection for Windows WorkSpaces

1. In the Group Policy Management Editor, choose **Computer
   Configuration**, **Policies**,
   **Administrative Templates**, **Amazon**,
   and **WSP**.
2. Open the **Configure WebRTC Redirection** setting.
3. In the **Configure WebRTC Redirection** dialog box,
   choose **Enabled** or **Disabled**.
4. Choose **OK**.
5. The Group Policy setting change takes effect after the WorkSpace session is
   restarted. To apply the Group Policy changes, reboot the WorkSpace by going to the
   Amazon WorkSpaces console and selecting the WorkSpace. Then, choose **Actions**,
   **Reboot WorkSpaces**).

#### Installing the Amazon DCV WebRTC Redirection Extension

Users install the Amazon DCV WebRTC Redirection Extension to use WebRTC redirection
after the feature is enabled by doing either of the following:

- Users will be prompted to enable the browser extension in their browser.

###### Note

As a one-time browser prompt, users will get the notification when you enable WebRTC redirection.

- You can force install the redirection extension for users using the following GPO policy. If you enable the GPO policy, the extension will
  automatically be installed when users launch the supported browsers with internet access.
- Users can install the extension manually with [Microsoft Edge Add-ons](https://microsoftedge.microsoft.com/addons/detail/amazon-dcv-webrtc-redirec/kjbbkjjiecchbcdoollhgffghfjnbhef "https://microsoftedge.microsoft.com/addons/detail/amazon-dcv-webrtc-redirec/kjbbkjjiecchbcdoollhgffghfjnbhef") or the [Chrome Web Store](https://chromewebstore.google.com/detail/dcv-webrtc-redirection-ex/diilpfplcnhehakckkpmcmibmhbingnd?hl=en&authuser=0&pli=1 "https://chromewebstore.google.com/detail/dcv-webrtc-redirection-ex/diilpfplcnhehakckkpmcmibmhbingnd?hl=en&authuser=0&pli=1").

##### Manage and install the browser extension using Group Policy

You can install the Amazon DCV WebRTC Redirection Extension using
Group Policy, either centrally from your domain, for session hosts
joined to an Active Directory (AD) domain, or using the Local Group
Policy Editor for each session host. This process will be different depending
on which browser you're using.

###### For Microsoft Edge

1. Download and install the
   [Microsoft Edge administrative template](https://learn.microsoft.com/en-us/deployedge/configure-microsoft-edge#1-download-and-install-the-microsoft-edge-administrative-template "https://learn.microsoft.com/en-us/deployedge/configure-microsoft-edge#1-download-and-install-the-microsoft-edge-administrative-template").
2. On a directory administration WorkSpace or an Amazon EC2 instance that is
   joined to your WorkSpaces directory, open the Group Policy Management tool
   (**gpmc.msc**).
3. Expand the forest
   (**Forest:`FQDN`**).
4. Expand **Domains**.
5. Expand your FQDN (for example,
   `example.com`).
6. Expand **Group Policy Objects**.
7. Select **Default Domain Policy**, open the context
   (right-click) menu, and choose **Edit**.
8. Choose **Computer Configuration** ,
   **Administrative Templates**, **Microsoft Edge**,
   and **Extensions**
9. Open **Configure extension management settings** and set it
   to **Enabled**.
10. Under **Configure extension management settings**, enter the following:

```
{"kjbbkjjiecchbcdoollhgffghfjnbhef":{"installation_mode":"force_installed","update_url":"https://edge.microsoft.com/extensionwebstorebase/v1/crx"}}
```

11. Choose **OK**.
12. The Group Policy setting change takes effect after the WorkSpace session is
    restarted. To apply the Group Policy changes, reboot the WorkSpace by going to the
    Amazon WorkSpaces console and selecting the WorkSpace. Then, choose **Actions**,
    **Reboot WorkSpaces**).

###### Note

You can block the installation of the extension by applying the following configuration management setting:

```
{"kjbbkjjiecchbcdoollhgffghfjnbhef":{"installation_mode":"blocked","update_url":"https://edge.microsoft.com/extensionwebstorebase/v1/crx"}}
```

###### For Google Chrome

1. Download and install the Google Chrome administrative template. For more information, see
   [Set Chrome Browser policies on managed PCs](https://support.google.com/chrome/a/answer/187202#zippy=%2Cwindows "https://support.google.com/chrome/a/answer/187202#zippy=%2Cwindows").
2. On a directory administration WorkSpace or an Amazon EC2 instance that is
   joined to your WorkSpaces directory, open the Group Policy Management tool
   (**gpmc.msc**).
3. Expand the forest
   (**Forest:`FQDN`**).
4. Expand **Domains**.
5. Expand your FQDN (for example,
   `example.com`).
6. Expand **Group Policy Objects**.
7. Select **Default Domain Policy**, open the context
   (right-click) menu, and choose **Edit**.
8. Choose **Computer Configuration** ,
   **Administrative Templates**, **Google Chrome**,
   and **Extensions**
9. Open **Configure extension management settings** and set it
   to **Enabled**.
10. Under **Configure extension management settings**, enter the following:

```
{"diilpfplcnhehakckkpmcmibmhbingnd":{ "installation_mode":"force_installed","update_url":"https://clients2.google.com/service/update2/crx"}}
```

11. Choose **OK**.
12. The Group Policy setting change takes effect after the WorkSpace session is
    restarted. To apply the Group Policy changes, reboot the WorkSpace by going to the
    Amazon WorkSpaces console and selecting the WorkSpace. Then, choose **Actions**,
    **Reboot WorkSpaces**).

###### Note

You can block the installation of the extension by applying the following configuration management setting:

```
{"diilpfplcnhehakckkpmcmibmhbingnd":{ "installation_mode":"blocked","update_url":"https://clients2.google.com/service/update2/crx"}}
```

If needed, you can disconnect users' WorkSpaces sessions when the Windows lock
screen is detected. To reconnect from the WorkSpaces client, users can use their
passwords or their smart cards to authenticate themselves, depending on which
type of authentication has been enabled for their WorkSpaces.

This Group Policy setting is disabled by default. If needed, you can enable
disconnecting the session when the Windows lock screen is detected for Windows
WorkSpaces by using Group Policy settings.

###### Note

- This Group Policy setting applies to both password-authenticated
  and smart card-authenticated sessions.
- To enable the use of smart cards with Windows WorkSpaces, additional
  steps are required. For more information, see [Use smart cards for authentication in WorkSpaces Personal](smart-cards.md "smart-cards.md").

###### To configure disconnect session on screen lock for Windows

WorkSpaces

1.  In the Group Policy Management Editor, choose **Computer
    Configuration**, **Policies**,
    **Administrative Templates**, **Amazon**,
    and **WSP**.
2.  Open the **Enable/disable disconnect session on screen
    lock** setting.
3.  In the **Enable/disable disconnect session on screen
    lock** dialog box, choose **Enabled** or
    **Disabled**.
4.  Choose **OK**.
5.  The Group Policy setting change takes effect after the next Group
    Policy update for the WorkSpace and after the WorkSpace session is
    restarted. To apply the Group Policy changes, do one of the
    following:

        * Reboot the WorkSpace (in the Amazon WorkSpaces console, select the
         WorkSpace, then choose **Actions**,
         **Reboot WorkSpaces**).
        * In an administrative command prompt, enter `gpupdate
         /force`.

    Screen Capture Protection prevents screenshots, screen recordings, and screen
    sharing of WorkSpaces sessions from local client tools. When enabled, attempts
    to capture screen content from client side will show either the background or
    a black rectangle, helping protect sensitive information from exfiltration.

#### Requirements

Screen capture protection for DCV requires the following:

- DCV host agent version 2.2.0.2116 or higher
- WorkSpaces clients:
  - Windows 5.30.2 or higher
  - MacOS 5.30.2 or higher

###### Note

- This feature is not supported on Linux clients, Web Access,
  or PCoIP protocol.
- Protection applies to captures initiated from the client
  device. Users can still take screenshots from within the
  WorkSpace itself.
- The feature is not compatible with screen sharing on MS
  Teams.

#### Known limitations

- The feature cannot prevent physical camera captures of
  screens.
- The feature does not protect against direct RDP
  connections to the host server.
- The feature does not protect against capture attempts
  initiated from within the WorkSpace itself, including screen
  share features of collaboration and chat tools.
- All capture methods are blocked when enabled (selective
  blocking is not available).
- MacOS client window may be grayed out if the feature
  is enabled and a video capture is attempted (e.g. trying to screen
  share the client window).

###### To configure Screen Capture Protection for Windows

WorkSpaces

1.  In the Group Policy Management Editor, choose **Computer
    Configuration**, **Policies**,
    **Administrative Templates**, **Amazon**,
    and **WSP**.
2.  Open the **Configure Screen Capture Protection**
    setting.
3.  In the **Configure Screen Capture Protection**
    dialog box, choose **Enabled** or
    **Disabled**.
4.  Choose **OK**.
5.  The Group Policy setting change takes effect after the next Group
    Policy update for the WorkSpace and after the WorkSpace session is
    restarted. To apply the Group Policy changes, do one of the
    following:

        1. Reboot the WorkSpace (in the WorkSpaces console, select the
         WorkSpace, then choose **Actions**,
         **Reboot WorkSpaces**).
        2. In an administrative command prompt, enter `gpupdate
         /force`.

    By default, WorkSpaces supports using Indirect Display Driver (IDD). If
    needed for Windows WorkSpaces, you can use Group Policy settings to disable this
    feature.

###### To configure Indirect Display Driver (IDD) for Windows

WorkSpaces

1.  In the Group Policy Management Editor, choose **Computer
    Configuration**, **Policies**,
    **Administrative Templates**, **Amazon**,
    and **WSP**.
2.  Open the **Enable the AWS Indirect Display Driver**
    setting.
3.  In the **Enable the AWS Indirect Display Driver**
    dialog box, choose **Enabled** or
    **Disabled**.
4.  Choose **OK**.
5.  The Group Policy setting change takes effect after the next Group
    Policy update for the WorkSpace and after the WorkSpace session is
    restarted. To apply the Group Policy changes, do one of the
    following:

        1. Reboot the WorkSpace (in the WorkSpaces console, select the
         WorkSpace, then choose **Actions**,
         **Reboot WorkSpaces**).
        2. In an administrative command prompt, enter `gpupdate
         /force`.

    WorkSpaces allows you to configure several different display settings, including
    the maximum frame rate, minimum image quality, maximum image quality, and YUV
    encoding. Adjust these settings based on the image quality, responsiveness, and
    color accuracy that you need.

By default, the maximum frame rate value is 25. The maximum frame rate value
specifies the maximum allowed frames per second (fps). A value of 0 means no
limit.

By default, the minimum image quality value is 30. The minimum image quality
can be optimized for best image responsiveness, or best image quality. For best
responsiveness, reduce the minimum quality. For best quality, increase the
minimum quality.

- Ideal values for best responsiveness are between 30 and 90.
- Ideal values for best quality are between 60 and 90.
  By default, the maximum image quality value is 80. The maximum image quality
  doesn't affect the image responsiveness or quality, but sets a maximum to limit
  network usage.

By default, image encoding is set to YUV420. Selecting **Enable YUV444
encoding** enables YUV444 encoding for high color accuracy.

For Windows WorkSpaces, you can use Group Policy settings to configure the maximum
frame rate, minimum image quality, and maximum image quality values.

###### To configure display settings for Windows WorkSpaces

1.  In the Group Policy Management Editor, choose **Computer
    Configuration**, **Policies**,
    **Administrative Templates**, **Amazon**,
    and **WSP**.
2.  Open the **Configure display settings**
    setting.
3.  In the **Configure display settings** dialog box,
    choose **Enabled** and then set the **Maximum
    frame rate (fps)**, **minimum image
    quality**, and **maximum image quality**
    values to the desired levels.
4.  Choose **OK**.
5.  The Group Policy setting change takes effect after the next Group
    Policy update for the WorkSpace and after you restart the WorkSpace
    session. To apply the Group Policy changes, do one of the
    following:

        * Reboot the WorkSpace. the Amazon WorkSpaces console, select the
         WorkSpace, then choose **Actions**,
         **Reboot WorkSpaces**
        * In an administrative command prompt, enter `gpupdate
         /force`.

    By default, WorkSpaces supports using the VSync feature for the AWS Virtual
    Display-Only Driver. If needed for Windows WorkSpaces, you can use Group Policy
    settings to disable this feature.

###### To configure VSync for Windows WorkSpaces

1.  In the Group Policy Management Editor, choose **Computer
    Configuration**, **Policies**,
    **Administrative Templates**, **Amazon**,
    and **WSP**.
2.  Open the **Enable VSync feature of the AWS Virtual Display
    Only Driver** setting.
3.  In the **Enable VSync feature of the AWS Virtual Display
    Only Driver** dialog box, choose
    **Enabled** or
    **Disabled**.
4.  Choose **OK**.
5.  The Group Policy setting change takes effect after the next Group
    Policy update for the WorkSpace and after the WorkSpace session is
    restarted. To apply the Group Policy changes, do the following:

        1. Restart the WorkSpace by doing the either of the
         following:


        	1. Option 1 — In the WorkSpaces console, choose the
        	 WorkSpace you want to reboot. Then, choose
        	 **Actions**, **Reboot
        	 WorkSpaces**.
        	2. Option 2 — In an administrative command prompt,
        	 enter `gpupdate /force`.
        2. Reconnect to the WorkSpace in order to apply the
         setting.
        3. Reboot the Workspace again.

    By default, the log verbosity level for DCV WorkSpaces is set to
    **Info**. You can set log levels to verbosity levels
    ranging from least verbose to most verbose, as detailed here:

- Error – least verbose
- Warning
- Info – default
- Debug – most verbose
  For Windows WorkSpaces, you can use Group Policy settings to configure the log
  verbosity levels.

###### To configure log verbosity levels for Windows WorkSpaces

1.  In the Group Policy Management Editor, choose **Computer
    Configuration**, **Policies**,
    **Administrative Templates**, **Amazon**,
    and **WSP**.
2.  Open the **Configure log verbosity** setting.
3.  In the **Configure log verbosity** dialog box, choose
    **Enabled** and then set the log verbosity level to
    **debug**, **error**,
    **info**, or **warning**.
4.  Choose **OK**.
5.  The Group Policy setting change takes effect after the next Group
    Policy update for the WorkSpace and after you restart the WorkSpace
    session. To apply the Group Policy changes, do one of the
    following:

        * Reboot the WorkSpace. In the Amazon WorkSpaces console, select the
         WorkSpace, then choose **Actions**,
         **Reboot WorkSpaces**.
        * In an administrative command prompt, enter `gpupdate
         /force`.

    WorkSpaces allows you to configure how long a user can be inactive, while connected to a WorkSpace,
    before they are disconnected. Examples of user activity input include the following:

- Keyboard events
- Mouse events (cursor movement, scrolling, clicking)
- Stylus events
- Touch events (tapping touchscreens, tablets)
- Gamepad events
- File storage operations (uploads, downloads, directory creation, list items)
- Webcam streaming
  Audio in, audio out, and pixels changing don't qualify as user activity.

When enabling idle disconnect timeout, you can optionally notify your user that their session will disconnect within the
configured time unless they engage.

By default, idle disconnect timeout is disabled, the timeout value is set to 0 minutes, and the
notification is disabled. If you enable this policy setting, the idle disconnect timeout value
defaults to 60 minutes and the idle disconnect warning value defaults to 60 seconds. For Windows WorkSpaces,
you can use Group Policy settings to configure this feature.

###### To configure idle disconnect timeout for Windows WorkSpaces

1. In the Group Policy Management Editor, choose **Computer
   Configuration**, **Policies**,
   **Administrative Templates**, **Amazon**,
   and **WSP**.
2. Open the **Configure Idle Disconnect Timeout** setting.
3. In the **Configure Idle Disconnect Timeout** dialog box, choose
   **Enabled** and then set the desired disconnect timeout value (in minutes),
   and optionally the warning timer value (in seconds).
4. Choose **Apply**, **OK**.
5. The Group Policy setting change takes effect immediately after you apply the change.
   By default, Amazon WorkSpaces disables the file transfer function. You can enable it to
   allow users to upload and download files between their local computer and WorkSpaces session.
   The files will be saved in a **My Storage** folder on the WorkSpaces session.

###### To enable file transfer for Windows WorkSpaces

1. In the Group Policy Management Editor, choose **Computer
   Configuration**, **Policies**,
   **Administrative Templates**, **Amazon**,
   and **WSP**.
2. Open the **Configure session storage** setting.
3. In the **Configure Session Storage** dialog box, choose
   **Enabled**.
4. (Optional) Specify a folder for session storage (for example,
   `c:/session-storage`). If not specified, the default folder
   for session storage will be the home folder.
5. You can configure your WorkSpaces with one of the following file transfer options:
   - Choose `Download and Upload` to allow two-way file transfer.
   - Choose `Upload Only` to only allow file uploads from a local computer
     to your WorkSpaces session.
   - Choose `Download Only` to only allow file downloads from your WorkSpaces
     session to a local computer.

6. Choose **OK**.
7. The Group Policy setting change takes effect after the next Group
   Policy update for the WorkSpace and after you restart the WorkSpace
   session. To apply the Group Policy changes, do one of the
   following:
   - Reboot the WorkSpace. In the Amazon WorkSpaces console, select the
     WorkSpace, then choose **Actions**,
     **Reboot WorkSpaces**.
   - In an administrative command prompt, enter `gpupdate
/force`.

#### Overview

Starting with version 2.2.0.2047, Amazon WorkSpaces supports generic USB redirection for DCV-based Windows WorkSpaces, allowing users to access local USB devices within their virtual desktop environments. This feature complements existing optimized redirection solutions for specific device classes.

###### Note

Amazon recommends using generic redirection only for devices where optimized redirection solutions are not available. Where available, optimized redirection solutions offer better performance.

#### Prerequisites

- Windows WorkSpaces using DCV protocol version 2.2.0.2047 or later
- Latest version of WorkSpaces Windows client (version 5.30.0 or later)
- Administrative access to configure Group Policy settings

#### Configuration

USB redirection is disabled by default. You can enable the feature by using Group Policy Objects (GPO). After the feature is enabled, you can add devices to the allowlist for redirection. By default, devices not in the allowlist are not available for redirection.

##### Group Policy Configuration

###### To configure USB redirection for DCV using Group Policy

1. Connect to the Windows WorkSpaces.
2. Copy policy template files (`wsp.admx` and `wsp.adml`) from the `C:\Program Files\Amazon\WSP` folder.
3. Paste `wsp.admx` into the `C:\Windows\PolicyDefinitions` folder.
4. Paste `wsp.adml` into the `C:\Windows\PolicyDefinitions\en-US` folder.
5. Launch Local GPO Editor (**gpedit.msc**).
6. Navigate to **Local Computer Policy** > **Computer Configuration** > **Administrative Templates** > **Amazon** > **WSP**.
7. Configure **Enable/disable USB** in the WSP setting.
8. Choose **Enabled** to activate USB redirection.

###### Note

Changes to this setting are applied on the next connection.

#### Device Management

After USB redirection is enabled, you can configure the device allowlist in the GPO to add devices that you want to support for redirection.

##### Device Allowlist Configuration

USB redirection follows a default deny-all security stance. Administrators must explicitly allow devices by adding them to the allowlist in the GPO using the following format:

```
Name, Base class, Subclass, Protocol, Id Vendor, Id Product, Support Auto-share, Skip reset
// Use * to skip any values
```

**Examples:**

**Adding a device with Vendor ID/Product ID:**

```
Credit Card Reader, *, *, *, 0x0483, 0x2016, 1, 0
// Allows Credit Card Reader with VID 0x0483 and PID 0x2016 with auto-share support
```

**Adding a device with Class/Subclass:**

```
3D Mouse Devices, 03, 01, *, *, *, 1, 0
// Allows all 3D mice using HID class (03), boot interface subclass (01), with auto-share support
```

###### Note

Test devices for compatibility and performance before adding them to the allowlist.

#### Security Considerations

##### Best Practices

- Use dedicated redirection methods when available for supported devices for best performance and compatibility. For example, for security keys like YubiKey, use WebAuthn redirection instead.
- Implement strict device allowlists.
- Monitor device access through audit logs.
- Assess data security implications before allowing new devices.

Use this setting to configure webcam resolution settings. If you enable this policy setting, you can specify:

- Maximum webcam resolution: This specifies the maximum webcam resolution that can be selected among the resolutions provided. If this value is missing
  or (0, 0) the default value is used.
- Preferred webcam resolution: This specifies the preferred webcam resolution among the resolutions provided by the client. If the specified resolution
  is not supported, the closest matching resolution is selected. If this value is missing or (0, 0) the default value is used.
  If you disable or do not configure this policy setting, the default resolutions are used.

###### To configure webcam resolution for Windows WorkSpaces

1.  In the Group Policy Management Editor, choose **Computer
    Configuration**, **Policies**,
    **Administrative Templates**, **Amazon**,
    and **WSP**.
2.  Open the **Configure webcam resolution** setting.
3.  In the **Configure webcam resolution** dialog box, choose
    **Enabled** and then set the **Maximum webcam resolution** (in pixels) and/or **Preferred webcam resolution** (in pixels).
4.  Choose **OK**.
5.  The Group Policy setting change takes effect after the next Group
    Policy update for the WorkSpace and after you restart the WorkSpace
    session. To apply the Group Policy changes, do one of the
    following:

        * Reboot the WorkSpace. In the Amazon WorkSpaces console, select the
         WorkSpace, then choose **Actions**,
         **Reboot WorkSpaces**.
        * In an administrative command prompt, enter `gpupdate
         /force`.

    This setting controls whether to use server side keyboard layout for key interpretation, as opposed to the default client side keyboard layout. Changes to this setting are applied on the next connection. For more details on keyboard handling please see the _Amazon WorkSpaces User Guide_.

If you enable this policy setting, you can choose one of the following options:

- **Always Off** - Always use client layout
- **Always On** - Always use server layout
  If you disable or do not configure this policy setting, the **Always Off** option is used.

###### Note

This feature is supported in the Amazon WorkSpaces Windows client version 5.29.2 or newer, and the Amazon WorkSpaces macOS client version 5.30.0 or newer.

###### To configure server keyboard layout usage for Windows WorkSpaces

1. In the Group Policy Management Editor, choose **Computer
   Configuration**, **Policies**,
   **Administrative Templates**, **Amazon**,
   and **WSP**.
2. Open the **Configure server keyboard layout usage** setting.
3. In the **Configure server keyboard layout usage** dialog box, choose
   **Enabled** and then set the **Server keyboard layout option**.
4. Choose **OK**.
5. The Group Policy setting change takes effect after the next Group
   Policy update for the WorkSpace and after you restart the WorkSpace
   session. To apply the Group Policy changes, do one of the
   following:
   - Reboot the WorkSpace. In the Amazon WorkSpaces console, select the
     WorkSpace, then choose **Actions**,
     **Reboot WorkSpaces**.
   - In an administrative command prompt, enter `gpupdate
/force`.

## Install the Group Policy administrative template

for PCoIP

To use the Group Policy settings that are specific to Amazon WorkSpaces when using the PCoIP
protocol, you must add the Group Policy administrative template that is appropriate to
the version of the PCoIP agent (either 32-bit or 64-bit) that is being used for your
WorkSpaces.

###### Note

If you have a mix of WorkSpaces with 32-bit and 64-bit agents, you can use the Group
Policy administrative templates for 32-bit agents, and your Group Policy settings
will be applied to both 32-bit and 64-bit agents. When all of your WorkSpaces are using
the 64-bit agent, you can switch to using the administrative template for 64-bit
agents.

###### To determine whether your WorkSpaces have the 32-bit agent or the 64-bit agent

1. Log in to a WorkSpace, and then open the Task Manager by choosing
   **View**, **Send Ctrl + Alt + Delete** or
   by right-clicking the task bar and choosing **Task
   Manager**.
2. In the Task Manager, go to the **Details** tab, right-click
   the column headers, and choose **Select Columns**.
3. In the **Select Columns** dialog box, select
   **Platform**, and then choose **OK**.
4. On the **Details** tab, find
   `pcoip_agent.exe`, and then check its value in the
   **Platform** column to determine if the PCoIP agent is
   32-bit or 64-bit. (You might see a mix of 32-bit and 64-bit WorkSpaces components;
   this is normal.)

To use the Group Policy settings that are specific to WorkSpaces when using the
PCoIP protocol with the 32-bit PCoIP agent, you must install the Group Policy
administrative template for PCoIP. Perform the following procedure on a
directory administration WorkSpace or Amazon EC2 instance that is joined to your
directory.

For more information about working with .adm files, see [Recommendations for managing Group Policy administrative template (.adm)
files](https://docs.microsoft.com/troubleshoot/windows-server/group-policy/manage-group-policy-adm-file "https://docs.microsoft.com/troubleshoot/windows-server/group-policy/manage-group-policy-adm-file") in the Microsoft documentation.

###### To install the Group Policy administrative template for PCoIP

1. From a running Windows WorkSpace, make a copy of the
   `pcoip.adm` file in the `C:\Program
Files (x86)\Teradici\PCoIP Agent\configuration`
   directory.
2. On a directory administration WorkSpace or an Amazon EC2 instance that is
   joined to your WorkSpaces directory, open the Group Policy Management tool
   (**gpmc.msc**) and navigate to the organizational
   unit in your domain that contains your WorkSpaces machine accounts.
3. Open the context (right-click) menu for the machine account
   organizational unit and choose **Create a GPO in this domain,
   and link it here**.
4. In the **New GPO** dialog box, enter a descriptive
   name for the GPO, such as **WorkSpaces Machine Policies**,
   and leave **Source Starter GPO** set to
   **(none)**. Choose **OK**.
5. Open the context (right-click) menu for the new GPO and choose
   **Edit**.
6. In the Group Policy Management Editor, choose **Computer
   Configuration**, **Policies**, and
   **Administrative Templates**. Choose
   **Action**, **Add/Remove
   Templates** from the main menu.
7. In the **Add/Remove Templates** dialog box, choose
   **Add**, select the `pcoip.adm`
   file copied previously, and then choose **Open**,
   **Close**.
8. Close the Group Policy Management Editor. You can now use this GPO to
   modify the Group Policy settings that are specific to WorkSpaces.

###### To verify that the administrative template file is correctly

installed

1. On a directory administration WorkSpace or an Amazon EC2 instance that is
   joined to your WorkSpaces directory, open the Group Policy Management tool
   (**gpmc.msc**) and navigate to and select the WorkSpaces
   GPO for your WorkSpaces machine accounts. Choose **Action**,
   **Edit** in the main menu.
2. In the Group Policy Management Editor, choose **Computer
   Configuration**, **Policies**,
   **Administrative Templates**, **Classic
   Administrative Templates**, and **PCoIP Session
   Variables**.
3. You can now use this **PCoIP Session Variables**
   Group Policy object to modify the Group Policy settings that are
   specific to Amazon WorkSpaces when using PCoIP.

###### Note

To allow the user to override your settings, choose
**Overridable Administrator Settings**;
otherwise, choose **Not Overridable Administrator
Settings**.

To use the Group Policy settings that are specific to WorkSpaces when using the
PCoIP protocol, you must add the Group Policy administrative template
`PCoIP.admx` and `PCoIP.adml` files
for PCoIP to the Central Store of the domain controller for your WorkSpaces
directory. For more information about `.admx` and
`.adml` files, see [How to create and manage the Central Store for Group Policy Administrative
Templates in Windows](https://support.microsoft.com/help/3087759/how-to-create-and-manage-the-central-store-for-group-policy-administra "https://support.microsoft.com/help/3087759/how-to-create-and-manage-the-central-store-for-group-policy-administra").

The following procedure describes how to create the Central Store and add the
administrative template files to it. Perform the following procedure on a
directory administration WorkSpace or Amazon EC2 instance that is joined to your
WorkSpaces directory.

###### To install the Group Policy administrative template files for

PCoIP

1. From a running Windows WorkSpace, make a copy of the
   `PCoIP.admx` and `PCoIP.adml`
   files in the `C:\Program Files\Teradici\PCoIP
Agent\configuration\policyDefinitions` directory. The
   `PCoIP.adml` file is in the
   `en-US` subfolder of that directory.
2. On a directory administration WorkSpace or an Amazon EC2 instance that is
   joined to your WorkSpaces directory, open Windows File Explorer, and in the
   address bar, enter your organization's fully qualified domain name
   (FQDN), such as `\\example.com`.
3. Open the `sysvol` folder.
4. Open the folder with the
   `FQDN` name.
5. Open the `Policies` folder. You should now be in
   `\\`FQDN`\sysvol\`FQDN`\Policies`.
6. If it doesn't already exist, create a folder named
   `PolicyDefinitions`.
7. Open the `PolicyDefinitions` folder.
8. Copy the `PCoIP.admx` file into the
   `\\`FQDN`\sysvol\`FQDN`\Policies\PolicyDefinitions`
   folder.
9. Create a folder named `en-US` in the
   `PolicyDefinitions` folder.
10. Open the `en-US` folder.
11. Copy the `PCoIP.adml` file into the
    `\\`FQDN`\sysvol\`FQDN`\Policies\PolicyDefinitions\en-US`
    folder.

###### To verify that the administrative template files are correctly

installed

1. On a directory administration WorkSpace or an Amazon EC2 instance that is
   joined to your WorkSpaces directory, open the Group Policy Management tool
   (**gpmc.msc**).
2. Expand the forest
   (**Forest:`FQDN`**).
3. Expand **Domains**.
4. Expand your FQDN (for example,
   `example.com`).
5. Expand **Group Policy Objects**.
6. Select **Default Domain Policy**, open the context
   (right-click) menu, and choose **Edit**.

###### Note

If the domain backing the WorkSpaces is an AWS Managed Microsoft AD directory, you
cannot use the Default Domain Policy to create your GPO. Instead,
you must create and link the GPO under the domain container that has
delegated privileges.

When you create a directory with AWS Managed Microsoft AD, Directory Service creates a
`yourdomainname` organizational unit
(OU) under the domain root. The name of this OU is based on the
NetBIOS name that you typed when you created your directory. If you
didn't specify a NetBIOS name, it will default to the first part of
your Directory DNS name (for example, in the case of
`corp.example.com`, the NetBIOS name is
`corp`).

To create your GPO, instead of selecting **Default Domain
Policy**, select the
`yourdomainname` OU (or any OU under
that one), open the context (right-click) menu, and choose
**Create a GPO in this domain, and Link it
here**.

For more information about the
`yourdomainname` OU, see [What Gets Created](../../../directoryservice/latest/admin-guide/ms_ad_getting_started_what_gets_created.md "../../../directoryservice/latest/admin-guide/ms_ad_getting_started_what_gets_created.md") in the
_AWS Directory Service Administration Guide_. 7. In the Group Policy Management Editor, choose **Computer
Configuration**, **Policies**,
**Administrative Templates**, and **PCoIP
Session Variables**. 8. You can now use this **PCoIP Session Variables**
Group Policy object to modify the Group Policy settings that are
specific to WorkSpaces when using PCoIP.

###### Note

To allow the user to override your settings, choose
**Overridable Administrator Settings**;
otherwise, choose **Not Overridable Administrator
Settings**.

## Manage Group Policy settings for PCoIP

Use Group Policy settings to manage your Windows WorkSpaces that use PCoIP.

By default, WorkSpaces enables Basic remote printing, which offers limited printing
capabilities because it uses a generic printer driver on the host side to ensure
compatible printing.

Advanced remote printing for Windows clients lets you use specific features of
your printer, such as double-sided printing, but it requires installation of the
matching printer driver on the host side.

Remote printing is implemented as a virtual channel. If virtual channels are
disabled, remote printing does not function.

For Windows WorkSpaces, you can use Group Policy settings to configure printer
support as needed.

###### To configure printer support

1.  Make sure that you've installed the most recent [WorkSpaces Group Policy
    administrative template for PCoIP (32-Bit)](#gp_install_template_pcoip_32_bit "#gp_install_template_pcoip_32_bit") or [WorkSpaces Group Policy
    administrative template for PCoIP (64-Bit)](#gp_install_template_pcoip_64_bit "#gp_install_template_pcoip_64_bit").
2.  On a directory administration WorkSpace or an Amazon EC2 instance that is
    joined to your WorkSpaces directory, open the Group Policy Management tool
    (**gpmc.msc**) and navigate to **PCoIP
    Session Variables**.
3.  Open the **Configure remote printing**
    setting.
4.  In the **Configure remote printing** dialog box, do
    one of the following:
    - To enable Advanced remote printing, choose
      **Enabled**, and then under
      **Options,**
      **Configure remote printing**, choose
      **Basic and Advanced printing for Windows
      clients**. To automatically use the client
      computer's current default printer, select
      **Automatically set default
      printer**.
    - To disable printing, choose **Enabled**, and
      then under **Options,**
      **Configure remote printing**, choose
      **Printing disabled**.

5.  Choose **OK**.
6.  The Group Policy setting change takes effect after the next Group
    Policy update for the WorkSpace and after the WorkSpace session is
    restarted. To apply the Group Policy changes, do one of the
    following:

        * Reboot the WorkSpace (in the Amazon WorkSpaces console, select the
         WorkSpace, then choose **Actions**,
         **Reboot WorkSpaces**).
        * In an administrative command prompt, enter `gpupdate
         /force`.

    By default, local printer auto-redirection is disabled. You can use Group
    Policy settings to enable this feature so that your local printer is set as the
    default printer every time that you connect to your WorkSpace.

###### Note

Local printer redirection is not available for Amazon Linux WorkSpaces.

###### To enable local printer auto-redirection

1.  Make sure that you've installed the most recent [WorkSpaces Group Policy
    administrative template for PCoIP (32-Bit)](#gp_install_template_pcoip_32_bit "#gp_install_template_pcoip_32_bit") or [WorkSpaces Group Policy
    administrative template for PCoIP (64-Bit)](#gp_install_template_pcoip_64_bit "#gp_install_template_pcoip_64_bit").
2.  On a directory administration WorkSpace or an Amazon EC2 instance that is
    joined to your WorkSpaces directory, open the Group Policy Management tool
    (**gpmc.msc**) and navigate to **PCoIP
    Session Variables**.
3.  Open the **Configure remote printing**
    setting.
4.  Choose **Enabled**, and then under
    **Options**, **Configure remote
    printing**, choose one of the following:
    - **Basic and Advanced printing for Windows
      clients**
    - **Basic printing**

5.  Select **Automatically set default printer**, and
    then choose **OK**.
6.  The Group Policy setting change takes effect after the next Group
    Policy update for the WorkSpace and after the WorkSpace session is
    restarted. To apply the Group Policy changes, do one of the
    following:

        * Reboot the WorkSpace (in the Amazon WorkSpaces console, select the
         WorkSpace, then choose **Actions**,
         **Reboot WorkSpaces**).
        * In an administrative command prompt, enter `gpupdate
         /force`.

    By default, WorkSpaces supports clipboard redirection. If needed for Windows WorkSpaces,
    you can use Group Policy settings to disable this feature.

###### To enable or disable clipboard redirection

1. Make sure that you've installed the most recent [WorkSpaces Group Policy
   administrative template for PCoIP (32-Bit)](#gp_install_template_pcoip_32_bit "#gp_install_template_pcoip_32_bit") or [WorkSpaces Group Policy
   administrative template for PCoIP (64-Bit)](#gp_install_template_pcoip_64_bit "#gp_install_template_pcoip_64_bit").
2. On a directory administration WorkSpace or an Amazon EC2 instance that is
   joined to your WorkSpaces directory, open the Group Policy Management tool
   (**gpmc.msc**) and navigate to **PCoIP
   Session Variables**.
3. Open the **Configure clipboard redirection**
   setting.
4. In the **Configure clipboard redirection** dialog
   box, choose **Enabled** and then choose one of the
   following settings to determine the direction in which clipboard
   redirection is allowed. When you're done, choose
   **OK**.
   - Disabled in both directions
   - Enabled agent to client only (WorkSpace to local
     computer)
   - Enabled client to agent only (local computer to
     WorkSpace)
   - Enabled in both directions

5. The Group Policy setting change takes effect after the next Group
   Policy update for the WorkSpace and after the WorkSpace session is
   restarted. To apply the Group Policy changes, do one of the
   following:
   - Reboot the WorkSpace (in the Amazon WorkSpaces console, select the
     WorkSpace, then choose **Actions**,
     **Reboot WorkSpaces**).
   - In an administrative command prompt, enter `gpupdate
/force`.

###### Known limitation

With clipboard redirection enabled on the WorkSpace, if you copy content
that is larger than 890 KB from a Microsoft Office application, the
application might become slow or unresponsive for up to 5 seconds.

When you lose network connectivity, your active WorkSpaces client session is
disconnected. WorkSpaces client applications for Windows and macOS attempt to
reconnect the session automatically if network connectivity is restored within a
certain amount of time. The default session resume timeout is 20 minutes, but
you can modify that value for WorkSpaces that are controlled by your domain's Group
Policy settings.

###### To set the automatic session resume timeout value

1.  Make sure that you've installed the most recent [WorkSpaces Group Policy
    administrative template for PCoIP (32-Bit)](#gp_install_template_pcoip_32_bit "#gp_install_template_pcoip_32_bit") or [WorkSpaces Group Policy
    administrative template for PCoIP (64-Bit)](#gp_install_template_pcoip_64_bit "#gp_install_template_pcoip_64_bit").
2.  On a directory administration WorkSpace or an Amazon EC2 instance that is
    joined to your WorkSpaces directory, open the Group Policy Management tool
    (**gpmc.msc**) and navigate to **PCoIP
    Session Variables**.
3.  Open the **Configure Session Automatic Reconnection
    Policy** setting.
4.  In the **Configure Session Automatic Reconnection
    Policy** dialog box, choose **Enabled**,
    set the **Configure Session Automatic Reconnection
    Policy** option to the desired timeout, in minutes, and
    choose **OK**.
5.  The Group Policy setting change takes effect after the next Group
    Policy update for the WorkSpace and after the WorkSpace session is
    restarted. To apply the Group Policy changes, do one of the
    following:

        * Reboot the WorkSpace (in the Amazon WorkSpaces console, select the
         WorkSpace, then choose **Actions**,
         **Reboot WorkSpaces**).
        * In an administrative command prompt, enter `gpupdate
         /force`.

    By default, Amazon WorkSpaces supports redirecting data from a local microphone. If
    needed for Windows WorkSpaces, you can use Group Policy settings to disable this
    feature.

###### Note

If you have a Group Policy setting that restricts users' local logon in
their WorkSpaces, audio-in won't work on your WorkSpaces. If you remove that Group
Policy setting, the audio-in feature is enabled after the next reboot of the
WorkSpace. For more information about this Group Policy setting, see [Allow logon locally](https://docs.microsoft.com/windows/security/threat-protection/security-policy-settings/allow-log-on-locally "https://docs.microsoft.com/windows/security/threat-protection/security-policy-settings/allow-log-on-locally") in the Microsoft documentation.

###### To enable or disable audio-in redirection

1.  Make sure that you've installed the most recent [WorkSpaces Group Policy
    administrative template for PCoIP (32-Bit)](#gp_install_template_pcoip_32_bit "#gp_install_template_pcoip_32_bit") or [WorkSpaces Group Policy
    administrative template for PCoIP (64-Bit)](#gp_install_template_pcoip_64_bit "#gp_install_template_pcoip_64_bit").
2.  On a directory administration WorkSpace or an Amazon EC2 instance that is
    joined to your WorkSpaces directory, open the Group Policy Management tool
    (**gpmc.msc**) and navigate to **PCoIP
    Session Variables**.
3.  Open the **Enable/disable audio in the PCoIP
    session** setting.
4.  In the **Enable/disable audio in the PCoIP session**
    dialog box, choose **Enabled** or
    **Disabled**.
5.  Choose **OK**.
6.  The Group Policy setting change takes effect after the next Group
    Policy update for the WorkSpace and after the WorkSpace session is
    restarted. To apply the Group Policy changes, do one of the
    following:

        * Reboot the WorkSpace (in the Amazon WorkSpaces console, select the
         WorkSpace, then choose **Actions**,
         **Reboot WorkSpaces**).
        * In an administrative command prompt, enter `gpupdate
         /force`.

    By default, the time within a Workspace is set to mirror the time zone of the
    client that is being used to connect to the WorkSpace. This behavior is
    controlled through time zone redirection. You might want to turn off time zone
    direction for various reasons:

- Your company wants all employees to work in a certain time zone (even
  if some employees are in other time zones).
- You have scheduled tasks in a WorkSpace that are meant to run at a
  certain time in a specific time zone.
- Your users who travel a lot want to keep their WorkSpaces in one time zone
  for consistency and personal preference.
  If needed for Windows WorkSpaces, you can use Group Policy settings to disable this
  feature.

###### To disable time zone redirection

1. Make sure that you've installed the most recent [WorkSpaces Group Policy
   administrative template for PCoIP (32-Bit)](#gp_install_template_pcoip_32_bit "#gp_install_template_pcoip_32_bit") or [WorkSpaces Group Policy
   administrative template for PCoIP (64-Bit)](#gp_install_template_pcoip_64_bit "#gp_install_template_pcoip_64_bit").
2. On a directory administration WorkSpace or an Amazon EC2 instance that is
   joined to your WorkSpaces directory, open the Group Policy Management tool
   (**gpmc.msc**) and navigate to **PCoIP
   Session Variables**.
3. Open the **Configure timezone redirection**
   setting.
4. In the **Configure timezone redirection** dialog box,
   choose **Disabled**.
5. Choose **OK**.
6. The Group Policy setting change takes effect after the next Group
   Policy update for the WorkSpace and after the WorkSpace session is
   restarted. To apply the Group Policy changes, do one of the
   following:
   - Reboot the WorkSpace (in the Amazon WorkSpaces console, select the
     WorkSpace, then choose **Actions**,
     **Reboot WorkSpaces**).
   - In an administrative command prompt, enter `gpupdate
/force`.

7. Set the time zone for the WorkSpaces to the desired time zone.
   The time zone of the WorkSpaces is now static and no longer mirrors the time zone
   of the client machines.

For PCoIP, data in transit is encrypted using TLS 1.2 encryption and SigV4
request signing. The PCoIP protocol uses encrypted UDP traffic, with AES
encryption, for streaming pixels. The streaming connection, using port 4172 (TCP
and UDP), is encrypted by using AES-128 and AES-256 ciphers, but the encryption
defaults to 128-bit. You can change this default to 256-bit by using the
**Configure PCoIP Security Settings** Group Policy
setting.

You can also use this Group Policy setting to modify the TLS Security Mode and
to block certain cipher suites. A detailed explanation of these settings and the
supported cipher suites is provided in the **Configure PCoIP Security
Settings** Group Policy dialog box.

###### To configure PCoIP security settings

1. Make sure that you've installed the most recent [WorkSpaces Group Policy
   administrative template for PCoIP (32-Bit)](#gp_install_template_pcoip_32_bit "#gp_install_template_pcoip_32_bit") or [WorkSpaces Group Policy
   administrative template for PCoIP (64-Bit)](#gp_install_template_pcoip_64_bit "#gp_install_template_pcoip_64_bit").
2. On a directory administration WorkSpace or an Amazon EC2 instance that is
   joined to your WorkSpaces directory, open the Group Policy Management tool
   (**gpmc.msc**) and navigate to **PCoIP
   Session Variables**.
3. Open the **Configure PCoIP Security Settings**
   setting.
4. In the **Configure PCoIP Security Settings** dialog
   box, choose **Enabled**. To set the default encryption
   for streaming traffic to 256-bit, go to the **PCoIP Data
   Encryption Ciphers** option, and select
   **AES-256-GCM only**.
5. (Optional) Adjust the **TLS Security Mode** setting,
   and then list any cipher suites that you want to block. For more
   information about these settings, see the descriptions provided in the
   **Configure PCoIP Security Settings** dialog
   box.
6. Choose **OK**.
7. The Group Policy setting change takes effect after the next Group
   Policy update for the WorkSpace and after the WorkSpace session is
   restarted. To apply the Group Policy changes, do one of the
   following:
   - Reboot the WorkSpace (in the Amazon WorkSpaces console, select the
     WorkSpace, then choose **Actions**,
     **Reboot WorkSpaces**).
   - In an administrative command prompt, enter `gpupdate
/force`.

###### Note

Amazon WorkSpaces currently supports USB redirection only for YubiKey U2F. Other
types of USB devices might be redirected but they are not supported and
might not work properly.

###### To enable USB redirection for PCoIP

1. Make sure that you've installed the most recent [WorkSpaces Group Policy
   administrative template for PCoIP (32-Bit)](#gp_install_template_pcoip_32_bit "#gp_install_template_pcoip_32_bit") or [WorkSpaces Group Policy
   administrative template for PCoIP (64-Bit)](#gp_install_template_pcoip_64_bit "#gp_install_template_pcoip_64_bit").
2. On a directory administration WorkSpace or an Amazon EC2 instance that is
   joined to your WorkSpaces directory, open the Group Policy Management tool
   (**gpmc.msc**) and navigate to **PCoIP
   Session Variables**.
3. Open the **Enable/disable USB in the PCOIP session**
   setting.
4. Choose **Enabled**, and then choose
   **OK**.
5. Open the **Configure PCoIP USB allowed and unallowed device
   rules** setting.
6. Choose **Enabled**, and under **Enter the USB
   authorization table (maximum ten rules)**, configure your
   USB device allow list rules.
   1. Authorization rule - 110500407. This value is a combination of
      a Vendor ID (VID) and a Product ID (PID). The format for a
      VID/PID combination is 1xxxxyyyy, where xxxx is the VID in
      hexadecimal format and yyyy is the PID in hexadecimal format.
      For this example, 1050 is the VID, and 0407 is the PID. For more
      YubiKey USB values, see [YubiKey USB ID Values](https://support.yubico.com/hc/en-us/articles/360016614920-YubiKey-USB-ID-Values "https://support.yubico.com/hc/en-us/articles/360016614920-YubiKey-USB-ID-Values").

7. Under **Enter the USB authorization table (maximum ten
   rules)**, configure your USB device block list rules.
   1. For **Unauthorization Rule**, set an empty
      string. This means that only USB devices in the authorization
      list are allowed.###### Note

You can define a maximum of 10 USB authorization rules and a
maximum of 10 USB unauthorization rules. Use the vertical bar (|)
character to separate multiple rules. For detailed information about
the authorization/unauthorization rules, see [Teradici PCoIP Standard Agent for Windows](https://www.teradici.com/web-help/pcoip_agent/standard_agent/windows/20.10/admin-guide/configuring/configuring/#pcoip-usb-allowed-and-unallowed-device-rules "https://www.teradici.com/web-help/pcoip_agent/standard_agent/windows/20.10/admin-guide/configuring/configuring/#pcoip-usb-allowed-and-unallowed-device-rules"). 8. Choose **OK**. 9. The Group Policy setting change takes effect after the next Group
Policy update for the WorkSpace and after the WorkSpace session is
restarted. To apply the Group Policy changes, do one of the
following:

    * Reboot the WorkSpace (in the Amazon WorkSpaces console, select the
     WorkSpace, then choose **Actions**,
     **Reboot WorkSpaces**).
    * In an administrative command prompt, enter `gpupdate
     /force`.

After the setting takes effect, all supported USB devices can redirect to
WorkSpaces unless restrictions are configured through the USB device rules
setting.

## Set the maximum lifetime for a Kerberos

ticket

If you have not disabled the **Remember Me** feature of your Windows
WorkSpaces, your WorkSpace users can use the **Remember Me** or
**Keep me logged in** check box in their WorkSpaces client application
to save their credentials. This feature allows users to easily connect to their WorkSpaces
while the client application remains running. Their credentials are securely cached up
to the maximum lifetime of their Kerberos tickets.

If your WorkSpace uses an AD Connector directory, you can modify the maximum lifetime
of the Kerberos tickets for your WorkSpaces users through Group Policy by following the steps
in [Maximum Lifetime for a User Ticket](https://docs.microsoft.com/windows/security/threat-protection/security-policy-settings/maximum-lifetime-for-user-ticket "https://docs.microsoft.com/windows/security/threat-protection/security-policy-settings/maximum-lifetime-for-user-ticket") in the Microsoft Windows
documentation.

To enable or disable the **Remember Me** feature, see [Enable self-service WorkSpaces
management capabilities for your users in WorkSpaces Personal](enable-user-self-service-workspace-management.md "enable-user-self-service-workspace-management.md").

## Configure device proxy server settings for internet

access

By default, the WorkSpaces client applications use the proxy server that’s specified in the
device operating system settings for HTTPS (port 443) traffic. The Amazon WorkSpaces client
applications use the HTTPS port for updates, registration, and authentication.

###### Note

Proxy servers that require authentication with sign-in credentials are not
supported.

You can configure the device proxy server settings for your Windows WorkSpaces through
Group Policy by following the steps in [Configure device proxy and internet connectivity settings](https://docs.microsoft.com/windows/security/threat-protection/microsoft-defender-atp/configure-proxy-internet "https://docs.microsoft.com/windows/security/threat-protection/microsoft-defender-atp/configure-proxy-internet") in the Microsoft
documentation.

For more information about configuring the proxy settings in the WorkSpaces Windows client
application, see [Proxy Server](../userguide/amazon-workspaces-windows-client.md#windows_proxy_server "../userguide/amazon-workspaces-windows-client.md#windows_proxy_server") in the _Amazon WorkSpaces User Guide_.

For more information about configuring the proxy settings in the WorkSpaces macOS client
application, see [Proxy Server](../userguide/amazon-workspaces-osx-client.md#osx_proxy_server "../userguide/amazon-workspaces-osx-client.md#osx_proxy_server") in the _Amazon WorkSpaces User Guide_.

For more information about configuring the proxy settings in the WorkSpaces Web Access
client application, see [Proxy Server](../userguide/amazon-workspaces-web-access.md#web-access-proxy "../userguide/amazon-workspaces-web-access.md#web-access-proxy") in the _Amazon WorkSpaces User Guide_.

### Proxying desktop traffic

For PCoIP WorkSpaces, the desktop client applications do not support the use of a proxy
server nor TLS decryption and inspection for port 4172 traffic in UDP (for desktop
traffic). They require a direct connection to ports 4172.

For DCV WorkSpaces, the WorkSpaces Windows client application (version 5.1 and above) and
macOS client application (version 5.4 and above) support the use of HTTP proxy
servers for port 4195 TCP traffic. TLS decryption and inspection are not
supported.

DCV does not support the use of proxy for desktop traffic over UDP. Only WorkSpaces
Windows and macOS desktop client applications and web access support the use of
proxy, for TCP traffic.

###### Note

If you choose to use a proxy server, the API calls that the client application
makes to the WorkSpaces services are also proxied. Both API calls and desktop traffic
should pass through the same proxy server.

### Recommendation on the use of proxy servers

We do not recommend the use of a proxy server with your WorkSpaces desktop
traffic.

Amazon WorkSpaces desktop traffic is already encrypted, so proxies do not improve
security. A proxy represents an additional hop in the network path that could impact
streaming quality by introducing latency. Proxies could also potentially reduce
throughput if a proxy is not properly sized to handle desktop streaming traffic.
Furthermore, most proxies are not designed for supporting long running WebSocket
(TCP) connections and may affect streaming quality and stability.

If you must use a proxy, please locate your proxy server as close to the WorkSpace
client as possible, preferably in the same network, to avoid adding network latency,
which could negatively impact streaming quality and responsiveness.

## Enable Amazon WorkSpaces for Zoom Meeting Media Plugin

support

Zoom supports optimized real-time communication for DCV and PCoIP Windows-based WorkSpaces,
with the Zoom VDI Plugin. Direct client communication allows video calls to bypass the cloud-based
virtual desktop and provide a local-like Zoom experience when the meeting is
running inside the your user’s WorkSpace.

### Enable Zoom Meeting Media Plugin for DCV

Before installing the Zoom VDI components, update your WorkSpaces configuration to support Zoom optimization.

#### Prerequisites

Before using the plugin, make sure the following requirements are met.

- Windows WorkSpaces client version 5.10.0+ with
  [Zoom VDI Plugin](https://support.zoom.com/hc/en/article?id=zm_kb&sysparm_article=KB0066757#h_01H6PE29K2S6NPYCC3SWB667AT:~:text=Zoom%20Meeting%20client.-,Install%20the%20Zoom%20VDI%20plugin,-To%20complete%20your "https://support.zoom.com/hc/en/article?id=zm_kb&sysparm_article=KB0066757#h_01H6PE29K2S6NPYCC3SWB667AT:~:text=Zoom%20Meeting%20client.-,Install%20the%20Zoom%20VDI%20plugin,-To%20complete%20your") version 5.17.10+
- Within your WorkSpaces — [Zoom VDI Meeting](https://support.zoom.com/hc/en/article?id=zm_kb&sysparm_article=KB0063810 "https://support.zoom.com/hc/en/article?id=zm_kb&sysparm_article=KB0063810") client version 5.17.10+

#### Before you begin

1. Enable the **Extensions** Group Policy setting. For more information, see
   [Configure extensions for DCV](#extensions "#extensions").
2. Disable the **Automatic reconnect** Group Policy setting. For more information, see
   [Set the session resume timeout for
   DCV](#gp_auto_resume_wsp "#gp_auto_resume_wsp").

#### Installing the Zoom components

To enable Zoom optimization, install two components, provided by Zoom, on your Windows WorkSpaces.
For more information, see[Using Zoom for Amazon Web Services](https://support.zoom.com/hc/en/article?id=zm_kb&sysparm_article=KB0066757#h_01H6PE29K2S6NPYCC3SWB667AT "https://support.zoom.com/hc/en/article?id=zm_kb&sysparm_article=KB0066757#h_01H6PE29K2S6NPYCC3SWB667AT").

1. Install the Zoom VDI Meeting client version 5.12.6+ within your WorkSpace.
2. Install the Zoom VDI Plugin (Windows Universal Installer) version 5.12.6+ on the
   client where your WorkSpace is installed
3. Validate the plugin is optimizing the Zoom traffic, by confirming that your VDI Plugin Status shows as **Connected** within the Zoom VDI client.
   For more information, see [How to confirm Amazon WorkSpaces optimization](https://support.zoom.com/hc/en/article?id=zm_kb&sysparm_article=KB0066757#h_01H6PE1MA5YMYFX5B5XM873V1Y "https://support.zoom.com/hc/en/article?id=zm_kb&sysparm_article=KB0066757#h_01H6PE1MA5YMYFX5B5XM873V1Y") .

### Enable Zoom Meeting Media Plugin for PCoIP

Users with administrative permission to Active Directory can generate a registry key
using their Group Policy Object (GPO). This allows users to send the registry key to all
the Windows WorkSpaces within your domain using a forced update. Alternatively, users with
administrative rights can also install registry keys individually on their WorkSpaces host.

#### Prerequisites

Before using the plugin, make sure the following requirements are met.

- Windows WorkSpaces client version 5.4.0+ with
  [Zoom VDI Plugin](https://support.zoom.com/hc/en/article?id=zm_kb&sysparm_article=KB0066757#h_01H6PE29K2S6NPYCC3SWB667AT:~:text=Zoom%20Meeting%20client.-,Install%20the%20Zoom%20VDI%20plugin,-To%20complete%20your "https://support.zoom.com/hc/en/article?id=zm_kb&sysparm_article=KB0066757#h_01H6PE29K2S6NPYCC3SWB667AT:~:text=Zoom%20Meeting%20client.-,Install%20the%20Zoom%20VDI%20plugin,-To%20complete%20your") version 5.12.6+.
- Within your WorkSpaces — [Zoom VDI Meeting](https://support.zoom.com/hc/en/article?id=zm_kb&sysparm_article=KB0063810 "https://support.zoom.com/hc/en/article?id=zm_kb&sysparm_article=KB0063810") client version 5.12.6+.

#### Create the registry key on a

Windows WorkSpaces host

Complete the following procedure to create a registry key on a Windows WorkSpaces host.
The registry key is required to use Zoom on Windows WorkSpaces.

1. Open Windows Registry Editor as an administrator.
2. Go to `\HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Amazon`.
3. If the **Extension** key doesn't exist, right-click and
   choose **New** > **Key** and name it
   **Extension**.
4. In the new **Extension** key, right-click and choose
   **New** > **DWORD** and name it
   **enable**. The name must be in lower-case.
5. Choose the new **DWORD** and change the **Value** to
   **1**.
6. Reboot the computer to complete the process.
7. On your WorkSpaces host, download and install the latest Zoom VDI client. On
   your WorkSpaces client (5.4 or higher), download and install the latest Zoom VDI
   client plugin for Amazon WorkSpaces. For more information, see [VDI releases and downloads](https://support.zoom.us/hc/en-us/articles/4415057249549-VDI-releases-and-downloads "https://support.zoom.us/hc/en-us/articles/4415057249549-VDI-releases-and-downloads") on the _Zoom support
   website_.

Launch Zoom to start your video call.

#### Troubleshooting

Complete the following actions to troubleshoot Zoom on Windows WorkSpaces.

- Confirm that The Registry Key Activation and Applied Correctly.
- Go to `C:\ProgramData\Amazon\Amazon WorkSpaces Extension`. You
  should see `wse_core_dll`.
- Make sure that the versions on the host and clients are correct and the
  same.

If you continue to experience difficulty, contact Support using the [Support Center](https://console.aws.amazon.com/support/home#/ "https://console.aws.amazon.com/support/home#/").

You can use the following examples to apply a GPO as an administrator of your
directory.

- **WSE.adml**

```
<?xml version="1.0" encoding="utf-8"?>
<policyDefinitionResources xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" revision="1.0" schemaVersion="1.0" xmlns="http://www.microsoft.com/GroupPolicy/PolicyDefinitions">
    <!-- 'displayName' and 'description' don't appear anywhere. All Windows native GPO template files have them set like this. -->
    <displayName>enter display name here</displayName>
    <description>enter description here</description>

    <resources>
    <stringTable>
        <string id="SUPPORTED_ProductOnly">N/A</string>
        <string id="Amazon">Amazon</string>
        <string id="Amazon_Help">Amazon Group Policies</string>
        <string id="WorkspacesExtension">Workspaces Extension</string>
        <string id="WorkspacesExtension_Help">Workspace Extension Group Policies</string>

        <!-- Extension Itself -->
        <string id="ToggleExtension">Enable/disable Extension Virtual Channel</string>
        <string id="ToggleExtension_Help">
Allows two-way Virtual Channel data communication for multiple purposes

By default, Extension is disabled.</string>

    </stringTable>
    </resources>
</policyDefinitionResources>
```

- **WSE.admx**

```
<?xml version="1.0" encoding="utf-8"?>
<policyDefinitions xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" revision="1.0" schemaVersion="1.0" xmlns="http://www.microsoft.com/GroupPolicy/PolicyDefinitions">
    <policyNamespaces>
        <target prefix="WorkspacesExtension" namespace="Microsoft.Policies.Amazon.WorkspacesExtension" />
    </policyNamespaces>
    <supersededAdm fileName="wse.adm" />
    <resources minRequiredRevision="1.0" />
    <supportedOn>
        <definitions>
            <definition name="SUPPORTED_ProductOnly" displayName="$(string.SUPPORTED_ProductOnly)"/>
        </definitions>
    </supportedOn>
    <categories>
        <category name="Amazon" displayName="$(string.Amazon)" explainText="$(string.Amazon_Help)" />
        <category name="WorkspacesExtension" displayName="$(string.WorkspacesExtension)" explainText="$(string.WorkspacesExtension_Help)">
            <parentCategory ref="Amazon" />
        </category>
    </categories>

    <policies>
        <policy name="ToggleExtension" class="Machine" displayName="$(string.ToggleExtension)" explainText="$(string.ToggleExtension_Help)" key="Software\Policies\Amazon\Extension" valueName="enable">
            <parentCategory ref="WorkspacesExtension" />
            <supportedOn ref="SUPPORTED_ProductOnly" />
            <enabledValue>
                <decimal value="1" />
            </enabledValue>
            <disabledValue>
                <decimal value="0" />
            </disabledValue>
        </policy>
    </policies>
</policyDefinitions>
```
