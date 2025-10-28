# Update or create a DNS CNAME record

After you properly configure SPNs for your file system, you can cut over to Amazon FSx by
replacing each DNS record that resolved to the original file system with a DNS record that
resolves to the default DNS name of the Amazon FSx file system.

The `dnsserver` and `activedirectory` Windows modules are required to
run the commands presented in this section.

###### To install the required PowerShell modules

1. Log on to a Windows instance joined to the same Active Directory that your Amazon FSx file
   system is joined to as a user that is a member of a group that has DNS administration
   permissions (**AWS Delegated Domain Name System
   Administrators** in AWS Managed Microsoft AD, and **Domain Admins** or another group to which you've delegated DNS
   administration permissions in your self-managed Active Directory).

For more information, see [Connecting to Your Windows
Instance](../../../AWSEC2/latest/WindowsGuide/connecting_to_windows_instance.md "../../../AWSEC2/latest/WindowsGuide/connecting_to_windows_instance.md") in the _Amazon EC2 User Guide_. 2. Open PowerShell as administrator. 3. The PowerShell DNS Server module is required
to perform the instructions in this procedure. Install it using the following command.

```
Install-WindowsFeature RSAT-DNS-Server
```

###### To update or create a custom DNS name to your Amazon FSx file system

1. Connect to your Amazon EC2 instance as a user that is a member of a group that has DNS
   administration permissions (**AWS Delegated Domain Name System
   Administrators** in AWS Managed Active Directory, and **Domain Admins** or another group to which you've delegated DNS
   administration permissions in your self-managed Active Directory).

For more information, see [Connecting to Your Windows
Instance](../../../AWSEC2/latest/WindowsGuide/connecting_to_windows_instance.md "../../../AWSEC2/latest/WindowsGuide/connecting_to_windows_instance.md") in the _Amazon EC2 User Guide_. 2. At the command prompt, run the following script. This script migrates any existing DNS
CNAME records to your Amazon FSx file system. If none are found, it creates a new DNS CNAME
record for the DNS alias `alias_fqdn` that resolves
to the default DNS name for your Amazon FSx file system.

To run the script:

    * Replace ``alias_fqdn``
     with the DNS alias that you associated with the file system.
    * Replace ``file_system_DNS_name``
     with the DNS name Amazon FSx has assigned to the file system.

```
$Alias="`alias_fqdn`"
$FSxDnsName="`file_system_dns_name`"
$AliasHost=$Alias.Split('.')[0]
$ZoneName=((Get-WmiObject Win32_ComputerSystem).Domain)
$DnsServerComputerName = (Resolve-DnsName $ZoneName -Type NS | Where Type -eq 'A' | Select -ExpandProperty Name) | Select -First 1
Add-DnsServerResourceRecordCName -Name $AliasHost -ComputerName $DnsServerComputerName -HostNameAlias $FSxDnsName -ZoneName $ZoneName

```

3. Repeat the previous step for each DNS alias that you associated with the file system
   in [Step 1](step1-assign-dns-alias.md "step1-assign-dns-alias.md").
   You've now added a DNS CNAME value for your Amazon FSx file system with the DNS alias. You can now use the
   DNS alias to access your data.

###### Note

When updating a DNS CNAME record to point to an Amazon FSx file system previously pointed to
another file system, clients might not be able to connect with file system for a brief
period of time. When the client DNS cache refreshes, they should be able to connect using
the DNS alias. For more information, see [Can't access the file system using a DNS alias](unable-to-access.md#cant-connect-using-dns-alias "unable-to-access.md#cant-connect-using-dns-alias").
