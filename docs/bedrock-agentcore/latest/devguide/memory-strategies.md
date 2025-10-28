# Memory strategies

In AgentCore Memory, you can add memory strategies to your memory resource. These
strategies determine what types of information to extract from raw conversations.
Strategies are configurations that intelligently capture and persist key concepts
from interactions, sent as events in the
[CreateEvent](../APIReference/API_CreateEvent.md "../APIReference/API_CreateEvent.md") operation. You can
add strategies to the memory resource as part of [CreateMemory](../../../bedrock-agentcore-control/latest/APIReference/API_CreateMemory.md "../../../bedrock-agentcore-control/latest/APIReference/API_CreateMemory.md") or
[UpdateMemory](../../../bedrock-agentcore-control/latest/APIReference/API_UpdateMemory.md "../../../bedrock-agentcore-control/latest/APIReference/API_UpdateMemory.md") operations. Once enabled, these strategies are
automatically executed on raw conversation events associated with that memory
resource to extract long-term memories.

If no strategies are specified, long-term memory records will not be extracted for
that memory.

AgentCore Memory supports a variety of memory strategies:

## Built-in strategies

AgentCore handles all memory extraction and consolidation
automatically with predefined algorithms.

- AgentCore handles all memory extraction and consolidation
  automatically
- No configuration required beyond basic trigger settings
- Uses predefined algorithms optimized and benchmarked for common use
  cases
- Suitable for standard conversational AI applications
- Limited customization options
- Higher cost for storage

## Built-in overrides

Extends built-in strategies with targeted customization while using
an AgentCore managed extraction pipeline.

- Extends built-in strategies with targetted customization
- Allows modification of prompts while still using AgentCore managed
  extraction pipeline
- Provides support for bedrock models (invoked in your account)
- Lower cost for storage than built-ins

## Self-managed strategies:

You have complete ownership of memory processing pipeline with custom
extraction and consolidation algorithms.

- Complete ownership of memory processing pipeline
- Custom extraction and consolidation algorithms using any model,
  prompts, etc.
- Full control over memory record schemas, namespaces etc.
- Integration with external systems and databases
- Requires infrastructure setup and maintenance
- Lower cost for storage than built-in strategies

A single memory resource can be configured to utilize both built-in and custom
strategies simultaneously, providing flexibility to address diverse memory
requirements.

###### Topics

- [Built-in strategies](built-in-strategies.md "built-in-strategies.md")
- [Built-in with overrides strategy](memory-custom-strategy.md "memory-custom-strategy.md")
- [Self-managed strategy](memory-self-managed-strategies.md "memory-self-managed-strategies.md")
