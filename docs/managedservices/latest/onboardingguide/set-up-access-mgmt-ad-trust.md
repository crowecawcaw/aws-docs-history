# Establish an Active Directory Trust

To set up a trust, AMS requires your domain controller **Local Policies -> Security Options ->
Network Access: Named Pipes that can be accessed anonymously**, have the
**Netlogon** and **lsarpc** pipes listed. These pipes are listed by default, but are sometimes removed for security
concerns. Once the trust is established, they can be removed from the list again.
