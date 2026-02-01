Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# SUPER type

Use the SUPER data type to store semi-structured data or documents as values.
Although Amazon Redshift is capable of storing such values using VARCHAR, we recommend
that you use the SUPER data type instead.

Semi-structured data doesn't conform to the rigid and tabular structure of
the relational data model used in SQL databases. It contains tags that reference
distinct entities within the data. They can contain complex values such as arrays,
nested structures, and other complex structures that are associated with
serialization formats, such as JSON. The SUPER data type is a set of schemaless
array and structure values that encompass all other scalar types of
Amazon Redshift.

The SUPER data type supports up to 16 MB of data for an individual SUPER object. For more information on the SUPER data type,
including examples of implementing it in a table, see [Semi-structured data in Amazon Redshift](super-overview.md "super-overview.md").

Amazon Redshift provides built-in support to ingest the following semi-structured data formats using the COPY command:

- JSON
- ARRAY
- TEXT
- CSV
  SUPER objects larger than 1MB can only be ingested from the following file formats:

- Parquet
- JSON
- TEXT
- CSV
  The SUPER data type has the following properties:

- An Amazon Redshift scalar value:
  - A null
  - A boolean
  - A number, such as smallint, integer, bigint, decimal, or floating
    point (such as float4 or float8)
  - A string value, such as varchar or char

- A complex value:

      + An array of values, including scalar or complex
      + A structure, also known as tuple or object, that is a map of
       attribute names and values (scalar or complex)

  Any of the two types of complex values contain their own scalars or complex
  values without having any restrictions for regularity.

The default compression encoding for the SUPER data type is ZSTD. For more information on
compression encoding, see [Compression encodings](c_Compression_encodings.md "c_Compression_encodings.md").

The SUPER data type supports the persistence of semi-structured data in a
schemaless form. Although hierarchical data model can change, the old versions of
data can coexist in the same SUPER column.

Amazon Redshift uses PartiQL to enable navigation into arrays and structures. Amazon Redshift
also uses the PartiQL syntax to iterate over SUPER arrays. For more information, see
[PartiQL – an SQL-compatible query language for Amazon Redshift](super-partiql.md "super-partiql.md").

Amazon Redshift uses dynamic typing to process schemaless SUPER data without needing to declare
the data types before you use them in your query. For more information, see
[Dynamic typing](query-super.md#dynamic-typing-lax-processing "query-super.md#dynamic-typing-lax-processing").

You can apply dynamic data masking policies to scalar values on the paths of SUPER
type columns. For more information about dynamic data masking, see [Dynamic data masking](t_ddm.md "t_ddm.md"). For information about using dynamic
data masking with the SUPER data type, see [Using dynamic data masking with SUPER data type paths](t_ddm-super.md "t_ddm-super.md").

We recommend that you set the `r_enable_case_sensitive_super_attribute` configuration option to
true when working with SUPER data. For more information, see
[enable_case_sensitive_super_attribute](r_enable_case_sensitive_super_attribute.md "r_enable_case_sensitive_super_attribute.md").
