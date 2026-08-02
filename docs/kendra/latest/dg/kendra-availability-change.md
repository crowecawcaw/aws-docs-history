Amazon Kendra is no longer open to new customers. For capabilities similar to Amazon Kendra, explore Amazon Bedrock Knowledge Bases. [Learn more](kendra-availability-change.md "kendra-availability-change.md").

# Amazon Kendra availability change

## Overview

After careful consideration, we have made the decision to put Amazon Kendra into
Maintenance Mode, effective June 30, 2026. As of this date, there is no new feature
or capability development for the service, and as of July 30, 2026, the service is
no longer open to new customers.

During Maintenance Mode, the service remains fully supported and AWS will continue to
provide bug fixes and security updates for existing customers, however new feature requests
will no longer be considered.

We recommend that customers migrate their Kendra applications and implement any new
search applications on Amazon Bedrock Managed Knowledge Base (BMKB) for similar
capabilities to Kendra and more advanced features for generative AI and agentic AI use
cases. Bedrock Managed Knowledge Base is a fully managed RAG solution, with built-in
connectors, smart parsing, managed vector store with hybrid search, along with the
ability to generate responses (with a Retrieve and Generate API) and do multi-step
reasoning across multiple knowledge bases (with an Agentic Retrieval API). BMKB also
gives you the ability to adjust the chunking strategies and embedding models to optimize
for your specific application as well as choose the foundation model for response
generation. This new level of features and flexibility comes with predictable costs based
on the size of the knowledge base ingested, the number of queries performed and the LLM
usage.

## Migration Guidance

Migrating from Amazon Kendra to Amazon Bedrock Managed Knowledge Base (BMKB) is
achievable for most enterprise search and RAG workloads with some careful planning. Not
all Kendra features are directly available in Bedrock Managed Knowledge Base, but many
can be implemented through workarounds. This guide provides a comprehensive, step-by-step
migration path for existing Kendra customers to transition their applications to BMKB,
including architecture mapping, API translation, code examples, feature gap analysis, and
recommended workarounds.

### Amazon Bedrock Managed Knowledge Base Features

BMKB manages the entire RAG pipeline end-to-end. It supports embedding models
including Amazon Titan Text Embeddings V2, Cohere Embed English v3, Cohere Embed
Multilingual v3, Cohere Embed v4, and Amazon Nova Multimodal Embeddings—all
fixed at 1024 dimensions with float32 vectors. The managed vector store is fully
operated by Bedrock, eliminating the need to provision or manage OpenSearch, Aurora,
or other vector databases. Chunking strategies include Default (fixed-size at
approximately 300 tokens), Fixed-size (configurable maxTokens and
overlapPercentage), Hierarchical (parent-child with level configurations), and No
Chunking; semantic chunking is not supported for managed knowledge bases.

BMKB currently supports seven data source connectors: Amazon S3, Confluence,
Microsoft SharePoint, Web Crawler, Google Drive, Microsoft OneDrive, and a Custom
connector. The service always performs hybrid search (keyword plus semantic) and does
not offer semantic-only search mode.

Architecture Comparison between Amazon Kendra and Bedrock Managed Knowledge Base| Feature | Kendra | Bedrock Managed Knowledge Base |
| --- | --- | --- |
| Native connectors | 32+ connectors | 7 connectors |
| Embedding | Managed internally | Customer-selectable (Titan V2, Cohere, Nova) |
| Vector store | Managed internally | Fully managed by Bedrock |
| Search type | Keyword, semantic, or hybrid | Hybrid (keyword + semantic) |
| RAG support | Requires external LLM integration | Native RetrieveAndGenerate API |
| Agentic retrieval | Not available | Native multi-iteration retrieval |
| Maximum results | 100 passages (Retrieve API) | 100 results (Retrieve API) |

## Migration Steps

### Amazon Bedrock Managed Knowledge Base Setup

#### Step 1: Configure IAM Roles

Create an IAM role that grants Bedrock permission to access your data sources
and invoke embedding models. The trust policy must allow
bedrock.amazonaws.com to assume the role, and the permissions policy must include
access to your S3 buckets and the selected embedding model.

IAM Configuration (Python code):

```

import boto3
import json

iam = boto3.client('iam')

trust_policy = {
    "Version": "2012-10-17",
    "Statement": [{
        "Effect": "Allow",
        "Principal": {"Service": "bedrock.amazonaws.com"},
        "Action": "sts:AssumeRole"
    }]
}

iam.create_role(
    RoleName="BedrockKBRole",
    AssumeRolePolicyDocument=json.dumps(trust_policy),
    Description="Role for Bedrock Managed Knowledge Base"
)

permissions_policy = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": ["s3:GetObject", "s3:ListBucket"],
            "Resource": [
                "arn:aws:s3:::your-bucket-name",
                "arn:aws:s3:::your-bucket-name/*"
            ]
        },
        {
            "Effect": "Allow",
            "Action": ["bedrock:InvokeModel"],
            "Resource": ["arn:aws:bedrock:*::foundation-model/amazon.titan-embed-text-v2:0"]
        }
    ]
}

iam.put_role_policy(
    RoleName="BedrockKBRole",
    PolicyName="BedrockKBPermissions",
    PolicyDocument=json.dumps(permissions_policy)
)

```

#### Step 2: Create a Managed Knowledge Base

Use the CreateKnowledgeBase API with type MANAGED to create the knowledge
base:

```

import boto3

bedrock_agent = boto3.client("bedrock-agent", region_name="us-east-1")

response = bedrock_agent.create_knowledge_base(
    name="my-managed-kb",
    description="Migrated from Kendra index",
    roleArn="arn:aws:iam::123456789012:role/BedrockKBRole",
    knowledgeBaseConfiguration={
        "type": "MANAGED",
        "managedKnowledgeBaseConfiguration": {
            "embeddingModelArn": "arn:aws:bedrock:us-east-1::foundation-model/amazon.titan-embed-text-v2:0",
            "embeddingModelConfiguration": {
                "bedrockEmbeddingModelConfiguration": {
                    "embeddingDataType": "FLOAT32"
                }
            }
        }
    }
)

kb_id = response["knowledgeBase"]["knowledgeBaseId"]
print(f"Created knowledge base: {kb_id}")

```

#### Step 3: Configure Data Sources

Create an S3 data source with the managed connector configuration:

```

response = bedrock_agent.create_data_source(
    knowledgeBaseId=kb_id,
    name="my-s3-data-source",
    description="Product documentation from S3",
    dataSourceConfiguration={
        "type": "MANAGED_KNOWLEDGE_BASE_CONNECTOR",
        "managedKnowledgeBaseConnectorConfiguration": {
            "connectorParameters": {
                "type": "S3",
                "version": "1",
                "connectionConfiguration": {
                    "bucketName": "your-bucket-name",
                    "bucketOwnerAccountId": "123456789012"
                },
                "filterConfiguration": {
                    "inclusionPrefixes": ["documents/"]
                }
            }
        }
    },
    vectorIngestionConfiguration={
        "parsingConfiguration": {
            "parsingStrategy": "SMART_PARSING"
        }
    }
)

data_source_id = response["dataSource"]["dataSourceId"]
print(f"Created data source: {data_source_id}")

```

###### Note

CreateDataSource is asynchronous for Managed Knowledge Bases. The data
source status transitions from CREATING to AVAILABLE, typically within 2–5
minutes. Do not proceed to ingestion until the status is AVAILABLE.

#### Step 4: Start and Monitor Ingestion

Trigger document ingestion and poll for completion:

```

import time

ingestion_response = bedrock_agent.start_ingestion_job(
    knowledgeBaseId=kb_id,
    dataSourceId=data_source_id,
    description="Initial ingestion"
)

ingestion_job_id = ingestion_response["ingestionJob"]["ingestionJobId"]
print(f"Started ingestion job: {ingestion_job_id}")

while True:
    job_response = bedrock_agent.get_ingestion_job(
        knowledgeBaseId=kb_id,
        dataSourceId=data_source_id,
        ingestionJobId=ingestion_job_id
    )
    job = job_response["ingestionJob"]
    status = job["status"]
    stats = job.get("statistics", {})

    print(f"Status: {status} | Scanned: {stats.get('numberOfDocumentsScanned', 0)} | "
          f"Indexed: {stats.get('numberOfNewDocumentsIndexed', 0)} | "
          f"Failed: {stats.get('numberOfDocumentsFailed', 0)}")

    if status == "COMPLETE":
        print("Ingestion complete!")
        break
    elif status in ("FAILED", "STOPPED"):
        print(f"Ingestion {status}: {job.get('failureReasons', [])}")
        break

    time.sleep(30)

```

## API Migration Mapping and Code Examples

### API Operation Mapping

API Operation Mapping from Kendra to BMKB| Operation | Kendra API | BMKB API | Client |
| --- | --- | --- | --- |
| Create index/KB | kendra.create\_index() | bedrock-agent.create\_knowledge\_base() | kendra → bedrock-agent |
| Add data source | kendra.create\_data\_source(Type="S3") | bedrock-agent.create\_data\_source() | kendra → bedrock-agent |
| Sync/ingest docs | kendra.start\_data\_source\_sync\_job() | bedrock-agent.start\_ingestion\_job() | kendra → bedrock-agent |
| Batch add docs | kendra.batch\_put\_document() | Not directly supported (use S3 upload + ingestion) | kendra → S3 + bedrock-agent |
| Retrieve passages | kendra.retrieve(QueryText=...) | bedrock-agent-runtime.retrieve() | kendra → bedrock-agent-runtime |
| Search with filters | AttributeFilter: {"EqualsTo": {...}} | filter: {"equals": {...}} | Same pattern, different syntax |
| RAG generation | N/A (external LLM required) | bedrock-agent-runtime.retrieve\_and\_generate() | New capability |

### Migrating the Retrieve API

Before (Kendra):

```

kendra_client = boto3.client("kendra")

response = kendra_client.retrieve(
    IndexId="your-kendra-index-id",
    QueryText="How do I configure VPC endpoints?",
    AttributeFilter={
        "EqualsTo": {
            "Key": "_category",
            "Value": {"StringValue": "networking"}
        }
    },
    PageSize=10
)

for item in response["ResultItems"]:
    print(item["DocumentTitle"])
    print(item["Content"])

```

After (BMKB):

```

bedrock_runtime = boto3.client("bedrock-agent-runtime", region_name="us-east-1")

response = bedrock_runtime.retrieve(
    knowledgeBaseId="your-kb-id",
    retrievalQuery={
        "text": "How do I configure VPC endpoints?"
    },
    retrievalConfiguration={
        "managedSearchConfiguration": {
            "numberOfResults": 10,
            "filter": {
                "equals": {
                    "key": "category",
                    "value": "networking"
                }
            }
        }
    }
)

for result in response["retrievalResults"]:
    print(f"Score: {result['score']}")
    print(f"Content: {result['content']['text']}")
    print(f"Source: {result['location']['s3Location']['uri']}")

```

The key differences are: the query text moves from a top-level parameter to a
nested retrievalQuery.text field; AttributeFilter becomes filter within
managedSearchConfiguration; and results include a relevance score field.

### Using RetrieveAndGenerate for RAG

BMKB provides a native RAG capability that eliminates the need to separately call
an LLM after retrieval:

```

response = bedrock_runtime.retrieve_and_generate(
    input={
        "text": "Explain how to configure VPC endpoints for S3 access"
    },
    retrieveAndGenerateConfiguration={
        "type": "KNOWLEDGE_BASE",
        "knowledgeBaseConfiguration": {
            "knowledgeBaseId": "your-kb-id",
            "modelArn": "arn:aws:bedrock:us-east-1::foundation-model/anthropic.claude-3-sonnet-20240229-v1:0",
            "retrievalConfiguration": {
                "managedSearchConfiguration": {
                    "numberOfResults": 5
                }
            }
        }
    }
)

# Generated answer with citations
print(response["output"]["text"])

# Source citations
for citation in response.get("citations", []):
    for ref in citation.get("retrievedReferences", []):
        print(f"Source: {ref['location']['s3Location']['uri']}")

```

This API returns a generated natural language response along with citations
pointing back to the source documents, providing built-in RAG that Kendra does not
natively offer.

### Metadata Filter Syntax Translation

Metadata Filter Operator Mapping| Kendra AttributeFilter | BMKB Filter | Notes |
| --- | --- | --- |
| EqualsTo | equals | Direct mapping |
| ContainsAll | in (partial) | BMKB uses set membership |
| ContainsAny | in | Direct mapping |
| GreaterThan | greaterThan | Direct mapping |
| LessThan | lessThan | Direct mapping |
| GreaterThanOrEquals | greaterThanOrEquals | Direct mapping |
| LessThanOrEquals | lessThanOrEquals | Direct mapping |
| NotFilter | notIn / notEquals | Use appropriate negation |
| AndAllFilters | andAll | Direct mapping |
| OrAllFilters | orAll | Direct mapping |

###### Note

BMKB does not support startsWith or stringContains operators for managed
knowledge bases. If your Kendra application uses wildcard or substring matching
in filters, you will need to restructure your metadata schema to use exact-match
or set-membership patterns instead.

## Feature Gaps and Workarounds

Not all Kendra features are available in BMKB. Query Suggestions, Faceted Search,
Custom Synonyms, Spell Checking, Incremental Learning, and Document Enrichment are
features that require workarounds in BMKB. This section discusses those
workarounds.

**Query Suggestions (Autocomplete)**

Kendra provides the GetQuerySuggestions API that returns autocomplete
suggestions based on indexed document vocabulary. BMKB does not currently
offer this capability.

**Workaround:** Implement a custom
autocomplete layer using Amazon OpenSearch Service with its built-in
suggester functionality, or use an LLM-based query completion service. You
can also leverage Bedrock Agents to reformulate partial queries before
retrieval. A practical approach is to maintain a separate OpenSearch index of
common query terms extracted from your document corpus and call its suggest
API from your frontend before invoking BMKB retrieval.

**Faceted Search**

Kendra supports document attribute facets via the Facets parameter in the
Query API, displaying up to 10 facet values per facet with document counts.
BMKB's architecture does not support faceted search.

**Workaround:** Simulate faceted navigation
using metadata filtering. Tag documents with structured metadata attributes
(department, author, document type, date range) in .metadata.json sidecar
files. Present filter options in your application UI based on your known
metadata schema, and apply the corresponding filter operators at query time.
While this does not provide dynamic facet counts, it enables users to narrow
results by category:

```

# Simulating faceted search with metadata filters
response = bedrock_runtime.retrieve(
    knowledgeBaseId="your-kb-id",
    retrievalQuery={"text": "security best practices"},
    retrievalConfiguration={
        "managedSearchConfiguration": {
            "numberOfResults": 10,
            "filter": {
                "andAll": [
                    {"equals": {"key": "department", "value": "engineering"}},
                    {"equals": {"key": "doc_type", "value": "policy"}}
                ]
            }
        }
    }
)

```

**Custom Synonyms**

Kendra allows building a custom mapping of business-specific terms that are
mapped to other terms for matching search results via a thesaurus file. BMKB
does not currently support custom synonyms.

**Workaround:** Build a lightweight synonym
expansion service in front of your BMKB queries:

- Maintain your existing Kendra thesaurus file (or a synonym
  dictionary in DynamoDB/S3)
- Before calling the BMKB Retrieve or RetrieveAndGenerate API,
  expand the user's query by appending matched synonyms
- Example: If the user queries "DNS issues", your app rewrites it to
  "DNS Route53 issues" before sending to BMKB

This works particularly well because BMKB always uses hybrid search
(keyword + semantic), so adding synonym terms to the query text will match on
both keyword and semantic dimensions.

**Spell Checking**

Kendra provides automatic spell corrections based on indexed document
vocabulary via SpellCorrectionConfiguration. BMKB does not currently support
spell checking.

**Workaround:** Add a preprocessing layer
before sending queries to BMKB. Use an AWS Lambda function that invokes a
spell-correction library (such as SymSpell or TextBlob) or calls an LLM for
query correction:

```

import boto3

lambda_client = boto3.client("lambda")

def correct_and_retrieve(query_text, kb_id):
    # Step 1: Spell-correct the query using a Lambda function
    correction_response = lambda_client.invoke(
        FunctionName="spell-correction-function",
        Payload=json.dumps({"query": query_text})
    )
    corrected_query = json.loads(correction_response["Payload"].read())["corrected"]

    # Step 2: Query BMKB with corrected text
    bedrock_runtime = boto3.client("bedrock-agent-runtime")
    return bedrock_runtime.retrieve(
        knowledgeBaseId=kb_id,
        retrievalQuery={"text": corrected_query},
        retrievalConfiguration={"managedSearchConfiguration": {"numberOfResults": 5}}
    )

```

**Incremental Learning**

Kendra supports the SubmitFeedback API for click-through signals and
relevance feedback to improve ranking over time. BMKB does not offer this
capability.

**Workaround:** Use BMKB's reranking models
to improve relevance at query time. Build a custom feedback loop that stores
user click and rating signals in an external data store (such as DynamoDB),
and use those signals to adjust metadata boost weights or reranking
parameters. For long-term improvement, consider periodically fine-tuning your
embedding model based on collected relevance feedback.

**Custom Document Enrichment**

Kendra supports pre-extraction and post-extraction Lambda hooks that
manipulate document content and metadata during ingestion. BMKB uses Smart
Parsing for document processing but does not offer equivalent Lambda
hooks.

**Workaround:** Implement a preprocessing
pipeline using AWS Step Functions or Lambda that transforms documents
before they are placed in S3 for BMKB ingestion. This pipeline can perform
content extraction, metadata enrichment, PII redaction, or format conversion
before the documents reach the BMKB data source bucket.

## Data Source Migration Strategy

### Connector Coverage Gap

Kendra supports 32 native connectors while BMKB supports 7. For data sources not
directly supported by BMKB, the recommended approach is to export content to Amazon
S3 and configure an S3 data source in BMKB.

**Migration pattern for unsupported connectors:**
Create an automated pipeline (using AWS Lambda, Step Functions, or Amazon
EventBridge Scheduler) that periodically extracts content from the source system via
its API, writes documents to an S3 bucket with appropriate metadata JSON sidecar
files, and triggers a BMKB ingestion job. This replicates the periodic sync behavior
of Kendra connectors.

### Metadata Migration

Kendra document attributes must be translated to BMKB metadata format. In Kendra,
attributes are defined at the index level and attached to documents during ingestion.
In BMKB, metadata is defined via .metadata.json sidecar files stored alongside
source documents in S3, with a maximum size of 10 KB per file. Each attribute must
be typed as STRING, NUMBER, or BOOLEAN.

### Chunking Strategy Selection

When migrating from Kendra (which handles chunking internally), you must explicitly
choose a chunking strategy for BMKB. For most migration scenarios, the Fixed-size
strategy with 200 tokens and 30% overlap provides a good starting point. If your
documents have clear hierarchical structure (chapters, sections, subsections),
consider Hierarchical chunking for improved retrieval of both broad context and
specific details.

## Testing and Validation

To evaluate performance, run both Kendra and BMKB in parallel. Send identical queries
to both services and compare results using the following dimensions: relevance quality
(measured by NDCG or MRR against a golden test set), latency (p50, p95, p99 response
times), throughput (queries per second under load), and completeness (percentage of
expected documents retrieved).

Create a test harness that evaluates retrieval quality:

```

def compare_retrieval(query, kendra_index_id, bmkb_kb_id):
    # Query Kendra
    kendra_results = kendra_client.retrieve(
        IndexId=kendra_index_id,
        QueryText=query,
        PageSize=10
    )

    # Query BMKB
    bmkb_results = bedrock_runtime.retrieve(
        knowledgeBaseId=bmkb_kb_id,
        retrievalQuery={"text": query},
        retrievalConfiguration={
            "managedSearchConfiguration": {"numberOfResults": 10}
        }
    )

    # Compare overlap in top-10 results
    kendra_docs = {r["DocumentId"] for r in kendra_results["ResultItems"]}
    bmkb_docs = {r["location"]["s3Location"]["uri"] for r in bmkb_results["retrievalResults"]}

    overlap = len(kendra_docs.intersection(bmkb_docs))
    print(f"Query: {query}")
    print(f"Result overlap: {overlap}/10 documents in common")
    return overlap

```

Before switching production traffic to BMKB, verify the following: all data sources
are ingested and up-to-date with no failed documents; metadata filters produce expected
results for all application filter patterns; access control workarounds correctly
restrict unauthorized access; relevance benchmarks meet or exceed Kendra baseline
quality; application error handling correctly processes BMKB response formats; and
monitoring and alerting are configured for BMKB API errors and latency.

## Summary

Migrating from Amazon Kendra to Bedrock Managed Knowledge Base requires two
primary efforts: re-ingesting data sources into BMKB and rewriting application code to
use BMKB APIs. While BMKB introduces powerful RAG-native capabilities including
RetrieveAndGenerate and agentic retrieval, customers using enterprise search features
such as faceting, query suggestions, custom synonyms, and incremental learning will need
to implement workarounds as described in this guide.

Please contact [AWS
Support](https://console.aws.amazon.com/support "https://console.aws.amazon.com/support") with any additional questions.
