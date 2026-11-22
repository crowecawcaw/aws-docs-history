

# Start dataset generation

 `StartDatasetGeneration` reads your agent’s traces, writes scenarios, and merges them into the dataset’s Draft. The operation is asynchronous and returns HTTP 202 with a `generationId`.

The target dataset must be `ACTIVE`, and its Draft example count plus `maxScenarios` must be 1,000 or less. You can run one generation for each dataset at a time. While a generation runs, changes to that dataset’s Draft and `CreateDatasetVersion` return `ConflictException`. For the quotas that apply to dataset generation, see [AgentCore Dataset Generation Service Quotas](bedrock-agentcore-limits.md#dataset-generation-service-limits).

## Code samples
<a name="dataset-generation-start-examples"></a>

The following example starts a `DYNAMIC` generation from CloudWatch Logs and selects multi-turn sessions with a `turnCount` filter.

**Example**  

1. 

   ```bash
   agentcore eval dataset-generation start \
     --dataset-id my-dataset-id \
     --name weeknight-sessions \
     --scenario-type dynamic \
     --generation-config '{"sourceConfig": {"cloudWatchLogs": {"logGroupNames": ["/aws/bedrock-agentcore/runtimes/my-agent-DEFAULT"], "serviceNames": ["my-agent.DEFAULT"]}}, "selection": {"filters": {"turnCount": {"min": 2, "max": 100}}}, "sampling": {"maxScenarios": 100}}'
   ```

   The `--generation-config` value is the `traceGeneration` source as JSON. You can also pass `file://<path>` to read it from a file, or `-` to read it from standard input. The CLI rejects keys that the source doesn’t have. `--scenario-type` takes `fixed` or `dynamic`; when you omit it, the service uses `DYNAMIC`.

1. 

   ```python
   import boto3
   
   client = boto3.client('bedrock-agentcore')
   
   response = client.start_dataset_generation(
       datasetId='my-dataset-id',
       name='weeknight-sessions',
       scenarioType='DYNAMIC',
       source={
           'traceGeneration': {
               'sourceConfig': {
                   'cloudWatchLogs': {
                       'logGroupNames': ['/aws/bedrock-agentcore/runtimes/my-agent-DEFAULT'],
                       'serviceNames': ['my-agent.DEFAULT']
                   }
               },
               'selection': {
                   'filters': {
                       'turnCount': {'min': 2, 'max': 100}
                   }
               },
               'sampling': {'maxScenarios': 100}
           }
       }
   )
   print(response['generationId'])
   ```

1. 

   ```bash
   aws bedrock-agentcore start-dataset-generation \
       --dataset-id my-dataset-id \
       --name weeknight-sessions \
       --scenario-type DYNAMIC \
       --source '{"traceGeneration": {"sourceConfig": {"cloudWatchLogs": {"logGroupNames": ["/aws/bedrock-agentcore/runtimes/my-agent-DEFAULT"], "serviceNames": ["my-agent.DEFAULT"]}}, "selection": {"filters": {"turnCount": {"min": 2, "max": 100}}}, "sampling": {"maxScenarios": 100}}}'
   ```

For more examples, see [Select sessions](dataset-generation-select.md) and [Redact sensitive data](dataset-generation-redaction.md).

## Request parameters
<a name="dataset-generation-start-params"></a>

The following table lists the request parameters.


| Parameter | Required | Description | 
| --- | --- | --- | 
|  `datasetId`  | Yes | The target dataset. It must already exist and be `ACTIVE`. | 
|  `name`  | Yes | A name for the generation, matching `^[a-zA-Z][a-zA-Z0-9_-]{0,47}$`. It becomes the prefix of the `generationId`. | 
|  `description`  | No | A description of up to 200 characters. | 
|  `scenarioType`  | No |  `FIXED` or `DYNAMIC`. The default is `DYNAMIC`. | 
|  `source`  | Yes | The trace source to read. The only variant is `traceGeneration`. | 
|  `clientToken`  | No | An idempotency token. The AWS SDKs set it for you. Retrying with the same token and the same parameters returns the same generation. Reusing a token with different parameters returns `ConflictException`. | 

## Trace source
<a name="dataset-generation-source"></a>

The `traceGeneration` source has the following members.


| Member | Required | Description | 
| --- | --- | --- | 
|  `sourceConfig`  | Yes | Where to read traces from. Set exactly one of `cloudWatchLogs`, `onlineEvaluation`, or `batchEvaluation`. | 
|  `selection`  | No | Which sessions to use. See [Select sessions](dataset-generation-select.md). | 
|  `sampling`  | No |  `maxScenarios`, from 1 to 1,000. The default is 100. Sampling is applied after selection. | 
|  `redactionConfiguration`  | No | Masks sensitive data before writing. When absent, no redaction is applied. See [Redact sensitive data](dataset-generation-redaction.md). | 
|  `groundTruth`  | No | Copies reference fields from the observed session. `FIXED` only. See [Ground truth](#dataset-generation-start-ground-truth). | 

Set exactly one of the following sources in `sourceConfig`.

### cloudWatchLogs
<a name="dataset-generation-source-cwl"></a>

Reads sessions directly from CloudWatch Logs.


| Field | Required | Description | 
| --- | --- | --- | 
|  `logGroupNames`  | Conditional | 1 to 5 log group names. Set this or `logGroupNamePrefixes`, not both. | 
|  `logGroupNamePrefixes`  | Conditional | 1 to 5 log group name prefixes. Set this or `logGroupNames`, not both. | 
|  `serviceNames`  | Yes | Exactly one service name, which matches the agent’s `service.name` resource attribute. On AgentCore Runtime, this is `<runtime-name>.<endpoint-name>`, for example `my-agent.DEFAULT`. | 
|  `startTime`  | No | ISO 8601 timestamp. Default: 7 days before `endTime`. | 
|  `endTime`  | No | ISO 8601 timestamp. Default: the request time. | 

### onlineEvaluation
<a name="dataset-generation-source-online"></a>

Reads sessions from an online evaluation configuration. The configuration must read CloudWatch Logs and run at least one evaluator.


| Field | Required | Description | 
| --- | --- | --- | 
|  `onlineEvaluationConfigArn`  | Yes | ARN of the online evaluation configuration. | 
|  `startTime`  | No | ISO 8601 timestamp. Default: 7 days before `endTime`. | 
|  `endTime`  | No | ISO 8601 timestamp. Default: the request time. | 

### batchEvaluation
<a name="dataset-generation-source-batch"></a>

Reads the sessions of a batch evaluation. The batch evaluation must be `COMPLETED` or `COMPLETED_WITH_ERRORS` and must read CloudWatch Logs. This source has no time window.


| Field | Required | Description | 
| --- | --- | --- | 
|  `batchEvaluationArn`  | Yes | ARN of the batch evaluation. | 

**Note**  
For `cloudWatchLogs` and `onlineEvaluation`, `startTime` must be before `endTime` and not later than the request time. A time window that ends before the log group’s retention period is rejected.

### Ground truth
<a name="dataset-generation-start-ground-truth"></a>

For a `FIXED` generation, set `groundTruth` to copy reference fields into each scenario. The service copies the values from the observed session and doesn’t generate them. Ground truth applies only to `FIXED` generations.


| Field | Required | Description | 
| --- | --- | --- | 
|  `fields`  | Yes | One or both of `expected_response` (copied into each turn) and `expected_trajectory` (the tools the session called). | 
|  `qualityFilters`  | No | Evaluator filters with the same fields as [evaluator filter fields](dataset-generation-select.md#dataset-generation-select-evaluator). Only sessions that also match these filters get reference fields; other selected sessions are still written, without them. If you don’t set `qualityFilters`, the service uses `selection.filters.evaluatorFilters`. An empty list applies no extra filter. Not supported for a `cloudWatchLogs` source. | 

The following `traceGeneration` source (the `--generation-config` value in the AgentCore CLI) copies both fields for the sessions in which every trace scored at least 0.8 on helpfulness. Use it with `scenarioType` set to `FIXED`:

```json
{
  "sourceConfig": {"onlineEvaluation": {"onlineEvaluationConfigArn": "ONLINE_EVALUATION_CONFIG_ARN"}},
  "groundTruth": {
    "fields": ["expected_response", "expected_trajectory"],
    "qualityFilters": [
      {"evaluatorId": "Builtin.Helpfulness", "operator": "GreaterThanOrEqual", "value": {"doubleValue": 0.8}, "aggregation": "Min"}
    ]
  }
}
```

The `examplesWithGroundTruth` count in the [generation results](dataset-generation-get.md#dataset-generation-get-results) reports how many examples received reference fields.

## Response
<a name="dataset-generation-start-response"></a>


| Field | Type | Description | 
| --- | --- | --- | 
|  `generationId`  | String | Unique identifier for the generation, in the form `{name}-{suffix}`, where the suffix is 10 characters. Use it to get the generation. For more information, see [Get dataset generation](dataset-generation-get.md). | 
|  `name`  | String | The name you specified. | 
|  `datasetId`  | String | The target dataset. | 
|  `status`  | String | Initial status: `IN_PROGRESS`. | 
|  `createdAt`  | Timestamp | When the generation was created. | 