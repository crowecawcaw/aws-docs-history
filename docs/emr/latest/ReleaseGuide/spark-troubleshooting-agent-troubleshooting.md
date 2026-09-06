

# Troubleshooting and Q&A
<a name="spark-troubleshooting-agent-troubleshooting"></a>

## Troubleshooting
<a name="spark-troubleshooting-common-issues"></a>

The error message from the Spark Troubleshooting Agent is available in different ways for different MCP clients. In this page, we list some general guidance for common issues you may see using Apache Spark troubleshooting agent for Amazon EMR.

Topics
+ [Error: MCP Server Failed to Load](#mcp-server-failed-to-load)
+ [Observation: Slow Tool Loading](#slow-tool-loading)
+ [Error: Tool Invocation Failed with Throttling Error](#throttling-error)
+ [Error: Tool Responds With User Error](#user-error)
+ [Error: Tool Responds With Internal Error](#internal-error)

### Error: MCP Server Failed to Load
<a name="mcp-server-failed-to-load"></a>
+ Verify your MCP configurations are properly configured.
+ **Validate JSON syntax**:
  + Ensure your JSON is valid with no syntax errors
  + Check for missing commas, quotes, or brackets
+ Verify your local AWS credentials and verify the policy for the MCP IAM role is properly configured.
+ Run /mcp to verify MCP server availability for `Kiro-CLI` case

### Observation: Slow Tool Loading
<a name="slow-tool-loading"></a>
+ Tools may take a few seconds to be loaded on first attempt of launching the server.
+ If tools don't appear, try restarting the chat.
+ Run `/tools` command to verify tool availability.
+ Run `/mcp` to verify if the server launched without error.

### Error: Tool Invocation Failed with Throttling Error
<a name="throttling-error"></a>
+ If you hit your service limit, please wait for a few seconds to issue a tool invocation if you see the throttling exception.

### Error: Tool Responds With User Error
<a name="user-error"></a>
+ AccessDeniedException - check the error message and fix the permission issue.
+ InvalidInputException - check the error message and correct the tool input parameters.
+ ResourceNotFoundException - check the error message and fix the input parameter for resource reference.

### Error: Tool Responds With Internal Error
<a name="internal-error"></a>
+ If you see `The service is handling high-volume requests` please retry the tool invocation in a few seconds.
+ If you see `INTERNAL SERVICE EXCEPTION` please document the analysis id, tool name, any error message available from the mcp log or tool response and optional sanitized conversation history and reach out to the AWS support.

## Q&A
<a name="spark-troubleshooting-qa"></a>

### 1. Should I enable "trust" setting for the tools by default?
<a name="qa-trust-setting"></a>

Do not turn on "trust" setting by default for all tool calls initially and operate on git-versioned build environment when accepting code recommendations. Review each tool execution to understand what changes are being made.

### 2. What are the common example prompts to leverage the troubleshooting tools?
<a name="qa-example-prompts"></a>

Please refer to [Prompt Examples](spark-troubleshooting-agent-prompt-examples.md) for the prompt examples about leveraging troubleshooting tools.

### 3. What data is transmitted to the LLM and how is it handled?
<a name="qa-data-transmitted-to-llm"></a>

Customer data and files remain within your chosen AWS Region and are not transmitted cross-region. When the agent operates in a Region that uses global cross-region inference from Amazon Bedrock, the service may route requests to the nearest Region with available capacity depending on demand. In such cases, only extracted metadata from customer logs and processed inference results are transmitted, not the underlying customer data or files. All data is PII-masked before it is sent to the LLM for processing, whether the inference occurs within the same Region or is routed to another Region. For more details on how cross-region inference works and which Regions are affected, see [Cross-Region Processing for the Apache Spark Troubleshooting Agent](spark-troubleshooting-cross-region-processing.md).