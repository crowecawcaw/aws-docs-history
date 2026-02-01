# Get started with AgentCore Memory

Amazon Bedrock Amazon Bedrock AgentCore Memory lets you create and manage AgentCore Memory resources that
store conversation context for your AI agents. This getting started guides you through
installing dependencies and implementing both short-term and long-term memory
features. The instructions use the
[AgentCore starter
toolkit](https://github.com/aws/bedrock-agentcore-starter-toolkit "https://github.com/aws/bedrock-agentcore-starter-toolkit").

The steps are as follows:

1. Create an AgentCore Memory containing a semantic strategy
2. Write events (conversation history) to the memory resource
3. Retrieve memory records from long term memory
   For other examples, see [Amazon Bedrock AgentCore Memory examples](memory-examples.md "memory-examples.md").

## Prerequisites

Before starting, make sure you have:

- **AWS Account** with credentials configured
  (`aws configure`)
- **Python 3.10+** installed

To get started with Amazon Bedrock Amazon Bedrock AgentCore Memory, make a folder for this
quick start, create a virtual environment, and install the dependencies. The below
command can be run directly in the terminal.

```
mkdir agentcore-memory-quickstart
cd agentcore-memory-quickstart
python -m venv .venv
source .venv/bin/activate
pip install bedrock-agentcore
pip install bedrock-agentcore-starter-toolkit
```

The starter toolkit includes a CLI (`agentcore`) for memory resource management. The CLI provides commands for creating, listing, getting, and deleting memory resources. For event operations and session management, use the starter toolkit Python API or AWS SDK.

###### Note

The Amazon Bedrock AgentCore Starter Toolkit is intended to help developers get started
quickly. For the complete set of Amazon Bedrock AgentCore Memory operations, see the Boto3
documentation: [bedrock-agentcore-control](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control.html "https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control.html") and [bedrock-agentcore](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore.html "https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore.html").

**Full example:** See the [complete code example](https://github.com/aws/bedrock-agentcore-starter-toolkit/blob/main/documentation/docs/examples/semantic_search.md "https://github.com/aws/bedrock-agentcore-starter-toolkit/blob/main/documentation/docs/examples/semantic_search.md") that demonstrates steps 1-3.

## Step 1: Create an AgentCore Memory

You need an AgentCore Memory to start storing information for your agent. By default,
memory events (which we refer to as short-term memory) can be written to an
AgentCore Memory. For insights to be extracted and placed into long term memory
records, the resource requires a
_memory strategy_ which is a configuration that defines how
conversational data should be processed, and what information to extract (such as facts,
preferences, or summaries).

In this step, you create an AgentCore Memory with a semantic strategy so that both short
term and long term memory can be utilized. This will take 2-3 minutes. You can also
create AgentCore Memory resources in the AWS console.

Starter toolkit CLI
Create memory with semantic strategy:

```
agentcore memory create CustomerSupportSemantic \
  --region us-west-2 \
  --description "Customer support memory store" \
  --strategies '[{"semanticMemoryStrategy": {"name": "semanticLongTermMemory", "namespaces": ["/strategies/{memoryStrategyId}/actors/{actorId}/"]}}]' \
  --wait
```

List memories to verify creation:

```
agentcore memory list --region us-west-2
```

Starter toolkit

```
from bedrock_agentcore_starter_toolkit.operations.memory.manager import MemoryManager
from bedrock_agentcore.memory.session import MemorySessionManager
from bedrock_agentcore.memory.constants import ConversationalMessage, MessageRole
from bedrock_agentcore_starter_toolkit.operations.memory.models.strategies import SemanticStrategy
import time

memory_manager = MemoryManager(region_name="us-west-2")

print("Creating memory resource...")

memory = memory_manager.get_or_create_memory(
    name="CustomerSupportSemantic",
    description="Customer support memory store",
    strategies=[
        SemanticStrategy(
            name="semanticLongTermMemory",
            namespaces=['/strategies/{memoryStrategyId}/actors/{actorId}/'],
        )
    ]
)

print(f"Memory ID: {memory.get('id')}")
```

You can call `list_memories` to see that the memory resource has been
created with:

```
memories = memory_manager.list_memories()
```

## Step 2: Write events to memory

You can write events to an AgentCore Memory as short-term memory and
extracts insights for long-term memory.

Writing events to memory has multiple purposes. First, event contents (most commonly
conversation history) are stored as short-term memory. Second, relevant insights are
pulled from events and written into memory records as a part of long-term memory.

The memory resource id, actor id, and session id are required to create an event. In
this step, you create three events, simulating messages between an end user and a chat
bot.

```
# Create a session to store memory events
session_manager = MemorySessionManager(
    memory_id=memory.get("id"),
    region_name="us-west-2")

session = session_manager.create_memory_session(
    actor_id="User1",
    session_id="OrderSupportSession1"
)

# Write memory events (conversation turns)
session.add_turns(
    messages=[
        ConversationalMessage(
            "Hi, how can I help you today?",
            MessageRole.ASSISTANT)],
)

session.add_turns(
    messages=[
        ConversationalMessage(
            "Hi, I am a new customer. I just made an order, but it hasn't arrived. The Order number is #35476",
            MessageRole.USER)],
)

session.add_turns(
    messages=[
        ConversationalMessage(
            "I'm sorry to hear that. Let me look up your order.",
            MessageRole.ASSISTANT)],
)
```

You can get events (turns) for a specific actor after they've been written.

```
# Get the last k turns in the session
turns = session.get_last_k_turns(k=5)

for turn in turns:
    print(f"Turn: {turn}")
```

In this case, you can see the last three events for the actor and session.

## Step 3: Retrieve records from long term

memory

After the events were written to the memory resource, they were analyzed and useful
information was sent to long term memory. Since the memory contains a semantic long term
memory strategy, the system extracts and stores factual information.

You can list all memory records with:

```
# List all memory records
memory_records = session.list_long_term_memory_records(
    namespace_prefix="/"
)

for record in memory_records:
    print(f"Memory record: {record}")
    print("--------------------------------------------------------------------")
```

Or ask for the most relevant information as part of a semantic search:

```
# Perform a semantic search
memory_records = session.search_long_term_memories(
    query="can you summarize the support issue",
    namespace_prefix="/",
    top_k=3
)
```

Important information about the user is likely stored is long term memory. Agents can
use long term memory rather than a full conversation history to make sure that LLMs are
not overloaded with context.

## Cleanup

When you're done with the memory resource, you can delete it:

Starter toolkit CLI

```
agentcore memory delete <memory-id> --region us-west-2 --wait
```

Starter toolkit

```
# Delete the memory resource
memory_manager.delete_memory(memory_id=memory.get("id"))
```

## Next steps

Consider the following::

- [Add another
  strategy](long-term-enabling-long-term-memory.md#long-term-adding-strategies-to-existing-memory "long-term-enabling-long-term-memory.md#long-term-adding-strategies-to-existing-memory") to your memory resource.
- [Enable observability](memory-observability.md "memory-observability.md") for more
  visibility into how memory is working
- Look at further [examples](memory-examples.md "memory-examples.md").
