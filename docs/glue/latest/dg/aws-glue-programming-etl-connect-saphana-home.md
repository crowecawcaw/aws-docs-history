# SAP HANA connections

You can use AWS Glue for Spark to read from and write to tables in SAP HANA in AWS Glue 4.0 and later versions. You
can define what to read from SAP HANA with a SQL query. You connect to SAP HANA using JDBC credentials stored in
AWS Secrets Manager through a AWS Glue SAP HANA connection.

For more information about SAP HANA JDBC, consult [the SAP HANA documentation](https://help.sap.com/docs/SAP_HANA_PLATFORM/0eec0d68141541d1b07893a39944924e/ff15928cf5594d78b841fbbe649f04b4.html "https://help.sap.com/docs/SAP_HANA_PLATFORM/0eec0d68141541d1b07893a39944924e/ff15928cf5594d78b841fbbe649f04b4.html").

## Configuring SAP HANA connections

To connect to SAP HANA from AWS Glue, you will need to create and store your SAP HANA credentials
in a AWS Secrets Manager secret, then associate that secret with a SAP HANA AWS Glue connection. You will need to configure
network connectivity between your SAP HANA service and AWS Glue.

To connect to SAP HANA, you may need some prerequisites:

- If your SAP HANA service is in an Amazon VPC, configure Amazon VPC to allow your AWS Glue job to communicate
  with the SAP HANA service without traffic traversing the public internet.

In Amazon VPC, identify or create a **VPC**, **Subnet** and
**Security group** that AWS Glue will use while executing the job. Additionally, you
need to ensure Amazon VPC is configured to permit network traffic between your SAP HANA endpoint and this
location. Your job will need to establish a TCP connection with your SAP HANA JDBC port. For more
information about SAP HANA ports, see the [SAP HANA documentation](https://help.sap.com/docs/HANA_SMART_DATA_INTEGRATION/7952ef28a6914997abc01745fef1b607/88e2e8bded9e4041ad3ad87dc46c7b55.html?locale=en-US "https://help.sap.com/docs/HANA_SMART_DATA_INTEGRATION/7952ef28a6914997abc01745fef1b607/88e2e8bded9e4041ad3ad87dc46c7b55.html?locale=en-US"). Based on your network layout, this may require changes to security
group rules, Network ACLs, NAT Gateways and Peering connections.

- There are no additional prerequisites if your SAP HANA endpoint is internet accesible.

###### To configure a connection to SAP HANA:

1.  In AWS Secrets Manager, create a secret using your SAP HANA credentials.
    To create a secret in Secrets Manager, follow the tutorial available in [Create an AWS Secrets Manager secret](../../../secretsmanager/latest/userguide/create_secret.md "../../../secretsmanager/latest/userguide/create_secret.md") in the AWS Secrets Manager documentation.
    After creating the secret, keep the Secret name, `secretName` for the next step.
    - When selecting **Key/value pairs**, create a pair for
      the key `username/USERNAME` with the value `saphanaUsername`.
    - When selecting **Key/value pairs**, create a pair for
      the key `password/PASSWORD` with the value `saphanaPassword`.

2.  In the AWS Glue console, create a connection by following the steps in [Adding an AWS Glue connection](console-connections.md "console-connections.md").
    After creating the connection, keep the connection name, `connectionName`, for future use in AWS Glue.
    - When selecting a **Connection type**, select SAP HANA.
    - When providing **SAP HANA URL**, provide the URL for your instance.

    SAP HANA JDBC URLs are in the form `jdbc:sap://`saphanaHostname`:`saphanaPort`/?`databaseName`=`saphanaDBname`,`ParameterName`=`ParameterValue``

    AWS Glue requires the following JDBC URL parameters:

        + `databaseName` – A default database in SAP HANA to connect to.

    - When selecting an **AWS Secret**, provide `secretName`.

After creating a AWS Glue SAP HANA connection, you will need to perform the following steps before running your AWS Glue job:

- Grant the IAM role associated with your AWS Glue job permission to read `secretName`.
- In your AWS Glue job configuration, provide `connectionName` as an **Additional network connection**.

## Reading from SAP HANA tables

**Prerequisites:**

- A SAP HANA table you would like to read from. You will need identification information for the
  table.

A table can be specified with a SAP HANA table name and schema name, in the form
``schemaName`.`tableName``. The schema
name and "." separator are not required if the table is in the default schema, "public". Call this
`tableIdentifier`. Note that the database is provided as a JDBC URL parameter in `connectionName`.

- A AWS Glue SAP HANA connection configured to provide auth information. Complete the steps in the previous procedure, _To configure a connection to SAP HANA_ to configure your auth
  information. You will need the name of the AWS Glue connection,
  `connectionName`.

For example:

```
saphana_read_table = glueContext.create_dynamic_frame.from_options(
    connection_type="saphana",
    connection_options={
        "connectionName": "`connectionName`",
        "dbtable": "`tableIdentifier`",
    }
)
```

You can also provide a SELECT SQL query, to filter the results returned to your DynamicFrame. You will need to configure `query`.

For example:

```
saphana_read_query = glueContext.create_dynamic_frame.from_options(
    connection_type="saphana",
    connection_options={
        "connectionName": "`connectionName`",
        "query": "`query`"
    }
)
```

## Writing to SAP HANA tables

This example writes information from an existing DynamicFrame, `dynamicFrame` to
SAP HANA. If the table already has information, AWS Glue will error.

**Prerequisites:**

- A SAP HANA table you would like to write to.

A table can be specified with a SAP HANA table name and schema name, in the form
``schemaName`.`tableName``. The schema
name and "." separator are not required if the table is in the default schema, "public". Call this
`tableIdentifier`. Note that the database is provided as a JDBC URL parameter in `connectionName`.

- SAP HANA auth information. Complete the steps in the previous procedure, _To configure a connection to SAP HANA_ to configure your auth
  information. You will need the name of the AWS Glue connection,
  `connectionName`.

For example:

```
options = {
    "connectionName": "`connectionName`",
    "dbtable": '`tableIdentifier`'
}

    saphana_write = glueContext.write_dynamic_frame.from_options(
        frame=`dynamicFrame`,
        connection_type="saphana",
        connection_options=options
)
```

## SAP HANA connection option reference

- `connectionName` — Required. Used for Read/Write. The name of a AWS Glue SAP HANA
  connection configured to provide auth and networking information to your connection method.
- `databaseName` — Used for Read/Write. Valid Values: names of databases in SAP HANA. Name of database to connect to.
- `dbtable` — Required for writing, required for reading unless `query`
  is provided. Used for Read/Write. Valid Values: contents of a SAP HANA
  SQL FROM clause. Identifies a table in SAP HANA to connect to. You may also provide other SQL than a
  table name, such as a subquery. For more information, see the [From clause](https://help.sap.com/docs/SAP_HANA_PLATFORM/4fe29514fd584807ac9f2a04f6754767/20fcf24075191014a89e9dc7b8408b26.html#loio20fcf24075191014a89e9dc7b8408b26__from_clause "https://help.sap.com/docs/SAP_HANA_PLATFORM/4fe29514fd584807ac9f2a04f6754767/20fcf24075191014a89e9dc7b8408b26.html#loio20fcf24075191014a89e9dc7b8408b26__from_clause") in the SAP HANA documentation.
- `query` — Used for Read. A SAP HANA SQL SELECT query defining what should be retrieved
  when reading from SAP HANA.
