

# Manage dataset examples
<a name="datasets-examples"></a>

After a dataset reaches `ACTIVE` status, you can add, update, delete, and list examples in the Draft. All example mutations are asynchronous (HTTP 202) and use all-or-nothing semantics — if any example ID is not found, the entire batch fails with `ResourceNotFoundException`.

Maximum 1,000 examples per request. Inline content limit: 5 MB.

In the AgentCore CLI, `agentcore eval dataset update` adds, updates, and deletes examples in one step. It makes the DRAFT match a local JSONL file by `exampleId`. A line without an `exampleId` is added as a new example. A line whose `exampleId` matches a DRAFT example updates that example if its content changed. Any DRAFT example whose `exampleId` is not in the file is deleted. Start from a file downloaded with `agentcore eval dataset get --id <DATASET_ID> --file-path <FILE>`, which includes the `exampleId` of each example. Don’t reuse the file that you passed to `agentcore eval dataset create`. That file has no `exampleId` values, so `update` deletes every DRAFT example and adds them all again with new IDs.

## AddDatasetExamples
<a name="datasets-add-examples"></a>

The following examples show how to add examples to a dataset:

**Example**  

1. Download the DRAFT, append scenarios to the downloaded JSONL file, then reconcile it with the DRAFT:

   ```
   # Download the DRAFT. Each line includes its exampleId.
   agentcore eval dataset get \
     --id <DATASET_ID> \
     --file-path my_eval_dataset.jsonl
   
   # Edit my_eval_dataset.jsonl — add new lines
   agentcore eval dataset update \
     --id <DATASET_ID> \
     --file-path my_eval_dataset.jsonl
   ```

   The command adds lines that have no `exampleId` and writes their assigned `exampleId` values back to the file. Unchanged lines that keep their `exampleId` are not uploaded again.

1. 

   ```
   from bedrock_agentcore.evaluation import DatasetClient
   
   client = DatasetClient(region_name="us-west-2")
   
   ds = client.add_examples_and_wait(
       datasetId="my-dataset-id",
       source={
           "inlineExamples": {
               "examples": [
                   {
                       "scenario_id": "TC-02",
                       "turns": [{"input": "Transfer $100", "expected_response": "Transfer complete."}],
                   }
               ]
           }
       },
   )
   print(f"Example count: {ds['exampleCount']}")
   ```

1. 

   ```
   import boto3
   import time
   
   client = boto3.client('bedrock-agentcore-control')
   
   resp = client.add_dataset_examples(
       datasetId='my-dataset-id',
       source={'inlineExamples': {'examples': [
           {'scenario_id': 'TC-02', 'turns': [{'input': 'Transfer $100', 'expected_response': 'Transfer complete.'}]}
       ]}}
   )
   print(f"Added example IDs: {resp['exampleIds']}")
   
   # Poll until ACTIVE
   while True:
       ds = client.get_dataset(datasetId='my-dataset-id')
       if ds['status'] == 'ACTIVE':
           break
       time.sleep(2)
   ```

1. 

   ```
   aws bedrock-agentcore-control add-dataset-examples \
       --dataset-id my-dataset-id \
       --source '{"inlineExamples": {"examples": [{"scenario_id": "TC-02", "turns": [{"input": "Transfer $100", "expected_response": "Transfer complete."}]}]}}'
   ```

## UpdateDatasetExamples
<a name="datasets-update-examples"></a>

Each entry must include `exampleId` plus the updated content fields. The dataset must be in `ACTIVE` or `UPDATE_FAILED` status.

The following examples show how to update dataset examples:

**Example**  

1. Modify existing scenarios in a JSONL file downloaded from the DRAFT, then reconcile it with the DRAFT:

   ```
   # Edit my_eval_dataset.jsonl — modify existing lines
   agentcore eval dataset update \
     --id <DATASET_ID> \
     --file-path my_eval_dataset.jsonl
   ```

   The command diffs your local file against the service and updates changed examples. Each line must retain its `exampleId` for the service to recognize it as an update rather than a new example.

1. 

   ```
   from bedrock_agentcore.evaluation import DatasetClient
   
   client = DatasetClient(region_name="us-west-2")
   
   ds = client.update_examples_and_wait(
       datasetId="my-dataset-id",
       examples=[
           {
               "exampleId": "example-id-from-list",
               "scenario_id": "TC-02-updated",
               "turns": [{"input": "Transfer $200", "expected_response": "Transfer complete."}],
           }
       ],
   )
   ```

1. 

   ```
   import boto3
   import time
   
   client = boto3.client('bedrock-agentcore-control')
   
   client.update_dataset_examples(
       datasetId='my-dataset-id',
       examples=[
           {
               'exampleId': 'example-id-from-list',
               'scenario_id': 'TC-02-updated',
               'turns': [{'input': 'Transfer $200', 'expected_response': 'Transfer complete.'}],
           }
       ]
   )
   
   # Poll until ACTIVE
   while True:
       ds = client.get_dataset(datasetId='my-dataset-id')
       if ds['status'] == 'ACTIVE':
           break
       time.sleep(2)
   ```

1. 

   ```
   aws bedrock-agentcore-control update-dataset-examples \
       --dataset-id my-dataset-id \
       --cli-input-json file://update-examples.json
   ```

## DeleteDatasetExamples
<a name="datasets-delete-examples"></a>

The dataset must be in `ACTIVE`, `UPDATE_FAILED`, or `CREATE_FAILED` status.

The following examples show how to delete dataset examples:

**Example**  

1. Remove the corresponding lines from a JSONL file downloaded from the DRAFT, then reconcile it with the DRAFT:

   ```
   # Edit my_eval_dataset.jsonl — remove lines
   agentcore eval dataset update \
     --id <DATASET_ID> \
     --file-path my_eval_dataset.jsonl
   ```

   The command deletes each DRAFT example whose `exampleId` is not in the file.

1. 

   ```
   from bedrock_agentcore.evaluation import DatasetClient
   
   client = DatasetClient(region_name="us-west-2")
   
   ds = client.delete_examples_and_wait(
       datasetId="my-dataset-id",
       exampleIds=["example-id-1", "example-id-2"],
   )
   ```

1. 

   ```
   import boto3
   import time
   
   client = boto3.client('bedrock-agentcore-control')
   
   client.delete_dataset_examples(
       datasetId='my-dataset-id',
       exampleIds=['example-id-1', 'example-id-2']
   )
   
   # Poll until ACTIVE
   while True:
       ds = client.get_dataset(datasetId='my-dataset-id')
       if ds['status'] == 'ACTIVE':
           break
       time.sleep(2)
   ```

1. 

   ```
   aws bedrock-agentcore-control delete-dataset-examples \
       --dataset-id my-dataset-id \
       --example-ids '["example-id-1", "example-id-2"]'
   ```

## ListDatasetExamples
<a name="datasets-list-examples"></a>

Returns a paginated list of examples with full content. By default reads from the Draft. Specify `datasetVersion` to read from a published version.

The following examples show how to list dataset examples:

**Example**  

1. 

   ```
   # Download examples from the DRAFT
   agentcore eval dataset get \
     --id <DATASET_ID> \
     --file-path my_eval_dataset.jsonl
   
   # Download examples from a published version
   agentcore eval dataset get \
     --id <DATASET_ID> \
     --version 1 \
     --file-path my_eval_dataset-v1.jsonl
   ```

1. 

   ```
   from bedrock_agentcore.evaluation import DatasetClient
   
   client = DatasetClient(region_name="us-west-2")
   
   # List examples from Draft
   resp = client.list_dataset_examples(datasetId="my-dataset-id")
   for example in resp["examples"]:
       print(f"  {example['exampleId']}: {example['scenario_id']}")
   
   # List examples from a published version
   resp = client.list_dataset_examples(datasetId="my-dataset-id", datasetVersion="1")
   ```

1. 

   ```
   import boto3
   
   client = boto3.client('bedrock-agentcore-control')
   
   resp = client.list_dataset_examples(datasetId='my-dataset-id')
   for example in resp['examples']:
       print(f"  {example['exampleId']}: {example.get('scenario_id')}")
   
   # List examples from a published version
   resp = client.list_dataset_examples(datasetId='my-dataset-id', datasetVersion='1')
   ```

1. 

   ```
   # List examples from Draft
   aws bedrock-agentcore-control list-dataset-examples \
       --dataset-id my-dataset-id
   
   # List examples from a published version
   aws bedrock-agentcore-control list-dataset-examples \
       --dataset-id my-dataset-id \
       --dataset-version 1
   ```