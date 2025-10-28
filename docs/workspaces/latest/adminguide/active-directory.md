# Using Active Directory with WorkSpaces Pools

You can join your Windows WorkSpaces in WorkSpaces Pools to domains in Microsoft Active Directory and
use your existing Active Directory domains, either cloud-based or on-premises, to launch
domain-joined streaming instances. You can also use AWS Directory Service for Microsoft Active Directory, also known as
AWS Managed Microsoft AD, to create an Active Directory domain and use that to support your WorkSpaces Pools
resources. For more information about using AWS Managed Microsoft AD, see [Microsoft Active Directory](../../../directoryservice/latest/admin-guide/directory_microsoft_ad.md "../../../directoryservice/latest/admin-guide/directory_microsoft_ad.md") in the
_AWS Directory Service Administration Guide_.

By joining WorkSpaces Pools to your Active Directory domain, you can:

- Allow your users and applications to access Active Directory resources such as
  printers and file shares from streaming sessions.
- Use Group Policy settings that are available in the Group Policy Management
  Console (GPMC) to define the end user experience.
- Stream applications that require users to be authenticated using their Active
  Directory login credentials.
- Apply your enterprise compliance and security policies to your WorkSpaces in
  WorkSpaces Pools.

###### Contents

- [Overview of Active Directory Domains](active-directory-overview.md "active-directory-overview.md")
- [Before You Begin Using Active Directory
  with WorkSpaces Pools](active-directory-prerequisites.md "active-directory-prerequisites.md")
- [Certificate-Based
  Authentication](pools-certificate-based-authentication.md "pools-certificate-based-authentication.md")
- [WorkSpaces Pools Active Directory
  Administration](active-directory-admin.md "active-directory-admin.md")
- [More Info](active-directory-more-info.md "active-directory-more-info.md")
