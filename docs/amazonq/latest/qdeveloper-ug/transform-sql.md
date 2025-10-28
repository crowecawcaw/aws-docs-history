# Converting embedded SQL in Java applications with Amazon Q Developer

The Amazon Q Developer agent for code transformation in the IDE can help you convert embedded SQL to
complete Oracle to PostgreSQL database migration with AWS Database Migration Service (AWS DMS).

AWS DMS is a cloud service that makes it possible to migrate relational databases,
data warehouses, NoSQL databases, and other types of data stores. DMS Schema Conversion in
AWS DMS helps you convert database schemas and code objects that you can apply to your
target database. For more information, see [What is AWS Database Migration Service?](../../../dms/latest/userguide/Welcome.md "../../../dms/latest/userguide/Welcome.md") in the
_AWS Database Migration Service User Guide_.

When you use AWS DMS and DMS Schema Conversion to migrate a database, you might need to
convert the embedded SQL in your application to be compatible with your target database.
Rather than converting it manually, you can use Amazon Q in the IDE to automate the
conversion. Amazon Q uses metadata from a DMS Schema Conversion to convert embedded SQL in
your application to a version that is compatible with your target database.

Currently, Amazon Q can convert SQL in Java applications for Oracle databases migrating to
PostgreSQL. You will only see the option to transform SQL code in the IDE if your application contains
Oracle SQL statements. See the prerequisites for more information.

## Step 1: Prerequisites

Before you continue, make sure you’ve completed the steps in
[Set up Amazon Q in your IDE](q-in-IDE-setup.md "q-in-IDE-setup.md").

Before you begin a code transformation job for SQL conversion, make sure the following prerequisites are
met:

- You are migrating a Java application with embedded SQL from an Oracle database
  to a PostgreSQL database. Your application must contain Oracle SQL statements
  for it to be eligible for transformation.
- You have completed the process for converting your database schema using AWS
  DMS Schema Conversion. For more information, see
  [Migrating Oracle databases to Amazon RDS for PostgreSQL with DMS Schema
  Conversion](../../../dms/latest/sbs/schema-conversion-oracle-postgresql.md "../../../dms/latest/sbs/schema-conversion-oracle-postgresql.md") in the _Database Migration
  Guide_.
- After schema conversion is complete, you have downloaded the migration project
  file from the AWS DMS console.

## Step 2: Configure your application

To convert your embedded SQL code, your Java project must contain at least one
`.java` file.

If you are using a JetBrains IDE, you must set the SDK field in Project Structure
settings to the applicable JDK. For information on configuring Project Structure
settings, see
[Project structure settings](https://www.jetbrains.com/help/idea/project-settings-and-structure.html "https://www.jetbrains.com/help/idea/project-settings-and-structure.html") in the JetBrains documentation.

## Step 3: Convert embedded SQL

To convert the embedded SQL code in your Java application to a format that is
compatible with your PostgreSQL target database, complete the following steps:

1. In your IDE where Amazon Q is installed, open the Java codebase that contains the embedded SQL you need to convert.
2. Choose the Amazon Q icon to open the chat panel.
3. Ask Amazon Q to transform your application in the chat panel.
4. If your Java application is eligible for SQL conversion, Amazon Q will prompt
   you to choose which type of transformation you'd like to perform. Enter
   `SQL conversion`.
5. Amazon Q prompts you to upload the schema metadata file you retrieved from Amazon S3.
   In the chat, Amazon Q provides instructions for retrieving the file.
6. Amazon Q prompts you to provide the project that contains the embedded SQL as
   well as the database schema file. Choose the appropriate files from the dropdown
   menus in the chat panel.
7. Confirm the details Amazon Q retrieved from the database schema are accurate.
8. Amazon Q begins converting your SQL code. This might take a few minutes.
9. After Amazon Q converts the SQL code, it provides a diff with any updates it has
   made to your files. Review the changes in the diffs, and then accept the changes
   to update your code.

Amazon Q also provides a transformation summary with details about the changes it made. 10. After updating your code, return to the AWS DMS console to verify the new SQL
is compatible with the migrated database.
