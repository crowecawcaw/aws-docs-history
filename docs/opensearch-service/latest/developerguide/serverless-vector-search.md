# Working with vector search collections

The _vector search_ collection type in OpenSearch Serverless provides a similarity
search capability that is scalable and high performing. It makes it easy for you to build
modern machine learning (ML) augmented search experiences and generative artificial
intelligence (AI) applications without having to manage the underlying vector database
infrastructure.

Use cases for vector search collections include image searches, document searches, music
retrieval, product recommendations, video searches, location-based searches, fraud
detection, and anomaly detection.

Because the vector engine for OpenSearch Serverless is powered by the [k-nearest neighbor
(k-NN) search feature](https://opensearch.org/docs/latest/search-plugins/knn/index/ "https://opensearch.org/docs/latest/search-plugins/knn/index/") in OpenSearch, you get the same functionality with the
simplicity of a serverless environment. The engine supports [k-NN plugin
API](https://opensearch.org/docs/latest/search-plugins/knn/api/ "https://opensearch.org/docs/latest/search-plugins/knn/api/"). With these operations, you can take advantage of full-text search, advanced
filtering, aggregations, geospatial queries, nested queries for faster retrieval of data,
and enhanced search results.

The vector engine provides distance metrics such as Euclidean distance, cosine similarity,
and dot product similarity, and can accommodate 16,000 dimensions. You can store fields with
various data types for metadata, such as numbers, Booleans, dates, keywords, and geopoints.
You can also store fields with text for descriptive information to add more context to
stored vectors. Colocating the data types reduces complexity, increases maintainability, and
avoids data duplication, version compatibility challenges, and licensing issues.

###### Note

Note the following information:

- Amazon OpenSearch Serverless supports Faiss 16-bit scalar quantization which can be used to
  perform conversions between 32-bit floating and 16-bit vectors. To learn more,
  see [Faiss 16-bit scalar quantization](https://opensearch.org/docs/latest/search-plugins/knn/knn-vector-quantization/#faiss-16-bit-scalar-quantization "https://opensearch.org/docs/latest/search-plugins/knn/knn-vector-quantization/#faiss-16-bit-scalar-quantization"). You can also use binary vectors
  to reduce memory costs. For more information, see [Binary vectors](https://opensearch.org/docs/latest/field-types/supported-field-types/knn-vector#binary-vectors "https://opensearch.org/docs/latest/field-types/supported-field-types/knn-vector#binary-vectors").
- Amazon OpenSearch Serverless supports disk-based vector search. Disk-based
  vector search significantly reduces the operational costs for vector workloads
  in low-memory environments. For more information, see [Disk-based vector search](https://docs.opensearch.org/2.19/vector-search/optimizing-storage/disk-based-vector-search/ "https://docs.opensearch.org/2.19/vector-search/optimizing-storage/disk-based-vector-search/").

## Getting started with vector search

collections

In this tutorial, you complete the following steps to store, search, and retrieve
vector embeddings in real time:

1. [Configure
   permissions](#serverless-vector-permissions "#serverless-vector-permissions")
2. [Create a collection](#serverless-vector-create "#serverless-vector-create")
3. [Upload and search data](#serverless-vector-index "#serverless-vector-index")
4. [Delete the collection](#serverless-vector-delete "#serverless-vector-delete")

### Step 1: Configure

permissions

To complete this tutorial (and to use OpenSearch Serverless in general), you must have the
correct AWS Identity and Access Management (IAM) permissions. In this tutorial, you create a collection,
upload and search data, and then delete the collection.

Your user or role must have an attached [identity-based policy](security-iam-serverless.md#security-iam-serverless-id-based-policies "security-iam-serverless.md#security-iam-serverless-id-based-policies")
with the following minimum permissions:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "aoss:CreateCollection",
 "aoss:ListCollections",
 "aoss:BatchGetCollection",
 "aoss:DeleteCollection",
 "aoss:CreateAccessPolicy",
 "aoss:ListAccessPolicies",
 "aoss:UpdateAccessPolicy",
 "aoss:CreateSecurityPolicy",
 "iam:ListUsers",
 "iam:ListRoles"
 ],
 "Effect": "Allow",
 "Resource": "*"
 }
 ]
}`

```

For more information about OpenSearch Serverless IAM permissions, see [Identity and Access Management for
Amazon OpenSearch Serverless](security-iam-serverless.md "security-iam-serverless.md").

### Step 2: Create a collection

A _collection_ is a group of OpenSearch indexes
that work together to support a specific workload or use case.

###### To create an OpenSearch Serverless collection

1. Open the Amazon OpenSearch Service console at [https://console.aws.amazon.com/aos/home](https://console.aws.amazon.com/aos/home "https://console.aws.amazon.com/aos/home ").
2. Choose **Collections** in the left navigation pane and
   choose **Create collection**.
3. Name the collection **housing**.
4. For collection type, choose **Vector search**. For more
   information, see [Choosing a collection type](serverless-overview.md#serverless-usecase "serverless-overview.md#serverless-usecase").
5. Under **Deployment type**, clear **Enable
   redundancy (active replicas)**. This creates a collection in
   development or testing mode, and reduces the number of OpenSearch Compute
   Units (OCUs) in your collection to two. If you want to create a production
   environment in this tutorial, leave the check box selected.
6. Under **Security**, select **Easy
   create** to streamline your security configuration. All the
   data in the vector engine is encrypted in transit and at rest by default.
   The vector engine supports fine-grained IAM permissions so that you can
   define who can create, update, and delete encryptions, networks,
   collections, and indexes.
7. Choose **Next**.
8. Review your collection settings and choose **Submit**. Wait several minutes for the collection status to
   become `Active`.

### Step 3: Upload and search data

An _index_ is a collection of documents with a
common data schema that provides a way for you to store, search, and retrieve your
vector embeddings and other fields. You can create and upload data to indexes in an
OpenSearch Serverless collection by using the [Dev
Tools](https://opensearch.org/docs/latest/dashboards/dev-tools/index-dev/ "https://opensearch.org/docs/latest/dashboards/dev-tools/index-dev/") console in OpenSearch Dashboards, or an HTTP tool such as [Postman](https://www.postman.com/downloads/ "https://www.postman.com/downloads/") or [awscurl](https://github.com/okigan/awscurl "https://github.com/okigan/awscurl"). This tutorial uses Dev
Tools.

###### To index and search data in the movies collection

1. To create a single index for your new collection, send the following
   request in the [Dev Tools](https://opensearch.org/docs/latest/dashboards/dev-tools/index-dev/ "https://opensearch.org/docs/latest/dashboards/dev-tools/index-dev/") console. By default, this creates an index with an
   `nmslib` engine and Euclidean distance.

```
PUT housing-index
{
   "settings": {
      "index.knn": true
   },
   "mappings": {
      "properties": {
         "housing-vector": {
            "type": "knn_vector",
            "dimension": 3
         },
         "title": {
            "type": "text"
         },
         "price": {
            "type": "long"
         },
         "location": {
            "type": "geo_point"
         }
      }
   }
}
```

2. To index a single document into _housing-index_, send
   the following request:

```
POST housing-index/_doc
{
  "housing-vector": [
    10,
    20,
    30
  ],
  "title": "2 bedroom in downtown Seattle",
  "price": "2800",
  "location": "47.71, 122.00"
}
```

3. To search for properties that are similar to the ones in your index, send
   the following query:

```
GET housing-index/_search
{
    "size": 5,
    "query": {
        "knn": {
            "housing-vector": {
                "vector": [
                    10,
                    20,
                    30
                ],
                "k": 5
            }
        }
    }
}
```

### Step 4: Delete the collection

Because the _housing_ collection is for test
purposes, make sure to delete it when you're done experimenting.

###### To delete an OpenSearch Serverless collection

1. Go back to the **Amazon OpenSearch Service** console.
2. Choose **Collections** in the left navigation pane and
   select the **properties** collection.
3. Choose **Delete** and confirm the deletion.

## Filtered search

You can use filters to refine your semantic search results. To create an index and
perform a filtered search on your documents, substitute [Upload and search data](#serverless-vector-index "#serverless-vector-index") in the previous
tutorial with the following instructions. The other steps remain the same. For more
information about filters, see [k-NN
search with filters](https://opensearch.org/docs/latest/search-plugins/knn/filter-search-knn/ "https://opensearch.org/docs/latest/search-plugins/knn/filter-search-knn/").

###### To index and search data in the movies collection

1. To create a single index for your collection, send the following request in
   the [Dev
   Tools](https://opensearch.org/docs/latest/dashboards/dev-tools/index-dev/ "https://opensearch.org/docs/latest/dashboards/dev-tools/index-dev/") console:

```
PUT housing-index-filtered
{
  "settings": {
    "index.knn": true
  },
  "mappings": {
    "properties": {
      "housing-vector": {
        "type": "knn_vector",
        "dimension": 3,
        "method": {
          "engine": "faiss",
          "name": "hnsw"
        }
      },
      "title": {
        "type": "text"
      },
      "price": {
        "type": "long"
      },
      "location": {
        "type": "geo_point"
      }
    }
  }
}
```

2. To index a single document into _housing-index-filtered_,
   send the following request:

```
POST housing-index-filtered/_doc
{
  "housing-vector": [
    10,
    20,
    30
  ],
  "title": "2 bedroom in downtown Seattle",
  "price": "2800",
  "location": "47.71, 122.00"
}
```

3. To search your data for an apartment in Seattle under a given price and within
   a given distance of a geographical point, send the following request:

```
GET housing-index-filtered/_search
{
  "size": 5,
  "query": {
    "knn": {
      "housing-vector": {
        "vector": [
          0.1,
          0.2,
          0.3
        ],
        "k": 5,
        "filter": {
          "bool": {
            "must": [
              {
                "query_string": {
                  "query": "Find me 2 bedroom apartment in Seattle under $3000 ",
                  "fields": [
                    "title"
                  ]
                }
              },
              {
                "range": {
                  "price": {
                    "lte": 3000
                  }
                }
              },
              {
                "geo_distance": {
                  "distance": "100miles",
                  "location": {
                    "lat": 48,
                    "lon": 121
                  }
                }
              }
            ]
          }
        }
      }
    }
  }
}
```

## Billion scale workloads

Vector search collections support workloads with billions of vectors. You don’t need
to reindex for scaling purposes because auto scaling does this for you. If you have
millions of vectors (or more) with a high number of dimensions and need more than 200
OCUs, contact [AWS Support](https://aws.amazon.com/premiumsupport/ "https://aws.amazon.com/premiumsupport/")
to raise your the maximum OpenSearch Compute Units (OCUs) for your account.

## Limitations

Vector search collections have the following limitations:

- Vector search collections don't support the Apache Lucene ANN engine.
- Vector search collections only support the HNSW algorithm with Faiss and do
  not support IVF and IVFQ.
- Vector search collections don't support the warmup, stats, and model training
  API operations.
- Vector search collections don't support inline or stored scripts.
- Index count information isn't available in the AWS Management Console for vector search
  collections.
- The refresh interval for indexes on vector search collections is 60
  seconds.

## Next steps

Now that you know how to create a vector search collection and index data, you might
want to try some of the following exercises:

- Use the OpenSearch Python client to work with vector search collections. See
  this tutorial on [GitHub](https://github.com/opensearch-project/opensearch-py/blob/main/guides/plugins/knn.md "https://github.com/opensearch-project/opensearch-py/blob/main/guides/plugins/knn.md").
- Use the OpenSearch Java client to work with vector search collections. See this
  tutorial on [GitHub](https://github.com/opensearch-project/opensearch-java/blob/main/guides/plugins/knn.md "https://github.com/opensearch-project/opensearch-java/blob/main/guides/plugins/knn.md").
- Set up LangChain to use OpenSearch as a vector store. LangChain is an open
  source framework for developing applications powered by language models. For
  more information, see the [LangChain documentation](https://python.langchain.com/docs/integrations/vectorstores/opensearch "https://python.langchain.com/docs/integrations/vectorstores/opensearch").
