

# Native multimodal processing
<a name="kb-managed-native-multimodal"></a>

With *native multimodal processing*, a managed Amazon Bedrock knowledge base sends each file directly to a multimodal embedding model. The model then creates embeddings from the raw image, audio, and video content.

Without a native multimodal embedding model, a knowledge base works differently. First it parses your files. Then it chunks the text that it extracts from them. Finally it embeds those chunks with a text embedding model.

Native multimodal processing skips parsing and text extraction. As a result, it keeps visual and audio detail that text extraction would lose.

To enable native multimodal processing, choose a native multimodal embedding model when you create the knowledge base. Currently, TwelveLabs Marengo Embed 3.0 (`twelvelabs.marengo-embed-3-0-v1:0`) is the only model that you can choose. For instructions on configuring it, see [Create a managed knowledge base](kb-managed-create.md).

## How native multimodal processing works
<a name="kb-managed-native-multimodal-how"></a>

When you configure a knowledge base with a native multimodal embedding model, the following applies:
+ **Only the `MULTI_MODAL_EMBEDDINGS` parsing strategy is supported.** You cannot combine a native multimodal embedding model with other parsing strategies.
+ **Files are sent directly to the embedding model.** The embedding model processes the raw file and produces embeddings from its native content.
+ **Text-based chunking strategies are not supported.** Because your files aren't parsed into text, the chunking strategies that apply to text, such as default chunking and fixed-size chunking, don't apply.
+ **You can configure segmentation for audio and video.** Instead of a text chunking strategy, you choose how the knowledge base splits audio and video files into segments. Use the segmentation settings in the `modelConfiguration` field. For more information, see [Create a managed knowledge base](kb-managed-create.md).
+ **Only the file types that the model supports are supported.** A knowledge base configured with a native multimodal embedding model can ingest only the file types that model accepts. For the file types and other settings that TwelveLabs Marengo Embed 3.0 supports, see [TwelveLabs Marengo Embed 3.0](model-parameters-marengo-3.md).
+ **You must provide a multimodal storage destination.** Provide an Amazon S3 location for the knowledge base to process and ingest your content. Amazon Bedrock Knowledge Bases creates an `aws/` prefix folder in your bucket. Use a different bucket from your data source bucket. For the permissions the service role needs, see [Permissions for your multimodal storage destination](kb-managed-permissions.md#kb-managed-permissions-multimodal-storage).
+ **Only the [Retrieve](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_Retrieve.html) API is supported.** You query a knowledge base that uses a native multimodal embedding model with the [Retrieve](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_Retrieve.html) operation. The [RetrieveAndGenerate](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_RetrieveAndGenerate.html) operation is not supported.
+ **Queries must be text.** You query your multimodal content by using text. Image queries are not supported.

For details about the metadata that the [Retrieve](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_Retrieve.html) operation returns for multimodal results, and how to fetch the matching file, see [Retrieve responses for native multimodal knowledge bases](kb-test-get-document-content.md#kb-get-doc-content-native-multimodal).

## How the knowledge base invokes the embedding model
<a name="kb-managed-native-multimodal-invocation"></a>

When you use a native multimodal embedding model, your knowledge base invokes that model both synchronously and asynchronously. It uses synchronous invocation when you submit a query, and asynchronous invocation when it ingests your content. Your service role needs permissions for both. For more information about the policy to attach, see [Permissions to access Amazon Bedrock models](kb-managed-permissions.md#kb-managed-permissions-access-models).

**Note**  
In some AWS Regions, the TwelveLabs Marengo Embed 3.0 model supports synchronous invocation only through an [inference profile](inference-profiles-support.md). Asynchronous invocation still uses the on-demand model. In these Regions, specify an inference profile when you create the knowledge base. The knowledge base then uses both the inference profile and the on-demand model to process your content. Your service role needs permissions for both.

To check how TwelveLabs Marengo Embed 3.0 is supported in the AWS Region that you use, see [TwelveLabs Marengo Embed 3.0](model-parameters-marengo-3.md).

## Managing transient data with Amazon S3 lifecycle policies
<a name="kb-managed-native-multimodal-lifecycle"></a>

While Amazon Bedrock Knowledge Bases processes your content, it stores transient data in your multimodal storage destination. It attempts to delete that data when processing finishes. To ensure that the data expires, we recommend that you apply a lifecycle policy to the transient data path.

------
#### [ Console ]

**To create a lifecycle rule using the console**

1. Open the [Amazon S3 console](https://console.aws.amazon.com/s3).

1. Navigate to the multimodal storage destination that you configured for your knowledge base.

1. Choose the **Management** tab, and then choose **Create lifecycle rule**.

1. For **Lifecycle rule name**, enter **Transient Data Deletion**.

1. Under **Filter type**, choose **Limit the scope of this rule using one or more filters**.

1. For **Prefix**, enter the transient data path for your knowledge base and data source.

   Replace the placeholder values in the following prefix with your actual identifiers:

   ```
   aws/bedrock/knowledge_bases/{{knowledge-base-id}}/{{data-source-id}}/transient_data
   ```
**Don't delete multimodal content**  
Do not apply lifecycle policies to the entire bucket or to the `aws/` prefix, as this will delete your multimodal content and may cause processing failures. Only use the transient data path shown in the preceding prefix example.

1. Under **Lifecycle rule actions**, select **Expire current versions of objects**.

1. For **Days after object creation**, enter **1**.

1. Choose **Create rule**.

------
#### [ AWS CLI ]

**To create a lifecycle rule using the AWS CLI**

1. Create a JSON file named `lifecycle-policy.json` with the following content, replacing the placeholder values with your actual identifiers:
   + {{knowledge-base-id}} – Your knowledge base identifier
   + {{data-source-id}} – Your data source identifier

   ```
   {
       "Rules": [
           {
               "ID": "TransientDataDeletion",
               "Status": "Enabled",
               "Filter": {
                   "Prefix": "aws/bedrock/knowledge_bases/{{knowledge-base-id}}/{{data-source-id}}/transient_data"
               },
               "Expiration": {
                   "Days": 1
               }
           }
       ]
   }
   ```

1. Apply the lifecycle policy to your bucket. Replace {{amzn-s3-demo-bucket}} with the name of your multimodal storage bucket:

   ```
   aws s3api put-bucket-lifecycle-configuration \
       --bucket {{amzn-s3-demo-bucket}} \
       --lifecycle-configuration file://lifecycle-policy.json
   ```

1. Verify that the lifecycle policy was applied:

   ```
   aws s3api get-bucket-lifecycle-configuration \
       --bucket {{amzn-s3-demo-bucket}}
   ```

------

For more information about Amazon S3 lifecycle policies, see [Managing the lifecycle of objects](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html) in the *Amazon S3 User Guide*.