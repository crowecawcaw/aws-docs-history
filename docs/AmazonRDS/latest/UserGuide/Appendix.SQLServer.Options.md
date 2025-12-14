# Support for SQL Server Integration Services in Amazon RDS for SQL Server

Microsoft SQL Server Integration Services (SSIS) is a component that you can use to perform
a broad range of data migration tasks. SSIS is a platform for data integration and workflow
applications. It features a data warehousing tool used for data extraction, transformation,
and loading (ETL). You can also use this tool to automate maintenance of SQL Server
databases and updates to multidimensional cube data.

SSIS projects are organized into packages saved as XML-based .dtsx files. Packages can
contain control flows and data flows. You use data flows to represent ETL operations. After
deployment, packages are stored in SQL Server in the SSISDB database. SSISDB is an online
transaction processing (OLTP) database in the full recovery mode.

Amazon RDS for SQL Server supports running SSIS directly on an RDS DB instance. You can enable SSIS on an existing or new DB instance.
SSIS is installed on the same DB instance as your database engine.

RDS supports SSIS for SQL Server Standard and Enterprise Editions on the following versions:

- SQL Server 2022, all versions
- SQL Server 2019, version 15.00.4043.16.v1 and higher
- SQL Server 2017, version 14.00.3223.3.v1 and higher
- SQL Server 2016, version 13.00.5426.0.v1 and higher

###### Contents

- [Limitations and recommendations](Appendix.SQLServer.Options.md#SSIS.Limitations "Appendix.SQLServer.Options.md#SSIS.Limitations")
- [Enabling SSIS](Appendix.SQLServer.Options.md#SSIS.Enabling "Appendix.SQLServer.Options.md#SSIS.Enabling")
  - [Creating the option group for
    SSIS](Appendix.SQLServer.Options.md#SSIS.OptionGroup "Appendix.SQLServer.Options.md#SSIS.OptionGroup")
  - [Adding the SSIS option to the option group](Appendix.SQLServer.Options.md#SSIS.Add "Appendix.SQLServer.Options.md#SSIS.Add")
  - [Creating the parameter group for
    SSIS](Appendix.SQLServer.Options.md#SSIS.CreateParamGroup "Appendix.SQLServer.Options.md#SSIS.CreateParamGroup")
  - [Modifying the parameter for SSIS](Appendix.SQLServer.Options.md#SSIS.ModifyParam "Appendix.SQLServer.Options.md#SSIS.ModifyParam")
  - [Associating the option group and parameter group with your DB
    instance](Appendix.SQLServer.Options.md#SSIS.Apply "Appendix.SQLServer.Options.md#SSIS.Apply")
  - [Enabling S3 integration](Appendix.SQLServer.Options.md#SSIS.EnableS3 "Appendix.SQLServer.Options.md#SSIS.EnableS3")

- [Administrative permissions on SSISDB](SSIS.md "SSIS.md")
  - [Setting up a Windows-authenticated user for SSIS](SSIS.md#SSIS.Use.Auth "SSIS.md#SSIS.Use.Auth")

- [Deploying an SSIS project](SSIS.md "SSIS.md")
- [Monitoring the status of a deployment task](SSIS.md "SSIS.md")
- [Using SSIS](SSIS.md "SSIS.md")
  - [Setting database connection managers for SSIS projects](SSIS.md#SSIS.Use.ConnMgrs "SSIS.md#SSIS.Use.ConnMgrs")
  - [Creating an SSIS proxy](SSIS.md#SSIS.Use.Proxy "SSIS.md#SSIS.Use.Proxy")
  - [Scheduling an SSIS package using SQL Server Agent](SSIS.md#SSIS.Use.Schedule "SSIS.md#SSIS.Use.Schedule")
  - [Revoking SSIS access from the proxy](SSIS.md#SSIS.Use.Revoke "SSIS.md#SSIS.Use.Revoke")

- [Disable and drop SSIS database](SSIS.md "SSIS.md")
  - [Disabling SSIS](SSIS.md#SSIS.Disable "SSIS.md#SSIS.Disable")
  - [Dropping the SSISDB database](SSIS.md#SSIS.Drop "SSIS.md#SSIS.Drop")

## Limitations and recommendations

The following limitations and recommendations apply to running SSIS on RDS for SQL Server:

- The DB instance must have an associated parameter group with the `clr enabled`
  parameter set to 1. For more information, see [Modifying the parameter for SSIS](#SSIS.ModifyParam "#SSIS.ModifyParam").

###### Note

If you enable the `clr enabled` parameter on SQL Server 2017 or 2019, you can't use the common language runtime
(CLR) on your DB instance. For more information, see [Features not supported and features with limited support](SQLServer.Concepts.General.md "SQLServer.Concepts.General.md").

- The following control flow tasks are supported:
  - Analysis Services Execute DDL Task
  - Analysis Services Processing Task
  - Bulk Insert Task
  - Check Database Integrity Task
  - Data Flow Task
  - Data Mining Query Task
  - Data Profiling Task
  - Execute Package Task
  - Execute SQL Server Agent Job Task
  - Execute SQL Task
  - Execute T-SQL Statement Task
  - Notify Operator Task
  - Rebuild Index Task
  - Reorganize Index Task
  - Shrink Database Task
  - Transfer Database Task
  - Transfer Jobs Task
  - Transfer Logins Task
  - Transfer SQL Server Objects Task
  - Update Statistics Task

- Only project deployment is supported.
- Running SSIS packages by using SQL Server Agent is supported.
- SSIS log records can be inserted only into user-created databases.
- Use only the `D:\S3` folder for working with files. Files placed in any other
  directory are deleted. Be aware of a few other file location details:
  - Place SSIS project input and output files in the `D:\S3` folder.
  - For the Data Flow Task, change the location for `BLOBTempStoragePath` and `BufferTempStoragePath` to a file
    inside the `D:\S3` folder. The file path must start with `D:\S3\`.
  - Ensure that all parameters, variables, and expressions used for file connections point
    to the `D:\S3` folder.
  - On Multi-AZ instances, files created by SSIS in the `D:\S3` folder are deleted after a failover. For more information, see
    [Multi-AZ limitations for S3 integration](User.SQLServer.Options.md#S3-MAZ "User.SQLServer.Options.md#S3-MAZ").
  - Upload the files created by SSIS in the `D:\S3` folder to
    your Amazon S3 bucket to make them durable.

- Import Column and Export Column transformations and the Script component on the Data Flow Task aren't supported.
- You can't enable dump on running SSIS packages, and you can't add data taps on SSIS packages.
- The SSIS Scale Out feature isn't supported.
- You can't deploy projects directly. We provide RDS stored procedures to do this. For more
  information, see [Deploying an SSIS project](SSIS.md "SSIS.md").
- Build SSIS project (.ispac) files with the `DoNotSavePasswords` protection
  mode for deploying on RDS.
- SSIS isn't supported on Always On instances with read replicas.
- You can't back up the SSISDB database that is associated with the `SSIS` option.
- Importing and restoring the SSISDB database from other instances of SSIS
  isn't supported.
- You can connect to other SQL Server DB instances or to an Oracle data source. Connecting to other database engines,
  such as MySQL or PostgreSQL, isn't supported for SSIS on RDS for SQL Server. For more information on connecting to an
  Oracle data source, see [Linked Servers with Oracle OLEDB](Appendix.SQLServer.Options.md "Appendix.SQLServer.Options.md").
- SSIS does not support a domain joined instance with an outgoing trust to an on-premises domain. When using an outgoing trust, run the SSIS job from an account in the local AWS domain.

## Enabling SSIS

You enable SSIS by adding the SSIS option to your DB instance. Use the following process:

1. Create a new option group, or choose an existing option group.
2. Add the `SSIS` option to the option group.
3. Create a new parameter group, or choose an existing parameter group.
4. Modify the parameter group to set the `clr enabled` parameter to 1.
5. Associate the option group and parameter group with the DB instance.
6. Enable Amazon S3 integration.

###### Note

If a database with the name SSISDB or a reserved SSIS login already exists on the DB
instance, you can't enable SSIS on the instance.

### Creating the option group for

SSIS

To work with SSIS, create an option group or modify an option group that corresponds to
the SQL Server edition and version of the DB instance that you plan to use. To do
this, use the AWS Management Console or the AWS CLI.

The following procedure creates an option group for SQL Server Standard Edition 2016.

###### To create the option group

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Option groups**.
3. Choose **Create group**.
4. In the **Create option group** window, do the following:
   1. For **Name**, enter a name for the option group that is unique
      within your AWS account, such as
      `ssis-se-2016`. The name can
      contain only letters, digits, and hyphens.
   2. For **Description**, enter a brief description of the option group,
      such as `SSIS option group for SQL Server SE
2016`. The description is used for
      display purposes.
   3. For **Engine**, choose **sqlserver-se**.
   4. For **Major engine version**, choose
      **13.00**.

5. Choose **Create**.
   The following procedure creates an option group for SQL Server Standard Edition
6.

###### To create the option group

- Run one of the following commands.

For Linux, macOS, or Unix:

```
aws rds create-option-group \
    --option-group-name `ssis-se-2016` \
    --engine-name `sqlserver-se` \
    --major-engine-version `13.00` \
    --option-group-description "`SSIS option group for SQL Server SE 2016`"
```

For Windows:

```
aws rds create-option-group ^
    --option-group-name `ssis-se-2016` ^
    --engine-name `sqlserver-se` ^
    --major-engine-version `13.00` ^
    --option-group-description "`SSIS option group for SQL Server SE 2016`"
```

### Adding the SSIS option to the option group

Next, use the AWS Management Console or the AWS CLI to add the `SSIS` option to your option
group.

###### To add the SSIS option

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Option groups**.
3. Choose the option group that you just created, **ssis-se-2016** in this example.
4. Choose **Add option**.
5. Under **Option details**, choose
   **SSIS** for **Option
   name**.
6. Under **Scheduling**, choose whether to add the
   option immediately or at the next maintenance window.
7. Choose **Add option**.

###### To add the SSIS option

- Add the `SSIS` option to the option group.

For Linux, macOS, or Unix:

```
aws rds add-option-to-option-group \
    --option-group-name `ssis-se-2016` \
    --options OptionName=SSIS \
    --apply-immediately
```

For Windows:

```
aws rds add-option-to-option-group ^
    --option-group-name `ssis-se-2016` ^
    --options OptionName=SSIS ^
    --apply-immediately
```

### Creating the parameter group for

SSIS

Create or modify a parameter group for the `clr enabled` parameter that
corresponds to the SQL Server edition and version of the DB instance that you plan
to use for SSIS.

The following procedure creates a parameter group for SQL Server Standard Edition 2016.

###### To create the parameter group

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Parameter groups**.
3. Choose **Create parameter group**.
4. In the **Create parameter group** pane, do the following:
   1. For **Parameter group family**, choose
      **sqlserver-se-13.0**.
   2. For **Group name**, enter an identifier for the parameter group,
      such as
      `ssis-sqlserver-se-13`.
   3. For **Description**, enter `clr enabled parameter
group`.

5. Choose **Create**.
   The following procedure creates a parameter group for SQL Server Standard Edition
6.

###### To create the parameter group

- Run one of the following commands.

For Linux, macOS, or Unix:

```
aws rds create-db-parameter-group \
    --db-parameter-group-name `ssis-sqlserver-se-13` \
    --db-parameter-group-family "`sqlserver-se-13.0`" \
    --description "`clr enabled parameter group`"
```

For Windows:

```
aws rds create-db-parameter-group ^
    --db-parameter-group-name `ssis-sqlserver-se-13` ^
    --db-parameter-group-family "`sqlserver-se-13.0`" ^
    --description "`clr enabled parameter group`"
```

### Modifying the parameter for SSIS

Modify the `clr enabled` parameter in the parameter group that corresponds to
the SQL Server edition and version of your DB instance. For SSIS, set the `clr
 enabled` parameter to 1.

The following procedure modifies the parameter group that you created for SQL Server
Standard Edition 2016.

###### To modify the parameter group

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Parameter groups**.
3. Choose the parameter group, such as **ssis-sqlserver-se-13**.
4. Under **Parameters**, filter the parameter list for `clr`.
5. Choose **clr enabled**.
6. Choose **Edit parameters**.
7. From **Values**, choose **1**.
8. Choose **Save changes**.
   The following procedure modifies the parameter group that you created for SQL Server
   Standard Edition 2016.

###### To modify the parameter group

- Run one of the following commands.

For Linux, macOS, or Unix:

```
aws rds modify-db-parameter-group \
    --db-parameter-group-name `ssis-sqlserver-se-13` \
    --parameters "ParameterName='clr enabled',ParameterValue=`1`,ApplyMethod=immediate"
```

For Windows:

```
aws rds modify-db-parameter-group ^
    --db-parameter-group-name `ssis-sqlserver-se-13` ^
    --parameters "ParameterName='clr enabled',ParameterValue=`1`,ApplyMethod=immediate"
```

### Associating the option group and parameter group with your DB

instance

To associate the SSIS option group and parameter group with your DB instance, use the
AWS Management Console or the AWS CLI

###### Note

If you use an existing instance, it must already have an Active Directory domain and AWS Identity and Access Management (IAM) role associated with it. If you create a new instance, specify an
existing Active Directory domain and IAM role. For more information, see [Working with Active Directory with RDS for SQL Server](User.SQLServer.md "User.SQLServer.md").

To finish enabling SSIS, associate your SSIS option group and parameter group with a new
or existing DB instance:

- For a new DB instance, associate them when you launch the instance. For more information, see [Creating an Amazon RDS DB instance](USER_CreateDBInstance.md "USER_CreateDBInstance.md").
- For an existing DB instance, associate them by modifying the instance. For more information, see [Modifying an Amazon RDS DB instance](Overview.DBInstance.md "Overview.DBInstance.md").
  You can associate the SSIS option group and parameter group with a new or existing DB instance.

###### To create an instance with the SSIS option group and parameter group

- Specify the same DB engine type and major version as you used when creating the option group.

For Linux, macOS, or Unix:

```
aws rds create-db-instance \
    --db-instance-identifier `myssisinstance` \
    --db-instance-class `db.m5.2xlarge` \
    --engine `sqlserver-se` \
    --engine-version `13.00.5426.0.v1` \
    --allocated-storage `100` \
    --manage-master-user-password \
    --master-username `admin` \
    --storage-type `gp2` \
    --license-model `li` \
    --domain-iam-role-name `my-directory-iam-role` \
    --domain `my-domain-id` \
    --option-group-name `ssis-se-2016` \
    --db-parameter-group-name `ssis-sqlserver-se-13`
```

For Windows:

```
aws rds create-db-instance ^
    --db-instance-identifier `myssisinstance` ^
    --db-instance-class `db.m5.2xlarge` ^
    --engine `sqlserver-se` ^
    --engine-version `13.00.5426.0.v1` ^
    --allocated-storage `100` ^
    --manage-master-user-password ^
    --master-username `admin` ^
    --storage-type `gp2` ^
    --license-model `li` ^
    --domain-iam-role-name `my-directory-iam-role` ^
    --domain `my-domain-id` ^
    --option-group-name `ssis-se-2016` ^
    --db-parameter-group-name `ssis-sqlserver-se-13`
```

###### To modify an instance and associate the SSIS option group and parameter group

- Run one of the following commands.

For Linux, macOS, or Unix:

```
aws rds modify-db-instance \
    --db-instance-identifier `myssisinstance` \
    --option-group-name `ssis-se-2016` \
    --db-parameter-group-name `ssis-sqlserver-se-13` \
    --apply-immediately
```

For Windows:

```
aws rds modify-db-instance ^
    --db-instance-identifier `myssisinstance` ^
    --option-group-name `ssis-se-2016` ^
    --db-parameter-group-name `ssis-sqlserver-se-13` ^
    --apply-immediately
```

### Enabling S3 integration

To download SSIS project (.ispac) files to your host for deployment, use S3 file
integration. For more information, see [Integrating an Amazon RDS for SQL Server
DB instance with Amazon S3](User.SQLServer.Options.md "User.SQLServer.Options.md").
