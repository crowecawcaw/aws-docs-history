# Configure WorkSpaces Thin Client

Most WorkSpaces bundles support Amazon WorkSpaces Thin Client Access. For a list of WorkSpaces that
support web browser access, see "Which Amazon WorkSpaces bundles support Thin Client Access?" in
[Client Access, Web Access, and User Experience](https://aws.amazon.com/workspaces/faqs/#Client_Access.2C_Web_Access.2C_and_User_Experience "https://aws.amazon.com/workspaces/faqs/#Client_Access.2C_Web_Access.2C_and_User_Experience").

## Step 1: Enable Access Control to your Amazon WorkSpaces Thin Client

You control Thin Client Access to your WorkSpaces at the directory level with user-agent based access control. For each directory
containing WorkSpaces that you want to allow users to access through the Thin Client Access
client, do the following steps.

###### To enable Thin Client Access to your WorkSpaces

1. Open the WorkSpaces console at [https://console.aws.amazon.com/workspaces/v2/home](https://console.aws.amazon.com/workspaces/v2/home "https://console.aws.amazon.com/workspaces/v2/home").
2. In the navigation pane, choose **Directories**.
3. Under the **Directory ID** column, choose the directory ID of the directory you want to enable Thin Client Access for.
4. On the **Directory Details** page, scroll down to the **Other platforms**
   section and choose **Edit**.
5. Select **WorkSpaces Thin Client**.
6. Choose **Save**.

## Step 2: Configure inbound and outbound access to ports for Thin Client Access

Amazon WorkSpaces Thin Client Access requires inbound and outbound access for certain ports. For more
information, see [Ports for Web Access](workspaces-port-requirements.md#web-access-ports "workspaces-port-requirements.md#web-access-ports").

## Step 3: Configure Group Policy and security policy settings to enable users to log on

Amazon WorkSpaces relies on a specific logon screen configuration to enable users to successfully log on from their Thin Client Access client.

1. To enable Thin Client Access users to log on to their WorkSpaces, you must configure a Group Policy setting and three Security Policy settings.
   If these settings are not correctly configured, users might experience long logon times or black screens when they try to log on to their
   WorkSpaces. To configure these settings, use the following procedures.
2. You can use Group Policy Objects (GPOs) to apply settings to manage Windows WorkSpaces or users that are part of your Windows WorkSpaces
   directory. We recommend that you create an organizational unit for your WorkSpaces Computer Objects and an organizational unit for your
   WorkSpaces User Objects.
3. For information about using the Active Directory administration tools to work with GPOs,
   see [Installing the Active Directory Administration Tools](../../../directoryservice/latest/admin-guide/ms_ad_install_ad_tools.md "../../../directoryservice/latest/admin-guide/ms_ad_install_ad_tools.md") in the _AWS Directory Service Administration Guide_.
4. In most cases, when a user attempts to log on to a WorkSpace, the user name field
   is prepopulated with the name of that user. However, if an administrator has
   established an RDP connection to the WorkSpace to perform maintenance tasks, the
   user name field is populated with the name of the administrator instead.
5. To avoid this issue, disable the **Hide entry points for Fast User Switching** Group Policy setting. When you
   disable this setting, the WorkSpaces logon agent can use the **Switch User** button to populate the user name
   field with the correct name.

###### To enable the WorkSpaces logon agent to switch users

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

By default, the list of last logged on users is displayed instead of the **Switch User** button. Depending on
the configuration of the WorkSpace, the list might not display the **Other User** tile. When this situation occurs,
if the prepopulated user name isn't correct, the WorkSpaces logon agent can't populate the field with the correct name.

To avoid this issue, enable the Security Policy setting **Interactive logon: Don't display last signed-in**
or **Interactive logon: Do not display last user name** (depending on which version of Windows you're using).

###### To hide the last logged on user name

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

For WorkSpaces Thin Client Access, you need to require that users press CTRL+ALT+DEL before they can log on. Requiring users to press
CTRL+ALT+DEL before they log on ensures that users are using a trusted path when they're entering their passwords.

###### To require pressing CTRL+ALT+DEL before users can log on

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

The WorkSpaces logon agent looks for the user's name and domain. After this setting is configured, the lock screen will display
the user's full name (if it is specified in Active Directory), their domain name, and their user name.

###### To display the domain and user information when the session is locked

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

Group Policy and Security Policy settings changes take effect after the next Group Policy update for the WorkSpace and after the WorkSpace session is
restarted. To apply the Group Policy and Security Policy changes in the prior procedures, do one of the following:

###### To apply the Group Policy and Security Policy settings changes

1. Reboot the WorkSpace (in the Amazon WorkSpaces console, select the WorkSpace, then choose
   **Actions**, **Reboot WorkSpaces**).
2. From an administrative command prompt, enter **gpupdate
   /force**.
