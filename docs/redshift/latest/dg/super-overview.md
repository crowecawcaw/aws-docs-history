Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Semi-structured data in Amazon Redshift

By using _semi-structured data support_ in Amazon Redshift, you can
ingest and store semi-structured data in your Amazon Redshift data warehouses. Using the SUPER data type
and PartiQL language, Amazon Redshift expands data warehouse capability to integrate with both SQL
and NoSQL data sources. This way, Amazon Redshift enables efficient analytics on relational and
semi-structured stored data such as JSON. For information on Amazon Redshift integration with PartiQL, see
[PartiQL – an SQL-compatible query language for Amazon Redshift](super-partiql.md "super-partiql.md").

Amazon Redshift offers two forms of semi-structured data support: the SUPER data type and
Amazon Redshift Spectrum.

You can query semi-structured data by ingesting it into Amazon Redshift and storing it in the
SUPER data type or use Amazon Redshift Spectrum to query the data stored in Amazon S3.

## Best practices for working with semi-structured data

Consider the following best practices when working with semi-structured data.

- We recommend that you set the `enable_case_sensitive_super_attribute` and
  `enable_case_sensitive_identifier`configuration options to
  true when working with SUPER data. For more information, see
  [enable_case_sensitive_super_attribute](r_enable_case_sensitive_super_attribute.md "r_enable_case_sensitive_super_attribute.md")
  and [enable_case_sensitive_identifier](r_enable_case_sensitive_identifier.md "r_enable_case_sensitive_identifier.md").
- Use the COPY command to load data from Amazon S3 buckets into Amazon Redshift SUPER columns.
- Use PartiQL dynamic typing and lax semantics to run ad hoc queries on SUPER data values without having to impose a schema before querying.
  For information on dynamic typing, see [Dynamic typing](query-super.md#dynamic-typing-lax-processing "query-super.md#dynamic-typing-lax-processing").
  For information on lax semantics, see [Lax semantics](query-super.md#lax-semantics "query-super.md#lax-semantics").
- Shred schemaless and semi-structured data into materialized views using PartiQL if
  you plan to query the data frequently. When you perform analytics on the shredded data,
  the columnar organization of Amazon Redshift materialized views provides better performance.
  Furthermore, users and business intelligence (BI) tools that require a conventional
  schema for ingested data can use views (either materialized or virtual) as the
  conventional schema presentation of the data.

After your PartiQL materialized views have extracted the data found in JSON
or SUPER into conventional columnar materialized views, you can query the
materialized views. For information on materialized views, see
[Materialized views in Amazon Redshift](materialized-view-overview.md "materialized-view-overview.md").
For more information on how the SUPER data type works with materialized views,
see [SUPER data type and materialized views](r_SUPER_MV.md "r_SUPER_MV.md").

## Concepts for SUPER data type use

Following, you can find some Amazon Redshift SUPER data type concepts.

**Understand what the SUPER data type is in Amazon Redshift**
– The _SUPER_ data type is an Amazon Redshift data type that enables the
storage of schemaless arrays and structures that contain Amazon Redshift scalars and possibly
nested arrays and structures. The SUPER data type can natively store different formats of
semi-structured data, such as JSON or data originating from document-oriented sources. You
can add a new SUPER column to store semi-structured data and write queries that access the
SUPER column, along with the usual scalar columns. For more information about the SUPER
data type, see [SUPER type](r_SUPER_type.md "r_SUPER_type.md").

**Ingest schemaless JSON into SUPER** – With the
flexible semi-structured SUPER data type, Amazon Redshift can receive and ingest schemaless JSON
into columns with the SUPER data type. For example, you can ingest the JSON value `[10.5, “first”]`
into a SUPER data type column by using the COPY command. The column would hold a
SUPER value of `[10.5, ‘first’]`. You can also ingest JSON using
[JSON_PARSE function](JSON_PARSE.md "JSON_PARSE.md"). Both COPY and
`json_parse` ingest JSON using strict parsing semantics by default. You can also construct
SUPER values including arrays and structures, using the database data themselves.

The SUPER column requires no schema modifications while ingesting the flexible
structures of schemaless JSON. For example, while analyzing a click-stream, you
initially store in the SUPER column “click” structures with attributes “IP” and “time”.
You can add an attribute “customer id” without changing your schema in order to ingest
such changes.

The native format used for the SUPER data type is a binary format that requires
less space than the JSON value in its textual form. This enables faster ingestion and
runtime processing of SUPER values at query.

**Query SUPER data with PartiQL** –
PartiQL is a
backward compatible extension of SQL-92 that many AWS services currently use. With the
use of PartiQL, familiar SQL constructs seamlessly combine access to both the classic,
tabular SQL data and the semi-structured data of SUPER. You can perform object and array
navigation and unnest arrays. PartiQL extends the standard SQL language to declaratively
express and process nested and multivalued data.

PartiQL is an extension of SQL where the nested and schemaless data of SUPER columns
are first-class citizens. PartiQL doesn't require all query expressions to be
type-checked during query compilation time. This approach enables query expressions that
contain the SUPER data type to be dynamically typed during query execution when the actual
types of the data inside the SUPER columns are accessed. Also, PartiQL operates in a lax
mode where type inconsistencies don't cause failures but return null. The combination of schemaless
and lax query processing makes PartiQL ideal for extract, load, transform (ELT) applications
where your SQL query evaluates the JSON data that are ingested in the SUPER columns.

For more information on PartiQL for Amazon Redshift,
see [PartiQL – an SQL-compatible query language for Amazon Redshift](super-partiql.md "super-partiql.md"). For information
on dynamic typing, see [Dynamic typing](query-super.md#dynamic-typing-lax-processing "query-super.md#dynamic-typing-lax-processing").
For information on lax query processing, see [Lax semantics](query-super.md#lax-semantics "query-super.md#lax-semantics").

**Integrate with Redshift Spectrum** – Amazon Redshift supports
multiple aspects of PartiQL when running Redshift Spectrum queries over JSON, Parquet, and other
formats that have nested data. Redshift Spectrum only supports nested data that has schemas. For
example, with Redshift Spectrum you can declare that your JSON data has the attribute
`nested_schemaful_example` in the schema
`ARRAY<STRUCT<a:INTEGER, b:DECIMAL(5,2)>>`. The schema of
this attribute determines that the data always contains an array, which contains a
structure with integer _a_ and decimal _b_. If the
data changes to include more attributes, the type also changes. In contrast, the SUPER data
type requires no schema. You can store arrays with structure elements that have different
attributes or types. Also, values can be stored outside arrays.

## Considerations for using SUPER type data

When working with SUPER data, consider the following:

- Use JDBC driver version 2.x, ODBC driver version 2.x, or
  Amazon Redshift Python driver version 2.0.872 or later. The ODBC driver version 1.x isn’t supported.

For information about JDBC drivers, see
[Configuring a connection for JDBC driver version 2.x for Amazon Redshift](../mgmt/jdbc20-install.md "../mgmt/jdbc20-install.md")
in the _Amazon Redshift Management Guide_.

For information about ODBC drivers, see
[Configuring a connection for ODBC driver version 2.x for Amazon Redshift](../mgmt/odbc20-install.md "../mgmt/odbc20-install.md")
in the _Amazon Redshift Management Guide_..

For information about Python drivers, see
[Amazon Redshift Python connector](../mgmt/python-redshift-driver.md "../mgmt/python-redshift-driver.md")
in the _Amazon Redshift Management Guide_..

For more information about SUPER configurations, see [SUPER configurations](super-configurations.md "super-configurations.md").
