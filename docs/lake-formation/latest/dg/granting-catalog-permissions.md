# Granting permissions on Data Catalog resources

You can grant **Data permissions** to principals in AWS Lake Formation so that
the principals can create and manage Data Catalog resources, and can access underlying data. You
can grant **Data lake permissions** on catalogs, databases, tables, and
views. When you grant permissions on tables, you can limit access to specific table columns or
rows for even more fine-grained access control.

You can grant permissions on individual catalogs, databases, tables and views, or with a single grant
operation, you can grant permissions on all databases, tables and views in a catalog or a
database. If you grant permissions on all tables in a database to IAM principals, you are
implicitly granting the `DESCRIBE` permission on the database. The database then
appears on the **Databases** page on the console, and is returned by the
`GetDatabases` API operation. The same principle applies at the catalog level -
when you receive permissions for databases within a catalog, you also get
`DESCRIBE` permissions for that catalog.

###### Important

The implicit `DESCRIBE` permission applies only when granting permissions to
IAM principals within the same AWS account. For cross-account resources, you must
explicitly grant `DESCRIBE` permissions. The automatic `DESCRIBE` permission grant
doesn't apply when using attribute-based access control (ABAC). When granting permissions
on all tables in a database using attributes, Lake Formation doesn't implicitly grant
`DESCRIBE` permission to the database.

You can grant permissions by using either the named resource method or the Lake Formation tag-based
access control (LF-TBAC) method.

You can grant permissions to principals in the same AWS account or to external accounts
or organizations. When you grant to external accounts or organizations, you are sharing Data
Catalog objects that you own with those accounts or organizations. Principals in those
accounts or organizations can then access Data Catalog objects that you own and the underlying
data.

###### Note

Currently, the LF-TBAC method supports granting cross-account permissions to IAM principals, AWS accounts, organizations, and organizational units (OUs).

When you grant permissions to external accounts or organizations, you must include the
grant option. Only the data lake administrator in the external account can access the shared
objects until the administrator grants permissions on the shared objects to other principals
in the external account.

You can grant Data Catalog permissions by using the AWS Lake Formation console, the API, or the AWS Command Line Interface
(AWS CLI).

###### Note

When you delete a Data Catalog object, all permissions that are associated with the object become
invalid. Recreating the same resource with the same name, will not recover Lake Formation
permissions. Users will have to setup new permissions again.

###### See also:

- [Sharing Data Catalog tables and databases across AWS
  Accounts](sharing-catalog-resources.md "sharing-catalog-resources.md")
- [Metadata access control](access-control-metadata.md "access-control-metadata.md")
- [Lake Formation permissions reference](lf-permissions-reference.md "lf-permissions-reference.md")
