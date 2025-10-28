# Data Catalog views considerations and limitations

The following considerations and limitations apply to Data Catalog views.

- You cannot create a Data Catalog view from the Lake Formation console. You can create views using the AWS CLI or SDK.
- You can create Data Catalog views from 10 tables. It is a hard limit. Underlying
  reference tables for a view can belong to the same database or different databases within
  the same AWS account.
- For additional considerations and limitations specific to creating Data Catalog
  views using Redshift, see the [Data Catalog views considerations and limitations](../../../redshift/latest/dg/data-catalog-views-overview.md#data-catalog-views-considerations "../../../redshift/latest/dg/data-catalog-views-overview.md#data-catalog-views-considerations") section in the Amazon Redshift Database Developer Guide. For
  Athena, see the [Data Catalog views
  considerations and limitations](../../../athena/latest/ug/views-glue.md#views-glue-limitations "../../../athena/latest/ug/views-glue.md#views-glue-limitations") section in the Amazon Athena User Guide.
- You can create Data Catalog views on tables registered with Lake Formation in both hybrid access mode and Lake Formation mode.

When using Data Catalog views with Lake Formation hybrid access mode, it is recommended to ensure
that the view consuming principals are opted in to Lake Formation permissions for the base tables
referenced in the view without granting access. This ensures that the base tables will not
be revealed to consumers through AWS Glue IAM permissions.

- There are no restrictions on the cross-account sharing version to share views.
- Views get versioned just like Data Catalog tables, when you use the `ALTER VIEW` statement for an already created view dialect. You cannot roll back to a previous view because the view version changes with the underlying data changes. You can delete a view version and it will default to the next available latest version. When you change the view version, make sure your data is in sync with the selected view version schema.
- No new Data Catalog APIs are introduced. The existing `CreateTable`, `UpdateTable`, `DeleteTable` and `GetTable` APIs are updated.
- Amazon Redshift always creates views with varchar columns from tables with strings. You must cast string
  columns to varchar with an explicit length when adding dialects from other engines.
- Granting data lake permissions to `All tables` within a database will result
  in the grantee having permissions on all tables and views within the database.
- You can't create views:
  - That reference other views.
  - When the reference table is a resource link.
  - When the reference table is in another account.
  - From external Hive metastores.
