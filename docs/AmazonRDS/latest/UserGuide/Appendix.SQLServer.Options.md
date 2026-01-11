# Support for Linked

Servers with Oracle OLEDB in Amazon RDS for SQL Server

Linked servers with the Oracle Provider for OLEDB on RDS for SQL Server lets you access external data
sources on an Oracle database. You can read data from remote Oracle data sources and run
commands against remote Oracle database servers outside of your RDS for SQL Server DB instance. Using
linked servers with Oracle OLEDB, you can:

- Directly access data sources other than SQL Server
- Query against diverse Oracle data sources with the same query without moving the
  data
- Issue distributed queries, updates, commands, and transactions on data sources across
  an enterprise ecosystem
- Integrate connections to an Oracle database from within the Microsoft Business Intelligence
  suite (SSIS, SSRS, SSAS)
- Migrate from an Oracle database to RDS for SQL Server
  You can activate one or more linked servers for Oracle on either an existing or new RDS for SQL Server
  DB instance. Then you can integrate external Oracle data sources with your DB
  instance.

###### Contents

- [Supported versions and Regions](Appendix.SQLServer.Options.md#LinkedServers_Oracle_OLEDB.VersionRegionSupport "Appendix.SQLServer.Options.md#LinkedServers_Oracle_OLEDB.VersionRegionSupport")
- [Limitations and recommendations](Appendix.SQLServer.Options.md#LinkedServers_Oracle_OLEDB.Limitations "Appendix.SQLServer.Options.md#LinkedServers_Oracle_OLEDB.Limitations")
- [Activating linked servers with
  Oracle](Appendix.SQLServer.Options.md#LinkedServers_Oracle_OLEDB.Enabling "Appendix.SQLServer.Options.md#LinkedServers_Oracle_OLEDB.Enabling")
  - [Creating the option group for
    OLEDB_ORACLE](Appendix.SQLServer.Options.md#LinkedServers_Oracle_OLEDB.OptionGroup "Appendix.SQLServer.Options.md#LinkedServers_Oracle_OLEDB.OptionGroup")
  - [Adding the OLEDB_ORACLE option to the option group](Appendix.SQLServer.Options.md#LinkedServers_Oracle_OLEDB.Add "Appendix.SQLServer.Options.md#LinkedServers_Oracle_OLEDB.Add")
  - [Modifying the OLEDB_ORACLE version option to another version](Appendix.SQLServer.Options.md#LinkedServers_Oracle_OLEDB.Modify "Appendix.SQLServer.Options.md#LinkedServers_Oracle_OLEDB.Modify")
  - [Associating the option group with your DB
    instance](Appendix.SQLServer.Options.md#LinkedServers_Oracle_OLEDB.Apply "Appendix.SQLServer.Options.md#LinkedServers_Oracle_OLEDB.Apply")

- [Modifying OLEDB provider properties](Appendix.SQLServer.Options.md#LinkedServers_Oracle_OLEDB.ModifyProviderProperties "Appendix.SQLServer.Options.md#LinkedServers_Oracle_OLEDB.ModifyProviderProperties")
- [Modifying OLEDB driver properties](Appendix.SQLServer.Options.md#LinkedServers_Oracle_OLEDB.ModifyDriverProperties "Appendix.SQLServer.Options.md#LinkedServers_Oracle_OLEDB.ModifyDriverProperties")
- [Deactivating linked servers with
  Oracle](Appendix.SQLServer.Options.md#LinkedServers_Oracle_OLEDB.Disable "Appendix.SQLServer.Options.md#LinkedServers_Oracle_OLEDB.Disable")

## Supported versions and Regions

RDS for SQL Server supports linked servers with Oracle OLEDB in all Regions for SQL Server Standard
and Enterprise Editions on the following versions:

- SQL Server 2022, all versions
- SQL Server 2019, all versions
- SQL Server 2017, all versions

Linked servers with Oracle OLEDB is supported for the following Oracle Database
versions:

- Oracle Database 21c, all versions
- Oracle Database 19c, all versions
- Oracle Database 18c, all versions

Linked servers with Oracle OLEDB is supported for the following OLEDB Oracle driver
versions:

- 21.7
- 21.16

## Limitations and recommendations

Keep in mind the following limitations and recommendations that apply to linked servers
with Oracle OLEDB:

- Allow network traffic by adding the applicable TCP port in the security group for each
  RDS for SQL Server DB instance. For example, if you’re configuring a linked server between
  an EC2 Oracle DB instance and an RDS for SQL Server DB instance, then you must allow
  traffic from the IP address of the EC2 Oracle DB instance. You also must allow
  traffic on the port that SQL Server is using to listen for database
  communication. For more information on security groups, see [Controlling access with security
  groups](Overview.md "Overview.md").
- Perform a reboot of the RDS for SQL Server DB instance after turning on, turning off, or modifying
  the `OLEDB_ORACLE` option in your option group. The option group
  status displays `pending_reboot` for these events and is
  required. For RDS for SQL Server Multi-AZ instances with AlwaysOn or Mirroring option enabled,
  a failover is expected when instance is rebooted after the new instance creation or restore.
- Only simple authentication is supported with a user name and password for the Oracle data
  source.
- Open Database Connectivity (ODBC) drivers are not supported. Only the OLEDB driver versions listed
  above are supported.
- Distributed transactions (XA) are supported. To activate distributed transactions, turn
  on the `MSDTC` option in the Option Group for your DB instance and
  make sure XA transactions are turned on. For more information, see [Support for Microsoft Distributed Transaction Coordinator in RDS for SQL Server](Appendix.SQLServer.Options.md "Appendix.SQLServer.Options.md").
- Creating data source names (DSNs) to use as a shortcut for a connection string is not supported.
- OLEDB driver tracing is not supported. You can use SQL Server Extended Events to trace OLEDB events.
  For more information, see [Set up Extended Events in RDS for SQL Server](https://aws.amazon.com/blogs/database/set-up-extended-events-in-amazon-rds-for-sql-server/ "https://aws.amazon.com/blogs/database/set-up-extended-events-in-amazon-rds-for-sql-server/").
- Access to the catalogs folder for an Oracle linked server is not supported using SQL Server Management Studio (SSMS).

## Activating linked servers with

Oracle

Activate linked servers with Oracle by adding the `OLEDB_ORACLE` option to your
RDS for SQL Server DB instance. Use the following process:

1. Create a new option group, or choose an existing option group.
2. Add the `OLEDB_ORACLE` option to the option group.
3. Choose a version of the OLEDB driver to use.
4. Associate the option group with the DB instance.
5. Reboot the DB instance.

### Creating the option group for

OLEDB_ORACLE

To work with linked servers with Oracle, create an option group or modify an option group
that corresponds to the SQL Server edition and version of the DB instance that you
plan to use. To complete this procedure, use the AWS Management Console or the AWS CLI.

The following procedure creates an option group for SQL Server Standard Edition 2019.

###### To create the option group

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Option groups**.
3. Choose **Create group**.
4. In the **Create option group** window, do the following:
   1. For **Name**, enter a name for the option group that is unique
      within your AWS account, such as
      `oracle-oledb-se-2019`. The name can
      contain only letters, digits, and hyphens.
   2. For **Description**, enter a brief description of the option group,
      such as `OLEDB_ORACLE option group for SQL Server
SE 2019`. The description is used for display
      purposes.
   3. For **Engine**, choose **sqlserver-se**.
   4. For **Major engine version**, choose
      **15.00**.

5. Choose **Create**.
   The following procedure creates an option group for SQL Server Standard Edition
6.

###### To create the option group

- Run one of the following commands.

For Linux, macOS, or Unix:

```
aws rds create-option-group \
    --option-group-name `oracle-oledb-se-2019` \
    --engine-name `sqlserver-se` \
    --major-engine-version `15.00` \
    --option-group-description "`OLEDB_ORACLE option group for SQL Server SE 2019`"
```

For Windows:

```
aws rds create-option-group ^
    --option-group-name `oracle-oledb-se-2019` ^
    --engine-name `sqlserver-se` ^
    --major-engine-version `15.00` ^
    --option-group-description "`OLEDB_ORACLE option group for SQL Server SE 2019`"
```

### Adding the `OLEDB_ORACLE` option to the option group

Next, use the AWS Management Console or the AWS CLI to add the `OLEDB_ORACLE` option to your option
group.

###### To add the OLEDB_ORACLE option

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Option groups**.
3. Choose the option group that you just created, which is
   **oracle-oledb-se-2019** in this
   example.
4. Choose **Add option**.
5. Under **Option details**, choose
   **OLEDB_ORACLE** for **Option
   name**.
6. Under **Version**, choose the version of the OLEDB Oracle driver you want to install.
7. Under **Scheduling**, choose whether to add the
   option immediately or at the next maintenance window.
8. Choose **Add option**.

###### To add the OLEDB_ORACLE option

- Add the `OLEDB_ORACLE` option to the option group.

For Linux, macOS, or Unix:

```
aws rds add-option-to-option-group \
    --option-group-name `oracle-oledb-se-2019` \
    --options OptionName=OLEDB_ORACLE, OptionVersion=21.16 \
    --apply-immediately
```

For Windows:

```
aws rds add-option-to-option-group ^
    --option-group-name `oracle-oledb-se-2019` ^
    --options OptionName=OLEDB_ORACLE, OptionVersion=21.16 ^
    --apply-immediately
```

### Modifying the `OLEDB_ORACLE` version option to another version

To modify the `OLEDB_ORACLE` option version to another version, use the AWS Management Console or the AWS CLI.

###### To Modify the OLEDB_ORACLE option

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Option groups**.
3. Choose the option group with the `OLEDB_ORACLE` option
   (**oracle-oledb-se-2019** in the previous example).
4. Choose **Modify option**.
5. Under **Option details**, choose
   **OLEDB_ORACLE** for **Option
   name**.
6. Under **Version**, choose the version of the OLEDB Oracle driver you want to use.
7. Under **Scheduling**, choose whether to modify the
   option immediately or at the next maintenance window.
8. Choose **Modify option**.
   To modify the `OLEDB_ORACLE` option version, use the
   [`rds add-option-to-option-group`](../../../cli/latest/reference/rds/add-option-to-option-group.md "../../../cli/latest/reference/rds/add-option-to-option-group.md")AWS CLI command with the option group and option version
   that you want to use.

###### To modify the OLEDB_ORACLE option

- For Linux, macOS, or Unix:

```
aws rds add-option-to-option-group \
    --option-group-name `oracle-oledb-se-2019` \
    --options OptionName=OLEDB_ORACLE, OptionVersion=21.7 \
    --apply-immediately
```

For Windows:

```
aws rds add-option-to-option-group ^
    --option-group-name `oracle-oledb-se-2019` ^
    --options OptionName=OLEDB_ORACLE, OptionVersion=21.7 ^
    --apply-immediately
```

### Associating the option group with your DB

instance

To associate the `OLEDB_ORACLE` option group and parameter group with your DB instance, use the
AWS Management Console or the AWS CLI

To finish activating linked servers for Oracle, associate your `OLEDB_ORACLE`
option group with a new or existing DB instance:

- For a new DB instance, associate them when you launch the instance. For more information, see [Creating an Amazon RDS DB instance](USER_CreateDBInstance.md "USER_CreateDBInstance.md").
- For an existing DB instance, associate them by modifying the instance. For more information, see [Modifying an Amazon RDS DB instance](Overview.DBInstance.md "Overview.DBInstance.md").
  You can associate the `OLEDB_ORACLE` option group and parameter group with a new or existing DB instance.

###### To create an instance with the `OLEDB_ORACLE` option group and parameter group

- Specify the same DB engine type and major version that you used when creating the option
  group.

For Linux, macOS, or Unix:

```
aws rds create-db-instance \
    --db-instance-identifier `mytestsqlserveroracleoledbinstance` \
    --db-instance-class `db.m5.2xlarge` \
    --engine `sqlserver-se` \
    --engine-version `15.0.4236.7.v1` \
    --allocated-storage `100` \
    --manage-master-user-password \
    --master-username `admin` \
    --storage-type `gp2` \
    --license-model `li` \
    --domain-iam-role-name `my-directory-iam-role` \
    --domain `my-domain-id` \
    --option-group-name `oracle-oledb-se-2019` \
    --db-parameter-group-name `my-parameter-group-name`
```

For Windows:

```
aws rds create-db-instance ^
    --db-instance-identifier `mytestsqlserveroracleoledbinstance` ^
    --db-instance-class `db.m5.2xlarge` ^
    --engine `sqlserver-se` ^
    --engine-version `15.0.4236.7.v1` ^
    --allocated-storage `100` ^
    --manage-master-user-password ^
    --master-username `admin` ^
    --storage-type `gp2` ^
    --license-model `li` ^
    --domain-iam-role-name `my-directory-iam-role` ^
    --domain `my-domain-id` ^
    --option-group-name `oracle-oledb-se-2019` ^
    --db-parameter-group-name `my-parameter-group-name`
```

###### To modify an instance and associate the `OLEDB_ORACLE` option group

- Run one of the following commands.

For Linux, macOS, or Unix:

```
aws rds modify-db-instance \
    --db-instance-identifier `mytestsqlserveroracleoledbinstance` \
    --option-group-name `oracle-oledb-se-2019` \
    --db-parameter-group-name `my-parameter-group-name` \
    --apply-immediately
```

For Windows:

```
aws rds modify-db-instance ^
    --db-instance-identifier `mytestsqlserveroracleoledbinstance` ^
    --option-group-name `oracle-oledb-se-2019` ^
    --db-parameter-group-name `my-parameter-group-name` ^
    --apply-immediately
```

## Modifying OLEDB provider properties

You can view and change the properties of the OLEDB provider. Only the `master`
user can perform this task. All linked servers for Oracle that are created on the DB
instance use the same properties of that OLEDB provider. Call the
`sp_MSset_oledb_prop` stored procedure to change the properties of the
OLEDB provider.

To change the OLEDB provider properties

```

USE [master]
GO
EXEC sp_MSset_oledb_prop N'OraOLEDB.Oracle', N'AllowInProcess', 1
EXEC sp_MSset_oledb_prop N'OraOLEDB.Oracle', N'DynamicParameters', 0
GO

```

The following properties can be modified:

| Property name            | Recommended Value (1 = On, 0 = Off) | Description                                                                                                                                                                                 |
| ------------------------ | ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Dynamic parameter`      | 1                                   | Allows SQL placeholders (represented by '?') in parameterized queries.                                                                                                                      |
| `Nested queries`         | 1                                   | Allows nested `SELECT` statements in the `FROM` clause, such as<br>sub-queries.                                                                                                             |
| `Level zero only`        | 0                                   | Only base-level OLEDB interfaces are called against the provider.                                                                                                                           |
| `Allow inprocess`        | 1                                   | If turned on, Microsoft SQL Server allows the provider to be instantiated as an in-process<br>server. Set this property to 1 to use Oracle linked servers.                                  |
| `Non transacted updates` | 0                                   | If non-zero, SQL Server allows updates.                                                                                                                                                     |
| `Index as access path`   | False                               | If non-zero, SQL Server attempts to use indexes of the provider to fetch data.                                                                                                              |
| `Disallow adhoc access`  | False                               | If set, SQL Server does not allow running pass-through queries against the OLEDB provider.<br>While this option can be checked, it is sometimes appropriate to run<br>pass-through queries. |
| `Supports LIKE operator` | 1                                   | Indicates that the provider supports queries using the LIKE keyword.                                                                                                                        |

## Modifying OLEDB driver properties

You can view and change the properties of the OLEDB driver when creating a linked server for
Oracle. Only the `master` user can perform this task. Driver properties
define how the OLEDB driver handles data when working with a remote Oracle data source.
Driver properties are specific to each Oracle linked server created on the DB instance.
Call the `master.dbo.sp_addlinkedserver` stored procedure to change the
properties of the OLEDB driver.

Example: To create a linked server and change the OLEDB driver `FetchSize` property

```

EXEC master.dbo.sp_addlinkedserver
@server = N`'Oracle_link2'`,
@srvproduct=N`'Oracle'`,
@provider=N`'OraOLEDB.Oracle'`,
@datasrc=N`'my-oracle-test.cnetsipka.us-west-2.rds.amazonaws.com:1521/ORCL'`,
@provstr=`'FetchSize=200'`
GO

```

```

EXEC master.dbo.sp_addlinkedsrvlogin
@rmtsrvname=N`'Oracle_link2'`,
@useself=N`'False'`,
@locallogin=`NULL`,
@rmtuser=N`'master'`,
@rmtpassword=`'Test#1234'`
GO

```

###### Note

Specify a password other than the prompt shown here as a security best practice.

## Deactivating linked servers with

Oracle

To deactivate linked servers with Oracle, remove the `OLEDB_ORACLE` option from
its option group.

###### Important

Removing the option doesn't delete the existing linked server configurations on the DB instance. You must manually drop them
to remove them from the DB instance.

You can reactivate the `OLEDB_ORACLE` option after removal to reuse the linked
server configurations that were previously configured on the DB instance.

The following procedure removes the `OLEDB_ORACLE` option.

###### To remove the OLEDB_ORACLE option from its option group

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Option groups**.
3. Choose the option group with the `OLEDB_ORACLE` option (`oracle-oledb-se-2019` in
   the previous examples).
4. Choose **Delete option**.
5. Under **Deletion options**, choose **OLEDB_ORACLE** for
   **Options to delete**.
6. Under **Apply immediately**, choose **Yes** to delete
   the option immediately, or **No** to delete it during
   the next maintenance window.
7. Choose **Delete**.
   The following procedure removes the `OLEDB_ORACLE` option.

###### To remove the OLEDB_ORACLE option from its option group

- Run one of the following commands.

For Linux, macOS, or Unix:

```
aws rds remove-option-from-option-group \
    --option-group-name `oracle-oledb-se-2019` \
    --options OLEDB_ORACLE \
    --apply-immediately
```

For Windows:

```
aws rds remove-option-from-option-group ^
    --option-group-name `oracle-oledb-se-2019` ^
    --options OLEDB_ORACLE ^
    --apply-immediately
```
