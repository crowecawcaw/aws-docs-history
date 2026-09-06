# Trails

Query the audit trail of changes made to workspace resources. Trails use an async query
pattern, submit a query, then poll for results.

###### Contents

- [StartTrailQuery](#acxd-trails-starttrailquery "#acxd-trails-starttrailquery")
- [GetTrailQueryResults](#acxd-trails-gettrailqueryresults "#acxd-trails-gettrailqueryresults")
- [Request Parameters](#acxd-trails-request-parameters "#acxd-trails-request-parameters")
- [Response Fields](#acxd-trails-response-fields "#acxd-trails-response-fields")
- [Event Names](#acxd-trails-event-names "#acxd-trails-event-names")

## StartTrailQuery

Submits an audit trail query. Returns a result ID for polling.

### Input

| Parameter         | Type    | Required |
| ----------------- | ------- | -------- |
| `startTimestamp`  | string  | Yes      |
| `endTimestamp`    | string  | Yes      |
| `eventType`       | string  | No       |
| `eventName`       | string  | No       |
| `principalId`     | string  | No       |
| `principalEmail`  | string  | No       |
| `sourceIpAddress` | string  | No       |
| `page`            | integer | No       |
| `size`            | integer | No       |

### Sample Request

```
await client.send(new StartTrailQueryCommand({
  startTimestamp: "2026-08-03T00:00:00.000Z",
  endTimestamp: "2026-08-10T23:59:59.000Z",
}));
```

### StartTrailQuery with Filters

```
await client.send(new StartTrailQueryCommand({
  startTimestamp: "2026-08-10T00:00:00.000Z",
  endTimestamp: "2026-08-10T23:59:59.000Z",
  eventType: "WRITE",
  size: 5,
}));
```

### Output

```
{
  "resultId": "qry-a1b2c3d4e5f6..."
}
```

### Errors

- `ValidationException` (400)
- `InternalServerException` (500)
- `ThrottlingException` (429)

## GetTrailQueryResults

Gets results of a previously submitted trail query.

### Input

| Parameter  | Type   | Required |
| ---------- | ------ | -------- |
| `resultId` | string | Yes      |

### Sample Request

```
await client.send(new GetTrailQueryResultsCommand({
  resultId: "7eba7313-ad4d-48d9-acba-dbf2a0d492cc",
}));
```

### Output

```
{
  "status": "SUCCEEDED",
  "items": [
    {
      "eventVersion": "1.0",
      "eventTime": "2026-08-10T18:07:08.008Z",
      "eventSource": "acxd.studio",
      "eventName": "FlowUpdate",
      "eventType": "WRITE",
      "userAgent": "ACXD-SDK/1.0",
      "requestId": "req-uuid",
      "requestParameters": "{\"flowId\":\"MainFlow\",\"customerId\":\"a018836f-...\"}",
      "responseElements": "{\"statusCode\":\"200\",\"message\":\"Flow updated successfully.\"}",
      "userType": "ACXDStudioUser",
      "userId": "user-uuid",
      "tier": ""
    }
  ]
}
```

### Errors

- `ValidationException` (400)
- `ResourceNotFoundException` (404)
- `InternalServerException` (500)
- `ThrottlingException` (429)

## Request Parameters

`resultId`

Type: String

The result ID returned by StartTrailQuery. Used to poll for results.

`startTimestamp`

Type: String

Start of time range (ISO 8601).

`endTimestamp`

Type: String

End of time range (ISO 8601).

`eventType`

Type: String

Filter by event type. One of: `WRITE`, `DELETE`.

`eventName`

Type: String

Filter by specific event name. See Event Names.

`principalId`

Type: String

Filter by the user who made the change. Alphanumeric, 24–30 characters.

`principalEmail`

Type: String

Filter by user email.

`sourceIpAddress`

Type: String

Filter by source IP address.

`page`

Type: Integer

Page number (0–100).

`size`

Type: Integer

Page size (1–100).

## Response Fields

`status`

Type: String

Query status. One of: `IN_PROGRESS` (poll again), `SUCCEEDED`
(results ready), `FAILED`, `CANCELLED`.

`items`

Type: Array

List of trail events. Each event contains:

`eventVersion`

Type: String

Event schema version.

`eventTime`

Type: String

When the event occurred (ISO 8601).

`eventSource`

Type: String

The source system (e.g., `acxd.studio`).

`eventName`

Type: String

The action that occurred. See Event Names.

`eventType`

Type: String

`WRITE` or `DELETE`.

`sourceIpAddress`

Type: String

The IP address of the caller.

`userAgent`

Type: String

The user agent string of the caller.

`requestId`

Type: String

Unique request identifier.

`requestParameters`

Type: String

The request parameters (JSON string).

`responseElements`

Type: String

The response elements (JSON string).

`errorCode`

Type: String

Error code if the action failed.

`errorMessage`

Type: String

Error message if the action failed.

`userType`

Type: String

Type of user who performed the action.

`userId`

Type: String

User identifier.

`email`

Type: String

User email.

`userName`

Type: String

User display name.

`tier`

Type: String

Account tier.

## Event Names

| Category           | Events                                                                                                                                                                                                                                                                             |
| ------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Applications       | `ApplicationCreate`, `ApplicationUpdate`,<br>`ApplicationDelete`, `ApplicationBatchUpdate`                                                                                                                                                                                         |
| Builds             | `BuildCreate`, `BuildUpdate`                                                                                                                                                                                                                                                       |
| Deployments        | `DeploymentCreate`, `DeploymentUpdate`,<br>`DeploymentDelete`                                                                                                                                                                                                                      |
| Conversation Flows | `ConversationFlowCreate`, `ConversationFlowUpdate`,<br>`ConversationFlowDelete`, `ConversationFlowCloneCreate`,<br>`ConversationFlowBatchUpdate`                                                                                                                                   |
| Data Requests      | `DataRequestCreate`, `DataRequestUpdate`,<br>`DataRequestDelete`, `DataRequestBatchUpdate`                                                                                                                                                                                         |
| Guardrail          | `GuardrailCreate`, `GuardrailUpdate`,<br>`GuardrailDelete`, `GuardrailBatchUpdate`                                                                                                                                                                                                 |
| Knowledge Bases    | `KnowledgeBaseCreate`, `KnowledgeBaseUpdate`,<br>`KnowledgeBaseDelete`, `KnowledgeBaseCloneCreate`,<br>`KnowledgeBaseBatchUpdate`, `KnowledgeBasePublish`                                                                                                                          |
| KB Articles        | `KnowledgeBaseArticleCreate`, `KnowledgeBaseArticleUpdate`,<br>`KnowledgeBaseArticleDelete`                                                                                                                                                                                        |
| KB Documents       | `KnowledgeBaseDocumentUpload`,<br>`KnowledgeBaseDocumentDelete`                                                                                                                                                                                                                    |
| Secrets            | `SecretCreate`, `SecretUpdate`,<br>`SecretDelete`, `SecretBatchUpdate`                                                                                                                                                                                                             |
| Slot Types         | `SlotCreate`, `SlotUpdate`,<br>`SlotDelete`, `SlotBatchUpdate`                                                                                                                                                                                                                     |
| Modalities         | `ModalityCreate`, `ModalityUpdate`,<br>`ModalityDelete`, `ModalityBatchUpdate`                                                                                                                                                                                                     |
| Integrations       | `IntegrationCreate`, `IntegrationUpdate`,<br>`IntegrationDelete`                                                                                                                                                                                                                   |
| Analytics Tags     | `AnalyticsTagsCreate`, `AnalyticsTagsUpdate`,<br>`AnalyticsTagsDelete`, `AnalyticsTagsBatchUpdate`                                                                                                                                                                                 |
| Context Variables  | `ContextVariablesCreate`, `ContextVariablesUpdate`,<br>`ContextVariablesDelete`                                                                                                                                                                                                    |
| Translations       | `TranslateContent`, `RequestTranslation`,<br>`RequestTranslationExport`, `SupportedLanguagesUpdate`,<br>`UpdateResourceSupportedLanguages`                                                                                                                                         |
| Downloads          | `DownloadConversations`, `RequestDownload`,<br>`DownloadFile`                                                                                                                                                                                                                      |
| Dashboards         | `DashboardCreate`, `DashboardUpdate`,<br>`DashboardDelete`                                                                                                                                                                                                                         |
| Monitors           | `AnalyticsMonitorCreate`, `AnalyticsSubscriptionCreate`,<br>`ClustersMonitorCreate`, `MonitorUpdate`,<br>`SubscriptionDelete`                                                                                                                                                      |
| Notifications      | `NotificationAlertUpdate`,<br>`NotificationAlertDelete`                                                                                                                                                                                                                            |
| History Tabs       | `HistoryTabCreate`, `HistoryTabUpdate`,<br>`HistoryTabDelete`                                                                                                                                                                                                                      |
| Tests              | `TestCreate`, `TestUpdate`,<br>`TestDelete`, `TestExecutionCreate`                                                                                                                                                                                                                 |
| LiveSyncScripts    | `LiveSyncScriptCreate`, `LiveSyncScriptUpdate`,<br>`LiveSyncScriptBatchUpdate`, `LiveSyncScriptDelete`,<br>`LiveSyncScriptBuildCreate`, `LiveSyncScriptBuildDelete`,<br>`LiveSyncScriptDeploymentCreate`,<br>`LiveSyncScriptDeploymentUpdate`,<br>`LiveSyncScriptDeploymentDelete` |
| Lifecycle Hooks    | `LifecycleHookCreate`, `LifecycleHookUpdate`,<br>`LifecycleHookDelete`                                                                                                                                                                                                             |
| Other              | `ApplyUpload`, `BatchDelete`,<br>`DeleteUpload`, `UnknownMessagesUpdate`,<br>`ResourceFoldersUpdate`, `ResourceTagsUpdate`,<br>`TimezoneUpdate`                                                                                                                                    |
