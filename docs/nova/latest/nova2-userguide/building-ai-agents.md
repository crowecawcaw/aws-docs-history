# Building AI agents

Amazon Nova models are optimized for building AI agents with Amazon Nova Act. The models provide
improved tool use, better reasoning for multi-step tasks, enhanced ability to maintain context
across complex agent workflows and support for remote MCP tools.

## Create an agent

AI agents built with Nova can orchestrate multiple tool calls, maintain context across
extended interactions and course-correct when needed. Extended thinking transforms agentic
workflows by enabling systematic reasoning through complex goals. Consider using a planning
framework SDK such as Strands Agents to make the planning and execution process of your agent
systems more robust.

### Agent design patterns

When designing agents with Nova:

- Enable reasoning on medium or high for best results for complex multi-step workflows
  requiring planning and verification
- Implement tool choice `auto` to allow flexible tool selection across agent
  interactions
- Design error handling that allows agents to recover and retry with modified
  approaches
- Maintain conversation history to preserve context across agent interactions
- Implement robust content filtering and moderation mechanisms across uncontrolled content
  that your agent system consumes. For example, Amazon offers Amazon Bedrock Guardrails, a feature
  designed to apply safeguards across multiple foundation models, knowledge bases and agents.
  These guardrails can filter harmful content, block denied topics, and redact sensitive
  information such as personally identifiable information.

### Multi-tool agent example

```
tool_config = {
    "tools": [
        {
            "toolSpec": {
                "name": "calculator",
                "description": "Perform mathematical calculations",
                "inputSchema": {
                    "json": {
                        "type": "object",
                        "properties": {
                            "expression": {
                                "type": "string",
                                "description": "Mathematical expression to evaluate"
                            }
                        },
                        "required": ["expression"]
                    }
                }
            }
        },
        {
            "toolSpec": {
                "name": "database_query",
                "description": "Query financial database for historical data",
                "inputSchema": {
                    "json": {
                        "type": "object",
                        "properties": {
                            "query": {
                                "type": "string",
                                "description": "SQL query to execute"
                            }
                        },
                        "required": ["query"]
                    }
                }
            }
        }
    ]
}

response = client.converse(
    modelId=" us.amazon.nova-2-lite-v1:0",
    messages=[{
        "role": "user",
        "content": [{
            "text": "Analyze our Q3 financial performance across all business units, calculate year-over-year growth rates with statistical significance testing, and recommend budget allocation strategies for Q4."
        }]
    }],
    toolConfig=tool_config,
    inferenceConfig={"maxTokens": 10000, "temperature": 1, “topP”: 0.9},
    additionalModelRequestFields={
        "reasoningConfig": {
            "type": "enabled",
            "maxReasoningEffort": "low"
        }
    }
)

```

## Invoke an agent

Agent invocation involves managing the conversation flow, processing tool calls, and
maintaining state across multiple interactions.

### Streaming agent responses

Stream responses to provide real-time visibility into the agent's reasoning and
actions:

```
import boto3
response = client.converse_stream(
    modelId=" us.amazon.nova-2-lite-v1:0",
    messages=[{
        "role": "user",
        "content": [{
            "text": "Design a scalable microservices architecture for an e-commerce platform handling 1M+ daily transactions. Consider data consistency, fault tolerance, performance, security, and cost optimization."
        }]
    }],
    inferenceConfig={"maxTokens": 10000, "temperature": 10},
    additionalModelRequestFields={
        "reasoningConfig": {
            "type": "enabled",
            "maxReasoningEffort": "low"
        }
    }
)

# Process the streaming response
reasoning_complete = False
for event in response["stream"]:
    if "contentBlockDelta" in event:
        delta = event["contentBlockDelta"]["delta"]
        
        if "reasoningContent" in delta:
            reasoning_text = delta["reasoningContent"]["reasoningText"]["text"]
            print(f"{reasoning_text}", end="", flush=True)
        elif "text" in delta:
            if not reasoning_complete:
                print(f"

Final Architecture Design:
")
                reasoning_complete = True
            print(f"{delta['text']}", end="", flush=True)

```

### Agent state management

Maintain conversation history and tool results to preserve context; the example below
demonstrates this for a single turn, but the developer can determine how to orchestrate overall
agent system based on workflow requirements. In addition, Amazon Web Services tools such as
Strands manage agent context and tool state on behalf of the developer.

```
messages = []

messages = []

# Initial user query
messages.append({
    "role": "user",
    "content": [{"text": user_query}]
})

# Get agent response
response = client.converse(
    modelId=" us.amazon.nova-2-lite-v1:0",
    messages=messages,
    toolConfig=tool_config,
    inferenceConfig=inf_params
)

# Add assistant response to history
messages.append(response["output"]["message"])

# Process tool calls and add results
if response["stopReason"] == "tool_use":
    tool = next(
        block["toolUse"]
        for block in response["output"]["message"]["content"]
        if "toolUse" in block
    )
    
    # Execute tool
    result = execute_tool(tool["name"], tool["input"])
    
    # Add tool result to conversation
    messages.append({
        "role": "user",
        "content": [{
            "toolResult": {
                "toolUseId": tool["toolUseId"],
                "content": [{"json": result}],
                "status": "success"
            }
        }]
    })
    
    # Continue conversation
    response = client.converse(
        modelId=" us.amazon.nova-2-lite-v1:0",
        messages=messages,
        toolConfig=tool_config,
        inferenceConfig=inf_params
    )

```

### Agent Best Practices

For more information about Agent Best Practices, see [General best practices](prompting-best-practices.md "prompting-best-practices.md").

For guidance on developing Conversational AI agents, see [Speech-to-Speech (Amazon Nova 2 Sonic)](using-conversational-speech.md "using-conversational-speech.md").
