

# Creating a Azure Cosmos DB target node
<a name="creating-azurecosmos-target-node"></a>

## Prerequisites needed
<a name="creating-azurecosmos-target-node-prerequisites"></a>
+ A AWS Glue Azure Cosmos DB connection, configured with an AWS Secrets Manager secret, as described in the previous section, [Creating a Azure Cosmos DB connection](creating-azurecosmos-connection.md).
+ Appropriate permissions on your job to read the secret used by the connection.
+ A Azure Cosmos DB table you would like to write to. You will need identification information for the container. **You must create the container before calling the connection method.**

  An Azure Cosmos for NoSQL container is identified by its database and container. You must provide the database, {{cosmosDBName}}, and container, {{cosmosContainerName}}, names when connecting to the Azure Cosmos for NoSQL API.

## Adding a Azure Cosmos DB data target
<a name="creating-azurecosmos-target-node-add"></a>

**To add a **Data target – Azure Cosmos DB** node:**

1.  Choose the connection for your Azure Cosmos DB data source. Since you have created it, it should be available in the dropdown. If you need to create a connection, choose **Create Azure Cosmos DB connection**. For more information see the previous section, [Creating a Azure Cosmos DB connection](creating-azurecosmos-connection.md). 

    Once you have chosen a connection, you can view the connection properties by clicking **View properties**. 

1. Choose **Cosmos DB Database Name** – provide the name of the database you want to read from, {{cosmosDBName}}.

1. Choose **Azure Cosmos DB Container** – provide the name of the container you want to read from, {{cosmosContainerName}}.

1.  In **Custom Azure Cosmos properties**, enter parameters and values as needed. 