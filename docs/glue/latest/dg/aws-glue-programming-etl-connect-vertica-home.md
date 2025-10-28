# Vertica connections

You can use AWS Glue for Spark to read from and write to tables in Vertica in AWS Glue 4.0 and later versions. You
can define what to read from Vertica with a SQL query. You connect to Vertica using username and password credentials stored in
AWS Secrets Manager through a AWS Glue connection.

For more information about Vertica, consult the [Vertica
documentation](https://www.vertica.com/docs/9.3.x/HTML/Content/Authoring/UsingVerticaOnAWS/UsingVerticaOnAWS.htm "https://www.vertica.com/docs/9.3.x/HTML/Content/Authoring/UsingVerticaOnAWS/UsingVerticaOnAWS.htm").

## Configuring Vertica connections

To connect to Vertica from AWS Glue, you will need to create and store your Vertica credentials in a
AWS Secrets Manager secret, then associate that secret with a Vertica AWS Glue connection. If your Vertica instance is in
an Amazon VPC, you will also need to provide networking options to your AWS Glue Vertica connection. You will need
an Amazon S3 bucket or folder to use for temporary storage when reading from and writing to the database.

To connect to Vertica from AWS Glue, you will need some prerequisites:

- An Amazon S3 bucket or folder to use for temporary storage when reading from and writing to the
  database, referred to by `tempS3Path`.

###### Note

When using Vertica in AWS Glue job data previews, temporary files may not be automatically
removed from `tempS3Path`. To ensure the removal of temporary files,
directly end the data preview session by choosing **End session** in the
**Data preview** pane.

If you cannot guarantee the data preview session is ended directly, consider setting Amazon S3
Lifecycle configuration to remove old data. We recommend removing data
older than 49 hours, based on maximum job runtime plus a margin. For more information about
configuring Amazon S3 Lifecycle, see [Managing your storage
lifecycle](../../../AmazonS3/latest/userguide/object-lifecycle-mgmt.md "../../../AmazonS3/latest/userguide/object-lifecycle-mgmt.md") in the Amazon S3 documentation.

- An IAM policy with appropriate permissions to your Amazon S3 path you can associate with your AWS Glue job role.
- If your Vertica instance is in an Amazon VPC, configure Amazon VPC to allow your AWS Glue job to communicate
  with the Vertica instance without traffic traversing the public internet.

In Amazon VPC, identify or create a **VPC**, **Subnet** and
**Security group** that AWS Glue will use while executing the job. Additionally, you
need to ensure Amazon VPC is configured to permit network traffic between your Vertica instance and this
location. Your job will need to establish a TCP connection with your Vertica client port, (default
5433). Based on your network layout, this may require changes to security group rules, Network ACLs,
NAT Gateways and Peering connections.

You can then proceed to configure AWS Glue for use with Vertica.

###### To configure a connection to Vertica:

1. In AWS Secrets Manager, create a secret using your Vertica credentials,
   `verticaUsername` and `verticaPassword`. To create
   a secret in Secrets Manager, follow the tutorial available in [Create an AWS Secrets Manager secret](../../../secretsmanager/latest/userguide/create_secret.md "../../../secretsmanager/latest/userguide/create_secret.md") in
   the AWS Secrets Manager documentation. After creating the secret, keep the Secret name,
   `secretName` for the next step.
   - When selecting **Key/value pairs**, create a pair for the key
     `user` with the value `verticaUsername`.
   - When selecting **Key/value pairs**, create a pair for the key
     `password` with the value `verticaPassword`.

2. In the AWS Glue console, create a connection by following the steps in [Adding an AWS Glue connection](console-connections.md "console-connections.md").
   After creating the connection, keep the connection name, `connectionName`, for the next step.
   - When selecting a **Connection type**, select Vertica.
   - When selecting **Vertica Host**, provide the hostname of your Vertica installation.
   - When selecting **Vertica Port**, the port your Vertica installation is available through.
   - When selecting an **AWS Secret**, provide `secretName`.

3. In the following situations, you may require additional configuration:
   - For Vertica instances hosted on AWS in an Amazon VPC
     - Provide Amazon VPC connection information to the AWS Glue connection that
       defines your Vertica security credentials. When creating or updating your
       connection, set **VPC**, **Subnet** and
       **Security groups** in **Network options**.

After creating a AWS Glue Vertica connection, you will need to perform the following steps before calling your connection method.

- Grant the IAM role associated with your AWS Glue job permissions to `tempS3Path`.
- Grant the IAM role associated with your AWS Glue job permission to read `secretName`.
- In your AWS Glue job configuration, provide `connectionName` as an **Additional network connection**.

## Reading from Vertica

**Prerequisites:**

- A Vertica table you would like to read from. You will need the Vertica database name,
  `dbName` and the table name, `tableName`.
- A AWS Glue Vertica connection configured to provide auth information. Complete the steps in the previous procedure, _To configure a connection to Vertica_ to configure your auth
  information. You will need the name of the AWS Glue connection,
  `connectionName`.
- A Amazon S3 bucket or folder to use for temporary storage, mentioned previously. You will need the name,
  `tempS3Path`. You will need to connect to this location using the
  `s3a` protocol.

For example:

```
dynamicFrame = glueContext.create_dynamic_frame.from_options(
    connection_type="vertica",
    connection_options={
        "connectionName": "`connectionName`",
        "staging_fs_url": "s3a://`tempS3Path`",
        "db": "`dbName`",
        "table": "`tableName`",
    }
)
```

You can also provide a SELECT SQL query, to filter the results returned to your DynamicFrame or to access a dataset from multiple
tables.

For example:

```
dynamicFrame = glueContext.create_dynamic_frame.from_options(
    connection_type="vertica",
    connection_options={
        "connectionName": "`connectionName`",
        "staging_fs_url": "s3a://`tempS3Path`",
        "db": "`dbName`",
        "query": "select * FROM `tableName`",
    },
)
```

## Writing to Vertica tables

This example writes information from an existing DynamicFrame, `dynamicFrame` to
Vertica. If the table already has information, AWS Glue will append data from your DynamicFrame.

**Prerequisites:**

- A current or desired table name, `tableName`, you would like to write to.
  You will also need the corresponding Vertica database name, `dbName`.
- A AWS Glue Vertica connection configured to provide auth information. Complete the steps in the previous procedure, _To configure a connection to Vertica_ to configure your auth
  information. You will need the name of the AWS Glue connection,
  `connectionName`.
- A Amazon S3 bucket or folder to use for temporary storage, mentioned previously. You will need the name,
  `tempS3Path`. You will need to connect to this location using the
  `s3a` protocol.

For example:

```
glueContext.write_dynamic_frame.from_options(
    frame=`dynamicFrame`,
    connection_type="vertica",
    connection_options={
        "connectionName": "`connectionName`",
        "staging_fs_url": "s3a://`tempS3Path`",
        "db": "`dbName`",
        "table": "`tableName`",
    }
)
```

## Vertica connection option reference

- `connectionName` — Required. Used for Read/Write. The name of a AWS Glue Vertica
  connection configured to provide auth and networking information to your connection method.
- `db` — Required. Used for Read/Write. The name of a database in Vertica your
  connection method will interact with.
- `dbSchema` — Required if needed to identify your table. Used for Read/Write.
  Default: `public`. The name of a schema your connection method will interact with.
- `table` — Required for writing, required for reading unless `query`
  is provided. Used for Read/Write. The name of a table your connection method will interact
  with.
- `query` — Used for Read. A SELECT SQL query defining what should be retrieved
  when reading from Teradata.
- `staging_fs_url` — Required. Used for Read/Write. Valid Values: `s3a`
  URLs. The URL of a Amazon S3 bucket or folder to use for temporary storage.
