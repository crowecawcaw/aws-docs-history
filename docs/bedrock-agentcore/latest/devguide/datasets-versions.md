

# Manage dataset versions

Dataset versioning lets you capture immutable, numbered snapshots of the Draft. Each version is a stable, reproducible copy that you can reuse for evaluation runs while you continue to edit the Draft. Use `CreateDatasetVersion` to publish the current Draft as a numbered version. The Draft persists unchanged after publishing — `draftStatus` changes from `MODIFIED` to `UNMODIFIED`.

## CreateDatasetVersion
<a name="datasets-create-version"></a>

The following examples show how to publish a version with the AgentCore CLI, AgentCore SDK, AWS SDK, and AWS CLI:

**Example**  

1. 

   ```bash
   agentcore eval dataset publish --id <DATASET_ID>
   ```

   The command returns the new `datasetVersion` while the dataset is still `UPDATING`. Run `agentcore eval dataset get --id <DATASET_ID> --version <VERSION>` until the status is `ACTIVE` before you download the version.

1. 

   ```python
   from bedrock_agentcore.evaluation import DatasetClient
   
   client = DatasetClient(region_name="us-west-2")
   
   ds = client.create_dataset_version_and_wait(datasetId="my-dataset-id")
   print(f"Published, draftStatus: {ds.get('draftStatus')}")
   ```

1. 

   ```python
   import boto3
   
   client = boto3.client('bedrock-agentcore-control')
   
   client.create_dataset_version(datasetId='my-dataset-id')
   ```

1. 

   ```bash
   aws bedrock-agentcore-control create-dataset-version \
       --dataset-id my-dataset-id
   ```

## ListDatasetVersions
<a name="datasets-list-versions"></a>

Returns published versions sorted newest first. Each version summary includes `datasetVersion`, `exampleCount`, `exampleCountByField` (that version’s counts for each field), and `createdAt`.

The following JSON shows the `exampleCountByField` field, which reports how many examples have each field:

```json
"exampleCountByField": { "turns": 12, "input": 30, "actorProfile": 25 }
```

Each value is the number of examples that have that field. An example can count under more than one field, so the values do not add up to `exampleCount`. The field is absent when the counts are unknown. An example has a field when its value is not null and not a blank string. The value must also not be an empty list or an empty object.

You can include an optional `filter` in the request to return only the versions whose counts match your conditions. A request without a filter returns all versions.

 `filter.exampleCountByField` is a list of 1–3 conditions, and a version matches when at least one condition holds. Each condition has a required `anyOf` list that holds 1–3 of `TURNS`, `INPUT`, and `ACTOR_PROFILE`. Each condition also sets a `min`, a `max`, or both. These bounds are inclusive and must be `>= 0`, and `min` must be less than or equal to `max`. A condition counts the examples that have at least one of its `anyOf` fields. Versions without counts never match.

The following `filter` value matches versions that have at least one fixed scenario:

```json
{"exampleCountByField": [{"anyOf": ["TURNS"], "min": 1}]}
```

**Note**  
A filtered page can contain fewer than `maxResults` items, or none, and still return a `nextToken`. Keep paging until `nextToken` is absent. Send the same filter on every page; a different or missing filter returns a `ValidationException`.

The following AgentCore SDK, AWS SDK, and AWS CLI examples show how to list versions, including a filtered request:

**Example**  

1. 

   ```python
   from bedrock_agentcore.evaluation import DatasetClient
   
   client = DatasetClient(region_name="us-west-2")
   
   resp = client.list_dataset_versions(datasetId="my-dataset-id")
   for v in resp["versions"]:
       print(f"  Version {v['datasetVersion']}: {v['exampleCount']} examples")
   
   # List only versions that have at least one fixed scenario
   resp = client.list_dataset_versions(
       datasetId="my-dataset-id",
       filter={"exampleCountByField": [{"anyOf": ["TURNS"], "min": 1}]},
   )
   ```

1. 

   ```python
   import boto3
   
   client = boto3.client('bedrock-agentcore-control')
   
   resp = client.list_dataset_versions(datasetId='my-dataset-id')
   for v in resp['versions']:
       print(f"  Version {v['datasetVersion']}: {v['exampleCount']} examples")
   
   # List only versions that have at least one fixed scenario
   resp = client.list_dataset_versions(
       datasetId='my-dataset-id',
       filter={'exampleCountByField': [{'anyOf': ['TURNS'], 'min': 1}]}
   )
   ```

1. 

   ```bash
   aws bedrock-agentcore-control list-dataset-versions \
       --dataset-id my-dataset-id
   
   # List only versions that have at least one fixed scenario
   aws bedrock-agentcore-control list-dataset-versions \
       --dataset-id my-dataset-id \
       --filter '{"exampleCountByField": [{"anyOf": ["TURNS"], "min": 1}]}'
   ```