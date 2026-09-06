

# Memory strategies
<a name="memory-strategies"></a>

In AgentCore Memory, you can add memory strategies to your memory resource. These strategies determine what types of information to extract from raw conversations. Strategies are configurations that intelligently capture and persist key concepts from interactions, sent as events in the [CreateEvent](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_CreateEvent.html) operation. You can add strategies to the memory resource as part of [CreateMemory](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_CreateMemory.html) or [UpdateMemory](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_UpdateMemory.html) operations. Once enabled, these strategies are automatically executed on raw conversation events associated with that memory resource to extract long-term memories.

If no strategies are specified, long-term memory records will not be extracted for that memory.

AgentCore Memory supports a variety of memory strategies:

**Topics**
+ [Built-in strategies](#memory-built-in-strategies-desc)
+ [Built-in overrides](#memory-built-in-overrides-desc)
+ [Self-managed strategies](#memory-self-managed-strategies-desc)
+ [Built-in strategies](built-in-strategies.md)
+ [Customize a built-in strategy or create your own strategy](memory-custom-strategy.md)
+ [Self-managed strategy](memory-self-managed-strategies.md)

## Built-in strategies
<a name="memory-built-in-strategies-desc"></a>

AgentCore handles all memory extraction and consolidation automatically with predefined algorithms.
+ AgentCore handles all memory extraction and consolidation automatically
+ No configuration required beyond basic trigger settings
+ Uses predefined algorithms optimized and benchmarked for common use cases
+ Suitable for standard conversational AI applications
+ Limited customization options
+ Higher cost for storage

## Built-in overrides
<a name="memory-built-in-overrides-desc"></a>

Extends built-in strategies with targeted customization while using an AgentCore managed extraction pipeline.
+ Extends built-in strategies with targeted customization
+ Allows modification of prompts while still using AgentCore managed extraction pipeline
+ Provides support for bedrock models (invoked in your account)
+ Lower cost for storage than built-ins

## Self-managed strategies
<a name="memory-self-managed-strategies-desc"></a>

You have complete ownership of memory processing pipeline with custom extraction and consolidation algorithms.
+ Complete ownership of memory processing pipeline
+ Custom extraction and consolidation algorithms using any model, prompts, etc.
+ Full control over memory record schemas, namespaces etc.
+ Integration with external systems and databases
+ Requires infrastructure setup and maintenance
+ Lower cost for storage than built-in strategies

A single memory resource can be configured to utilize both built-in and custom strategies simultaneously, providing flexibility to address diverse memory requirements.