# Use the AWS CLI to recreate an AWS Glue

database and its tables

Renaming a AWS Glue database directly is not possible, but you can copy its definition,
modify the definition, and use the definition to recreate the database with a different
name. Similarly, you can copy the definitions of the tables in the old database, modify the
definitions, and use the modified definitions to recreate the tables in the new
database.

###### Note

The method presented does not copy table partitioning.

The following procedure for Windows assumes that your AWS CLI is configured for JSON output.
To change the default output format in the AWS CLI, run `aws configure`.

###### To copy an AWS Glue Database using the AWS CLI

1. At a command prompt, run the following AWS CLI command to retrieve the definition of
   the AWS Glue database that you want to copy.

```
aws glue get-database --name `database_name`
```

For more information about the `get-database` command, see [get-database](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/get-database.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/get-database.html"). 2. Save the JSON output to a file with the name of the new database (for example,
``new_database_name`.json`) to
 your desktop.
3. Open the ``new_database_name`.json`
file in a text editor. 4. In the JSON file, perform the following steps:

    1. Remove the outer `{ "Database":` entry and the corresponding
     closing brace `}` at the end of the file.
    2. Change the `Name` entry to the new database name.
    3. Remove the `CatalogId` field.

5. Save the file.
6. At a command prompt, run the following AWS CLI command to use the modified database
   definition file to create the database with the new name.

```
aws glue create-database --database-input "file://~/Desktop\`new_database_name`.json"
```

For more information about the `create-database` command, see [create-database](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/create-database.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/create-database.html"). For information about loading AWS CLI parameters from a
file, see [Loading AWS CLI
parameters from a file](../../../cli/latest/userguide/cli-usage-parameters-file.md "../../../cli/latest/userguide/cli-usage-parameters-file.md") in the _AWS Command Line Interface User Guide_. 7. To verify that the new database has been created in AWS Glue, run the following
command:

```
aws glue get-database --name `new_database_name`
```

Now you are ready to get the definition for a table that you want to copy to the new
database, modify the definition, and use the modified definition to recreate the table in
the new database. This procedure does not change the table name.

###### To copy an AWS Glue table using the AWS CLI

1. At a command prompt, run the following AWS CLI command.

```
aws glue get-table --database-name `database_name` --name `table_name`
```

For more information about the `get-table` command, see [get-table](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/get-table.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/get-table.html"). 2. Save the JSON output to a file with the name of the table (for example,
`table_name`.json) to your Windows desktop. 3. Open the file in a text editor. 4. In the JSON file, remove the outer `{"Table":` entry and the
corresponding closing brace `}` at the end of the file. 5. In the JSON file, remove the following entries and their values:

    * `DatabaseName` – This entry is not required because the
     `create-table` CLI command uses the
     `--database-name` parameter.
    * `CreateTime`
    * `UpdateTime`
    * `CreatedBy`
    * `IsRegisteredWithLakeFormation`
    * `CatalogId`
    * `VersionId`

6. Save the table definition file.
7. At a command prompt, run the following AWS CLI command to recreate the table in the
   new database:

```
aws glue create-table --database-name `new_database_name` --table-input "file://~/Desktop\`table_name`.json"
```

For more information about the `create-table` command, see [create-table](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/create-table.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/create-table.html").

The table now appears in the new database in AWS Glue and can be queried from
Athena. 8. Repeat the steps to copy each additional table to the new database in
AWS Glue.
