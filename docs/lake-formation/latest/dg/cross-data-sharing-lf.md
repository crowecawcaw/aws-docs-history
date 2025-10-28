# Cross-account data sharing in Lake Formation

With Lake Formation, you can share Data Catalog resources (databases and tables) within an AWS
account and across accounts in a simple setup using the named resource method or
LF-Tags. You can share an entire database or select tables from a database to any IAM
principals (IAM roles and users) in an account, to other AWS accounts at the account
level, or directly to IAM principals in another account.

You can also share Data Catalog tables with data filters to restrict access to the details
at the row-level and cell-level details. Lake Formation uses AWS Resource Access Manager (AWS RAM) to facilitate
granting permissions between accounts. When a resource is shared between two accounts,
AWS RAM sends invites to the recipient account. When a user accepts a AWS RAM share
invitation, AWS RAM provides the necessary permissions to Lake Formation to have the Data Catalog
resources available as well as enabled storage level enforcement. For more
information, see [Cross-account data sharing in Lake Formation](cross-account-permissions.md "cross-account-permissions.md").

When the data lake administrator of the recipient account accepts the AWS RAM share, the
shared resources are available in the recipient account. The data lake administrator
grants further Lake Formation permissions on the shared resource to additional IAM principals in
the recipient account, if the administrator has `GRANTABLE` permissions on
the shared resource.

However, the principals can't query the shared resources using Athena or Redshift Spectrum without
a resource link. A resource link is an entity in the Data Catalog and is similar to a
Linux-Symlink concept.

The data lake administrator of the recipient account creates a resource link on the
shared resource. The administrator grants `Describe` permissions on the
resource link with the required permissions on the original shared resource to
additional users. A user in recipient account can then use the resource link to query
the shared resource using Athena and Redshift Spectrum. For more information about resource links,
see [Creating resource links](creating-resource-links.md "creating-resource-links.md").
