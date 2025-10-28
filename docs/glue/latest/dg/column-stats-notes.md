# Considerations and limitations

The following considerations and limitations apply to generating column statistics.

###### Considerations

- Using sampling to generate statistics reduces run time, but can generate inaccurate
  statistics.
- Data Catalog doesn't store different versions of the statistics.
- You can only run one statistics generation task at a time per table.
- If a table is encrypted using customer AWS KMS key registered with Data Catalog, AWS Glue uses the
  same key to encrypt statistics.

###### Column statistics task supports generating statistics:

- When the IAM role has full table permissions (IAM or Lake Formation).
- When the IAM role has permissions on the table using Lake Formation hybrid access mode.

###### Column statistics task doesn’t support generating statistics for:

- Tables with Lake Formation cell-based access control
- Transactional data lakes - Linux foundation Delta Lake, Apache Hudi
- Tables in federated databases - Hive metastore, Amazon Redshift datashares
- Nested columns, arrays, and struct data types.
- Table that is shared with you from another account
