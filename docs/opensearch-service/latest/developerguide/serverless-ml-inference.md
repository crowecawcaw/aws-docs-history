

# ML inference pipelines in Amazon OpenSearch Serverless
<a name="serverless-ml-inference"></a>

The `ml_inference` processor in Amazon OpenSearch Serverless is a general-purpose processor that calls a configured machine learning model and maps the model's inputs and outputs to document or query fields. You control the mapping with the `input_map` and `output_map` parameters, which specify the document or query fields that supply the model input and the fields that receive the model output.

Unlike the purpose-built machine learning processors such as `text_embedding`, `text_image_embedding`, and `sparse_encoding`, which each support a single model type, the `ml_inference` processor works with any configured model. It can also run in both ingest pipelines and search pipelines, so you can apply model inference during indexing, before a query runs, or after results are returned. Use the `ml_inference` processor when you need a model or an input and output mapping that the purpose-built processors don't provide. For complete conceptual documentation, see [ML inference processor](https://docs.opensearch.org/latest/ingest-pipelines/processors/ml-inference/) on the *OpenSearch Documentation* website.

You can use the `ml_inference` processor to support workflows such as the following:
+ Semantic search
+ Retrieval-augmented generation (RAG)
+ Multimodal search
+ Result summarization
+ Query enrichment

**Topics**
+ [Prerequisites](#serverless-ml-inference-prerequisites)
+ [Example: Set up an Amazon Titan embedding model](#serverless-ml-inference-model-setup)
+ [Match the processor to your model](#serverless-ml-inference-match-model)
+ [Using ml\_inference in an ingest pipeline](#serverless-ml-inference-ingest)
+ [Using ml\_inference in a search pipeline](#serverless-ml-inference-search)
+ [Pricing](#serverless-ml-inference-pricing)
+ [Required permissions](#serverless-ml-inference-permissions)
+ [Troubleshooting](#serverless-ml-inference-troubleshooting)
+ [For more information](#serverless-ml-inference-more-info)

## Prerequisites
<a name="serverless-ml-inference-prerequisites"></a>

Before you use the `ml_inference` processor, complete the following:
+ **Create a vector search collection.** OpenSearch Serverless supports the `ml_inference` processor on vector search collections (type `VECTORSEARCH`) in a NextGen collection group. OpenSearch Serverless accepts only models with a `function_name` of `remote`. To create the collection group, see [Create a collection group](serverless-collection-groups-procedures.md#collection-groups-create). To create the collection, see [Working with vector search collections](serverless-vector-search.md). Enable standby replicas on both the collection group and the collection.

  The following AWS CLI example creates a NextGen collection group and a vector search collection in it. Replace {{my-collection-group}} and {{my-collection}} with your own names.

  ```
  aws opensearchserverless create-collection-group \
      --name {{my-collection-group}} \
      --generation NEXTGEN \
      --standby-replicas ENABLED \
      --capacity-limits maxIndexingCapacityInOCU={{8}},maxSearchCapacityInOCU={{8}}
  
  aws opensearchserverless create-collection \
      --name {{my-collection}} \
      --type VECTORSEARCH \
      --collection-group-name {{my-collection-group}} \
      --standby-replicas ENABLED
  ```
+ **Configure and deploy a remote model.** The processor calls a configured and deployed remote model, which you reference by its model ID. For an example that sets up an Amazon Titan embedding model, see [Example: Set up an Amazon Titan embedding model](#serverless-ml-inference-model-setup). For more information, see [Configure Machine Learning on Amazon OpenSearch Serverless](serverless-configure-machine-learning.md).
+ **Sign your requests.** Sign every request to the collection endpoint with AWS Signature Version 4 using the service name `aoss`. For more information, see [Signing HTTP requests with other clients](serverless-clients.md#serverless-signing).

## Example: Set up an Amazon Titan embedding model
<a name="serverless-ml-inference-model-setup"></a>

The examples in this topic use an Amazon Titan Text Embeddings V2 model in Amazon Bedrock. The following steps create the connector and the model in your collection.

1. Create an IAM role that OpenSearch Serverless assumes to call Amazon Bedrock. The role's trust policy must allow the `ml.opensearchservice.amazonaws.com` service principal, and the role's permissions policy must allow `bedrock:InvokeModel` on the model. The principal that creates the connector also needs `iam:PassRole` on this role.

1. Create the connector. Replace {{region}} with the AWS Region of the Amazon Bedrock model, {{account-id}} with your AWS account ID, and {{bedrock-role}} with the name of the role from the previous step.

   ```
   POST /_plugins/_ml/connectors/_create
   {
     "name": "Amazon Bedrock Titan Text Embeddings V2",
     "description": "Connector for amazon.titan-embed-text-v2:0",
     "version": 1,
     "protocol": "aws_sigv4",
     "parameters": {
       "region": "{{region}}",
       "service_name": "bedrock",
       "model": "amazon.titan-embed-text-v2:0"
     },
     "credential": {
       "roleArn": "arn:aws:iam::{{account-id}}:role/{{bedrock-role}}"
     },
     "actions": [
       {
         "action_type": "predict",
         "method": "POST",
         "url": "https://bedrock-runtime.${parameters.region}.amazonaws.com/model/${parameters.model}/invoke",
         "headers": {
           "content-type": "application/json",
           "x-amz-content-sha256": "required"
         },
         "request_body": "{ \"inputText\": \"${parameters.inputText}\" }",
         "post_process_function": "connector.post_process.bedrock.embedding"
       }
     ]
   }
   ```

   The response contains the connector ID. The `post_process_function` setting returns the embedding at `$.inference_results[0].output[0].data`, which is the path that the examples in this topic use.

1. Register the model with the connector. Replace {{my-connector-id}} with the connector ID from the previous step.

   ```
   POST /_plugins/_ml/models/_register
   {
     "name": "titan-embed-text-v2",
     "function_name": "remote",
     "description": "Amazon Titan Text Embeddings V2",
     "connector_id": "{{my-connector-id}}"
   }
   ```

   The response contains the model ID.

1. Deploy the model. Replace {{my-model-id}} with the model ID from the previous step.

   ```
   POST /_plugins/_ml/models/{{my-model-id}}/_deploy
   ```

1. Test the model with the predict API, as shown in [Match the processor to your model](#serverless-ml-inference-match-model).

These steps require the following permissions on the `model` resource type: `aoss:CreateMLResource` to create the connector and register the model, `aoss:UpdateMLResource` to deploy it, and `aoss:ExecuteMLResource` to call the predict API. For an example data access policy that grants these permissions, see [Configure permissions for Machine Learning](serverless-configure-machine-learning.md#serverless-configure-machine-learning-permissions).

## Match the processor to your model
<a name="serverless-ml-inference-match-model"></a>

The `ml_inference` processor doesn't know the shape of your model. You tell it with `input_map` and `output_map`. If these don't match the model's predict API, the processor fails or writes the wrong value. Test the model with the predict API first, then copy the parameter names and the output path into your pipeline.

The following table shows where each part of the mapping comes from.


| Mapping | What it must match | 
| --- | --- | 
| Key in input\_map | A parameter name in the predict request, which is a ${parameters.{{name}}} placeholder in the connector request\_body. | 
| Value in input\_map | The document field, or the query field, that supplies the value. | 
| Key in output\_map | The name of the field that receives the model output. | 
| Value in output\_map | A JSON path into the predict response, for example $.inference\_results[0].output[0].data. | 

The following example calls the predict API for a text embedding model. The `inputText` parameter is the same name that the ingest pipeline example uses as the key in `input_map`. Replace {{my-model-id}} with the ID of your deployed model.

```
POST /_plugins/_ml/models/{{my-model-id}}/_predict
{
  "parameters": {
    "inputText": "Example document text"
  }
}
```

The model returns a response like the following. The `data` array is shortened for readability.

```
{
  "inference_results": [
    {
      "output": [
        {
          "name": "sentence_embedding",
          "data_type": "FLOAT32",
          "shape": [1024],
          "data": [0.0123, -0.0456, 0.0789]
        }
      ],
      "status_code": 200
    }
  ]
}
```

The embedding is in the `data` array of the first output. The JSON path `$.inference_results[0].output[0].data` selects it. This is the path that the ingest pipeline example uses in `output_map`.

**Note**  
This response shape applies when the Amazon Titan embedding connector sets `post_process_function` to `connector.post_process.bedrock.embedding`. Without a post-processing function, the vector is at `$.inference_results[0].output[0].dataAsMap.embedding` instead. For connector setup, see [Configure Machine Learning on Amazon OpenSearch Serverless](serverless-configure-machine-learning.md).

**Important**  
The request parameters and the response shape depend on the model and its connector. When you use a different model, don't reuse the paths from the examples in this topic. Run the predict API for your model and read the paths from its response.

For example, a large language model that returns its raw response has a different shape. The text is nested inside the `dataAsMap` object, and the parameter you send is named after the connector placeholder instead of `inputText`.

```
POST /_plugins/_ml/models/{{my-llm-model-id}}/_predict
{
  "parameters": {
    "messages": "[{\"role\":\"user\",\"content\":[{\"text\":\"Summarize: Example text\"}]}]"
  }
}
```

```
{
  "inference_results": [
    {
      "output": [
        {
          "name": "response",
          "dataAsMap": {
            "output": {
              "message": {
                "role": "assistant",
                "content": [
                  {
                    "text": "A short summary of the example text."
                  }
                ]
              }
            },
            "stopReason": "end_turn"
          }
        }
      ],
      "status_code": 200
    }
  ]
}
```

For this response, the JSON path is `$.inference_results[0].output[0].dataAsMap.output.message.content[0].text`. The exact structure under `dataAsMap` is the response of your model provider, so it differs between providers and models.

To switch the processor to a different model, do the following:

1. Find the parameter names in the `request_body` of the model's connector. Each `${parameters.{{name}}}` placeholder is a name that you can use as a key in `input_map`.

1. Call the predict API with a sample value for each parameter.

1. Read the predict response, and write the JSON path to the value that you want to keep.

1. Update `model_id`, `input_map`, and `output_map` in the pipeline.

1. Run the `_simulate` API on a sample document to confirm that the output field has the value that you expect.

**Note**  
The predict API requires the `aoss:ExecuteMLResource` permission on the model resource. For more information, see [Configure Machine Learning on Amazon OpenSearch Serverless](serverless-configure-machine-learning.md).

## Using ml\_inference in an ingest pipeline
<a name="serverless-ml-inference-ingest"></a>

In an ingest pipeline, the `ml_inference` processor runs model inference during indexing. A common use is to generate vector embeddings from a text field so that you can run semantic search over your data. The `input_map` maps a document field to the model input, and the `output_map` writes the model output to a new field.

The following example creates a pipeline that sends the `text` field to the model and writes the returned embedding to an `embedding` field. Replace {{my-pipeline}} with the name of your pipeline and {{my-model-id}} with the ID of your deployed model.

```
PUT _ingest/pipeline/{{my-pipeline}}
{
  "description": "Generates embeddings with a configured model",
  "processors": [
    {
      "ml_inference": {
        "model_id": "{{my-model-id}}",
        "full_response_path": true,
        "input_map": [
          {
            "inputText": "text"
          }
        ],
        "output_map": [
          {
            "embedding": "$.inference_results[0].output[0].data"
          }
        ]
      }
    }
  ]
}
```

The request returns the following response:

```
{
  "acknowledged": true
}
```

The `output_map` path is rooted at `inference_results` because `full_response_path` is set to `true`. This setting evaluates the output path against the full model response. For more information, see [ML inference processor](https://docs.opensearch.org/latest/ingest-pipelines/processors/ml-inference/) on the *OpenSearch Documentation* website.

Before you apply the pipeline to live traffic, you can simulate it against sample documents with the `_simulate` endpoint. To run model inference automatically on every document that's indexed into an index, set the `index.default_pipeline` setting when you create the index. Alternatively, specify the pipeline on an individual indexing request with the `pipeline` query parameter. For more information about creating, simulating, and applying ingest pipelines, see [Ingest pipelines in Amazon OpenSearch Serverless](serverless-ingest-pipelines.md).

The following example indexes a document and runs the pipeline. Replace {{my-index}} with the name of your index and {{my-pipeline}} with the name of your pipeline.

```
POST {{my-index}}/_doc?pipeline={{my-pipeline}}
{
  "text": "Example document text"
}
```

The response confirms that the document was indexed:

```
{
  "_index": "my-index",
  "_id": "93VTg6EBtHTIBjFym5yW",
  "_version": 1,
  "result": "created",
  "_shards": {
    "total": 0,
    "successful": 0,
    "failed": 0
  },
  "_seq_no": 0,
  "_primary_term": 0
}
```

**Note**  
The target index must be configured for vector search. Enable `index.knn` and map the output field (for example, `embedding`) as a `knn_vector` field with a dimension that matches your model.

## Using ml\_inference in a search pipeline
<a name="serverless-ml-inference-search"></a>

In a search pipeline, the `ml_inference` processor runs model inference as part of a query. A search request processor transforms or rewrites the query before it runs. A search response processor enriches the results before you receive them. To run a search pipeline, send the request with the `search_pipeline` query parameter. Replace {{my-index}} with the name of your index and {{my-pipeline}} with the name of your pipeline.

```
POST {{my-index}}/_search?search_pipeline={{my-pipeline}}
```

To create or update a search pipeline, send the pipeline body to the `_search/pipeline` endpoint, as the examples in the following sections show.

**Note**  
A newly created search pipeline can take a few minutes to take effect, even after the create request returns `"acknowledged": true`. Until then, search requests that reference the pipeline fail with a `Pipeline {{my-pipeline}} is not defined` error. Retry the request after a short wait.

### Search request processor
<a name="serverless-ml-inference-search-request"></a>

You use a search request processor to rewrite an incoming query before OpenSearch Serverless runs it. The following example takes the text of a `match` query, generates a vector from it with a configured model, and rewrites the request into a k-NN query with the `query_template` parameter. OpenSearch Serverless replaces the `${query_vec}` placeholder in the template with the model output that `output_map` captures. Replace {{my-model-id}} with the ID of your deployed model.

```
PUT /_search/pipeline/{{my-pipeline}}
{
  "request_processors": [
    {
      "ml_inference": {
        "model_id": "{{my-model-id}}",
        "full_response_path": true,
        "query_template": "{\"size\":2,\"_source\":[\"text\"],\"query\":{\"knn\":{\"embedding\":{\"vector\":${query_vec},\"k\":2}}}}",
        "input_map": [
          {
            "inputText": "query.match.text.query"
          }
        ],
        "output_map": [
          {
            "query_vec": "$.inference_results[0].output[0].data"
          }
        ],
        "ignore_missing": true
      }
    }
  ]
}
```

Set `full_response_path` to `true` so that the `output_map` JSON path resolves against the full model response. This lets you use the same output path that you read from the predict API response.

Set `ignore_missing` to `true` when the source field might be missing. A query that doesn't contain the mapped field, such as a `match_all` query, then passes through unchanged instead of failing. The processor still rewrites queries that contain the field.

### Search response processor
<a name="serverless-ml-inference-search-response"></a>

A search response processor runs after a query returns, so you can enrich or summarize each hit. The following example sends the `text` field of each hit to a configured model and writes the model output to a `text_vec` field. Set `one_to_one` to `true` so that the processor runs the model once for each search hit. The default is `false`, which sends all hits to the model in a single request, and models that expect a single input value reject that request. Replace {{my-model-id}} with the ID of your deployed model.

```
PUT /_search/pipeline/{{my-pipeline}}
{
  "response_processors": [
    {
      "ml_inference": {
        "model_id": "{{my-model-id}}",
        "full_response_path": true,
        "input_map": [
          {
            "inputText": "text"
          }
        ],
        "output_map": [
          {
            "text_vec": "$.inference_results[0].output[0].data"
          }
        ],
        "one_to_one": true
      }
    }
  ]
}
```

To summarize results with a large language model, add a `model_config` object that contains the model prompt, and set `one_to_one` to `true` so that the processor summarizes each search hit separately. The prompt can reference the mapped input through a template parameter such as `${parameters.context}`. The `output_map` path in this example matches a model that returns its raw response. For more information, see [Match the processor to your model](#serverless-ml-inference-match-model). Replace {{my-model-id}} with the ID of your deployed model.

```
PUT /_search/pipeline/{{my-pipeline}}
{
  "response_processors": [
    {
      "ml_inference": {
        "model_id": "{{my-model-id}}",
        "full_response_path": true,
        "input_map": [
          {
            "context": "text"
          }
        ],
        "output_map": [
          {
            "summary": "$.inference_results[0].output[0].dataAsMap.output.message.content[0].text"
          }
        ],
        "model_config": {
          "messages": "[{\"role\":\"user\",\"content\":[{\"text\":\"Summarize the following text: ${parameters.context}\"}]}]"
        },
        "one_to_one": true
      }
    }
  ]
}
```

## Pricing
<a name="serverless-ml-inference-pricing"></a>

The `ml_inference` processor runs on the compute that processes your collection's requests. In an ingest pipeline, its processing counts toward the indexing OpenSearch Compute Units (OCUs) for your collection. In a search pipeline, its processing counts toward the search OCUs, in the same way as other indexing and search activity. Pipelines with more processors, or with compute-intensive processors, consume more capacity than simple pipelines. For more information about how capacity scales and is billed, see [Managing capacity limits for Amazon OpenSearch Serverless](serverless-scaling.md) and [Amazon OpenSearch Service pricing](https://aws.amazon.com/opensearch-service/pricing/).

The processor also invokes the remote model that you configured, and the model provider bills model inference separately.

## Required permissions
<a name="serverless-ml-inference-permissions"></a>

Managing the search and ingest pipelines that contain an `ml_inference` processor maps to the following OpenSearch Serverless data access policy permissions. The permissions apply to the `collection` resource type.
+ `aoss:CreateCollectionItems` – Create or update a pipeline.
+ `aoss:DescribeCollectionItems` – Get, list, and simulate pipelines.
+ `aoss:DeleteCollectionItems` – Delete a pipeline.

The processor also calls the model that you configured. For the data access policy permissions that a principal needs to create and run models, see [Configure Machine Learning on Amazon OpenSearch Serverless](serverless-configure-machine-learning.md).

**Important**  
The principal that sends a request through the pipeline needs the `aoss:ExecuteMLResource` permission on the model. This applies to indexing documents, running `_simulate`, and searching. Without this permission, these requests fail with a `Forbidden` error that doesn't name the missing permission.

The following example data access policy grants a principal permission to manage pipelines in a collection and to run the models in that collection. Replace {{collection-name}} with the name of your collection, {{account-id}} with your AWS account ID, and {{role-name}} with the name of the IAM role that manages and uses the pipelines.

```
[
    {
        "Description": "Manage pipelines and run models",
        "Rules": [
            {
                "ResourceType": "collection",
                "Resource": ["collection/{{collection-name}}"],
                "Permission": [
                    "aoss:CreateCollectionItems",
                    "aoss:DescribeCollectionItems",
                    "aoss:DeleteCollectionItems"
                ]
            },
            {
                "ResourceType": "model",
                "Resource": ["model/{{collection-name}}/*"],
                "Permission": [
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

For the complete mapping of OpenSearch API operations to OpenSearch Serverless permissions, see [Supported operations and plugins in Amazon OpenSearch Serverless](serverless-genref.md).

## Troubleshooting
<a name="serverless-ml-inference-troubleshooting"></a>

If a request that uses an `ml_inference` pipeline fails with a `Forbidden` error, check the following common causes:
+ The calling principal doesn't have `aoss:ExecuteMLResource` on the model. Add a `model` rule to the data access policy, as shown in [Required permissions](#serverless-ml-inference-permissions).
+ The data access policy doesn't grant the principal the index or collection permissions for the operation, such as writing documents, searching, or creating pipelines.
+ The request is signed with the service name `es` instead of `aoss`.
+ The network policy for the collection doesn't allow access from the source of the request.

If a search request fails with a `Pipeline {{my-pipeline}} is not defined` error right after you create the pipeline, wait a few minutes and retry. For more information, see [Using ml\_inference in a search pipeline](#serverless-ml-inference-search).

## For more information
<a name="serverless-ml-inference-more-info"></a>

For more information about the `ml_inference` processor, see the following:
+ For the ingest-pipeline processor reference, see [ML inference processor](https://docs.opensearch.org/latest/ingest-pipelines/processors/ml-inference/) on the *OpenSearch Documentation* website.
+ For the search request processor reference, see [ML inference search request processor](https://docs.opensearch.org/latest/search-plugins/search-pipelines/ml-inference-search-request/) on the *OpenSearch Documentation* website.
+ For the search response processor reference, see [ML inference search response processor](https://docs.opensearch.org/latest/search-plugins/search-pipelines/ml-inference-search-response/) on the *OpenSearch Documentation* website.
+ For a worked example of review summarization and semantic search, see [Introduction to ML inference processors in OpenSearch: review summarization and semantic search](https://opensearch.org/blog/introduction-to-ml-inference-processors-in-opensearch-review-summarization-and-semantic-search/) on the *OpenSearch* blog.