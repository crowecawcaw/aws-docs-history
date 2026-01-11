# Using tools (function calling)

Tools extend Amazon Nova capabilities by connecting the model to external functionality such as
APIs, databases and code execution environments. Tool use enables Amazon Nova to access real-time
information, perform calculations and interact with external systems.

## Understanding the tool use workflow

Tool use with Amazon Nova involves three key phases:

User Query and Tool Definition

Define tools by providing JSON schemas that describe each tool's
functionality and input requirements. The tool configuration must include
explicit details about when and how to use each tool.

Tool Selection

When a user sends a message, Amazon Nova analyzes it to determine if a tool is
necessary. This automatic tool choice examines the context and decides which
tool (if any) to invoke. If Amazon Nova identifies a suitable tool, it returns
the tool name and required parameters.

You are responsible for executing the tool based on the model's request.
This means writing code that invokes the tool's functionality and processes
the input parameters provided by the model.

Return Results

After executing the tool, send the results back to Amazon Nova in a structured
format using JSON or a combination of text and images. Amazon Nova incorporates
the tool's output into the final response. If errors occur during execution,
denote this in the tool response to allow Amazon Nova to adjust
accordingly.

## Create a tool

Define tools using a tool configuration that includes an array of tools and optionally
a tool choice parameter. Each tool specification must include:

- **Name:** Clear identifier for the tool
- **Description:** Concise explanation of the
  tool's functionality
- **Input Schema:** JSON schema defining required
  and optional parameters

###### Example Tool configuration example

```
tool_config = {
    "tools": [
        {
            "toolSpec": {
                "name": "calculator",
                "description": "A calculator tool that can execute a math equation",
                "inputSchema": {
                    "json": {
                        "type": "object",
                        "properties": {
                            "equation": {
                                "type": "string",
                                "description": "The full equation to evaluate"
                            }
                        },
                        "required": ["equation"]
                    }
                }
            }
        }
    ]
}
```

### Best practices for tool definitions

- Ensure the name and description explicitly convey the tool's exact functionality; avoid tools that are overly semantically similar
- Include key differentiators in the description to help the model distinguish between similar tools
- Limit JSON schemas to two layers of nesting for best performance
- Constrain inputs using schema types (e.g., enum, int, float) rather than describing structure in plain text
- Denote required vs. optional parameters using JSON schema notation (e.g., "required": ["param1", "param2"])
- Validate your JSON schema using a standard validator before submitting
- Place long string arguments last in the schema and avoid nesting them

### Structured output with constrained

decoding

Amazon Nova models leverage constrained decoding to ensure high reliability in
generated outputs. This technique uses grammar to constrain possible tokens at each
generation step, preventing invalid keys and enforcing correct data types based on
your defined schema.

###### Example Structured output example

```
tool_config = {
    "tools": [
        {
            "toolSpec": {
                "name": "ProductAnalysis",
                "description": "Analyze product information from text.",
                "inputSchema": {
                    "json": {
                        "type": "object",
                        "properties": {
                            "name": {
                                "type": "string",
                                "description": "Product name"
                            },
                            "rating": {
                                "maximum": 5,
                                "description": "Customer rating 1-5",
                                "type": ["number", "null"],
                                "minimum": 1
                            },
                            "features": {
                                "description": "Key product features",
                                "type": "array",
                                "items": {"type": "string"}
                            },
                            "category": {
                                "type": "string",
                                "description": "Product category"
                            },
                            "price": {
                                "type": "number",
                                "description": "Price in USD"
                            }
                        },
                        "required": ["name", "category", "price", "features"]
                    }
                }
            }
        }
    ],
    "toolChoice": {
        "tool": {"name": "ProductAnalysis"}
    }
}
```

### Tool choice options

Amazon Nova supports three tool choice parameters:

Tool

The specified tool will be called once, ideal for structured output
use cases

Any

One of the provided tools will be called at least once, useful for API
selection scenarios

Auto

The model decides whether to call a tool and how many tools to call
(default behavior)

## Call a tool

When Amazon Nova decides to call a tool, it returns a tool use block as part of the
assistant message with stopReason set to "tool_use". The tool block contains the tool
name and its inputs.

###### Note

Run following code sections sequentially (Calling a tool → Processing tool call → Returning tool results) in a single Python session. To run the examples again, restart your Python session.

###### Example Calling a tool

```
import boto3
import json

# Create Bedrock client
bedrock = boto3.client('bedrock-runtime', region_name='us-east-1')

# Complex calculation that benefits from precise computation
messages = [{
    "role": "user",
    "content": [{
        "text": "Calculate the compound interest on $10,000 invested at 4.75% annual rate for 7 years, compounded quarterly. Use the formula A = P(1 + r/n)^(nt) where P=10000, r=0.0475, n=4, t=7"
    }]
}]

# Define tool configuration with calculator
tool_config = {
    "tools": [{
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
    }]
}

# Invoke Model
response = bedrock.converse(
    modelId="us.amazon.nova-2-lite-v1:0",
    messages=messages,
    toolConfig=tool_config
)

# Extract tool use from response
tool = next(
    block["toolUse"]
    for block in response["output"]["message"]["content"]
    if "toolUse" in block
)

print(f"Tool: {tool['name']}")
print(f"Expression: {tool['input']['expression']}")
```

### Processing tool calls

Extract the tool name and arguments from the message, then invoke the tool:

```
def calculate(expression):
    """Evaluate mathematical expression"""
    print(f"Calculating: {expression}")
    P = 10000
    r = 0.0475
    n = 4
    t = 7
    result = P * (1 + r/n) ** (n*t)
    return result

stop_reason = response["stopReason"]

if stop_reason == "tool_use":
    if tool["name"] == "calculator":
        result = calculate(tool["input"]["expression"])
```

### Returning tool results

Return tool results using the ToolResultBlock schema:

```
messages.append(response["output"]["message"])

# Add the tool result
messages.append({
    "role": "user",
    "content": [{
        "toolResult": {
            "toolUseId": tool['toolUseId'],
            "content": [{"json": {"result": result}}],
            "status": "success"
        }
    }]
})

# Send the tool result to the model
response = bedrock.converse(
    modelId="us.amazon.nova-2-lite-v1:0",
    messages=messages,
    toolConfig=tool_config
)

# Extract and display final response
final_text = next(
    block["text"]
    for block in response["output"]["message"]["content"]
    if "text" in block
)

print(f"\nFinal Response:\n{final_text}")
```

### Error handling

Report errors back to Amazon Nova to allow request modification and retry:

```
tool_result_message = {
    "role": "user",
    "content": [
        {
            "toolResult": {
                "toolUseId": tool["toolUseId"],
                "content": [{"text": "A validation exception occurred on field: sample.field"}],
                "status": "error"
            }
        }
    ]
}
```

### Security considerations

- Validate that tools exist before invoking them
- Ensure inputs are formatted correctly
- Verify appropriate permissions are in place before tool execution
- Rely on session details rather than allowing Amazon Nova to inject user
  information into tool calls
- Remember that LLMs can hallucinate tool calls; always validate before
  execution

## Built-in system tools

Amazon Nova 2.0 models include fully managed built-in tools that require no custom
implementation. Enable these tools with a simple toggle in the Converse API.

### Code Interpreter

Code Interpreter allows Nova to securely execute Python code in isolated sandbox environments. This tool is designed for mathematical computations, logical operations, and iterative algorithms.

###### Note

Code Interpreter is available in the IAD, PDX, and NRT AWS Regions. To ensure your requests are routed to a supported Region, use Global CRIS. When using Bedrock API keys, you'll need to manually add `InvokeTool` permissions to the policy definitions. The default Bedrock role does not allow the `InvokeTool` action.

Enable Code Interpreter by specifying the systemTool parameter:

```
import boto3
import json

bedrock = boto3.client('bedrock-runtime', region_name='us-east-1')

tool_config = {
    "tools": [{
        "systemTool": {
            "name": "nova_code_interpreter"
        }
    }]
}

response = bedrock.converse(
    modelId="us.amazon.nova-2-lite-v1:0",
    messages=[{
        "role": "user",
        "content": [{
            "text": "What is the average of 10, 24, 2, 3, 43, 52, 13, 68, 6, 7, 902, 82"
        }]
    }],
    toolConfig=tool_config,
    inferenceConfig={"maxTokens": 10000, "temperature": 0}
)

# Pretty print the response
for block in response["output"]["message"]["content"]:
    if "toolUse" in block:
        print("=== Tool Use ===")
        print(f"Tool: {block['toolUse']['name']}")
        print(f"Code:\n{block['toolUse']['input']['snippet']}\n")

    elif "toolResult" in block:
        print("=== Tool Result ===")
        result = block['toolResult']['content'][0]['json']
        print(f"Output: {result['stdOut']}")
        if result['stdErr']:
            print(f"Error: {result['stdErr']}")
        print(f"Exit Code: {result['exitCode']}\n")

    elif "text" in block:
        print("=== Final Answer ===")
        print(block["text"])
```

The interpreter runs code in a sandbox and returns results in a standard
schema:

```
{
    "stdOut": "String",
    "stdErr": "String",
    "exitCode": "int",
    "isError": "boolean"
}
```

### Web Grounding

Web grounding enables Amazon Nova to access real-time information from the internet,
providing up-to-date responses and reducing hallucinations. Enable by specifying the
nova_grounding system tool:

```
tool_config = {
    "tools": [{
        "systemTool": {"name": "nova_grounding"}
    }]
}
```

For detailed information about Web Grounding, see [Web Grounding](web-grounding.md "web-grounding.md").

### Model Context Protocol (MCP)

The Model Context Protocol (MCP) is an open standard that enables secure, two-way
connections between data sources and AI-powered tools. Instead of writing custom
adapters for each API or service, run an MCP server and let Amazon Nova discover its
tools automatically through a client bridge.

Once connected, Amazon Nova treats MCP tools like any other external integration: it
decides when to call them, sends required parameters and incorporates results into
responses. Using Amazon Nova with Strands makes this easier with a built-in MCPClient
that manages discovery, connection and result mapping automatically.
