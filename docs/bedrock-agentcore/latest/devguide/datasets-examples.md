

# Manage dataset examples

Dataset examples are the test cases that your evaluations run against. After a dataset reaches `ACTIVE` status, you can add, update, delete, and list examples in the Draft. All example mutations are asynchronous and return HTTP 202. They use all-or-nothing semantics. If any example ID is not found, the entire batch fails with `ResourceNotFoundException`.

Each request can include a maximum of 1,000 examples. The inline content limit is 5 MB.

In the Amazon Bedrock AgentCore CLI, `agentcore eval dataset update` adds, updates, and deletes examples in one step. It makes the DRAFT match a local JSONL file by `exampleId`. A line without an `exampleId` is added as a new example. A line whose `exampleId` matches a DRAFT example updates that example if its content changed. `update` deletes any DRAFT example whose `exampleId` is not in the file. Start from a file downloaded with `agentcore eval dataset get --id <DATASET_ID> --file-path <FILE>`, which includes the `exampleId` of each example. Don’t reuse the file that you passed to `agentcore eval dataset create`. That file has no `exampleId` values. As a result, `update` deletes every DRAFT example and adds them all again with new IDs.

## AddDatasetExamples
<a name="datasets-add-examples"></a>

When you add an example, it’s validated as a fixed or dynamic scenario, with the type inferred from the example’s fields. Each example must have a non-empty `scenario_id` and at least one of `turns`, `input`, or `actor_profile`. For the full field rules, see [Dataset schema](dataset-evaluations-schema.md).

The following AgentCore CLI, AgentCore SDK, AWS SDK, and AWS CLI examples show how to add examples to a dataset:

**Example**  

1. Download the DRAFT, append scenarios to the downloaded JSONL file, then reconcile it with the DRAFT:

   ```bash
   # Download the DRAFT. Each line includes its exampleId.
   agentcore eval dataset get \
     --id <DATASET_ID> \
     --file-path my_eval_dataset.jsonl
   
   # Edit my_eval_dataset.jsonl — add new lines
   agentcore eval dataset update \
     --id <DATASET_ID> \
     --file-path my_eval_dataset.jsonl
   ```

   Running this command adds lines that have no `exampleId` and writes their assigned `exampleId` values back to the file. Unchanged lines that keep their `exampleId` are not uploaded again.

1. 

   ```python
   from bedrock_agentcore.evaluation import DatasetClient
   
   client = DatasetClient(region_name="us-west-2")
   
   ds = client.add_examples_and_wait(
       datasetId="my-dataset-id",
       source={
           "inlineExamples": {
               "examples": [
                   {
                       "scenario_id": "TC-02",
                       "turns": [{"input": "What is 15 + 27?", "expected_response": "15 + 27 = 42"}],
                   },
                   {
                       "scenario_id": "TC-03",
                       "input": "I am visiting Seattle this weekend. What should I pack?",
                       "actor_profile": {
                           "context": "A traveler planning a weekend trip to Seattle.",
                           "goal": "Find out whether to pack a rain jacket.",
                       },
                   },
               ]
           }
       },
   )
   print(f"Example count: {ds['exampleCount']}")
   ```

1. 

   ```python
   import boto3
   import time
   
   client = boto3.client('bedrock-agentcore-control')
   
   resp = client.add_dataset_examples(
       datasetId='my-dataset-id',
       source={'inlineExamples': {'examples': [
           {'scenario_id': 'TC-02', 'turns': [{'input': 'What is 15 + 27?', 'expected_response': '15 + 27 = 42'}]}
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

   ```bash
   aws bedrock-agentcore-control add-dataset-examples \
       --dataset-id my-dataset-id \
       --source '{"inlineExamples": {"examples": [{"scenario_id": "TC-02", "turns": [{"input": "What is 15 + 27?", "expected_response": "15 + 27 = 42"}]}]}}'
   ```

## UpdateDatasetExamples
<a name="datasets-update-examples"></a>

Each entry must include `exampleId` plus the updated content fields. The dataset must be in `ACTIVE` or `UPDATE_FAILED` status.

The following AgentCore CLI, AgentCore SDK, AWS SDK, and AWS CLI examples show how to update dataset examples:

**Example**  

1. Modify existing scenarios in a JSONL file downloaded from the DRAFT, then reconcile it with the DRAFT:

   ```bash
   # Edit my_eval_dataset.jsonl — modify existing lines
   agentcore eval dataset update \
     --id <DATASET_ID> \
     --file-path my_eval_dataset.jsonl
   ```

   Running the command diffs your local file against the service and updates changed examples. Each line must retain its `exampleId` for the service to recognize it as an update rather than a new example.

1. 

   ```python
   from bedrock_agentcore.evaluation import DatasetClient
   
   client = DatasetClient(region_name="us-west-2")
   
   ds = client.update_examples_and_wait(
       datasetId="my-dataset-id",
       examples=[
           {
               "exampleId": "example-id-from-list",
               "scenario_id": "TC-02-updated",
               "turns": [{"input": "What is 15 + 28?", "expected_response": "15 + 28 = 43"}],
           }
       ],
   )
   ```

1. 

   ```python
   import boto3
   import time
   
   client = boto3.client('bedrock-agentcore-control')
   
   client.update_dataset_examples(
       datasetId='my-dataset-id',
       examples=[
           {
               'exampleId': 'example-id-from-list',
               'scenario_id': 'TC-02-updated',
               'turns': [{'input': 'What is 15 + 28?', 'expected_response': '15 + 28 = 43'}],
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

   ```bash
   aws bedrock-agentcore-control update-dataset-examples \
       --dataset-id my-dataset-id \
       --cli-input-json file://update-examples.json
   ```

## DeleteDatasetExamples
<a name="datasets-delete-examples"></a>

The dataset must be in `ACTIVE`, `UPDATE_FAILED`, or `CREATE_FAILED` status.

The following AgentCore CLI, AgentCore SDK, AWS SDK, and AWS CLI examples show how to delete dataset examples:

**Example**  

1. Remove the corresponding lines from a JSONL file downloaded from the DRAFT, then reconcile it with the DRAFT:

   ```bash
   # Edit my_eval_dataset.jsonl — remove lines
   agentcore eval dataset update \
     --id <DATASET_ID> \
     --file-path my_eval_dataset.jsonl
   ```

   Running the command deletes each DRAFT example whose `exampleId` is not in the file.

1. 

   ```python
   from bedrock_agentcore.evaluation import DatasetClient
   
   client = DatasetClient(region_name="us-west-2")
   
   ds = client.delete_examples_and_wait(
       datasetId="my-dataset-id",
       exampleIds=["example-id-1", "example-id-2"],
   )
   ```

1. 

   ```python
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

   ```bash
   aws bedrock-agentcore-control delete-dataset-examples \
       --dataset-id my-dataset-id \
       --example-ids '["example-id-1", "example-id-2"]'
   ```

## ListDatasetExamples
<a name="datasets-list-examples"></a>

Returns a paginated list of examples with full content. By default, reads from the Draft. Specify `datasetVersion` to read from a published version.

You can pass an optional `filter` to return only matching examples. A request without a filter returns all examples. The `filter` has two members:
+  `exampleFields` – A list of 1 to 3 conditions. Each condition has the form `{"anyOf": [<ExampleField>, …​]}`, where each `ExampleField` is `TURNS`, `INPUT`, or `ACTOR_PROFILE`. A condition holds when the example has at least one of its listed fields. An example matches when at least one condition holds. Examples whose fields were not recorded never match. For example, examples last written before this filter existed don’t match.
+  `generationIds` – A list of exactly one dataset generation ID. Returns the examples that the dataset generation produced, matching each example’s `metadata.generation_id`. For more information, see [Dataset generation](dataset-generation.md).

The service AND-combines the `filter` members, and OR-combines the values within each list. The following `filter` value returns only examples that have an `input` field, an `actor_profile` field, or both:

```json
{"exampleFields": [{"anyOf": ["INPUT", "ACTOR_PROFILE"]}]}
```

The following AgentCore CLI, AgentCore SDK, AWS SDK, and AWS CLI examples show how to list dataset examples:

**Example**  

1. 

   ```bash
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

   ```python
   from bedrock_agentcore.evaluation import DatasetClient
   
   client = DatasetClient(region_name="us-west-2")
   
   # List examples from Draft
   resp = client.list_dataset_examples(datasetId="my-dataset-id")
   for example in resp["examples"]:
       print(f"  {example['exampleId']}: {example['scenario_id']}")
   
   # List examples from a published version
   resp = client.list_dataset_examples(datasetId="my-dataset-id", datasetVersion="1")
   
   # List only dynamic-scenario examples (those with an input or actor_profile field)
   resp = client.list_dataset_examples(
       datasetId="my-dataset-id",
       filter={"exampleFields": [{"anyOf": ["INPUT", "ACTOR_PROFILE"]}]},
   )
   ```

1. 

   ```python
   import boto3
   
   client = boto3.client('bedrock-agentcore-control')
   
   resp = client.list_dataset_examples(datasetId='my-dataset-id')
   for example in resp['examples']:
       print(f"  {example['exampleId']}: {example.get('scenario_id')}")
   
   # List examples from a published version
   resp = client.list_dataset_examples(datasetId='my-dataset-id', datasetVersion='1')
   
   # List only dynamic-scenario examples, paging through every result.
   # Send the same filter on every page.
   example_filter = {'exampleFields': [{'anyOf': ['INPUT', 'ACTOR_PROFILE']}]}
   next_token = None
   while True:
       kwargs = {'datasetId': 'my-dataset-id', 'filter': example_filter}
       if next_token:
           kwargs['nextToken'] = next_token
       resp = client.list_dataset_examples(**kwargs)
       for example in resp['examples']:
           print(f"  {example['exampleId']}: {example.get('scenario_id')}")
       next_token = resp.get('nextToken')
       if not next_token:
           break
   ```

1. 

   ```bash
   # List examples from Draft
   aws bedrock-agentcore-control list-dataset-examples \
       --dataset-id my-dataset-id
   
   # List examples from a published version
   aws bedrock-agentcore-control list-dataset-examples \
       --dataset-id my-dataset-id \
       --dataset-version 1
   
   # List only examples that have a turns field
   aws bedrock-agentcore-control list-dataset-examples \
       --dataset-id my-dataset-id \
       --filter '{"exampleFields": [{"anyOf": ["TURNS"]}]}'
   ```

When you filter, a page might contain fewer than `maxResults` items, or none, and still return a `nextToken`. Keep paging until the response has no `nextToken`. Send the same `filter` on every page; if the `filter` changes between pages, the request fails with `ValidationException`.

The dataset version is pinned in the `nextToken`. On later pages, you can omit `datasetVersion`. If you send a `datasetVersion` that differs from the version pinned in the token, the request fails with `ValidationException`.