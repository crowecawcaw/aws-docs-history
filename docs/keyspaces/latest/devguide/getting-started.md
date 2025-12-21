# Getting started with Amazon Keyspaces (for Apache Cassandra)

If you're new to Apache Cassandra and Amazon Keyspaces, this tutorial guides you through installing the necessary programs and tools to use
Amazon Keyspaces successfully. You'll learn how to create a keyspace and table using Cassandra Query Language (CQL), the AWS Management Console, or the AWS Command Line Interface (AWS CLI).
You then use Cassandra Query Language (CQL) to perform create, read, update, and delete (CRUD) operations on
data in your Amazon Keyspaces table.

This tutorial covers the following steps.

- **Prerequisites** – Before starting the tutorial, follow
  the AWS setup instructions to sign up for AWS and create an IAM user with access to
  Amazon Keyspaces. Then you set up the `cqhsh-expansion` and AWS CloudShell. Alternatively you can use the AWS CLI to create resources in Amazon Keyspaces.
- **Step 1: Create a keyspace and table** – In this section, you'll create a keyspace named
  "catalog" and a table named "book_awards" within it. You'll specify the table's columns, data types, partition key, and clustering
  column using the AWS Management Console, CQL, or the AWS CLI.
- **Step 2: Perform CRUD operations** – Here, you'll use the `cqlsh-expansion`
  in CloudShell to insert, read, update, and delete data in the "book_awards" table. You'll learn how to use various CQL statements like SELECT, INSERT, UPDATE,
  and DELETE, and practice filtering and modifying data.
- **Step 3: Clean up resources** – To avoid incurring charges for unused resources, this section
  guides you through deleting the "book_awards" table and "catalog" keyspace using the console, CQL, or the AWS CLI.
  For tutorials to connect programmatically to Amazon Keyspaces using different Apache Cassandra
  client drivers, see [Using a Cassandra client driver to access
  Amazon Keyspaces programmatically](programmatic.md "programmatic.md"). For code examples using different AWS SDKs, see [Code examples for Amazon Keyspaces using AWS SDKs](service_code_examples.md "service_code_examples.md").

###### Topics

- [Tutorial prerequisites and considerations](getting-started.md "getting-started.md")
- [Create a keyspace in Amazon Keyspaces](getting-started.md "getting-started.md")
- [Check keyspace creation status in Amazon Keyspaces](keyspaces-create.md "keyspaces-create.md")
- [Create a table in Amazon Keyspaces](getting-started.md "getting-started.md")
- [Check table creation status in Amazon Keyspaces](tables-create.md "tables-create.md")
- [Create, read, update, and delete
  data (CRUD) using CQL in Amazon Keyspaces](getting-started.md "getting-started.md")
- [Delete a table in Amazon Keyspaces](getting-started.clean-up.md "getting-started.clean-up.md")
- [Delete a keyspace in Amazon Keyspaces](getting-started.clean-up.md "getting-started.clean-up.md")
