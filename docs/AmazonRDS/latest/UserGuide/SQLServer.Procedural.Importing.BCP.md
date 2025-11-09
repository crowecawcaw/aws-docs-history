# Using BCP utility from Linux to import and export data

The BCP (Bulk Copy Program) utility provides an efficient way to transfer large amounts
of data between your RDS for SQL Server DB instance and data files. You can use BCP from Linux environments
to perform bulk data operations, making it useful for data migration,
ETL processes, and regular data transfers.

BCP supports both importing data from files into SQL Server
tables and exporting data from SQL Server tables to files. This is particularly effective
for transferring structured data in various formats including delimited text files.

## Prerequisites

Before using BCP with your RDS for SQL Server DB instance from Linux, ensure you have the following:

- A Linux environment with network connectivity to your RDS for SQL Server DB instance
- Microsoft SQL Server command-line tools installed on your Linux system, including:
  - sqlcmd - SQL Server command-line query tool
  - bcp - Bulk Copy Program utility

- Valid credentials for your RDS for SQL Server DB instance
- Network access configured through security groups to allow connections on the SQL Server port (typically 1433)
- Appropriate database permissions for the operations you want to perform

## Installing SQL Server command-line tools on Linux

To use BCP from Linux, you need to install the Microsoft SQL Server command-line tools.
For detailed installation instructions for your specific Linux distribution,
see the following Microsoft documentation:

- [Install sqlcmd and bcp the SQL Server command-line tools on Linux](https://docs.microsoft.com/en-us/sql/linux/sql-server-linux-setup-tools "https://docs.microsoft.com/en-us/sql/linux/sql-server-linux-setup-tools")
- [bcp utility](https://docs.microsoft.com/en-us/sql/tools/bcp-utility "https://docs.microsoft.com/en-us/sql/tools/bcp-utility") - Complete reference for the BCP utility

After installation, ensure the tools are available in your PATH by running:

```
bcp -v
sqlcmd -?
```

## Exporting data from RDS for SQL Server

You can use BCP to export data from your RDS for SQL Server DB instance to files on your Linux system.
This is useful for creating backups, data analysis, or preparing data for migration.

### Basic export syntax

The basic syntax for exporting data using BCP is:

```
bcp `database.schema.table` out output_file -S server_name -U `username` -P `password` [options]
```

Where:

- `database.schema.table` - The fully qualified table name
- `output_file` - The path and name of the output file
- `server_name` - Your RDS for SQL Server endpoint
- `username` - Your database username
- `password` - Your database password

### Export example

The following example exports data from a table named `customers` in the `sales` database:

```
bcp sales.dbo.customers out /home/user/customers.txt \
    -S mydb.cluster-abc123.us-east-1.rds.amazonaws.com \
    -U `admin` \
    -P `mypassword` \
    -c \
    -t "|" \
    -r "\n"
```

This command:

- Exports data from the `customers` table
- Saves the output to `/home/user/customers.txt`
- Uses character format (`-c`)
- Uses pipe (|) as the field delimiter (`-t "|"`)
- Uses newline as the row delimiter (`-r "\n"`)

## Importing data to RDS for SQL Server

You can use BCP to import data from files on your Linux system into your RDS for SQL Server DB instance.
This is useful for data migration, loading test data, or regular data updates.

### Basic import syntax

The basic syntax for importing data using BCP is:

```
bcp `database.schema.table` in input_file -S `server_name` -U `username` -P `password` [options]
```

Where:

- `database.schema.table` - The fully qualified destination table name
- `input_file` - The path and name of the input file
- `server_name` - Your RDS for SQL Server endpoint
- `username` - Your database username
- `password` - Your database password

### Import example

The following example imports data from a file into a table named `customers`:

```
bcp sales.dbo.customers in /home/user/customers.txt \
    -S mydb.cluster-abc123.us-east-1.rds.amazonaws.com \
    -U `admin` \
    -P `mypassword` \
    -c \
    -t "|" \
    -r "\n" \
    -b 1000
```

This command:

- Imports data into the `customers` table
- Reads data from `/home/user/customers.txt`
- Uses character format (`-c`)
- Uses pipe (|) as the field delimiter (`-t "|"`)
- Uses newline as the row delimiter (`-r "\n"`)
- Processes data in batches of 1000 rows (`-b 1000`)

## Common BCP options

BCP provides numerous options to control data formatting and transfer behavior.
The following table describes commonly used options:

| Option | Description                                      |
| ------ | ------------------------------------------------ |
| `-c`   | Uses character data type for all columns         |
| `-n`   | Uses native database data types                  |
| `-t`   | Specifies the field delimiter (default is tab)   |
| `-r`   | Specifies the row delimiter (default is newline) |
| `-b`   | Specifies the batch size for bulk operations     |
| `-F`   | Specifies the first row to export or import      |
| `-L`   | Specifies the last row to export or import       |
| `-e`   | Specifies an error file to capture rejected rows |
| `-f`   | Specifies a format file for data formatting      |
| `-q`   | Uses quoted identifiers for object names         |

## Best practices and considerations

When using BCP with RDS for SQL Server from Linux, consider the following best practices:

- **Use batch processing** – For large datasets,
  use the `-b` option to process data in batches. T
  his improves performance and allows for better error recovery.
- **Handle errors gracefully** – Use the `-e`
  option to capture error information and rejected rows in a separate file for analysis.
- **Choose appropriate data formats** – Use character format
  (`-c`) for cross-platform compatibility or native format (`-n`)
  for better performance when both source and destination are SQL Server.
- **Secure your credentials** – Avoid putting passwords
  directly in command lines. Consider using environment variables or configuration files with appropriate permissions.
- **Test with small datasets** – Before processing
  large amounts of data, test your BCP commands with smaller datasets to verify formatting and connectivity.
- **Monitor network connectivity** – Ensure stable
  network connections, especially for large data transfers. Consider using tools like `screen` or `tmux` for long-running operations.
- **Validate data integrity** – After data transfer,
  verify row counts and sample data to ensure the operation completed successfully.

## Troubleshooting common issues

The following table describes common issues you might encounter when using BCP from Linux and their solutions:

| Issue                                | Solution                                                                                                                                                                    |
| ------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Connection timeout or network errors | Verify your Amazon RDS endpoint, security group settings, and network connectivity.<br>Make sure the SQL Server port (typically 1433) is accessible from your Linux system. |
| Authentication failures              | Verify your username and password. Make sure the database user<br>has appropriate permissions for the operations you're performing.                                         |
| Data format errors                   | Check your field and row delimiters. Make sure the data format matches what BCP expects.<br>Use format files for complex data structures.                                   |
| Permission denied errors             | Make sure your database user has `INSERT` permissions for imports or<br>`SELECT` permissions for exports on the target tables.                                              |
| Large file handling issues           | Use batch processing with the `-b` option. Consider splitting<br>large files into smaller chunks for better performance and error recovery.                                 |
| Character encoding problems          | Ensure your data files use compatible character encoding. Use the `-c`<br>option for character format or specify appropriate code pages.                                    |
