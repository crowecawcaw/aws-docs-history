# Create a database

After you have set up a query results location, creating a database in the Athena
console query editor is straightforward.

###### To create a database using the Athena query editor

1. Open the Athena console at
   [https://console.aws.amazon.com/athena/](https://console.aws.amazon.com/athena/home "https://console.aws.amazon.com/athena/home").
2. On the **Editor** tab, in the query editor, enter the Hive
   data definition language (DDL) command `CREATE DATABASE
`myDataBase``. Replace
`myDatabase` with the name that you want to use.
   For restrictions on database names, see [Name databases, tables, and columns](tables-databases-columns-names.md "tables-databases-columns-names.md").
3. Choose **Run** or press
   `Ctrl+ENTER`.
4. To make your database the current database, select it from the
   **Database** menu on the left of the query editor.
   For information about controlling permissions to Athena databases, see [Configure access to databases and
   tables in the AWS Glue Data Catalog](fine-grained-access-to-glue-resources.md "fine-grained-access-to-glue-resources.md").
