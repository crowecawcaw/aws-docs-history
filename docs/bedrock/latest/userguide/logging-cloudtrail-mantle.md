# Monitor `bedrock-mantle` API calls using CloudTrail

The `bedrock-mantle.`region`.api.aws` endpoint integrates
with AWS CloudTrail. CloudTrail records calls to the `bedrock-mantle` API operations as events,
including calls from the AWS Management Console, the AWS CLI, the OpenAI SDK, the Anthropic SDK, and direct HTTPS
calls. Events have an `eventSource` of
`bedrock-mantle.amazonaws.com`.

If your application calls inference through
`bedrock-runtime.`region`.amazonaws.com`, see [Monitor Amazon Bedrock API calls using CloudTrail](logging-using-cloudtrail.md "logging-using-cloudtrail.md") instead.

For background on CloudTrail itself, see the [AWS CloudTrail User Guide](../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md "../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md").

## Management events

Management events are logged by default to your CloudTrail **Event history** at
no additional cost. `bedrock-mantle` logs the following operations as management
events. The `requestParameters` field of each event also contains
`callWithBearerToken` (and `bearerTokenType` when applicable), which are
added by the service for every event.

| Models       | Event name               | HTTP route | Additional request parameters |
| ------------ | ------------------------ | ---------- | ----------------------------- |
| `ListModels` | `GET /v1/models`         | none       |
| `GetModel`   | `GET /v1/models/{model}` | `model`    |

| Fine-tuning           | Event name                                                    | HTTP route                                                                                                                                                       | Additional request parameters |
| --------------------- | ------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------- |
| `ListFineTuningJobs`  | `GET /v1/fine_tuning/jobs`                                    | none                                                                                                                                                             |
| `CreateFineTuningJob` | `POST /v1/fine_tuning/jobs`                                   | `model`, `trainingFile`, `validationFile`,<br>`metadata`, `method` (structured object including `type`<br>and, for reinforcement runs, `grader.lambda.function`) |
| `GetFineTuningJob`    | `GET /v1/fine_tuning/jobs/{id}`, `/events`,<br>`/checkpoints` | `fineTuningJob`                                                                                                                                                  |
| `CancelFineTuningJob` | `POST /v1/fine_tuning/jobs/{id}/cancel`                       | `fineTuningJob`                                                                                                                                                  |

| Projects         | Event name                                            | HTTP route                                                     | Additional request parameters |
| ---------------- | ----------------------------------------------------- | -------------------------------------------------------------- | ----------------------------- |
| `ListProjects`   | `GET /v1/organization/projects`                       | none                                                           |
| `CreateProject`  | `POST /v1/organization/projects`                      | `name`, `tags`                                                 |
| `GetProject`     | `GET /v1/organization/projects/{project_id}`          | `project_id`                                                   |
| `UpdateProject`  | `POST /v1/organization/projects/{project_id}`         | `project_id`, `name`, `add_tags`,<br>`remove_tag_keys`, `tags` |
| `ArchiveProject` | `POST /v1/organization/projects/{project_id}/archive` | `project_id`                                                   |

## Data events

Data events are not logged by default and incur additional CloudTrail charges.
`bedrock-mantle` logs the following operations as data events. To capture them,
configure advanced event selectors on your trail or event data store as described in [Logging data events](../../../awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.md "../../../awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.md").

| Inference         | Event name                                 | HTTP route                                                           | Additional request parameters |
| ----------------- | ------------------------------------------ | -------------------------------------------------------------------- | ----------------------------- |
| `CreateInference` | `POST /v1/responses`                       | `model`, `previousResponse`, `stream`,<br>`service_tier`, `metadata` |
| `CreateInference` | `POST /v1/responses/compact`               | `model`, `previous_response_id`                                      |
| `CreateInference` | `POST /v1/chat/completions`                | `model`, `stream`, `service_tier`,<br>`metadata`                     |
| `CreateInference` | `POST /v1/embeddings`                      | `model`                                                              |
| `CreateInference` | `POST /anthropic/v1/messages`              | `model`, `stream`, `max_tokens`                                      |
| `GetInference`    | `GET /v1/responses/{response_id}`          | `response`, `stream`                                                 |
| `CancelInference` | `POST /v1/responses/{response_id}/cancel`  | `response`                                                           |
| `DeleteInference` | `DELETE /v1/responses/{response_id}`       | `response`                                                           |
| `CountTokens`     | `POST /anthropic/v1/messages/count_tokens` | `model`                                                              |

| Files        | Event name                            | HTTP route                           | Additional request parameters |
| ------------ | ------------------------------------- | ------------------------------------ | ----------------------------- |
| `ListFiles`  | `GET /v1/files`                       | `limit`, `order`, `purpose`, `after` |
| `CreateFile` | `POST /v1/files`                      | `purpose`, `filename`, `bytes`       |
| `GetFile`    | `GET /v1/files/{file_id}`, `/content` | `file`                               |
| `DeleteFile` | `DELETE /v1/files/{file_id}`          | `file`                               |

###### Note

Customer-supplied `metadata` on `CreateInference` calls is logged
verbatim in CloudTrail. Do not include secrets, credentials, or other sensitive values in
`metadata` if you are capturing data events.

## Configuring data event capture

The following example configures a trail to capture all `bedrock-mantle`
inference and file data events:

```
aws cloudtrail put-event-selectors \
    --trail-name <trailName> \
    --advanced-event-selectors '[
      {
        "Name": "Log Bedrock Mantle inference and file events",
        "FieldSelectors": [
          { "Field": "eventCategory", "Equals": ["Data"] },
          { "Field": "resources.type", "Equals": [
            "AWS::BedrockMantle::Project",
            "AWS::BedrockMantle::CustomizedModel",
            "AWS::BedrockMantle::Reservation"
          ]}
        ]
      }
    ]'
```

You can additionally filter by `eventName` and `resources.ARN`. For
details on advanced event selectors, see [AdvancedFieldSelector](../../../awscloudtrail/latest/APIReference/API_AdvancedFieldSelector.md "../../../awscloudtrail/latest/APIReference/API_AdvancedFieldSelector.md").

## Resource types

`bedrock-mantle` CloudTrail events reference the following resource types:

- `AWS::BedrockMantle::Project`
- `AWS::BedrockMantle::Reservation`
- `AWS::BedrockMantle::CustomizedModel`
- `AWS::BedrockMantle::Environment`
- `AWS::BedrockMantle::Runtime`
- `AWS::BedrockMantle::Skill`

## Example log entry

```
{
    "eventVersion": "1.08",
    "userIdentity": {
        "type": "IAMUser",
        "principalId": "AROAICFHPEXAMPLE",
        "arn": "arn:aws:iam::111122223333:user/userxyz",
        "accountId": "111122223333",
        "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
        "userName": "userxyz"
    },
    "eventTime": "2026-05-30T14:32:11Z",
    "eventSource": "bedrock-mantle.amazonaws.com",
    "eventName": "CreateInference",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "192.0.2.0",
    "userAgent": "OpenAI/Python 1.50.0",
    "requestParameters": {
        "model": "anthropic.claude-opus-4-7",
        "stream": true,
        "service_tier": "default",
        "metadata": {"team": "platform"},
        "callWithBearerToken": true,
        "bearerTokenType": "ABSK"
    },
    "responseElements": null,
    "requestID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
    "eventID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
    "readOnly": false,
    "eventType": "AwsApiCall",
    "managementEvent": false,
    "recipientAccountId": "111122223333",
    "eventCategory": "Data",
    "resources": [
        {
            "accountId": "111122223333",
            "type": "AWS::BedrockMantle::Project",
            "ARN": "arn:aws:bedrock-mantle:us-east-1:111122223333:project/proj_abc123"
        }
    ],
    "tlsDetails": {
        "tlsVersion": "TLSv1.3",
        "cipherSuite": "TLS_AES_128_GCM_SHA256",
        "clientProvidedHostHeader": "bedrock-mantle.us-east-1.api.aws"
    }
}
```

## Differences from `bedrock-runtime` CloudTrail logging

- **Inference is a data event on `bedrock-mantle`, a
  management event on `bedrock-runtime`.** The `bedrock-runtime`
  endpoint logs [Converse](../APIReference/API_runtime_Converse.md "../APIReference/API_runtime_Converse.md"), [ConverseStream](../APIReference/API_runtime_ConverseStream.md "../APIReference/API_runtime_ConverseStream.md"), [InvokeModel](../APIReference/API_runtime_InvokeModel.md "../APIReference/API_runtime_InvokeModel.md"), and [InvokeModelWithResponseStream](../APIReference/API_runtime_InvokeModelWithResponseStream.md "../APIReference/API_runtime_InvokeModelWithResponseStream.md") as management
  events at no additional cost. The `bedrock-mantle` endpoint logs
  `CreateInference` and the other inference operations as data events, which incur
  CloudTrail data event charges. If you require an audit trail of inference calls on
  `bedrock-mantle`, you must explicitly enable data event capture on your trail or
  event data store.
- **Different event source and resource types.**
  `bedrock-mantle` events use an `eventSource` of
  `bedrock-mantle.amazonaws.com` and reference `AWS::BedrockMantle::*`
  resource types. CloudTrail Lake queries, Athena views, and detective controls that filter on
  `bedrock.amazonaws.com` or `bedrock-runtime.amazonaws.com` will not
  capture `bedrock-mantle` activity.
