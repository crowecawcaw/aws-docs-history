# Deploy streaming data vectorization blueprint

This topic describes how to deploy a streaming data vectorization blueprint.

###### Deploy streaming data vectorization blueprint

1. Ensure following resources are setup correctly:
   1. Provisioned or Serverless MSK cluster with one or more topics containing data.

2. Bedrock Setup: [Access to desired Bedrock Model](../../../bedrock/latest/userguide/model-access.md "../../../bedrock/latest/userguide/model-access.md"). Currently supported Bedrock models are:
   - Amazon Titan Embeddings G1 - Text
   - Amazon Titan Text Embeddings V2
   - Amazon Titan Multimodal Embeddings G1
   - Cohere Embed English
   - Cohere Embed Multilingual

3. AWS OpenSearch collection:
   - You may use a provisioned or Serverless OpenSearch Service collection.
   - The OpenSearch Service collection must have at least one index.
   - If you plan to use an **OpenSearch Serverless collection**, make sure to create a vector search collection. For details on how to setup a vector index, see [Prerequisites for your own vector store for a knowledge base](../../../bedrock/latest/userguide/knowledge-base-setup.md "../../../bedrock/latest/userguide/knowledge-base-setup.md"). To learn more about vectorization, see [Amazon OpenSearch Service’s vector database capabilities explained](https://aws.amazon.com/blogs/big-data/amazon-opensearch-services-vector-database-capabilities-explained/ "https://aws.amazon.com/blogs/big-data/amazon-opensearch-services-vector-database-capabilities-explained/").

   ###### Note

   When creating a vector index, you must use the vector field name `embedded_data`.
   - If you plan to use an **OpenSearch Provisioned collection**, you need to add the MSF application role (that contains the Opensearch access policy) that was created by the blueprint, as a master user to your OpenSearch collection. Also, confirm that the access policy in OpenSearch is set to "Allow" actions. This is needed to [enable fine grain access control](../../../opensearch-service/latest/developerguide/fgac.md#fgac-enabling "../../../opensearch-service/latest/developerguide/fgac.md#fgac-enabling").
   - Optionally, you can enable access to the OpenSearch dashboard to view results. Refer to [enable fine grain access control](../../../opensearch-service/latest/developerguide/fgac.md#fgac-enabling "../../../opensearch-service/latest/developerguide/fgac.md#fgac-enabling").

4. Login using a role that allows [aws:CreateStack](../../../systems-manager/latest/userguide/automation-action-createstack.md "../../../systems-manager/latest/userguide/automation-action-createstack.md") permissions.
5. Go to the MSF console dashboard and select **Create Streaming Application**.
6. In **Choose a method to setup the stream processing application** select **Use a Blueprint**.
7. Select **Real-time AI application blueprint** from the blueprints drop-down menu.
8. Provide desired configurations. See [Create page configurations](#ai-vector-embedding-integration-create-page-configs "#ai-vector-embedding-integration-create-page-configs").
9. Select **Deploy Blueprint** to start a CloudFormation deployment.
10. Once the CloudFormation deployment is complete, go to the deployed Flink application. Check Runtime properties of the application.
11. You can choose to change/add runtime properties to your application. See [Runtime Properties Configuration](../../../managed-flink/latest/java/troubleshooting-blueprints.md "../../../managed-flink/latest/java/troubleshooting-blueprints.md") for details to configure these properties.

###### Note

Note:

If you are using OpenSearch provisioned, please ensure you enabled [fine grain access control](../../../opensearch-service/latest/developerguide/fgac.md#fgac-enabling "../../../opensearch-service/latest/developerguide/fgac.md#fgac-enabling").

If your provisioned cluster is private, add `https://` to your OpenSearch Provisioned VPC endpoint URL and change `sink.os.endpoint` to point to this endpoint.

If your provisioned cluster is public, ensure your MSF application can access the internet. For more information, see >>>>>> express-brokers-publication-merge
type="documentation"
url="managed-flink/latest/java/vpc-internet.html"

> Internet and service access for a VPC-connected Managed Service for Apache Flink application. 12. Once you are satisfied with all the configurations, select `Run`. The application will start running. 13. Pump messages in your MSK cluster. 14. Navigate to the Opensearch cluster and go to the OpenSearch dashboard. 15. On the dashboard, select **Discover** in the left menu. You should see persisted documents along with their vector embeddings. 16. Refer to [Working with vector search collections](../../../opensearch-service/latest/developerguide/serverless-vector-search.md "../../../opensearch-service/latest/developerguide/serverless-vector-search.md") to see how you can use the vectors stored in the index.

## Create page configurations

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
Select one from the list. Ensure that you have model access for the model you choose, otherwise the stack might fail. See [Add or remove access to Amazon Bedrock foundation models](../../../bedrock/latest/userguide/model-access-modify.md "../../../bedrock/latest/userguide/model-access-modify.md").

**OpenSearch cluster**
Select the cluster you created from the dropdown.

**OpenSearch vector index name**
Select the vector index that you created in the above step.
