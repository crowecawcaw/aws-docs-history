# Configure service principal names (SPNs) for Kerberos

We recommend that you use Kerberos-based authentication and encryption in transit with
Amazon FSx. Kerberos provides the most secure authentication for clients that access your file
system.

To enable Kerberos authentication for clients that access Amazon FSx using a DNS alias, you
must add service principal names (SPNs) that correspond to the DNS alias on your Amazon FSx file
system’s Active Directory computer object. An SPN can only be associated with a single Active
Directory computer object at a time. If you have existing SPNs for the DNS name configured for
your original file system's Active Directory computer object, you must delete them first.

There are two required SPNs for Kerberos authentication:

```
HOST/`alias`
HOST/`alias.domain`
```

If the alias is `finance.domain.com`, the following are the two required
SPNs:

```
HOST/finance
HOST/finance.domain.com
```

###### Note

You will need to delete any existing HOST SPNs that correspond to the DNS alias on the Active Directory
computer object before you create new HOST SPNs for your Amazon FSx file system's Active Directory (AD) computer object.
Attempts to set SPNs for your Amazon FSx file system will fail if an SPN for the DNS alias exists in the AD.

The following procedures describes how to do the following:

- Find any existing DNS alias SPNs on the original file system's Active
  Directory computer object.
- Delete the existing SPNs found, if any.
- Create new DNS alias SPNs for your Amazon FSx file system's Active Directory computer object.

###### To install the required PowerShell Active Directory module

1. Log on to a Windows instance joined to the Active Directory to which your Amazon FSx file
   system is joined.
2. Open PowerShell as administrator.
3. Install the PowerShell Active Directory module using the following command.

```
Install-WindowsFeature RSAT-AD-PowerShell
```

###### To find and delete existing DNS alias SPNs on the original file system's Active

Directory computer object

If you have SPNs conﬁgured for the DNS alias that you've assigned to another ﬁle system on a
computer object in your Active Directory, you must ﬁrst remove those SPNs before adding SPNs to
your ﬁle system’s computer object.

1. Find any existing SPNs by using the following commands. Replace `alias_fqdn`
   with the DNS alias that you associated with the file system in [Step 1](step1-assign-dns-alias.md "step1-assign-dns-alias.md").

```
## Find SPNs for original file system's AD computer object
$ALIAS = "`alias_fqdn`"
SetSPN /Q ("HOST/" + $ALIAS)
SetSPN /Q ("HOST/" + $ALIAS.Split(".")[0])
```

2. Delete the existing HOST SPNs returned in the previous step by using the following example script.
   - Replace `alias_fqdn` with the full DNS alias
     that you associated with the file system in [Step 1](step1-assign-dns-alias.md "step1-assign-dns-alias.md").
   - Replace `file_system_DNS_name` with the original file system's DNS name.

```
## Delete SPNs for original file system's AD computer object
$Alias = "`alias_fqdn`"
$FileSystemDnsName = "`file_system_dns_name`"
$FileSystemHost = (Resolve-DnsName ${FileSystemDnsName} | Where Type -eq 'A')[0].Name.Split(".")[0]
$FSxAdComputer = (Get-AdComputer -Identity ${FileSystemHost})

SetSPN /D ("HOST/" + ${Alias}) ${FSxAdComputer}.Name
SetSPN /D ("HOST/" + ${Alias}.Split(".")[0]) ${FSxAdComputer}.Name

```

3. Repeat the previous steps for each DNS alias that you've associated with the file
   system in [Step 1](step1-assign-dns-alias.md "step1-assign-dns-alias.md").

###### To set SPNs on your Amazon FSx file system’s Active Directory computer object

1. Set new SPNs for your Amazon FSx file system by running the following commands.
   - Replace `file_system_DNS_name` with the DNS name that
     Amazon FSx assigned to the file system.

   To find your file system's DNS name on the Amazon FSx console, choose
   **File systems**, choose your file system, and then choose the
   **Network & security** pane on the file system details page.

   You can also get the DNS name in the response of the [DescribeFileSystems](../APIReference/API_DescribeFileSystems.md "../APIReference/API_DescribeFileSystems.md") API operation.
   - Replace `alias_fqdn` with the full DNS alias that you
     associated with the file system in [Step
     1](step1-assign-dns-alias.md "step1-assign-dns-alias.md").

```
## Set SPNs for FSx file system AD computer object
$FSxDnsName = "`file_system_DNS_name`"
$Alias = "`alias_fqdn`"
$FileSystemHost = (Resolve-DnsName $FSxDnsName | Where Type -eq 'A')[0].Name.Split(".")[0]
$FSxAdComputer = (Get-AdComputer -Identity $FileSystemHost)

##Use the following command to set both the full FQDN and Alias SPNs
Set-AdComputer -Identity $FSxAdComputer -Add @{"msDS-AdditionalDnsHostname" = @($Alias, $Alias.Split(".")[0])}
```

###### Note

Setting an SPN for your Amazon FSx file system will fail if an SPN for the DNS alias exists in the AD for the
original file system's computer object. For information about finding and deleting existing SPNs, see
[To find and delete existing DNS alias SPNs on the original file system's Active
Directory computer object](#find-delete-existing-spns "#find-delete-existing-spns"). 2. Verify that the new SPNs are configured for the DNS alias using the following example script. Ensure that the
response includes two HOST SPNs, `HOST/`alias`` and
 `HOST/`alias_fqdn``, as described previously in this procedure.

Replace `file_system_DNS_name` with the DNS name that
Amazon FSx assigned to your file system. To find your file system's DNS name on the Amazon FSx console, choose
**File systems**, choose your file system, and then choose the
**Network & security** pane on the file system details page.

You can also get the DNS name in the response of the [DescribeFileSystems](../APIReference/API_DescribeFileSystems.md "../APIReference/API_DescribeFileSystems.md") API operation.

```
## Verify SPNs on FSx file system AD computer object
$FileSystemDnsName = "`file_system_dns_name`"
$FileSystemHost = (Resolve-DnsName ${FileSystemDnsName} | Where Type -eq 'A')[0].Name.Split(".")[0]
$FSxAdComputer = (Get-AdComputer -Identity ${FileSystemHost})
SetSpn /L ${FSxAdComputer}.Name
```

3. Repeat the previous steps for each DNS alias that you've associated with the file
   system in [Step 1](step1-assign-dns-alias.md "step1-assign-dns-alias.md").
