

# Deploy streaming data vectorization blueprint
<a name="ai-vector-embedding-integration-deploy"></a>

This topic describes how to deploy a streaming data vectorization blueprint.

**Deploy streaming data vectorization blueprint**

1. Ensure following resources are setup correctly:

   1. Provisioned or Serverless MSK cluster with one or more topics containing data.

1. Bedrock Setup: [Access to desired Bedrock Model](https://docs.aws.amazon.com/bedrock/latest/userguide/model-access.html). Currently supported Bedrock models are:
   + Amazon Titan Embeddings G1 - Text
   + Amazon Titan Text Embeddings V2
   + Amazon Titan Multimodal Embeddings G1
   + Cohere Embed English
   + Cohere Embed Multilingual

1. AWS OpenSearch collection:
   + You may use a provisioned or Serverless OpenSearch Service collection.
   + The OpenSearch Service collection must have at least one index.
   + If you plan to use an **OpenSearch Serverless collection**, make sure to create a vector search collection. For details on how to setup a vector index, see [Prerequisites for your own vector store for a knowledge base](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-setup.html). To learn more about vectorization, see [Amazon OpenSearch Service’s vector database capabilities explained](https://aws.amazon.com/blogs/big-data/amazon-opensearch-services-vector-database-capabilities-explained/).
**Note**  
When creating a vector index, you must use the vector field name `embedded_data`.
   + If you plan to use an **OpenSearch Provisioned collection**, you need to add the MSF application role (that contains the Opensearch access policy) that was created by the blueprint, as a master user to your OpenSearch collection. Also, confirm that the access policy in OpenSearch is set to "Allow" actions. This is needed to [enable fine grain access control](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/fgac.html#fgac-enabling).
   + Optionally, you can enable access to the OpenSearch dashboard to view results. Refer to [enable fine grain access control](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/fgac.html#fgac-enabling).

1. Login using a role that allows [aws:CreateStack](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-action-createstack.html) permissions.

1. Go to the MSF console dashboard and select **Create Streaming Application**.

1. In **Choose a method to setup the stream processing application** select **Use a Blueprint**.

1. Select **Real-time AI application blueprint** from the blueprints drop-down menu.

1. Provide desired configurations. See [Create page configurations](#ai-vector-embedding-integration-create-page-configs).

1. Select **Deploy Blueprint** to start a CloudFormation deployment.

1. Once the CloudFormation deployment is complete, go to the deployed Flink application. Check Runtime properties of the application.

1. You can choose to change/add runtime properties to your application. See [Runtime Properties Configuration](https://docs.aws.amazon.com/managed-flink/latest/java/troubleshooting-blueprints.html) for details to configure these properties.
**Note**  
Note:  
If you are using OpenSearch provisioned, please ensure you enabled [fine grain access control](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/fgac.html#fgac-enabling).  
If your provisioned cluster is private, add `https://` to your OpenSearch Provisioned VPC endpoint URL and change `sink.os.endpoint` to point to this endpoint.  
If your provisioned cluster is public, ensure your MSF application can access the internet. For more information, see [>>>>>> express-brokers-publication-merge type="documentation" url="managed-flink/latest/java/vpc-internet.html" >Internet and service access for a VPC-connected Managed Service for Apache Flink application]().

1. Once you are satisfied with all the configurations, select `Run`. The application will start running.

1. Pump messages in your MSK cluster.

1. Navigate to the Opensearch cluster and go to the OpenSearch dashboard.

1. On the dashboard, select **Discover** in the left menu. You should see persisted documents along with their vector embeddings.

1. Refer to [Working with vector search collections](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-vector-search.html) to see how you can use the vectors stored in the index.

## Create page configurations
<a name="ai-vector-embedding-integration-create-page-configs"></a>

This topic describes create page configurations to refer to when specifying configurations for real-time AI application blueprints.

**Application name**  
Existing field in MSF, give any name to your application.

**MSK cluster**  
Select the MSK cluster you created during setup from the dropdown list.

**Topics**  
Add the name of the topic(s) which you created in the setup.

**Input stream data type**  
Choose **String** if you will supply string input to the MSK stream.  
Choose **JSON** if the input in the MSK stream is JSON. In **JSON keys embedded**, write the names of the fields in your input JSON whose value you want to send to Bedrock for generating embeddings.

**Bedrock embedding model**  
Select one from the list. Ensure that you have model access for the model you choose, otherwise the stack might fail. See [Add or remove access to Amazon Bedrock foundation models](https://docs.aws.amazon.com/bedrock/latest/userguide/model-access-modify.html).

**OpenSearch cluster**  
Select the cluster you created from the dropdown.

**OpenSearch vector index name**  
Select the vector index that you created in the above step.