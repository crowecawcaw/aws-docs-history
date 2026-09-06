

# Invoke Amazon Bedrock AgentCore harness with Step Functions
<a name="connect-bedrockagentcore"></a>

You can integrate Step Functions with Amazon Bedrock AgentCore to invoke a harness from your state machine. A harness is a managed runtime that orchestrates model inference, tool use, and multi-turn conversations. In Workflow Studio, search for **AgentCore InvokeHarness** to find this state and drag it into your workflow.

From the configuration panel, you can create a new harness and execution role using **Quick Create Harness**, or select an existing harness ARN. When you use an existing harness, you can override configurations on a per-invocation basis – values in your Task state definition override the harness defaults. For available parameters, see [InvokeHarness](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_InvokeHarness.html) in the *Amazon Bedrock AgentCore API Reference*. For more information about harness execution roles, see [Runtime permissions](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-permissions.html) in the *Amazon Bedrock AgentCore Developer Guide*.

**Tip**  
To add observability to your agentic resources, enable CloudWatch Transaction Search. For more information, see [Add observability to your agentic resources](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AgentCore-GettingStarted.html#add-observability-agentic-resources) in the *Amazon CloudWatch User Guide*.

To learn about integrating with AWS services in Step Functions, see [Integrating services](integrate-services.md) and [Passing parameters to a service API in Step Functions](connect-parameters.md).

**Key features of Optimized AgentCore harness integration**  
Only the [Request Response](connect-to-resource.md#connect-default) integration pattern is supported. The [Run a Job (.sync)](connect-to-resource.md#connect-sync) and [Wait for a Callback with Task Token](connect-to-resource.md#connect-wait-token) patterns are not supported.
The response is transformed into a [Converse](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_Converse.html#API_runtime_Converse_ResponseSyntax)-shaped JSON structure. Only the final assistant message is returned; earlier turns in multi-turn conversations are discarded.
Token usage metrics (`InputTokens`, `OutputTokens`, `TotalTokens`) are aggregated across all messages in the conversation.
Only text content is included in the response. Tool use and reasoning blocks are omitted from `Output.Message.Content`.
The output size is subject to the Task state output limit. For the current value, see [Quotas related to task executions](service-quotas.md#service-limits-task-executions).
The `InvokeHarness` Task state has a maximum execution time of 15 minutes (900 seconds), even if the `TimeoutSeconds` value exceeds that limit. After the Task state times out, the harness continues executing until it reaches its own configured timeout. To avoid unexpected costs, ensure your harness timeout does not exceed 15 minutes.
The Step Functions console execution details view displays a CloudWatch link beside the agent step, providing a turn-by-turn view of the agent's reasoning including tool use.

## Optimized Amazon Bedrock AgentCore harness APIs
<a name="connect-bedrockagentcore-apis"></a>

The following API is supported:

### [InvokeHarness](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_InvokeHarness.html)
<a name="connect-bedrockagentcore-apis-invokeharness"></a>

Invokes a harness to run an AI agent that can use tools, access memory, and execute multi-turn conversations.

**Supported pattern:** Request Response only.

For the full request syntax, see [InvokeHarness](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_InvokeHarness.html) in the *Amazon Bedrock AgentCore API Reference*.

**Parameters in Step Functions are expressed in PascalCase**  
Even if the native service API is in camelCase, for example the API action `startSyncExecution`, you specify parameters in PascalCase, such as: `StateMachineArn`.

**Response fields**
+ `Output.Message` – The agent's final assistant message. Contains `Role` (always `"assistant"`) and `Content` (an array of text blocks). Only the last assistant turn is returned; earlier turns in multi-turn conversations are discarded.
+ `Output.Message.Content` – Array of content blocks. Each block contains a `Text` field with the agent's response text. Only text content is included; tool use and reasoning blocks are omitted.
+ `StopReason` – Why the agent stopped. Values: `end_turn`, `max_tokens`, `stop_sequence`, `tool_use`.
+ `Usage` – Token consumption metrics aggregated across all turns. Contains `InputTokens`, `OutputTokens`, and `TotalTokens`.
+ `Metrics.LatencyMs` – Total invocation latency in milliseconds, aggregated across all turns.

**Response syntax**

```
{
  "Output": {
    "Message": {
      "Role": "{{string}}",
      "Content": [
        {
          "Text": "{{string}}"
        }
      ]
    }
  },
  "StopReason": "{{string}}",
  "Usage": {
    "InputTokens": {{long}},
    "OutputTokens": {{long}},
    "TotalTokens": {{long}}
  },
  "Metrics": {
    "LatencyMs": {{long}}
  }
}
```

**Note**  
Stopping an execution or the Task state does not stop the harness from continuing to run.

## Task state definition for Amazon Bedrock AgentCore integration
<a name="connect-bedrockagentcore-task-definition"></a>

The following examples show how to define a Task state that invokes an Amazon Bedrock AgentCore harness.

The `RuntimeSessionId` field identifies the conversation session. Use the same session ID across invocations to continue a conversation.

**Note**  
The Step Functions resource URI uses `bedrockagentcore` (no hyphen), while Amazon Bedrock AgentCore resource ARNs use `bedrock-agentcore` (with hyphen).

**Example basic invocation with model override and system prompt**  

```
{
  "Type": "Task",
  "Resource": "arn:aws:states:::bedrockagentcore:invokeHarness",
  "Arguments": {
    "HarnessArn": "arn:aws:bedrock-agentcore:{{us-east-1}}:{{123456789012}}:harness/{{my-agent-harness}}",
    "RuntimeSessionId": "{% $uuid() %}",
    "Messages": [
      {
        "Content": [{ "Text": "{% $states.input.userMessage %}" }],
        "Role": "user"
      }
    ],
    "SystemPrompt": [{ "Text": "You are a helpful customer service agent." }],
    "Model": {
      "BedrockModelConfig": {
        "Temperature": 0.7,
        "ModelId": "global.anthropic.claude-sonnet-4-6"
      }
    },
    "MaxIterations": 75,
    "TimeoutSeconds": 600
  },
  "End": true
}
```

**Example invocation with tools (browser)**  

```
{
  "Type": "Task",
  "Resource": "arn:aws:states:::bedrockagentcore:invokeHarness",
  "Arguments": {
    "HarnessArn": "arn:aws:bedrock-agentcore:{{us-east-1}}:{{123456789012}}:harness/{{order-agent}}",
    "RuntimeSessionId": "{% $uuid() %}",
    "Messages": [
      {
        "Content": [{ "Text": "What is the status of order #12345?" }],
        "Role": "user"
      }
    ],
    "Tools": [
      {
        "Type": "agentcore_browser",
        "Name": "aws_browser_v1",
        "Config": {
          "AgentCoreBrowser": {
            "BrowserArn": "arn:aws:bedrock-agentcore:{{us-east-1}}:aws:browser/aws.browser.v1"
          }
        }
      }
    ],
    "MaxIterations": 10,
    "TimeoutSeconds": 300
  },
  "End": true
}
```

**Tip**  
You can test this state individually using the [TestState](https://docs.aws.amazon.com/step-functions/latest/apireference/API_TestState.html) API before running a full execution.

## Error handling
<a name="connect-bedrockagentcore-errors"></a>

The `InvokeHarness` API can fail with a variety of errors, including throttling, validation, and access denied errors. For a complete list, see [InvokeHarness errors](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_InvokeHarness.html#API_InvokeHarness_Errors) in the *Amazon Bedrock AgentCore API Reference*.

The following example shows a Task state with `Retry` and `Catch` fields for error handling:

```
{
  "Type": "Task",
  "Resource": "arn:aws:states:::bedrockagentcore:invokeHarness",
  "Arguments": {
    "HarnessArn": "arn:aws:bedrock-agentcore:{{us-east-1}}:{{123456789012}}:harness/{{my-harness}}",
    "Messages": [
      {
        "Content": [{ "Text": "{% $states.input.userMessage %}" }],
        "Role": "user"
      }
    ]
  },
  "Retry": [
    {
      "ErrorEquals": ["BedrockAgentCore.ThrottlingException"],
      "IntervalSeconds": 2,
      "MaxAttempts": 3,
      "BackoffRate": 2.0
    }
  ],
  "Catch": [
    {
      "ErrorEquals": ["BedrockAgentCore.ResourceNotFoundException"],
      "Next": "HandleNotFound"
    },
    {
      "ErrorEquals": ["States.ALL"],
      "Next": "HandleError"
    }
  ],
  "End": true
}
```

## IAM policies for calling Amazon Bedrock AgentCore
<a name="bedrockagentcore-iam"></a>

The following example templates show how AWS Step Functions generates IAM policies based on the resources in your state machine definition. For more information, see [How Step Functions generates IAM policies for integrated services](service-integration-iam-templates.md) and [Discover service integration patterns in Step Functions](connect-to-resource.md).

### IAM policy examples for Amazon Bedrock AgentCore integration
<a name="bedrockagentcore-iam-policy-eg"></a>

 The following examples show how you can create IAM policies for your Step Functions execution role to interact with Amazon Bedrock AgentCore resources. 

In the following policy examples, replace the placeholder values with your own values.
+ [IAM policy to invoke a specific harness](#bedrockagentcore-policy-invoke-specific-harness)
+ [IAM policy to invoke all harnesses in an account](#bedrockagentcore-policy-invoke-all-harnesses)

#### IAM policy to invoke a specific harness
<a name="bedrockagentcore-policy-invoke-specific-harness"></a>

 The following example policy allows invoking a specific Amazon Bedrock AgentCore harness by ARN. 

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "InvokeSpecificHarness",
            "Effect": "Allow",
            "Action": [
                "bedrock-agentcore:InvokeHarness",
                "bedrock-agentcore:InvokeAgentRuntime"
            ],
            "Resource": "arn:aws:bedrock-agentcore:{{region}}:{{accountId}}:harness/{{harnessName}}"
        }
    ]
}
```

#### IAM policy to invoke all harnesses in an account
<a name="bedrockagentcore-policy-invoke-all-harnesses"></a>

 The following example policy allows invoking any Amazon Bedrock AgentCore harness in your account. We recommend scoping down to a specific harness ARN when possible. 

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "InvokeAllHarnesses",
            "Effect": "Allow",
            "Action": [
                "bedrock-agentcore:InvokeHarness",
                "bedrock-agentcore:InvokeAgentRuntime"
            ],
            "Resource": "arn:aws:bedrock-agentcore:{{region}}:{{accountId}}:harness/*"
        }
    ]
}
```

**Note**  
If your harness uses tools such as gateways, browsers, or code interpreters, those permissions are configured on the *harness execution role*, not the Step Functions execution role. For more information, see [Harness execution role permissions](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/harness-security.html) in the *Amazon Bedrock AgentCore User Guide*.