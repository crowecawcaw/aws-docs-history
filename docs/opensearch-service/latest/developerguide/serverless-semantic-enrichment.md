# About automatic semantic

enrichment

When you create or edit a collection, you can configure automatic semantic enrichment,
which simplifies semantic search implementation and capabilities in Amazon OpenSearch Service. Semantic
search returns query results that incorporate not just keyword matching, but the intent
and contextual meaning of the user's search. For example, if a user searches for "how to
treat a headache", a semantic search system might return the following results:

- Migraine remedies
- Pain management techniques
- Over-the-counter pain relievers
- Natural headache relief methods
  The system understands the underlying intent even when these exact phrases aren't in
  the original query.

Automatic semantic enrichment offers the following benefits:

######

**Simplified implementation**

You don't need machine learning (ML) expertise or complex
integrations.

**Automated process**

Semantic enrichment happens automatically during data ingestion.

**Improved search relevance**

Semantic enrichment enhances the quality and contextual accuracy of search
results.

**Scalability**

Semantic enrichment applies semantic search to large datasets without
manual intervention.

## How it works

To get started with automatic semantic enrichment, you create or edit a collection
and specify which fields in your data require semantic search capabilities. After
you identify fields for semantic search, as data enters OpenSearch Service, the automatic semantic
enrichment process automatically enriches these fields. The enriched data powers
more intelligent and context-aware searches.

###### Note

Consider the following factors when implementing automatic semantic
enrichment:

- Processing overhead: The enrichment process may add processing time
  during ingestion.
- Storage implications: Enriched data requires additional storage
  space.
- Language limitations: Check if the multi-lingual option supports your
  required languages.

Automatic semantic enrichment for serverless offers the following language
options.

English-only option

- Optimized for English language content
- Ideal for applications primarily dealing with English
  text

Multi-lingual option

- Supports the following languages: Arabic, Bengali, Chinese,
  English, Finnish, French, Hindi, Indonesian, Japanese, Korean,
  Persian, Russian, Spanish, Swahili, and Telugu
- Perfect for diverse, international content or multilingual
  applications

## Configuring permissions

for automatic semantic enrichment

Before creating an automated semantic enrichment index, you need to configure the
required permissions. This section explains the permissions needed and how to set
them up.

### IAM policy permissions

Use the following AWS Identity and Access Management (IAM) policy to grant the necessary permissions
for working with automatic semantic enrichment:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AutomaticSemanticEnrichmentPermissions",
 "Effect": "Allow",
 "Action": [
 "aoss:CreateIndex",
 "aoss:GetIndex",
 "aoss:UpdateIndex",
 "aoss:DeleteIndex",
 "aoss:APIAccessAll"
 ],
 "Resource": "*"
 }
 ]
}`

```

**Key permissions**

- The `aoss:*Index` permissions enable index
  management
- The `aoss:APIAccessAll` permission allows
  OpenSearch API operations
- To restrict permissions to a specific collection, replace
  `"Resource": "*"` with the collection's
  ARN

### Configure data

access permissions

To set up an index for automatic semantic enrichment, you must have
appropriate data access policies that grant permission to access index,
pipeline, and model collection resources. For more information about data access
policies, see [Data access control for Amazon OpenSearch Serverless](serverless-data-access.md "serverless-data-access.md"). For the procedure to configure a
data access policy, see [Creating data access policies
(console)](serverless-data-access.md#serverless-data-access-console "serverless-data-access.md#serverless-data-access-console").

#### Data access

permissions

```
[
    {
        "Description": "Create index permission",
        "Rules": [
            {
                "ResourceType": "index",
                "Resource": ["index/`collection_name`/*"],
                "Permission": [
                  "aoss:CreateIndex",
                  "aoss:DescribeIndex",
                  "aoss:UpdateIndex",
                  "aoss:DeleteIndex"
                ]
            }
        ],
        "Principal": [
            "arn:aws:iam::`account_id`:role/`role_name`"
        ]
    },
    {
        "Description": "Create pipeline permission",
        "Rules": [
            {
                "ResourceType": "collection",
                "Resource": ["collection/`collection_name`"],
                "Permission": [
                  "aoss:CreateCollectionItems",
                  "aoss:DescribeCollectionItems"
                ]
            }
        ],
        "Principal": [
            "arn:aws:iam::`account_id`:role/`role_name`"
        ]
    },
    {
        "Description": "Create model permission",
        "Rules": [
            {
                "ResourceType": "model",
                "Resource": ["model/`collection_name`/*"],
                "Permission": ["aoss:CreateMLResource"]
            }
        ],
        "Principal": [
            "arn:aws:iam::`account_id`:role/`role_name`"
        ]
    },
]
```

#### Network

access permissions

To allow service APIs to access private collections, you must configure
network policies that permit the required access between the service API and
the collection. For more information about network policies, see [Network access for Amazon OpenSearch Serverless](serverless-network.md "serverless-network.md") .

```
[
   {
      "Description":"Enable automatic semantic enrichment in a private collection",
      "Rules":[
         {
            "ResourceType":"collection",
            "Resource":[
               "collection/`collection_name`"
            ]
         }
      ],
      "AllowFromPublic":false,
      "SourceServices":[
         "aoss.amazonaws.com"
      ],
   }
]
```

###### To configure network access permissions for a private

collection

1. Sign in to the OpenSearch Service console at [https://console.aws.amazon.com/aos/home](https://console.aws.amazon.com/aos/home "https://console.aws.amazon.com/aos/home").
2. In the left navigation, choose _Network
   policies_. Then do one of the following:
   - Choose an existing policy name and choose
     _Edit_
   - Choose _Create network policy_ and
     configure the policy details

3. In the _Access type_ area, choose
   _Private (recommended)_, and then select
   _AWS service private access_.
4. In the search field, choose _Service_, and then
   choose _aoss.amazonaws.com_.
5. In the _Resource type_ area, select the
   _Enable access to OpenSearch endpoint_
   box.
6. For _Search collection(s), or input specific prefix
   term(s)_, in the search field, select
   _Collection Name_. Then enter or select the
   name of the collections to associate with the network policy.
7. Choose _Create_ for a new network policy or
   _Update_ for an existing network
   policy.

## Index set up example

For a practical example, refer to the blog post [https://aws.amazon.com/blogs/big-data/boosting-search-relevance-automatic-semantic-enrichment-in-amazon-opensearch-serverless/](https://aws.amazon.com/blogs/big-data/boosting-search-relevance-automatic-semantic-enrichment-in-amazon-opensearch-serverless/ "https://aws.amazon.com/blogs/big-data/boosting-search-relevance-automatic-semantic-enrichment-in-amazon-opensearch-serverless/")
for index setup for product catalog search using automatic semantic enrichment.
