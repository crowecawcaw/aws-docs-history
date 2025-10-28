# Set up multicast for Windows Server in AWS Transit Gateway

You'll need to perform additional steps when setting up multicast to work with transit gateways on
Windows Server 2019 or 2022. To set this up you'll need to use PowerShell, and run the following
commands:

###### To set up multicast for Windows Server using PowerShell

1. Change Windows Server to use IGMPv2 instead of IGMPv3 for the TCP/IP stack:

`PS C:\> New-ItemProperty -Path
 HKLM:\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters -Name IGMPVersion
 -PropertyType DWord -Value 3`

###### Note

`New-ItemProperty` is a property index that specifies the IGMP version.
Because IGMP v2 is the supported version for multicast, the property `Value`
must be `3`. Instead of editing the Windows registry you can run the
following command to set the IGMP version to 2.:

`Set-NetIPv4Protocol -IGMPVersion Version2` 2. Windows Firewall drops most UDP traffic by default. You'll first need to check which
connection profile is being used for multicast:

```
PS C:\> Get-NetConnectionProfile | Select-Object NetworkCategory

NetworkCategory
---------------
         Public
```

3. Update the connection profile from the previous step to allow access to the required UDP
   port(s):

`PS C:\> Set-NetFirewallProfile -Profile Public -Enabled False` 4. Reboot the EC2 instance. 5. Test your multicast application to ensure traffic is flowing as expected.
