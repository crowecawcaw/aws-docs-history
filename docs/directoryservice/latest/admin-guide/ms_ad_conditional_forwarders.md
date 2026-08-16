# Managing DNS conditional forwarders for your directory

A conditional forwarder is a DNS setting you configure in Active Directory to route queries
for a specific domain to a defined set of DNS servers. Conditional forwarders are required for
Active Directory trusts and are also used to support private DNS domains. Each conditional
forwarder consists of the fully qualified domain name (FQDN) of the remote domain and one or
more DNS server IP addresses.

###### Note

On AWS Managed Microsoft AD, a conditional forwarder is stored in Active Directory and replicated to
every domain controller in the domain (its replication scope is `Domain`). If your
directory uses [Multi-Region
replication](multi-region-how-it-works.md "multi-region-how-it-works.md") (available with the Enterprise Edition), the conditional forwarder is
also replicated automatically to every replicated AWS Region. You create, update, or remove the
conditional forwarder once, from any Region. The change then propagates to all Regions through
native Active Directory replication.

You can run the following commands from
[AWS CloudShell](../../../cloudshell/latest/userguide/welcome.md "../../../cloudshell/latest/userguide/welcome.md"), which comes with
the [AWS CLI](../../../cli/latest/userguide/cli-chap-welcome.md "../../../cli/latest/userguide/cli-chap-welcome.md") and
[AWS Tools for PowerShell](../../../powershell/latest/userguide/pstools-welcome.md "../../../powershell/latest/userguide/pstools-welcome.md") pre-installed. AWS CloudShell automatically
configures your credentials.

1. Sign in to the AWS Management Console.
2. Open [AWS CloudShell](https://console.aws.amazon.com/cloudshell/home "https://console.aws.amazon.com/cloudshell/home").
   To use the PowerShell commands, run `pwsh`.

## List conditional forwarders on your directory

You can list conditional forwarders on your directory by using the AWS CLI or PowerShell:

AWS CLI

###### To list conditional forwarders on your directory

- Run the following command, replacing the example value with your own:

```
aws ds describe-conditional-forwarders \
  --directory-id `d-123456abcd`
```

For more information, see [describe-conditional-forwarders](../../../cli/latest/reference/ds/describe-conditional-forwarders.md "../../../cli/latest/reference/ds/describe-conditional-forwarders.md") in the _AWS CLI Command Reference_.

PowerShell

###### To list conditional forwarders on your directory

- Run the following command, replacing the example value with your own:

```
Get-DSConditionalForwarder `
  -DirectoryId `d-123456abcd`
```

For more information, see [Get-DSConditionalForwarder](../../../powershell/latest/reference/items/Get-DSConditionalForwarder.md "../../../powershell/latest/reference/items/Get-DSConditionalForwarder.md") in the _AWS Tools for PowerShell Cmdlet Reference_.

## Create a conditional forwarder for your directory

You can create a conditional forwarder for your directory by using the AWS CLI or PowerShell:

AWS CLI

###### To create a conditional forwarder for your directory

- Run the following command, replacing the example values with your own:

```
aws ds create-conditional-forwarder \
  --directory-id `d-123456abcd` \
  --remote-domain-name `company.example.com` \
  --dns-ip-addrs `10.0.0.20` `10.0.0.21`
```

For more information, see [create-conditional-forwarder](../../../cli/latest/reference/ds/create-conditional-forwarder.md "../../../cli/latest/reference/ds/create-conditional-forwarder.md") in the _AWS CLI Command Reference_.

PowerShell

###### To create a conditional forwarder for your directory

- Run the following command, replacing the example values with your own:

```
New-DSConditionalForwarder `
  -DirectoryId `d-123456abcd` `
  -RemoteDomainName `company.example.com` `
  -DnsIpAddr `10.0.0.20`,`10.0.0.21`
```

For more information, see [New-DSConditionalForwarder](../../../powershell/latest/reference/items/New-DSConditionalForwarder.md "../../../powershell/latest/reference/items/New-DSConditionalForwarder.md") in the _AWS Tools for PowerShell Cmdlet Reference_.

## Update a conditional forwarder on your directory

To update the DNS servers for an existing conditional forwarder, use the same remote domain
name with the new set of DNS server IP addresses. The new addresses overwrite the previous IP addresses.
You can update a conditional forwarder by using the AWS CLI or PowerShell:

AWS CLI

###### To update a conditional forwarder on your directory

- Run the following command, replacing the example values with your own:

```
aws ds update-conditional-forwarder \
  --directory-id `d-123456abcd` \
  --remote-domain-name `company.example.com` \
  --dns-ip-addrs `10.2.0.20` `10.2.0.21`
```

For more information, see [update-conditional-forwarder](../../../cli/latest/reference/ds/update-conditional-forwarder.md "../../../cli/latest/reference/ds/update-conditional-forwarder.md") in the _AWS CLI Command Reference_.

PowerShell

###### To update a conditional forwarder on your directory

- Run the following command, replacing the example values with your own:

```
Update-DSConditionalForwarder `
  -DirectoryId `d-123456abcd` `
  -RemoteDomainName `company.example.com` `
  -DnsIpAddr `10.2.0.20`,`10.2.0.21`
```

For more information, see [Update-DSConditionalForwarder](../../../powershell/latest/reference/items/Update-DSConditionalForwarder.md "../../../powershell/latest/reference/items/Update-DSConditionalForwarder.md") in the _AWS Tools for PowerShell Cmdlet Reference_.

## Remove a conditional forwarder from your directory

You can remove a conditional forwarder from your directory by using the AWS CLI or PowerShell:

AWS CLI

###### To remove a conditional forwarder from your directory

- Run the following command, replacing the example values with your own:

```
aws ds delete-conditional-forwarder \
  --directory-id `d-123456abcd` \
  --remote-domain-name `company.example.com`
```

For more information, see [delete-conditional-forwarder](../../../cli/latest/reference/ds/delete-conditional-forwarder.md "../../../cli/latest/reference/ds/delete-conditional-forwarder.md") in the _AWS CLI Command Reference_.

PowerShell

###### To remove a conditional forwarder from your directory

- Run the following command, replacing the example values with your own:

```
Remove-DSConditionalForwarder `
  -DirectoryId `d-123456abcd` `
  -RemoteDomainName `company.example.com`
```

For more information, see [Remove-DSConditionalForwarder](../../../powershell/latest/reference/items/Remove-DSConditionalForwarder.md "../../../powershell/latest/reference/items/Remove-DSConditionalForwarder.md") in the _AWS Tools for PowerShell Cmdlet Reference_.
