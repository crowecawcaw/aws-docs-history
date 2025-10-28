# Managing DNS aliases

In addition to the default Domain Name System (DNS) name that Amazon FSx provides, you can also
associate DNS aliases of your choosing with your file systems. With DNS aliases, you can continue
using existing DNS names to access data stored on Amazon FSx when [migrating file system storage](migrate-to-fsx.md "migrate-to-fsx.md")
from on-premises to Amazon FSx, without needing to update any tools or applications.

You can associate DNS aliases with new and existing FSx for Windows File Server file systems, and when you restore a
backup to a new file system, using the AWS Management Console and AWS CLI. You can associate up to 50 DNS aliases with a file system at any one time.

###### Note

Support for DNS aliases is available on FSx for Windows File Server file systems created after 12:00 pm ET on November 9, 2020.
To use DNS aliases on a file system created before 12:00 pm ET on November 9, 2020, do the following:

1. Take a backup of the existing file system. For more information, see [Working with user-initiated backups](using-backups.md#user-initiated-backups "using-backups.md#user-initiated-backups").
2. Restore the backup to a new file system. For more information, see [Restoring backups to new file system](using-backups.md#restoring-backups "using-backups.md#restoring-backups").
   Once the new file system is available, you will be able to use DNS aliases to access it, using the information provided in this section.

###### Note

The information presented here assumes that you're working entirely within Active Directory
and that you're not using external DNS providers. Third-party DNS providers may result in unexpected behavior.

Amazon FSx only registers DNS records for a file system if the Active Directory domain that you are joining it to is
using Microsoft DNS as the default DNS. If you are using a third-party DNS, you will need to manually
set up DNS entries for your Amazon FSx file systems after you create your file system. For more information
on choosing the correct IP addresses to use for the file system,
see [Getting the correct file system IP addresses to use for manual DNS entries](file-system-ip-addresses-for-dns.md "file-system-ip-addresses-for-dns.md").

You can associate DNS aliases with existing FSx for Windows File Server file systems, when you create new
file systems, and when you create a new file system from a backup. You can associate up to 50 DNS
aliases with a file system at any one time.

In addition to associating DNS aliases with your file system, for clients to connect to the
file system using the DNS aliases, you also must do the following:

- Configure service principal names (SPNs) for Kerberos authentication and encryption.
- Configure a DNS CNAME record for the DNS alias that resolves to
  the default DNS name for your Amazon FSx file system.
  For more information,
  see [Accessing data using DNS aliases](dns-aliases.md "dns-aliases.md").

A DNS alias name for your FSx for Windows File Server file system needs to meet the following requirements:

- Must be formatted as a fully qualified domain name (FQDN).
- Can contain alphanumeric characters and hyphens (‐).
- Cannot start or end with a hyphen.
- Can start with a numeric.
  For DNS alias names, Amazon FSx stores alphabetic characters as lowercase letters (a-z),
  regardless of how you specify them: as uppercase letters, lowercase letters, or the corresponding
  letters in escape codes.

If you try to associate an alias that is already associated with the file system, it has no
effect. If you try to disassociate an alias from a file system that is not associated with the
file system, Amazon FSx responds with a bad request error.

###### Note

When Amazon FSx adds or removes aliases on a file system, connected clients are temporarily
disconnected and will automatically reconnect to the file system. Any files that were open by
clients mapping a non-Continuously-Available (non-CA) share at the time of disconnection must be
reopened by the client.

###### Topics

- [DNS alias status](#alias-status "#alias-status")
- [Using DNS aliases with Kerberos authentication](#aliases-and-kerberos "#aliases-and-kerberos")
- [Viewing DNS aliases for file systems and backups](view-aliases.md "view-aliases.md")
- [Associating DNS aliases with file systems](add-alias-new-filesystem.md "add-alias-new-filesystem.md")
- [Managing DNS aliases on existing file systems](manage-aliases-existing-fs.md "manage-aliases-existing-fs.md")

## DNS alias status

DNS aliases can have one of the following status values:

- Available – The DNS alias is associated with an Amazon FSx file system.
- Creating – Amazon FSx is creating the DNS alias and associating it with the file
  system.
- Deleting – Amazon FSx is disassociating the DNS alias from the file system and deleting
  it.
- Failed to create – Amazon FSx was unable to associate the DNS alias with the file
  system.
- Failed to delete – Amazon FSx was unable to disassociate the DNS alias from the file
  system.

## Using DNS aliases with Kerberos authentication

We recommend that you use Kerberos-based authentication and encryption in transit with
Amazon FSx. Kerberos provides the most secure authentication for clients accessing your file system.
To enable Kerberos authentication for clients that access your Amazon FSx file system using a DNS
alias, you must configure service principal names (SPNs) that correspond to the DNS alias on your
file system’s Active Directory computer object.

If you have SPNs conﬁgured for the DNS alias that you've assigned to another ﬁle system on a
computer object in your Active Directory, you must ﬁrst remove those SPNs before adding SPNs to
your ﬁle system’s computer object. For more information, see
[Configure service principal names (SPNs) for Kerberos](step2-configure-spn-kerberos.md "step2-configure-spn-kerberos.md").
