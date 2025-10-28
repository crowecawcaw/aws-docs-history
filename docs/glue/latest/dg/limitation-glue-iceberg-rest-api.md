# Considerations and limitations when using AWS Glue Iceberg REST Catalog APIs

Following are the considerations and limitations when using the Apache Iceberg REST Catalog Data Definition Language (DDL) operation behavior.

###### Considerations

- **`RenameTable` API behavior** – The
  `RenameTable` operation is supported in tables in Amazon Redshift but not in Amazon S3.
- **DDL operations for namespaces and tables in Amazon Redshift** – Create,
  Update, Delete operations for namespaces and tables in Amazon Redshift are asynchronous operations
  because they are dependent on when Amazon Redshift managed workgroup is available and whether a
  conflicting DDL and DML transaction is in progress and operation has to wait for lock and
  then attempt to commit changes.

###### Limitations

- View APIs in the Apache Iceberg REST specification are not supported in AWS Glue Iceberg REST Catalog.
