# Create an AgentCore Memory

You can create an AgentCore Memory with the Amazon Bedrock AgentCore starter toolkit, AgentCore
python SDK, the AWS console, or with the [CreateMemory](../../../bedrock-agentcore-control/latest/APIReference/API_CreateMemory.md "../../../bedrock-agentcore-control/latest/APIReference/API_CreateMemory.md") AWS SDK operation. When creating a memory, you can configure
settings such as name, description, encryption settings, expiration timestamp for raw
events, and memory strategies if you want to extract long-term memory.

When creating an AgentCore Memory, consider the following factors to maintain it meets your
application's needs:

**Event retention** – Choose how long raw events are retained
(up to 365 days) for short-term memory.

**Security requirements** – If your application handles
sensitive information, consider using a [customer managed AWS KMS key](../../../kms/latest/developerguide/concepts.md "../../../kms/latest/developerguide/concepts.md") for
encryption. The service still encrypts data using a service managed key, even if you don't
provide a customer-managed AWS KMS key.

**Memory strategies** – Define how events are processed into
meaningful long-term memories using built-in or built-in with overrides strategies. If you
do not define any strategy, only short-term memory containing raw events are stored. For
more information, see [Use long-term memory](long-term-memory-long-term.md "long-term-memory-long-term.md").

**Naming conventions** – Use clear, descriptive names that
help identify the purpose of each AgentCore Memory, especially if your application uses
multiple stores.

Starter toolkit CLI
**Create** a basic memory (short-term only):

```
agentcore memory create my_agent_memory --region us-west-2
```

**Create** memory with long-term strategies:

```
agentcore memory create ShoppingSupportAgentMemory \
  --region us-west-2 \
  --description "Memory for a customer support agent." \
  --strategies '[{"summaryMemoryStrategy": {"name": "SessionSummarizer", "namespaces": ["/summaries/{actorId}/{sessionId}/"]}}, {"userPreferenceMemoryStrategy": {"name": "PreferenceLearner", "namespaces": ["/users/{actorId}/preferences/"]}}]' \
  --wait
```

**List** all memories:

```
agentcore memory list --region us-west-2
```

**Get** memory details:

```
agentcore memory get <memory-id> --region us-west-2
```

**Check** memory status:

```
agentcore memory status <memory-id> --region us-west-2
```

Starter toolkit
for the full example, see [Get started with AgentCore Memory](memory-get-started.md "memory-get-started.md").

```

from bedrock_agentcore_starter_toolkit.operations.memory.manager import MemoryManager
from bedrock_agentcore.memory.session import MemorySessionManager
from bedrock_agentcore.memory.constants import ConversationalMessage, MessageRole
from bedrock_agentcore_starter_toolkit.operations.memory.models.strategies import SummaryStrategy, UserPreferenceStrategy
import time

# Create memory manager
memory_manager = MemoryManager(region_name="us-west-2")

print("Creating a new memory resource and waiting for it to become active...")

# Create memory resource with summary and user preference strategy
memory = memory_manager.get_or_create_memory(
    name="ShoppingSupportAgentMemory",
    description="Memory for a customer support agent.",
    strategies=[
        SummaryStrategy(
            name="SessionSummarizer",
            namespaces=["/summaries/{actorId}/{sessionId}/"]
        ),
        UserPreferenceStrategy(
            name="PreferenceLearner",
            namespaces=["/users/{actorId}/preferences/"]
        )
    ]
)

memory_id = memory.get('id')
print(f"Memory resource is now ACTIVE with ID: {memory_id}")
```

AgentCore python SDK
For more information, see [Amazon Bedrock AgentCore SDK](agentcore-sdk-memory.md "agentcore-sdk-memory.md").

```
from bedrock_agentcore.memory import MemoryClient
import time

client = MemoryClient(region_name="us-east-1")

memory = client.create_memory_and_wait(
    name="MyAgentMemory",
    strategies=[{
        "summaryMemoryStrategy": {
            # Name of the extraction model/strategy
            "name": "SessionSummarizer",
            # Organize facts by session ID for easy retrieval
            # Example: "summaries/session123" contains summary of session123
            "namespaces": ["/summaries/{actorId}/{sessionId}/"]
        }
    }]
)

```

AWS SDK
For more information, see [AWS SDK](aws-sdk-memory.md "aws-sdk-memory.md").

```
import boto3
import time

# Initialize the Boto3 clients for control plane and data plane operations
control_client = boto3.client('bedrock-agentcore-control')
data_client = boto3.client('bedrock-agentcore')

print("Creating a new memory resource...")

# Create the memory resource with defined strategies
response = control_client.create_memory(
    name="ShoppingSupportAgentMemory",
    description="Memory for a customer support agent.",
    memoryStrategies=[
        {
            'summaryMemoryStrategy': {
                'name': 'SessionSummarizer',
                'namespaces': ['/summaries/{actorId}/{sessionId}/']
            }
        },
        {
            'userPreferenceMemoryStrategy': {
                'name': 'UserPreferenceExtractor',
                'namespaces': ['/users/{actorId}/preferences/']
            }
        }
    ]
)

memory_id = response['memory']['id']
print(f"Memory resource created with ID: {memory_id}")

# Poll the memory status until it becomes ACTIVE
while True:
    mem_status_response = control_client.get_memory(memoryId=memory_id)
    status = mem_status_response.get('memory', {}).get('status')
    if status == 'ACTIVE':
        print("Memory resource is now ACTIVE.")
        break
    elif status == 'FAILED':
        raise Exception("Memory resource creation FAILED.")
    print("Waiting for memory to become active...")
    time.sleep(10)
```

Console

###### To create an AgentCore memory

1. Open the [Amazon Bedrock AgentCore](https://console.aws.amazon.com/bedrock-agentcore/ "https://console.aws.amazon.com/bedrock-agentcore/") console.
2. In the left navigation pane, choose
   **Memory**.
3. Choose **Create memory**.
4. For **Memory name** enter a name for the
   AgentCore Memory.
5. (Optional) For **Short-term memory (raw event)
   expiration** set the duration (days), for which the
   AgentCore Memory will store events.
6. (Optional) In **Additional configurations** set the
   following:
   1. For **Memory description**, enter a
      description for the AgentCore Memory.
   2. If you want to use your own AWS KMS key to encrypt your data, do
      the following:
      1. In **KMS key**, choose
         **Customize encryption settings
         (advanced)**.
      2. In **Choose an AWS KMS key** choose or
         enter the ARN of an existing AWS KMS key. Alternatively,
         choose **Create an AWS KMS** to create a
         new AWS KMS key.

7. (Optional) For **Long-term memory extraction
   strategies** choose one or more [memory strategies](memory-strategies.md "memory-strategies.md"). For more
   information:
   - [Built-in strategies](built-in-strategies.md "built-in-strategies.md")
   - [Customize a built-in strategy or create your own strategy](memory-custom-strategy.md "memory-custom-strategy.md")
   - [Self-managed strategy](memory-self-managed-strategies.md "memory-self-managed-strategies.md")

8. Choose **Create memory** to create the
   AgentCore Memory.
