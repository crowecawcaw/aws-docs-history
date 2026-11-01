

# Ingest pipelines in Amazon OpenSearch Serverless
<a name="serverless-ingest-pipelines"></a>

An ingest pipeline is an ordered sequence of *processors* that transforms and enriches documents before they are indexed. For example, a pipeline can rename a field, normalize the case of a string, parse a timestamp, or generate vector embeddings for semantic search.

You define a pipeline once, and then apply it to incoming documents either as the default pipeline for an index or on individual indexing requests. Because the pipeline runs in Amazon OpenSearch Serverless, your documents receive the same transformations regardless of which client or integration sends them, which reduces the need for custom preprocessing logic in your applications.

With OpenSearch Serverless, you can use a subset of the ingest pipeline functionality that's available in OpenSearch. This topic describes the processors that OpenSearch Serverless supports, the limitations compared to the open-source implementation, and how to create and manage pipelines. For complete conceptual documentation on ingest pipelines, see [Ingest pipelines](https://docs.opensearch.org/latest/ingest-pipelines/) on the *OpenSearch Documentation* website.

**Topics**
+ [Supported processors](#serverless-ingest-pipelines-processors)
+ [Limitations](#serverless-ingest-pipelines-limitations)
+ [Pricing](#serverless-ingest-pipelines-pricing)
+ [Required permissions](#serverless-ingest-pipelines-permissions)
+ [Working with ingest pipelines](#serverless-ingest-pipelines-working)

## Supported processors
<a name="serverless-ingest-pipelines-processors"></a>

With OpenSearch Serverless, you can use a curated set of ingest processors. OpenSearch Serverless rejects pipelines that reference any other processor type when you create or update the pipeline.

The following processors support neural search and semantic enrichment workflows. They require a configured machine learning model connection. For more information, see [Configure Neural Search and Hybrid Search on OpenSearch Serverless](serverless-configure-neural-search.md).
+ `text_chunking` – Splits long text into passages that fit within the token limits of embedding models. For more information, see [Text chunking processor](https://docs.opensearch.org/latest/ingest-pipelines/processors/text-chunking/) on the *OpenSearch Documentation* website.
+ `text_embedding` – Generates dense vector embeddings from text fields for semantic search. For more information, see [Text embedding processor](https://docs.opensearch.org/latest/ingest-pipelines/processors/text-embedding/) on the *OpenSearch Documentation* website.
+ `text_image_embedding` – Generates combined vector embeddings from text and image fields for multimodal search. For more information, see [Text image embedding processor](https://docs.opensearch.org/latest/ingest-pipelines/processors/text-image-embedding/) on the *OpenSearch Documentation* website.
+ `sparse_encoding` – Generates sparse vector representations from text fields for neural sparse search. For more information, see [Sparse encoding processor](https://docs.opensearch.org/latest/ingest-pipelines/processors/sparse-encoding/) on the *OpenSearch Documentation* website.

The following processors perform general-purpose transformations on document fields.


| Processor | Description | 
| --- | --- | 
| copy | Copies the value of a source field to a target field. The source field is retained. | 
| date | Parses a date string from a field and writes a canonical timestamp to a target field. | 
| dot\_expander | Expands a field name that contains dots into a nested object structure. | 
| join | Joins the elements of an array field into a single string with a separator. | 
| lowercase | Converts a string field to lowercase. | 
| remove | Removes one or more fields from the document. | 
| rename | Renames a field. | 
| set | Sets a field to a static value. To copy the value of another field, use the copy processor instead. | 
| trim | Removes leading and trailing whitespace from a string field. | 
| uppercase | Converts a string field to uppercase. | 

For configuration details for each processor, see [Ingest processors](https://docs.opensearch.org/latest/ingest-pipelines/processors/index-processors/) on the *OpenSearch Documentation* website.

## Limitations
<a name="serverless-ingest-pipelines-limitations"></a>

Ingest pipelines in OpenSearch Serverless have the following limitations compared to the open-source OpenSearch implementation:
+ **No scripting.** The `script` processor and Painless scripting aren't supported in ingest pipelines.
+ **No Mustache templates.** Processor configuration values must be literal values. You can't use Mustache template snippets such as `{{{field_name}}}` to reference the value of another field. For example, the `set` processor writes static values only. To copy a value from one field to another, use the `copy` processor.
+ **Supported processors only.** OpenSearch Serverless rejects a request to create or update a pipeline that contains a processor type that isn't listed in [Supported processors](#serverless-ingest-pipelines-processors).
+ **Propagation latency.** Expect up to 15 seconds of latency before a newly created or updated pipeline takes effect.

## Pricing
<a name="serverless-ingest-pipelines-pricing"></a>

Ingest pipelines run on the compute that processes indexing requests for your collection. The processing time that your pipelines consume counts toward the indexing OpenSearch Compute Units (OCUs) for your collection, in the same way as other indexing activity. Pipelines with more processors, or with compute-intensive processors, consume more indexing capacity than simple pipelines. For more information about how indexing capacity scales and is billed, see [Managing capacity limits for Amazon OpenSearch Serverless](serverless-scaling.md) and [Amazon OpenSearch Service pricing](https://aws.amazon.com/opensearch-service/pricing/).

Machine learning processors such as `text_embedding` additionally invoke the remote model that you configured, and the model provider bills model inference separately.

## Required permissions
<a name="serverless-ingest-pipelines-permissions"></a>

Ingest pipeline operations map to the following OpenSearch Serverless data access policy permissions. The permissions apply to the `collection` resource type.
+ `aoss:CreateCollectionItems` – Create or update a pipeline.
+ `aoss:DescribeCollectionItems` – Get, list, and simulate pipelines.
+ `aoss:DeleteCollectionItems` – Delete a pipeline.

The following example data access policy grants a principal permission to manage pipelines in a collection. Replace {{collection-name}} with the name of your collection, {{account-id}} with your AWS account ID, and {{role-name}} with the name of the IAM role that manages pipelines.

```
[
    {
        "Description": "Manage pipelines",
        "Rules": [
            {
                "ResourceType": "collection",
                "Resource": ["collection/{{collection-name}}"],
                "Permission": [
                    "aoss:CreateCollectionItems",
                    "aoss:DescribeCollectionItems",
                    "aoss:DeleteCollectionItems"
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

## Working with ingest pipelines
<a name="serverless-ingest-pipelines-working"></a>

You create and manage ingest pipelines with the OpenSearch REST API against your collection endpoint. All requests must be signed with AWS Signature Version 4 using the service name `aoss`. For more information, see [Signing HTTP requests with other clients](serverless-clients.md#serverless-signing).

### Create or update a pipeline
<a name="serverless-ingest-pipelines-create"></a>

To create a pipeline, send a `PUT` request to the `_ingest/pipeline` endpoint with the pipeline name and an ordered list of processors. Documents pass through the processors in the order that they're defined. To update an existing pipeline, send the same request with the modified definition.

The following example creates a pipeline that trims a field, lowercases it, and renames it. Replace {{my-pipeline}} with the name of your pipeline.

```
PUT _ingest/pipeline/{{my-pipeline}}
{
  "description": "Normalizes the category field",
  "processors": [
    {
      "trim": {
        "field": "category"
      }
    },
    {
      "lowercase": {
        "field": "category"
      }
    },
    {
      "rename": {
        "field": "category",
        "target_field": "category_normalized"
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

The following example creates a pipeline that chunks a text field and generates vector embeddings for each chunk. It requires a configured model. For more information, see [Configure Neural Search and Hybrid Search on OpenSearch Serverless](serverless-configure-neural-search.md).

```
PUT _ingest/pipeline/{{nlp-ingest-pipeline}}
{
  "description": "Chunks text and generates embeddings",
  "processors": [
    {
      "text_chunking": {
        "algorithm": {
          "fixed_token_length": {
            "token_limit": 384
          }
        },
        "field_map": {
          "{{text-field}}": "{{text-chunks-field}}"
        }
      }
    },
    {
      "text_embedding": {
        "model_id": "{{my-model-id}}",
        "field_map": {
          "{{text-chunks-field}}": "{{embedding-field}}"
        }
      }
    }
  ]
}
```

For more information, see [Create pipeline](https://docs.opensearch.org/latest/ingest-pipelines/create-ingest/) on the *OpenSearch Documentation* website.

### Get a pipeline
<a name="serverless-ingest-pipelines-get"></a>

To retrieve the definition of a pipeline, send a `GET` request with the pipeline name:

```
GET _ingest/pipeline/{{my-pipeline}}
```

The request returns the pipeline definition:

```
{
  "my-pipeline": {
    "description": "Normalizes the category field",
    "processors": [
      {
        "trim": {
          "field": "category"
        }
      },
      {
        "lowercase": {
          "field": "category"
        }
      },
      {
        "rename": {
          "field": "category",
          "target_field": "category_normalized"
        }
      }
    ]
  }
}
```

For more information, see [Get pipeline](https://docs.opensearch.org/latest/ingest-pipelines/get-ingest/) on the *OpenSearch Documentation* website.

### List pipelines
<a name="serverless-ingest-pipelines-list"></a>

To list all of the pipelines in a collection, send a `GET` request without a pipeline name:

```
GET _ingest/pipeline
```

The request returns the definitions of all of the pipelines in the collection, keyed by pipeline name.

### Simulate a pipeline
<a name="serverless-ingest-pipelines-simulate"></a>

Before you apply a pipeline to live traffic, you can simulate it against sample documents and inspect the transformed output. To simulate an existing pipeline, send a `POST` request with the pipeline name and the sample documents:

```
POST _ingest/pipeline/{{my-pipeline}}/_simulate
{
  "docs": [
    {
      "_index": "{{my-index}}",
      "_id": "1",
      "_source": {
        "category": "  Home Appliances  "
      }
    }
  ]
}
```

The response shows each document as it would be indexed after the pipeline runs. In this example, the pipeline trimmed and lowercased the `category` field and renamed it to `category_normalized`:

```
{
  "docs": [
    {
      "doc": {
        "_index": "my-index",
        "_id": "1",
        "_source": {
          "category_normalized": "home appliances"
        },
        "_ingest": {
          "timestamp": "2026-10-28T16:23:40.895265415Z"
        }
      }
    }
  ]
}
```

You can also simulate a pipeline definition that you haven't created yet by including the definition in the request body:

```
POST _ingest/pipeline/_simulate
{
  "pipeline": {
    "processors": [
      {
        "lowercase": {
          "field": "category"
        }
      }
    ]
  },
  "docs": [
    {
      "_index": "{{my-index}}",
      "_id": "1",
      "_source": {
        "category": "Home Appliances"
      }
    }
  ]
}
```

For more information, see [Simulate pipeline](https://docs.opensearch.org/latest/ingest-pipelines/simulate-ingest/) on the *OpenSearch Documentation* website.

### Delete a pipeline
<a name="serverless-ingest-pipelines-delete"></a>

To delete a pipeline that you no longer need, send a `DELETE` request with the pipeline name:

```
DELETE _ingest/pipeline/{{my-pipeline}}
```

The request returns the following response:

```
{
  "acknowledged": true
}
```

### Apply a pipeline to indexing requests
<a name="serverless-ingest-pipelines-use"></a>

To run a pipeline on every document that's indexed into an index, set the `index.default_pipeline` setting when you create the index:

```
PUT {{my-index}}
{
  "settings": {
    "index.default_pipeline": "{{my-pipeline}}"
  }
}
```

The request returns the following response:

```
{
  "acknowledged": true,
  "shards_acknowledged": false,
  "index": "my-index"
}
```

Alternatively, specify the pipeline on an individual indexing or bulk request with the `pipeline` query parameter:

```
POST {{my-index}}/_doc?pipeline={{my-pipeline}}
{
  "category": "  Home Appliances  "
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
A `pipeline` query parameter overrides the `default_pipeline` setting of the index for that request. The two don't combine. If a service feature such as automatic semantic enrichment manages the default pipeline for your index, overriding or replacing it can prevent that feature's processing from running.