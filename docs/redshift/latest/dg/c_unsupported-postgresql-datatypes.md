Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Unsupported PostgreSQL data

types

Generally, if a query attempts to use an unsupported data type, including explicit
or implicit casts, it will return an error. However, some queries that use
unsupported data types will run on the leader node but not on the compute nodes. See
[SQL functions supported on the leader
node](c_sql-functions-leader-node.md "c_sql-functions-leader-node.md").

For a list of the supported data types, see [Data types](c_Supported_data_types.md "c_Supported_data_types.md").

These PostgreSQL data types are not supported in Amazon Redshift.

- Arrays
- BIT, BIT VARYING
- BYTEA
- Composite Types
- Enumerated Types
- Geometric Types (Amazon Redshift implementation of geometric types differs from
  PostgreSQL)
- HSTORE
- JSON
- Network Address Types
- Numeric Types
  - SERIAL, BIGSERIAL, SMALLSERIAL
  - MONEY

- Object Identifier Types
- Pseudo-Types
- Range Types
- Special Character Types

      + "char" – A single-byte internal type (where the data type named
       char is enclosed in quotation marks).
      + name – An internal type for object names.

  For more information about these types, see [Special
  Character Types](https://www.postgresql.org/docs/8.0/datatype-character.html "https://www.postgresql.org/docs/8.0/datatype-character.html") in the PostgreSQL documentation.

- Text Search Types
- TXID_SNAPSHOT
- UUID
- XML
