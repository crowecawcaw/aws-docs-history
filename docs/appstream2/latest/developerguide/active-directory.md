# Using Active Directory with AppStream 2.0

You can join your Amazon AppStream 2.0 Always-On and On-Demand Windows fleets and image builders to
domains in Microsoft Active Directory and use your existing Active Directory domains, either
cloud-based or on-premises, to launch domain-joined streaming instances. You can also use
AWS Directory Service for Microsoft Active Directory, also known as AWS Managed Microsoft AD, to create an Active Directory
domain and use that to support your AppStream 2.0 resources. For more information about using AWS
Managed Microsoft AD, see [Microsoft Active Directory](../../../directoryservice/latest/admin-guide/directory_microsoft_ad.md "../../../directoryservice/latest/admin-guide/directory_microsoft_ad.md") in the
_AWS Directory Service Administration Guide_.

###### Note

Amazon Linux 2 fleets, image builders, elastic fleets, and app block builders
currently do not support domain join.

By joining AppStream 2.0 to your Active Directory domain, you can:

- Allow your users and applications to access Active Directory resources such
  as printers and file shares from streaming sessions.
- Use Group Policy settings that are available in the Group Policy Management
  Console (GPMC) to define the end user experience.
- Stream applications that require users to be authenticated using their Active
  Directory login credentials.
- Apply your enterprise compliance and security policies to your AppStream 2.0 streaming
  instances.

###### Contents

- [Overview of Active Directory Domains](active-directory-overview.md "active-directory-overview.md")
- [Before You Begin Using Active Directory with Amazon AppStream 2.0](active-directory-prerequisites.md "active-directory-prerequisites.md")
- [Tutorial: Setting Up Active
  Directory](active-directory-directory-setup.md "active-directory-directory-setup.md")
- [Certificate-Based
  Authentication](certificate-based-authentication.md "certificate-based-authentication.md")
- [AppStream 2.0 Active Directory Administration](active-directory-admin.md "active-directory-admin.md")
- [More Info](active-directory-more-info.md "active-directory-more-info.md")
