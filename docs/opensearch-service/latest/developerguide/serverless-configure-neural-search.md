

# Configure Neural Search and Hybrid Search on OpenSearch Serverless

## Neural Search
<a name="serverless-configure-neural-search-what-is"></a>

Amazon OpenSearch Serverless supports Neural Search functionality for semantic search operations on your data. Neural Search uses machine learning models to understand the semantic meaning and context of your queries, providing more relevant search results than traditional keyword-based searches. This section explains how to configure Neural Search in OpenSearch Serverless, including the required permissions, supported processors, and key differences from the standard OpenSearch implementation.

Semantic search in OpenSearch Serverless uses the following components:
+ Text embedding ingest pipeline processor
+ Neural query
+ Neural sparse query

To set up semantic search without creating ingest pipelines, use the `semantic` field type. For more information, see [Semantic field](#serverless-configure-neural-search-semantic-field).

## Hybrid Search
<a name="serverless-configure-hybrid-search"></a>

With hybrid search, you can improve search relevance by combining keyword and semantic search capabilities. To use hybrid search, create a search pipeline that processes your search results and combines document scores. For more information, see [Search pipelines](https://docs.opensearch.org/latest/search-plugins/search-pipelines/index/) on the *OpenSearch Documentation* website. Use the following components to implement hybrid search:
+ Normalization search pipeline processor

**Supported normalization techniques**
  + `min_max`
  + `l2`

**Supported combination techniques**
  + `arithmetic_mean`
  + `geometric_mean`
  + `harmonic_mean`

  For more information about normalization and combination techniques, see [Request body fields](https://docs.opensearch.org/latest/search-plugins/search-pipelines/normalization-processor/#request-body-fields) on the *OpenSearch Documentation* website.
+ Hybrid query

## Neural and hybrid queries
<a name="serverless-configure-neural-search-hybrid-queries"></a>

By default, OpenSearch calculates document scores using the keyword-based Okapi BM25 algorithm, which works well for search queries that contain keywords. Neural Search provides new query types for natural language queries and the ability to combine both semantic and keyword search.

**Example : `neural`**  

```JSON
"neural": {
  "{{vector_field}}": {
    "query_text": "{{query_text}}",
    "query_image": "{{image_binary}}",
    "model_id": "{{model_id}}",
    "k": 100
  }
}
```

For more information, see [Neural query](https://docs.opensearch.org/latest/query-dsl/specialized/neural/) on the *OpenSearch Documentation* website.

**Example : `hybrid`**  

```JSON
"hybrid": {
      "queries": [
        {{array of lexical, neural, or combined queries}}
      ]
    }
```

For more information, see [Hybrid query](https://docs.opensearch.org/latest/query-dsl/compound/hybrid/) on the *OpenSearch Documentation* website.

To configure semantic search components in Amazon OpenSearch Serverless, follow the steps in the [Neural Search tutorial](https://docs.opensearch.org/latest/tutorials/vector-search/neural-search-tutorial/) on the *OpenSearch Documentation* website. Keep in mind these important differences:
+ OpenSearch Serverless supports only remote models. You must configure connectors to remotely hosted models. For more information, see [Configure Machine Learning on Amazon OpenSearch Serverless](serverless-configure-machine-learning.md). To delete a deployed model, first undeploy it. For the required permissions, see [Delete models and connectors](serverless-configure-machine-learning.md#serverless-configure-machine-learning-delete).
+ Expect up to 15 seconds of latency when you search against your vector index or search for recently created search and ingest pipelines.

## Semantic field
<a name="serverless-configure-neural-search-semantic-field"></a>

The `semantic` field type is a high-level abstraction that simplifies setting up semantic and neural sparse search. It automatically enables semantic indexing and querying based on the ML model that you specify. When you index documents, OpenSearch Serverless generates the embeddings and stores them in a separate field. When you search, OpenSearch Serverless uses the same model to convert your query text.

To compare the `semantic` field with automatic semantic enrichment, see [Choosing between automatic semantic enrichment and the semantic field](serverless-semantic-enrichment.md#serverless-semantic-enrichment-vs-semantic-field).

The collection types that support the semantic field depend on the model:
+ For a dense embedding model, use a Vector Search collection. For more information, see [Working with vector search collections](serverless-vector-search.md).
+ For a sparse encoding model, use a Search, Time Series, or Vector Search collection. For more information, see [Creating collections](serverless-create.md).

### Model configuration
<a name="serverless-configure-neural-search-semantic-field-model"></a>

OpenSearch Serverless uses the model configuration to create the embedding field for a semantic field: a `knn_vector` field for a dense model or a `rank_features` field for a sparse model. The following table lists the required `model_config` fields for each model type.


| Model | `model_config.model_type` | Other required `model_config` fields | 
| --- | --- | --- | 
| Dense embedding model | TEXT\_EMBEDDING | embedding\_dimension – The number of dimensions in the embeddings that the model produces. additional\_config.space\_type – The distance metric used to compare vectors, for example, l2 or cosinesimil. | 
| Sparse encoding model | SPARSE\_ENCODING or SPARSE\_TOKENIZE | None | 

The `embedding_dimension` must match the vector dimension of the model. The `space_type` must match the distance metric that the model uses. OpenSearch Serverless reads these values from the model configuration when you create the mapping. You can't set them in the field mapping directly.

When you register a new model, include `model_config` in the register request, as shown in [Configuring a semantic field](#serverless-configure-neural-search-semantic-field-configure). If you already registered the model without a model configuration, add the configuration to the existing model instead of registering the model again. Add the configuration before you create the semantic field, because OpenSearch Serverless reads it when you create or update a mapping that uses the model. The update request contains only the `model_config` object.

To add a model configuration to a registered model, send the following request:

```json
PUT /_plugins/_ml/models/{{model-id}}
{
  "model_config": {
    "model_type": "TEXT_EMBEDDING",
    "embedding_dimension": 1024,
    "framework_type": "SENTENCE_TRANSFORMERS",
    "additional_config": {
      "space_type": "l2"
    }
  }
}
```
+ The `model-id` is the ID of the model that you registered.
+ The `embedding_dimension` is the number of dimensions in the embeddings that the model produces.
+ The `space_type` is the distance metric used to compare vectors, for example, `l2` or `cosinesimil`.

For more information, see [*Update Model API*](https://docs.opensearch.org/latest/ml-commons-plugin/api/model-apis/update-model/) on the *OpenSearch Documentation* website.

### Configuring a semantic field
<a name="serverless-configure-neural-search-semantic-field-configure"></a>

To configure a semantic field in an index, use the following steps.

**Prerequisites**
+ Create a collection of the type that your model requires.
+ Configure the permissions described in [Configure permissions](#serverless-configure-neural-search-permissions).

**To configure a semantic field**

1. Create a connector as described in [Configure Machine Learning on Amazon OpenSearch Serverless](serverless-configure-machine-learning.md).

1. The following OpenSearch REST API request registers and deploys an Amazon Titan Text Embeddings V2 model that returns vectors with 1,024 dimensions. Replace the {{placeholder values}} with your own information:

   ```json
   POST /_plugins/_ml/models/_register?deploy=true
   {
     "name": "{{my-embedding-model}}",
     "function_name": "remote",
     "connector_id": "{{connector-id}}",
     "model_config": {
       "model_type": "TEXT_EMBEDDING",
       "embedding_dimension": 1024,
       "framework_type": "SENTENCE_TRANSFORMERS",
       "additional_config": {
         "space_type": "l2"
       }
     }
   }
   ```
   + The `connector-id` is the ID of the connector that you created.
   + The `embedding_dimension` is the number of dimensions in the embeddings that the model produces.
   + The `space_type` is the distance metric used to compare vectors, for example, `l2` or `cosinesimil`.

1. The following OpenSearch REST API request creates an index containing a semantic field. For a dense model, set `index.knn` to `true`. You must define semantic fields explicitly in the mapping. Dynamic mapping doesn't create semantic fields. A semantic field can't be a multi-field.

   ```json
   PUT my-semantic-index
   {
     "settings": {
       "index.knn": true
     },
     "mappings": {
       "properties": {
         "passage": {
           "type": "semantic",
           "model_id": "{{model-id}}"
         }
       }
     }
   }
   ```
   + The `model-id` is the model ID returned by the Register Model API.

   Once you create the mapping, OpenSearch Serverless automatically adds a field named `passage_semantic_info` to store the generated embeddings. For a dense model, its `embedding` subfield is a `knn_vector` field with the dimension and space type from `model_config`. For a sparse model, the `embedding` subfield is a `rank_features` field. To verify the mapping, run a `GET my-semantic-index/_mapping` request.

   You can also define semantic fields with the Put Mapping API or in index templates and component templates. For more information, see [Put mapping](https://docs.opensearch.org/latest/api-reference/index-apis/put-mapping/) and [Index templates](https://docs.opensearch.org/latest/im-plugin/index-templates/) on the *OpenSearch Documentation* website.

1. Index documents containing `passage` fields. OpenSearch Serverless generates the embeddings automatically:

   ```json
   POST _bulk
   { "index": { "_index": "my-semantic-index" } }
   { "passage": "Alzheimer's disease is a progressive neurodegenerative disorder." }
   { "index": { "_index": "my-semantic-index" } }
   { "passage": "Parkinson's disease affects motor neurons over time." }
   ```

1. Use the `neural` query on a semantic field for both dense and sparse models. To search for specific text, provide the `query_text` in the `neural` query clause. You don't have to specify the model because the field references it:

   ```json
   POST my-semantic-index/_search
   {
     "query": {
       "neural": {
         "passage": {
           "query_text": "dementia and cognitive decline"
         }
       }
     }
   }
   ```

### Considerations
<a name="serverless-configure-neural-search-semantic-field-considerations"></a>
+ An index mapping can reference at most 10 unique model IDs.
+ If OpenSearch Serverless can't generate an embedding for a document, that document fails in the bulk response and isn't indexed. The other documents in the bulk request are indexed.
+ By default, OpenSearch Serverless doesn't return dense embeddings in `_source`. To return dense embeddings, add the embedding field to `includes`, for example, `"_source": { "includes": ["passage_semantic_info.embedding"] }`.

For all semantic field parameters, such as `raw_field_type` and `chunking`, see [Semantic field type](https://docs.opensearch.org/latest/mappings/supported-field-types/semantic/) on the *OpenSearch Documentation* website.

## Configure permissions
<a name="serverless-configure-neural-search-permissions"></a>

Semantic search in OpenSearch Serverless requires both an AWS Identity and Access Management (IAM) policy and a data access policy. The IAM policy lets you call the collection's OpenSearch APIs, and the data access policy controls the operations you can perform on indexes, pipelines, and models. For more information, see [Supported policy permissions](serverless-data-access.md#serverless-data-supported-permissions).

Attach the following IAM policy to the IAM role or user that creates connectors and models, indexes documents, and runs searches. Replace the {{placeholder values}} with your specific information:

**Example : Neural search IAM policy**  

```JSON
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "CollectionDataPlane",
            "Effect": "Allow",
            "Action": "aoss:APIAccessAll",
            "Resource": "arn:aws:aoss:{{region}}:{{account-id}}:collection/{{collection-id}}"
        },
        {
            "Sid": "PassConnectorRole",
            "Effect": "Allow",
            "Action": "iam:PassRole",
            "Resource": "arn:aws:iam::{{account-id}}:role/{{connector-role-name}}"
        }
    ]
}
```
+ `aoss:APIAccessAll` – Allows you to send OpenSearch API requests to the collection. Without it, every request to the collection endpoint fails with a 403 error, even if a data access policy grants you access.
+ `iam:PassRole` – Allows you to create a connector that uses the IAM role in the connector's `credential.roleArn`. You need this permission only to create connectors.
+ The `region` is the AWS Region of the collection.
+ The `account-id` is your AWS account ID.
+ The `collection-id` is the ID of the collection.
+ The `connector-role-name` is the name of the IAM role in the connector's `credential.roleArn`.

The following data access policy grants the permissions that semantic search requires. Replace the {{placeholder values}} with your specific information:

**Example : Data access policy**  

```JSON
[
    {
        "Description": "Index permissions",
        "Rules": [
            {
                "ResourceType": "index",
                "Resource": ["index/{{collection-name}}/*"],
                "Permission": [
                  "aoss:CreateIndex", 
                  "aoss:DescribeIndex",
                  "aoss:UpdateIndex",
                  "aoss:DeleteIndex",
                  "aoss:ReadDocument",
                  "aoss:WriteDocument"
                ]
            }
        ],
        "Principal": [
            "arn:aws:iam::{{account-id}}:role/{{role-name}}"
        ]
    },
    {
        "Description": "Pipeline permissions",
        "Rules": [
            {
                "ResourceType": "collection",
                "Resource": ["collection/{{collection-name}}"],
                "Permission": [
                  "aoss:CreateCollectionItems",
                  "aoss:DescribeCollectionItems",
                  "aoss:UpdateCollectionItems",
                  "aoss:DeleteCollectionItems"
                ]
            }
        ],
        "Principal": [
            "arn:aws:iam::{{account-id}}:role/{{role-name}}"
        ]
    },
    {
        "Description": "Model permissions",
        "Rules": [
            {
                "ResourceType": "model",
                "Resource": ["model/{{collection-name}}/*"],
                "Permission": [
                  "aoss:DescribeMLResource",
                  "aoss:CreateMLResource",
                  "aoss:UpdateMLResource",
                  "aoss:DeleteMLResource",
                  "aoss:ExecuteMLResource"
                ]
            }
        ],
        "Principal": [
            "arn:aws:iam::{{account-id}}:role/{{role-name}}"
        ]
    }
]
```
+ The `collection-name` is the name of the collection.
+ The `account-id` is your AWS account ID.
+ The `role-name` is the name of the IAM role that you grant access to.
+ **Index permissions** – These permissions let you create and manage the indexes that store embeddings and read and write documents.
+ **Pipeline permissions** – These permissions let you create and manage ingest and search pipelines.
+ **Model permissions** – These permissions let you manage and run connectors and models. The following table describes each permission.


| Permission | Required to | 
| --- | --- | 
| aoss:CreateMLResource | Create connectors and register and deploy models. | 
| aoss:DescribeMLResource | Get models and create a mapping containing a semantic field. | 
| aoss:UpdateMLResource | Update models, for example, to add a model configuration. | 
| aoss:ExecuteMLResource | Run models. OpenSearch Serverless runs the model when you index documents containing a semantic field or through a text embedding ingest pipeline, and when you run a neural or hybrid query. | 
| aoss:DeleteMLResource | Delete connectors and models. | 

To use the `semantic` field, your data access policy must grant `aoss:DescribeMLResource` and `aoss:ExecuteMLResource` on the model.

## Supported AWS Regions
<a name="serverless-neural-search-supported-regions"></a>

Semantic and hybrid search for OpenSearch Serverless, including the `semantic` field, are available in the following AWS Regions:
+ US East (N. Virginia)
+ US East (Ohio)
+ US West (N. California)
+ US West (Oregon)
+ Asia Pacific (Hong Kong)
+ Asia Pacific (Mumbai)
+ Asia Pacific (Singapore)
+ Asia Pacific (Sydney)
+ Asia Pacific (Tokyo)
+ Asia Pacific (Seoul)
+ Canada (Central)
+ Europe (Frankfurt)
+ Europe (Ireland)
+ Europe (London)
+ Europe (Paris)
+ Europe (Stockholm)
+ Europe (Spain)
+ South America (São Paulo)