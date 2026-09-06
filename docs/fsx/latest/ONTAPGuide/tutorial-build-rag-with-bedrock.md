

# Build a RAG application using Amazon Bedrock Knowledge Bases
<a name="tutorial-build-rag-with-bedrock"></a>

Many enterprises accumulate large repositories of documents on their NFS and SMB file shares — product manuals, policy documents, contracts, research reports, engineering specifications, and user-generated content.

With an Amazon S3 access point attached to the FSx for ONTAP volume, Amazon Bedrock Knowledge Bases ingests content directly from the volume. Foundation-model responses are grounded in the documents where your teams save them over NFS or SMB. Content that writers update on the share becomes available to the knowledge base on the next sync.

In this tutorial, you upload a small set of sample PDFs to your FSx for ONTAP volume through an Amazon S3 access point, create a Amazon Bedrock knowledge base that points to the access point, ingest the documents, and run a question through the `RetrieveAndGenerate` API.

**Note**  
This tutorial takes approximately **35 to 45 minutes** to complete. The AWS services used incur charges for the resources you create. If you complete all the steps, including the **Clean up** section promptly, the expected cost is less than **$1** in the US East (N. Virginia) AWS Region. This estimate does not include ongoing charges for the FSx for ONTAP volume itself.

## Prerequisites
<a name="tutorial-bedrock-kb-prerequisites"></a>

Before you begin, make sure you have the following:
+ An FSx for ONTAP volume with an Amazon S3 access point attached. The access point must have an **internet** network origin so that the Amazon Bedrock service can reach it. For instructions on creating an access point, see [Creating an access point](fsxn-creating-access-points.md).
+ Model access enabled for an embedding model supported by Amazon Bedrock Knowledge Bases and at least one text generation model (for example, `amazon.nova-lite-v1:0`) in the AWS Region where you will create the knowledge base. This tutorial uses `amazon.titan-embed-text-v2:0` (1024 dimensions) as the embedding model; Cohere Embed models are also supported. If you choose a different embedding model, adjust the vector index dimension in Step 2 to match the model's output dimension. Model access is enabled in the Amazon Bedrock console under **Model access**. For more information, see [Access Amazon Bedrock foundation models](https://docs.aws.amazon.com/bedrock/latest/userguide/model-access.html) in the *Amazon Bedrock User Guide*.
+ AWS CLI version 2 installed and configured with credentials that can create IAM roles, Amazon S3 Vectors resources, and Amazon Bedrock Knowledge Bases.

## Step 1: Upload sample documents to the access point
<a name="tutorial-bedrock-kb-upload"></a>

Download a few public PDFs to use as a sample corpus, then upload them to your access point using the Amazon S3 access point alias.

1. Create a local directory and download sample PDFs.

   ```
   $ mkdir -p ~/kb-pdfs && cd ~/kb-pdfs
   curl -sSL -o aws-overview.pdf https://d1.awsstatic.com/whitepapers/aws-overview.pdf
   curl -sSL -o wellarchitected-framework.pdf https://docs.aws.amazon.com/pdfs/wellarchitected/latest/framework/wellarchitected-framework.pdf
   curl -sSL -o s3-userguide.pdf https://docs.aws.amazon.com/pdfs/AmazonS3/latest/userguide/s3-userguide.pdf
   ```

1. Upload each file to the access point. Replace {{access-point-alias}} with your access point alias (for example, `my-kb-ap-a1b2c3d4e5f6g7h8i9j0kl1mnop2uuse1a-ext-s3alias`). You can find the alias in the Amazon FSx console under **Attached Amazon S3 access points** for your volume, or by running `aws fsx describe-s3-access-point-attachments`.

   ```
   $ for f in *.pdf; do
       aws s3 cp "$f" "s3://{{access-point-alias}}/$f"
   done
   ```

1. Verify the files landed on the volume.

   ```
   $ aws s3 ls s3://{{access-point-alias}}/
   ```

**Note**  
Amazon Bedrock Knowledge Bases enforces a maximum file size of 50 MB per document. Files larger than 50 MB are skipped during ingestion.

## Step 2: Create a vector store
<a name="tutorial-bedrock-kb-vector-store"></a>

The knowledge base stores document embeddings in a vector store. Amazon Bedrock Knowledge Bases supports several vector stores; this tutorial uses Amazon S3 Vectors as the default because it is cost-optimized for RAG workloads and requires minimal setup. Amazon OpenSearch Serverless is also supported; see the collapsible section at the end of this step for those instructions.

### To create the vector store using the console
<a name="tutorial-bedrock-kb-vector-store-console"></a>

If you use the console to create the knowledge base in [Step 4: Create the knowledge base and data source](#tutorial-bedrock-kb-create-kb), choose **Quick create a new vector store** in the **Vector database** step, and select either **Amazon S3 Vectors** (recommended) or **Amazon OpenSearch Serverless**. Amazon Bedrock creates the vector store and all required configuration automatically. Skip ahead to [Step 3: Create an IAM role for the knowledge base](#tutorial-bedrock-kb-iam-role).

### To create an Amazon S3 Vectors vector store using the AWS CLI
<a name="tutorial-bedrock-kb-vector-store-cli"></a>

1. Create an Amazon S3 vector bucket. Vector bucket names follow the same global-uniqueness rules as standard Amazon S3 buckets. This tutorial uses `fsxn-kb-vectors`; replace with a unique name.

   ```
   $ aws s3vectors create-vector-bucket --vector-bucket-name fsxn-kb-vectors
   ```

1. Create a vector index in the bucket. The index dimension must match the output dimension of the embedding model; Titan Text Embeddings v2 outputs 1024 dimensions. The `nonFilterableMetadataKeys` setting marks the Bedrock metadata fields as non-filterable, which keeps them out of the 2 KB per-vector filterable metadata limit.

   ```
   $ aws s3vectors create-index --vector-bucket-name fsxn-kb-vectors \
       --index-name bedrock-kb-index \
       --dimension 1024 --distance-metric cosine --data-type float32 \
       --metadata-configuration '{"nonFilterableMetadataKeys":["AMAZON_BEDROCK_METADATA","AMAZON_BEDROCK_TEXT"]}'
   ```

   Note the `indexArn` in the response; you use it in [Step 4: Create the knowledge base and data source](#tutorial-bedrock-kb-create-kb).

### Alternative: Create an OpenSearch Service Serverless vector store using the AWS CLI
<a name="tutorial-bedrock-kb-vector-store-oss"></a>

If you prefer OpenSearch Service Serverless (for higher queries-per-second, advanced search features, or existing operational familiarity), use the following steps instead of the Amazon S3 Vectors procedure above.

1. Create encryption and network security policies for the collection.

   ```
   $ aws opensearchserverless create-security-policy --name kb-enc --type encryption \
       --policy '{"Rules":[{"ResourceType":"collection","Resource":["collection/fsxn-kb"]}],"AWSOwnedKey":true}'
   aws opensearchserverless create-security-policy --name kb-net --type network \
       --policy '[{"Rules":[{"ResourceType":"collection","Resource":["collection/fsxn-kb"]},{"ResourceType":"dashboard","Resource":["collection/fsxn-kb"]}],"AllowFromPublic":true}]'
   ```

1. Create a data access policy that grants the knowledge base role and your current user permission to read and write the collection. Replace {{account-id}} and {{current-user}} with your values.

   ```
   $ aws opensearchserverless create-access-policy --name kb-data --type data --policy '[{
       "Rules":[
           {"ResourceType":"index","Resource":["index/fsxn-kb/*"],"Permission":["aoss:*"]},
           {"ResourceType":"collection","Resource":["collection/fsxn-kb"],"Permission":["aoss:*"]}
       ],
       "Principal":[
           "arn:aws:iam::{{account-id}}:role/fsxn-kb-role",
           "arn:aws:iam::{{account-id}}:user/{{current-user}}"
       ]
   }]'
   ```

1. Create the collection and wait for it to become `ACTIVE`.

   ```
   $ aws opensearchserverless create-collection --name fsxn-kb --type VECTORSEARCH
   aws opensearchserverless batch-get-collection --names fsxn-kb \
       --query 'collectionDetails[0].{status:status,endpoint:collectionEndpoint}'
   ```

1. Create the vector index on the collection using a Python script with signed requests. The index must use dimension 1024 (for Titan Text Embeddings v2) and field names that Amazon Bedrock Knowledge Bases expects. For the full script and subsequent configuration steps, see [Prerequisites for using OpenSearch Service Serverless](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-setup-oss.html) in the *Amazon Bedrock User Guide*. Use the resulting collection ARN and index name in Step 4 with a `storage-configuration` of type `OPENSEARCH_SERVERLESS`.

## Step 3: Create an IAM role for the knowledge base
<a name="tutorial-bedrock-kb-iam-role"></a>

The knowledge base needs an IAM role that it can assume to invoke the embedding model, read objects through the Amazon S3 access point, and access the vector store. The policy shown below grants access to an Amazon S3 Vectors vector store. If you use OpenSearch Service Serverless instead, replace the `S3Vectors` statement with one that grants `aoss:APIAccessAll` on the collection ARN.

### To create the role using the console
<a name="tutorial-bedrock-kb-iam-role-console"></a>

When you create the knowledge base using the Amazon Bedrock console in [Step 4: Create the knowledge base and data source](#tutorial-bedrock-kb-create-kb), choose **Create and use a new service role**. Amazon Bedrock creates a role with the required trust and permissions, scoped to your knowledge base, embedding model, vector store, and data source. Skip ahead to [Step 4: Create the knowledge base and data source](#tutorial-bedrock-kb-create-kb).

### To create the role using the AWS CLI
<a name="tutorial-bedrock-kb-iam-role-cli"></a>

1. Save the following trust policy as `kb-trust-policy.json`. It allows Amazon Bedrock to assume the role. Replace {{account-id}} with your AWS account ID.

   ```
   {
       "Version": "2012-10-17", 		 	 	 
       "Statement": [{
           "Effect": "Allow",
           "Principal": {"Service": "bedrock.amazonaws.com"},
           "Action": "sts:AssumeRole",
           "Condition": {"StringEquals": {"aws:SourceAccount": "{{account-id}}"}}
       }]
   }
   ```

1. Save the following permissions policy as `kb-permissions.json`. It grants access to the embedding model, the Amazon S3 access point, and the vector store. Replace the placeholders with your values.

   ```
   {
       "Version": "2012-10-17", 		 	 	 
       "Statement": [
           {
               "Sid": "FoundationModel",
               "Effect": "Allow",
               "Action": ["bedrock:InvokeModel"],
               "Resource": ["arn:aws:bedrock:{{region}}::foundation-model/amazon.titan-embed-text-v2:0"]
           },
           {
               "Sid": "S3AccessPoint",
               "Effect": "Allow",
               "Action": ["s3:GetObject", "s3:ListBucket"],
               "Resource": [
                   "arn:aws:s3:{{region}}:{{account-id}}:accesspoint/{{access-point-name}}",
                   "arn:aws:s3:{{region}}:{{account-id}}:accesspoint/{{access-point-name}}/object/*"
               ]
           },
           {
               "Sid": "S3Vectors",
               "Effect": "Allow",
               "Action": [
                   "s3vectors:GetIndex",
                   "s3vectors:PutVectors",
                   "s3vectors:GetVectors",
                   "s3vectors:ListVectors",
                   "s3vectors:DeleteVectors",
                   "s3vectors:QueryVectors"
               ],
               "Resource": [
                   "arn:aws:s3vectors:{{region}}:{{account-id}}:bucket/fsxn-kb-vectors",
                   "arn:aws:s3vectors:{{region}}:{{account-id}}:bucket/fsxn-kb-vectors/index/*"
               ]
           }
       ]
   }
   ```

1. Create the role and attach the permissions policy.

   ```
   $ aws iam create-role --role-name fsxn-kb-role \
       --assume-role-policy-document file://kb-trust-policy.json
   aws iam put-role-policy --role-name fsxn-kb-role --policy-name kb-access \
       --policy-document file://kb-permissions.json
   ```

## Step 4: Create the knowledge base and data source
<a name="tutorial-bedrock-kb-create-kb"></a>

The data source points at your Amazon S3 access point alias. Amazon Bedrock Knowledge Bases accepts the access point alias in place of a bucket name.

### To create the knowledge base using the console
<a name="tutorial-bedrock-kb-create-kb-console"></a>

1. Open the Amazon Bedrock console at [https://console.aws.amazon.com/bedrock/](https://console.aws.amazon.com/bedrock/).

1. In the left navigation pane, choose **Knowledge bases**, and then choose **Create knowledge base**.

1. Under **Knowledge base details**, enter a name (for example, `fsxn-kb`) and description.

1. Under **IAM permissions**, choose **Create and use a new service role**.

1. For **Data source**, choose **Amazon S3**, and then choose **Next**.

1. Enter a data source name (for example, `fsxn-s3ap-source`).

1. For **S3 URI**, enter `s3://` followed by your access point alias, for example `s3://my-kb-ap-a1b2c3d4e5f6g7h8i9j0kl1mnop2uuse1a-ext-s3alias`. The console does not distinguish between a bucket name and an access point alias in this field; the access point alias is accepted as-is.

1. Choose **Next**.

1. Under **Embeddings model**, choose **Titan Text Embeddings v2**.

1. Under **Vector database**, choose **Quick create a new vector store** and select **Amazon S3 Vectors**. Choose **Next**.

1. Review the configuration and choose **Create knowledge base**. The knowledge base can take several minutes to create.

### To create the knowledge base using the AWS CLI
<a name="tutorial-bedrock-kb-create-kb-cli"></a>

1. Create the knowledge base. Replace the placeholders with your values. The `indexArn` is the ARN of the Amazon S3 vector index you created in Step 2.

   ```
   $ aws bedrock-agent create-knowledge-base --name fsxn-kb \
       --role-arn arn:aws:iam::{{account-id}}:role/fsxn-kb-role \
       --knowledge-base-configuration '{
           "type":"VECTOR",
           "vectorKnowledgeBaseConfiguration":{
               "embeddingModelArn":"arn:aws:bedrock:{{region}}::foundation-model/amazon.titan-embed-text-v2:0"
           }
       }' \
       --storage-configuration '{
           "type":"S3_VECTORS",
           "s3VectorsConfiguration":{
               "indexArn":"{{index-arn}}"
           }
       }'
   ```

   Note the `knowledgeBaseId` in the response.

1. Create the data source. Pass the Amazon S3 access point alias as the bucket name in the `bucketArn` field, using the form `arn:aws:s3:::{{access-point-alias}}`.

   ```
   $ aws bedrock-agent create-data-source \
       --knowledge-base-id {{knowledge-base-id}} \
       --name fsxn-s3ap-source \
       --data-source-configuration '{
           "type":"S3",
           "s3Configuration":{"bucketArn":"arn:aws:s3:::{{access-point-alias}}"}
       }'
   ```

   Note the `dataSourceId` in the response.

## Step 5: Ingest the documents
<a name="tutorial-bedrock-kb-ingest"></a>

Run an ingestion job to crawl the documents through the access point, generate embeddings, and index them in the vector store.

### To run ingestion using the console
<a name="tutorial-bedrock-kb-ingest-console"></a>

1. In the Amazon Bedrock console, open your knowledge base.

1. In the **Data source** section, select your data source, and then choose **Sync**.

1. Wait for **Sync status** to show **Ready**.

### To run ingestion using the AWS CLI
<a name="tutorial-bedrock-kb-ingest-cli"></a>

1. Start the ingestion job.

   ```
   $ aws bedrock-agent start-ingestion-job \
       --knowledge-base-id {{knowledge-base-id}} \
       --data-source-id {{data-source-id}}
   ```

   Note the `ingestionJobId` in the response.

1. Poll the job until it completes.

   ```
   $ aws bedrock-agent get-ingestion-job \
       --knowledge-base-id {{knowledge-base-id}} \
       --data-source-id {{data-source-id}} \
       --ingestion-job-id {{ingestion-job-id}}
   ```

   The `status` field transitions from `IN_PROGRESS` to `COMPLETE`. The `statistics` field shows how many documents were scanned and indexed.

## Step 6: Query the knowledge base
<a name="tutorial-bedrock-kb-query"></a>

Ask the knowledge base a question grounded in the ingested documents. The response includes citations that reference the source documents through the Amazon S3 access point alias.

### To query using the console
<a name="tutorial-bedrock-kb-query-console"></a>

1. In the Amazon Bedrock console, open your knowledge base.

1. Choose **Test knowledge base**.

1. Under **Generate responses**, select a text generation model (for example, **Nova Lite**).

1. Enter a question such as `What are the pillars of the AWS Well-Architected Framework?` and choose **Run**. The answer displays with citation references that link to the source documents in the Amazon S3 access point.

### To query using the AWS CLI
<a name="tutorial-bedrock-kb-query-cli"></a>

Use the `retrieve-and-generate` command. Replace the placeholders with your values. The `modelArn` must refer to an inference profile for a text generation model to which you have access.

```
$ aws bedrock-agent-runtime retrieve-and-generate \
    --input '{"text":"What are the pillars of the AWS Well-Architected Framework?"}' \
    --retrieve-and-generate-configuration '{
        "type":"KNOWLEDGE_BASE",
        "knowledgeBaseConfiguration":{
            "knowledgeBaseId":"{{knowledge-base-id}}",
            "modelArn":"arn:aws:bedrock:{{region}}:{{account-id}}:inference-profile/us.amazon.nova-lite-v1:0"
        }
    }'
```

The response contains the generated answer in `output.text` and a list of citations in the `citations` array. Each citation includes an `s3Location.uri` field that points to the source document through the access point alias, in the form `s3://{{access-point-alias}}/{{file.pdf}}`.

## Troubleshooting
<a name="tutorial-bedrock-kb-troubleshooting"></a>

Ingestion job reports files were ignored  
Amazon Bedrock Knowledge Bases enforces a maximum file size of 50 MB per document. Files larger than 50 MB are listed in `failureReasons` and skipped. Split or compress large documents before uploading.

`ValidationException`: model marked as Legacy  
The text generation model you specified has been deprecated for your account. Choose an active inference profile, such as `us.amazon.nova-lite-v1:0` or another currently supported model. Run `aws bedrock list-inference-profiles` to list available profiles.

`AccessDeniedException` during ingestion  
Verify that the knowledge base IAM role has `s3:GetObject` and `s3:ListBucket` on the access point ARN (not on the underlying volume) and that the access point has an internet network origin so that the Amazon Bedrock service can reach it. If you chose the OpenSearch Service Serverless alternative in Step 2, also verify that the data access policy lists the role as a principal.

Ingestion job succeeds but queries return no relevant passages  
Confirm that the vector index was created with `dimension: 1024` (for Titan Text Embeddings v2) and that the field names in the index mapping match the field names configured on the knowledge base.

## Clean up
<a name="tutorial-bedrock-kb-clean-up"></a>

To avoid ongoing charges, delete the resources you created:
+ Amazon Bedrock knowledge base and data source
+ Amazon S3 vector index and vector bucket (or OpenSearch Service Serverless collection, if you used the alternative in Step 2)
+ IAM role and inline policy
+ Objects uploaded to the access point (if no longer needed)

```
$ aws bedrock-agent delete-data-source --knowledge-base-id {{knowledge-base-id}} --data-source-id {{data-source-id}}
aws bedrock-agent delete-knowledge-base --knowledge-base-id {{knowledge-base-id}}
aws s3vectors delete-index --vector-bucket-name fsxn-kb-vectors --index-name bedrock-kb-index
aws s3vectors delete-vector-bucket --vector-bucket-name fsxn-kb-vectors
aws iam delete-role-policy --role-name fsxn-kb-role --policy-name kb-access
aws iam delete-role --role-name fsxn-kb-role
```

### Alternative: Clean up OpenSearch Service Serverless resources
<a name="tutorial-bedrock-kb-clean-up-oss"></a>

If you chose the OpenSearch Service Serverless alternative in Step 2, replace the `s3vectors` commands above with the following. Idle OpenSearch Service Serverless collections accrue OCU-hour charges, so delete them promptly when you are done with the tutorial.

```
$ # Get the collection ID (required by delete-collection; the name is not accepted)
COLLECTION_ID=$(aws opensearchserverless batch-get-collection --names fsxn-kb \
    --query 'collectionDetails[0].id' --output text)

# Delete the collection, then the policies
aws opensearchserverless delete-collection --id "$COLLECTION_ID"
aws opensearchserverless delete-access-policy --name kb-data --type data
aws opensearchserverless delete-security-policy --name kb-net --type network
aws opensearchserverless delete-security-policy --name kb-enc --type encryption
```