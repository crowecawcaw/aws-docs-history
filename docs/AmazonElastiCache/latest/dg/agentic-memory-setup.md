

# Setting up ElastiCache for Valkey as a vector store for agentic memory
<a name="agentic-memory-setup"></a>

The following walkthrough shows how to build a memory-enabled AI agent using Mem0 with ElastiCache for Valkey as the vector store.

## Step 1: Create a basic agent without memory
<a name="agentic-memory-step1"></a>

First, install Strands Agents and create a basic agent:

```
pip install strands-agents strands-agents-tools strands-agents-builder
```

Initialize a basic agent with an HTTP tool for web browsing:

```
from strands import Agent
from strands.tools import http_request

# Initialize agent with access to the tool to browse the web
agent = Agent(tools=[http_request])

# Format messages as expected by Strands
formatted_messages = [
    {
        "role": "user",
        "content": [{"text": "What is the URL for the project mem0 and its most important metrics?"}]
    }
]

result = agent(formatted_messages)
```

Without memory, the agent performs the same research tasks repeatedly for each request. In testing, the agent makes three tool calls to answer the request, using approximately 70,000 tokens and taking over 9 seconds to complete.

## Step 2: Configure Mem0 with ElastiCache for Valkey
<a name="agentic-memory-step2"></a>

Install the Mem0 library with the Valkey vector store connector:

```
pip install mem0ai "mem0ai[vector_stores]"
```

Configure Valkey as the vector store. ElastiCache for Valkey supports vector search capabilities starting with version 8.2:

```
from mem0 import Memory

# Configure Mem0 with ElastiCache for Valkey
config = {
    "vector_store": {
        "provider": "valkey",
        "config": {
            "valkey_url": "your-elasticache-cluster.cache.amazonaws.com:6379",
            "index_name": "agent_memory",
            "embedding_model_dims": 1024,
            "index_type": "flat"
        }
    }
}

m = Memory.from_config(config)
```

Replace {{your-elasticache-cluster.cache.amazonaws.com}} with your ElastiCache cluster's endpoint. For instructions on finding your cluster endpoint, see [Accessing your ElastiCache cluster](accessing-elasticache.md).

## Step 3: Add memory tools to the agent
<a name="agentic-memory-step3"></a>

Create memory tools that the agent can use to store and retrieve information. The `@tool` decorator transforms regular Python functions into tools the agent can invoke:

```
from strands import Agent, tool
from strands.tools import http_request

@tool
def store_memory_tool(information: str, user_id: str = "user") -> str:
    """Store important information in long-term memory."""
    memory_message = [{"role": "user", "content": information}]

    # Create new memories using Mem0 and store them in Valkey
    m.add(memory_message, user_id=user_id)

    return f"Stored: {information}"

@tool
def search_memory_tool(query: str, user_id: str = "user") -> str:
    """Search stored memories for relevant information."""

    # Search memories using Mem0 stored in Valkey
    results = m.search(query, user_id=user_id)
    if results['results']:
        return "\n".join([r['memory'] for r in results['results']])
    return "No memories found"

# Initialize Strands agent with memory tools
agent = Agent(tools=[http_request, store_memory_tool, search_memory_tool])
```

## Step 4: Test the memory-enabled agent
<a name="agentic-memory-step4"></a>

With memory enabled, the agent stores information from its interactions and retrieves it in subsequent requests:

```
# First request - agent searches the web and stores results in memory
formatted_messages = [
    {
        "role": "user",
        "content": [{"text": "What is the URL for the project mem0 and its most important metrics?"}]
    }
]
result = agent(formatted_messages)

# Second request (same question) - agent retrieves from memory
result = agent(formatted_messages)
```

On the second request, the agent retrieves the information from memory instead of making web tool calls. In testing, this reduced token usage from approximately 70,000 to 6,300 (a 12x reduction) and improved response time from 9.25 seconds to 2 seconds (more than 3x faster).

## How it works under the hood
<a name="agentic-memory-valkey-commands"></a>

The following table shows the Valkey commands that Mem0 uses internally to implement agentic memory with ElastiCache. Mem0 abstracts these commands through its API — the exact schema and key naming may vary depending on the Mem0 version and configuration:


| Operation | Valkey command | Description | 
| --- | --- | --- | 
| Create vector index | FT.CREATE agent\_memory SCHEMA embedding VECTOR HNSW 6 TYPE FLOAT32 DIM 1024 DISTANCE\_METRIC COSINE | Creates a vector index for semantic memory search | 
| Store memory | HSET mem:{id} memory "..." embedding [bytes] user\_id "user\_123" created\_at "..." | Stores a memory with its vector embedding | 
| Search memories | FT.SEARCH agent\_memory "\*=>[KNN 5 @embedding $query\_vec]" PARAMS 2 query\_vec [bytes] DIALECT 2 | Finds the most semantically similar memories | 
| Set expiration | EXPIRE mem:{id} 86400 | Sets TTL for memory entries | 