

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# PartiQL – an SQL-compatible query language for Amazon Redshift
<a name="super-partiql"></a>

Amazon Redshift supports PartiQL, an SQL-compatible query language, to select, insert, update, and delete data in Amazon Redshift. Using PartiQL, you can easily interact with Amazon Redshift tables and run ad hoc queries using the AWS Management Console, SQL Workbench/J, the AWS Command Line Interface, and Amazon Redshift Data APIs for PartiQL. 

PartiQL operations provide the same availability, latency, and performance as the other Redshift data plane operations.

The following sections describe the Amazon Redshift implementation of PartiQL.

## What is PartiQL?
<a name="super-partiql-overview"></a>

PartiQL provides SQL-compatible query access across multiple data stores containing structured, semi-structured, and nested data. It is widely used within Amazon and is now available as part of many AWS services, including Amazon Redshift.

For the PartiQL specification and a tutorial on the core query language, see the [PartiQL overview](https://partiql.org/dql/overview.html).

For examples of using PartiQL queries in Amazon Redshift with semi-structured data, see [Examples of using semi-structured data in Amazon Redshift](super-examples.md).

**Note**  
Amazon Redshift supports a subset of the PartiQL query language.
Amazon Redshift doesn't support the [ Amazon Ion](https://amazon-ion.github.io/ion-docs/index.html) data format or Amazon Ion literals.

## PartiQL in Amazon Redshift
<a name="super-partiql-rs"></a>

To run PartiQL queries in Amazon Redshift, you can use the following methods:
+  The AWS Management Console 
+  SQL Workbench/J 
+  The AWS CLI 
+  Amazon Redshift Data APIs for PartiQL 