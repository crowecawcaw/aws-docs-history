• AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

 

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see
[Amazon CloudWatch Dashboard documentation](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md").

# Install the Session Manager plugin on

Windows

You can install the Session Manager plugin on Windows Vista or later using
the standalone installer.

When updates are released, you must repeat the installation process to get the
latest version of the Session Manager plugin.

###### Note

Note the following information.

- The Session Manager plugin installer needs Administrator rights to install the
  plugin.
- For best results, we recommend that you start sessions on
  Windows clients using Windows
  PowerShell, version 5 or later. Alternatively, you can
  use the Command shell in Windows 10. The Session Manager plugin
  only supports PowerShell and the Command shell.
  Third-party command line tools might not be compatible with the
  plugin.

###### To install the Session Manager plugin using the EXE installer

1. Download the installer using the following URL.

```
https://s3.amazonaws.com/session-manager-downloads/plugin/latest/windows/SessionManagerPluginSetup.exe
```

Alternatively, you can download a zipped version of the installer
using the following URL.

```
https://s3.amazonaws.com/session-manager-downloads/plugin/latest/windows/SessionManagerPlugin.zip
```

2. Run the downloaded installer, and follow the on-screen instructions.
   If you downloaded the zipped version of the installer, you must unzip
   the installer first.

Leave the install location box blank to install the plugin to the
default directory.

    * `%PROGRAMFILES%\Amazon\SessionManagerPlugin\bin\`

3. Verify that the installation was successful. For information, see
   [Verify the Session Manager plugin installation](install-plugin-verify.md "install-plugin-verify.md").

###### Note

If Windows is unable to find the executable, you
might need to re-open the command prompt or add the installation
directory to your `PATH` environment variable
manually. For information, see the troubleshooting topic [Session Manager plugin not automatically added to
command line path (Windows)](session-manager-troubleshooting.md#windows-plugin-env-var-not-set "session-manager-troubleshooting.md#windows-plugin-env-var-not-set").
