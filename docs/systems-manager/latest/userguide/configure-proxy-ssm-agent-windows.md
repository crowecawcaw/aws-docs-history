AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

# Configure SSM Agent to use a

proxy for Windows Server instances

The information in this topic applies to Windows Server instances created on or after
November 2016 that do _not_ use the Nano
installation option. If you intend to use Session Manager, note that HTTPS proxy servers
aren't supported.

###### Before you begin

Before you configure SSM Agent to use a proxy, note the following important
information.

In the following procedure, you run a command to configure SSM Agent to use a
proxy. The command includes a `no_proxy` setting with an IP
address. The IP address is the instance metadata services (IMDS) endpoint for Systems Manager.
If you don't specify `no_proxy`, calls to Systems Manager take on the
identity from the proxy service (if IMDSv1 fallback is enabled) or calls to Systems Manager
fail (if IMDSv2 is enforced).

- For IPv4, specify `no_proxy=169.254.169.254`.
- For IPv6, specify `no_proxy=[fd00:ec2::254]`. The
  IPv6 address of the instance metadata service is compatible with IMDSv2
  commands. The IPv6 address is only accessible on instances built on the
  [AWS Nitro
  System](../../../ec2/latest/instancetypes/ec2-nitro-instances.md "../../../ec2/latest/instancetypes/ec2-nitro-instances.md"). For more information, see [How
  Instance Metadata Service Version 2 works](../../../AWSEC2/latest/UserGuide/instance-metadata-v2-how-it-works.md "../../../AWSEC2/latest/UserGuide/instance-metadata-v2-how-it-works.md") in the
  _Amazon EC2 User Guide_.

###### To configure SSM Agent to use a proxy

1. Using Remote Desktop or Windows PowerShell, connect to the instance that
   you would like to configure to use a proxy.
2. Run the following command block in PowerShell. Replace
   `hostname` and `port`
   with the information about your proxy.

```
$serviceKey = "HKLM:\SYSTEM\CurrentControlSet\Services\AmazonSSMAgent"
$keyInfo = (Get-Item -Path $serviceKey).GetValue("Environment")
$proxyVariables = @("http_proxy=`hostname`:`port`", "https_proxy=`hostname`:`port`", "no_proxy=`IP address for instance metadata services (IMDS)`")

if ($keyInfo -eq $null) {
    New-ItemProperty -Path $serviceKey -Name Environment -Value $proxyVariables -PropertyType MultiString -Force
} else {
    Set-ItemProperty -Path $serviceKey -Name Environment -Value $proxyVariables
}

Restart-Service AmazonSSMAgent
```

After running the preceding command, you can review the SSM Agent logs to confirm
the proxy settings were applied. Entries in the logs look similar to the following.
For more information about SSM Agent logs, see [Viewing SSM Agent logs](ssm-agent-logs.md "ssm-agent-logs.md").

```
2020-02-24 15:31:54 INFO Getting IE proxy configuration for current user: The operation completed successfully.
2020-02-24 15:31:54 INFO Getting WinHTTP proxy default configuration: The operation completed successfully.
2020-02-24 15:31:54 INFO Proxy environment variables:
2020-02-24 15:31:54 INFO http_proxy: hostname:port
2020-02-24 15:31:54 INFO https_proxy: hostname:port
2020-02-24 15:31:54 INFO no_proxy: IP address for instance metadata services (IMDS)
2020-02-24 15:31:54 INFO Starting Agent: amazon-ssm-agent - v2.3.871.0
2020-02-24 15:31:54 INFO OS: windows, Arch: amd64
```

###### To reset SSM Agent proxy configuration

1. Using Remote Desktop or Windows PowerShell, connect to the instance to
   configure.
2. If you connected using Remote Desktop, launch PowerShell as an
   administrator.
3. Run the following command block in PowerShell.

```
Remove-ItemProperty -Path HKLM:\SYSTEM\CurrentControlSet\Services\AmazonSSMAgent -Name Environment
Restart-Service AmazonSSMAgent
```

## SSM Agent proxy setting

precedence

When configuring proxy settings for the SSM Agent on Windows Server instances, it's
important to understand these settings are evaluated and applied to the agent
configuration when the SSM Agent is started. How you configure your proxy
settings for a Windows Server instance can determine whether other settings might
supersede your intended settings. The agent uses the first proxy settings it
finds.

###### Important

SSM Agent communicates using the HTTPS protocol. For this reason, you must
configure the `HTTPS proxy` parameter by using one of the
following settings options.

SSM Agent proxy settings are evaluated in the following order.

1. `AmazonSSMAgent` Registry settings
   (`HKLM:\SYSTEM\CurrentControlSet\Services\AmazonSSMAgent`)
2. `System` environment variables (`http_proxy`,
   `https_proxy`, `no_proxy`)
3. `LocalSystem` user account environment variables
   `http_proxy`, `https_proxy`,
   `no_proxy`)
4. Browser settings (`HTTP`, `secure`,
   `exceptions`)
5. `WinHTTP` proxy settings (`http=`,
   `https=`, `bypass-list=`)

## SSM Agent proxy settings and Systems Manager

services

If you configured the SSM Agent to use a proxy and are using AWS Systems Manager tools,
such as Run Command and Patch Manager, that use PowerShell or the Windows Update client
during their execution on Windows Server instances, configure additional proxy
settings. Otherwise, the operation might fail because proxy settings used by
PowerShell and the Windows Update client aren't inherited from the SSM Agent
proxy configuration.

For Run Command, configure `WinINet` proxy settings on your Windows Server
instances. The `[System.Net.WebRequest]` commands provided are
per-session. To apply these configurations to subsequent network commands that
are run in Run Command, these commands must precede other PowerShell commands in
the same `aws:runPowershellScript` plugin input.

The following PowerShell commands return the current `WinINet`
proxy settings, and apply your proxy settings to `WinINet`.

```
[System.Net.WebRequest]::DefaultWebProxy

$proxyServer = "http://`hostname`:`port`"
$proxyBypass = "169.254.169.254"
$WebProxy = New-Object System.Net.WebProxy($proxyServer,$true,$proxyBypass)

[System.Net.WebRequest]::DefaultWebProxy = $WebProxy
```

For Patch Manager, configure system-wide proxy settings so the Windows Update
client can scan for and download updates. We recommend that you use Run Command to
run the following commands because they run on the SYSTEM account, and the
settings apply system-wide. The following `netsh` commands return the
current proxy settings, and apply your proxy settings to the local
system.

```
netsh winhttp show proxy

netsh winhttp set proxy proxy-server="`hostname`:`port`" bypass-list="169.254.169.254"
```

For more information about using Run Command, see [AWS Systems Manager Run Command](run-command.md "run-command.md").
