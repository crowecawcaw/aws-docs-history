

# Get dataset generation

Call `GetDatasetGeneration` to check the status and results of a generation. Poll it until the status is terminal. `GetDataset` doesn’t report on generations.

A generation moves through these status values:
+  `IN_PROGRESS` - The generation is running.
+  `COMPLETED` - Every selected session was processed and the examples were written to the Draft.
+  `COMPLETED_WITH_ERRORS` - Some sessions failed; the rest were written to the Draft.
+  `FAILED` - The generation failed. `failureReason` describes why.
+  `DELETING` - The generation record is being deleted.

## Code samples
<a name="dataset-generation-get-examples"></a>

The following example polls a generation until it finishes, then prints the result counts.

**Example**  

1. 

   ```bash
   agentcore eval dataset-generation get \
     --dataset-id my-dataset-id \
     --id weeknight-sessions-abcd123456
   ```

   Run the command until `status` is `COMPLETED`, `COMPLETED_WITH_ERRORS`, or `FAILED`.

1. 

   ```python
   import boto3
   import time
   
   client = boto3.client('bedrock-agentcore')
   
   while True:
       gen = client.get_dataset_generation(
           datasetId='my-dataset-id',
           generationId='weeknight-sessions-abcd123456'
       )
       status = gen['status']
       if status in ('COMPLETED', 'COMPLETED_WITH_ERRORS', 'FAILED'):
           break
       time.sleep(10)
   
   results = gen['generationResults']
   print(f"Examples written to the Draft: {results['examplesWritten']}")
   for error in gen.get('errorDetails', []):
       print(f"{error['errorCode']}: {error['count']} sessions")
   ```

1. 

   ```bash
   aws bedrock-agentcore get-dataset-generation \
       --dataset-id my-dataset-id \
       --generation-id weeknight-sessions-abcd123456
   ```

## Response
<a name="dataset-generation-get-response"></a>


| Field | Type | Description | 
| --- | --- | --- | 
|  `generationId`  | String | Unique identifier for the generation. | 
|  `name`  | String | The name you specified. | 
|  `description`  | String | The description you specified, if any. | 
|  `datasetId`  | String | The target dataset. | 
|  `scenarioType`  | String |  `FIXED` or `DYNAMIC`. If you didn’t specify one, this is `DYNAMIC`. | 
|  `status`  | String | One of `IN_PROGRESS`, `COMPLETED`, `COMPLETED_WITH_ERRORS`, `FAILED`, `DELETING`. | 
|  `failureReason`  | String | Why the generation failed. Present only when `status` is `FAILED`. | 
|  `createdAt`  | Timestamp | When the generation was created. | 
|  `updatedAt`  | Timestamp | When the status last changed. | 
|  `completedAt`  | Timestamp | When the generation finished. Present only in a terminal status. | 
|  `source`  | Object | The request’s `traceGeneration` source, with the resolved time window and resolved `turnCount.max`. | 
|  `generationResults`  | Object | Counts for the run. See [Generation results](#dataset-generation-get-results). | 
|  `errorDetails`  | List | Errors grouped by error code. See [Error details](#dataset-generation-get-errors). | 
|  `redactionSummary`  | Object |  `scenariosScanned` and `findingCounts` (findings for each identifier). Present only when you configured redaction. | 

### Generation results
<a name="dataset-generation-get-results"></a>


| Field | Description | 
| --- | --- | 
|  `sessionsMatched`  | Sessions that matched the filters or were listed, before sampling, including sessions that failed. | 
|  `sessionsSelected`  | Sessions remaining after sampling. | 
|  `sessionsUnscored`  | Sessions left out because they had no result for an evaluator filter. | 
|  `sessionsFailed`  | Sessions that failed. `errorDetails` lists the reasons. | 
|  `scenariosGenerated`  | Scenarios the service wrote. | 
|  `scenariosDeduplicated`  | Scenarios removed as duplicates, within the run or of examples already in the Draft. | 
|  `examplesWritten`  | Examples added to the Draft. | 
|  `examplesWithGroundTruth`  | Of `examplesWritten`, the examples that received reference fields. For more information, see [Ground truth](dataset-generation-start.md#dataset-generation-start-ground-truth). | 

### Error details
<a name="dataset-generation-get-errors"></a>

 `errorDetails` has up to 10 entries, one for each error code, most frequent first.


| Field | Description | 
| --- | --- | 
|  `errorCode`  | The error code, for example `SPANS_INCOMPLETE`, `EXTRACTION_FAILED`, `ACCESS_DENIED`, or `EXPIRED_CREDENTIALS`. New codes can appear. | 
|  `errorMessage`  | A description of the error. | 
|  `count`  | How many sessions or traces failed with this code. | 
|  `sessionIds`  | Up to 10 of the affected session IDs, or trace IDs for listed traces. | 