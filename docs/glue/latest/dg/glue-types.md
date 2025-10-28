# AWS Glue type systems

AWS Glue uses multiple type systems to provide a versatile interface over data systems that store data in very
different ways. This document disambiguates AWS Glue type systems and data standards.

## AWS Glue Data Catalog Types

The Data Catalog is a registry of tables and fields stored in various data systems, a metastore. When AWS Glue
components, such as AWS Glue crawlers and AWS Glue with Spark jobs, write to the Data Catalog, they do so with an
internal type system for tracking the types of fields. These values are shown in the **Data
type** column of the table schema in the AWS Glue Console. This type system is based on Apache Hive's type
system. For more information about the Apache Hive type system, see [Types](https://cwiki.apache.org/confluence/display/hive/languagemanual+types "https://cwiki.apache.org/confluence/display/hive/languagemanual+types") in the Apache Hive
wiki. For more information about specific types and support, examples are provided in the AWS Glue Console, as
part of the Schema Builder.

### Validation, compatibility and other uses

The Data Catalog does not validate types written to type fields. When AWS Glue components read and write to
the Data Catalog, they will be compatible with each other. AWS Glue components also aim to preserve a high
degree of compatibility with the Hive types. However, AWS Glue components do not guarantee compatibility
with all Hive types. This allows for interoperability with tools like Athena DDL when
working with tables in the Data Catalog.

Since the Data Catalog does not validate types, other services may use the Data Catalog to track types using
systems that strictly conform to the Hive type system, or any other system.

## Types in AWS Glue with Spark scripts

When a AWS Glue with Spark script interprets or transforms a dataset, we provide `DynamicFrame`,
an in-memory representation of your dataset as it is used in your script. The goal of a
`DynamicFrame` is similar to that of the Spark `DataFrame`– it models your
dataset so that Spark can schedule and execute transforms on your data. We guarantee that the type
representation of `DynamicFrame` is intercompatible with `DataFrame` by providing the
`toDF` and `fromDF` methods.

If type information can be inferred or provided to a `DataFrame`, it can be inferred or
provided to a `DynamicFrame`, unless otherwise documented. When we provide optimized readers or
writers for specific data formats, if Spark can read or write your data, our provided readers and writers
will be able to, subject to documented limitations. For more information about readers and writers, see
[Data format options for inputs and outputs in
AWS Glue for Spark](aws-glue-programming-etl-format.md "aws-glue-programming-etl-format.md").

### The Choice Type

`DynamicFrames` provide a mechanism for modeling fields in a dataset whose value may have
inconsistent types on disk across rows. For instance, a field may hold a number stored as a string in
certain rows, and an integer in others. This mechanism is an in-memory type called `Choice`.
We provide transforms such as the `ResolveChoice` method, to resolve Choice columns to a
concrete type. AWS Glue ETL will not write the Choice type to the Data Catalog in the normal course of
operation; Choice types only exist in the context of DynamicFrame memory models of datasets. For an
example of Choice type usage, see [Code example:
Data preparation using ResolveChoice, Lambda, and ApplyMapping](aws-glue-programming-python-samples-medicaid.md "aws-glue-programming-python-samples-medicaid.md").

## AWS Glue Crawler Types

Crawlers aim to produce a consistent, usable schema for your dataset, then store it in Data Catalog for use in
other AWS Glue components and Athena. Crawlers deal with types as described in the previous section on the
Data Catalog, [AWS Glue Data Catalog Types](#glue-types-catalog "#glue-types-catalog"). To produce a usable type in "Choice" type scenarios, where a
column contains values of two or more types, Crawlers will create a `struct` type that
models the potential types.
