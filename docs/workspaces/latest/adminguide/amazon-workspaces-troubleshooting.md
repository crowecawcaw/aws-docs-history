# Troubleshoot issues for WorkSpaces Personal

The following information can help you troubleshoot issues with your WorkSpaces.

## Enabling advanced logging

To help troubleshoot issues that your users might experience, you can enable advanced
logging on any Amazon WorkSpaces client.

Advanced logging generates log files that contain diagnostic information and
debugging-level details, including verbose performance data. For the 1.0+ and 2.0+ clients,
these advanced logging files are automatically uploaded to a database in AWS.

###### Note

To get AWS review of advanced logging files, and to receive technical support
for issues with your WorkSpaces clients, contact AWS Support. For more information, see
[AWS Support Center](https://console.aws.amazon.com/support/home#/ "https://console.aws.amazon.com/support/home#/").

###### To enable advanced logging for Web Access

1. Open your Amazon WorkSpaces Web Access client.
2. At the top of the WorkSpaces sign in page, choose **Diagnostic logging**.
3. In the pop-up dialog box, ensure that **Diagnostic logging** is enabled.
4. For **Log level**, choose **Advanced logging**.

###### To access log files in Google Chrome, Microsoft Edge, and Firefox

1. Open the context (right-click) menu on the browsers or press **Ctrl**+**Shift**+**I**
   (or for Mac, **command**+**option**+**I**) on your keyboard to open the developer tools panel.
2. In the developer tools panel, choose the **Console** tab to find the log files.

###### To access log files in Safari

1. Choose **Safari**, **Settings**.
2. In the **Settings** window, choose the **Advanced** tab.
3. Choose **Show Develop menu in menu bar**.
4. From the **Develop** tab in the menu bar, choose **Develop** > **Show Web Inspector**.
5. In the Safari Web Inspector panel, choose the **Console** tab to find the log files.

###### Windows clients

The Windows client logs are stored in the following location:

`%LOCALAPPDATA%\Amazon Web Services\Amazon WorkSpaces\logs`

###### To enable advanced logging for Windows clients

1. Close the Amazon WorkSpaces client.
2. Open the Command Prompt app.
3. Launch the WorkSpaces client with the `-l3` flag.

`c:`

`cd "C:\Program Files\Amazon Web Services, Inc\Amazon WorkSpaces"`

`workspaces.exe -l3`

###### Note

If WorkSpaces is installed for one user and not all users, use the
following commands:

`c:`

`cd "%LocalAppData%\Programs\Amazon Web Services, Inc\Amazon WorkSpaces"`

`workspaces.exe -l3`

###### macOS clients

The macOS client logs are stored in the following location:

`~/Library/"Application Support"/"Amazon Web Services"/"Amazon WorkSpaces"/logs`

###### To enable advanced logging for macOS clients

1. Close the Amazon WorkSpaces client.
2. Open Terminal.
3. Run the following command.

`open -a workspaces --args -l3`

###### Android clients

###### To enable advanced logging for Android clients

1. Close the Amazon WorkSpaces client.
2. Open the Android client menu.
3. Select **Support**.
4. Select **Logging settings**.
5. Select **Enable advanced logging**.

###### To retrieve logs for Android clients after enabling advanced logging:

- Select **Extract log** to save zipped logs locally.

###### Linux clients

The Linux client logs are stored in the following location:

`~/.local/share/Amazon Web Services/Amazon WorkSpaces/logs`

###### To enable advanced logging for Linux clients

1. Close the Amazon WorkSpaces client.
2. Open Terminal.
3. Run the following command.

`/opt/workspacesclient/workspacesclient -l3`

###### Windows clients

The Windows client logs are stored in the following location:

`%LOCALAPPDATA%\Amazon Web Services\Amazon WorkSpaces\logs`

###### To enable advanced logging for Windows clients

1. Close the Amazon WorkSpaces client.
2. Open the Command Prompt app.
3. Launch the WorkSpaces client with the `-l3` flag.

`c:`

`cd "C:\Program Files (x86)\Amazon Web Services, Inc\Amazon WorkSpaces"`

`workspaces.exe -l3`

###### Note

If WorkSpaces is installed for one user and not all users, use the
following commands:

`c:`

`cd "%LocalAppData%\Programs\Amazon Web Services, Inc\Amazon WorkSpaces"`

`workspaces.exe -l3`

###### macOS clients

The macOS client logs are stored in the following location:

`~/Library/"Application Support"/"Amazon Web Services"/"Amazon WorkSpaces"/logs`

###### To enable advanced logging for macOS clients

1. Close the Amazon WorkSpaces client.
2. Open Terminal.
3. Run the following command.

`open -a workspaces --args -l3`

###### Android clients

###### To enable advanced logging for Android clients

1. Close the Amazon WorkSpaces client.
2. Open the Android client menu.
3. Select **Support**.
4. Select **Logging settings**.
5. Select **Enable advanced logging**.

###### To retrieve logs for Android clients after enabling advanced logging:

- Select **Extract log** to save zipped logs locally.

###### Linux clients

The Linux client logs are stored in the following location:

`~/.local/share/Amazon Web Services/Amazon WorkSpaces/logs`

###### To enable advanced logging for Linux clients

1. Close the Amazon WorkSpaces client.
2. Open Terminal.
3. Run the following command.

`/opt/workspacesclient/workspacesclient -l3`

1. Open the WorkSpaces client.
2. Choose the gear icon in the upper-right corner of the client
   application.
3. Choose **Advanced Settings**.
4. Select the **Enable Advanced Logging** check box.
5. Choose **Save**.
   The Windows client logs are stored in the following location:

`%LOCALAPPDATA%\Amazon Web Services\Amazon WorkSpaces\1.0\Logs`

The macOS client logs are stored in the following location:

`~/Library/Logs/Amazon Web Services/Amazon WorkSpaces/1.0`

## Troubleshoot specific issues

The following information can help you troubleshoot specific issues with your
WorkSpaces.

###### Issues

- [I can't create an Amazon Linux
  WorkSpace because there are non-valid characters in the user name](#linux_workspace_provision_fail_username "#linux_workspace_provision_fail_username")
- [I changed the shell
  for my Amazon Linux WorkSpace and now I can't provision a PCoIP session](#linux_workspace_provision_fail_shell_override "#linux_workspace_provision_fail_shell_override")
- [My Amazon Linux WorkSpaces
  won't start](#linux_workspace_provision_fail_pcoip_agent_upgrade "#linux_workspace_provision_fail_pcoip_agent_upgrade")
- [Launching WorkSpaces in my connected directory often
  fails](#provision_fail "#provision_fail")
- [Launching WorkSpaces fails with an internal
  error](#launch-failure-ipv6 "#launch-failure-ipv6")
- [When I try to register a directory, the
  registration fails and leaves the directory in an ERROR state](#cannot-register-directory "#cannot-register-directory")
- [My users can't connect to a Windows WorkSpace with an
  interactive logon banner](#logon_banner "#logon_banner")
- [My users can't connect to a Windows WorkSpace](#gpo_security_user_rights "#gpo_security_user_rights")
- [My users are having issues when they try to log
  on to WorkSpaces from WorkSpaces Web Access](#byol_logon_issues "#byol_logon_issues")
- [The Amazon WorkSpaces client displays a gray "Loading..."
  screen for a while before returning to the login screen. No other error message
  appears.](#loading_screen "#loading_screen")
- [My users receive the message "WorkSpace Status:
  Unhealthy. We were unable to connect you to your WorkSpace. Please try again in a
  few minutes."](#unhealthy_cant_connect "#unhealthy_cant_connect")
- [My users receive the message "This device is not
  authorized to access the WorkSpace. Please contact your administrator for assistance."](#device_not_authorized "#device_not_authorized")
- [My users receive the message "No network. Network connection lost.
  Check your network connection or contact your administrator for help." when trying to connect
  to a DCV WorkSpace](#no_network "#no_network")
- [The WorkSpaces client gives my users a network error, but
  they are able to use other network-enabled apps on their devices](#network_error "#network_error")
- [My WorkSpace users see the following error message:
  "Device can't connect to the registration service. Check your network settings."](#registration_service_failure "#registration_service_failure")
- [My PCoIP zero client users are receiving the error
  "The supplied certificate is invalid due to timestamp"](#pcoip_zero_client_ntp "#pcoip_zero_client_ntp")
- [USB printers and other USB peripherals aren't working for PCoIP
  zero clients](#pcoip_zero_client_usb "#pcoip_zero_client_usb")
- [My users skipped updating their Windows or macOS client
  applications and aren't getting prompted to install the latest version](#client_update_skipped "#client_update_skipped")
- [My users are unable to install the Android client application
  on their Chromebooks](#install_android_chromebook "#install_android_chromebook")
- [My users aren't receiving invitation emails or password reset emails](#welcome_emails "#welcome_emails")
- [My users don't see the Forgot password? option on the client login screen](#forgot_password "#forgot_password")
- [I receive the message "The system administrator has set
  policies to prevent this installation" when I try to install applications on a Windows WorkSpace](#msi_wont_install "#msi_wont_install")
- [No WorkSpaces in my directory can connect to the
  internet](#no_internet "#no_internet")
- [My WorkSpace has lost its internet access](#lost_internet_access "#lost_internet_access")
- [I receive a "DNS unavailable" error when I try to
  connect to my on-premises directory](#dns_unavailable "#dns_unavailable")
- [I receive a "Connectivity issues
  detected" error when I try to connect to my on-premises directory](#connectivity_issues_detected "#connectivity_issues_detected")
- [I receive an "SRV record" error when I try to
  connect to my on-premises directory](#srv_record_not_found "#srv_record_not_found")
- [My Windows WorkSpace goes to
  sleep when it's left idle](#windows_workspace_sleeps_when_idle "#windows_workspace_sleeps_when_idle")
- [One of my WorkSpaces has a state of
  UNHEALTHY](#unhealthy "#unhealthy")
- [My WorkSpace is unexpectedly crashing or rebooting](#crash_web_access "#crash_web_access")
- [The same username has more than
  one WorkSpace, but the user can log in to only one of the WorkSpaces](#multiple_workspaces_same_username "#multiple_workspaces_same_username")
- [I'm having trouble using Docker with Amazon WorkSpaces](#docker_support "#docker_support")
- [I receive ThrottlingException errors to some of my API calls](#throttled-api-calls "#throttled-api-calls")
- [My WorkSpace keeps disconnecting when I let it run in the background](#workspaces-disconnecting "#workspaces-disconnecting")
- [SAML 2.0 federation isn't working. My
  users are not authorized to stream their WorkSpaces desktop.](#saml-federation-not-working "#saml-federation-not-working")
- [My users are getting disconnected from
  their WorkSpaces session every 60 minutes.](#disconnected-workspace "#disconnected-workspace")
- [My users get a redirect URI error when they
  federate using the SAML 2.0 identity provider (IdP)-initiated flow, or an
  additional instance of the WorkSpaces client application starts every time my users
  attempt to sign in from the client after federating to the IdP.](#invalid-redirect-uri "#invalid-redirect-uri")
- [My users receive the message, "Something
  went wrong: An error occurred while launching your WorkSpace" when they attempt
  to sign in to the WorkSpaces client application after federating to the IdP.](#federating-error-message "#federating-error-message")
- [My users receive the message, "Unable to
  validate tags” when they attempt to sign in to the WorkSpaces client application
  after federating to the IdP.](#unable-to-validate-tags "#unable-to-validate-tags")
- [My users receive the message, "The client and
  the server cannot communicate, because they do not possess a common algorithm".](#no-common-algorithm "#no-common-algorithm")
- [My microphone or web cam is not working on
  Windows WorkSpaces.](#microphone-not-working "#microphone-not-working")
- [My users cannot log in using
  certificate-based authentication and are prompted for the password either at the
  WorkSpaces client or the Windows sign-on screen when they connect to their desktop
  session.](#cert-based-auth-troubleshooting "#cert-based-auth-troubleshooting")
- [I am trying to do something that
  requires Windows installation media but WorkSpaces does not provide it.](#install-media-troubleshooting "#install-media-troubleshooting")
- [I want to launch WorkSpaces with an existing AWS Managed Directory created in an
  unsupported WorkSpaces Region.](#unsupported-regions-troubleshooting "#unsupported-regions-troubleshooting")
- [I want to update Firefox on Amazon Linux 2.](#firefox_al2 "#firefox_al2")
- [My user is able to reset their password using the WorkSpaces client,
  ignoring the Fine Grained Password Policy (FFGP) setting that is configured on AWS Managed Microsoft AD.](#password-setting-mad "#password-setting-mad")
- [My users receive the error message "This OS/platform is not authorized to access your WorkSpace"
  when trying to access the Windows/Linux WorkSpace using Web Access](#os-authorized-access "#os-authorized-access")
- [My user's WorkSpace is showing as unhealthy after they connect
  to an AutoStop WorkSpace that is in the stopped state](#autostop-unhealthy "#autostop-unhealthy")
- [Gnome crashes on WorkSpaces Ubuntu bundles after
  login](#gnome-crashes-ubuntu "#gnome-crashes-ubuntu")

### I can't create an Amazon Linux

WorkSpace because there are non-valid characters in the user name

For Amazon Linux WorkSpaces, user names:

- Can contain a maximum of 20 characters
- Can contain letters, spaces, and numbers that are representable in
  UTF-8
- Can include the following special characters: \_.-#
- Cannot begin with a dash symbol (-) as the first character of the user
  name

###### Note

These limitations do not apply to Windows WorkSpaces. Windows WorkSpaces support the @
and - symbols for all characters in the user name.

### I changed the shell

for my Amazon Linux WorkSpace and now I can't provision a PCoIP session

To override the default shell for Linux WorkSpaces, see [Override the default shell for Amazon Linux WorkSpaces](manage_linux_workspace.md#linux_shell "manage_linux_workspace.md#linux_shell").

### My Amazon Linux WorkSpaces

won't start

Starting July 20, 2020, Amazon Linux WorkSpaces will be using new license certificates.
These new certificates are compatible only with versions 2.14.1.1, 2.14.7, 2.14.9,
and 20.10.6 or later of the PCoIP agent.

If you're using an unsupported version of the PCoIP agent, you must upgrade it to
the latest version (20.10.6), which has the latest fixes and performance
improvements that are compatible with the new certificates. If you don't make these
upgrades by July 20, session provisioning for your Linux WorkSpaces will fail and your
end users won't be able to connect to their WorkSpaces.

###### To upgrade your PCoIP agent to the latest version

1. Open the WorkSpaces console at [https://console.aws.amazon.com/workspaces/v2/home](https://console.aws.amazon.com/workspaces/v2/home "https://console.aws.amazon.com/workspaces/v2/home").
2. In the navigation pane, choose **WorkSpaces**.
3. Select your Linux WorkSpace, and reboot it by choosing **Actions**,
   **Reboot WorkSpaces**. If the WorkSpace status is `STOPPED`,
   you must choose **Actions**, **Start WorkSpaces**
   first and wait until its status is `AVAILABLE` before you can reboot it.
4. After your WorkSpace has rebooted and its status is `AVAILABLE`, we recommend
   that you change the status of the WorkSpace to `ADMIN_MAINTENANCE` while you are
   performing this upgrade. When you are finished, change the status of the WorkSpace to
   `AVAILABLE`. For more information about `ADMIN_MAINTENANCE` mode, see
   [Manual Maintenance](workspace-maintenance.md#admin-maintenance "workspace-maintenance.md#admin-maintenance").

To change the status of a WorkSpace to `ADMIN_MAINTENANCE`, do the
following:

    1. Select the WorkSpace and choose **Actions**, **Modify WorkSpace**.
    2. Choose **Modify State**.
    3. For **Intended State**, select **ADMIN\_MAINTENANCE**.
    4. Choose **Modify**.

5. Connect to your Linux WorkSpace through SSH. For more information, see
   [Enable SSH connections for
   your Linux WorkSpaces in WorkSpaces Personal](connect-to-linux-workspaces-with-ssh.md "connect-to-linux-workspaces-with-ssh.md").
6. To update the PCoIP agent, run the following command:

```
sudo yum --enablerepo=pcoip-stable install pcoip-agent-standard-20.10.6
```

7. To verify the agent version and to confirm that the update succeeded, run the
   following command:

```
rpm -q pcoip-agent-standard
```

The verification command should produce following result:

```
pcoip-agent-standard-20.10.6-1.el7.x86_64
```

8. Disconnect from the WorkSpace and reboot it again.
9. If you set the status of the WorkSpace to `ADMIN_MAINTENANCE` in
   [Step 4](#step_maintenance_mode "#step_maintenance_mode"), repeat [Step 4](#step_maintenance_mode "#step_maintenance_mode")
   and set **Intended State** to `AVAILABLE`.

If your Linux WorkSpace still fails to start after you upgrade the PCoIP agent, contact
AWS Support.

### Launching WorkSpaces in my connected directory often

fails

Verify that the two DNS servers or domain controllers in your on-premises
directory are accessible from each of the subnets that you specified when you
connected to your directory. You can verify this connectivity by launching an Amazon EC2
instance in each subnet and joining the instance to your directory using the IP
addresses of the two DNS servers.

### Launching WorkSpaces fails with an internal

error

Check whether your subnets are configured to automatically assign IPv6 addresses
to instances launched in the subnet. To check this setting, open the Amazon VPC console,
select your subnet, and choose **Subnet Actions**, **Modify
auto-assign IP settings**. If this setting is enabled, you cannot
launch WorkSpaces using the Performance or Graphics bundles. Instead, disable this
setting and specify IPv6 addresses manually when you launch your instances.

### When I try to register a directory, the

registration fails and leaves the directory in an ERROR state

This problem can occur if you're trying to register an AWS Managed Microsoft AD
directory that has been configured for multi-Region replication. Although the directory
in the primary Region can be successfully registered for use with Amazon WorkSpaces,
attempting to register the directory in a replicated Region fails. Multi-Region replication
with AWS Managed Microsoft AD isn't supported for use with Amazon WorkSpaces within replicated
Regions.

### My users can't connect to a Windows WorkSpace with an

interactive logon banner

If an interactive logon message has been implemented to display a logon banner,
this prevents users from being able to access their Windows WorkSpaces. The interactive
logon message Group Policy setting is not currently supported by PCoIP WorkSpaces. Move the
WorkSpaces to an organizational unit (OU) where the **Interactive logon: Message
text for users attempting to log on** Group Policy isn’t applied.
The logon message is supported on DCV WorkSpaces, and users have to login again after
accepting the logon banner.

### My users can't connect to a Windows WorkSpace

My users receive the following error when they try to connect to their Windows
WorkSpaces:

```
"An error occurred while launching your WorkSpace. Please try again."
```

This error often occurs when the WorkSpace can't load the Windows desktop using PCoIP.
Check the following:

- This message appears if the PCoIP Standard Agent for Windows service is not
  running. [Connect using RDP](https://aws.amazon.com/premiumsupport/knowledge-center/connect-workspace-rdp/ "https://aws.amazon.com/premiumsupport/knowledge-center/connect-workspace-rdp/")
  to verify that the service is running, that it's set to start automatically, and
  that it can communicate over the management interface (eth0).

- If the PCoIP agent was uninstalled, reboot the WorkSpace through the Amazon WorkSpaces
  console to reinstall it automatically.

- You might also receive this error on the Amazon WorkSpaces client after a long
  delay if the [WorkSpaces
  security group](amazon-workspaces-security-groups.md "amazon-workspaces-security-groups.md") was modified to restrict outbound traffic.
  Restricting outbound traffic prevents Windows from communicating with your
  directory controllers for login. Verify that your security groups allow your
  WorkSpaces to communicate with your directory controllers on all [required ports](workspaces-port-requirements.md "workspaces-port-requirements.md") over the
  primary network interface.

Another cause of this error is related to the User Rights Assignment Group Policy.
If the following group policy is incorrectly configured, it prevents users from
being able to access their Windows WorkSpaces:

**Computer Configuration\Windows Settings\Security Settings\Local Policies\User Rights Assignment**

- **Incorrect policy:**

Policy: **Access this computer from the network**

Setting: `Domain name`\Domain Computers

Winning GPO: Allow File Access

- **Correct policy:**

Policy: **Access this computer from the network**

Setting: `Domain name`\Domain Users

Winning GPO: Allow File Access

###### Note

This policy setting should be applied to **Domain Users** instead of
**Domain Computers**.

For more information, see [Access this computer from the network - security policy setting](https://docs.microsoft.com/windows/security/threat-protection/security-policy-settings/access-this-computer-from-the-network "https://docs.microsoft.com/windows/security/threat-protection/security-policy-settings/access-this-computer-from-the-network") and [Configure security policy settings](https://docs.microsoft.com/windows/security/threat-protection/security-policy-settings/how-to-configure-security-policy-settings "https://docs.microsoft.com/windows/security/threat-protection/security-policy-settings/how-to-configure-security-policy-settings") in the Microsoft Windows documentation.

### My users are having issues when they try to log

on to WorkSpaces from WorkSpaces Web Access

Amazon WorkSpaces relies on a specific logon screen configuration to enable users to
successfully log on from their Web Access client.

To enable Web Access users to log on to their WorkSpaces, you must configure a Group
Policy setting and three Security Policy settings. If these settings are not
correctly configured, users might experience long logon times or black screens when
they try to log on to their WorkSpaces. To configure these settings, see [Enable and configure WorkSpaces Web Access for WorkSpaces Personal](web-access.md "web-access.md").

###### Important

Beginning October 1, 2020, customers will no longer be able to use the
Amazon WorkSpaces Web Access client to connect to Windows 7 custom WorkSpaces or to Windows 7
Bring Your Own License (BYOL) WorkSpaces.

### The Amazon WorkSpaces client displays a gray "Loading..."

screen for a while before returning to the login screen. No other error message
appears.

This behavior usually indicates that the WorkSpaces client can authenticate over port
443, but can't establish a streaming connection over port 4172 (PCoIP) or port 4195
(DCV). This situation can occur when [network prerequisites](workspaces-port-requirements.md "workspaces-port-requirements.md") aren't met.
Issues on the client side often cause the network check in the client to fail. To
see which health checks are failing, choose the network check icon (typically a red
triangle with an exclamation point in the bottom-right corner of the login screen
for 2.0+ clients or the network icon
![Network icon](images/network-icon.png)
in the upper-right corner of the 3.0+ clients).

###### Note

The most common cause of this problem is a client-side firewall or proxy preventing
access over port 4172 or 4195 (TCP and UDP). If this health check fails, check your local
firewall settings.

If the network check passes, there might be a problem with the network configuration
of the WorkSpace. For example, a Windows Firewall rule might block port UDP 4172 or 4195 on the
management interface. [Connect to the WorkSpace using a Remote Desktop Protocol (RDP) client](https://aws.amazon.com/premiumsupport/knowledge-center/connect-workspace-rdp/ "https://aws.amazon.com/premiumsupport/knowledge-center/connect-workspace-rdp/") to verify
that the WorkSpace meets the necessary [port requirements](workspaces-port-requirements.md "workspaces-port-requirements.md").

### My users receive the message "WorkSpace Status:

Unhealthy. We were unable to connect you to your WorkSpace. Please try again in a
few minutes."

This error usually indicates the SkyLightWorkSpacesConfigService service isn't
responding to health checks.

If you just rebooted or started your WorkSpace, wait a few minutes, and then try again.

If the WorkSpace has been running for some time and you still see this error,
[connect using RDP](https://aws.amazon.com/premiumsupport/knowledge-center/connect-workspace-rdp/ "https://aws.amazon.com/premiumsupport/knowledge-center/connect-workspace-rdp/")
to verify that the SkyLightWorkSpacesConfigService service:

- Is running.

- Is set to start automatically.

- Can communicate over the management interface (eth0).

- Isn't blocked by any third-party antivirus software.

### My users receive the message "This device is not

authorized to access the WorkSpace. Please contact your administrator for assistance."

This error indicates that one of the following might be occurring:

- [IP access control
  groups](amazon-workspaces-ip-access-control-groups.md "amazon-workspaces-ip-access-control-groups.md") are configured on the WorkSpace directory, but the client IP
  address isn't allowlisted.

Check the settings on your directory. Confirm that the public IP address the user is
connecting from allows access to the WorkSpace.

- Under access control, your device’s operating system isn’t allowed as a trusted
  device or your device doesn’t have the proper certificates installed when using the
  **Trusted devices** option. Add your device type as a trusted device
  by doing the following:
  1.  Open the WorkSpaces console at [https://console.aws.amazon.com/workspaces/v2/home](https://console.aws.amazon.com/workspaces/v2/home "https://console.aws.amazon.com/workspaces/v2/home").
  2.  In the navigation pane, choose **Directories**.
  3.  Choose the directory you're using.
  4.  Scroll down to **Access control options** and choose
      **Edit**.
  5.  Under **Trusted devices**, for the device types you want to
      allow access to, choose **Allow all** in the drop-down. If you
      want to restrict the devices to ones that have client certificates installed, choose
      **Trusted devices**.
  6.  If you chose **Trusted devices** in the previous step, ensure
      you have imported at least one root certificate and that the client certificate
      that has been issued by the root certification authority (CA) has been installed
      on the client. For more information about creating, deploying, and importing root
      certificates, see [Restrict access to trusted devices for WorkSpaces Personal](trusted-devices.md "trusted-devices.md").
  7.  Choose **Save**.

- Your device types are not granted access to WorkSpaces. Grant access to your device type by
  doing the following:
  1.  Open the WorkSpaces console at [https://console.aws.amazon.com/workspaces/v2/home](https://console.aws.amazon.com/workspaces/v2/home "https://console.aws.amazon.com/workspaces/v2/home").
  2.  In the navigation pane, choose **Directories**.
  3.  Choose the directory you're using.
  4.  Scroll down to **Other platforms** and choose
      **Edit**.
  5.  Check from one of the following device types you want to grant WorkSpaces access.
      - ChromeOS
      - iOS
      - Linux
      - Web Access
      - Zero Clients

  6.  Choose **Save**.

### My users receive the message "No network. Network connection lost.

Check your network connection or contact your administrator for help." when trying to connect
to a DCV WorkSpace

If this error occurs and your users don't have connectivity issues, make sure that
port 4195 is open on your network's firewalls. For WorkSpaces using DCV,
the port used to stream the client session was changed from 4172 to 4195.

### The WorkSpaces client gives my users a network error, but

they are able to use other network-enabled apps on their devices

The WorkSpaces client applications rely on access to resources in the AWS Cloud, and
require a connection that provides at least 1 Mbps download bandwidth. If a device
has an intermittent connection to the network, the WorkSpaces client application
might report an issue with the network.

WorkSpaces enforces the use of digital certificates issued by Amazon Trust Services, as
of May 2018. Amazon Trust Services is already a trusted Root CA on the operating
systems that are supported by WorkSpaces. If the Root CA list for the operating system is
not up to date, the device cannot connect to WorkSpaces and the client gives a network
error.

###### To recognize connection issues due to certificate failures

- PCoIP zero clients — The following error message is
  displayed.

```
Failed to connect. The server provided a certificate that is invalid. See below for details:
- The supplied certificate is invalid due to timestamp
- The supplied certificate is not rooted in the devices local certificate store
```

- Other clients — The health checks fail with a red warning triangle for **Internet**.

###### To resolve certificate failures

- [Windows client application](#certificate-issues-windows "#certificate-issues-windows")
- [PCoIP zero clients](#certificate-issues-zero-clients "#certificate-issues-zero-clients")
- [Other client applications](#certificate-issues-other "#certificate-issues-other")

#### Windows client application

Use one of the following solutions for certificate failures.

###### Solution 1: Update the client application

Download and install the latest Windows client application from [https://clients.amazonworkspaces.com/](https://clients.amazonworkspaces.com/ "https://clients.amazonworkspaces.com/")

.
During installation, the client application ensures that your operating system trusts certificates
issued by Amazon Trust Services.

###### Solution 2: Add Amazon Trust Services to the local Root CA list

1. Open [https://www.amazontrust.com/repository/](https://www.amazontrust.com/repository/ "https://www.amazontrust.com/repository/").
2. Download the Starfield certificate in DER format (2b071c59a0a0ae76b0eadb2bad23bad4580b69c3601b630c2eaf0613afa83f92).
3. Open the Microsoft Management Console. (From the Command Prompt, run
   **mmc**.)
4. Choose **File**, **Add/Remove Snap-in**, **Certificates**,
   **Add**.
5. On the **Certificates snap-in** page, select **Computer account**
   and choose **Next**. Keep the default, **Local computer**.
   Choose **Finish**. Choose **OK**.
6. Expand **Certificates (Local Computer)** and select **Trusted Root
   Certification Authorities**. Choose **Action**, **All Tasks**,
   **Import**.
7. Follow the wizard to import the certificate that you downloaded.
8. Exit and restart the WorkSpaces client application.

###### Solution 3: Deploy Amazon Trust Services as a trusted CA using Group Policy

Add the Starfield certificate to the trusted Root CAs for the domain using
Group Policy. For more information, see [Use Policy to Distribute Certificates](<https://docs.microsoft.com/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/cc772491(v=ws.11)> "https://docs.microsoft.com/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/cc772491(v=ws.11)").

#### PCoIP zero clients

To connect directly to a WorkSpace using firmware version 6.0 or later, download and install the
certificate issued by Amazon Trust Services.

###### To add Amazon Trust Services as a trusted Root CA

1. Open [https://certs.secureserver.net/repository/](https://certs.secureserver.net/repository/ "https://certs.secureserver.net/repository/").
2. Download the certificate under **Starfield Certificate
   Chain** with the thumbprint 14 65 FA 20 53 97 B8 76 FA A6 F0 A9
   95 8E 55 90 E4 0F CC 7F AA 4F B7 C2 C8 67 75 21 FB 5F B6 58.
3. Upload the certificate to the zero client. For more information, see
   [Uploading Certificates](https://www.teradici.com/web-help/TER1504003/6.0/default.htm#05_Managing/04_UploadCertificate.htm "https://www.teradici.com/web-help/TER1504003/6.0/default.htm#05_Managing/04_UploadCertificate.htm") in the Teradici documentation.

#### Other client applications

Add the Starfield certificate (2b071c59a0a0ae76b0eadb2bad23bad4580b69c3601b630c2eaf0613afa83f92)
from [Amazon Trust Services](https://www.amazontrust.com/repository/ "https://www.amazontrust.com/repository/"). For more
information about how to add a Root CA, see the following documentation:

- Android: [Add & remove certificates](https://support.google.com/nexus/answer/2844832 "https://support.google.com/nexus/answer/2844832")
- Chrome OS: [Manage client certificates on Chrome devices](https://support.google.com/chrome/a/answer/6080885 "https://support.google.com/chrome/a/answer/6080885")
- macOS and iOS: [Installing a CA's Root Certificate on Your Test Device](https://developer.apple.com/library/content/qa/qa1948/_index.html#/apple_ref/doc/uid/DTS40017603-CH1-SECINSTALLING "https://developer.apple.com/library/content/qa/qa1948/_index.html#/apple_ref/doc/uid/DTS40017603-CH1-SECINSTALLING")

### My WorkSpace users see the following error message:

"Device can't connect to the registration service. Check your network settings."

When a registration service failure occurs, your WorkSpace users might see the
following error message on the **Connection Health Check** page:
"Your device is not able to connect to the WorkSpaces Registration service. You will not
be able to register your device with WorkSpaces. Please check your network
settings."

This error occurs when the WorkSpaces client application can't reach the registration
service. Typically, this happens when the WorkSpaces directory has been deleted. To
resolve this error, make sure that the registration code is valid and corresponds to
a running directory in the AWS Cloud.

### My PCoIP zero client users are receiving the error

"The supplied certificate is invalid due to timestamp"

If Network Time Protocol (NTP) isn't enabled in Teradici, your PCoIP zero client users might receive
certificate failure errors. To set up NTP, see [Set up PCoIP zero clients for WorkSpaces Personal](set-up-pcoip-zero-client.md "set-up-pcoip-zero-client.md").

### USB printers and other USB peripherals aren't working for PCoIP

zero clients

Starting with version 20.10.4 of the PCoIP agent, Amazon WorkSpaces disables USB redirection by default through
the Windows registry. This registry setting affects the behavior of USB peripherals when your users are
using PCoIP zero client devices to connect to their WorkSpaces.

If your WorkSpaces are using version 20.10.4 or later of the PCoIP agent, USB
peripheral devices won't work with PCoIP zero client devices until you've enabled
USB redirection.

###### Note

If you're using 32-bit virtual printer drivers, you must also update those drivers to their 64-bit
versions.

###### To enable USB redirection for PCoIP zero client devices

We recommend that you push out these registry changes to your WorkSpaces through
Group Policy. For more information, see [Configuring the agent](https://www.teradici.com/web-help/pcoip_agent/standard_agent/windows/20.10/admin-guide/configuring/configuring/ "https://www.teradici.com/web-help/pcoip_agent/standard_agent/windows/20.10/admin-guide/configuring/configuring/") and [Configurable settings](https://www.teradici.com/web-help/pcoip_agent/standard_agent/windows/20.10/admin-guide/configuring/configuring/#enabledisable-usb-in-the-pcoip-session "https://www.teradici.com/web-help/pcoip_agent/standard_agent/windows/20.10/admin-guide/configuring/configuring/#enabledisable-usb-in-the-pcoip-session") in the Teradici documentation.

1. Set the following registry key value to 1 (enabled):

KeyPath = **HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Teradici\PCoIP\pcoip_admin**

KeyName = **pcoip.enable_usb**

KeyType = **DWORD**

KeyValue = **1** 2. Set the following registry key value to 1 (enabled):

KeyPath = **HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Teradici\PCoIP\pcoip_admin_defaults**

KeyName = **pcoip.enable_usb**

KeyType = **DWORD**

KeyValue = **1** 3. If you haven't already done so, log out of the WorkSpace, and then log back in. Your USB
devices should now work.

### My users skipped updating their Windows or macOS client

applications and aren't getting prompted to install the latest version

When users skip updates to the Amazon WorkSpaces Windows client application, the **SkipThisVersion**
registry key gets set, and they are no longer prompted to update their clients when a new version of
the client is released. To update to the latest version, you can edit the registry as described
in [Update the WorkSpaces Windows Client Application to a Newer Version](../userguide/amazon-workspaces-windows-client.md#windows_setup "../userguide/amazon-workspaces-windows-client.md#windows_setup") in the
_Amazon WorkSpaces User Guide_. You can also run the following PowerShell command:

```
Remove-ItemProperty -Path "HKCU:\Software\Amazon Web Services. LLC\Amazon WorkSpaces\WinSparkle" -Name "SkipThisVersion"
```

When users skip updates to the Amazon WorkSpaces macOS client application, the `SUSkippedVersion`
preference gets set, and they are no longer prompted to update their clients when a new version of the
client is released. To update to the latest version, you can reset this preference as described in
[Update the WorkSpaces macOS Client Application to a Newer Version](../userguide/amazon-workspaces-osx-client.md#osx_setup "../userguide/amazon-workspaces-osx-client.md#osx_setup") in the
_Amazon WorkSpaces User Guide_.

### My users are unable to install the Android client application

on their Chromebooks

Version 2.4.13 is the final release of the Amazon WorkSpaces Chromebook client
application. Because [Google is phasing out support for Chrome Apps](https://blog.chromium.org/2020/01/moving-forward-from-chrome-apps.html "https://blog.chromium.org/2020/01/moving-forward-from-chrome-apps.html"), there will be no further
updates to the WorkSpaces Chromebook client application, and its use is
unsupported.

For [Chromebooks that support installing Android applications](https://sites.google.com/a/chromium.org/dev/chromium-os/chrome-os-systems-supporting-android-apps "https://sites.google.com/a/chromium.org/dev/chromium-os/chrome-os-systems-supporting-android-apps"), we recommend using the
[WorkSpaces Android client application](../userguide/amazon-workspaces-android-client.md "../userguide/amazon-workspaces-android-client.md") instead.

In some cases, you might need to enable your users' Chromebooks to install Android applications. For more information,
see [Set up Android for Chromebook for WorkSpaces Personal](set-up-android-chromebook.md "set-up-android-chromebook.md").

### My users aren't receiving invitation emails or password reset emails

Users do not automatically receive welcome or password reset emails for WorkSpaces that were created using
AD Connector or a trusted domain. Invitation emails also aren't sent automatically if the user already
exists in Active Directory.

To manually send welcome emails to these users, see
[Send an invitation email](manage-workspaces-users.md#send-invitation "manage-workspaces-users.md#send-invitation").

To reset user passwords, see [Set up Active Directory Administration Tools for WorkSpaces Personal](directory_administration.md "directory_administration.md").

### My users don't see the Forgot password? option on the client login screen

If you're using AD Connector or a trusted domain, your users won't be able to
reset their own passwords. (The **Forgot password?** option on the
WorkSpaces client application login screen won't be available.) For information about how
to reset user passwords, see [Set up Active Directory Administration Tools for WorkSpaces Personal](directory_administration.md "directory_administration.md").

### I receive the message "The system administrator has set

policies to prevent this installation" when I try to install applications on a Windows WorkSpace

You can address this issue by modifying the Windows Installer Group Policy
setting. To deploy this policy to multiple WorkSpaces in your directory, apply this
setting to a Group Policy object that is linked to the WorkSpaces organizational unit
(OU) from a domain-joined EC2 instance. If you are using AD Connector, you can make
these changes from a domain controller. For more information about using the Active
Directory administration tools to work with Group Policy objects, see [Installing
the Active Directory Administration Tools](../../../directoryservice/latest/admin-guide/ms_ad_install_ad_tools.md "../../../directoryservice/latest/admin-guide/ms_ad_install_ad_tools.md") in the
_AWS Directory Service Administration Guide_.

The following procedure shows how to configure the Windows Installer setting for the WorkSpaces Group
Policy object.

1. Make sure that the most recent [WorkSpaces Group
   Policy administrative template](group_policy.md#gp_install_template "group_policy.md#gp_install_template") is installed in your domain.
2. Open the Group Policy Management tool on your Windows WorkSpace client and
   navigate to and select the WorkSpaces Group Policy object for your WorkSpaces machine
   accounts. From the main menu, choose **Action**,
   **Edit**.
3. In the Group Policy Management Editor, choose **Computer
   Configuration**, **Policies**,
   **Administrative Templates**, **Classic
   Administrative Templates**, **Windows Components**,
   **Windows Installer**.
4. Open the **Turn Off Windows Installer** setting.
5. In the **Turn Off Windows Installer** dialog box, change **Not Configured**
   to **Enabled**, and then set **Disable Windows Installer** to **Never**.
6. Choose **OK**.
7. To apply the group policy changes, do one of the following:
   - Reboot the WorkSpace (in the WorkSpaces console, select the WorkSpace, then choose
     **Actions**, **Reboot WorkSpaces**).
   - From an administrative command prompt, enter **gpupdate /force**.

### No WorkSpaces in my directory can connect to the

internet

WorkSpaces cannot communicate with the internet by default. You must explicitly provide
internet access. For more information, see [Provide internet access for WorkSpaces Personal](amazon-workspaces-internet-access.md "amazon-workspaces-internet-access.md").

### My WorkSpace has lost its internet access

If your WorkSpace has lost access to the internet and you can't
[connect to the WorkSpace by using RDP](https://aws.amazon.com/premiumsupport/knowledge-center/connect-workspace-rdp/ "https://aws.amazon.com/premiumsupport/knowledge-center/connect-workspace-rdp/"),
this issue is probably caused by the loss of the public IP address for the WorkSpace. If you
have [enabled automatic assignment of Elastic IP addresses](automatic-assignment.md "automatic-assignment.md")
at the directory level, an [Elastic IP address](../../../vpc/latest/userguide/vpc-eips.md "../../../vpc/latest/userguide/vpc-eips.md") (from the Amazon-provided pool) is assigned to your WorkSpace when it is
launched. However, if you associate an Elastic IP address that you own to a WorkSpace, and then you
later disassociate that Elastic IP address from the WorkSpace, the WorkSpace loses its public IP
address, and it doesn't automatically get a new one from the Amazon-provided pool.

To associate a new public IP address from the Amazon-provided pool with the WorkSpace, you must
[rebuild the WorkSpace](rebuild-workspace.md "rebuild-workspace.md"). If you don't want to rebuild the WorkSpace,
you must associate another Elastic IP address that you own to the WorkSpace.

We recommend that you not modify the elastic network interface of a WorkSpace
after the WorkSpace is launched. After an Elastic IP address has been assigned to a
WorkSpace, the WorkSpace retains the same public IP address (unless the WorkSpace is
rebuilt, in which case it gets a new public IP address).

### I receive a "DNS unavailable" error when I try to

connect to my on-premises directory

You receive an error message similar to the following when connecting to your
on-premises directory.

```
DNS unavailable (TCP port 53) for IP: dns-ip-address
```

AD Connector must be able to communicate with your on-premises DNS servers via
TCP and UDP over port 53. Verify that your security groups and on-premises firewalls
allow TCP and UDP communication over this port.

### I receive a "Connectivity issues

detected" error when I try to connect to my on-premises directory

You receive an error message similar to the following when connecting to your
on-premises directory.

```
Connectivity issues detected: LDAP unavailable (TCP port 389) for IP: ip-address
Kerberos/authentication unavailable (TCP port 88) for IP: ip-address
Please ensure that the listed ports are available and retry the operation.
```

AD Connector must be able to communicate with your on-premises domain
controllers via TCP and UDP over the following ports. Verify that your security
groups and on-premises firewalls allow TCP and UDP communication over these
ports:

- 88 (Kerberos)
- 389 (LDAP)

### I receive an "SRV record" error when I try to

connect to my on-premises directory

You receive an error message similar to one or more of the following when
connecting to your on-premises directory.

```
SRV record for LDAP does not exist for IP: dns-ip-address

SRV record for Kerberos does not exist for IP: dns-ip-address
```

AD Connector needs to obtain the
`_ldap._tcp.`dns-domain-name`` and
 `_kerberos._tcp.`dns-domain-name`` SRV
records when connecting to your directory. You get this error if the service cannot
obtain these records from the DNS servers that you specified when connecting to your
directory. Make sure that your DNS servers contain these SRV records. For more
information, see [SRV Resource
Records](https://technet.microsoft.com/en-us/library/cc961719.aspx "https://technet.microsoft.com/en-us/library/cc961719.aspx") on Microsoft TechNet.

### My Windows WorkSpace goes to

sleep when it's left idle

To resolve this issue, connect to the WorkSpace and change the power plan to
**High performance** by using the following procedure:

1. From the WorkSpace, open **Control Panel**, then choose
   **Hardware** or choose **Hardware and Sound**
   (the name might differ, depending on your version of Windows).
2. Under **Power Options**, choose **Choose a power
   plan**.
3. In the **Choose or customize a power plan** pane, choose
   the **High performance** power plan, and then choose
   **Change plan settings**.
   - If the option to choose the **High performance**
     power plan is disabled, choose **Change settings that are
     currently unavailable**, and then choose the
     **High performance** power plan.
   - If the **High performance** plan isn't visible,
     choose the arrow to the right of **Show additional plans**
     to display it, or choose **Create a power plan** in
     the left navigation, choose **High performance**,
     give the power plan a name, and then choose **Next**.

4. On the **Change settings for the plan: High performance**
   page, make sure **Turn off the display** and (if available)
   **Put the computer to sleep** are set to **Never**.
5. If you made any changes to the high performance plan, choose
   **Save changes** (or choose **Create** if you're
   creating a new plan).

If the preceding steps do not solve the issue, do the following:

1. From the WorkSpace, open **Control Panel**, then choose
   **Hardware** or choose **Hardware and Sound**
   (the name might differ, depending on your version of Windows).
2. Under **Power Options**, choose **Choose a power
   plan**.
3. In the **Choose or customize a power plan** pane, choose
   the **Change plan settings** link to the right of the
   **High performance** power plan, then choose the
   **Change advanced power settings** link.
4. In the **Power Options** dialog box, in the list of
   settings, choose the plus sign to the left of **Hard disk**
   to display the relevant settings.
5. Verify that the **Turn off hard disk after** value for
   **Plugged in** is greater than the value for
   **On battery** (the default value is 20
   minutes).
6. Choose the plus sign to the left of **PCI Express**, and
   do the same for **Link State Power Management**.
7. Verify that the **Link State Power Management** settings
   are **Off**.
8. Choose **OK** (or **Apply** if you
   changed any settings) to close the dialog box.
9. In the **Change settings for the plan** pane, if you
   changed any settings, choose **Save changes**.

### One of my WorkSpaces has a state of

`UNHEALTHY`

The WorkSpaces service periodically sends status requests to a WorkSpace. A WorkSpace
is marked `UNHEALTHY` when it fails to respond to these requests. Common
causes for this problem are:

- An application on the WorkSpace is blocking network ports, which prevents
  the WorkSpace from responding to the status request.
- High CPU utilization is preventing the WorkSpace from responding to the
  status request in a timely manner.
- The computer name of the WorkSpace has been changed. This prevents a
  secure channel from being established between WorkSpaces and the
  WorkSpace.

You can attempt to correct the situation using the following methods:

- Reboot the WorkSpace from the WorkSpaces console.
- Connect to the unhealthy WorkSpace using the following procedure, which
  should be used only for troubleshooting purposes:
  1.  Connect to an operational WorkSpace in the same directory as the
      unhealthy WorkSpace.
  2.  From the operational WorkSpace, use Remote Desktop Protocol (RDP)
      to connect to the unhealthy WorkSpace using the IP address of the
      unhealthy WorkSpace. Depending on the extent of the problem, you
      might not be able to connect to the unhealthy WorkSpace.
  3.  On the unhealthy WorkSpace, confirm that the minimum
      [port requirements](workspaces-port-requirements.md "workspaces-port-requirements.md")
      are met.

- Make sure the SkyLightWorkSpacesConfigService service can respond to health checks.
  To troubleshoot this issue, see [My users receive the message "WorkSpace Status:
  Unhealthy. We were unable to connect you to your WorkSpace. Please try again in a
  few minutes."](#unhealthy_cant_connect "#unhealthy_cant_connect").
- Rebuild the WorkSpace from the WorkSpaces console. Because rebuilding a
  WorkSpace can potentially cause a loss of data, this option should be
  used only if all other attempts to correct the problem have been
  unsuccessful.

### My WorkSpace is unexpectedly crashing or rebooting

If your WorkSpace configured for PCoIP is repeatedly crashing or rebooting and your error logs or crash dumps are
pointing to problems with `spacedeskHookKmode.sys` or
`spacedeskHookUmode.dll`, or if you're receiving the following error messages,
you might need to disable Web Access to the WorkSpace:

```
The kernel power manager has initiated a shutdown transition.
Shutdown reason: Kernel API
```

```
The computer has rebooted from a bugcheck.
```

###### Note

- These troubleshooting steps are not applicable to WorkSpaces that are
  configured for DCV. They are applicable only to WorkSpaces that
  are configured for PCoIP.
- You should disable Web Access only if you aren't allowing your users to use Web Access.

To disable Web Access to the WorkSpace, you must disable Web Access in the WorkSpaces directory and reboot the WorkSpace.

### The same username has more than

one WorkSpace, but the user can log in to only one of the WorkSpaces

If you delete a user in Active Directory (AD) without first deleting their
WorkSpace and then you add the user back to Active Directory and create a new
WorkSpace for that user, the same username will now have two WorkSpaces in the same
directory. However, if the user tries to connect to their original WorkSpace, they
will receive the following error:

```
"Unrecognized user. No WorkSpace found under your username. Contact your administrator to request one."
```

Additionally, searches for the username in the Amazon WorkSpaces console return only
the new WorkSpace, even though both WorkSpaces still exist. (You can find the original
WorkSpace by searching for the WorkSpace ID instead of the username.)

This behavior can also occur if you rename a user in Active Directory without
first deleting their WorkSpace. If you then change their username back to the
original username and create a new WorkSpace for the user, the same username will
have two WorkSpaces in the directory.

This problem occurs because Active Directory uses the user's security identifier
(SID), rather than the username, to uniquely identify the user. When a user is
deleted and recreated in Active Directory, the user is assigned a new SID, even if
their username remains the same. During searches for a username, the Amazon WorkSpaces
console uses the SID to search Active Directory for matches. The Amazon WorkSpaces clients
also use the SID to identify users when they are connecting to WorkSpaces.

To resolve this problem, do one of the following:

- If this problem occurred because the user was deleted and recreated in Active Directory, you
  might be able to restore the original deleted user object if you have enabled the
  [Recycle Bin feature in Active Directory](https://docs.microsoft.com/windows-server/identity/ad-ds/get-started/adac/introduction-to-active-directory-administrative-center-enhancements--level-100- "https://docs.microsoft.com/windows-server/identity/ad-ds/get-started/adac/introduction-to-active-directory-administrative-center-enhancements--level-100-"). If you're able to restore the original
  user object, make sure the user can connect to their original WorkSpace. If they can, you can
  [delete the new WorkSpace](delete-workspaces.md "delete-workspaces.md") after manually backing up
  and transferring any user data from the new WorkSpace to the original WorkSpace (if needed).
- If you can't restore the original user object, [delete the user's original WorkSpace](delete-workspaces.md "delete-workspaces.md"). The user should be able to connect to and use
  their new WorkSpace instead. Be sure to manually back up and transfer any user data from the
  original WorkSpace to the new WorkSpace.

###### Warning

Deleting a WorkSpace is a permanent action and cannot be undone. The WorkSpace user's
data does not persist and is destroyed. For help with backing up user data, contact AWS
Support.

### I'm having trouble using Docker with Amazon WorkSpaces

###### Windows WorkSpaces

Nested virtualization (including the use of Docker) is not supported on
Windows WorkSpaces. For more information, see the [Docker documentation](https://docs.docker.com/docker-for-windows/troubleshoot/#running-docker-desktop-in-nested-virtualization-scenarios "https://docs.docker.com/docker-for-windows/troubleshoot/#running-docker-desktop-in-nested-virtualization-scenarios").

###### Linux WorkSpaces

To use Docker on Linux WorkSpaces, make sure that the CIDR blocks used by Docker
don't overlap with the CIDR blocks used in the two elastic network interfaces
(ENIs) associated with the WorkSpace. If you encounter problems with using
Docker on Linux WorkSpaces, contact Docker for assistance.

### I receive ThrottlingException errors to some of my API calls

The default allowed rate for WorkSpaces API calls is a constant rate of two API calls per second, with a maximum
allowed "burst" rate of five API calls per second. The following table shows how the burst rate limit works for
API requests.

| Second | Number of requests sent | Net requests allowed | Details                                                                                                                                                                                                        |
| ------ | ----------------------- | -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1      | 0                       | 5                    | During the first second (second 1), five requests are allowed,<br>up to the burst rate maximum of five calls per second.                                                                                       |
| 2      | 2                       | 5                    | Because two or fewer calls were issued in second 1, the full burst capacity<br>of five calls is still available.                                                                                               |
| 3      | 5                       | 5                    | Because only two calls were issued in second 2, the full burst capacity of<br>five calls is still available.                                                                                                   |
| 4      | 2                       | 2                    | Because the full burst capacity was used in second 3, only the constant rate of two<br>calls per second is available.                                                                                          |
| 5      | 3                       | 2                    | Because there is no remaining burst capacity, only two calls are allowed at this time.<br>This means that one of the three API calls is throttled. The one throttled call will<br>respond after a short delay. |
| 6      | 0                       | 1                    | Because one of the calls from second 5 is being retried in second 6, there is capacity<br>for only one additional call in second 6 because of the constant rate limit of two calls<br>per second.              |
| 7      | 0                       | 3                    | Now that there are no longer any throttled API calls in the queue,<br>the rate limit continues to increase, up to the burst rate limit<br>of five calls.                                                       |
| 8      | 0                       | 5                    | Because no calls were issued in second 7, the maximum number of requests is allowed.                                                                                                                           |
| 9      | 0                       | 5                    | Even though no calls were issued in second 8, the rate limit does not increase above five.                                                                                                                     |

### My WorkSpace keeps disconnecting when I let it run in the background

For Mac users, check to see if the Power Nap feature is on. If it is on, turn it off. To turn Power Nap off, open your
terminal and run the following command:

```
defaults write com.amazon.workspaces NSAppSleepDisabled -bool YES
```

### SAML 2.0 federation isn't working. My

users are not authorized to stream their WorkSpaces desktop.

This might happen because the inline policy that is embedded for the SAML 2.0
federation IAM role does not include permissions to stream from the directory
Amazon Resource Name (ARN). The IAM role is assumed by the federated user who is
accessing a WorkSpaces directory. Edit the role permissions to include the directory ARN
and ensure that the user has a WorkSpace in the directory. For more information, see
[SAML 2.0 Authentication](amazon-workspaces-saml.md "amazon-workspaces-saml.md") and [Troubleshooting SAML 2.0 Federation with AWS](../../../IAM/latest/UserGuide/troubleshoot_saml.md "../../../IAM/latest/UserGuide/troubleshoot_saml.md").

### My users are getting disconnected from

their WorkSpaces session every 60 minutes.

If you have configured SAML 2.0 authentication to WorkSpaces, depending on your
identity provider (IdP), you might need to configure the information that the IdP
passes as SAML attributes to AWS as part of the authentication response. This
includes configuring the **Attribute** element with the
`SessionDuration` attribute set to
`https://aws.amazon.com/SAML/Attributes/SessionDuration`.

`SessionDuration` specifies the maximum amount of time that a federated
streaming session can remain active for a user before reauthentication is required.
Although `SessionDuration` is an optional attribute, we recommend that
you include it in the SAML authentication response. If you don't specify this
attribute, the session duration defaults to 60 minutes.

To resolve this issue, configure your IdP to include the
`SessionDuration` value in the SAML authentication response and set
the value as required. For more information, see [Step 5: Create assertions for the SAML authentication response](setting-up-saml.md#create-assertions-saml-auth "setting-up-saml.md#create-assertions-saml-auth").

### My users get a redirect URI error when they

federate using the SAML 2.0 identity provider (IdP)-initiated flow, or an
additional instance of the WorkSpaces client application starts every time my users
attempt to sign in from the client after federating to the IdP.

This error occurs due to a relay state URL that's not valid. Make sure that the
relay state in your IdP federation setup is correct, and that the user access URL
and relay state parameter name are configured correctly for your IdP federation in
the WorkSpaces directory properties. If they are valid and the problem still persists,
contact AWS Support. For more information, see [Setting Up SAML](setting-up-saml.md "setting-up-saml.md").

### My users receive the message, "Something

went wrong: An error occurred while launching your WorkSpace" when they attempt
to sign in to the WorkSpaces client application after federating to the IdP.

Review the SAML 2.0 assertions for your federation. The **SAML Subject
NameID** value must match the WorkSpaces user name, and is typically the
same as the **sAMAccountName** attribute for the Active Directory
user. In addition, the **Attribute** element that has the
`PrincipalTag:Email` attribute set to
`https://aws.amazon.com/SAML/Attributes/PrincipalTag:Email` must
match the WorkSpaces user's email address as defined in the WorkSpaces directory. For more
information, see [Setting Up SAML](setting-up-saml.md "setting-up-saml.md").

### My users receive the message, "Unable to

validate tags” when they attempt to sign in to the WorkSpaces client application
after federating to the IdP.

Review the `PrincipalTag` attribute values in the SAML 2.0 assertions
for your federation, such as
`https://aws.amazon.com/SAML/Attributes/PrincipalTag:Email`. Tag
values may include combinations of the characters `_ . : / = + - @`,
letters, numbers, and spaces.. For more information, see [Rules for tagging in IAM and AWS STS](../../../IAM/latest/UserGuide/id_tags.md#id_tags_rules "../../../IAM/latest/UserGuide/id_tags.md#id_tags_rules").

### My users receive the message, "The client and

the server cannot communicate, because they do not possess a common algorithm".

This problem can occur if you do not enable TLS 1.2.

### My microphone or web cam is not working on

Windows WorkSpaces.

Check your privacy setting by opening the Start menu

- **Start** > **Settings** > **Privacy** > **Camera**
- **Start** > **Settings** > **Privacy** > **Microphone**

If they are turned off turn them on.

Alternatively, WorkSpaces administrators can create a Group Policy Object (GPO) to enable microphone and or webcam as needed.

### My users cannot log in using

certificate-based authentication and are prompted for the password either at the
WorkSpaces client or the Windows sign-on screen when they connect to their desktop
session.

Certificate-based authentication was unsuccessful for the session. If the problem
continues, certificate-based authentication failure can be the result of one of the
following issues:

- The WorkSpaces or the client is not supported. Certificate-based authentication
  is supported with Windows WorkSpaces on DCV bundles using the latest
  WorkSpaces Windows client application.
- The WorkSpaces needs to be rebooted after enabling certificate-based
  authentication on the WorkSpaces Directory.
- WorkSpaces could not communicate with AWS Private CA, or AWS Private CA did not issue the
  certificate. Check [AWS CloudTrail](../../../awscloudtrail/latest/userguide.md "../../../awscloudtrail/latest/userguide.md") to determine if a
  certificate was issued. For more information, see [Manage certificate-based authentication](certificate-based-authentication.md#manage-cert-based-auth "certificate-based-authentication.md#manage-cert-based-auth").
- The domain controller has no domain controller certificate for smart card
  logon, or it is expired. For more information, see step 7,
  “_Configure domain controllers with a domain controller
  certificate to authenticate smart card users_” in [Prerequisites](certificate-based-authentication.md#cert-based-auth-prerequesites "certificate-based-authentication.md#cert-based-auth-prerequesites").
- The certificate is not trusted. For more information, see step 7,
  “_Publish the CA to Active Directory_” in [Prerequisites](certificate-based-authentication.md#cert-based-auth-prerequesites "certificate-based-authentication.md#cert-based-auth-prerequesites").
  Run `certutil –viewstore –enterprise NTAuth` on domain
  controllers to confirm that the CA is published.
- There is a certificate in cache, but attributes have changed for the user
  that have invalidated the certificate. Contact Support to clear the cache
  before certificate expiry (24 hours). For more information, see [Support Center](https://console.aws.amazon.com/support/home#/ "https://console.aws.amazon.com/support/home#/").
- The userPrincipalName format for the `UserPrincipalName` SAML
  attribute is not formatted properly or does not resolve to the actual domain
  for the user. For more information, see step 1 in [Prerequisites](certificate-based-authentication.md#cert-based-auth-prerequesites "certificate-based-authentication.md#cert-based-auth-prerequesites").
- The (optional) `ObjectSid` attribute in your SAML assertion
  does not match the Active Directory security identifier (SID) for user
  specified in the SAML_Subject `NameID`. Confirm that attribute
  mapping is correct in your SAML federation and that your SAML identity
  provider is synchronizing the SID attribute for the Active Directory
  user.
- There are Group Policy settings that are modifying the default Active
  Directory settings for smart card logon or taking action if a smart card is
  removed from a smart card reader. These settings may cause additional
  unexpected behavior than the errors listed above. Certificate-based
  authentication presents a virtual smart card to the instance operating
  system and removes it after logon is complete. Check the [Primary Group Policy settings for smart cards](https://learn.microsoft.com/en-us/windows/security/identity-protection/smart-cards/smart-card-group-policy-and-registry-settings#primary-group-policy-settings-for-smart-cards "https://learn.microsoft.com/en-us/windows/security/identity-protection/smart-cards/smart-card-group-policy-and-registry-settings#primary-group-policy-settings-for-smart-cards") and the [Additional smart card Group Policy settings and registry keys](https://learn.microsoft.com/en-us/windows/security/identity-protection/smart-cards/smart-card-group-policy-and-registry-settings#additional-smart-card-group-policy-settings-and-registry-keys "https://learn.microsoft.com/en-us/windows/security/identity-protection/smart-cards/smart-card-group-policy-and-registry-settings#additional-smart-card-group-policy-settings-and-registry-keys"),
  including Smart card removal behavior.
- The CRL distribution point for the private CA is not online nor accessible
  from either the WorkSpaces or the domain controller. For more information, see
  step 5 in [Prerequisites](certificate-based-authentication.md#cert-based-auth-prerequesites "certificate-based-authentication.md#cert-based-auth-prerequesites").
- To check if there are any stale CAs in the domain or forest, run `PKIVIEW.msc` on the CA to verify.
  If there are stale CAs, use the `PKIVIEW.msc` mmc to manually delete them.
- To check if Active Directory replication is working and that there are no stale domain controllers in the
  domain, run `repadmin /replsum`.

Additional troubleshooting steps involve reviewing the WorkSpaces instance Windows
event logs. A common event to review for logon failure is [Event 4625: An account failed to logon](https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4625 "https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4625") in the Windows Security
log.

If the problem persists, contact Support. For more information, see [Support Center](https://console.aws.amazon.com/support/home#/ "https://console.aws.amazon.com/support/home#/").

### I am trying to do something that

requires Windows installation media but WorkSpaces does not provide it.

If you are using an AWS-provided public bundle, you can use the Windows Server OS installation media EBS snapshots provided by Amazon EC2 when needed.

Create an EBS volume from these snapshots, attach it to Amazon EC2, and transfer the files to the WorkSpace where the files as needed.
If you are using Windows 10 on BYOL on WorkSpaces and need an installation media, you will need to prepare your own installation media.
For more information, see [Add Windows components using installation media](../../../AWSEC2/latest/WindowsGuide/windows-optional-components.md#adding-windows-components-console "../../../AWSEC2/latest/WindowsGuide/windows-optional-components.md#adding-windows-components-console"). Since you can't directly attach an EBS volume to a WorkSpace, you'll need to attach it
to an Amazon EC2 instance and copy the files.

### I want to launch WorkSpaces with an existing AWS Managed Directory created in an

unsupported WorkSpaces Region.

To launch Amazon WorkSpaces using a directory in a Region that is not currently supported by WorkSpaces, follow the steps below.

###### Note

If you receive errors when running AWS Command Line Interface commands, ensure you’re using the most recent AWS CLI version. For more information,
see [Confirm that you're running a recent version
of the AWS CLI](../../../cli/latest/userguide/cli-chap-troubleshooting.md#general-latest "../../../cli/latest/userguide/cli-chap-troubleshooting.md#general-latest").

#### Step 1: Create virtual private cloud (VPC) peering with another VPC in your account

1. Create the VPC peering connection with a VPC in a different Region. For more information, see
   [Create with VPCs in the same account and different Regions](../../../vpc/latest/peering/create-vpc-peering-connection.md#same-account-different-region "../../../vpc/latest/peering/create-vpc-peering-connection.md#same-account-different-region").
2. Accept the VPC peering connection. For more information, see
   [Accept a VPC peering connection](../../../vpc/latest/peering/accept-vpc-peering-connection.md "../../../vpc/latest/peering/accept-vpc-peering-connection.md").
3. After you activate the VPC peering connection, you can view your VPC peering connections using the Amazon VPC console, the AWS CLI, or an API.

#### Step 2: Update route tables for VPC peering in both Regions

Update your route tables to turn on communication with the peer VPC over IPv4 or IPv6. For more information, see
[Update your route tables for a VPC peering connection](../../../vpc/latest/peering/vpc-peering-routing.md "../../../vpc/latest/peering/vpc-peering-routing.md").

#### Step 3: Create an AD Connector and register Amazon WorkSpaces

1. To review the AD Connector prerequisites, see [AD Connector prerequisites](../../../directoryservice/latest/admin-guide/prereq_connector.md "../../../directoryservice/latest/admin-guide/prereq_connector.md").
2. Connect your existing directory with AD Connector. For more information, see
   [Create an AD Connector](../../../directoryservice/latest/admin-guide/create_ad_connector.md "../../../directoryservice/latest/admin-guide/create_ad_connector.md").
3. When the AD Connector status changes to **Active**, open the [AWS Directory Service console](https://console.aws.amazon.com/directoryservice "https://console.aws.amazon.com/directoryservice"), then choose the hyperlink for your **Directory ID**.
4. For AWS apps and services, choose **Amazon WorkSpaces** to turn on access for WorkSpaces on this directory.
5. Register the directory with WorkSpaces. For more information, see
   [Register a directory with WorkSpaces](register-deregister-directory.md "register-deregister-directory.md").

### I want to update Firefox on Amazon Linux 2.

#### Step 1: Verify auto-update is enabled

To verify that autoupdate is enabled, run the command `systemctl status
 *os-update-mgmt.timer | grep enabled` on your WorkSpace. In the
output, there should be two lines with the word `enabled` on
them.

#### Step 2: Initiate an update

Firefox usually updates automatically in Amazon Linux 2 WorkSpaces along with all other
software packages in the system during the maintenance window. However, this
depends on the type of WorkSpaces you are using.

- For AlwaysOn WorkSpaces, the weekly maintenance window is on Sunday 00h00 to 04h00, in the time zone of the WorkSpace.
- For AutoStop WorkSpaces. beginning on the third Monday of the month, and for up to two weeks, the maintenance window is open each day
  from about 00h00 to 05h00, in the time zone of the AWS Region for the WorkSpace.

For more information about maintenance windows, see [WorkSpace maintenance](workspace-maintenance.md "workspace-maintenance.md").

You can also initiate an immediate update cycle by rebooting your WorkSpace
and reconnecting after 15 minutes. You can also initiate updates by entering
`sudo yum update`. To initiate an update for Firefox only, enter
`sudo yum install firefox`.

If you are not able to configure access for Amazon Linux 2 repositories and prefer to install Firefox using binaries built by Mozilla, see
[Install Firefox from Mozilla builds](https://support.mozilla.org/en-US/kb/install-firefox-linux#w_install-firefox-from-mozilla-builds "https://support.mozilla.org/en-US/kb/install-firefox-linux#w_install-firefox-from-mozilla-builds")
on Mozilla support. We recommend uninstalling the RPM-packaged version of Firefox altogether to make sure you don't run an outdated version by mistake.
You can uninstall it by running command `sudo yum remove firefox`.

You can also download the necessary RPM packages from Amazon Linux 2 repositories by
running the command `yumdownloader firefox` on a different machine.
Then, side-load the repositories onto WorkSpaces, where you can install them with a
standard `YUM` command like `sudo yum install
 firefox-102.11.0-2.amzn2.0.1.x86_64.rpm`.

###### Note

The exact file name will change based on the package version.

#### Step 3: Verify Firefox repository is used

Amazon Linux Extras automatically provides Firefox updates for Amazon Linux 2 WorkSpaces. Amazon Linux 2
WorkSpaces created after July 31, 2023 will already have the Firefox Extra repository
activated. To verify that your WorkSpace is using the Firefox Extra repository,
run the following command.

```
yum repolist | grep amzn2extra-firefox
```

The command output should look something like
`amzn2extra-firefox/2/x86_64 Amazon Extras repo for firefox 10`
if Firefox Extra repository is used. It will be empty if the Firefox Extra
repository is not used. If Firefox Extra repository is not used, you can attempt
to enable it manually with the following command:

```
sudo amazon-linux-extras install firefox
```

If the Firefox Extra repository activation still fails, check your internet
access and ensure that your VPC endpoints are unconfigured. To continue
receiving Firefox updates for Amazon Linux 2 WorkSpaces via YUM repositories, ensure that your
WorkSpaces are able to reach Amazon Linux 2 repositories. For more information on accessing
Amazon Linux 2 repositories without internet access, see [this knowledge center article](https://repost.aws/knowledge-center/ec2-al1-al2-update-yum-without-internet "https://repost.aws/knowledge-center/ec2-al1-al2-update-yum-without-internet").

### My user is able to reset their password using the WorkSpaces client,

ignoring the Fine Grained Password Policy (FFGP) setting that is configured on AWS Managed Microsoft AD.

If your user's WorkSpaces client is associated with AWS Managed Microsoft AD, they will have to reset their password using
the default complexity setting.

The default complexity password is case-sensitive and must be between 8 and 64
characters in length, inclusive. It must contain at least one character
from each of the following categories:

- Lowercase characters (a-z)
- Uppercase characters (A-Z)
- Numbers (0-9)
- Non-alphanumeric characters (~!@#$%^&\*\_-+=`|\(){}[]:;"'<>,.?/)

Make sure the password doesn't include non-printable unicode characters, such as white spaces, carriage reture tabs, line breaks, and null characters.

If your organization requires you to enforce FFGP for WorkSpaces, contact your Active Directory administrator to reset your
user's password directly from the Active Directory instead of the WorkSpaces client.

### My users receive the error message "This OS/platform is not authorized to access your WorkSpace"

when trying to access the Windows/Linux WorkSpace using Web Access

The operating system version your user is trying to use isn't compatible with WorkSpaces Web Access. Make sure you enable
Web Access under the WorkSpace directory's **Other Platform** setting. For more information on enabling your
WorkSpace's Web Access, see [Enable and configure WorkSpaces Web Access for WorkSpaces Personal](web-access.md "web-access.md").

### My user's WorkSpace is showing as unhealthy after they connect

to an AutoStop WorkSpace that is in the stopped state

Your user might be using software that is known to cause issues to the network interfaces when resuming from hibernation.
For example, if the WorkSpace has the NPCAP 1.1 application installed, update to version 1.2 or above to resolve this issue.

### Gnome crashes on WorkSpaces Ubuntu bundles after

login

If a WorkSpace is launched using the `ubuntu` username, there will be conflicts
with the `ubuntu` user that exists by default. This will cause
crashes in Gnome and potentially other degraded performance. To avoid this issue, don't specify the
`ubuntu` username when provisioning Ubuntu WorkSpaces.
