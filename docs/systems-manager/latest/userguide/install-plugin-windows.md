

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# Install the Session Manager plugin on Windows
<a name="install-plugin-windows"></a>

You can install the Session Manager plugin on 64-bit Windows 10 or later, or Windows Server 2016 or later, using the standalone installer.

When updates are released, you must repeat the installation process to get the latest version of the Session Manager plugin.

**Note**  
Note the following information.  
The Session Manager plugin installer needs Administrator rights to install the plugin.
For best results, we recommend that you start sessions on Windows clients using Windows PowerShell, version 5 or later. Alternatively, you can use the Command shell in Windows 10. The Session Manager plugin only supports PowerShell and the Command shell. Third-party command line tools might not be compatible with the plugin.

**To install the Session Manager plugin using the EXE installer**

1. Download the installer using the following URL.

   ```
   https://s3.amazonaws.com/session-manager-downloads/plugin/latest/windows/SessionManagerPluginSetup.exe
   ```

   Alternatively, you can download a zipped version of the installer using the following URL.

   ```
   https://s3.amazonaws.com/session-manager-downloads/plugin/latest/windows/SessionManagerPlugin.zip
   ```

1. Run the downloaded installer, and follow the on-screen instructions. If you downloaded the zipped version of the installer, you must unzip the installer first.

   Leave the install location box blank to install the plugin to the default directory.
   +  `%PROGRAMFILES%\Amazon\SessionManagerPlugin\bin\` 

1. Verify that the installation was successful. For information, see [Verify the Session Manager plugin installation](install-plugin-verify.md).
**Note**  
If Windows is unable to find the executable, you might need to re-open the command prompt or add the installation directory to your `PATH` environment variable manually. For information, see the troubleshooting topic [Session Manager plugin not automatically added to command line path (Windows)](session-manager-troubleshooting.md#windows-plugin-env-var-not-set).