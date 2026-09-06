

# Using DynamoDB as a storage backend for Strands Agents
<a name="ddb-strands-storage"></a>

[Strands Agents](https://strandsagents.com/) is an open source SDK that takes a model-driven approach to building AI agents in a few lines of code, with first-class support for Amazon Bedrock and other model providers. Among its building blocks is a unified storage interface: a byte-oriented contract (`write`, `read`, `delete`, `list`) that every stateful subsystem in the SDK speaks. The Session Manager persists conversation snapshots through it, the Memory Manager stores long-term memories through it, and the context offloader and transcripts use the same operations.

The [strands-dynamodb-storage](https://github.com/aws/strands-dynamodb-storage) package implements that contract on a single DynamoDB table, for both Python and TypeScript. The SDK's `/`-separated storage keys map directly onto the DynamoDB key model: a key's first two segments become the partition key and the remainder becomes the sort key, so point operations are single-item calls and listing a prefix is a native partition `Query`, never a table scan.

## Key features
<a name="strands-key-features"></a>

One table for all agent state  
A single `DynamoDBStorage` instance backs session persistence, long-term memory, transcripts, and context offloading, each namespaced under its own key prefix.

Semantic memory search  
With a vector index on the table, memories can be written with embeddings and recalled by meaning through the `SearchVectors` API. See [Semantic long-term memory with vector indexes](#strands-semantic-memory).

Amazon S3 offload for large values  
Offload is opt-in: pass a bucket name on the constructor, and values above the 400 KB DynamoDB item size limit are transparently offloaded to Amazon Simple Storage Service, with a small pointer item remaining in the table.

Optional compression and Time to Live  
Optional gzip compression keeps compressible values inline at lower cost. Optional Time to Live stamps a DynamoDB-native expiry attribute, and reads and listings filter items whose expiry has already passed.

Multi-tenant prefixes  
A constructor-bound key prefix pins every operation inside its own key space, so two tenants sharing a table resolve the same logical key to physically distinct partitions.

## Prerequisites
<a name="strands-prerequisites"></a>
+ An AWS account with permissions to create DynamoDB tables (and optionally Amazon S3 buckets, if you configure large-value offload)
+ Python 3.10 or later with `strands-agents` 1.48.0 or later, or Node.js 20 or later with `@strands-agents/sdk` 1.10.0 or later
+ AWS credentials configured (see the AWS documentation for credential setup options)
+ For semantic memory: access to an embeddings model such as Amazon Titan Text Embeddings V2 in Amazon Bedrock, and a table created with a vector index (see [Using vector indexes in DynamoDB](VectorSearch.md))

## Installation
<a name="strands-installation"></a>

Install the package from PyPI:

```
pip install strands-dynamodb-storage "strands-agents>=1.48.0"
```

Or from npm for TypeScript (the TypeScript package is a feature-parity mirror):

```
npm install strands-dynamodb-storage
```

## Create the table
<a name="strands-table-setup"></a>

The package holds no `CreateTable` permission and never creates infrastructure: you create the table in advance, with your own tagging, backup, and encryption settings applied. A table with a string partition key `pk` and a string sort key `sk` is the only requirement:

```
aws dynamodb create-table \
  --table-name agent-storage \
  --attribute-definitions AttributeName=pk,AttributeType=S AttributeName=sk,AttributeType=S \
  --key-schema AttributeName=pk,KeyType=HASH AttributeName=sk,KeyType=RANGE \
  --billing-mode PAY_PER_REQUEST
```

If you plan to use semantic memory, declare the vector index in this same command: an index's name, dimensions, and distance function cannot be changed after creation, so size the dimensions to your embedding model. The [package README](https://github.com/aws/strands-dynamodb-storage) shows the full call that declares the index.

## Persist agent sessions
<a name="strands-session-persistence"></a>

Hand the storage to your agent's session manager. The SDK namespaces the keys, snapshots the conversation on every invocation, and restores it when the same session returns:

```
from strands import Agent
from strands.session import SnapshotSessionManager
from strands_dynamodb_storage import DynamoDBStorage

storage = DynamoDBStorage("agent-storage", region_name="us-east-1")
session = SnapshotSessionManager(session_id="user-42", storage=storage)

agent = Agent(session_manager=session)
agent("Where did we leave off?")
```

You can also set storage once on the `Agent` itself. Every subsystem that accepts a storage then inherits it, each namespaced under its own key prefix, so one table carries the whole agent's state:

```
from strands.vended_plugins.context_offloader import ContextOffloader

agent = Agent(
    storage=storage,
    session_manager=SnapshotSessionManager(),  # persists under session/
    plugins=[ContextOffloader()],              # offloads oversized tool results under offloader/
)
```

The byte contract is also available directly. The contract is async: inside an agent the SDK drives it for you, and in a plain script you wrap the calls in `asyncio.run`:

```
import asyncio


async def main():
    await storage.write("session/user-42/notes", b"prefers aisle seats")
    keys = await storage.list("session/user-42/")


asyncio.run(main())
```

## Semantic long-term memory with vector indexes
<a name="strands-semantic-memory"></a>

Session persistence solves half of the memory problem: your agent survives a restart and resumes the conversation. The harder half is recalling something a user told the agent weeks ago, in a new conversation that shares no keys with the old one, and that requires searching memories by meaning rather than by key. DynamoDB vector indexes bring nearest-neighbor search to the same table that holds your agent's state (see [Using vector indexes in DynamoDB](VectorSearch.md)).

The following examples embed text with Amazon Titan Text Embeddings V2 through Amazon Bedrock. The model returns 1,024-dimension vectors by default, so the index for these examples is created with 1,024 dimensions. The following code defines the `embed()` function that the remaining examples use:

```
import json

import boto3

bedrock = boto3.client("bedrock-runtime", region_name="us-east-1")


def embed(text):
    response = bedrock.invoke_model(
        modelId="amazon.titan-embed-text-v2:0",
        body=json.dumps({"inputText": text, "dimensions": 1024}),
    )
    return json.loads(response["body"].read())["embedding"]
```

Writing a memory attaches an embedding and optional metadata alongside the bytes. The following code constructs the store with a per-tenant prefix, so the key `memories/m1` lands in the physical partition `user/u1`:

```
from strands_dynamodb_storage import DynamoDBStorage, SearchQuery

storage = DynamoDBStorage("agent-storage", region_name="us-east-1", prefix="user/u1")

await storage.write(
    "memories/m1",
    b"prefers window seats on long flights",
    vector=embed("prefers window seats on long flights"),
    metadata={"kind": "preference"},
)
```

Recalling by meaning is one call, scoped to the same partition:

```
results = await storage.search(SearchQuery(
    vector=embed("what are this user's seating preferences?"),
    top_k=5,
    pk="user/u1",  # the physical partition: the full key's first two segments
    filter={"kind": "preference"},
))
```

Notice the `pk` argument. The vector index is partitioned the same way the table is, and every search is scoped to one partition, so a tenant's search never ranges over another tenant's memories, and the work each search performs tracks the size of that tenant's memory rather than the whole table. Keep in mind that the partition value is supplied by the caller, so this is query scoping rather than an authorization boundary: a principal holding `dynamodb:SearchVectors` on the table can search any partition, and tenant access control belongs in IAM and your application layer.

Results return most similar first. The raw score's direction follows the index's distance function: lower is nearer for cosine and Euclidean distance, and higher is more similar for dot product.

## Wire memory into an agent
<a name="strands-memory-manager"></a>

In a real agent you want retrieved memories to reach the model automatically, and the SDK's Memory Manager handles that: it retrieves relevant entries before each model call and folds them into the model input, and it registers a `search_memory` tool the model can call on demand. The Memory Manager accepts any object implementing the SDK's `MemoryStore` protocol. The package does not ship one, so you define a small class in your own application that embeds on write, embeds on search, and returns `MemoryEntry` values:

```
import uuid

from strands.memory import MemoryEntry
from strands_dynamodb_storage import DynamoDBStorage, SearchQuery


class DynamoDBMemoryStore:
    def __init__(self, storage, partition, embed):
        self.storage = storage
        self.partition = partition
        self.embed = embed  # the embed() function defined earlier
        self.name = "dynamodb"
        self.description = "Long-term memories in DynamoDB, searched by meaning"
        self.max_search_results = 3
        self.writable = True
        self.extraction = None

    async def add(self, content, metadata=None):
        await self.storage.write(
            f"memories/{uuid.uuid4().hex[:8]}",
            content.encode(),
            vector=self.embed(content),
            metadata=metadata,
        )

    async def search(self, query, options=None):
        results = await self.storage.search(SearchQuery(
            vector=self.embed(query),
            top_k=self.max_search_results,
            pk=self.partition,
            include_values=True,
        ))
        return [
            MemoryEntry(content=r.data.decode(), metadata=r.metadata)
            for r in results
            if r.data is not None
        ]
```

The following code seeds three memories and wires the store into the agent, so retrieved memories reach the model with no orchestration code on your side:

```
import asyncio

from strands import Agent
from strands.memory import MemoryManager

storage = DynamoDBStorage("agent-storage", region_name="us-east-1", prefix="user/u1")
store = DynamoDBMemoryStore(storage, partition="user/u1", embed=embed)


async def seed():
    await store.add("Prefers window seats on long flights")
    await store.add("Planning a trip to Tokyo in December")
    await store.add("Allergic to peanuts")


asyncio.run(seed())

memory = MemoryManager(stores=[store], add_tool_config=True)
agent = Agent(memory_manager=memory)
agent("Book me a flight seat for my December trip. Which seat should I pick?")
```

Running this against a live table, the agent calls its `search_memory` tool, matches the Tokyo trip and the window-seat preference from DynamoDB, and recommends a window seat for the flight. Passing `add_tool_config=True` also registers an `add_memory` tool, so the model can store new facts through the same table it recalls from.

## Required IAM permissions
<a name="strands-iam-permissions"></a>

At runtime the package issues four DynamoDB operations, plus `SearchVectors` when you use semantic search, and Amazon S3 operations only when you configure offload, so the least-privilege IAM policy is short. Replace {{111122223333}} with your AWS account ID and update the Region to match your environment:

```
{
  "Version": "2012-10-17",		 	 	 
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "dynamodb:PutItem",
        "dynamodb:GetItem",
        "dynamodb:DeleteItem",
        "dynamodb:Query"
      ],
      "Resource": "arn:aws:dynamodb:us-east-1:111122223333:table/agent-storage"
    }
  ]
}
```

The [package README](https://github.com/aws/strands-dynamodb-storage) carries the complete policy, including the additional statements for semantic search, Amazon S3 offload, and embedding model invocation.

## Considerations
<a name="strands-considerations"></a>
+ A vector index's name, dimensions, and distance function are immutable after creation, and a newly created index backfills before it is searchable. A table supports up to five vector indexes, so adopting a different configuration later means adding an index, not rebuilding the table.
+ Vector indexes are eventually consistent, the same model as a global secondary index. A memory written moments ago may take a short time to become searchable.
+ Time to Live expiry filtering applies to read and list operations. Because Time to Live deletion is asynchronous, a search can briefly return items whose expiry has passed but which DynamoDB has not yet physically removed.
+ Listing requires a prefix that covers at least a full scope and identifier. Broad listings such as an empty prefix are rejected; the package never falls back to a table scan.
+ If you enable Time to Live on offloaded values, add an Amazon S3 lifecycle rule: DynamoDB removes the expired pointer item, and the lifecycle rule is what reclaims the Amazon S3 object.

## Additional resources
<a name="strands-additional-resources"></a>
+ [strands-dynamodb-storage on GitHub](https://github.com/aws/strands-dynamodb-storage)
+ [strands-dynamodb-storage on PyPI](https://pypi.org/project/strands-dynamodb-storage/)
+ [strands-dynamodb-storage on npm](https://www.npmjs.com/package/strands-dynamodb-storage)
+ [Strands Agents documentation](https://strandsagents.com/)