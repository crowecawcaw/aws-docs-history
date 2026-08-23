# Monitor AI agents using CloudWatch

To gain visibility into the real-time recommendations that AI agents provide to your
agents, and the customer intents they detect through natural language understanding, you
can query CloudWatch Logs. CloudWatch Logs give you visibility into the entire contact journey: the
conversation, triggers, intents, recommendations. You can also use this information for
debugging, or provide it to Support when you contact them for help.

This topic explains how to enable logging for AI agents.

###### Contents

- [Required IAM
  permissions](#permissions-cw-q "#permissions-cw-q")
- [Enable logging](#enable-assistant-logging "#enable-assistant-logging")
- [Supported log
  types](#supported-log-types-q "#supported-log-types-q")
- [Check for CloudWatch Logs quotas](#cwl-quotas "#cwl-quotas")
- [Documenting CloudWatch Events by using Interactive Handler](#documenting-cw-events-ih "#documenting-cw-events-ih")
- [Examples of common queries to
  debug assistant logs](#example2-assistant-log "#example2-assistant-log")

## Required IAM permissions

Before you enable logging for a Connect assistant, check that you have the
following AWS Identity and Access Management permissions. They are required for the user account that is
signed into the Connect Customer console:

- `wisdom:AllowVendedLogDeliveryForResource`: Required to allow
  logs to be delivered for the assistant resource.

To view an example IAM role with all the required permissions for your specific
logging destination, see [Logging that requires additional permissions [V2]](../../../AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.md#AWS-vended-logs-permissions-V2 "../../../AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.md#AWS-vended-logs-permissions-V2"). That topic contains
examples for different logging destinations, such as logs sent to CloudWatch Logs and logs
sent to Amazon S3 The examples show how to allow updates to your specific logging
destination resource.

## Enable logging for AI agents

To enable logging for AI agents, you use the CloudWatch API. Complete the following steps.

1. Get the ARN of your _assistant_ (also known as
   its [domain](ai-agent-initial-setup.md#ai-agent-requirements "ai-agent-initial-setup.md#ai-agent-requirements")). After you [create an assistant](ai-agent-initial-setup.md#enable-ai-agents-step1 "ai-agent-initial-setup.md#enable-ai-agents-step1"), you can obtain it's
   ARN from the Connect Customer console or by calling the [GetAssistant](../APIReference/API_amazon-q-connect_GetAssistant.md "../APIReference/API_amazon-q-connect_GetAssistant.md") API. The ARN follows this format:

`arn:aws:wisdom:`your-region`:`your-account-id`:assistant/`assistant-id`` 2. Call [PutDeliverySource](../../../AmazonCloudWatchLogs/latest/APIReference/API_PutDeliverySource.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_PutDeliverySource.md"): Use this CloudWatch API to create a delivery
source for the assistant. Pass the ARN of the assistant as the
`resourceArn`. For `logType`, specify
`EVENT_LOGS` to collect logs from your assistant.

```
{
"logType": "EVENT_LOGS",
"name": "`your-assistant-delivery-source`",
"resourceArn": "arn:aws:wisdom:`your-region`:`your-account-id`:assistant/`assistant_id`
}
```

3. Call [PutDeliveryDestination](../../../AmazonCloudWatchLogs/latest/APIReference/API_PutDeliveryDestination.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_PutDeliveryDestination.md"): Use this CloudWatch API to configure where
   the logs are to be stored. You can choose CloudWatch Logs, Amazon S3, or Amazon Data Firehose as the
   destination for storing logs. You must specify the ARN of one of the
   destination options for where your logs are to be stored. You can choose the
   `outputFormat` of the logs to be one of the following:
   `json`, `plain`, `w3c`,
   `raw`, `parquet`.

The following example shows how to configure logs to be stored in an
Amazon CloudWatch Logs Group and in JSON format.

```
{
"deliveryDestinationConfiguration": {
    "destinationResourceArn": "arn:aws:logs:`your-region`:`your-account-id`:log-group:`your-log-group-name`:*"
},
"name": "string",
"outputFormat": "json",
"tags": {
    "key": "value"
}
}
```

4. Call [CreateDelivery](../../../AmazonCloudWatchLogs/latest/APIReference/API_CreateDelivery.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_CreateDelivery.md"): Use this CloudWatch API to link the delivery source
   to the delivery destination that you created in the previous steps. This API
   operation associates the delivery source with the end destination.

```
{
"deliveryDestinationArn": "string",
"deliverySourceName": "string",
"tags": {
    "string": "string"
}
}
```

The following example shows how to run the previous steps as a sequence of AWS CLI
commands. This example enables event logging for an assistant and sends the logs to a
Amazon CloudWatch Logs log group. Run the commands in order, and replace each
`value` with your own resource names and ARNs.

1. Create a delivery source for the assistant. Use the assistant ARN as the
   resource ARN, and specify `EVENT_LOGS` as the log type.

```
aws logs put-delivery-source \
    --name `your-assistant-delivery-source` \
    --resource-arn arn:aws:wisdom:`your-region`:`your-account-id`:assistant/`assistant-id` \
    --log-type EVENT_LOGS
```

2. Create a delivery destination that points to your log group. To send logs to
   Amazon S3 or Amazon Data Firehose instead, specify that resource ARN.

```
aws logs put-delivery-destination \
    --name `your-delivery-destination` \
    --delivery-destination-configuration "destinationResourceArn=arn:aws:logs:`your-region`:`your-account-id`:log-group:`your-log-group-name`" \
    --output-format json
```

3. Link the delivery source to the delivery destination. Use the destination ARN
   that the previous command returns.

```
aws logs create-delivery \
    --delivery-source-name `your-assistant-delivery-source` \
    --delivery-destination-arn arn:aws:logs:`your-region`:`your-account-id`:delivery-destination:`your-delivery-destination`
```

After you create the delivery, you can view logged events in your log group. To
confirm that logging works, generate assistant activity, and then query the log group as
described in [Examples of common queries to
debug assistant logs](#example2-assistant-log "#example2-assistant-log").

## Supported log types

AI agents support the following log type:

- `EVENT_LOGS`: Logs that track event of an Connect assistant
  during calls, chats, tasks, and emails.

## Check for CloudWatch Logs quotas

We recommend checking [Amazon CloudWatch Logs endpoints and quotas](../../../general/latest/gr/cwl_region.md "../../../general/latest/gr/cwl_region.md")
to see whether there are any quotas for making CloudWatch Logs delivery-related API calls.
Quotas set a maximum number of times you can call an API or create a resource.
Exceeding the limit results in a `ServiceQuotaExceededException`
error.

## Documenting CloudWatch Events by using Interactive Handler

### Event Type Definitions

The following table describes each event type. Note that different event types
contain different fields. Refer to the [Field Definitions](#field-definitions "#field-definitions") section for detailed information about
each field.

| EventType                                         | Definition                                                                                                                                                                                                                                                                  |
| ------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| TRANSCRIPT\_CREATE\_SESSION                       | Logged when a new AI agents session is created.<br>This marks the beginning of a conversation.                                                                                                                                                                              |
| TRANSCRIPT\_INTENT\_TRIGGERING\_REFERENCE         | Logged when a specific customer intent is detected in the<br>conversation, which might trigger automated responses or<br>workflows.                                                                                                                                         |
| TRANSCRIPT\_LARGE\_LANGUAGE\_MODEL\_INVOCATION    | Logged when a large language model (LLM) is invoked to<br>generate responses or process conversation content. Records the<br>inputs to and outputs from the LLM.                                                                                                            |
| TRANSCRIPT\_QUERY\_ASSISTANT                      | Logged when one of the following AI agents is invoked:<br>AnswerRecommendation, CaseSummarization, EmailGenerativeAnswer,<br>EmailOverview, EmailResponse, ManualSearch, NoteTaking.                                                                                        |
| TRANSCRIPT\_RECOMMENDATION                        | Logged when the system provides a recommendation to an agent<br>or customer, which might include knowledge articles, generated<br>responses, or suggested actions.                                                                                                          |
| TRANSCRIPT\_RESULT\_FEEDBACK                      | Logged when feedback is provided about a search or query<br>result's usefulness or relevance.                                                                                                                                                                               |
| TRANSCRIPT\_SELF\_SERVICE\_MESSAGE                | Logged when a customer interacts with a SelfService AI agent                                                                                                                                                                                                                |
| TRANSCRIPT\_SESSION\_POLLED                       | Logged when the system detects an agent is connected to a<br>session (A session is polled when a GetRecommendations API call<br>has been made)                                                                                                                              |
| TRANSCRIPT\_TRIGGER\_DETECTION\_MODEL\_INVOCATION | Logged when the trigger detection model is invoked to<br>determine if a conversation has intents                                                                                                                                                                            |
| TRANSCRIPT\_UTTERANCE                             | Logged when a message is sent by any participant in the<br>conversation, recording the actual conversation content.                                                                                                                                                         |
| TRANSCRIPT\_ORCHESTRATION\_MESSAGE                | Logged for each step within an orchestration loop, including<br>the initial customer message, bot text responses, reasoning,<br>tool use requests, and tool results. Captures the full detail<br>of multi-turn agentic reasoning performed by an Orchestration<br>AI agent. |
| TRANSCRIPT\_ORCHESTRATION\_ERROR                  | Logged when an error occurs during orchestration, such as<br>exceeding the maximum number of orchestration iterations,<br>system capacity constraints, or a general orchestration<br>failure.                                                                               |
| TRANSCRIPT\_AI\_AGENT\_TRACE                      | Logged for each execution span during AI agent orchestration,<br>capturing detailed traces including LLM configuration, token usage,<br>messages, and guardrail assessment results.                                                                                         |

### Field Definitions

The following table describes each field.

| Field                               | Definition                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| ai\_agent\_id                       | Unique identifier for the AI agent<br>resource.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| assistant\_id                       | Unique identifier for the Connect assistant<br>resource.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| completion                          | The raw completion text returned by the LLM or generated for<br>the message.                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| connect\_user\_arn                  | Amazon Resource Name (ARN) of the Connect user accessing the<br>session.                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| event\_timestamp                    | Unix timestamp (in milliseconds) when the event<br>occurred.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| event\_type                         | Type of the event, indicating what action or process occurred<br>in the system.                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| generation\_id                      | Unique identifier for a specific AI-generated<br>response.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| intent                              | The intent text or description.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| intent\_clicked                     | Boolean indicating if the recommendation was triggered by a<br>clicked intent.                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| intent\_id                          | Unique identifier for the detected intent.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| issue\_probability                  | Numerical probability (0.0–1.0) that an issue was detected in<br>the conversation (A probability greater than 0.5 will invoke<br>intent generation)                                                                                                                                                                                                                                                                                                                                                                                                    |
| is\_recommendation\_useful          | Boolean indicating whether the user found the result<br>helpful.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| is\_valid\_trigger                  | Boolean indicating whether the detection model analysis<br>resulted in a valid trigger.                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| model\_id                           | Identifier of the AI model used to invoke the LLM.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| parsed\_response                    | The processed/parsed version of the language model response,<br>often in structured format.                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| prompt                              | The input prompt used to invoke the LLM.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| prompt\_type                        | Type of AI prompt used for processing the<br>message or query.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| recommendation                      | The actual recommendation text content provided to the<br>user                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| recommendation\_id                  | Unique identifier for the recommendation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| response                            | The final response text generated for the user after<br>processing.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| session\_event\_id                  | Unique identifier for a specific event within the<br>session.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| session\_event\_ids                 | List of session event identifiers.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| session\_id                         | Unique identifier for the AI agents session.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| session\_message\_id                | Unique identifier for a self-service message within a<br>session.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| session\_name                       | Name of the session.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| utterance                           | The actual message text exchanged in the<br>conversation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| orchestration\_id                   | Unique identifier for the orchestration run. Corresponds to<br>the initial customer message ID that triggered<br>orchestration.                                                                                                                                                                                                                                                                                                                                                                                                                        |
| orchestration\_iteration            | The iteration number within the orchestration loop.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ai\_agent\_orchestration\_use\_case | The orchestrator use case, such as<br>`CONNECT_AGENT_ASSISTANCE` or<br>`CONNECT_SELF_SERVICE`.                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| participant                         | The participant role for the message, such as<br>`CUSTOMER` or `BOT`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| values                              | JSON-serialized list of message values. Each entry has a<br>type: `text` (with a text value),<br>`tool_use` (with toolUseId, toolId, name, and<br>arguments), `tool_result` (with toolUseId, toolId,<br>name, values, and error), or `reasoning` (with a<br>text value).                                                                                                                                                                                                                                                                               |
| guardrail\_blocked                  | Boolean indicating whether the response was blocked by an<br>AI guardrail.                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| orchestration\_error                | JSON-serialized error details containing<br>`errorMessage` and an optional<br>`errorDetails` object (with<br>`estimatedInputTokens` and<br>`estimatedOutputTokens`).                                                                                                                                                                                                                                                                                                                                                                                   |
| span                                | JSON-serialized map of the full span object. Each key is<br>snake\_case. Notable keys include<br>`input_messages` (conversation history sent to the<br>model), `output_messages` (model response messages),<br>`guardrail_assessments` (list of guardrail<br>evaluation results with `guardrailId`,<br>`guardrailName`, `source`,<br>`action`, and `policies`), and<br>`input_messages_truncated` (`"true"` when<br>input messages were truncated to fit the 256KB record limit).<br>Present only when `event_type` is<br>`TRANSCRIPT_AI_AGENT_TRACE`. |

### Examples of assistant logs

Below are examples of different event logs for each event type. Refer to the
[Event Type Definitions](#event-type-definitions "#event-type-definitions") section for detailed explanations
of each event type.

#### CreateSession

```

{
"assistant_id": "a1c2d3e4-5b67-4a89-9abc-def012345678",
"event_timestamp": 1729530173612,
"event_type": "TRANSCRIPT_CREATE_SESSION",
"session_id": "s9f8e7d6-1234-4cde-9abc-ffeeddccbbaa",
"session_name": "nabbccdd-9999-4b23-aaee-112233445566"
}

```

#### IntentTriggeringReference

```

{
"assistant_id": "a1c2d3e4-5b67-4a89-9abc-def012345678",
"event_timestamp": 1729530173623,
"event_type": "TRANSCRIPT_INTENT_TRIGGERING_REFERENCE",
"intent": "To learn about how to autoscale DynamoDB.",
"intent_id": "i78bc90-1234-4dce-8012-f0e1d2c3b4a5",
"session_id": "s9f8e7d6-1234-4cde-9abc-ffeeddccbbaa"
}

```

#### LargeLanguageModelInvocation

Query Reformulation

```

{
"ai_agent_id": "ai112233-7a85-4b3c-8def-0123456789ab",
"assistant_id": "a1c2d3e4-5b67-4a89-9abc-def012345678",
"completion": "<query>The customer is asking for information on how to autoscale DynamoDB.</query>",
"event_timestamp": 1729530173645,
"event_type": "TRANSCRIPT_LARGE_LANGUAGE_MODEL_INVOCATION",
"generation_id": "gabc1234-9def-47ff-bb88-abcdefabcdef",
"intent_id": "i78bc90-1234-4dce-8012-f0e1d2c3b4a5"
"model_id": "us.amazon.nova-lite-v1:0",
"parsed_response": "The customer is asking for information on how to autoscale DynamoDB.",
"prompt": "{\"anthropic_version\":\"bedrock-2023-05-31\",\"max_tokens\":1024,\"system\":\"You are a...\"}",
"prompt_type": "BEDROCK_KB_QUERY_REFORMULATION",
"session_event_id": "seaa9988-2233-4f44-8899-abcabcabcabc",
"session_id": "s9f8e7d6-1234-4cde-9abc-ffeeddccbbaa"
}

```

Intent Detection

```

{
"ai_agent_id": "ai112233-7a85-4b3c-8def-0123456789ab",
"assistant_id": "a1c2d3e4-5b67-4a89-9abc-def012345678",
"completion": "no</malice>\n  - Step 2. <specific>yes</specific>\n  - Step 3. <intent>To learn how to autoscale DynamoDB.</intent>",
"event_timestamp": 1729530173645,
"event_type": "TRANSCRIPT_LARGE_LANGUAGE_MODEL_INVOCATION",
"generation_id": "gabc1234-9def-47ff-bb88-abcdefabcdef",
"intent_id": "i78bc90-1234-4dce-8012-f0e1d2c3b4a5"
"model_id": "us.amazon.nova-lite-v1:0",
"parsed_response": "To learn how to autoscale DynamoDB.",
"prompt": "{\"anthropic_version\":\"bedrock-2023-05-31\",\"max_tokens\":1024,\"system\":\"You are a...\"}",
"prompt_type": "GENERATIVE_INTENT_DETECTION",
"session_event_id": "seaa9988-2233-4f44-8899-abcabcabcabc",
"session_id": "s9f8e7d6-1234-4cde-9abc-ffeeddccbbaa"
}

```

Intent Answer Generation

```

{
"ai_agent_id": "ai112233-7a85-4b3c-8def-0123456789ab",
"assistant_id": "a1c2d3e4-5b67-4a89-9abc-def012345678",
"completion": "{\"citations\":[{\"citation\":{\"generatedResponsePart\":{\"textResponsePart\":{\"span\":{\"end\":1065,\"start\":0},\"text\":\"\\nDynamoDB auto s\"}}}}]}",
"event_timestamp": 1729530173645,
"event_type": "TRANSCRIPT_LARGE_LANGUAGE_MODEL_INVOCATION",
"generation_id": "gabc1234-9def-47ff-bb88-abcdefabcdef",
"intent_id": "i78bc90-1234-4dce-8012-f0e1d2c3b4a5",
"model_id": "us.anthropic.claude-3-7-sonnet-20250219-v1:0",
"parsed_response": "DynamoDB auto scaling works by creating CloudWatch alarms that monitor your table's activity. When the...",
"prompt": "{\"input\":{\"text\":\"The customer is seeking information on how to autoscale DynamoDB. Key utterance: \\\"How can \"}}",
"prompt_type": "BEDROCK_KB_GENERATIVE_ANSWER",
"session_event_id": "seaa9988-2233-4f44-8899-abcabcabcabc",
"session_id": "s9f8e7d6-1234-4cde-9abc-ffeeddccbbaa"
}

```

Manual Search Generation

```

{
"ai_agent_id": "ai112233-7a85-4b3c-8def-0123456789ab",
"assistant_id": "a1c2d3e4-5b67-4a89-9abc-def012345678",
"completion": "no</malice>\n  - Step 2. <specific>yes</specific>\n  - Step 3. <intent>To learn how to autoscale DynamoDB.</intent>",
"event_timestamp": 1729530173645,
"event_type": "TRANSCRIPT_LARGE_LANGUAGE_MODEL_INVOCATION",
"generation_id": "gabc1234-9def-47ff-bb88-abcdefabcdef",
"intent_id": "i78bc90-1234-4dce-8012-f0e1d2c3b4a5",
"model_id": "us.anthropic.claude-3-7-sonnet-20250219-v1:0",
"parsed_response": "DynamoDB auto scaling works by creating CloudWatch alarms that monitor...",
"prompt": "{\"anthropic_version\":\"bedrock-2023-05-31\",\"max_tokens\":1024,\"system\":\"You are a...\"}",
"prompt_type": "BEDROCK_KB_GENERATIVE_ANSWER",
"session_id": "******************-*****************"
}

```

#### QueryAssistant

```

{
"assistant_id": "a1c2d3e4-5b67-4a89-9abc-def012345678",
"event_timestamp": 1729530173667,
"event_type": "TRANSCRIPT_QUERY_ASSISTANT",
"recommendation_id": "r0001112-3f4e-4fa5-9111-aabbccddeeff",
"session_id": "s9f8e7d6-1234-4cde-9abc-ffeeddccbbaa"
}

```

#### Recommendation

```

{
"assistant_id": "a1c2d3e4-5b67-4a89-9abc-def012345678",
"event_timestamp": 1729530173656,
"event_type": "TRANSCRIPT_RECOMMENDATION",
"intent_clicked": 1,
"intent_id": "i78bc90-1234-4dce-8012-f0e1d2c3b4a5",
"recommendation_id": "r0001112-3f4e-4fa5-9111-aabbccddeeff",
"session_id": "s9f8e7d6-1234-4cde-9abc-ffeeddccbbaa"
}

```

#### ResultFeedback

```

{
"assistant_id": "a1c2d3e4-5b67-4a89-9abc-def012345678",
"event_timestamp": 1729530173667,
"event_type": "TRANSCRIPT_RESULT_FEEDBACK",
"generation_id": "gabc1234-9def-47ff-bb88-abcdefabcdef",
"is_recommendation_useful": 1,
"recommendation_id": "r0001112-3f4e-4fa5-9111-aabbccddeeff"
}

```

#### SelfServiceMessage

```

{
"assistant_id": "a1c2d3e4-5b67-4a89-9abc-def012345678",
"completion": "{\"citations\":[{\"generatedResponsePart\":{\"textResponsePart\":{\"span\":{\"end\":276,\"start\":0},\"text\":\"To autoscale Amazon DynamoDB...\"}}]}",
"event_timestamp": 1729530173678,
"event_type": "TRANSCRIPT_SELF_SERVICE_MESSAGE",
"model_id": "us.amazon.nova-pro-v1:0",
"parsed_response": "To autoscale Amazon DynamoDB, follow these steps:...",
"prompt": "{\"input\":{\"text\":\"how to autoscale dynamodb\"},\"retrieveAndGenerateConfiguration\":...}",
"prompt_type": "SELF_SERVICE_ANSWER_GENERATION",
"session_id": "s9f8e7d6-1234-4cde-9abc-ffeeddccbbaa",
"session_message_id": "mdee1234-5678-4eab-9333-ffeebb998877",
"utterance": "[Customer] How can I autoscale DyanmoDB?"
}

```

#### TranscriptSessionPolled

```

{
"assistant_id": "a1c2d3e4-5b67-4a89-9abc-def012345678",
"connect_user_arn": "arn:aws:connect:us-east-1:204585150770:instance/seaa9988-2233-4f44-8899-abcabcabcabc/agent/agbbccdd-9999-4b23-aaee-112233445566",
"event_timestamp": 1729530173623,
"event_type": "TRANSCRIPT_SESSION_POLLED",
"session_id": "s9f8e7d6-1234-4cde-9abc-ffeeddccbbaa",
"session_name": "nabbccdd-9999-4b23-aaee-112233445566"
}

```

#### TriggerDetectionModelInvocation

```

{
"assistant_id": "a1c2d3e4-5b67-4a89-9abc-def012345678",
"event_timestamp": 1729530173634,
"event_type": "TRANSCRIPT_TRIGGER_DETECTION_MODEL_INVOCATION",
"is_valid_trigger": 1,
"issue_probability": "0.87",
"session_event_id": "seaa9988-2233-4f44-8899-abcabcabcabc",
"session_event_ids": ["seaa9988-2233-4f44-8899-abcabcabcabc"],
"session_id": "s9f8e7d6-1234-4cde-9abc-ffeeddccbbaa"
}

```

#### Utterance

```

{
"assistant_id": "a1c2d3e4-5b67-4a89-9abc-def012345678",
"event_timestamp": 1729530173623,
"event_type": "TRANSCRIPT_UTTERANCE",
"session_event_id": "seaa9988-2233-4f44-8899-abcabcabcabc",
"session_id": "s9f8e7d6-1234-4cde-9abc-ffeeddccbbaa",
"utterance": "[Customer] My laptop won't connect to WiFi after the recent update"
}

```

#### OrchestrationMessage

Customer message

```

{
"ai_agent_id": "ai112233-7a85-4b3c-8def-0123456789ab",
"ai_agent_orchestration_use_case": "CONNECT_AGENT_ASSISTANCE",
"assistant_id": "a1c2d3e4-5b67-4a89-9abc-def012345678",
"event_timestamp": 1729530173612,
"event_type": "TRANSCRIPT_ORCHESTRATION_MESSAGE",
"model_id": "us.anthropic.claude-4-5-sonnet-20250929-v1:0",
"orchestration_id": "m1234567-abcd-4ef0-9876-aabbccddeeff",
"participant": "CUSTOMER",
"session_id": "s9f8e7d6-1234-4cde-9abc-ffeeddccbbaa",
"session_message_id": "m1234567-abcd-4ef0-9876-aabbccddeeff",
"values": "[{\"type\":\"text\",\"value\":\"How do I reset my password?\"}]"
}

```

Bot text response

```

{
"ai_agent_id": "ai112233-7a85-4b3c-8def-0123456789ab",
"ai_agent_orchestration_use_case": "CONNECT_AGENT_ASSISTANCE",
"assistant_id": "a1c2d3e4-5b67-4a89-9abc-def012345678",
"event_timestamp": 1729530174234,
"event_type": "TRANSCRIPT_ORCHESTRATION_MESSAGE",
"guardrail_blocked": false,
"model_id": "us.anthropic.claude-4-5-sonnet-20250929-v1:0",
"orchestration_id": "m1234567-abcd-4ef0-9876-aabbccddeeff",
"orchestration_iteration": 1,
"participant": "BOT",
"session_id": "s9f8e7d6-1234-4cde-9abc-ffeeddccbbaa",
"session_message_id": "mfff1234-5678-4eab-9333-112233445566",
"values": "[{\"type\":\"text\",\"value\":\"I can help you reset your password. Let me look up your account.\"}]"
}

```

Tool use

```

{
"ai_agent_id": "ai112233-7a85-4b3c-8def-0123456789ab",
"ai_agent_orchestration_use_case": "CONNECT_AGENT_ASSISTANCE",
"assistant_id": "a1c2d3e4-5b67-4a89-9abc-def012345678",
"event_timestamp": 1729530174500,
"event_type": "TRANSCRIPT_ORCHESTRATION_MESSAGE",
"model_id": "us.anthropic.claude-4-5-sonnet-20250929-v1:0",
"orchestration_id": "m1234567-abcd-4ef0-9876-aabbccddeeff",
"orchestration_iteration": 1,
"participant": "BOT",
"session_id": "s9f8e7d6-1234-4cde-9abc-ffeeddccbbaa",
"session_message_id": "maaa2222-3333-4bbb-cccc-ddddeeeeffff",
"values": "[{\"type\":\"tool_use\",\"toolUseId\":\"toolu_01ABC\",\"toolId\":\"ResetPassword\",\"name\":\"ResetPassword\",\"arguments\":{\"email\":\"customer@example.com\"}}]"
}

```

Tool result

```

{
"ai_agent_id": "ai112233-7a85-4b3c-8def-0123456789ab",
"ai_agent_orchestration_use_case": "CONNECT_AGENT_ASSISTANCE",
"assistant_id": "a1c2d3e4-5b67-4a89-9abc-def012345678",
"event_timestamp": 1729530175100,
"event_type": "TRANSCRIPT_ORCHESTRATION_MESSAGE",
"model_id": "us.anthropic.claude-4-5-sonnet-20250929-v1:0",
"orchestration_id": "m1234567-abcd-4ef0-9876-aabbccddeeff",
"orchestration_iteration": 1,
"participant": "BOT",
"session_id": "s9f8e7d6-1234-4cde-9abc-ffeeddccbbaa",
"session_message_id": "mbbb3333-4444-5ccc-dddd-eeeeffff0000",
"values": "[{\"type\":\"tool_result\",\"toolUseId\":\"toolu_01ABC\",\"toolId\":\"ResetPassword\",\"name\":\"ResetPassword\",\"values\":[{\"type\":\"text\",\"value\":\"Password reset email sent successfully.\"}],\"error\":null}]"
}

```

Reasoning

```

{
"ai_agent_id": "ai112233-7a85-4b3c-8def-0123456789ab",
"ai_agent_orchestration_use_case": "CONNECT_AGENT_ASSISTANCE",
"assistant_id": "a1c2d3e4-5b67-4a89-9abc-def012345678",
"event_timestamp": 1729530175200,
"event_type": "TRANSCRIPT_ORCHESTRATION_MESSAGE",
"model_id": "us.anthropic.claude-4-5-sonnet-20250929-v1:0",
"orchestration_id": "m1234567-abcd-4ef0-9876-aabbccddeeff",
"orchestration_iteration": 1,
"participant": "BOT",
"session_id": "s9f8e7d6-1234-4cde-9abc-ffeeddccbbaa",
"session_message_id": "mccc4444-5555-6ddd-eeee-ffff00001111",
"values": "[{\"type\":\"reasoning\",\"value\":\"The password reset was successful. I should inform the customer and ask if they need further help.\"}]"
}

```

#### OrchestrationError

Maximum orchestration iterations exceeded

```

{
"ai_agent_id": "ai112233-7a85-4b3c-8def-0123456789ab",
"ai_agent_orchestration_use_case": "CONNECT_AGENT_ASSISTANCE",
"assistant_id": "a1c2d3e4-5b67-4a89-9abc-def012345678",
"event_timestamp": 1729530180000,
"event_type": "TRANSCRIPT_ORCHESTRATION_ERROR",
"model_id": "us.anthropic.claude-4-5-sonnet-20250929-v1:0",
"orchestration_error": "{\"errorMessage\":\"The orchestration exceeded the maximum number of iterations\"}",
"orchestration_id": "m1234567-abcd-4ef0-9876-aabbccddeeff",
"orchestration_iteration": 9,
"session_id": "s9f8e7d6-1234-4cde-9abc-ffeeddccbbaa"
}

```

System capacity constraints

```

{
"ai_agent_id": "ai112233-7a85-4b3c-8def-0123456789ab",
"ai_agent_orchestration_use_case": "CONNECT_AGENT_ASSISTANCE",
"assistant_id": "a1c2d3e4-5b67-4a89-9abc-def012345678",
"event_timestamp": 1729530180000,
"event_type": "TRANSCRIPT_ORCHESTRATION_ERROR",
"model_id": "us.anthropic.claude-4-5-sonnet-20250929-v1:0",
"orchestration_error": "{\"errorMessage\":\"System capacity is constrained. We are actively working on scaling system to prevent such failures.\",\"errorDetails\":{\"estimatedInputTokens\":50000,\"estimatedOutputTokens\":2048}}",
"orchestration_id": "m1234567-abcd-4ef0-9876-aabbccddeeff",
"orchestration_iteration": 3,
"session_id": "s9f8e7d6-1234-4cde-9abc-ffeeddccbbaa"
}

```

#### AIAgentTrace

Successful orchestration span (no guardrail intervention)

```

{
"timestamp": 1729530173612,
"resource_arn": "arn:aws:wisdom:us-east-1:204585150770:assistant/a1c2d3e4-5b67-4a89-9abc-def012345678",
"event_timestamp": 1729530175612,
"event_type": "TRANSCRIPT_AI_AGENT_TRACE",
"session_id": "s9f8e7d6-1234-4cde-9abc-ffeeddccbbaa",
"ai_agent_id": "ai112233-7a85-4b3c-8def-0123456789ab",
"model_id": "us.anthropic.claude-4-5-sonnet-20250929-v1:0",
"span": {
    "span_id": "7a3f2b1c-4d5e-6f7a-8b9c-0d1e2f3a4b5c",
    "parent_span_id": "eb06e7cf-c3ba-4e75-86ef-ba761fd0ee30",
    "span_name": "inference",
    "span_type": "CLIENT",
    "start_timestamp": "1729530173612",
    "end_timestamp": "1729530175612",
    "status": "OK",
    "operation_name": "inference",
    "provider_name": "aws.bedrock",
    "session_name": "nabbccdd-9999-4b23-aaee-112233445566",
    "ai_agent_arn": "arn:aws:wisdom:us-east-1:204585150770:ai-agent/ai112233-7a85-4b3c-8def-0123456789ab",
    "ai_agent_type": "ANSWER_RECOMMENDATION",
    "ai_agent_name": "MyAgent",
    "ai_agent_version": "3",
    "ai_agent_orchestrator_use_case": "Connect.AgentAssistance",
    "request_model": "us.anthropic.claude-4-5-sonnet-20250929-v1:0",
    "request_max_tokens": "4096",
    "temperature": "1.0",
    "response_finish_reasons": "[\"end_turn\"]",
    "usage_input_tokens": "5274",
    "usage_output_tokens": "266",
    "usage_total_tokens": "5540",
    "cache_read_input_tokens": "4800",
    "cache_write_input_tokens": "0",
    "prompt_arn": "arn:aws:wisdom:us-east-1:204585150770:ai-prompt/prompt-abc:2",
    "prompt_id": "prompt-abc",
    "prompt_type": "ORCHESTRATION",
    "prompt_name": "Agent Assistance Orchestration",
    "prompt_version": "2",
    "time_to_first_token_ms": "850",
    "input_messages": "[{\"messageId\":\"msg-1\",\"participant\":\"CUSTOMER\",\"timestamp\":1729530173000,\"values\":[{\"text\":{\"value\":\"How can I autoscale DynamoDB?\"}}]}]",
    "output_messages": "[{\"messageId\":\"msg-2\",\"participant\":\"BOT\",\"timestamp\":1729530175612,\"values\":[{\"text\":{\"value\":\"DynamoDB auto scaling works by creating CloudWatch alarms that monitor your table's activity.\"}}]}]",
    "system_instructions": "[{\"messageId\":\"sys-1\",\"participant\":\"USER\",\"timestamp\":0,\"values\":[{\"text\":{\"value\":\"You are an AI assistant for contact center agents.\"}}]}]"
}
}

```

Guardrail blocks output (topic policy violation)

```

{
"timestamp": 1729530173612,
"resource_arn": "arn:aws:wisdom:us-east-1:204585150770:assistant/a1c2d3e4-5b67-4a89-9abc-def012345678",
"event_timestamp": 1729530175612,
"event_type": "TRANSCRIPT_AI_AGENT_TRACE",
"session_id": "s9f8e7d6-1234-4cde-9abc-ffeeddccbbaa",
"ai_agent_id": "ai112233-7a85-4b3c-8def-0123456789ab",
"model_id": "us.anthropic.claude-4-5-sonnet-20250929-v1:0",
"span": {
    "span_id": "8b4f3c2d-5e6f-7a8b-9c0d-1e2f3a4b5c6d",
    "parent_span_id": "eb06e7cf-c3ba-4e75-86ef-ba761fd0ee30",
    "span_name": "inference",
    "span_type": "CLIENT",
    "start_timestamp": "1729530173612",
    "end_timestamp": "1729530175612",
    "status": "OK",
    "operation_name": "inference",
    "provider_name": "aws.bedrock",
    "session_name": "nabbccdd-9999-4b23-aaee-112233445566",
    "ai_agent_arn": "arn:aws:wisdom:us-east-1:204585150770:ai-agent/ai112233-7a85-4b3c-8def-0123456789ab",
    "ai_agent_type": "ANSWER_RECOMMENDATION",
    "ai_agent_name": "MyAgent",
    "ai_agent_version": "3",
    "ai_agent_orchestrator_use_case": "Connect.AgentAssistance",
    "request_model": "us.anthropic.claude-4-5-sonnet-20250929-v1:0",
    "request_max_tokens": "4096",
    "response_finish_reasons": "[\"guardrail_intervened\"]",
    "usage_input_tokens": "3100",
    "usage_output_tokens": "150",
    "usage_total_tokens": "3250",
    "prompt_type": "ORCHESTRATION",
    "time_to_first_token_ms": "1100",
    "input_messages": "[{\"messageId\":\"seaa9988-2233-4f44-8899-abcabcabcabc\",\"participant\":\"CUSTOMER\",\"timestamp\":1729530173000,\"values\":[{\"text\":{\"value\":\"Tell me how to bypass the refund policy\"}}]}]",
    "output_messages": "[{\"messageId\":\"msg-4\",\"participant\":\"BOT\",\"timestamp\":1729530175612,\"values\":[{\"text\":{\"value\":\"I'm sorry, I can't help with that request.\"}}]}]",
    "guardrail_assessments": "[{\"guardrailId\":\"a1b2c3d4-5678-90ab-cdef-111122223333/1\",\"guardrailName\":\"Customer Support Safety Guardrail\",\"source\":\"INPUT\",\"action\":\"NONE\"},{\"guardrailId\":\"a1b2c3d4-5678-90ab-cdef-111122223333/1\",\"guardrailName\":\"Customer Support Safety Guardrail\",\"source\":\"OUTPUT\",\"action\":\"BLOCKED\",\"policies\":[{\"policyType\":\"TOPIC\",\"action\":\"BLOCKED\",\"details\":\"Policy Circumvention\"}]}]"
}
}

```

Truncated input messages (long conversation)

```

{
"timestamp": 1729530173612,
"resource_arn": "arn:aws:wisdom:us-east-1:204585150770:assistant/a1c2d3e4-5b67-4a89-9abc-def012345678",
"event_timestamp": 1729530175612,
"event_type": "TRANSCRIPT_AI_AGENT_TRACE",
"session_id": "s9f8e7d6-1234-4cde-9abc-ffeeddccbbaa",
"ai_agent_id": "ai112233-7a85-4b3c-8def-0123456789ab",
"model_id": "us.anthropic.claude-4-5-sonnet-20250929-v1:0",
"span": {
    "span_id": "9c5f4d3e-6f7a-8b9c-0d1e-2f3a4b5c6d7e",
    "parent_span_id": "eb06e7cf-c3ba-4e75-86ef-ba761fd0ee30",
    "span_name": "inference",
    "span_type": "CLIENT",
    "start_timestamp": "1729530173612",
    "end_timestamp": "1729530175612",
    "status": "OK",
    "operation_name": "inference",
    "provider_name": "aws.bedrock",
    "session_name": "nabbccdd-9999-4b23-aaee-112233445566",
    "request_model": "us.anthropic.claude-4-5-sonnet-20250929-v1:0",
    "response_finish_reasons": "[\"end_turn\"]",
    "usage_input_tokens": "48000",
    "usage_output_tokens": "500",
    "usage_total_tokens": "48500",
    "input_messages": "[{\"messageId\":\"msg-98\",\"participant\":\"CUSTOMER\",\"timestamp\":1729530173000,\"values\":[{\"text\":{\"value\":\"What about the shipping timeline?\"}}]}]",
    "input_messages_truncated": "true",
    "output_messages": "[{\"messageId\":\"msg-99\",\"participant\":\"BOT\",\"timestamp\":1729530175612,\"values\":[{\"text\":{\"value\":\"Based on your location, delivery takes 3-5 business days after shipping.\"}}]}]",
    "guardrail_assessments": "[{\"guardrailId\":\"a1b2c3d4-5678-90ab-cdef-111122223333/1\",\"guardrailName\":\"Customer Support Safety Guardrail\",\"source\":\"INPUT\",\"action\":\"NONE\"},{\"guardrailId\":\"a1b2c3d4-5678-90ab-cdef-111122223333/1\",\"guardrailName\":\"Customer Support Safety Guardrail\",\"source\":\"OUTPUT\",\"action\":\"NONE\"}]"
}
}

```

## Examples of common queries to debug assistant logs

You can interact with logs by using queries. For example, you can query for all
events within a session by using `SESSION_NAME`.

Following are two common queries to return all the logs generated for a specific
session.

- `filter session_name =
 "`SessionName`"`
- `filter session_id =
 "`SessionId`"`
