# Considerations and limitations for Athena views

Athena views have the following considerations and limitations.

## Considerations

The following considerations apply to creating and using views in Athena:

- In Athena, you can preview and work with views created in the Athena
  Console, in the AWS Glue Data Catalog or with Presto running on the Amazon EMR cluster
  connected to the same catalog.
- If you have created Athena views in the Data Catalog, then Data Catalog treats views
  as tables. You can use table level fine-grained access control in Data Catalog to
  [restrict
  access](fine-grained-access-to-glue-resources.md "fine-grained-access-to-glue-resources.md") to these views.
- Athena prevents you from running recursive views and displays an error
  message in such cases. A recursive view is a view query that references
  itself.
- Athena displays an error message when it detects stale views. A stale view
  is reported when one of the following occurs:
  - The view references tables or databases that do not exist.
  - A schema or metadata change is made in a referenced table.
  - A referenced table is dropped and recreated with a different
    schema or configuration.

- You can create and run nested views as long as the query behind the nested
  view is valid and the tables and databases exist.

## Limitations

- Athena view names cannot contain special characters, other than underscore
  `(_)`. For more information, see [Name databases, tables, and columns](tables-databases-columns-names.md "tables-databases-columns-names.md").
- Avoid using reserved keywords for naming views. If you use reserved
  keywords, use double quotes to enclose reserved keywords in your queries on
  views. See [Escape reserved keywords in queries](reserved-words.md "reserved-words.md").
- You cannot use views created in Athena with external Hive metastores or
  UDFs. For information about working with views created externally in Hive,
  see [Work with Hive views](hive-views.md "hive-views.md").
- You cannot use views with geospatial functions.
- You cannot use views to manage access control on data in Amazon S3. To query a
  view, you need permissions to access the data stored in Amazon S3. For more
  information, see [Control access to Amazon S3 from Athena](s3-permissions.md "s3-permissions.md").
- While querying views across accounts is supported in Athena engine version 3, you cannot
  create a view that includes a cross-account AWS Glue Data Catalog. For information
  about cross-account data catalog access, see [Configure cross-account access to AWS Glue data catalogs](security-iam-cross-account-glue-catalog-access.md "security-iam-cross-account-glue-catalog-access.md").
- The Hive or Iceberg hidden metadata columns `$bucket`,
  `$file_modified_time`, `$file_size`, and
  `$partition` are not supported for views in Athena. For
  information about using the `$path` metadata column in Athena, see
  [Getting the file locations for source data in Amazon S3](select.md#select-path "select.md#select-path").
