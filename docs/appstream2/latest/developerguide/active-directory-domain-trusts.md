# Configuring AppStream 2.0 to Use Domain

Trusts

AppStream 2.0 supports Active Directory domain environments where network resources such
as file servers, applications, and computer objects reside in one domain, and the
user objects reside in another. The domain service account used for computer object
operations does not need to be in the same domain as the AppStream 2.0 computer objects.

When creating the directory configuration, specify a service account that has the
appropriate permissions to manage computer objects in the Active Directory domain
where the file servers, applications, computer objects and other network resources
reside.

Your end user Active Directory accounts must have the "Allowed to Authenticate"
permissions for the following:

- AppStream 2.0 computer objects
- Domain controllers for the domain
  For more information, see [Granting Permissions to Create and Manage
  Active Directory Computer Objects](active-directory-permissions.md "active-directory-permissions.md").
