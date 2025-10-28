# Enable and configure WorkSpaces Web Access for WorkSpaces Personal

Most WorkSpaces bundles support Amazon WorkSpaces Web Access. For a list of WorkSpaces that
support web browser access, see "Which Amazon WorkSpaces bundles support Web Access?" in
[Client Access, Web Access, and User Experience](https://aws.amazon.com/workspaces/faqs/#Client_Access.2C_Web_Access.2C_and_User_Experience "https://aws.amazon.com/workspaces/faqs/#Client_Access.2C_Web_Access.2C_and_User_Experience").

###### Note

- Starting November 7, 2025, Amazon WorkSpaces PCoIP Web Access will no longer be open to new customers. After this date, the feature will only receive critical functional and security updates. For more information, see the [Amazon WorkSpaces User Guide](../userguide/amazon-workspaces-web-access.md "../userguide/amazon-workspaces-web-access.md").
- Web Access with DCV for Windows and Ubuntu WorkSpaces is supported in all Regions where DCV WorkSpaces
  are available. DCV for Amazon Linux WorkSpaces is only available in AWS GovCloud (US-West).
- We strongly recommend using Web Access with DCV WorkSpaces for best streaming quality and user experience.
  The following are limitations when using Web Access with PCoIP WorkSpaces:
  - Web Access with PCoIP is not supported in the AWS GovCloud (US) Regions, Asia Pacific (Mumbai),
    Africa (Cape Town), Europe (Frankfurt), and Israel (Tel Aviv)
  - Web Access with PCoIP is only supported for Windows WorkSpaces, not with Amazon Linux or Ubuntu WorkSpaces.
  - Web Access is not available for some Windows 10 WorkSpaces that are using the PCoIP protocol.
    If your PCoIP WorkSpaces are powered by Windows Server 2019 or 2022, Web Access is not available.
  - Web Access with PCoIP is limited in feature functionality. It supports video-out, audio-out,
    keyboard and mouse. It does not support many features, including video-in, audio-in, clipboard redirection,
    and web cams.

- If you are using macOS on VPN and using the Firefox web browser,
  the web browser will not support streaming PCoIP WorkSpaces using WorkSpaces Web Access.
  This is due to a limitation in Firefox implementation of the WebRTC protocol.

###### Important

Beginning October 1, 2020, customers will no longer be able to use the Amazon WorkSpaces Web Access client
to connect to Windows 7 custom WorkSpaces or to Windows 7 Bring Your Own License (BYOL) WorkSpaces.

## Step 1: Enable Web Access to your WorkSpaces

You control Web Access to your WorkSpaces at the directory level. For each directory
containing WorkSpaces that you want to allow users to access through the Web Access
client, do the following steps.

###### To enable Web Access to your WorkSpaces

1. Open the WorkSpaces console at [https://console.aws.amazon.com/workspaces/v2/home](https://console.aws.amazon.com/workspaces/v2/home "https://console.aws.amazon.com/workspaces/v2/home").
2. In the navigation pane, choose **Directories**.
3. Under the **Directory ID** column, choose the directory ID of the directory you want to enable Web Access for.
4. On the **Directory Details** page, scroll down to the **Other platforms**
   section and choose **Edit**.
5. Choose **Web Access**.
6. Choose **Save**.

###### Note

After you enable Web Access, reboot your WorkSpace for the change to apply.

## Step 2: Configure inbound and outbound access to ports for Web Access

Amazon WorkSpaces Web Access requires inbound and outbound access for certain ports. For more
information, see [Ports for Web Access](workspaces-port-requirements.md#web-access-ports "workspaces-port-requirements.md#web-access-ports").

## Step 3: Configure Group Policy and security policy settings to enable users to log on

Amazon WorkSpaces relies on a specific logon screen configuration to enable users to successfully log on from their Web Access client.

To enable Web Access users to log on to their WorkSpaces, you must configure a Group Policy setting and three Security Policy settings.
If these settings are not correctly configured, users might experience long logon times or black screens when they try to log on to their
WorkSpaces. To configure these settings, use the following procedures.

You can use Group Policy Objects (GPOs) to apply settings to manage Windows WorkSpaces or users that are part of your Windows WorkSpaces
directory. We recommend that you create an organizational unit for your WorkSpaces Computer Objects and an organizational unit for your
WorkSpaces User Objects.

For information about using the Active Directory administration tools to work with GPOs,
see [Installing the Active Directory Administration Tools](../../../directoryservice/latest/admin-guide/ms_ad_install_ad_tools.md "../../../directoryservice/latest/admin-guide/ms_ad_install_ad_tools.md") in the _AWS Directory Service Administration Guide_.

###### To enable the WorkSpaces logon agent to switch users

In most cases, when a user attempts to log on to a WorkSpace, the user name field
is prepopulated with the name of that user. However, if an administrator has
established an RDP connection to the WorkSpace to perform maintenance tasks, the
user name field is populated with the name of the administrator instead.

To avoid this issue, disable the **Hide entry points for Fast User Switching** Group Policy setting. When you
disable this setting, the WorkSpaces logon agent can use the **Switch User** button to populate the user name
field with the correct name.

1. Open the Group Policy Management tool (**gpmc.msc**) and
   navigate to and select a GPO at the domain or domain controller level of the
   directory that you use for your WorkSpaces. (If you have the [WorkSpaces Group Policy administrative
   template](group_policy.md#gp_install_template "group_policy.md#gp_install_template") installed in your domain, you can use the WorkSpaces GPO for
   your WorkSpaces machine accounts.)
2. Choose **Action**, **Edit** in the main menu.
3. In the Group Policy Management Editor, choose **Computer Configuration**, **Policies**,
   **Administrative Templates**, **System**, and **Logon**.
4. Open the **Hide entry points for Fast User Switching** setting.
5. In the **Hide entry points for Fast User Switching** dialog box, choose **Disabled**,
   and then choose **OK**.

###### To hide the last logged on user name

By default, the list of last logged on users is displayed instead of the **Switch User** button. Depending on
the configuration of the WorkSpace, the list might not display the **Other User** tile. When this situation occurs,
if the prepopulated user name isn't correct, the WorkSpaces logon agent can't populate the field with the correct name.

To avoid this issue, enable the Security Policy setting **Interactive logon: Don't display last signed-in**
or **Interactive logon: Do not display last user name** (depending on which version of Windows you're using).

1. Open the Group Policy Management tool (**gpmc.msc**) and
   navigate to and select a GPO at the domain or domain controller level of the
   directory that you use for your WorkSpaces. (If you have the [WorkSpaces Group Policy administrative
   template](group_policy.md#gp_install_template "group_policy.md#gp_install_template") installed in your domain, you can use the WorkSpaces GPO for
   your WorkSpaces machine accounts.)
2. Choose **Action**, **Edit** in the main menu.
3. In the Group Policy Management Editor, choose **Computer Configuration**, **Windows Settings**,
   **Security Settings**, **Local Policies**, and **Security Options**.
4. Open one of the following settings:
   - For Windows 7 — **Interactive logon: Don't display last signed-in**
   - For Windows 10 — **Interactive logon: Do not display last user name**

5. In the **Properties** dialog box for the setting, choose **Enabled**, and then choose
   **OK**.

###### To require pressing CTRL+ALT+DEL before users can log on

For WorkSpaces Web Access, you need to require that users press CTRL+ALT+DEL before they can log on. Requiring users to press
CTRL+ALT+DEL before they log on ensures that users are using a trusted path when they're entering their passwords.

1. Open the Group Policy Management tool (**gpmc.msc**) and
   navigate to and select a GPO at the domain or domain controller level of the
   directory that you use for your WorkSpaces. (If you have the [WorkSpaces Group Policy administrative
   template](group_policy.md#gp_install_template "group_policy.md#gp_install_template") installed in your domain, you can use the WorkSpaces GPO for
   your WorkSpaces machine accounts.)
2. Choose **Action**, **Edit** in the main menu.
3. In the Group Policy Management Editor, choose **Computer Configuration**, **Windows Settings**,
   **Security Settings**, **Local Policies**, and **Security Options**.
4. Open the **Interactive logon: Do not require CTRL+ALT+DEL** setting.
5. On the **Local Security Setting** tab, choose **Disabled**, and then choose
   **OK**.

###### To display the domain and user information when the session is locked

The WorkSpaces logon agent looks for the user's name and domain. After this setting is configured, the lock screen will display
the user's full name (if it is specified in Active Directory), their domain name, and their user name.

1. Open the Group Policy Management tool (**gpmc.msc**) and
   navigate to and select a GPO at the domain or domain controller level of the
   directory that you use for your WorkSpaces. (If you have the [WorkSpaces Group Policy administrative
   template](group_policy.md#gp_install_template "group_policy.md#gp_install_template") installed in your domain, you can use the WorkSpaces GPO for
   your WorkSpaces machine accounts.)
2. Choose **Action**, **Edit** in the main menu.
3. In the Group Policy Management Editor, choose **Computer Configuration**, **Windows Settings**,
   **Security Settings**, **Local Policies**, and **Security Options**.
4. Open the **Interactive logon: Display user information when the session is locked** setting.
5. On the **Local Security Setting** tab, choose **User display name, domain and user names**,
   and then choose **OK**.

###### To apply the Group Policy and Security Policy settings changes

Group Policy and Security Policy settings changes take effect after the next Group Policy update for the WorkSpace and after the WorkSpace session is
restarted. To apply the Group Policy and Security Policy changes in the prior procedures, do one of the following:

- Reboot the WorkSpace (in the Amazon WorkSpaces console, select the WorkSpace, then choose
  **Actions**, **Reboot WorkSpaces**).
- From an administrative command prompt, enter **gpupdate
  /force**.
