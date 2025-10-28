# Azure Cosmos DB connections

You can use AWS Glue for Spark to read from and write to existing containers in Azure Cosmos DB using the NoSQL
API in AWS Glue 4.0 and later versions. You can define what to read from Azure Cosmos DB with a SQL query. You
connect to Azure Cosmos DB using an Azure Cosmos DB Key stored in AWS Secrets Manager through a AWS Glue connection.

For more information about Azure Cosmos DB for NoSQL, consult [the Azure documentation](https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/ "https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/").

## Configuring Azure Cosmos DB connections

To connect to Azure Cosmos DB from AWS Glue, you will need to create and store your Azure Cosmos DB Key
in a AWS Secrets Manager secret, then associate that secret with a Azure Cosmos DB AWS Glue connection.

**Prerequisites:**

- In Azure, you will need to identify or generate an Azure Cosmos DB Key for use by AWS Glue, `cosmosKey`. For more information,
  see [Secure access to data in Azure Cosmos DB](https://learn.microsoft.com/en-us/azure/cosmos-db/secure-access-to-data?tabs=using-primary-key "https://learn.microsoft.com/en-us/azure/cosmos-db/secure-access-to-data?tabs=using-primary-key") in the
  Azure documentation.

###### To configure a connection to Azure Cosmos DB:

1. In AWS Secrets Manager, create a secret using your Azure Cosmos DB Key.
   To create a secret in Secrets Manager, follow the tutorial available in [Create an AWS Secrets Manager secret](../../../secretsmanager/latest/userguide/create_secret.md "../../../secretsmanager/latest/userguide/create_secret.md") in the AWS Secrets Manager documentation.
   After creating the secret, keep the Secret name, `secretName` for the next step.
   - When selecting **Key/value pairs**, create a pair for
     the key `spark.cosmos.accountKey` with the value `cosmosKey`.

2. In the AWS Glue console, create a connection by following the steps in [Adding an AWS Glue connection](console-connections.md "console-connections.md").
   After creating the connection, keep the connection name, `connectionName`, for future use in AWS Glue.
   - When selecting a **Connection type**, select Azure Cosmos DB.
   - When selecting an **AWS Secret**, provide `secretName`.

After creating a AWS Glue Azure Cosmos DB connection, you will need to perform the following steps before running your AWS Glue job:

- Grant the IAM role associated with your AWS Glue job permission to read `secretName`.
- In your AWS Glue job configuration, provide `connectionName` as an **Additional network connection**.

## Reading from Azure Cosmos DB for NoSQL containers

**Prerequisites:**

- A Azure Cosmos DB for NoSQL container you would like to read from. You will need identification information for the container.

An Azure Cosmos for NoSQL container is identified by its database and container. You must
provide the database, `cosmosDBName`, and container, `cosmosContainerName`, names when connecting to the Azure Cosmos for NoSQL API.

- A AWS Glue Azure Cosmos DB connection configured to provide auth and network location information. To acquire this, complete the steps in the previous procedure, _To configure a connection to Azure Cosmos DB_. You will need the name of the AWS Glue connection,
  `connectionName`.

For example:

```
azurecosmos_read = glueContext.create_dynamic_frame.from_options(
    connection_type="azurecosmos",
    connection_options={
    "connectionName": `connectionName`,
    "spark.cosmos.database": `cosmosDBName`,
    "spark.cosmos.container": `cosmosContainerName`,
    }
)
```

You can also provide a SELECT SQL query, to filter the results returned to your DynamicFrame. You will need to configure `query`.

For example:

```
azurecosmos_read_query = glueContext.create_dynamic_frame.from_options(
    connection_type="azurecosmos",
    connection_options={
        "connectionName": "`connectionName`",
        "spark.cosmos.database": `cosmosDBName`,
        "spark.cosmos.container": `cosmosContainerName`,
        "spark.cosmos.read.customQuery": "`query`"
    }
)
```

## Writing to Azure Cosmos DB for NoSQL containers

This example writes information from an existing DynamicFrame, `dynamicFrame` to
Azure Cosmos DB. If the container already has information, AWS Glue will append data from your DynamicFrame. If the information in the
container has a different schema from the information you write, you will run into errors.

**Prerequisites:**

- A Azure Cosmos DB table you would like to write to. You will need identification information for the container. **You must create the
  container before calling the connection method.**

An Azure Cosmos for NoSQL container is identified by its database and container. You must
provide the database, `cosmosDBName`, and container, `cosmosContainerName`, names when connecting to the Azure Cosmos for NoSQL API.

- A AWS Glue Azure Cosmos DB connection configured to provide auth and network location information. To acquire this, complete the steps in the previous procedure, _To configure a connection to Azure Cosmos DB_. You will need the name of the AWS Glue connection,
  `connectionName`.

For example:

```
azurecosmos_write = glueContext.write_dynamic_frame.from_options(
    frame=`dynamicFrame`,
    connection_type="azurecosmos",
    connection_options={
    "connectionName": `connectionName`,
    "spark.cosmos.database": `cosmosDBName`,
    "spark.cosmos.container": `cosmosContainerName`
)
```

## Azure Cosmos DB connection option reference

- `connectionName` — Required. Used for Read/Write. The name of a AWS Glue Azure Cosmos DB
  connection configured to provide auth and network location information to your connection method.
- `spark.cosmos.database` — Required. Used for Read/Write. Valid Values: database names. Azure Cosmos DB for NoSQL database name.
- `spark.cosmos.container` — Required. Used for Read/Write. Valid Values: container names. Azure Cosmos DB for NoSQL container name.
- `spark.cosmos.read.customQuery` — Used for Read. Valid Values: SELECT SQL queries. Custom query to select documents to be read.
