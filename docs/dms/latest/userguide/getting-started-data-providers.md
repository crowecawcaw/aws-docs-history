

# Create data providers for DMS Schema Conversion
<a name="getting-started-data-providers"></a>

Next, you create data providers that describe your source and target databases. For each data provider, you specify a data store type and location information. You don't store your database credentials in a data provider.

------
#### [ AWS Management Console ]

**To create a data provider**

1. Sign in to the AWS Management Console, and open the AWS DMS console.

1. In the navigation pane, choose **Data providers**, and then choose **Create data provider**.

1. For **Name**, enter a unique name for your source data provider. For example, enter `sc-dp`.

1. For **Purpose**, select **Schema Conversion**.

1. For **Engine type**, choose the type of database engine for your data provider.

1. To use this data provider for Schema Conversion without connecting to a database, turn on **Virtual Mode**.

   There are two use cases where **Virtual Mode** applies:
   + Offline source – Convert schemas from exported script files without connecting to the source database. Offline source is currently available for Microsoft SQL Server.
   + Virtual target – Convert schemas without provisioning target infrastructure. Available for all supported target databases.

   When **Virtual Mode** is on, the console automatically sets connection information using defaults.

   For more information about using **Virtual Mode**, see [Virtual mode for offline source and virtual target](virtual-data-provider.md).

1. For **Engine configuration**, choose one of the following:
   + **Choose RDS database instance from list** – Choose **Browse**, and then choose your Amazon RDS database. DMS Schema Conversion automatically retrieves the engine type, server name, and port. For **Database name**, enter the name of your database.
   + **Enter manually** – Enter the connection information for your database. The connection parameters depend on your database engine. For more information, see [ Creating data providers](data-providers-create.md).

1. For **Secure Socket Layer (SSL) mode**, choose the type of SSL enforcement.

1. Choose **Create data provider**.

------
#### [ AWS CLI ]

To create a data provider, use the [create-data-provider](https://docs.aws.amazon.com/cli/latest/reference/dms/create-data-provider.html) command.

```
aws dms create-data-provider \
    --data-provider-name {{my-data-provider}} \
    --engine {{engine-type}} \
    --settings '{{{"EngineSettings"}}:{
        "ServerName":"{{server-name}}",
        "Port":{{port}},
        "DatabaseName":"{{database-name}}",
        "SslMode":"{{ssl-mode}}"
    }}'
```

Replace the following:
+ {{my-data-provider}} – A unique name for your data provider.
+ {{engine-type}} – The database engine. Valid values include `sqlserver`, `postgres`, `oracle`, `mysql`, `aurora`, `aurora-postgresql`.
+ {{EngineSettings}} – The engine-specific settings object, for example `MicrosoftSqlServerSettings`, `PostgreSqlSettings`, or `OracleSettings`.
+ {{server-name}} – The DNS name or IP address of your database server. This value becomes the `server-name` in selection rules.
+ {{port}} – The port used to connect to the database server.
+ {{database-name}} – The name of the database.
+ {{ssl-mode}} – The SSL mode. Valid values: `none`, `require`, `verify-ca`, `verify-full`.

**Create an offline source**

To create an offline source data provider, use the [create-data-provider](https://docs.aws.amazon.com/cli/latest/reference/dms/create-data-provider.html) command with the `--virtual` flag and the S3 settings in the engine configuration.

```
aws dms create-data-provider \
    --data-provider-name {{my-offline-source}} \
    --engine sqlserver \
    --settings '{"MicrosoftSqlServerSettings":
                    {"ServerName": "{{my-source-server}}",
                     "Port": 1433,
                     "DatabaseName": "{{MyDatabase}}",
                     "SslMode": "none",
                     "S3Path": "s3://{{amzn-s3-demo-bucket}}/{{my-prefix}}",
                     "S3AccessRoleArn": "arn:aws:iam::{{111122223333}}:role/{{my-s3-read-role}}"}}' \
    --virtual
```

The following table describes each setting. All settings are required for an offline source.


**Offline source settings**  

| Setting | Required | Description | 
| --- | --- | --- | 
| ServerName | Yes | An identifier for this data provider. Used as server-name in selection rules. Does not need to be a real hostname. | 
| Port | Yes | Standard port for the engine (1433 for SQL Server). No connection is made. | 
| DatabaseName | Yes | A database name value. No connection is made. | 
| SslMode | Yes | Use none. No connection is made. | 
| S3Path | Yes | S3 URI prefix containing your exported DDL scripts (for example, s3://amzn-s3-demo-bucket/my-prefix). | 
| S3AccessRoleArn | Yes | ARN of the IAM role that grants DMS read access to the S3 bucket. For more information, see [Configure S3 access permissions for an offline source](virtual-source-s3-permissions.md). | 

For more information about offline source prerequisites and S3 permissions, see [Offline source](virtual-data-provider.md#virtual-source-data-provider).

**Create a virtual target**

To create a virtual target data provider, use the [create-data-provider](https://docs.aws.amazon.com/cli/latest/reference/dms/create-data-provider.html) command with the `--virtual` flag. Do not include `S3Path` or `S3AccessRoleArn` – these settings are rejected for a virtual target.

```
aws dms create-data-provider \
    --data-provider-name {{my-virtual-target}} \
    --engine postgres \
    --settings '{"PostgreSqlSettings":
                    {"ServerName": "{{my-target-server}}",
                     "Port": 5432,
                     "DatabaseName": "{{postgres}}",
                     "SslMode": "none"}}' \
    --virtual
```

The following table describes each setting.


**Virtual target settings**  

| Setting | Required | Description | 
| --- | --- | --- | 
| ServerName | Yes | An identifier for this data provider. Used as server-name in selection rules. Does not need to be a real hostname. | 
| Port | Yes | Standard port for the engine (5432 for PostgreSQL, 3306 for MySQL). No connection is made. | 
| DatabaseName | Yes | A database name placeholder. No connection is made. | 
| SslMode | Yes | Use none. No connection is made. | 
| S3Path | N/A | Do not include. Rejected for virtual targets. | 
| S3AccessRoleArn | N/A | Do not include. Rejected for virtual targets. | 

For more information about virtual mode, see [Virtual target](virtual-data-provider.md#virtual-target-data-provider).

------