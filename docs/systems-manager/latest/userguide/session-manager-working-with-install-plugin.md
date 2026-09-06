

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# Install the Session Manager plugin for the AWS CLI
<a name="session-manager-working-with-install-plugin"></a>

**Minimum plugin version required**  
Update your Session Manager plugin to version 1.2.764.0 or later. Session Manager will soon stop supporting earlier versions, and your operations might not succeed. To check your installed version, run the following command.  

```
session-manager-plugin --version
```

To initiate Session Manager sessions with your managed nodes by using the AWS Command Line Interface (AWS CLI), you must install the *Session Manager plugin* on your local machine. You can install the plugin on supported versions of Microsoft Windows Server, macOS, Linux, and Ubuntu Server.

**Note**  
To use the Session Manager plugin, you must have AWS CLI version 1.16.12 or later installed on your local machine. For more information, see [Installing or updating the latest version of the AWS Command Line Interface](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html).

**Topics**
+ [Session Manager plugin latest version and release history](plugin-version-history.md)
+ [Install the Session Manager plugin on Windows](install-plugin-windows.md)
+ [Install the Session Manager plugin on macOS](install-plugin-macos-overview.md)
+ [Install the Session Manager plugin on Linux](install-plugin-linux-overview.md)
+ [Verify the Session Manager plugin installation](install-plugin-verify.md)
+ [Session Manager plugin on GitHub](plugin-github.md)
+ [(Optional) Turn on Session Manager plugin logging](install-plugin-configure-logs.md)