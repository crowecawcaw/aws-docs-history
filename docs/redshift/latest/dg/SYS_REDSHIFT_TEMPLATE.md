Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# SYS_REDSHIFT_TEMPLATE

Use SYS_REDSHIFT_TEMPLATE to view details of Redshift TEMPLATES.

This view contains the TEMPLATES that have been created.

SYS_REDSHIFT_TEMPLATE is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and
views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data").

## Table columns

| Column name         | Data type      | Description                                                                                    |
| ------------------- | -------------- | ---------------------------------------------------------------------------------------------- |
| database_name       | character(128) | The Redshift Database in which the template is created.                                        |
| schema_name         | character(128) | The Redshift Schema in which the template is created.                                          |
| template_name       | character(128) | The name of the template.                                                                      |
| template_type       | integer        | An integer indicating the Redshift command type associated with the template. 1 = COPY command |
| create_time         | timestamp      | Timestamp when the template was created.                                                       |
| last_modified_time  | timestamp      | Timestamp when the template was last modified.                                                 |
| owner_id            | integer        | User ID of the user who owns the template.                                                     |
| last_modified_by    | integer        | User ID of the user who last modified the template.                                            |
| template_parameters | text           | A JSON string containing the template parameters and their values.                             |

## Sample queries

The following query returns all templates visible to the current user:

```
SELECT * FROM SYS_REDSHIFT_TEMPLATE;
```

Sample output.

```
`database_name | schema_name | template_name | template_type | create_time | last_modified_time | owner_id | last_modified_by | template_parameters
---------------+-------------+--------------------+---------------+----------------------------+----------------------------+----------+------------------+---------------------
 dev | s1 | shapefile_template | 1 | 2025-12-17 22:42:02.079758 | 2025-12-17 22:42:02.079758 | 101 | 101 | {
 "SIMPLIFY_AUTO": 0.000001,
 "SHAPEFILE": 1,
 "COMPRESSION_UPDATE": 0
}
 dev | s2 | orc_template | 1 | 2025-12-17 22:42:23.582815 | 2025-12-17 22:42:23.582815 | 101 | 101 | {
 "ORC": "serializetojson_default"
}
 dev | s1 | csv_template | 1 | 2025-12-17 22:43:01.822361 | 2025-12-17 22:43:01.822361 | 101 | 101 | {
 "ENCRYPTED": 1,
 "CSV": 1,
 "ENCODING": 1,
 "DELIMITER": ","
}
(3 rows)`
```
