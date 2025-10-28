# Windows Service administration for EC2Launch v2 and EC2Config agents

If you've logged into your instance as a user with administrative rights, you can manage the
EC2Launch v2 and EC2Config launch agents just as you would any other Windows service. EC2Launch v1 is a
set of PowerShell scripts that is managed via scheduled task by default. This section covers service
administration for EC2Launch v2 and EC2Config.

To apply updated settings to your instance, you can stop and restart the EC2Launch v2 agent or the
EC2Config service launch agent from the Microsoft Management Console (MMC) interface for Services.
Similarly, when you install a new version of the launch agent, you must stop the agent first, then
restart it when the installation is complete.

###### Note

You must open the MMC Services interface as an administrator to select these actions. To
do this, you can select **Run as administrator** from the context menu.
Alternatively, to open the interface using your keyboard, follow these steps:

1. Using the `Tab` key or arrow keys, select the **Services**
   menu item from the **Administrative Tools** menu.
2. Use the following keyboard combination to open as an administrator:
   `Ctrl` + `Shift` + `Enter`.
   The following procedures list steps to stop and start the launch agent on your instance.

###### Stop the launch agent

1. Launch and connect to your Windows instance.
2. Select **Administrative Tools** from the Windows
   **Start** menu.
3. Open the **Services** console as an administrator, as
   described at the beginning of this section.
4. In the list of services, select the agent that's running on your instance
   (**EC2Launch** or **EC2Config**),
   then choose **Stop** from the **Action**
   menu. Alternatively, you can use the context menu to stop the agent.

###### Restart the launch agent

1. Launch and connect to your Windows instance.
2. Select **Administrative Tools** from the Windows
   **Start** menu.
3. Open the **Services** console as an administrator, as
   described at the beginning of this section.
4. In the list of services, select the agent that's running on your instance
   (**EC2Launch** or **EC2Config**), then
   choose **Start** or **Restart** from the
   **Action** menu. Alternatively, you can use the context menu
   to restart the agent.
   If you don't need to update the configuration settings, create your own AMI, or use
   AWS Systems Manager, you can delete or uninstall the launch agent.

_Delete_

Deleting a service removes
its registry subkey.

_Uninstall_

Uninstalling a service removes the files, the registry subkey, and
any shortcuts to the service.

###### Delete the launch agent

1. Launch and connect to your Windows instance.
2. Start a Windows Command Prompt window.
3. Run one of the following commands to delete the launch agent.
   - Run the following command to delete the EC2Launch or EC2Launch v2:

   ```
   `sc delete ec2launch`
   ```

   - Run the following command to delete the EC2Config service:

   ```
   `sc delete ec2config`
   ```

###### Uninstall the launch agent

1. Launch and connect to your Windows instance.
2. Choose **Windows System**, then
   **Control Panel** from the Windows
   **Start** menu.
3. Choose **Programs and Features** to open the list of
   programs that are installed on your instance.
4. Select your launch agent from the list (**Amazon EC2Launch** or
   **EC2ConfigService**), then choose **Uninstall**
   from the **File** menu. Alternatively, you can use the
   context menu.

###### Note

You can see what launch agent version is installed in the
**Version** column.
