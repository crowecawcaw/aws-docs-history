Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# System catalog tables

###### Topics

- [PG_ATTRIBUTE_INFO](r_PG_ATTRIBUTE_INFO.md "r_PG_ATTRIBUTE_INFO.md")
- [PG_CLASS_INFO](r_PG_CLASS_INFO.md "r_PG_CLASS_INFO.md")
- [PG_DATABASE_INFO](r_PG_DATABASE_INFO.md "r_PG_DATABASE_INFO.md")
- [PG_DEFAULT_ACL](r_PG_DEFAULT_ACL.md "r_PG_DEFAULT_ACL.md")
- [PG_EXTERNAL_SCHEMA](r_PG_EXTERNAL_SCHEMA.md "r_PG_EXTERNAL_SCHEMA.md")
- [PG_LIBRARY](r_PG_LIBRARY.md "r_PG_LIBRARY.md")
- [PG_PROC_INFO](r_PG_PROC_INFO.md "r_PG_PROC_INFO.md")
- [PG_STATISTIC_INDICATOR](r_PG_STATISTIC_INDICATOR.md "r_PG_STATISTIC_INDICATOR.md")
- [PG_TABLE_DEF](r_PG_TABLE_DEF.md "r_PG_TABLE_DEF.md")
- [PG_USER_INFO](pg_user_info.md "pg_user_info.md")
- [Querying the catalog tables](c_join_PG.md "c_join_PG.md")
  The system catalogs store schema metadata, such as information about tables and columns.
  System catalog tables have a PG prefix.

The standard PostgreSQL catalog tables are accessible to Amazon Redshift users. For more
information about PostgreSQL system catalogs, see [PostgreSQL system tables](https://www.postgresql.org/docs/8.0/static/catalogs.html#CATALOGS-OVERVIEW "https://www.postgresql.org/docs/8.0/static/catalogs.html#CATALOGS-OVERVIEW")
