# Configure .NET proxy settings for the EC2Config service

You can configure the EC2Config service to communicate through a proxy using one of
the following methods: the AWS SDK for .NET, the `system.net` element, or
Microsoft Group Policy and Internet Explorer. Using the AWS SDK for .NET is the
preferred method because you can specify sign-in credentials.

###### Methods

- [Configure proxy settings using the AWS SDK for .NET (Preferred)](#sdk-proxy "#sdk-proxy")
- [Configure proxy settings using the system.net element](#system-proxy "#system-proxy")
- [Configure proxy settings using Microsoft Group Policy and Microsoft Internet Explorer](#ie-proxy "#ie-proxy")

## Configure proxy settings using the AWS SDK for .NET (Preferred)

You can configure proxy settings for the EC2Config service by specifying the
`proxy` element in the `Ec2Config.exe.config`
file. For more information, see [Configuration Files Reference for AWS SDK for .NET](../../../sdk-for-net/latest/developer-guide/net-dg-config-ref.md#net-dg-config-ref-elements-proxy "../../../sdk-for-net/latest/developer-guide/net-dg-config-ref.md#net-dg-config-ref-elements-proxy").

###### To specify the proxy element in Ec2Config.exe.config

1. Edit the `Ec2Config.exe.config` file on an instance
   where you want the EC2Config service to communicate through a proxy. By
   default, the file is located in the following directory:
   `%ProgramFiles%\Amazon\Ec2ConfigService`.
2. Add the following `aws` element to the
   `configSections`. Do not add this to any existing
   `sectionGroups`.

**For EC2Config versions 3.17 or earlier**

```
<configSections>
   <section name="aws" type="Amazon.AWSSection, AWSSDK"/>
</configSections>
```

**For EC2Config versions 3.18 or later**

```
<configSections>
     <section name="aws" type="Amazon.AWSSection, AWSSDK.Core"/>
</configSections>

```

3. Add the following `aws` element to the
   `Ec2Config.exe.config` file.

```
<aws>
   <proxy
     host="`string value`"
     port="`string value`"
     username="`string value`"
     password="`string value`" />
</aws>
```

4. Save your changes.

## Configure proxy settings using the system.net element

You can specify proxy settings in a `system.net` element in the
`Ec2Config.exe.config` file. For more information, see
[defaultProxy element (network settings)](https://learn.microsoft.com/en-us/dotnet/framework/configure-apps/file-schema/network/defaultproxy-element-network-settings "https://learn.microsoft.com/en-us/dotnet/framework/configure-apps/file-schema/network/defaultproxy-element-network-settings").

###### To specify the system.net element in Ec2Config.exe.config

1. Edit the `Ec2Config.exe.config` file on an instance
   where you want the EC2Config service to communicate through a proxy. By
   default, the file is located in the following directory:
   `%ProgramFiles%\Amazon\Ec2ConfigService`.
2. Add a `defaultProxy` entry to `system.net`. For more information, see
   [defaultProxy element (network settings)](https://learn.microsoft.com/en-us/dotnet/framework/configure-apps/file-schema/network/defaultproxy-element-network-settings "https://learn.microsoft.com/en-us/dotnet/framework/configure-apps/file-schema/network/defaultproxy-element-network-settings").

For example, the following configuration routes all traffic to use the
proxy that is currently configured for Internet Explorer, with the exception
of the metadata and licensing traffic, which will bypass the proxy.

```
<defaultProxy>
    <proxy usesystemdefault="true" />
    <bypasslist>
        <add address="169.254.169.250" />
        <add address="169.254.169.251" />
        <add address="169.254.169.254" />
        <add address="[fd00:ec2::250]" />
        <add address="[fd00:ec2::254]" />
    </bypasslist>
</defaultProxy>
```

3. Save your changes.

## Configure proxy settings using Microsoft Group Policy and Microsoft Internet Explorer

The EC2Config service runs under the Local System user account. You can specify
instance-wide proxy settings for this account in Internet Explorer after you change
Group Policy settings on the instance.

###### To configure proxy settings using Group Policy and Internet Explorer

1. On an instance where you want the EC2Config service to communicate through
   a proxy, open a Command prompt as an Administrator, type
   `gpedit.msc`, and press Enter.
2. In the Local Group Policy Editor, under **Local Computer
   Policy**, choose **Computer Configuration**,
   **Administrative Templates**, **Windows
   Components**, **Internet Explorer**.
3. In the right-pane, choose **Make proxy settings per-machine
   (rather than per-user)** and then choose **Edit policy
   setting**.
4. Choose **Enabled**, and then choose
   **Apply**.
5. Open Internet Explorer, and then choose the **Tools**
   button.
6. Choose **Internet Option**, and then choose the
   **Connections** tab.
7. Choose **LAN settings**.
8. Under **Proxy server**, choose the **Use a proxy
   server for your LAN** option.
9. Specify address and port information and then choose
   **OK**.
