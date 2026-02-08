# Scripting features

This topic provides reference information about the differences in scripting and automation capabilities between Microsoft SQL Server 2019 and Amazon Aurora MySQL. You can understand the contrasting tool sets and scripting languages used in these database systems.

| Feature compatibility    | AWS SCT / AWS DMS automation level | AWS SCT action code index | Key differences                                                                                                             |
| ------------------------ | ---------------------------------- | ------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| No feature compatibility | N/A                                | N/A                       | Non-compatible tool sets and scripting languages. Use MySQL Workbench, Amazon RDS API, AWS Management Console, and AWS CLI. |

## SQL Server Usage

SQL Server supports T-SQL and XQuery scripting within multiple run frameworks such as SQL Server Agent, and stored procedures.

The `SQLCMD` command line utility can also be used to run T-SQL scripts. However, the most extensive and feature-rich scripting environment is PowerShell.

SQL Server provides two PowerShell snap-ins that implement a provider exposing the entire SQL Server Management Object Model (SMO) as PowerShell paths. Additionally, you can use `cmd` in SQL Server to run specific SQL Server commands.

###### Note

You can use `Invoke-Sqlcmd` to run scripts using the SQLCMD utility.

The `sqlps` utility launches the PowerShell scripting environment and automatically loads the SQL Server modules. You can launch `sqlps` from a command prompt or from the Object Explorer pane of SQL Server Management Studio. You can run one-time PowerShell commands and script files (for example, `.\SomeFolder\SomeScript.ps1`).

###### Note

SQL Server Agent supports running PowerShell scripts in job steps. For more information, see [SQL Server Agent and MySQL Agent](chap-sql-server-aurora-mysql.management.md "chap-sql-server-aurora-mysql.management.md").

SQL Server also supports three types of direct database engine queries: T-SQL, XQuery, and the SQLCMD utility. You can call T-SQL and XQuery from stored procedures, SQL Server Management Studio (or other IDE), and SQL Server agent jobs. The SQLCMD utility also supports commands and variables.

### Examples

Backup a database with PowerShell using the default backup options.

```
PS C:\> Backup-SqlDatabase -ServerInstance "MyServer\SQLServerInstance" -Database "MyDB"
```

Get all rows from the `MyTable` table in the `MyDB` database.

```
PS C:\> Read-SqlTableData -ServerInstance MyServer\SQLServerInstance" -DatabaseName "MyDB" -TableName "MyTable"
```

For more information, see [SQL Server PowerShell](https://docs.microsoft.com/en-us/sql/powershell/sql-server-powershell?view=sql-server-ver15 "https://docs.microsoft.com/en-us/sql/powershell/sql-server-powershell?view=sql-server-ver15"), [Database Engine Scripting](https://docs.microsoft.com/en-us/sql/ssms/scripting/database-engine-scripting?view=sql-server-ver15 "https://docs.microsoft.com/en-us/sql/ssms/scripting/database-engine-scripting?view=sql-server-ver15"), and [sqlcmd Utility](https://docs.microsoft.com/en-us/sql/tools/sqlcmd-utility?view=sql-server-ver15 "https://docs.microsoft.com/en-us/sql/tools/sqlcmd-utility?view=sql-server-ver15") in the _SQL Server documentation_.

## MySQL Usage

As a Platform as a Service (PaaS), Aurora MySQL accepts connections from any compatible client, but you can’t access the MySQL command line utility typically used for database administration. However, you can use MySQL tools installed on a network host and the Amazon RDS API. The most common tools for Aurora MySQL scripting and automation include MySQL Workbench, MySQL Utilities, and the Amazon RDS API. The following sections describe each tool.

### MySQL Workbench

MySQL Workbench is the most commonly used tool for development and administration of MySQL servers. It is available as a free Community Edition and a paid Commercial Edition that adds enterprise features such as database documentation features. MySQL Workbench is an integrated IDE with the following features:

- **SQL Development** — Manage and configure connections to aurora MySQL clusters and run SQL queries using the SQL editor.
- **Data Modeling** — Reverse and forward engineer graphical database schema models and manage schemas with the Table Editor.
- **Server Administration** — Not applicable to Aurora MySQL. Use the Amazon RDS console to administer servers.

The MySQL Workbench also supports a Python scripting shell that you can use interactively and programmatically.

### MySQL Utilities

MySQL Utilities are a set of Python command line tools used for common maintenance and administration of MySQL servers tasks. They can reduce the need to write custom code for common tasks and can be easily customized.

The following tools are included in the MySQL Utilities set. Note that some tools will not work with Aurora MySQL because you don’t have root access to the underlying server.

- **Admin utilities** — Clone, Copy, Compare, Diff, Export, Import, and User Management.
- **Replication utilities** — Setup, Configuration, and Verification
- **General utilities** — Disk Usage, Redundant Indexes, Manage Metadata, and Manage Audit Data

### Amazon RDS API

The Amazon RDS API is a web service for managing and maintaining Aurora PostgreSQL and other relational databases. You can use Amazon RDS API to setup, operate, scale, backup, and perform many common administration tasks. The Amazon RDS API supports multiple database platforms and can integrate administration seamlessly for heterogeneous environments.

###### Note

The Amazon RDS API is asynchronous. Some interfaces may require polling or callback functions to receive command status and results.

You can access Amazon RDS using the AWS Management Console, the AWS Command Line Interface (CLI), and the Amazon RDS Programmatic API as described in the following sections.

### AWS Management Console

The AWS Management Console is a simple web-based set of tools for interactive management of Aurora PostgreSQL and other Amazon RDS services. To access the AWS Management Console, sign in to your AWS account, and choose **RDS**.

### AWS Command Line Interface

The AWS Command Line Interface is an open source tool that runs on Linux, Windows, or macOS having Python 2 version 2.6.5 and higher or Python 3 version 3.3 and higher.

The AWS CLI is built on top of the AWS SDK for Python (Boto), which provides commands for interacting with AWS services. With minimal configuration, you can start using all AWS Management Console functionality from your favorite terminal application.

- **Linux shells** — Use common shell programs such as Bash, Zsh, or tsch.
- **Windows command line** — Run commands in PowerShell or the Windows Command Processor.
- **Remotely** — Run commands on Amazon EC2 instances through a remote terminal such as PuTTY or SSH.

The AWS Tools for Windows PowerShell and AWS Tools for PowerShell Core are PowerShell modules built on the functionality exposed by the AWS SDK for .NET. These Tools enable scripting operations for AWS resources using the PowerShell command line.

###### Note

You can’t use SQL Server cmdlets in PowerShell.

### Amazon RDS Programmatic API

You can use the Amazon RDS API to automate management of database instances and other Amazon RDS objects.

For more information, see [Actions](../../../AmazonRDS/latest/APIReference/API_Operations.md "../../../AmazonRDS/latest/APIReference/API_Operations.md"), [Data Types](../../../AmazonRDS/latest/APIReference/API_Types.md "../../../AmazonRDS/latest/APIReference/API_Types.md"), [Common Parameters](../../../AmazonRDS/latest/APIReference/CommonParameters.md "../../../AmazonRDS/latest/APIReference/CommonParameters.md"), and [Common Errors](../../../AmazonRDS/latest/APIReference/CommonErrors.md "../../../AmazonRDS/latest/APIReference/CommonErrors.md") in the _Amazon Relational Database Service API Reference_.

### Examples

The following walkthrough describes how to connect to an Aurora MySQL database instance using the MySQL utility.

1. Sign in to your AWS account, choose **RDS**, and then choose **Databases**.
2. Choose the MySQL database you want to connect to and copy the cluster endpoint address.

###### Note

You can also connect to individual database instances. For more information, see [High Availability Essentials](chap-sql-server-aurora-mysql.hadr.md "chap-sql-server-aurora-mysql.hadr.md"). 3. In the command shell, enter the following:

```
mysql -h <mysql-instance-endpoint-address> -P 3306 -u MasterUser
```

In the preceding example, the `-h` parameter is the endpoint Domain Name System (DNS) name of the Aurora MySQL database cluster.

In the preceding example, the `-P` parameter is the port number. 4. Provide the password when prompted. The system displays the following (or similar) message.

```
Welcome to the MySQL monitor. Commands end with ; or \g.
Your MySQL connection id is 350
Server version: 5.6.27-log MySQL Community Server (GPL)
Type 'help;' or '\h' for help. Type '\c' to clear the buffer.
mysql>
```

For more information, see [MySQL Product Archives](https://downloads.mysql.com/archives/utilities/ "https://downloads.mysql.com/archives/utilities/"), [MySQL Workbench 8.0.29](https://dev.mysql.com/downloads/workbench/ "https://dev.mysql.com/downloads/workbench/"), [Command Line Interface](../../../cli/latest/reference.md "../../../cli/latest/reference.md"), and [Amazon Relational Database Service API Reference](../../../AmazonRDS/latest/APIReference/Welcome.md "../../../AmazonRDS/latest/APIReference/Welcome.md").
