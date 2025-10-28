# Maintenance in WorkSpaces Personal

We recommend that you maintain your WorkSpaces on a regular basis. WorkSpaces schedules default
maintenance windows for your WorkSpaces. During the maintenance window, the WorkSpace installs
important updates from Amazon WorkSpaces and reboots as necessary. If available, operating system
updates are also installed from the OS update server that the WorkSpace is configured to
use. During maintenance, your WorkSpaces might be unavailable.

By default, your Windows WorkSpaces are configured to receive updates from Windows Update.
To configure your own automatic update mechanisms for Windows, see the documentation for
[Windows Server Update Services (WSUS)](https://docs.microsoft.com/windows-server/administration/windows-server-update-services/deploy/deploy-windows-server-update-services "https://docs.microsoft.com/windows-server/administration/windows-server-update-services/deploy/deploy-windows-server-update-services") and [Configuration Manager](https://docs.microsoft.com/configmgr/sum/deploy-use/deploy-software-updates "https://docs.microsoft.com/configmgr/sum/deploy-use/deploy-software-updates").

###### Requirement

Your WorkSpaces must have access to the internet so that you can install updates
to the operating system and deploy applications. For more information, see
[Provide internet access for WorkSpaces Personal](amazon-workspaces-internet-access.md "amazon-workspaces-internet-access.md").

## Maintenance windows for AlwaysOn WorkSpaces

For AlwaysOn WorkSpaces, the maintenance window is determined by operating system
settings. The default is a four-hour period from 00h00 to 04h00, in the time zone of the
WorkSpace, each Sunday morning. By default, the time zone of an AlwaysOn WorkSpace is
the time zone of the AWS Region for the WorkSpace. However, if you connect from
another Region and time zone redirection is enabled, and then you disconnect, the time
zone of the WorkSpace is updated to the time zone of the Region that you connected
from.

You can [disable time zone redirection for Windows
WorkSpaces](group_policy.md#gp_time_zone "group_policy.md#gp_time_zone") using Group Policy. You can [disable time
zone redirection for Linux WorkSpaces](manage_linux_workspace.md#linux_time_zone "manage_linux_workspace.md#linux_time_zone") by using the PCoIP Agent conf.

For Windows WorkSpaces, you can configure the maintenance window using Group Policy; see
[Configure Group Policy Settings for Automatic Updates](https://docs.microsoft.com/windows-server/administration/windows-server-update-services/deploy/4-configure-group-policy-settings-for-automatic-updates "https://docs.microsoft.com/windows-server/administration/windows-server-update-services/deploy/4-configure-group-policy-settings-for-automatic-updates"). You cannot configure
the maintenance window for Linux WorkSpaces.

## Maintenance windows for AutoStop WorkSpaces

AutoStop WorkSpaces are started automatically once a month in order to install important
updates. Beginning on the third Monday of the month, and for up to two weeks, the
maintenance window is open each day from about 00h00 to 05h00, in the time zone of the
AWS Region for the WorkSpace. The WorkSpace can be maintained on any one day in the
maintenance window. During this window, only WorkSpaces older than 7 days are maintained.

During the time period when the WorkSpace is undergoing maintenance, the state of the
WorkSpace is set to `MAINTENANCE`.

Although you cannot modify the time zone that is used for maintaining AutoStop WorkSpaces,
you can disable the maintenance window for your AutoStop WorkSpaces as follows. If you
disable maintenance mode, your WorkSpaces are not rebooted and do not enter the
`MAINTENANCE` state.

###### To disable maintenance mode

1. Open the WorkSpaces console at [https://console.aws.amazon.com/workspaces/v2/home](https://console.aws.amazon.com/workspaces/v2/home "https://console.aws.amazon.com/workspaces/v2/home").
2. In the navigation pane, choose **Directories**.
3. Select your directory, and choose **Actions**,
   **Update Details**.
4. Expand **Maintenance Mode**.
5. To enable automatic updates, choose **Enabled**. If you prefer
   to manage updates manually, choose **Disabled**.
6. Choose **Update and Exit**.

## Manual maintenance

If you prefer, you can maintain your WorkSpaces on your own schedule. When you perform
maintenance tasks, we recommend that you change the state of the WorkSpace to
**Maintenance**. When you are finished, change the state of the
WorkSpace to **Available**.

When a WorkSpace is in **Maintenance** state, the following
behaviors occur:

- The WorkSpace does not respond to requests to reboot, stop, start, or
  rebuild.
- Users cannot log in to the WorkSpace.
- An AutoStop WorkSpace is not hibernated.

###### To change the state of the WorkSpace using the console

###### Note

To change the state of a WorkSpace, the WorkSpace must be in the **Available**
state. The **Modify state** setting is not
available when a WorkSpace is not in the **Available** state.

1. Open the WorkSpaces console at [https://console.aws.amazon.com/workspaces/v2/home](https://console.aws.amazon.com/workspaces/v2/home "https://console.aws.amazon.com/workspaces/v2/home").
2. In the navigation pane, choose **WorkSpaces**.
3. Select your WorkSpace, and choose **Actions**,
   **Modify state**.
4. Under **Modify state**, choose **Available** or
   **Maintenance**.
5. Choose **Save**.

###### To change the state of the WorkSpace using the AWS CLI

Use the [modify-workspace-state](../../../cli/latest/reference/workspaces/modify-workspace-state.md "../../../cli/latest/reference/workspaces/modify-workspace-state.md") command.
