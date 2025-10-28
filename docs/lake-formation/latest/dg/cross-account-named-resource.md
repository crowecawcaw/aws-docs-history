# Cross-account data sharing using the named resource method

You can grant permissions to directly to principals in the another AWS account, or to
external AWS accounts or AWS Organizations. Granting Lake Formation permissions to Organizations
or organizational units is equivalent to granting the permission to every AWS account in
that organization or organizational unit.

When you grant permissions to external accounts or organizations, you must include the
**Grantable permissions** option. Only the data lake administrator in the external account can access the shared
resources until the administrator grants permissions on the shared resources to other
principals in the external account.

###### Note

**Grantable permissions** option is not supported when granting permissions directly to IAM principals from external accounts.

Follow instructions in [Granting database permissions using the
named resource method](granting-database-permissions.md "granting-database-permissions.md") to grant cross-account permissions using the named resource method.

The following video demonstrates how to share data with an AWS organization using Lake Formation.
