# Configuring server options

This topic provides reference content comparing server and database configuration options between Microsoft SQL Server 2019 and Amazon Aurora MySQL. You can understand the key differences in how these database systems manage global settings, runtime configurations, and security parameters.

| Feature compatibility          | AWS SCT / AWS DMS automation level | AWS SCT action code index | Key differences                            |
| ------------------------------ | ---------------------------------- | ------------------------- | ------------------------------------------ |
| One star feature compatibility | N/A                                | N/A                       | Use cluster and database parameter groups. |

## SQL Server Usage

SQL Server provides server-level settings that affect all databases and all sessions. You can modify these settings using the `sp_configure` system stored procedure.

You can use server options to perform the following configuration tasks:

- Define hardware utilization such as memory management, affinity mask, priority boost, network packet size, and soft Non-Uniform Memory Access (NUMA).
- Alter run time global values such as recovery interval, remote login timeout, optimization for ad-hoc workloads, and cost threshold for parallelism.
- Turn on and turn off global features such as C2 Audit, OLE, procedures, CLR procedures, and allow trigger recursion.
- Configure global security settings such as server authentication mode, remote access, shell access with `xp_cmdshell`, CLR access level, and database chaining.
- Set default values for sessions such as user options, default language, backup compression, and fill factor.

Some settings require an explicit `RECONFIGURE` command to apply the changes to the server. High risk settings require `RECONFIGURE WITH OVERRIDE` for the changes to be applied. Some advanced options are hidden by default. To view and modify these settings, set show advanced options to 1 and run `sp_configure`.

###### Note

Server audits are managed through the T-SQL commands `CREATE` and `ALTER SERVER AUDIT`.

### Syntax

```
EXECUTE sp_configure <option>, <value>;
```

### Examples

Limit server memory usage to 4 GB.

```
EXECUTE sp_configure 'show advanced options', 1;
```

```
RECONFIGURE;
```

```
sp_configure 'max server memory', 4096;
```

```
RECONFIGURE;
```

Allow command shell access from T-SQL.

```
EXEC sp_configure 'show advanced options', 1;
```

```
RECONFIGURE;
```

```
EXEC sp_configure 'xp_cmdshell', 1;
```

```
RECONFIGURE;
```

View current values.

```
EXECUTE sp_configure
```

For more information, see [Server Configuration Options (SQL Server)](https://docs.microsoft.com/en-us/sql/database-engine/configure-windows/server-configuration-options-sql-server?view=sql-server-ver15 "https://docs.microsoft.com/en-us/sql/database-engine/configure-windows/server-configuration-options-sql-server?view=sql-server-ver15") in the _SQL Server documentation_.

## MySQL Usage

The concept of an database in Amazon Aurora MySQL-Compatible Edition (Aurora MySQL) is different than SQL Server. For Aurora MySQL, the terms database and schema are synonymous. Therefore, the concept of database options does isn’t applicable to Aurora MySQL.

The Aurora MySQL equivalent of SQL Server database and server options are Server System Variables, which are run time settings you can modify using one of the following approaches:

- MySQL command line utility.
- Aurora DB Cluster and DB Instance Parameters.
- System variables used by the SQL `SET` command.

Compared to SQL Server, Aurora MySQL provides a much wider range of server settings and configurations. For a full list of the options available in Aurora MySQL, see the links at the end of this section. The Aurora MySQL default parameter group lists more than 250 different parameters.

###### Note

Unlike standalone installations of MySQL, Amazon Aurora doesn’t provide file system access to the configuration file. Cluster-level parameters are managed in database cluster parameter groups. Instance-level parameters are managed in database parameter groups. Also, in Aurora MySQL some parameters from the full base set of standalone MySQL installations can’t be modified and others were removed. Many parameters are viewable but not modifiable.

SQL Server and Aurora MySQL are completely different engines. Except for a few obvious settings such as max server memory which has an equivalent of `innodb_buffer_pool_size`, most of the Aurora MySQL parameter settings aren’t compatible with SQL Server.

In most cases, you should use the default parameter groups because they are optimized for common use cases. Amazon Aurora is a cluster of DB instances and, as a direct result, some of the MySQL parameters apply to the entire cluster while other parameters apply only to particular database instances in the cluster. The following table describes how Aurora MySQL parameters are controlled:

| Aurora MySQL Parameter Class                                                                                                                 | Controlled by                                                                                                                        |
| -------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| Cluster-level parameters<br>Single cluster parameter group for each Amazon Aurora cluster.                                                   | Managed by cluster parameter groups. For example, `aurora_load_from_s3_role`, `default_password_lifetime`, `default_storage_engine`. |
| Database instance-level parameters<br>You can associate every instance in your Amazon Aurora cluster with a unique database parameter group. | Managed by database parameter groups. For example, `autocommit`, `connect_timeout`, `innodb_change_buffer_max_size`.                 |

### Syntax

Server-level options are set with the `SET GLOBAL` command.

```
SET GLOBAL <option> = <Value>;
```

### Examples

**Modify compression level**

Decrease compression level to reduce CPU usage.

```
SET GLOBAL innodb_compression_level = 5;
```

**Create parameter groups**

The following walkthrough demonstrates how to create and configure the Amazon Aurora database and cluster parameter groups:

1. Navigate to **Parameter group** in the Amazon RDS service of the AWS Console.
2. Choose **Create parameter group**.

###### Note

You can’t edit the default parameter group. Create a custom parameter group to apply changes to your Amazon Aurora cluster and its database instances. 3. For **Parameter group family**, choose `aurora-mysql5.7`. 4. For **Type**, choose **DB Parameter Group**. Another option is to choose **Cluster Parameter Group** to modify cluster parameters. 5. Choose **Create**.

**Modify a parameter group**

The following walkthrough demonstrates how to modify an existing parameter group

1. Navigate to **Parameter group** in the Amazon RDS service of the AWS Console.
2. Choose the name of the parameter group to edit.
3. Choose **Edit parameters**.
4. Change parameter values and choose **Save changes**.

For more information, see [Working with parameter groups](../../../AmazonRDS/latest/UserGuide/USER_WorkingWithParamGroups.md "../../../AmazonRDS/latest/UserGuide/USER_WorkingWithParamGroups.md") in the _Amazon Relational Database Service User Guide_ and [Server System Variables](https://dev.mysql.com/doc/refman/5.7/en/server-system-variables.html "https://dev.mysql.com/doc/refman/5.7/en/server-system-variables.html") in the _MySQL documentation_.
