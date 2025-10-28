Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# PartiQL – an SQL-compatible query language for Amazon Redshift

Amazon Redshift supports PartiQL, an SQL-compatible query language, to select, insert, update,
and delete data in Amazon Redshift. Using PartiQL, you can easily interact with Amazon Redshift tables and run ad
hoc queries using the AWS Management Console, SQL Workbench/J, the AWS Command Line Interface, and Amazon Redshift Data APIs for PartiQL.

PartiQL operations provide the same availability, latency, and performance as the other Redshift data plane operations.

The following sections describe the Amazon Redshift implementation of PartiQL.

## What is PartiQL?

PartiQL provides SQL-compatible query access across multiple data stores containing
structured, semi-structured, and nested data. It is widely used within
Amazon and is now available as part of many AWS services, including Amazon Redshift.

For the PartiQL specification and a tutorial on the core query language, see the
[PartiQL overview](https://partiql.org/dql/overview.html "https://partiql.org/dql/overview.html").

For examples of using PartiQL queries in Amazon Redshift with semi-structured data, see
[Examples of using semi-structured data in Amazon Redshift](super-examples.md "super-examples.md").

###### Note

- Amazon Redshift supports a subset of the PartiQL query language.
- Amazon Redshift doesn't support the [Amazon Ion](https://amazon-ion.github.io/ion-docs/index.html "https://amazon-ion.github.io/ion-docs/index.html") data format or Amazon Ion literals.

## PartiQL in Amazon Redshift

To run PartiQL queries in Amazon Redshift, you can use the following methods:

- The AWS Management Console
- SQL Workbench/J
- The AWS CLI
- Amazon Redshift Data APIs for PartiQL
