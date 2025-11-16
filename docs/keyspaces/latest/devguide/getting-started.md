# Create, read, update, and delete

data (CRUD) using CQL in Amazon Keyspaces

In this step of the tutorial, you'll learn how to insert, read, update, and delete data
in an Amazon Keyspaces table using CQL data manipulation language (DML) statements. In Amazon Keyspaces, you can only create DML statements in CQL language.
In this tutorial, you'll practice running DML statements using the `cqlsh-expansion`
with [AWS CloudShell](using-aws-with-cloudshell.md "using-aws-with-cloudshell.md") in the AWS Management Console.

- **Inserting data** – This section covers inserting single and multiple records into a table
  using the `INSERT` statement. You'll learn how to upload data from a CSV file and verify successful inserts using `SELECT` queries.
- **Reading data** – Here, you'll explore different variations of the `SELECT` statement
  to retrieve data from a table. Topics include selecting all data, selecting specific columns, filtering rows based on conditions using the
  `WHERE` clause, and understanding simple and compound conditions.
- **Updating data** – In this section, you'll learn how to modify existing data in a table
  using the `UPDATE` statement. You'll practice updating single and multiple columns while understanding restrictions around
  updating primary key columns.
- **Deleting data** – The final section covers deleting data from a table using the
  `DELETE`statement. You'll learn how to delete specific cells, entire rows, and the implications of deleting data versus
  deleting the entire table or keyspace.
  Throughout the tutorial, you'll find examples, tips, and opportunities to practice writing your own CQL queries for various scenarios.

###### Topics

- [Inserting and loading data into
  an Amazon Keyspaces table](getting-started.dml.md "getting-started.dml.md")
- [Read data from a table using the CQL SELECT statement in Amazon Keyspaces](getting-started.dml.md "getting-started.dml.md")
- [Update data in an Amazon Keyspaces
  table using CQL](getting-started.dml.md "getting-started.dml.md")
- [Delete data from a table using the CQL DELETE statement](getting-started.dml.md "getting-started.dml.md")
