

# Getting started

Datasets let you define reusable test scenarios so that you can evaluate your agent’s behavior consistently as it changes. This topic provides an end-to-end workflow for creating, populating, and publishing a dataset.

## Scenario types
<a name="datasets-gs-schema-overview"></a>

A dataset is a collection of scenarios. It doesn’t declare a schema type. Each scenario is a fixed scenario or a dynamic scenario, and a single dataset can hold a mix of both. The fields in each scenario determine its type and how it runs. Every scenario has a `scenario_id`, which is the scenario’s **unique identifier** within the dataset.
+  **Fixed scenario** - Contains `turns`, a sequence of one or more pre-written conversation turns that the runner replays exactly as written. A fixed scenario can be single-turn or multi-turn.
+  **Dynamic scenario** - Has no `turns`, and contains `input`, `actor_profile`, or both. An actor drives the conversation based on a persona and goal.

**Note**  
If an older client sends a `schemaType` value, AgentCore ignores it.

For field definitions, examples, limits, and ground truth mapping, see [Dataset schema](dataset-evaluations-schema.md).

## End-to-end workflow
<a name="datasets-gs-workflow"></a>

The following example demonstrates the complete dataset lifecycle: create a dataset, change its examples, publish a version, and clean up.

**Example**  

1. 

   Create a file named `my_eval_dataset.jsonl`, a JSON Lines (JSONL) file. Save the following examples to it, one JSON object per line:

   ```json
   {"scenario_id": "TC-01", "turns": [{"input": "What is the weather in Seattle today?", "expected_response": "It is 15°C and cloudy in Seattle today."}, {"input": "Will it rain there tomorrow?", "expected_response": "Yes, rain is expected in Seattle tomorrow."}], "assertions": ["Agent answers the second question about Seattle, the city from the first turn", "Agent used the weather tool for both questions"]}
   {"scenario_id": "TC-02", "turns": [{"input": "What is 15 + 27?", "expected_response": "15 + 27 = 42"}]}
   ```

   Then run the following AgentCore CLI commands, which use `jq` to read the dataset ID and version from the JSON output:

   ```bash
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

   The following Python code example shows the complete dataset lifecycle using the AgentCore SDK:

   ```python
   from bedrock_agentcore.evaluation import DatasetClient
   
   client = DatasetClient(region_name="us-west-2")
   
   # 1. Create dataset (polls until ACTIVE)
   ds = client.create_dataset_and_wait(
       datasetName="my_eval_dataset",
       source={
           "inlineExamples": {
               "examples": [
                   {
                       "scenario_id": "TC-01",
                       "turns": [
                           {
                               "input": "What is the weather in Seattle today?",
                               "expected_response": "It is 15°C and cloudy in Seattle today.",
                           },
                           {
                               "input": "Will it rain there tomorrow?",
                               "expected_response": "Yes, rain is expected in Seattle tomorrow.",
                           },
                       ],
                       "assertions": [
                           "Agent answers the second question about Seattle, the city from the first turn",
                           "Agent used the weather tool for both questions",
                       ],
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
                   {"scenario_id": "TC-02", "turns": [{"input": "What is 15 + 27?", "expected_response": "15 + 27 = 42"}]}
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

After you publish a version, choose whether AgentCore or your code invokes the agent. See [Choose how to run a dataset evaluation](dataset-evaluations.md#dataset-evaluations-choose).