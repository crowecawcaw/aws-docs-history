# Automatic semantic enrichment for

Amazon OpenSearch Service

Amazon OpenSearch Service uses word-to-word matching (lexical search) to find results, similar to other
traditional search engines. This approach works well for specific queries like product codes
or model numbers, but struggles with abstract searches where understanding user intent
becomes crucial. For example, when you search for "shoes for the beach," lexical search
matches individual words "shoes," "beach," "for," and "the" in catalog items, potentially
missing relevant products like "water-resistant sandals" or "surf footwear" that don't
contain the exact search terms.

Automatic Semantic Enrichment solves this limitation by considering both keyword matches
and the contextual meaning behind searches. This feature understands search intent and
improves search relevance by up to 20%. Enable this feature for text fields in your index to
enhance search results.

###### Note

AAutomatic semantic enrichment is available for OpenSearch Service domains running version 2.19 or later.
Additionally, domains with OpenSearch version 2.19 also need to be on the latest service software version update.

## How it works

The enrichment process analyzes designated text fields and generates semantic
embeddings that capture meaning and context. These embeddings help the search engine
understand relationships between concepts, synonyms, and related terms even when they
don't appear in your search query. For example, if a user searches for "how to treat a
headache", a semantic search system might return the following results:

- Migraine remedies
- Pain management techniques
- Over-the-counter pain relievers
- Natural headache relief methods

The system understands the underlying intent even when these exact phrases aren't in
the original query.

Automatic semantic enrichment offers the following benefits:

######

**Simplified implementation**

You don't need machine learning expertise or complex integrations to
implement semantic search capabilities.

**Index-level configuration**

Semantic enrichment is configured at the index level during creation,
giving you granular control over which data receives semantic
processing.

**Minimal impact on search latency**

Automatic Semantic Enrichment stores sparse encodings directly in your
index during indexing. You don't need separate KNN indices. Your searches
maintain their original speed while delivering enhanced results.

**Automated process**

Semantic enrichment happens automatically during data ingestion without
requiring manual intervention.

**Improved search relevance**

Semantic enrichment enhances the quality and contextual accuracy of search
results by understanding user intent.

**Scalability**

Semantic enrichment applies semantic search capabilities to large datasets
without manual intervention.

### Requirements and

considerations

Before implementing automatic semantic enrichment, consider the following
requirements and limitations:

######

**Version requirements**

Automatic semantic enrichment is available for Amazon OpenSearch Service version 2.19
and later. For existing domains running Amazon OpenSearch Service version 2.19 or 3.1,
you must update to the latest patch version to use this feature.

**Public domains only**

Automatic Semantic Enrichment is available only for public domains.
You can't use it with VPC domains.

**Processing overhead**

The enrichment process adds minimal processing time during data
ingestion as the system generates semantic embeddings for designated
fields.

**Storage implications**

Enriched data requires additional storage space for the semantic
embeddings generated alongside your original data.

**Language support**

Automatic semantic enrichment for managed domains offers the following
language options:

English-only option

- Ideal for applications primarily dealing with English
  text

Multi-lingual option

- Supports the following languages: Arabic, Bengali, Chinese,
  English, Finnish, French, Hindi, Indonesian, Japanese, Korean,
  Persian, Russian, Spanish, Swahili, and Telugu
- Perfect for diverse, international content or multilingual
  applications

#### Pricing

With Automatic Semantic Enrichment, you pay only for the resources your
workload consumes. The compute capacity is measured in OpenSearch Compute Units
(OCUs). Check the pricing details for your specific Region and pricing
illustration on the [https://aws.amazon.com/opensearch-service/pricing/](https://aws.amazon.com/opensearch-service/pricing/ "https://aws.amazon.com/opensearch-service/pricing/")OpenSearch Service pricing page.

## Index set up example

For a practical example, refer to the blog post [https://aws.amazon.com/blogs/big-data/boosting-search-relevance-automatic-semantic-enrichment-in-amazon-opensearch-serverless/](https://aws.amazon.com/blogs/big-data/boosting-search-relevance-automatic-semantic-enrichment-in-amazon-opensearch-serverless/ "https://aws.amazon.com/blogs/big-data/boosting-search-relevance-automatic-semantic-enrichment-in-amazon-opensearch-serverless/")
on index setup for product catalog search using automatic semantic enrichment. Although the blog focuses on OpenSearch Serverless,
the approach applies to managed clusters as well. Use this example as a starting point, then test with your own workload to
validate search relevance improvements.

## Configuring permissions for

automatic semantic enrichment

Before creating an index with automatic semantic enrichment, you need to configure the
required permissions. This section explains the permissions needed for different index
operations and how to set them up for both AWS Identity and Access Management (IAM) and fine-grained access
control scenarios.

### IAM

permissions

The following IAM permissions are required for automatic semantic enrichment
operations. These permissions vary depending on the specific index operation you
want to perform.

#### CreateIndex API permissions

To create an index with automatic semantic enrichment, you need the following
IAM permissions:

- `es:CreateIndex` – Create an index with semantic
  enrichment capabilities.
- `es:ESHttpHead` – Perform HEAD requests to check
  index existence.
- `es:ESHttpPut` – Perform PUT requests for index
  creation.
- `es:ESHttpPost` – Perform POST requests for index
  operations.

#### UpdateIndex API permissions

To update an existing index with automatic semantic enrichment, you need the
following IAM permissions:

- `es:UpdateIndex` – Update index settings and
  mappings.
- `es:ESHttpPut` – Perform PUT requests for index
  updates.
- `es:ESHttpGet` – Perform GET requests to retrieve
  index information.
- `es:ESHttpPost` – Perform POST requests for index
  operations.

#### GetIndex

API permissions

To retrieve information about an index with automatic semantic enrichment, you
need the following IAM permissions:

- `es:GetIndex` – Retrieve index information and
  settings.
- `es:ESHttpGet` – Perform GET requests to retrieve
  index data.

#### DeleteIndex API permissions

To delete an index with automatic semantic enrichment, you need the following
IAM permissions:

- `es:DeleteIndex` – Delete an index and its semantic
  enrichment components.
- `es:ESHttpDelete` – Perform DELETE requests for
  index removal.

### Sample IAM

policy

The following sample identity-based access policy provides the permissions
necessary for a user to manage indexes with automatic semantic enrichment:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AllowSemanticEnrichmentIndexOperations",
            "Effect": "Allow",
            "Action": [
                "es:CreateIndex",
                "es:UpdateIndex",
                "es:GetIndex",
                "es:DeleteIndex",
                "es:ESHttpHead",
                "es:ESHttpGet",
                "es:ESHttpPut",
                "es:ESHttpPost",
                "es:ESHttpDelete"
            ],
            "Resource": "arn:aws:es:`aws-region`:`111122223333`:domain/`domain-name`/*"
        }
    ]
}
```

Replace `aws-region`, `111122223333`, and
`domain-name` with your specific values. You can
further restrict access by specifying particular index patterns in the resource
ARN.

### Fine-grained

access control permissions

If your Amazon OpenSearch Service domain has fine-grained access control enabled, you need
additional permissions beyond the IAM permissions. The following permissions are
required for each index operation.

#### CreateIndex API permissions

When fine-grained access control is enabled, the following additional
permissions are required for creating an index with automatic semantic
enrichment:

- `indices:admin/create` – Create index
  operations.
- `indices:admin/mapping/put` – Create and update
  index mappings.
- `cluster:admin/opensearch/ml/create_connector` –
  Create machine learning connectors for semantic processing.
- `cluster:admin/opensearch/ml/register_model` –
  Register machine learning models for semantic enrichment.
- `cluster:admin/ingest/pipeline/put` – Create ingest
  pipelines for data processing.
- `cluster:admin/search/pipeline/put` – Create search
  pipelines for query processing.

#### UpdateIndex API permissions

When fine-grained access control is enabled, the following additional
permissions are required for updating an index with automatic semantic
enrichment:

- `indices:admin/get` – Retrieve index
  information.
- `indices:admin/settings/update` – Update index
  settings.
- `indices:admin/mapping/put` – Update index
  mappings.
- `cluster:admin/opensearch/ml/create_connector` –
  Create machine learning connectors.
- `cluster:admin/opensearch/ml/register_model` –
  Register machine learning models.
- `cluster:admin/ingest/pipeline/put` – Create ingest
  pipelines.
- `cluster:admin/search/pipeline/put` – Create search
  pipelines.
- `cluster:admin/ingest/pipeline/get` – Retrieve
  ingest pipeline information.
- `cluster:admin/search/pipeline/get` – Retrieve
  search pipeline information.

#### GetIndex

API permissions

When fine-grained access control is enabled, the following additional
permissions are required for retrieving information about an index with
automatic semantic enrichment:

- `indices:admin/get` – Retrieve index
  information.
- `cluster:admin/ingest/pipeline/get` – Retrieve
  ingest pipeline information.
- `cluster:admin/search/pipeline/get` – Retrieve
  search pipeline information.

#### DeleteIndex API permissions

When fine-grained access control is enabled, the following additional
permission is required for deleting an index with automatic semantic
enrichment:

- `indices:admin/delete` – Delete index
  operations.
