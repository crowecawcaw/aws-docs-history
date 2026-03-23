# Export and import features

This topic provides reference information on data export and import capabilities in Microsoft SQL Server and PostgreSQL, with a focus on migration scenarios. You can use various tools and utilities to export data from SQL Server and import it into PostgreSQL, which is particularly useful when migrating to Amazon Aurora PostgreSQL.

| Feature compatibility    | AWS SCT / AWS DMS automation level | AWS SCT action code index | Key differences      |
| ------------------------ | ---------------------------------- | ------------------------- | -------------------- |
| No feature compatibility | N/A                                | N/A                       | Non-compatible tool. |

## SQL Server Usage

SQL Server provides many options for exporting and importing text files. These operations are commonly used for data migration, scripting, and backup.

- Save results to a file in SQL Server Management Studio (SSMS). For more information, see [KB - How to create .csv or .rpt files from an SQL statement in Microsoft SQL Server](https://support.microsoft.com/en-us/topic/kb-how-to-create-csv-or-rpt-files-from-an-sql-statement-in-microsoft-sql-server-baaccba6-a3d9-b77d-7f4e-107ae4dd739b "https://support.microsoft.com/en-us/topic/kb-how-to-create-csv-or-rpt-files-from-an-sql-statement-in-microsoft-sql-server-baaccba6-a3d9-b77d-7f4e-107ae4dd739b") in the _SQL Server documentation_.
  l SQLCMD. For more information, see [Run the script file](https://docs.microsoft.com/en-us/sql/ssms/scripting/sqlcmd-run-transact-sql-script-files?view=sql-server-ver15#save-the-output-to-a-text-file "https://docs.microsoft.com/en-us/sql/ssms/scripting/sqlcmd-run-transact-sql-script-files?view=sql-server-ver15#save-the-output-to-a-text-file") in the _SQL Server documentation_.
  l PowerShell wrapper for SQLCMD
  l SSMS Import/Export Wizard. For more information, see [Start the SQL Server Import and Export Wizard](https://docs.microsoft.com/en-us/sql/integration-services/import-export-data/start-the-sql-server-import-and-export-wizard?view=sql-server-ver15 "https://docs.microsoft.com/en-us/sql/integration-services/import-export-data/start-the-sql-server-import-and-export-wizard?view=sql-server-ver15") in the _SQL Server documentation_.
  l SQL Server Reporting Services (SSRS)
  l Bulk Copy Program (BCP). For more information, see [Import and export bulk data using bcp (SQL Server)](https://docs.microsoft.com/en-us/sql/relational-databases/import-export/import-and-export-bulk-data-by-using-the-bcp-utility-sql-server?view=sql-server-ver15 "https://docs.microsoft.com/en-us/sql/relational-databases/import-export/import-and-export-bulk-data-by-using-the-bcp-utility-sql-server?view=sql-server-ver15") in the _SQL Server documentation_.

All of the options described before required additional tools to export data. Most of the tools are open source and provide support for a variety of databases.

SQLCMD is a command line utility for running T-SQL statements, system procedures, and script files. It uses ODBC to run T-SQL batches. For example:

```
SQLCMD -i C:\sql\myquery.sql -o C:\sql\output.txt
```

SQLCMD utility syntax:

```
sqlcmd
    -a packet_size
    -A (dedicated administrator connection)
    -b (terminate batch job if there is an error)
    -c batch_terminator
    -C (trust the server certificate)
    -d db_name
    -e (echo input)
    -E (use trusted connection)
    -f codepage | i:codepage[,o:codepage] | o:codepage[,i:codepage]
    -g (enable column encryption)
    -G (use Azure Active Directory for authentication)
    -h rows_per_header
    -H workstation_name
    -i input_file
    -I (enable quoted identifiers)
    -j (Print raw error messages)
    -k[1 | 2] (remove or replace control characters)
    -K application_intent
    -l login_timeout
    -L[c] (list servers, optional clean output)
    -m error_level
    -M multisubnet_failover
    -N (encrypt connection)
    -o output_file
    -p[1] (print statistics, optional colon format)
    -P password
    -q "cmdline query"
    -Q "cmdline query" (and exit)
    -r[0 | 1] (msgs to stderr)
    -R (use client regional settings)
    -s col_separator
    -S [protocol:]server[instance_name][,port]
    -t query_timeout
    -u (unicode output file)
    -U login_id
    -v var = "value"
    -V error_severity_level
    -w column_width
    -W (remove trailing spaces)
    -x (disable variable substitution)
    -X[1] (disable commands, startup script, environment variables, optional exit)
    -y variable_length_type_display_width
    -Y fixed_length_type_display_width
    -z new_password
    -Z new_password (and exit)
    -? (usage)
```

### Examples

Connect to a named instance using Windows Authentication and specify input and output files.

```
sqlcmd -S MyMSSQLServer\MyMSSQLInstance -i query.sql -o outputfile.txt
```

If the file is needed for import to another database, query the data as `INSERT` commands and `CREATE` for the object.

You can export data with SQLCMD and import with the Export/Import wizard.

For more information, see [sqlcmd Utility](https://docs.microsoft.com/en-us/sql/tools/sqlcmd-utility?view=sql-server-ver15 "https://docs.microsoft.com/en-us/sql/tools/sqlcmd-utility?view=sql-server-ver15") in the _SQL Server documentation_.

## PostgreSQL Usage

PostgreSQL provides the native utilities `pg_dump` and `pg_restore` to perform logical database exports and imports with comparable functionality to the SQl Server SQLCMD utility. For example, moving data between two databases and creating logical database backups.

- **pg_dump** to export data.
- **pg_restore** to import data.

The binaries for both utilities must be installed on your local workstation or on an Amazon EC2 server as part of the PostgreSQL client binaries.

You can export and copy PostgreSQL dump files created using `pg_dump` to an Amazon S3 bucket as cloud backup storage or for maintaining the desired backup retention policy. Later, when you need the dump files for database restore, you can copy them copied back to a desktop or server that has a PostgreSQL client, such as your workstation or an Amazon EC2 server. Then you can issue the `pg_restore` command.

Starting with PostgreSQL 10, these capabilities were added:

- You can exclude a schema in `pg_dump` and `pg_restore` commands.
- Can create dumps with no blobs.
- Allow to run `pg_dumpall` by non-superusers, using the `--no-role-passwords` option.
- Create additional integrity option to ensure that the data is stored in disk using `fsync()` method.

Starting with PostgreSQL 11, the following capabilities were added: \* `pg_dump` and `pg_restore` now export or import relationships between extensions and database objects established with `ALTER …​ DEPENDS ON EXTENSION`, which allows these objects to be dropped when extension is dropped with `CASCADE` option.

### Notes

- `pg_dump` creates consistent backups even if the database is being used concurrently.
- `pg_dump` doesn’t block other users accessing the database (readers or writers).
- `pg_dump` only exports a single database. To backup global objects common to all databases in a cluster (such as roles and tablespaces), use `pg_dumpall`.
- PostgreSQL dump files can be plain-text and custom format files.

Another option to export and import data from PostgreSQL database is to use `COPY TO/COPY FROM` commands. Starting with PostgreSQL 12, you can use the `COPY FROM` command to load data into DB. This command has support for filtering incoming rows with the `WHERE` condition.

```
CREATE TABLE tst_copy(v TEXT);

COPY tst_copy FROM '/home/postgres/file.csv' WITH (FORMAT CSV) WHERE v LIKE '%apple%';
```

### Examples

Export data using `pg_dump`. Use a workstation or server with the PostgreSQL client installed to connect to the Amazon Aurora PostgreSQL-Compatible Edition (Aurora PostgreSQL) instance. Issue the `pg_dump` command providing the hostname (-h), database user name (-U), and database name (-d).

```
$ pg_dump -h hostname.rds.amazonaws.com -U username -d db_name -f dump_file_name.sql
```

The output `dump_file_name.sql` file is stored on the server where the `pg_dump` command runs. You can copy the output file to an Amazon S3 bucket if needed.

Run `pg_dump` and copy the backup file to an Amazon S3 bucket using a pipe and the AWS CLI.

```
$ pg_dump -h hostname.rds.amazonaws.com -U username -d db_name -f dump_file_name.sql | aws s3 cp - s3://pg-backup/pg_bck-$(date"+%Y-%m-%d-%H-%M-%S")
```

Restore data using `pg_restore`. Use a workstation or server with the PostgreSQL client installed to connect to the Aurora PostgreSQL instance. Issue the `pg_restore` command providing the hostname (-h), database user name (-U), database name (-d), and the dump file.

```
$ pg_restore -h hostname.rds.amazonaws.com -U username -d dbname_restore dump_file_name.sql
```

Copy the output file from the local server to an Amazon S3 Bucket using the AWS CLI. Upload the dump file to an Amazon S3 bucket.

```
$ aws s3 cp /usr/Exports/hr.dmp s3://my-bucket/backup-$(date "+%Y-%m-%d-%H-%M-%S")
```

###### Note

The `{-$(date "+%Y-%m-%d-%H-%M-%S")}` format is valid on Linux servers only.

Download the output file from the Amazon S3 bucket.

```
$ aws s3 cp s3://my-bucket/backup-2017-09-10-01-10-10 /usr/Exports/hr.dmp
```

###### Note

You can create a copy of an existing database without having to use `pg_dump` or `pg_restore`. Instead, use the template keyword to specify the source database.

```
CREATE DATABASE mydb_copy TEPLATE mydb;
```

## Summary

| Description                                                                                         | SQL Server export / import                                                                           |
| --------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| PostgreSQL Dump                                                                                     | Export data to a file                                                                                |
| Using SQLCMD or Export/Import Wizard<br>`<br>SQLCMD -i C:\sql\myquery.sql -o C:\sql\output.txt<br>` | `<br>pg_dump -F c -h hostname.rds.amazonaws.com<br>-U username -d hr -p 5432 > c:\Export\hr.dmp<br>` |
| Import data to a new database with a new name                                                       | Run SQLCMD with objects and data creation script<br>`<br>SQLCMD -i C:\sql\myquery.sql<br>`           |

For more information, see [SQL Dump](https://www.postgresql.org/docs/13/backup-dump.html "https://www.postgresql.org/docs/13/backup-dump.html") and [pg_restore](https://www.postgresql.org/docs/13/app-pgrestore.html "https://www.postgresql.org/docs/13/app-pgrestore.html") in the _PostgreSQL documentation_.
