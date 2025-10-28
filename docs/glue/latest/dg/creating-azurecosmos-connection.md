# Creating a Azure Cosmos DB connection

**Prerequisites**:

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
