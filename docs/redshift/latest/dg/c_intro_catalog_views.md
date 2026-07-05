Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# System catalog tables

###### Topics

- [PG\_ATTRIBUTE\_INFO](r_PG_ATTRIBUTE_INFO.md "r_PG_ATTRIBUTE_INFO.md")
- [PG\_CLASS\_INFO](r_PG_CLASS_INFO.md "r_PG_CLASS_INFO.md")
- [PG\_DATABASE\_INFO](r_PG_DATABASE_INFO.md "r_PG_DATABASE_INFO.md")
- [PG\_DEFAULT\_ACL](r_PG_DEFAULT_ACL.md "r_PG_DEFAULT_ACL.md")
- [PG\_EXTERNAL\_SCHEMA](r_PG_EXTERNAL_SCHEMA.md "r_PG_EXTERNAL_SCHEMA.md")
- [PG\_LIBRARY](r_PG_LIBRARY.md "r_PG_LIBRARY.md")
- [PG\_PROC\_INFO](r_PG_PROC_INFO.md "r_PG_PROC_INFO.md")
- [PG\_STATISTIC\_INDICATOR](r_PG_STATISTIC_INDICATOR.md "r_PG_STATISTIC_INDICATOR.md")
- [PG\_TABLE\_DEF](r_PG_TABLE_DEF.md "r_PG_TABLE_DEF.md")
- [PG\_USER\_INFO](pg_user_info.md "pg_user_info.md")
- [Querying the catalog tables](c_join_PG.md "c_join_PG.md")
  The system catalogs store schema metadata, such as information about tables and columns.
  System catalog tables have a PG prefix.

The standard PostgreSQL catalog tables are accessible to Amazon Redshift users. For more
information about PostgreSQL system catalogs, see [PostgreSQL system tables](https://www.postgresql.org/docs/8.0/static/catalogs.html#CATALOGS-OVERVIEW "https://www.postgresql.org/docs/8.0/static/catalogs.html#CATALOGS-OVERVIEW")
