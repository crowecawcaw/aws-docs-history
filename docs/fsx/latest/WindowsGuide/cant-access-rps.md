

# Troubleshooting access to the Amazon FSx CLI on PowerShell
<a name="cant-access-rps"></a>

There are a number of potential causes for being unable to connect to your file system using Remote PowerShell, each with their own resolution, as follows.

To first ensure that you can connect successfully to the Windows Remote PowerShell Endpoint, you can also run a basic connectivity test. For example, you can run the `test-netconnection endpoint -port 5985` command.

## The file system's security group lacks the required inbound rules to allow a remote PowerShell connection
<a name="w2aac20c19b7"></a>

The file system's security group must have an inbound rule that allows traffic on port 5985 in order to establish a Remote PowerShell session. For more information, see [Amazon VPC Security Groups](limit-access-security-groups.md#fsx-vpc-security-groups).

## You have an external trust configured between the AWS managed Microsoft Active Directory and your on-premises Active Directory
<a name="w2aac20c19b9"></a>

In order to use the Amazon FSx Remote PowerShell with Kerberos authentication, you need to configure a local group policy on the client for forest search order. For more information, see the Microsoft documentation [Configure Kerberos Forest Search Order (KFSO)](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/hh921473(v=ws.10)?redirectedfrom=MSDN).

## A language localization error occurs when trying to initiate a remote PowerShell session
<a name="w2aac20c19c11"></a>

You need to add the following `-SessionOption` to your command: `-SessionOption (New-PSSessionOption -uiCulture "en-US")`

Following are two examples using `-SessionOption` when initiating a remote PowerShell session on your file system.

```
PS C:\Users\delegateadmin> Invoke-Command -ComputerName {{Windows Remote PowerShell Endpoint}} -ConfigurationName FSxRemoteAdmin -scriptblock {{{fsx-command}}} -SessionOption (New-PSSessionOption -uiCulture "en-US")
```

```
PS C:\Users\delegateadmin> Enter-Pssession -ComputerName {{Windows Remote PowerShell Endpoint}} -ConfigurationName FsxRemoteAdmin -SessionOption (New-PSSessionOption -uiCulture "en-US")
```