# Modify a data source for your Amazon Bedrock knowledge base

You can update a data source for your knowledge base, such as changing the data source configurations.

You can update a data source in the following ways:

- Add, change, or remove files or content from the the data source.
- Change the data source configurations, or the KMS key to use for encrypting transient data
  during data ingestion. If you change the source or endpoint configuration details, you should
  update or create a new IAM role with the required access permissions and Secrets Manager secret
  (if applicable).
- Set your data source deletion policy is to either "Delete" or "Retain".
  You can delete all data from your data source that’s converted
  into vector embeddings upon deletion of a knowledge base or data source resource.
  You can retain all data from your data source that’s converted
  into vector embeddings upon deletion of a knowledge base or data source resource.
  Note that the **vector store itself is not deleted**
  if you delete a knowledge base or data source resource.
  Each time you add, modify, or remove files from your data source, you must sync the data source so that it is re-indexed to the knowledge base. Syncing is incremental, so Amazon Bedrock only processes added, modified, or deleted documents since the last sync. Before you begin ingestion, check that your data source fulfills the following conditions:

- The files are in supported formats. For more information,
  see [Support document formats](knowledge-base-ds.md#kb-ds-supported-doc-formats-limits "knowledge-base-ds.md#kb-ds-supported-doc-formats-limits").
- The files don't exceed the **Ingestion job file size** specified in [Amazon Bedrock endpoints and quotas](../../../general/latest/gr/bedrock.md "../../../general/latest/gr/bedrock.md") in the AWS General Reference.
- If your data source contains metadata files, check the following conditions to ensure that the metadata files aren't ignored:

      + Each `.metadata.json` file shares the same file name and extension as the source file that it's associated with.
      + If the vector index for your knowledge base is in an Amazon OpenSearch Serverless vector store, check that the vector index is configured with the `faiss` engine. If the vector index is configured with the `nmslib` engine, you'll have to do one of the following:




      	- [Create a new knowledge base](knowledge-base-create.md "knowledge-base-create.md") in the console and let Amazon Bedrock automatically create a vector index in Amazon OpenSearch Serverless for you.
      	- [Create another vector index](knowledge-base-setup.md "knowledge-base-setup.md") in the vector store and select `faiss` as the **Engine**. Then [create a new knowledge base](knowledge-base-create.md "knowledge-base-create.md") and specify the new vector index.
      + If the vector index for your knowledge base is in an Amazon Aurora database cluster, we recommend that you use the custom metadata field to store all your metadata in a single column
       and create an index on this column. If you do not provide the custom metadata field, you must check that the table for your index contains a column for each metadata property in your
       metadata files before starting ingestion. For more information, see [Prerequisites for using a vector store you created for a
       knowledge base](knowledge-base-setup.md "knowledge-base-setup.md").

  To learn how to update a data source, choose the tab for your preferred method, and then follow the steps:

Console

###### To update a data source

1. Sign in to the AWS Management Console with an IAM identity that has permissions to use the Amazon Bedrock console. Then, open the Amazon Bedrock console at
   [https://console.aws.amazon.com/bedrock](https://console.aws.amazon.com/bedrock "https://console.aws.amazon.com/bedrock").
2. In the left navigation pane, choose **Knowledge bases**.
3. Select the name of your knowledge base.
4. In the **Data source** section, select the radio button next to the data source that you want edit and sync.
5. (Optional) Choose **Edit**, change your configurations, and select **Submit**.
   If you change the source or endpoint configuration details, you should
   update or create a new IAM role with the required access permissions and Secrets Manager secret
   (if applicable). Alos, note that can't change the chunking configurations that are based on the original data ingested.
   You must re-create the data source.

###### Note

You can't change the chunking configurations. You must re-create the data source. 6. (Optional) Choose to edit your data source data deletion policy as part of the advanced settings:

For data deletion policy settings, you can choose either:

    * Delete: Deletes all data from your data source that’s converted
     into vector embeddings upon deletion of a knowledge base or data source resource.
     Note that the **vector store itself is not deleted**,
     only the data. This flag is ignored if an AWS account is deleted.
    * Retain: Retains all data from your data source that’s converted
     into vector embeddings upon deletion of a knowledge base or data source resource.
     Note that the **vector store itself is not deleted**
     if you delete a knowledge base or data source resource.

7. Choose **Sync**.
8. A green banner appears when the sync is complete and the **Status** becomes **Ready**.

API

###### To update a data source

1. (Optional) Send an [UpdateDataSource](../APIReference/API_agent_UpdateDataSource.md "../APIReference/API_agent_UpdateDataSource.md") request with a [Agents for Amazon Bedrock build-time endpoint](../../../general/latest/gr/bedrock.md#bra-bt "../../../general/latest/gr/bedrock.md#bra-bt"), changing any configurations
   and specifying the same configurations you don't want to change. If you change the source
   or endpoint configuration details, you should
   update or create a new IAM role with the required access permissions and Secrets Manager secret
   (if applicable).

###### Note

You can't change the `chunkingConfiguration`. Send the request with the
existing `chunkingConfiguration`, or re-create the data source. 2. (Optional) Change the `dataDeletionPolicy` for your data source. You can
`DELETE` all data from your data source that’s converted
into vector embeddings upon deletion of a knowledge base or data source resource.
This flag is ignored if an AWS account is deleted. You can `RETAIN`
all data from your data source that’s converted into vector embeddings upon deletion
of a knowledge base or data source resource. Note that the **vector
store itself is not deleted** if you delete a knowledge base or data
source resource. 3. Send a [StartIngestionJob](../APIReference/API_agent_StartIngestionJob.md "../APIReference/API_agent_StartIngestionJob.md") request with a [Agents for Amazon Bedrock build-time endpoint](../../../general/latest/gr/bedrock.md#bra-bt "../../../general/latest/gr/bedrock.md#bra-bt"), specifying the `dataSourceId`
and the `knowledgeBaseId`.
