

AWS Application Discovery Service is no longer open to new customers. Alternatively, use AWS Transform which provides similar capabilities. For more information, see [AWS Application Discovery Service availability change](https://docs.aws.amazon.com/application-discovery/latest/userguide/application-discovery-service-availability-change.html).

# Uninstalling Discovery Agent
<a name="uninstall"></a>

This page covers how to uninstall the Discovery Agent on Linux and Microsoft Windows.

## Uninstall Discovery Agent on Linux
<a name="using_on_linux-uninstall"></a>

This section describes how to uninstall Discovery Agent on Linux.

**To uninstall an agent if you're using the yum package manager**
+ Use the following command to uninstall an agent if using yum.

  ```
  rpm -e --nodeps aws-discovery-agent
  ```

**To uninstall an agent if you're using the apt-get package manager**
+ Use the following command to uninstall an agent if using apt-get.

  ```
  apt-get remove aws-discovery-agent:i386
  ```

**To uninstall an agent if you're using the zypper package manager**
+ Use the following command to uninstall an agent if using zypper.

  ```
  zypper remove aws-discovery-agent
  ```

## Uninstall Discovery Agent on Microsoft Windows
<a name="using_on_windows-uninstall"></a>

This section describes how to uninstall Discovery Agent on Microsoft Windows.

**To uninstall a discovery agent on Windows**

1. Open the Control Panel in Windows.

1. Choose **Programs**.

1. Choose **Programs and Features**.

1. Select **AWS Discovery Agent**.

1. Choose **Uninstall**.

   
**Note**  
If you choose to reinstall the agent after uninstalling it, run the following command with the `/repair` and `/norestart` options.  

   ```
   .\AWSDiscoveryAgentInstaller.exe REGION="{{your-home-region}}" KEY_ID="{{aws-access-key-id}}" KEY_SECRET="{{aws-secret-access-key}}" /quiet /repair /norestart
   ```

   

**To uninstall a discovery agent on Windows using the command line**

1. Right-click **Start**.

1. Choose **Command Prompt**.

1. Use the following command to uninstall a discovery agent on Windows. 

   ```
   wmic product where name='AWS Discovery Agent' call uninstall
   ```

**Note**  
If the `.exe` file is present on the server, you can uninstall the agent completely from the server by using the following command. If you use this command to uninstall, you don't need to use the `/repair` and `/norestart` options when you reinstall the agent.  

```
 .\AWSDiscoveryAgentInstaller.exe /quiet /uninstall
```