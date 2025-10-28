# What is Cassandra Query Language (CQL)?

_Cassandra Query Language_ (CQL) is the primary language for
communicating with Apache Cassandra. Amazon Keyspaces (for Apache Cassandra) is compatible with the CQL 3.x API
(backward-compatible with version 2.x).

In CQL, data is stored in tables, columns, and rows. In this sense CQL is similar to Structured Query Language (SQL). These are the key
concepts in CQL.

- **CQL elements** – The fundamental elements of CQL are identifiers, constants, terms, and data types.
- **Data Definition Language (DDL)** – DDL statements are used to manage data structures like
  keyspaces and tables, which are AWS resources in Amazon Keyspaces. DDL statements are control plane operations in AWS.
- **Data Manipulation Language (DML)** – DML statements are used to manage data within tables.
  DML statements are used for selecting, inserting, updating, and deleting data. These are data plane operations in AWS.
- **Built-in functions** – Amazon Keyspaces supports a variety of built-in scalar functions that you can use
  in CQL statements.
  For more information about CQL, see [CQL language reference for Amazon Keyspaces (for Apache Cassandra)](cql.md "cql.md"). For
  functional differences with Apache Cassandra, see [Functional differences: Amazon Keyspaces vs. Apache Cassandra](functional-differences.md "functional-differences.md").

To run CQL queries, you can do one of the following:

- Use the CQL editor in the AWS Management Console.
- Use AWS CloudShell and the [cqlsh-expansion](programmatic.md#using_cqlsh "programmatic.md#using_cqlsh").
- Use a `cqlsh` client.
- Use an Apache 2.0 licensed Cassandra client driver.
  In addition to CQL, you can perform Data Definition Language (DDL) operations in Amazon Keyspaces using the AWS SDKs and the AWS Command Line Interface.

For more information about using these methods to access Amazon Keyspaces, see [Accessing Amazon Keyspaces (for Apache Cassandra)](accessing.md "accessing.md").
