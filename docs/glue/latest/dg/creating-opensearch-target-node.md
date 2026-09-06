

# Creating a OpenSearch Service target node
<a name="creating-opensearch-target-node"></a>

## Prerequisites needed
<a name="creating-opensearch-target-node-prerequisites"></a>
+ A AWS Glue OpenSearch Service connection, configured with an AWS Secrets Manager secret, as described in the previous section, [Creating a OpenSearch Service connection](creating-opensearch-connection.md).
+ Appropriate permissions on your job to read the secret used by the connection.
+ A OpenSearch Service index you would like to write to, {{aosIndex}}.

## Adding a OpenSearch Service data target
<a name="creating-opensearch-target-node-add"></a>

**To add a **Data target – OpenSearch Service** node:**

1.  Choose the connection for your OpenSearch Service data source. Since you have created it, it should be available in the dropdown. If you need to create a connection, choose **Create OpenSearch Service connection**. For more information see the previous section, [Creating a OpenSearch Service connection](creating-opensearch-connection.md). 

    Once you have chosen a connection, you can view the connection properties by clicking **View properties**. 

1. Provide **Index**, the index you would like to read.

1.  In **Custom OpenSearch Service properties**, enter parameters and values as needed. 