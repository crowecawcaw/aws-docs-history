# Batching HTTP action messages

You can use batching to send multiple HTTP action messages in a single request.

## Overview

Batching enables you to send messages from AWS IoT Core Rules Engine to your HTTP endpoints in batches.
This functionality can help reduce your costs by lowering the number of HTTP action executions as well as
improve efficiency by reducing the overhead associated with establishing new connections.

###### Note

The batched HTTP action is metered as a single action. You are metered in increments of 5 kiB, based on the size of outbound batched payload emitted by the AWS IoT Core Rules Engine to the downstream service. For more information, see the [AWS IoT Core pricing page](https://aws.amazon.com/iot-core/pricing/ "https://aws.amazon.com/iot-core/pricing/").

When you enable batching in the definition of your IoT Rule Action, the following parameters will be available for configuration:

`maxBatchOpenMs`

The maximum amount of time (in milliseconds) an outgoing message waits for other messages to create the batch.
The higher the setting, the longer the latency of the batched HTTP action.

Minimum Value: 5 ms. Maximum Value: 200 ms.

Default Value: 20 ms

Supports [substitution templates](iot-substitution-templates.md "iot-substitution-templates.md"): No

`maxBatchSize`

The maximum number of messages that are batched together in a single IoT rule action execution.

Minimum Value: 2 messages. Maximum Value: 10 messages

Default Value: 10 messages

Supports [substitution templates](iot-substitution-templates.md "iot-substitution-templates.md"): No

`maxBatchSizeBytes`

Maximum size of a message batch, in bytes.

Minimum Value: 100 bytes. Maximum Value: 131,072 bytes

Default Value: 5120 bytes

Supports [substitution templates](iot-substitution-templates.md "iot-substitution-templates.md"): No

###### Important

When you specify multiple batch parameters, batching completes when the first limit is reached. For example, if you specify 100 ms as the Maximum Batch Open Time and 5 kiB as the Maximum Batch Size, and Rules Engine batches only 2 kiB within 100 ms, then a 2 kiB batch will be created and sent.

## Using HTTP headers in a batch

When you use headers in your HTTP action, the batched request uses the header value from the last message that was added to the batch (not necessarily the last message you published). We recommend using header values that are either:

- Identical across all messages in the batch
- Applicable to all messages (for example, authentication credentials)

The headers are sent with the HTTP request and are not part of the message body.

###### Note

When batching is enabled:

- The batched request automatically includes the `Content-Type: application/json` header, as the batch is sent as a JSON array.
- We can't guarantee that the last message in the batch is the last message that you published. It is the last message that made it into the batch.

## Payload Example

The following example shows the structure of a batched message payload sent to your HTTP endpoint:

```
[
  {
    "user_id": "user1",
    "steps_today": 1000
  },
  {
    "user_id": "user2",
    "steps_today": 21000
  },
  {
    "user_id": "user8",
    "steps_today": 1500
  },
  ...
]
```

## Limitations

The following are limitations on batching:

- AWS IoT Core does not guarantee overall message ordering. Batching is performed locally on each host, which may result in messages within a batch being processed in a different order than they were received.
- AWS IoT Core does not provide message processing support on the receiver side. You are responsible for ensuring that your downstream service is configured to accept and process data in batches.
- Cross-account batching is not supported, even if messages are destined for the same resource identifier (HTTP URL or resource ARN).
- AWS IoT Core does not guarantee that the batch size will meet the configuration you specified. Batches may be smaller than your configured limits based on timing and message flow.
- When batching is enabled, binary payloads (non-UTF-8 data) are not supported. Only UTF-8 text payloads (such as JSON) are accepted. To send binary data, base64 encode it before sending it to the HTTP action, and then decode it at your receiving endpoint. For example, you can use the [encode function](iot-sql-functions.md#iot-function-encode "iot-sql-functions.md#iot-function-encode") in IoT rules to encode the binary payload. Alternatively, you can encode the binary payload in your IoT device and publish it to AWS IoT Core.

## Error Actions for Batching

You will not be able to define a separate batching logic in your Error Action definition.
However, your Error Action will support batching if you have defined batching logic in your primary Action.

When a batch request fails, AWS IoT Core Rules engine will follow the [HTTP action retry logic](https-rule-action.md#https-rule-action-retry-logic "https-rule-action.md#https-rule-action-retry-logic"). After the final retry attempt,
an error action will be invoked for each individual message.

The following is an example of an error action message with batching enabled:

```
{
    "ruleName": "FailedTopicRule",
    "topic": "topic/rulesengine",
    "payloadsWithMetadata": [
        {
            "id": 1,
            "cloudwatchTraceId": "bebd6d93-6d4a-899e-9e40-56e82252d2be",
            "clientId": "Test",
            "sourceIp": "10.0.0.0",
            "base64OriginalPayload": "eyJ1c2VyX2lkIjogInVzZXI1NjQ3IiwgInN0ZXBzX3RvZGF5IjogMTMzNjUsICJ0aW1lc3RhbXAiOiAiMjAyNS0xMC0wOVQwNzoyMjo1OC45ODQ3OTAxNzZaIn0="
        },
        {
            "id": 2,
            "cloudwatchTraceId": "af94d3b8-0b18-1dbf-2c7d-513f5cb9e2e1",
            "clientId": "Test",
            "sourceIp": "10.0.0.0",
            "base64OriginalPayload": "eyJ1c2VyX2lkIjogInVzZXI1NjQ3IiwgInN0ZXBzX3RvZGF5IjogMTMzNjUsICJ0aW1lc3RhbXAiOiAiMjAyNS0xMC0wOVQwNzoyMjo1OC45ODQ3OTAxNzZaIn0="
        },
        {
            "id": 3,
            "cloudwatchTraceId": "ca441266-c2ce-c916-6aee-b9e5c7831675",
            "clientId": "Test",
            "sourceIp": "10.0.0.0",
            "base64OriginalPayload": "eyJ1c2VyX2lkIjogInVzZXI1NjQ3IiwgInN0ZXBzX3RvZGF5IjogMTMzNjUsICJ0aW1lc3RhbXAiOiAiMjAyNS0xMC0wOVQwNzoyMjo1OC45ODQ3OTAxNzZaIn0="
        }
    ],
    "failures": [
        {
            "affectedIds": [
                1,
                2,
                3
            ],
            "failedAction": "HttpAction",
            "failedResource": "https://example.foobar.com/HttpAction",
            "errorMessage": "HttpAction failed to make a request to the specified endpoint. StatusCode: 500. Reason: Internal Server Error."
        },
        {
            "affectedIds": [
                3
            ],
            "failedAction": "S3Action",
            "failedResource": "amzn-s3-demo-bucket",
            "errorMessage": "Failed to put S3 object. The error received was The specified bucket does not exist"
        },
        {
            "affectedIds": [
                3
            ],
            "failedAction": "LambdaAction",
            "failedResource": "arn:aws:lambda:us-west-2:123456789012:function:dummy",
            "errorMessage": "Failed to invoke lambda function. Received Server error from Lambda. The error code is 403"
        }
    ]
}
```

###### Note

Batched action failures also generate larger error action payloads which can increase the probability of error action failures due to size. You can monitor error action failures using the `ErrorActionFailure` metric. See [Rule action metrics](metrics_dimensions.md#rule-action-metrics "metrics_dimensions.md#rule-action-metrics") for more information.

## Batching HTTP action messages with the AWS CLI

### Creating or updating a rule action with batching

1. Use the appropriate AWS CLI command to create or update a rule:
   - To create a new rule, use the [create-topic-rule](../../../cli/latest/reference/iot/create-topic-rule.md "../../../cli/latest/reference/iot/create-topic-rule.md") command:

   ```
   `aws iot create-topic-rule --rule-name `myrule` --topic-rule-payload file://`myrule`.json`
   ```

   - To update an existing rule, use the [replace-topic-rule](../../../cli/latest/reference/iot/replace-topic-rule.md "../../../cli/latest/reference/iot/replace-topic-rule.md") command:

   ```
   `aws iot replace-topic-rule --rule-name `myrule` --topic-rule-payload file://`myrule`.json`
   ```

2. Enable batching capabilities by setting the enableBatching parameter to true in your topic rule payload:

```
{
        "topicRulePayload": {
        "sql": "SELECT * FROM 'some/topic'",
        "ruleDisabled": false,
        "awsIotSqlVersion": "2016-03-23",
        "actions": [
            {
                "http": {
                    "url": "https://www.example.com/subpath",
                    "confirmationUrl": "https://www.example.com",
                    "headers": [
                        {
                            "key": "static_header_key",
                            "value": "static_header_value"
                        },
                        {
                            "key": "substitutable_header_key",
                            "value": "${value_from_payload}"
                         }
                    ],
                    "enableBatching": true,
                    "batchConfig": {
                       "maxBatchOpenMs": `100`,
                       "maxBatchSize": `5`,
                       "maxBatchSizeBytes": `1024`
                    }
                }
            }
      ]
}
```

3. Configure the batching parameters. You do not need to specify all batch parameters.
   You can choose to specify 1, 2, or all 3 batch parameters. If you do not specify a batch
   parameter, Rules Engine will update that parameter with the default values. For more
   information on batching parameters and their default values, see [HTTP parameters](https-rule-action.md#https-rule-action-parameters "https-rule-action.md#https-rule-action-parameters").
