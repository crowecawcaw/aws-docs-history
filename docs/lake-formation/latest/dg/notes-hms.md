# Hive metadata store data sharing considerations and

limitations

With AWS Glue Data Catalog metadata federation (Data Catalog federation), you can connect the Data Catalog to
external metastores that store metadata for your Amazon S3 data, and securely manage data access
permissions using AWS Lake Formation.

The following considerations and limitations apply to federated databases that are created from
Hive databases:

###### Considerations

- AWS SAM application support – You're responsible
  for the availability of application resources that AWS SAM deploys (Amazon API Gateway and
  Lambda function). Make sure that the connection between the AWS Glue Data Catalog and the Hive
  metastore is working when users run queries.
- Hive metastore version requirement – You can create federated databases only using Apache Hive version 3 and above.
- Mapped database requirement – Every Hive database
  must be mapped to a new database in Lake Formation.
- Database-level federation support – You can connect to
  Hive metastore only at the database level.
- Permissions on federated databases – The permissions
  applied on a federated database or tables under a federated database persist even when a
  source table or a database is deleted. When the source database or table is recreated, you
  don't need to regrant the permissions. When a federated table with Lake Formation permissions is
  deleted at source, Lake Formation permissions are still visible, and you can revoke them if
  needed.

If a user deletes a federated database, all of its corresponding permissions are lost.
Recreating the same database with the same name, will not recover Lake Formation permissions. Users
will have to setup new permissions again.

- IAMAllowedPrincipal group permissions on federated databases
  – Based on the `DataLakeSettings`, Lake Formation might set permissions to all
  databases and tables to a virtual group named `IAMAllowedPrincipal`. The
  `IAMAllowedPrincipal` refers to all IAM principals who have access to
  Data Catalog resources through IAM principal policies and AWS Glue resource policies. If these
  permissions exist on a database or a table, all principals are granted access to the
  database or table.

However, Lake Formation doesn't allow `IAMAllowedPrincipal` permissions on tables
under federated databases. When you create federated databases, make sure that you pass
the `CreateTableDefaultPermissions` parameter as an empty list.

For more information, see [Changing the default settings for your data
lake](change-settings.md "change-settings.md").

- Joining tables in queries – You can join Hive metastore tables with Data Catalog native tables to run queries.

###### Limitations

- Limitation on syncing metadata between the AWS Glue Data Catalog and the Hive
  metastore – After establishing the Hive metastore connection, you need to
  create a federated database to sync metadata in the Hive metastore with the AWS Glue Data Catalog.
  The tables under the federated database are synced at runtime when users run queries.
- Limitation on creating new tables under a federated database – You will not be able to create new tables under federated databases.
- Data permission limitation – Support for
  permissions on Hive metastore table views is not available.
