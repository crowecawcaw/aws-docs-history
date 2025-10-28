AWS Application Discovery Service will discontinue onboarding new customers starting November 7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. Alternatively, use AWS Transform which provides similar capabilities. For more information, see [AWS Application Discovery Service availability change](application-discovery-service-availability-change.md "application-discovery-service-availability-change.md").

# Uninstalling Discovery Agent

This page covers how to uninstall the Discovery Agent on Linux and Microsoft Windows.

## Uninstall Discovery Agent on Linux

This section describes how to uninstall Discovery Agent on Linux.

###### To uninstall an agent if you're using the yum package manager

- Use the following command to uninstall an agent if using yum.

```
rpm -e --nodeps aws-discovery-agent
```

###### To uninstall an agent if you're using the apt-get package manager

- Use the following command to uninstall an agent if using apt-get.

```
apt-get remove aws-discovery-agent:i386
```

###### To uninstall an agent if you're using the zypper package manager

- Use the following command to uninstall an agent if using zypper.

```
zypper remove aws-discovery-agent
```

## Uninstall Discovery Agent on Microsoft

Windows

This section describes how to uninstall Discovery Agent on Microsoft Windows.

###### To uninstall a discovery agent on Windows

1. Open the Control Panel in Windows.
2. Choose **Programs**.
3. Choose **Programs and Features**.
4. Select **AWS Discovery Agent**.
5. Choose **Uninstall**.

###### Note

If you choose to reinstall the agent after uninstalling it, run the
following command with the `/repair` and
`/norestart` options.

```
.\AWSDiscoveryAgentInstaller.exe REGION="`your-home-region`" KEY_ID="`aws-access-key-id`" KEY_SECRET="`aws-secret-access-key`" /quiet /repair /norestart
```

###### To uninstall a discovery agent on Windows using the command line

1. Right-click **Start**.
2. Choose **Command Prompt**.
3. Use the following command to uninstall a discovery agent on Windows.

```
wmic product where name='AWS Discovery Agent' call uninstall
```

###### Note

If the `.exe` file is present on the server, you can
uninstall the agent completely from the server by using the following command.
If you use this command to uninstall, you don't need to use the
`/repair` and `/norestart` options when you reinstall
the agent.

```
 .\AWSDiscoveryAgentInstaller.exe /quiet /uninstall
```
