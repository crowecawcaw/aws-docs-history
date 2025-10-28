AWS Application Discovery Service will discontinue onboarding new customers starting November 7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. Alternatively, use AWS Transform which provides similar capabilities. For more information, see [AWS Application Discovery Service availability change](application-discovery-service-availability-change.md "application-discovery-service-availability-change.md").

# Configuring set up

To discover the databases running on the previously added OS Servers, the data
collection module requires access to the operating system and database servers. This
page outlines the steps you need to take to make sure that your database is
accessible at the port that you specified in connection settings. You'll also turn
on the remote authentication on your database server and provide your data
collection module with permissions.

## Configure set up on Linux

Complete the following procedure to configure set up to discover database servers
on Linux.

###### To configure Linux to discover database servers

1. Provide sudo access to the `ss` and `netstat`
   commands.

The following code example grants sudo access to the `ss` and
`netstat` commands.

```
sudo bash -c "cat << EOF >> /etc/sudoers.d/`username`
`username` ALL=(ALL) NOPASSWD: /usr/bin/ss
`username` ALL=(ALL) NOPASSWD: /usr/bin/netstat
EOF"
```

In the preceding example, replace
`username` with the name of
the Linux user that you specified in OS server connection
credentials.

The preceding example uses the `/usr/bin/` path to the
`ss` and `netstat` commands. This path might be
different in your environment. To determine the path to the `ss`
and `netstat` commands, run the `which ss` and
`which netstat` commands. 2. Configure your Linux servers to allow running remote SSH scripts and allow
the Internet Control Message Protocol (ICMP) traffic.

## Configure set up on Microsoft Windows

Complete the following procedure to configure set up to discover database servers
on Microsoft Windows.

###### To configure Microsoft Windows to discover database servers

1. Provide credentials with grants to run Windows Management Instrumentation
   (WMI) and WMI Query Language (WQL) queries and read the registry.
2. Add the Windows user that you specified in OS server connection
   credentials to the following groups: Distributed COM Users, Performance Log
   Users, Performance Monitor Users, and Event Log Readers. To do so, use the
   following code example.

```
net localgroup "Distributed COM Users" `username` /ADD
net localgroup "Performance Log Users" `username` /ADD
net localgroup "Performance Monitor Users" `username` /ADD
net localgroup "Event Log Readers" `username` /ADD
```

In the preceding example, replace
`username` with the name of
the Windows user that you specified in OS server connection
credentials. 3. Grant the required permissions for the Windows user that you specified in
OS server connection credentials.

    * For **Windows Management and Instrumentation
     Properties**, choose **Local Launch**
     and **Remote Activation**.
    * For **WMI Control**, choose the **Execute
     Methods**, **Enable Account**,
     **Remote Enable**, and **Read
     Security** permissions for the `CIMV2`,
     `DEFAULT`, `StandartCimv2`, and
     `WMI` namespaces.
    * For  **WMI plug-in**, run `winrm configsddl
     default` and then choose **Read** and
     **Execute**.

4. Configure your Windows host by using the following code example.

```
netsh advfirewall firewall add rule name="Open Ports for WinRM incoming traffic" dir=in action=allow protocol=TCP localport=5985, 5986 # Opens ports for WinRM
netsh advfirewall firewall add rule name="All ICMP V4" protocol=icmpv4:any,any dir=in action=allow # Allows ICPM traffic

Enable-PSRemoting -Force # Enables WinRM
Set-Service WinRM -StartMode Automatic # Allows WinRM service to run on host startup
Set-Item WSMan:\localhost\Client\TrustedHosts -Value {IP} -Force # Sets the specific IP from which the access to WinRM is allowed

winrm set winrm/config/service '@{Negotiation="true"}' # Allow Negosiate auth usage
winrm set winrm/config/service '@{AllowUnencrypted="true"}' # Allow unencrypted connection
```
