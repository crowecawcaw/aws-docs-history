Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Unsupported PostgreSQL

features

These PostgreSQL features are not supported in Amazon Redshift.

###### Important

Do not assume that the semantics of elements that Amazon Redshift and PostgreSQL have
in common are identical. Make sure to consult the _Amazon Redshift Developer
Guide_
[SQL commands](c_SQL_commands.md "c_SQL_commands.md") to understand the
often subtle differences.

- The query tool _psql_ is unsupported. The [Amazon Redshift RSQL](../mgmt/rsql-query-tool.md "../mgmt/rsql-query-tool.md") client is
  supported.
- Table partitioning (range and list partitioning)
- Tablespaces
- Constraints

      + Unique
      + Foreign key
      + Primary key
      + Check constraints
      + Exclusion constraints

  Unique, primary key, and foreign key constraints are permitted, but they are
  informational only. They are not enforced by the system, but they are used by
  the query planner.

- Inheritance
- PostgreSQL system columns

Amazon Redshift SQL does not implicitly define system columns. However, the
following PostgreSQL system column names cannot be used as names of
user-defined columns: `oid`, `tableoid`,
`xmin`, `cmin`, `xmax`, `cmax`,
and `ctid`. For more information, see [https://www.postgresql.org/docs/8.0/static/ddl-system-columns.html](https://www.postgresql.org/docs/8.0/static/ddl-system-columns.html "https://www.postgresql.org/docs/8.0/static/ddl-system-columns.html").

- Indexes
- NULLS clause in Window functions
- Collations

Amazon Redshift does not support locale-specific or user-defined collation
sequences. See [Collation sequences](c_collation_sequences.md "c_collation_sequences.md").

- Value expressions
  - Subscripted expressions
  - Array constructors
  - Row constructors

- Triggers
- Management of External Data (SQL/MED)
- Table functions
- VALUES list used as constant tables
- Sequences
- Full text search
- The RULE and TRIGGER permissions.

Amazon Redshift grants or revokes these permissions when you run GRANT ALL or
REVOKE ALL, but the presence or absence of the RULE and TRIGGER permissions
doesn’t affect the grantee’s access permissions in any way.
