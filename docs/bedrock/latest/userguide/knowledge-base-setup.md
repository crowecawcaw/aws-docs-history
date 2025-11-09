# Prerequisites for using a vector store you created for a

knowledge base

To store the vector embeddings that your documents are converted to, you use a vector
store. Amazon Bedrock Knowledge Bases supports a quick-create flow for some of the vector stores, so if you prefer
for Amazon Bedrock to automatically create a vector index for you in one of those vector stores, skip
this prerequisite and proceed to [Create a knowledge base by connecting to a data source in Amazon Bedrock Knowledge Bases](knowledge-base-create.md "knowledge-base-create.md").

If you want to store binary vector embeddings instead of the standard floating-point
(float32) vector embeddings, then you must use a vector store that supports binary vectors.

###### Note

Amazon OpenSearch Serverless and Amazon OpenSearch Managed clusters are the only vector stores that support
storing binary vectors.

You can set up your own supported vector store to index the vector embeddings
representation of your data. You create fields for the following data:

- A field for the vectors generated from the text in your data source by the
  embeddings model that you choose.
- A field for the text chunks extracted from the files in your data source.
- Fields for source files metadata that Amazon Bedrock manages.
- (If you use an Amazon Aurora database and want to set up [filtering on metadata](kb-test-config.md "kb-test-config.md")) Fields for metadata that
  you associate with your source files. If you plan to set up filtering in other
  vector stores, you don't have to set up these fields for filtering.
  You can encrypt third-party vector stores with a KMS key. For more information, see
  [Encryption
  of knowledge base resources](encryption-kb.md "encryption-kb.md").

Select the tab corresponding to the vector store service that you will use to create your
vector index.

###### Note

Your choice of embeddings model and vector dimensions can affect the available vector
store choices. If you are not able to use your preferred vector store, choose compatible
options the embeddings model and vector dimensions.

Amazon OpenSearch Serverless

1. To configure permissions and create a vector search collection in
   Amazon OpenSearch Serverless in the AWS Management Console, follow steps 1 and 2 at [Working with vector search collections](../../../opensearch-service/latest/developerguide/serverless-vector-search.md "../../../opensearch-service/latest/developerguide/serverless-vector-search.md") in the
   Amazon OpenSearch Service Developer Guide. Note the following considerations while setting up your
   collection:
   1. Give the collection a name and description of your
      choice.
   2. To make your collection private, select **Standard
      create** for the **Security**
      section. Then, in the **Network access
      settings** section, select
      **VPC** as the **Access
      type** and choose a VPC endpoint. For more
      information about setting up a VPC endpoint for an Amazon OpenSearch Serverless
      collection, see [Access Amazon OpenSearch Serverless using an interface endpoint
      (AWS PrivateLink)](../../../opensearch-service/latest/developerguide/serverless-vpc.md "../../../opensearch-service/latest/developerguide/serverless-vpc.md") in the Amazon OpenSearch Service Developer Guide.

2. Once the collection is created, take note of the **Collection
   ARN** for when you create the knowledge base.
3. In the left navigation pane, select
   **Collections** under
   **Serverless**. Then select your vector search
   collection.
4. Select the **Indexes** tab. Then choose
   **Create vector index**.
5. In the **Vector index details** section, enter a
   name for your index in the **Vector index name**
   field.
6. In the **Vector fields** section, choose
   **Add vector field**. Amazon Bedrock stores the vector
   embeddings for your data source in this field. Provide the following
   configurations:
   - **Vector field name** –
     Provide a name for the field (for example,
     `embeddings`).
   - **Engine** – The vector
     engine used for search. Select
     **faiss**.
   - **Dimensions** – The number
     of dimensions in the vector. Refer to the following table to
     determine how many dimensions the vector should contain:

   | Model                         | Dimensions          |
   | ----------------------------- | ------------------- |
   | Titan G1 Embeddings<br>• Text | 1,536               |
   | Titan V2 Embeddings<br>• Text | 1,024, 512, and 256 |
   | Cohere Embed English          | 1,024               |
   | Cohere Embed Multilingual     | 1,024               |
   - **Distance metric** – The
     metric used to measure the similarity between vectors. We
     recommend using **Euclidean** for floating-point
     vector embeddings.

7. Expand the **Metadata management** section and
   add two fields to configure the vector index to store additional
   metadata that a knowledge base can retrieve with vectors. The following
   table describes the fields and the values to specify for each
   field:

| Field description                                                                         | Mapping field                                            | Data type | Filterable |
| ----------------------------------------------------------------------------------------- | -------------------------------------------------------- | --------- | ---------- |
| Amazon Bedrock chunks the raw text from your data and stores<br>the chunks in this field. | Name of your choice (for example,<br>`text`)             | String    | True       |
| Amazon Bedrock stores metadata related to your knowledge base<br>in this field.           | Name of your choice (for example,<br>`bedrock-metadata`) | String    | False      |

8. Take note of the names you choose for the vector index name, vector
   field name, and metadata management mapping field names for when you
   create your knowledge base. Then choose
   **Create**.

After the vector index is created, you can proceed to [create your knowledge base](knowledge-base-create.md "knowledge-base-create.md"). The
following table summarizes where you will enter each piece of information that
you took note of.

| Field                                      | Corresponding field in knowledge base setup (Console) | Corresponding field in knowledge base setup (API) | Description                                                                         |
| ------------------------------------------ | ----------------------------------------------------- | ------------------------------------------------- | ----------------------------------------------------------------------------------- |
| Collection ARN                             | Collection ARN                                        | collectionARN                                     | The Amazon Resource Name (ARN) of the vector search<br>collection.                  |
| Vector index name                          | Vector index name                                     | vectorIndexName                                   | The name of the vector index.                                                       |
| Vector field name                          | Vector field                                          | vectorField                                       | The name of the field in which to store vector embeddings for<br>your data sources. |
| Metadata management (first mapping field)  | Text field                                            | textField                                         | The name of the field in which to store the raw text from<br>your data sources.     |
| Metadata management (second mapping field) | Bedrock-managed metadata field                        | metadataField                                     | The name of the field in which to store metadata that Amazon Bedrock<br>manages.    |

For more detailed documentation on setting up a vector store in Amazon OpenSearch Serverless, see
[Working with vector search collections](../../../opensearch-service/latest/developerguide/serverless-vector-search.md "../../../opensearch-service/latest/developerguide/serverless-vector-search.md") in the
Amazon OpenSearch Service Developer Guide.

Amazon OpenSearch Service Managed Clusters

###### Important

- Before using any domain resources in OpenSearch Managed clusters, you need
  to configure certain IAM access permissions and policies. For more information,
  see [Prerequisites and permissions required for using
  OpenSearch Managed Clusters with Amazon Bedrock Knowledge Bases](kb-osm-permissions-prereq.md "kb-osm-permissions-prereq.md").
- If you encounter data ingestion failures, it might
  indicate insufficient OpenSearch domain capacity. To resolve this issue, increase your
  domain's capacity by provisioning higher IOPS and by increasing the throughput settings.
  For more information, see [Operational
  best practices for Amazon OpenSearch Service](../../../opensearch-service/latest/developerguide/bp.md "../../../opensearch-service/latest/developerguide/bp.md").

1. To create a domain and vector index in OpenSearch Cluster in the
   AWS Management Console, follow the steps described in [Creating and managing OpenSearch Service domains](../../../opensearch-service/latest/developerguide/createupdatedomains.md "../../../opensearch-service/latest/developerguide/createupdatedomains.md") in the
   _Amazon OpenSearch Service Developer Guide_.

Note the following considerations while setting up your domain:

    1. Give the domain a name of your choice.
    2. We recommend that you use the **Easy create**
     option to get started quickly with creating your domain.


    ###### Note

    This option gives you a domain with a low throughput. If you
     have larger workloads that require a higher throughput, choose the
     **Standard Create** option. You can adjust the
     capacity later as required. With this option, you
     can start with the lowest capacity, which can then be
     modified later as needed.
    3. For Network, you must choose **Public
     access**. OpenSearch domains that are behind a VPC
     are not supported for your Knowledge Base.
    4. For **Version**, if you're using binary vector
     embeddings, Amazon Bedrock Knowledge Bases requires an Engine version of 2.16 or later. In addition,
     a version of 2.13 or higher is required to create a k-nn index. For
     more information, see [K-NN Search](../../../opensearch-service/latest/developerguide/knn.md "../../../opensearch-service/latest/developerguide/knn.md")
     in the *Amazon OpenSearch Service developer guide*.
    5. We recommend that you use the **Dual-stack
     mode**.
    6. We recommend that you enable **Fine-grained access
     control** to protect the data in your domain, and
     further control the permissions that grants your Knowledge base
     service role access to the OpenSearch domain and make
     requests.
    7. Leave all other settings to their default values and choose
     **Create** to create your domain.

2. Once the domain is created, click it to take note of the
   **Domain ARN** and **Domain
   endpoint** for when you create the knowledge base.
3. After you've created the domain, you can create a vector index by running the
   following commands on an OpenSearch dashboard or using curl commands. For more
   information, see the
   [OpenSearch
   documentation](https://opensearch.org/docs/latest/search-plugins/knn/knn-index/ "https://opensearch.org/docs/latest/search-plugins/knn/knn-index/").

When running the command:

    * Provide a name for the vector field (for example,
     `embeddings`).
    * Make sure that the vector used for search is **faiss**.
     **nmslib** is not supported.
    * For the number of dimensions in the vector, refer to the following table to
     determine how many dimensions the vector should contain:


    ###### Note

    The Titan V2 Embeddings - Text model supports multiple dimensions. It
     can also be 256 or 512.




    | Model | Dimensions |
    | --- | --- |
    | Titan G1 Embeddings<br>• Text | 1,536 |
    | Titan V2 Embeddings<br>• Text | 1,024, 512, and 256 |
    | Cohere Embed English | 1,024 |
    | Cohere Embed Multilingual | 1,024 |
    * You can add two fields to configure the vector index to store additional
     metadata that a knowledge base can retrieve with vectors. The following
     table describes the fields and the values to specify for each of them.




    | Field description | Mapping field |
    | --- | --- |
    | Amazon Bedrock chunks the raw text from your data and stores<br>the chunks in this field. | Specified as an object, for example,<br>`AMAZON_BEDROCK_TEXT_CHUNK`. |
    | Amazon Bedrock stores metadata related to your knowledge base<br>in this field. | Specified as an object, for example,<br>`AMAZON_BEDROCK_METADATA`. |

```
PUT /`<index-name>`
{
    "settings": {
        "index": {
            "knn": true
        }
    },
    "mappings": {
        "properties": {
            "`<vector-name>`": {
                "type": "knn_vector",
                "dimension": `<embedding-dimension>`,
                "data_type": "binary",          # Only needed for binary embeddings
                "space_type": "l2" | "hamming", # Use l2 for float embeddings and hamming for binary embeddings
                "method": {
                    "name": "hnsw",
                    "engine": "faiss",
                    "parameters": {
                        "ef_construction": 128,
                        "m": 24
                    }
                }
            },

            "AMAZON_BEDROCK_METADATA": {
                "type": "text",
                "index": "false"
            },
            "AMAZON_BEDROCK_TEXT_CHUNK": {
                "type": "text",
                "index": "true"
            }
        }
    }
}
```

4. Take note of the domain ARN and endpoint, and the
   names you choose for the vector index name, vector
   field name, and metadata management mapping field names for when you
   create your knowledge base.

After the vector index is created, you can proceed to [create your knowledge base](knowledge-base-create.md "knowledge-base-create.md"). The
following table summarizes where you will enter each piece of information that
you took note of.

| Field                                      | Corresponding field in knowledge base setup (Console) | Corresponding field in knowledge base setup (API) | Description                                                                         |
| ------------------------------------------ | ----------------------------------------------------- | ------------------------------------------------- | ----------------------------------------------------------------------------------- |
| Domain ARN                                 | Domain ARN                                            | domainARN                                         | The Amazon Resource Name (ARN) of the OpenSearch<br>domain.                         |
| Domain endpoint                            | Domain endpoint                                       | domainEndpoint                                    | The endpoint to connect to the OpenSearch domain.                                   |
| Vector index name                          | Vector index name                                     | vectorIndexName                                   | The name of the vector index.                                                       |
| Vector field name                          | Vector field                                          | vectorField                                       | The name of the field in which to store vector embeddings for<br>your data sources. |
| Metadata management (first mapping field)  | Text field                                            | textField                                         | The name of the field in which to store the raw text from<br>your data sources.     |
| Metadata management (second mapping field) | Bedrock-managed metadata field                        | metadataField                                     | The name of the field in which to store metadata that Amazon Bedrock<br>manages.    |

Amazon S3 Vectors
Amazon S3 Vectors provides cost-effective vector storage in Amazon S3 that can be used to store and query
vector data. It provides durable and elastic storage of large vector datasets with
sub-second query performance. Amazon S3 Vectors is best suited for infrequent query workloads, and can
help reduce costs when used in retrieval augmented generation (RAG) and semantic search applications.

###### Important

The Amazon S3 Vectors integration with Amazon Bedrock Knowledge Bases is in preview release
and is subject to change.

Amazon S3 Vectors introduces S3 vector buckets, which you can query based on semantic meaning and
similarity. It can be used to deliver sub-second query response times and reduce costs while storing,
accessing, and querying vector data at scale without provisioning any infrastructure. Inside a
vector bucket, you can organize your vector data within vector indexes. Your vector bucket can have
multiple vector indexes, and each vector index can hold millions of vectors. For more information,
see [Amazon S3 Vectors](../../../AmazonS3/latest/userguide/s3-vectors.md "../../../AmazonS3/latest/userguide/s3-vectors.md")
in the _Amazon S3 User Guide_.

###### Note

- You can create a knowledge base for Amazon S3 Vectors in all AWS Regions where both Amazon Bedrock and
  Amazon S3 Vectors are available. For information about regional availability of Amazon S3 Vectors, see
  [Amazon S3 Vectors](../../../AmazonS3/latest/userguide/s3-vectors.md "../../../AmazonS3/latest/userguide/s3-vectors.md")
  in the _Amazon S3 User Guide_.
- When creating a knowledge base for Amazon S3 Vectors, hierarchical chunking is not supported. For information about chunking strategies, see [How content chunking works for knowledge bases](kb-chunking.md "kb-chunking.md").

###### Metadata support

After creating a vector index, when adding vector data to the index, you can attach
metadata as key-value pairs to each vector. By default, all metadata attached to a vector
is filterable and can be used as filters in a similarity search query. The filterable metadata can
be used to filter incoming queries based on a set of conditions, such as dates, categories,
or user preferences.

You can also configure the metadata to be non-filterable when creating the vector index. Amazon S3 vector
indexes support string, boolean, and number types. It can support up to a maximum of 40 KB of metadata
for each vector. Within this 40 KB of metadata, the filterable metadata can be up to a maximum of 2 KB
for each vector. By default, the filterable metadata also includes system metadata and chunk text so if you require additional space for the user metadata, you must configure it as non-filterable. The filterable metadata space can be used to store the embeddings after the knowledge
base has been created.

If the metadata exceeds any of these limits, it results in an error when creating the vector index.
For more information, see [Amazon S3 Vectors](../../../AmazonS3/latest/userguide/s3-vectors.md "../../../AmazonS3/latest/userguide/s3-vectors.md") in the _Amazon S3 User
Guide_.

###### Required permissions

Make sure that your IAM policy allows Amazon Bedrock to access your vector index in S3 vector bucket.
For more information about the required permissions, see [Create a service role for Amazon Bedrock Knowledge Bases](kb-permissions.md "kb-permissions.md").

###### Create S3 vector bucket and index

To use Amazon S3 Vectors with your knowledge base, you need to create an S3 vector bucket and
a vector index. You can create a vector bucket and index using the Amazon S3 console, AWS CLI, or
AWS SDK. For detailed instructions, see [Create a vector index](../../../AmazonS3/latest/userguide/s3-vectors-index-create.md "../../../AmazonS3/latest/userguide/s3-vectors-index-create.md") in
the _Amazon S3 User Guide_.

Note the following considerations when creating your vector bucket and index in the
[Amazon S3 console](https://console.aws.amazon.com/s3/vector-buckets# "https://console.aws.amazon.com/s3/vector-buckets#").

1. When creating your S3 vector bucket, take note of the following considerations.
   - Provide a unique **Vector bucket name**.
   - (Optional) Amazon S3 will automatically encrypt the data using the default
     **Server-side encryption with Amazon S3 managed keys (SSE-S3)**.
     You can choose whether to use this default encryption, or the
     **Server-side encryption with AWS Key Management Service keys (SSE-KMS)**
     instead.

   ###### Note

   The encryption type can't be changed once the vector bucket has been
   created.

   For step-by-step instructions, see [Encryption
   with AWS KMS keys](../../../AmazonS3/latest/userguide/s3-vectors-bucket-encryption.md "../../../AmazonS3/latest/userguide/s3-vectors-bucket-encryption.md").

2. Once you've created the S3 vector bucket, take note of the **Amazon Resource
   Name (ARN)** of the vector bucket for when you create the knowledge base.
3. Choose the vector bucket that you created and then create a vector index. When creating
   the vector index, take note of the following considerations.
   - **Vector index name** –
     Provide a name for the field (for example,
     `embeddings`).
   - **Dimension** – The number
     of dimensions in the vector. The dimensions must be a value between
     1 and 4096. Refer to the following table to
     determine how many dimensions the vector should contain based on your
     selection of the embeddings model:

   | Model                         | Dimensions          |
   | ----------------------------- | ------------------- |
   | Titan G1 Embeddings<br>• Text | 1,536               |
   | Titan V2 Embeddings<br>• Text | 1,024, 512, and 256 |
   | Cohere Embed English          | 1,024               |
   | Cohere Embed Multilingual     | 1,024               |
   - ###### Note

   Amazon S3 Vectors only support floating-point embeddings. Binary
   embeddings are not supported.

   **Distance metric** – The
   metric used to measure the similarity between vectors.
   You can use **Cosine** or **Euclidean**.

4. Expand the **Additional settings** and provide any
   non-filterable metadata in the **Non-filterable metadata**
   field.

###### Note

If you expect your text chunks to exceed the 2 KB metadata space,
we recommend that you add the text field `AMAZON_BEDROCK_TEXT`
and `AMAZON_BEDROCK_METADATA` as non-filterable metadata keys. Your knowledge base will use these fields
to store the text chunks and system metadata.

You can configure up to a maximum of 10 non-filterable metadata keys.
Choose **Add key** and then add `AMAZON_BEDROCK_TEXT`
and `AMAZON_BEDROCK_METADATA` as keys. 5. Create the vector index and take note of the **Amazon Resource
Name (ARN)** of the vector index for when you create the knowledge base.

###### Create knowledge base for S3 vector bucket

After you've gathered this information, you can proceed to [create your knowledge base](knowledge-base-create.md "knowledge-base-create.md").
When creating your knowledge base with S3 vector bucket, you'll need to provide the ARN of the vector bucket and
the vector index. The vector index will store the embeddings that's generated from your data sources.
The following table summarizes where you will enter each piece of information:

| Field             | Corresponding field in knowledge base setup (Console) | Corresponding field in knowledge base setup (API) | Description                                                                   |
| ----------------- | ----------------------------------------------------- | ------------------------------------------------- | ----------------------------------------------------------------------------- |
| Vector bucket ARN | S3 vector bucket ARN                                  | vectorBucketArn                                   | The Amazon Resource Name (ARN) of your S3 vector bucket.                      |
| Vector index ARN  | S3 vector index ARN                                   | vectorIndexARN                                    | The Amazon Resource Name (ARN) of the vector index for your S3 vector bucket. |

Amazon Aurora (RDS)

1. Create an Amazon Aurora database (DB) cluster, schema, and table by
   following the steps at [Using Aurora PostgreSQL as a knowledge base](../../../AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.md "../../../AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.md"). When you create
   the table, configure it with the following columns and data types. You
   can use column names of your liking instead of the ones listed in the
   following table. Take note of the column names you choose so that you
   can provide them during knowledge base setup.

You must provide these fields before creating the knowledge base.
They connot be updated once the knowledge base has been created.

###### Important

The Aurora cluster must reside in the same AWS account as the one
where the knowledge base is created for Amazon Bedrock.

| Column name     | Data type        | Corresponding field in knowledge base setup<br>(Console) | Corresponding field in knowledge base setup<br>(API) | Description                                                                                                                                      |
| --------------- | ---------------- | -------------------------------------------------------- | ---------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| id              | UUID primary key | Primary key                                              | `primaryKeyField`                                    | Contains unique identifiers for each record.                                                                                                     |
| embedding       | Vector           | Vector field                                             | `vectorField`                                        | Contains the vector embeddings of the data<br>sources.                                                                                           |
| chunks          | Text             | Text field                                               | `textField`                                          | Contains the chunks of raw text from your data<br>sources.                                                                                       |
| metadata        | JSON             | Bedrock-managed metadata field                           | `metadataField`                                      | Contains metadata required to carry out source<br>attribution and to enable data ingestion and<br>querying                                       |
| custom_metadata | JSONB            | Custom metadata field                                    | `customMetadataField`                                | Optional field that indicates the column where Amazon Bedrock<br>will write all the information of any metadata files from<br>your data sources. |

2. You must create an index on the columns vector and text for your
   text and embeddings fields. If you're using the custom metadata field,
   you must also create a GIN index on this column. GIN indexes can be used
   to efficiently search for key-value pairs in jsonb documents for metadata
   filtering. For more information, see [jsonb
   indexing](https://www.postgresql.org/docs/current/datatype-json.html#JSON-INDEXING "https://www.postgresql.org/docs/current/datatype-json.html#JSON-INDEXING") in the _PostgreSQL documentation_.

| Column name     | Create index on                                                                             | Required?                                            |
| --------------- | ------------------------------------------------------------------------------------------- | ---------------------------------------------------- |
| embedding       | `CREATE INDEX ON bedrock_integration.bedrock_kb USING hnsw (embedding vector_cosine_ops);`  | Yes                                                  |
| chunks          | `CREATE INDEX ON bedrock_integration.bedrock_kb USING gin (to_tsvector('simple', chunks));` | Yes                                                  |
| custom metadata | `CREATE INDEX ON bedrock_integration.bedrock_kb USING gin (custom_metadata);`               | Only if you have created the custom metadata column. |

###### Note

For improving hybrid search accuracy and latency with English content, consider using the 'english' dictionary instead of 'simple':

```
CREATE INDEX ON bedrock_integration.bedrock_kb USING gin (to_tsvector('english', chunks));
```

3. (Optional) If you [added metadata to
   your files for filtering](kb-test-config.md "kb-test-config.md"), we recommend that you provide the column
   name in the custom metadata field to store all your metadata in a single column.
   During [data ingestion](kb-data-source-sync-ingest.md "kb-data-source-sync-ingest.md"), this
   column will be populated with all the information in the metadata files from
   your data sources. If you choose to provide this field, you must create a GIN
   index on this column.

###### Note

If you frequently use range filters over numerical metadata, then to optimize
performance, create an index for the specific key. For example, if you use filters
such as `"lessThan": { "key": "year", "value": 1989 }`, create an expression
index on the `year` key. For more information, see [Indexes on
expressions](https://www.postgresql.org/docs/current/indexes-expressional.html "https://www.postgresql.org/docs/current/indexes-expressional.html") in the _PostgreSQL documentation_.

```
CREATE INDEX ON your_table ((custom_metadata->>'year')::double precision
```

Alternatively, if you don't provide this field name, you can create a column for
each metadata attribute in your files and specify the data type (text,
number, or boolean). For example, if the attribute `genre`
exists in your data source, you would add a column named
`genre` and specify `text` as the data type. During
[data ingestion](kb-data-source-sync-ingest.md "kb-data-source-sync-ingest.md"), these
separate columns will be populated with the corresponding attribute values. 4. Configure an AWS Secrets Manager secret for your Aurora DB cluster by following
the steps at [Password management with Amazon Aurora and AWS Secrets Manager](../../../AmazonRDS/latest/AuroraUserGuide/rds-secrets-manager.md "../../../AmazonRDS/latest/AuroraUserGuide/rds-secrets-manager.md"). 5. Take note of the following information after you create your DB
cluster and set up the secret.

| Field in knowledge base setup (Console) | Field in knowledge base setup (API) | Description                                                   |
| --------------------------------------- | ----------------------------------- | ------------------------------------------------------------- |
| Amazon Aurora DB Cluster ARN            | resourceArn                         | The ARN of your DB cluster.                                   |
| Database name                           | databaseName                        | The name of your database                                     |
| Table name                              | tableName                           | The name of the table in your DB cluster                      |
| Secret ARN                              | credentialsSecretArn                | The ARN of the AWS Secrets Manager key for your DB<br>cluster |

Neptune Analytics graphs (GraphRAG)

1. To create a graph and vector store in Neptune Analytics in the
   AWS Management Console, follow the steps described in [Vector
   indexing in Neptune Analytics](../../../neptune-analytics/latest/userguide/vector-index.md "../../../neptune-analytics/latest/userguide/vector-index.md") in the _Neptune
   Analytics User Guide_.

###### Note

To use Neptune GraphRAG, create an empty Neptune
Analytics graph with a vector search index. The vector search index
can only be created when the graph is created. When you create a
[Neptune Analytics graph in the console](../../../neptune-analytics/latest/userguide/create-graph-using-console.md "../../../neptune-analytics/latest/userguide/create-graph-using-console.md"), you specify the
index dimension under **Vector search settings**
near the end of the process.

Note the following considerations while creating the graph:

    1. Give the graph a name of your choice.
    2. Under **Data source**, choose
     **Create empty graph**, and specify the
     number of m-NCUs to be allocated. Each m-NCU has around one GiB
     of memory capacity and corresponding compute and
     networking.


    ###### Note

    The capacity of your graph can be modified later. We recommend
     that you start with the smallest instance and later choose a
     different instance, if needed.
    3. You can leave the default network connectivity settings. Amazon Bedrock will create a
     networking connection to the Neptune Analytics graph that you associate the
     knowledge base with. You do not have to configure public connectivity or private
     endpoints for your graph.
    4. Under **Vector search settings**, choose
     **Use vector dimension** and specify the
     number of dimensions in each vector.


    ###### Note

    The number of dimensions in each vector must match the
     vector dimensions in the embeddings model. Refer to the
     following table to determine how many dimensions the vector
     should contain:




    | Model | Dimensions |
    | --- | --- |
    | Titan G1 Embeddings<br>• Text | 1,536 |
    | Titan V2 Embeddings<br>• Text | 1,024, 512, and 256 |
    | Cohere Embed English | 1,024 |
    | Cohere Embed Multilingual | 1,024 |
    5. Leave all other settings to their default and create the
     graph.

2. Once the graph is created, click it to take note of the
   **Resource ARN** and **Vector
   dimensions** for when you create the knowledge base.
   When choosing the embeddings model in Amazon Bedrock, make sure that you choose
   a model with the same dimensions as the **Vector
   dimensions** you configured on your Neptune Analytics graph.

After the vector index is created, you can proceed to [create your knowledge base](knowledge-base-create.md "knowledge-base-create.md"). The
following table summarizes where you will enter each piece of information that
you took note of.

| Field                                      | Corresponding field in knowledge base setup (Console) | Corresponding field in knowledge base setup (API) | Description                                                                                                                                            |
| ------------------------------------------ | ----------------------------------------------------- | ------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Graph ARN                                  | Neptune Analytics Graph ARN                           | graphARN                                          | The Amazon Resource Name (ARN) of the Neptune Analytics<br>graph.                                                                                      |
| Metadata management (first mapping field)  | Text field name                                       | textField                                         | The name of the field in which to store the raw text from<br>your data sources. You can provide any value for this field, for<br>example, _text_.      |
| Metadata management (second mapping field) | Bedrock-managed metadata field                        | metadataField                                     | The name of the field in which to store metadata that Amazon Bedrock<br>manages. You can provide any value for this field, for example,<br>_metadata_. |

Pinecone

###### Note

If you use Pinecone, you agree to authorize AWS to access the
designated third-party source on your behalf in order to provide vector
store services to you. You're responsible for complying with any third-party
terms applicable to use and and transfer of data from the third-party
service.

For detailed documentation on setting up a vector store in Pinecone, see
[Pinecone as a
knowledge base for Amazon Bedrock](https://docs.pinecone.io/docs/amazon-bedrock "https://docs.pinecone.io/docs/amazon-bedrock").

While you set up the vector store, take note of the following information,
which you will fill out when you create a knowledge base:

- **Endpoint URL** – The endpoint URL for your index management page.
- **Credentials secret ARN** – The
  Amazon Resource Name (ARN) of the secret that you created in AWS Secrets Manager that contains the username and password for a database user.
- **(Optional) Customer-managed KMS key for your
  Credentials secret ARN** – if you encrypted your
  credentials secret ARN, provide the KMS key so that Amazon Bedrock can decrypt it.
- **Name Space** – (Optional) The namespace to be used to write new data to your database. For more information, see [Using namespaces](https://docs.pinecone.io/docs/namespaces "https://docs.pinecone.io/docs/namespaces").

There are additional configurations that you must provide when creating a
Pinecone index:

- **Text field name** – The name of
  the field which Amazon Bedrock should store the raw chunk text in.
- **Metadata field name** – The name
  of the field which Amazon Bedrock should store source attribution
  metadata in.

To access your Pinecone index, you must provide your Pinecone API key to
Amazon Bedrock through the AWS Secrets Manager.

###### To set up a secret for your Pinecone configuration

1. Follow the steps at [Create an AWS Secrets Manager secret](../../../secretsmanager/latest/userguide/create_secret.md "../../../secretsmanager/latest/userguide/create_secret.md"), setting the key as
   `apiKey` and the value as the API key to access your
   Pinecone index.
2. To find your API key, open your [Pinecone console](https://app.pinecone.io/ "https://app.pinecone.io/") and select **API
   Keys**.
3. After you create the secret, take note of the ARN of the
   KMS key.
4. Attach permissions to your service role to decrypt the ARN of the
   KMS key by following the steps in [Permissions to decrypt an AWS Secrets Manager secret for the vector store containing your knowledge base](encryption-kb.md#encryption-kb-3p "encryption-kb.md#encryption-kb-3p").
5. Later, when you create your knowledge base, enter the ARN in the
   **Credentials secret ARN** field.

Redis Enterprise Cloud

###### Note

If you use Redis Enterprise Cloud, you agree to authorize AWS to access the designated
third-party source on your behalf in order to provide vector store services
to you. You're responsible for complying with any third-party terms
applicable to use and transfer of data from the third-party service.

For detailed documentation on setting up a vector store in Redis Enterprise Cloud, see [Integrating Redis Enterprise Cloud with Amazon Bedrock](https://docs.redis.com/latest/rc/cloud-integrations/aws-marketplace/aws-bedrock/ "https://docs.redis.com/latest/rc/cloud-integrations/aws-marketplace/aws-bedrock/").

While you set up the vector store, take note of the following information,
which you will fill out when you create a knowledge base:

- **Endpoint URL** – The public
  endpoint URL for your database.
- **Vector index name** – The name of
  the vector index for your database.
- **Vector field** – The name of the
  field where the vector embeddings will be stored. Refer to the following
  table to determine how many dimensions the vector should contain.

| Model                         | Dimensions          |
| ----------------------------- | ------------------- |
| Titan G1 Embeddings<br>• Text | 1,536               |
| Titan V2 Embeddings<br>• Text | 1,024, 512, and 256 |
| Cohere Embed English          | 1,024               |
| Cohere Embed Multilingual     | 1,024               |

- **Text field** – The name of the
  field where the Amazon Bedrock stores the chunks of raw text.
- **Bedrock-managed metadata field**
  – The name of the field where Amazon Bedrock stores metadata related to your
  knowledge base.

To access your Redis Enterprise Cloud cluster, you must provide your Redis Enterprise Cloud security
configuration to Amazon Bedrock through the AWS Secrets Manager.

###### To set up a secret for your Redis Enterprise Cloud configuration

1. Enable TLS to use your database with Amazon Bedrock by following the steps at
   [Transport Layer Security (TLS)](https://docs.redis.com/latest/rc/security/database-security/tls-ssl/ "https://docs.redis.com/latest/rc/security/database-security/tls-ssl/").
2. Follow the steps at [Create an AWS Secrets Manager secret](../../../secretsmanager/latest/userguide/create_secret.md "../../../secretsmanager/latest/userguide/create_secret.md"). Set up the following keys with
   the appropriate values from your Redis Enterprise Cloud configuration in the
   secret:
   - `username` – The username to access your
     Redis Enterprise Cloud database. To find your username, look under the
     **Security** section of your database in
     the [Redis
     Console](http://app.redislabs.com/ "http://app.redislabs.com/").
   - `password` – The password to access your
     Redis Enterprise Cloud database. To find your password, look under the
     **Security** section of your database in
     the [Redis
     Console](http://app.redislabs.com/ "http://app.redislabs.com/").
   - `serverCertificate` – The content of the
     certificate from the Redis Cloud Certificate authority. Download
     the server certificate from the Redis Admin Console by following
     the steps at [Download certificates](https://docs.redis.com/latest/rc/security/database-security/tls-ssl/#download-certificates "https://docs.redis.com/latest/rc/security/database-security/tls-ssl/#download-certificates").
   - `clientPrivateKey` – The private key of the
     certificate from the Redis Cloud Certificate authority. Download
     the server certificate from the Redis Admin Console by following
     the steps at [Download certificates](https://docs.redis.com/latest/rc/security/database-security/tls-ssl/#download-certificates "https://docs.redis.com/latest/rc/security/database-security/tls-ssl/#download-certificates").
   - `clientCertificate` – The public key of the
     certificate from the Redis Cloud Certificate authority. Download
     the server certificate from the Redis Admin Console by following
     the steps at [Download certificates](https://docs.redis.com/latest/rc/security/database-security/tls-ssl/#download-certificates "https://docs.redis.com/latest/rc/security/database-security/tls-ssl/#download-certificates").

3. After you create the secret, take note of its ARN. Later, when you
   create your knowledge base, enter the ARN in the **Credentials
   secret ARN** field.

MongoDB Atlas

###### Note

If you use MongoDB Atlas, you agree to authorize AWS to access the designated
third-party source on your behalf in order to provide vector store services
to you. You're responsible for complying with any third-party terms
applicable to use and and transfer of data from the third-party
service.

For detailed documentation on setting up a vector store in MongoDB Atlas, see [Launch a Fully Managed RAG Workflow With MongoDB Atlas and Amazon Bedrock](https://www.mongodb.com/developer/products/atlas/rag-workflow-with-atlas-amazon-bedrock/ "https://www.mongodb.com/developer/products/atlas/rag-workflow-with-atlas-amazon-bedrock/").

When you set up the vector store, note the following information which you
will add when you create a knowledge base:

- **Endpoint URL** – The endpoint URL
  of your MongoDB Atlas cluster.
- **Database name** – The name of the
  database in your MongoDB Atlas cluster.
- **Collection name** – The name of
  the collection in your database.
- **Credentials secret ARN** – The
  Amazon Resource Name (ARN) of the secret that you created in AWS Secrets Manager that contains the username and password for a database user in
  your MongoDB Atlas cluster. The secret must contain keys named `username` and `password`.
- **(Optional) Customer-managed KMS key for your
  Credentials secret ARN** – if you encrypted your
  credentials secret ARN, provide the KMS key so that Amazon Bedrock can decrypt it.

There are additional configurations for **Field mapping**
that you must provide when creating a MongoDB Atlas index:

- **Vector index name** – The name of
  the MongoDB Atlas Vector Search Index on your collection.
- **Vector field name** – The name of
  the field which Amazon Bedrock should store vector embeddings in.
- **Text field name** – The name of
  the field which Amazon Bedrock should store the raw chunk text in.
- **Metadata field name** – The name
  of the field which Amazon Bedrock should store source attribution
  metadata in.
- **(Optional) Text search index name** –
  The name of the MongoDB Atlas Search index on your collection.

###### Important

If you plan to use metadata filtering with your MongoDB Atlas knowledge base, you must manually configure filters in your vector index. Metadata filtering doesn't work by default and requires additional setup in your MongoDB Atlas vector index configuration.

(Optional) To have Amazon Bedrock connect to your MongoDB Atlas cluster over AWS PrivateLink, see [RAG workflow with MongoDB Atlas using Amazon Bedrock](https://www.mongodb.com/developer/products/atlas/rag-workflow-with-atlas-amazon-bedrock/ "https://www.mongodb.com/developer/products/atlas/rag-workflow-with-atlas-amazon-bedrock/").
