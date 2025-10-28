# Creating a catalog

Catalogs represent the highest or top-most level in the three-level metadata hierarchy of
the AWS Glue Data Catalog. You can use multiple methods to bring data into the Data Catalog and create multi-level catalogs.

For more information on creating catalogs from external data sources, see [Bringing your data into the AWS Glue Data Catalog](bring-your-data-overview.md "bring-your-data-overview.md").

To create a catalog using the Lake Formation console, you must be signed in as a data lake
administrator or a _catalog creator_. A catalog creator is a
principal who has been granted the Lake Formation `CREATE_CATALOG` permission. You can see a
list of catalog creators on the **Administrative roles and tasks** page of the
Lake Formation console. To view this list, you must have the `lakeformation:ListPermissions`
IAM permission and be signed in as a data lake administrator or as a catalog creator with the
grant option on the `CREATE_CATALOG` permission.
