# Accessing data using DNS aliases

FSx for Windows File Server provides a DNS name for every file system that you can use to access your
file shares. You can also access your file shares using DNS names other than the
default DNS name by registering DNS aliases for your FSx for Windows File Server
file systems.

Using DNS aliases, you can move your Windows file share data to FSx for Windows File Server and continue
using the existing DNS names to access data on Amazon FSx. DNS aliases also allow you to
use meaningful names that make it easier to administer tools and applications to
connect to your Amazon FSx file systems. You can associate up to 50 DNS aliases with a file system at any one time.
For more information about associating and disassociating
DNS aliases with an FSx for Windows File Server file system, see [Managing DNS aliases](managing-dns-aliases.md "managing-dns-aliases.md").

To configure access to your FSx for Windows File Server file systems using DNS aliases, you must perform the following
steps:

1. [Associate DNS aliases with your file system](step1-assign-dns-alias.md "step1-assign-dns-alias.md").
2. [Create a DNS CNAME record](step4-configure-dns-cname.md "step4-configure-dns-cname.md") for the file system
   and the DNS aliases associated with it.
   For more information about using DNS aliases with FSx for Windows File Server file systems, see
   [Managing DNS aliases](managing-dns-aliases.md "managing-dns-aliases.md").

## Using Kerberos authentication and encryption with DNS aliases

We recommend that you use Kerberos-based authentication and encryption in transit
with Amazon FSx. Kerberos provides the most secure authentication for clients
accessing your file system. To enable Kerberos authentication for clients that
access Amazon FSx using a DNS alias, you must add service principal names (SPNs) that
correspond to the DNS alias on your Amazon FSx file system’s Active Directory
computer object.

To set up Kerberos authentication and encryption when accessing your file system using DNS aliases, see
[Configure service principal names (SPNs) for Kerberos](step2-configure-spn-kerberos.md "step2-configure-spn-kerberos.md").

You can optionally enforce clients that access the file system using a DNS
alias to use Kerberos authentication and encryption by setting the following
Group Policy Objects (GPOs) in your Active Directory:

- **Restrict NTLM: Outgoing NTLM traffic to remote servers** - Use this policy setting to deny or audit
  outgoing NTLM traffic from a computer to any remote server running the Windows operating system.
- **Restrict NTLM: Add remote server exceptions for NTLM authentication** - Use this policy setting
  to create an exception list of remote servers to which client devices are allowed to use NTLM authentication if the
  _Network security: Restrict NTLM: Outgoing NTLM traffic to remote servers_
  policy setting is configured.

To enforce Kerberos authentication and encryption when accessing your file system using DNS aliases, see
[Enforcing Kerberos authentication using Group Policy Objects (GPOs)](enforce-kerberos.md "enforce-kerberos.md").

For more information about configure your file system to use DNS aliases, see the following procedures:

- [Associate DNS aliases with your file system](step1-assign-dns-alias.md "step1-assign-dns-alias.md")
- [Configure service principal names (SPNs) for Kerberos](step2-configure-spn-kerberos.md "step2-configure-spn-kerberos.md")
- [Update or create a DNS CNAME record](step4-configure-dns-cname.md "step4-configure-dns-cname.md")
- [Enforcing Kerberos authentication using Group Policy Objects (GPOs)](enforce-kerberos.md "enforce-kerberos.md")
