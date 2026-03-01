# Use Athena to query data registered with AWS Lake Formation

[AWS Lake Formation](../../../lake-formation/latest/dg/what-is-lake-formation.md "../../../lake-formation/latest/dg/what-is-lake-formation.md") allows you to define
and enforce database, table, and column-level access policies when using Athena queries to
read data stored in Amazon S3 or accessed through federated data sources. Lake Formation provides an
authorization and governance layer on data stored in Amazon S3 or federated data catalogs. You
can use a hierarchy of permissions in Lake Formation to grant or revoke permissions to read data
catalog objects such as databases, tables, and columns. Lake Formation simplifies the management of
permissions and allows you to implement fine-grained access control (FGAC) for your
data.

You can use Athena to query both data that is registered with Lake Formation and data that is not
registered with Lake Formation.

Lake Formation permissions apply when using Athena to query source data from Amazon S3 locations or data
catalogs that are registered with Lake Formation. Lake Formation permissions also apply when you create
databases and tables that point to registered Amazon S3 data locations or data catalogs.

Lake Formation permissions do not apply when writing objects, nor do they apply when querying data
or metadata that are not registered with Lake Formation. For source data and metadata that are not
registered with Lake Formation, access is determined by IAM permissions policies and AWS Glue actions.
Athena query results locations in Amazon S3 cannot be registered with Lake Formation, and IAM permissions
policies for Amazon S3 control access. In addition, Lake Formation permissions do not apply to Athena query
history. You can use Athena workgroups to control access to query history.

For more information about Lake Formation, see [Lake Formation FAQs](https://aws.amazon.com/lake-formation/faqs/ "https://aws.amazon.com/lake-formation/faqs/") and the [AWS Lake Formation
Developer Guide](../../../lake-formation/latest/dg/what-is-lake-formation.md "../../../lake-formation/latest/dg/what-is-lake-formation.md").

## Apply Lake Formation permissions to existing databases and tables

If you are new to Athena and you use Lake Formation to configure access to query data, you do not
need to configure IAM policies so that users can read data and create metadata. You
can use Lake Formation to administer permissions.

Registering data with Lake Formation and updating IAM permissions policies is not a
requirement. If data is not registered with Lake Formation, Athena users who have appropriate
permissions can continue to query data not registered with Lake Formation.

If you have existing Athena users who query Amazon S3 data not registered with Lake Formation, you can
update IAM permissions for Amazon S3—and the AWS Glue Data Catalog, if applicable—so
that you can use Lake Formation permissions to manage user access centrally. For permission to
read Amazon S3 data locations, you can update resource-based and identity-based policies to
modify Amazon S3 permissions. For access to metadata, if you configured resource-level
policies for fine-grained access control with AWS Glue, you can use Lake Formation permissions to
manage access instead.

For more information, see [Configure access to databases and tables in the AWS Glue Data Catalog](fine-grained-access-to-glue-resources.md "fine-grained-access-to-glue-resources.md") and [Upgrading AWS Glue data permissions
to the AWS Lake Formation model](../../../lake-formation/latest/dg/upgrade-glue-lake-formation.md "../../../lake-formation/latest/dg/upgrade-glue-lake-formation.md") in the _AWS Lake Formation Developer
Guide_.

###### Topics

- [How data access works](lf-athena-access.md "lf-athena-access.md")
- [Considerations and limitations](lf-athena-limitations.md "lf-athena-limitations.md")
- [Cross-account access](lf-athena-limitations-cross-account.md "lf-athena-limitations-cross-account.md")
- [Manage user permissions](lf-athena-user-permissions.md "lf-athena-user-permissions.md")
- [Use Lake Formation and JDBC or ODBC for federated access](security-athena-lake-formation-jdbc.md "security-athena-lake-formation-jdbc.md")
