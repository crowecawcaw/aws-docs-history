

# Select sessions for dataset generation

Use `selection` to choose which sessions become scenarios. Set exactly one of `filters` or `identifiers`. When `selection` is absent, every session in the source and window that has at most 100 turns is a candidate.

## Select by filters
<a name="dataset-generation-select-filters"></a>

Set `filters` to have the service find matching sessions. The service AND-combines the members you set. A member that you don’t set doesn’t narrow the selection.


| Member | Description | 
| --- | --- | 
|  `attributeFilters`  | Up to 5 conditions on span attributes, AND-combined. A session matches when any span in it matches. | 
|  `turnCount`  |  `{"min": …​, "max": …​}`, each from 1 to 100. `max` defaults to 100. Set `max` to 1 for single-turn sessions only, or `min` to 2 for multi-turn sessions only. | 
|  `evaluatorFilters`  | Up to 10 conditions on evaluator results. Use these only with an `onlineEvaluation` or `batchEvaluation` source. Sessions without a result for the evaluator are left out and counted in `sessionsUnscored`. | 

Sessions with more than 100 turns are never selected.

### Attribute filter fields
<a name="dataset-generation-select-attribute"></a>


| Field | Required | Description | 
| --- | --- | --- | 
|  `key`  | Yes | The span field to match, 1 to 256 characters matching `^[a-zA-Z0-9._-]+$`. Start the key with `attributes.` for a span attribute or `resource.attributes.` for a resource attribute, for example `attributes.session.id`. A key without one of these prefixes is rejected with `ValidationException`. | 
|  `operator`  | Yes | One of `Equals`, `NotEquals`, `GreaterThan`, `LessThan`, `GreaterThanOrEqual`, `LessThanOrEqual`, `Contains`, `NotContains`. | 
|  `value`  | Yes | Exactly one of `stringValue` (up to 1,024 characters), `doubleValue`, or `booleanValue`. | 

You can’t combine `Contains` or `NotContains` with an ordering operator (`GreaterThan`, `LessThan`, `GreaterThanOrEqual`, or `LessThanOrEqual`) on the same key.

### Evaluator filter fields
<a name="dataset-generation-select-evaluator"></a>


| Field | Required | Description | 
| --- | --- | --- | 
|  `evaluatorId`  | Yes | The evaluator whose results to compare, for example `Builtin.Helpfulness`. | 
|  `operator`  | Yes | Same operators as attribute filters. | 
|  `value`  | Yes |  `doubleValue` for a score, or `stringValue` for a label. | 
|  `aggregation`  | Conditional | How to combine per-trace or per-span results into one session result. Required for a trace-scoped or span-scoped evaluator, and not allowed for a session-scoped evaluator. There is no default. For scores: `Min`, `Max`, or `Mean`. For labels: `AllMatch` or `AnyMatch`. | 
|  `evaluationDimensionName`  | Conditional | Required for a multi-dimension evaluator, and not allowed otherwise. | 

**Tip**  
Choose `aggregation` based on what you want to collect:  
 **Good sessions (every turn good)** - For a score, use `Min` with `GreaterThanOrEqual` and a high threshold, so every trace in the session meets it. For a label, use `AllMatch` on the passing label.
 **Sessions with at least one failure** - For a score, use `Min` with `LessThan` and a low threshold. For a label, use `AnyMatch` on the failing label.

### Example: Select sessions by evaluator score
<a name="dataset-generation-select-evaluator-example"></a>

The following example reads sessions from an online evaluation configuration and keeps only the sessions in which every trace scored at least 0.8 on helpfulness. Replace the online evaluation configuration ARN with your own.

**Example**  

1. 

   ```bash
   agentcore eval dataset-generation start \
     --dataset-id my-dataset-id \
     --name high-quality-sessions \
     --scenario-type dynamic \
     --generation-config '{"sourceConfig": {"onlineEvaluation": {"onlineEvaluationConfigArn": "ONLINE_EVALUATION_CONFIG_ARN"}}, "selection": {"filters": {"evaluatorFilters": [{"evaluatorId": "Builtin.Helpfulness", "operator": "GreaterThanOrEqual", "value": {"doubleValue": 0.8}, "aggregation": "Min"}]}}}'
   ```

1. 

   ```python
   import boto3
   
   client = boto3.client('bedrock-agentcore')
   
   response = client.start_dataset_generation(
       datasetId='my-dataset-id',
       name='high-quality-sessions',
       scenarioType='DYNAMIC',
       source={
           'traceGeneration': {
               'sourceConfig': {
                   'onlineEvaluation': {
                       'onlineEvaluationConfigArn': 'ONLINE_EVALUATION_CONFIG_ARN'
                   }
               },
               'selection': {
                   'filters': {
                       'evaluatorFilters': [
                           {
                               'evaluatorId': 'Builtin.Helpfulness',
                               'operator': 'GreaterThanOrEqual',
                               'value': {'doubleValue': 0.8},
                               'aggregation': 'Min'
                           }
                       ]
                   }
               }
           }
       }
   )
   print(response['generationId'])
   ```

1. 

   ```bash
   aws bedrock-agentcore start-dataset-generation \
       --dataset-id my-dataset-id \
       --name high-quality-sessions \
       --scenario-type DYNAMIC \
       --source '{"traceGeneration": {"sourceConfig": {"onlineEvaluation": {"onlineEvaluationConfigArn": "ONLINE_EVALUATION_CONFIG_ARN"}}, "selection": {"filters": {"evaluatorFilters": [{"evaluatorId": "Builtin.Helpfulness", "operator": "GreaterThanOrEqual", "value": {"doubleValue": 0.8}, "aggregation": "Min"}]}}}}'
   ```

## Select by ID
<a name="dataset-generation-select-identifiers"></a>

Set `identifiers` to choose sessions and traces yourself. Filters don’t apply to them.


| Field | Description | 
| --- | --- | 
|  `sessionIds`  | Up to 25 session IDs. Each session becomes one scenario. A listed session with more than 100 turns is reported as an error and produces no example. | 
|  `traceIds`  | Up to 25 trace IDs. Each trace becomes a single-trace scenario. | 

Set `sessionIds`, `traceIds`, or both. At least one must be non-empty.

### Example: Select sessions and traces by ID
<a name="dataset-generation-select-example"></a>

The following example selects sessions and traces by ID instead of by filter.

**Example**  

1. 

   ```bash
   agentcore eval dataset-generation start \
     --dataset-id my-dataset-id \
     --name specific-sessions \
     --scenario-type dynamic \
     --generation-config '{"sourceConfig": {"cloudWatchLogs": {"logGroupNames": ["/aws/bedrock-agentcore/runtimes/my-agent-DEFAULT"], "serviceNames": ["my-agent.DEFAULT"]}}, "selection": {"identifiers": {"sessionIds": ["session-abc", "session-def"], "traceIds": ["0123456789abcdef0123456789abcdef"]}}}'
   ```

1. 

   ```python
   import boto3
   
   client = boto3.client('bedrock-agentcore')
   
   response = client.start_dataset_generation(
       datasetId='my-dataset-id',
       name='specific-sessions',
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
                   'identifiers': {
                       'sessionIds': ['session-abc', 'session-def'],
                       'traceIds': ['0123456789abcdef0123456789abcdef']
                   }
               }
           }
       }
   )
   print(response['generationId'])
   ```

1. 

   ```bash
   aws bedrock-agentcore start-dataset-generation \
       --dataset-id my-dataset-id \
       --name specific-sessions \
       --scenario-type DYNAMIC \
       --source '{"traceGeneration": {"sourceConfig": {"cloudWatchLogs": {"logGroupNames": ["/aws/bedrock-agentcore/runtimes/my-agent-DEFAULT"], "serviceNames": ["my-agent.DEFAULT"]}}, "selection": {"identifiers": {"sessionIds": ["session-abc", "session-def"], "traceIds": ["0123456789abcdef0123456789abcdef"]}}}}'
   ```