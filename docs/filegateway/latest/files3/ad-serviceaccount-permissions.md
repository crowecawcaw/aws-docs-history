# Active Directory service account permission

requirements

If you plan to use Microsoft Active directory to provide user authenticated access to the
file shares on your AWS Storage Gateway, you need to make sure that you have an Active
Directory service account, and that the service account has delegated permissions to join
computers to your domain. A service account is an Active Directory user account that has
been delegated permission to perform certain tasks. You provide the username and password
credentials for this account when you join a Storage Gateway to your Active Directory domain.

The Active Directory service account must be delegated the following permissions in the OU
to which you are joining your gateway:

- Ability to create and delete computer objects
- Ability to reset passwords
- Ability to modify permissions
- Ability to restrict accounts from reading and writing data
- Validated ability to read and write Account Restrictions
- Validated ability to write to the service principal name
- Validated ability to write to the DNS host name
  These represent the minimum set of permissions that are required to join computer objects
  to your Active Directory. For more information, see the Microsoft Windows Server
  documentation topic [Error: Access is denied when non-administrator users who have been delegated control
  try to join computers to a domain controller](https://learn.microsoft.com/en-us/troubleshoot/windows-server/active-directory/access-denied-when-joining-computers "https://learn.microsoft.com/en-us/troubleshoot/windows-server/active-directory/access-denied-when-joining-computers").
