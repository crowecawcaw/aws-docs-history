# Metadata permissions

Lake Formation provides authorization and access control for the Data Catalog. When an IAM role
makes a Data Catalog API call from any system, the Data Catalog verifies the user's data
permissions and only returns the metadata that the user has permissions to access. For
example, if an IAM role has access to only one table within a database, and a service
or a user assuming the role performs the `GetTables` operation, the response will contain only the one table, regardless of the number of
tables in the database.

**Default settings - `IAMAllowedPrincipal` group permissions**

AWS Lake Formation, by default, sets permissions to all databases and tables to a virtual group
named `IAMAllowedPrincipal`. This group is unique and visible only within
Lake Formation. The `IAMAllowedPrincipal` group includes all IAM principals who have
access to Data Catalog resources through IAM principal policies and AWS Glue resource
policies. If this permissions exists on a database or table,
all principals will be granted access to the database or table.

If you want to provide more granular permissions on a database or table, remove
`IAMAllowedPrincipal` permission and, Lake Formation enforces all other policies
associated with that database or table. For example, if there is a policy that allows
User A to access Database A with `DESCRIBE` permissions, and the
`IAMAllowedPrincipal` exists with all permissions, User A will continue
to perform all other actions, until the `IAMAllowedPrincipal` permission is
revoked.

Additionally, by default, the `IAMAllowedPrincipal` group has permissions
on all new databases and tables when they are created. There are two configurations that
control this behaviour. The first is at the account and Region-level that enables this
for newly created databases, and the second is at the database level. To modify the default
setting, see [Change the default permission model or use
hybrid access mode](initial-lf-config.md#setup-change-cat-settings "initial-lf-config.md#setup-change-cat-settings").

## Granting permissions

Data lake administrators can grant Data Catalog permissions to principals so that the principals can create and manage databases and tables, and can access underlying data.

**Database and table-level permissions**

When you grant permissions within Lake Formation, the grantor must specify the principal to
grant permissions to, the resources to grant permissions on, and the actions that
the grantee should have access to perform. For most resources within Lake Formation, the
principal list and resources to grant permissions are similar, but the actions that
a grantee can perform differs based on the resource type. For example,
`SELECT` permissions are available for tables to read the tables, but
`SELECT` permissions are not allowed on databases. The
`CREATE_TABLE` permission is permissible on databases, but not on
tables.

You can grant AWS Lake Formation permissions using two methods:

- [Named resource method](granting-cat-perms-named-resource.md "granting-cat-perms-named-resource.md") – Allows you to choose database and table names while granting permissions to users.
- [LF-Tag based access control (LF-TBAC)](granting-catalog-perms-TBAC.md "granting-catalog-perms-TBAC.md") – Users create LF-Tags, associate them with Data Catalog resources, grant `Describe` permission on LF-Tags, associate permissions to
  individual users, and write LF permissions policies using LF-Tags to different
  users. Such LF-Tag-based policies apply to all Data Catalog resources that are
  associated with those LF-Tag values.

###### Note

LF-Tags are unique to Lake Formation. They are only visible in Lake Formation and should not be confused with AWS resource tags.

LF-TBAC is a feature that allows users to group
resources into user-defined categories of LF-Tags and apply permissions on those
resource groups. Hence, it is the best way to scale permissions across huge
number of Data Catalog resources.

For more information, see [Lake Formation tag-based access control](tag-based-access-control.md "tag-based-access-control.md").

When you grant permissions to a principal, Lake Formation evaluates permissions as a union
of all the policies for that user. For example, if you have two policies on a table
for a principal where one policy grants permissions to columns col1, col2, and col3
through named resource method, and the other policy grants permissions to the same
table and principal to col5, and col6 through LF-Tags, the effective permissions
will be a union of the permissions which would be col1, col2, col3, col5, and col6.
This also includes data filters and rows.

###### Data location permissions

Data location permissions provides non-administrative users the ability to create databases
and tables at specific Amazon S3 locations. If a user attempts to create a database or a
table in a location that they don't have permissions to create, the creation task
fails. This is to prevent users from creating tables in arbitrary locations within
the data lake and provides control over where those users can read and write data. There
is an implicit permission when creating tables in the Amazon S3 location within the
database it is being created in. For more information, see [Granting data location permissions](granting-location-permissions.md "granting-location-permissions.md").

###### Create table and database permissions

Non administrative users by default don't have permissions to create databases
or tables within a database. Database creation is controlled at the
account-level using the Lake Formation settings so that only authorized principals can
create databases. For more information, see [Creating a database](creating-database.md "creating-database.md"). To create a table, a principal requires
`CREATE_TABLE` permission on the database where the table is
being created. For more information, see [Creating tables](creating-tables.md "creating-tables.md").

###### Implicit and explicit permissions

Lake Formation provides implicit permissions depending on the persona and the actions that the persona performs.
For example, data lake administrators automatically get `DESCRIBE` permissions to all resources within the Data Catalog,
data location permissions to all locations, permissions to create databases and tables in all locations, as well as `Grant` and `Revoke` permissions on any resource.
Database creators automatically get all database permissions on the databases that they create, and
table creators get all permissions on the tables that they create.
For more information, see [Implicit Lake Formation permissions](implicit-permissions.md "implicit-permissions.md").

###### Grantable permissions

Data lake administrators have the ability to delegate the management of
permissions to non administrative users by providing grantable permissions. When
a principal is provided grantable permissions on a resource and a set of
permissions, that principal gains the ability to grant permissions to other
principals on that resource.
