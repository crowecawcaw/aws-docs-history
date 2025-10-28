# Amazon Redshift data sharing limitations

AWS Lake Formation allows you to securely manage data in a datashare from Amazon Redshift.
Amazon Redshift is a fully managed, petabyte-scale data warehouse service in the AWS Cloud.
Using the data sharing capability, Amazon Redshift helps you to share data across AWS accounts.
For more information about Amazon Redshift data sharing, see [Overview of data sharing in Amazon Redshift](../../../redshift/latest/dg/data_sharing_intro.md "../../../redshift/latest/dg/data_sharing_intro.md").

The following notes and restrictions apply to federated databases that are created from
Amazon Redshift datashares:

- Mapped database requirement – Every Amazon Redshift datashare must
  be mapped to a new database in Lake Formation. This is required to maintain unique table names when
  the datashare objects representation is flattened in the Data Catalog database.
- Limitation on creating new tables under a federated
  database – You will not be able to create new tables under federated
  databases.
- Permissions on the federated databases – The permissions
  applied on a federated database or tables under a federated database persist even when a
  source table or a database is deleted. When the source database or table is recreated, you
  do not need to regrant the permissions. When a federated table with Lake Formation permissions is
  deleted at source, Lake Formation permissions will still be visible and you can revoke them if
  needed.

If a user deletes a federated database, all its corresponding permissions are lost.
Recreating the same database with the same name, will not recover Lake Formation permissions. Users
will have to setup new permissions again.

- IAMAllowedPrincipal group permissions on federated databases – Based on the
  `DataLakeSettings`, Lake Formation might set permissions to all databases and tables to a
  virtual group named `IAMAllowedPrincipal`. The `IAMAllowedPrincipal`
  refers to all IAM principals who have access to Data Catalog resources through IAM
  principal policies and AWS Glue resource policies. If these permissions exist on a database
  or a table, all principals are granted access to the database or table.

However, Lake Formation
doesn't allow `IAMAllowedPrincipal` permissions on tables under federated
databases. When you create federated databases, make sure that you pass the
`CreateTableDefaultPermissions` parameter as an empty list.

For more information, see [Changing the default settings for your data
lake](change-settings.md "change-settings.md").

- Data filtering – In Lake Formation, you can grant permissions on a
  table under a federated database with column-level and row-level filtering. However, you
  can't combine column-level and row-level filtering to restrict access at cell-level
  granularity on tables under federated databases.
- Case sensitivity identifier – Amazon Redshift datashare objects
  managed by Lake Formation, will support table names and column names only in lowercase. Don't turn
  on case sensitivity identifier for databases, tables, and columns in Amazon Redshift datashares, if
  they will be shared and managed using Lake Formation.
- Query support – You can query Amazon Redshift datashares
  managed by Lake Formation with Amazon Redshift. Athena doesn't support querying Amazon Redshift datashares managed by
  Lake Formation.
  For more information on limitations when working with datashares in Amazon Redshift, see [Limitations for data sharing](../../../redshift/latest/dg/datashare-overview.md#limitations-datashare "../../../redshift/latest/dg/datashare-overview.md#limitations-datashare") in the Amazon Redshift Database Developer Guide.
