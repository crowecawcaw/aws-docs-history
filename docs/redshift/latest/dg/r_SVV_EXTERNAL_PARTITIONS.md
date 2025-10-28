Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# SVV_EXTERNAL_PARTITIONS

Use SVV_EXTERNAL_PARTITIONS to view details for partitions in external tables.

SVV_EXTERNAL_PARTITIONS is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and
views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data")..

## Table columns

| Column name       | Data type | Description                                                                                                         |
| ----------------- | --------- | ------------------------------------------------------------------------------------------------------------------- |
| schemaname        | text      | The name of the Amazon Redshift external schema for the external table with the specified partitions.               |
| tablename         | text      | The name of the external table.                                                                                     |
| values            | text      | Values for the partition.                                                                                           |
| location          | text      | The location of the partition. The column size is limited to 128 characters. Longer values are truncated.           |
| input_format      | text      | The input format.                                                                                                   |
| output_format     | text      | The output format.                                                                                                  |
| serialization_lib | text      | The serialization library.                                                                                          |
| serde_parameters  | text      | SerDe parameters.                                                                                                   |
| compressed        | integer   | A value that indicates whether the partition is compressed; `1` indicates compressed, `0` indicates not compressed. |
| parameters        | text      | Partition properties.                                                                                               |
