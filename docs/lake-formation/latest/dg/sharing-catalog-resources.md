# Sharing Data Catalog tables and databases across AWS

Accounts

You can share Data Catalog resources (databases and tables) with external AWS accounts by
granting Lake Formation permissions on the resources to the external accounts. Users can then run queries
and jobs that join and query tables across multiple accounts. With some restrictions, when you
share a Data Catalog resource with another account, principals in that account can operate on that
resource as if the resource were in their Data Catalog.

You don't share resources with specific principals in external AWS accounts—you
share the resources with an AWS account or organization. When you share a resource with an AWS
organization, you're sharing the resource with all accounts at all levels in that organization.
The data lake administrator in each external account must then grant permissions on the shared
resources to principals in their account.

For more information, see [Cross-account data sharing in Lake Formation](cross-account-permissions.md "cross-account-permissions.md") and [Granting permissions on Data Catalog resources](granting-catalog-permissions.md "granting-catalog-permissions.md").

###### See Also:

- [Accessing and viewing shared Data Catalog tables and
  databases](viewing-shared-resources.md "viewing-shared-resources.md")
- [Prerequisites](cross-account-prereqs.md "cross-account-prereqs.md")
