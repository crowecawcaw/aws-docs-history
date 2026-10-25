

# Getting started
<a name="datasets-getting-started"></a>

This topic provides an end-to-end workflow for creating, populating, and publishing a dataset.

## Dataset schemas
<a name="datasets-gs-schema-overview"></a>

Each dataset declares a `schemaType` at creation time. AgentCore validates every example against the declared schema before accepting it. Two schema types are supported:
+  **AGENTCORE\_EVALUATION\_PREDEFINED\_V1** — For testing agents against pre-written conversation turns. Required fields: `scenario_id`, `turns` (non-empty list; each turn must contain `input`).
+  **AGENTCORE\_EVALUATION\_SIMULATED\_V1** — For synthetic conversation generation. Required fields: `scenario_id`, `actor_profile` (object with required `context` and `goal`), `input`.

For full schema field definitions, examples, and ground truth mapping, see [Dataset schema](dataset-evaluations-schema.md).

## End-to-end workflow
<a name="datasets-gs-workflow"></a>

The following example demonstrates the complete dataset lifecycle: create a dataset, change its examples, publish a version, and clean up.

**Example**  

1. 

   Save the following examples as `my_eval_dataset.jsonl`, one JSON object per line:

   ```
   {"scenario_id": "TC-01", "turns": [{"input": "What is my balance?", "expected_response": "Your balance is $50."}], "assertions": ["Response includes a dollar amount"]}
   {"scenario_id": "TC-02", "turns": [{"input": "Transfer $100", "expected_response": "Transfer complete."}]}
   ```

   Then run the following commands. They use `jq` to read the dataset ID and version from the JSON output.

   ```
   # Wait until a dataset version is ACTIVE and has a download URL.
   # Usage: wait_for_dataset DRAFT, or wait_for_dataset <version-number>
   wait_for_dataset() {
     for attempt in $(seq 1 60); do
       METADATA=$(agentcore eval dataset get --id "$DATASET_ID" --version "$1")
       STATUS=$(echo "$METADATA" | jq -r '.status')
       case "$STATUS" in
         ACTIVE) echo "$METADATA" | jq -e '.downloadUrl' > /dev/null && return 0 ;;
         *_FAILED) echo "Dataset status is $STATUS" >&2; return 1 ;;
       esac
       sleep 5
     done
     echo "Timed out waiting for dataset $DATASET_ID" >&2
     return 1
   }
   
   # 1. Create dataset from a JSONL file and wait for ingestion to finish
   DATASET_ID=$(agentcore eval dataset create \
     --name my_eval_dataset \
     --schema-type predefined \
     --source file://my_eval_dataset.jsonl | jq -r '.datasetId')
   wait_for_dataset DRAFT
   
   # 2. Download the DRAFT. Each line now includes the exampleId that the service assigned.
   agentcore eval dataset get \
     --id "$DATASET_ID" \
     --file-path my_eval_dataset.jsonl
   
   # 3. Edit my_eval_dataset.jsonl. Keep the exampleId on each existing line.
   #    Then reconcile your changes into the DRAFT.
   agentcore eval dataset update \
     --id "$DATASET_ID" \
     --file-path my_eval_dataset.jsonl
   
   # 4. Publish a version and wait for it to be ready
   DATASET_VERSION=$(agentcore eval dataset publish --id "$DATASET_ID" | jq -r '.datasetVersion')
   wait_for_dataset "$DATASET_VERSION"
   
   # 5. Download the published version
   agentcore eval dataset get \
     --id "$DATASET_ID" \
     --version "$DATASET_VERSION" \
     --file-path "my_eval_dataset-v$DATASET_VERSION.jsonl"
   
   # 6. Cleanup
   agentcore eval dataset delete --id "$DATASET_ID"
   ```

   The `create` and `publish` commands return while the dataset is still `CREATING` or `UPDATING`. The `update` command waits for each batch of changes to finish before it returns.

1. 

   ```
   from bedrock_agentcore.evaluation import DatasetClient
   
   client = DatasetClient(region_name="us-west-2")
   
   # 1. Create dataset (polls until ACTIVE)
   ds = client.create_dataset_and_wait(
       datasetName="my_eval_dataset",
       schemaType="AGENTCORE_EVALUATION_PREDEFINED_V1",
       source={
           "inlineExamples": {
               "examples": [
                   {
                       "scenario_id": "TC-01",
                       "turns": [{"input": "What is my balance?", "expected_response": "Your balance is $50."}],
                       "assertions": ["Response includes a dollar amount"],
                   }
               ]
           }
       },
   )
   dataset_id = ds["datasetId"]
   print(f"Created: {dataset_id}, status={ds['status']}")
   
   # 2. Add more examples
   ds = client.add_examples_and_wait(
       datasetId=dataset_id,
       source={
           "inlineExamples": {
               "examples": [
                   {"scenario_id": "TC-02", "turns": [{"input": "Transfer $100", "expected_response": "Transfer complete."}]}
               ]
           }
       },
   )
   print(f"Example count: {ds['exampleCount']}")
   
   # 3. List examples
   resp = client.list_dataset_examples(datasetId=dataset_id)
   for example in resp["examples"]:
       print(f"  {example['exampleId']}: {example['scenario_id']}")
   
   # 4. Publish version 1
   ds = client.create_dataset_version_and_wait(datasetId=dataset_id)
   print(f"Published, draftStatus: {ds.get('draftStatus')}")
   
   # 5. List versions
   resp = client.list_dataset_versions(datasetId=dataset_id)
   for v in resp["versions"]:
       print(f"  Version {v['datasetVersion']}: {v['exampleCount']} examples")
   
   # 6. Cleanup
   client.delete_dataset_and_wait(datasetId=dataset_id)
   ```