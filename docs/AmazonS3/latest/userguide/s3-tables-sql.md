# Granting access with SQL semantics

You can grant permissions to tables by using SQL semantics in table and table bucket policies. Examples of SQL semantics you can use are `CREATE`, `INSERT`, `DELETE`, `UPDATE`, and `ALTER`. The following
table provides a list of API actions associated with SQL semantics that you can use to grant permissions to your users.

S3 Tables partially supports permissions using SQL semantics. For example, the
`CreateTable` API only creates an empty table in the table bucket. You
need additional permissions such as, `UpdateTableMetadata`,
`PutTableData`, and `GetTableMetadataLocation` to be able to
set the table schema. These additional permissions also mean that you are also granting
the user access to insert rows in the table. If you wish to govern access purely based
on SQL semantics, then we recommend using [AWS Lake Formation](../../../lake-formation/latest/dg/what-is-lake-formation.md "../../../lake-formation/latest/dg/what-is-lake-formation.md") or any
third-party solution that is integrated with S3 Tables.

| Table-level activity | IAM actions                                                                                                                            |
| -------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| `SELECT`             | `s3tables:GetTableData`,<br>`s3tables:GetTableMetadataLocation`                                                                        |
| `CREATE`             | `s3tables:CreateTable`,<br>`s3tables:UpdateTableMetadataLocation`,<br>`s3tables:PutTableData`,<br>`s3tables:GetTableMetadataLocation`, |
| `INSERT`             | `s3tables:UpdateTableMetadataLocation`,<br>`s3tables:PutTableData`,<br>`s3tables:GetTableMetadataLocation`                             |
| `UPDATE`             | `s3tables:UpdateTableMetadataLocation`,<br>`s3tables:PutTableData`,<br>`s3tables:GetTableMetadataLocation`                             |
| `ALTER`,`RENAME`     | `s3tables:UpdateTableMetadataLocation`,<br>`s3tables:PutTableData`,<br>`s3tables:GetTableMetadataLocation`,<br>`s3tables:RenameTable`  |
| `DELETE`,`DROP`      | `s3tables:DeleteTable`,<br>`s3tables:UpdateTableMetadataLocation`,<br>`s3tables:PutTableData`,<br>`s3tables:GetTableMetadataLocation`  |

###### Note

The `s3tables:DeleteTable` permission is required to delete a table from a table bucket. This permission allows you to permanently remove a table and all its associated data and metadata. Use this permission carefully as the delete operation cannot be undone.
