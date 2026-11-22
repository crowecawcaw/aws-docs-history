

# Manage datasets

Amazon Bedrock AgentCore (AgentCore) datasets store the evaluation examples that you run against your agents. This topic covers creating, retrieving, listing, updating, and deleting datasets so that you can maintain your evaluation data over time.

## Create dataset
<a name="datasets-create"></a>

The `CreateDataset` API creates a new evaluation dataset. This is an asynchronous operation. The dataset transitions from `CREATING` to `ACTIVE` once ingestion completes.

 **Required parameters:** `datasetName` (alphanumeric and underscores only, `^[a-zA-Z][a-zA-Z0-9_]{0,47}$`).

 **Optional parameters:** `source` (inline examples or S3 URI), `description`, `kmsKeyArn` (customer managed encryption key, immutable after creation; see [Dataset encryption](datasets-encryption.md)), `tags`.

If you omit `source`, you create an empty dataset (a Draft with zero examples) that you fill later with the `AddDatasetExamples` API. A dataset can hold a mix of fixed scenarios and dynamic scenarios.

**Note**  
If an older client sends a `schemaType` value, the service ignores it.

The following AgentCore CLI, AgentCore SDK, AWS SDK, and AWS CLI examples show how to create a dataset:

**Example**  

1. 

   ```bash
   # Create a dataset from a JSONL file
   agentcore eval dataset create \
     --name my_eval_dataset \
     --source file://my_eval_dataset.jsonl
   ```

   The command returns the dataset ID while the dataset is still `CREATING`. Run `agentcore eval dataset get --id <DATASET_ID>` until the status is `ACTIVE` before you change the dataset.

1. 

   ```python
   from bedrock_agentcore.evaluation import DatasetClient
   
   client = DatasetClient(region_name="us-west-2")
   
   # Create with inline examples (polls until ACTIVE)
   ds = client.create_dataset_and_wait(
       datasetName="customer_support_scenarios",
       source={
           "inlineExamples": {
               "examples": [
                   {
                       "scenario_id": "TC-01",
                       "turns": [{"input": "What is the weather in Seattle today?", "expected_response": "It is 15°C and cloudy in Seattle today."}],
                       "assertions": ["Response includes a temperature"],
                   }
               ]
           }
       },
   )
   print(f"Dataset ID: {ds['datasetId']}, Status: {ds['status']}")
   
   # Create with S3 source
   ds = client.create_dataset_and_wait(
       datasetName="my_s3_dataset",
       source={"s3Source": {"s3Uri": "s3://my-bucket/scenarios.jsonl"}},
   )
   ```
**Note**  
For S3 ingestion, each line in the JSONL file must include an `exampleId` field. The S3 bucket must be accessible using the caller’s credentials.

1. 

   ```python
   import boto3
   import time
   
   client = boto3.client('bedrock-agentcore-control')
   
   response = client.create_dataset(
       datasetName='customer_support_scenarios',
       source={
           'inlineExamples': {
               'examples': [
                   {
                       'scenario_id': 'TC-01',
                       'turns': [{'input': 'What is the weather in Seattle today?', 'expected_response': 'It is 15°C and cloudy in Seattle today.'}],
                       'assertions': ['Response includes a temperature'],
                   }
               ]
           }
       }
   )
   dataset_id = response['datasetId']
   
   # Create with S3 source
   response = client.create_dataset(
       datasetName='my_s3_dataset',
       source={
           's3Source': {'s3Uri': 's3://my-bucket/scenarios.jsonl'}
       }
   )
   
   # Poll until ACTIVE
   while True:
       ds = client.get_dataset(datasetId=dataset_id)
       if ds['status'] in ('ACTIVE', 'CREATE_FAILED'):
           break
       time.sleep(2)
   ```

1. 

   ```bash
   # Create with inline examples
   aws bedrock-agentcore-control create-dataset \
       --dataset-name "customer_support_scenarios" \
       --source '{"inlineExamples": {"examples": [{"scenario_id": "TC-01", "turns": [{"input": "What is the weather in Seattle today?", "expected_response": "It is 15°C and cloudy in Seattle today."}], "assertions": ["Response includes a temperature"]}]}}'
   
   # Create with S3 source
   aws bedrock-agentcore-control create-dataset \
       --dataset-name "my_s3_dataset" \
       --source '{"s3Source": {"s3Uri": "s3://my-bucket/scenarios.jsonl"}}'
   
   # Poll until ACTIVE
   aws bedrock-agentcore-control get-dataset \
       --dataset-id my-dataset-id
   ```

## Get dataset
<a name="datasets-get"></a>

The `GetDataset` API retrieves dataset metadata, status, example count, and per-field example counts. It also returns a presigned download URL for the dataset content. By default, this operation reads the Draft. To read a published version, specify `datasetVersion`.

The response includes an `exampleCountByField` field that reports how many examples have each field:

```json
"exampleCountByField": { "turns": 12, "input": 30, "actorProfile": 25 }
```

Each value is the number of examples that have that field. An example can count under more than one field, so the values do not add up to `exampleCount`. The response omits the field when the counts are unknown. An example has a field when its value is not null, not a blank string, not an empty list, and not an empty object.

The `downloadUrl` is a presigned S3 URL for the full `dataset.jsonl` file. You can download it with a plain HTTPS GET request without authentication headers.

The following AgentCore CLI, AgentCore SDK, AWS SDK, and AWS CLI examples show how to get a dataset:

**Example**  

1. 

   ```bash
   # Show dataset metadata
   agentcore eval dataset get --id <DATASET_ID>
   
   # Download the DRAFT
   agentcore eval dataset get \
     --id <DATASET_ID> \
     --file-path my_eval_dataset.jsonl
   
   # Download a specific published version
   agentcore eval dataset get \
     --id <DATASET_ID> \
     --version 1 \
     --file-path my_eval_dataset-v1.jsonl
   ```

1. 

   ```python
   from bedrock_agentcore.evaluation import DatasetClient
   
   client = DatasetClient(region_name="us-west-2")
   
   # Get dataset (default: Draft)
   ds = client.get_dataset(datasetId="my-dataset-id")
   print(f"Status: {ds['status']}, Examples: {ds['exampleCount']}")
   print(f"Download URL: {ds['downloadUrl']}")
   
   # Get a specific published version
   ds_v1 = client.get_dataset(datasetId="my-dataset-id", datasetVersion="1")
   ```

1. 

   ```python
   import boto3
   
   client = boto3.client('bedrock-agentcore-control')
   
   response = client.get_dataset(datasetId='my-dataset-id')
   print(f"Status: {response['status']}, Examples: {response['exampleCount']}")
   
   # Download the dataset content via presigned URL
   if 'downloadUrl' in response:
       import requests
       data = requests.get(response['downloadUrl'])
       print(data.text)
   
   # Get a specific published version
   response = client.get_dataset(datasetId='my-dataset-id', datasetVersion='1')
   ```

1. 

   ```bash
   # Get dataset (default: Draft)
   aws bedrock-agentcore-control get-dataset \
       --dataset-id my-dataset-id
   
   # Get a specific published version
   aws bedrock-agentcore-control get-dataset \
       --dataset-id my-dataset-id \
       --dataset-version 1
   ```

## List datasets
<a name="datasets-list"></a>

The `ListDatasets` API returns a paginated list of datasets in your account and Region. Each dataset summary includes `exampleCountByField` for the Draft, the per-field example counts described in [Get dataset](#datasets-get).

You can include an optional `filter` in the request to return only the datasets whose counts match your conditions. A request without a filter returns all datasets.

 `filter.exampleCountByField` is a list of 1–3 conditions, and a dataset matches when at least one condition holds. Each condition has a required `anyOf` list of 1–3 of `TURNS`, `INPUT`, and `ACTOR_PROFILE`. Each condition also has a `min`, a `max`, or both, which are inclusive, `>= 0`, with `min` less than or equal to `max`. A condition counts the examples that have at least one of its `anyOf` fields. `ListDatasets` compares the `DRAFT` counts. Datasets without counts never match.

The following `filter` value matches datasets that have at least one fixed scenario:

```json
{"exampleCountByField": [{"anyOf": ["TURNS"], "min": 1}]}
```

**Note**  
A filtered page can contain fewer than `maxResults` items, or none. It can still return a `nextToken`. Keep paging until `nextToken` is absent. Send the same filter on every page. A different or missing filter returns a `ValidationException`.

The following AgentCore CLI, AgentCore SDK, AWS SDK, and AWS CLI examples show how to list datasets. The AgentCore SDK, AWS SDK, and AWS CLI examples also show a filtered request. The AgentCore CLI doesn’t support the `filter`.

**Example**  

1. 

   ```bash
   agentcore eval dataset list
   ```

1. 

   ```python
   from bedrock_agentcore.evaluation import DatasetClient
   
   client = DatasetClient(region_name="us-west-2")
   
   response = client.list_datasets()
   for dataset in response["datasets"]:
       print(f"  {dataset['datasetName']} ({dataset['status']})")
   
   # List only datasets that have at least one fixed scenario
   response = client.list_datasets(
       filter={"exampleCountByField": [{"anyOf": ["TURNS"], "min": 1}]}
   )
   ```

1. 

   ```python
   import boto3
   
   client = boto3.client('bedrock-agentcore-control')
   
   response = client.list_datasets()
   for dataset in response['datasets']:
       print(f"  {dataset['datasetName']} ({dataset['status']})")
   
   # List only datasets that have at least one fixed scenario
   response = client.list_datasets(
       filter={'exampleCountByField': [{'anyOf': ['TURNS'], 'min': 1}]}
   )
   ```

1. 

   ```bash
   aws bedrock-agentcore-control list-datasets
   
   # List only datasets that have at least one fixed scenario
   aws bedrock-agentcore-control list-datasets \
       --filter '{"exampleCountByField": [{"anyOf": ["TURNS"], "min": 1}]}'
   ```

## Update dataset
<a name="datasets-update"></a>

The `UpdateDataset` API updates dataset metadata. This is a synchronous operation (HTTP 200). You can update only `description`. To change tags, use the `TagResource` and `UntagResource` APIs. You can’t change `datasetName` or `kmsKeyArn` after you create the dataset.

The dataset must be in `ACTIVE`, `UPDATE_FAILED`, or `CREATE_FAILED` status.

The following AgentCore CLI, AgentCore SDK, AWS SDK, and AWS CLI examples show how to update dataset metadata:

**Example**  

1. The `agentcore eval dataset update` command changes DRAFT examples, not dataset metadata. To change the description, use the AgentCore SDK or the AWS SDK instead.

1. 

   ```python
   from bedrock_agentcore.evaluation import DatasetClient
   
   client = DatasetClient(region_name="us-west-2")
   
   client.update_dataset(datasetId="my-dataset-id", description="Updated description")
   ```

1. 

   ```python
   import boto3
   
   client = boto3.client('bedrock-agentcore-control')
   
   client.update_dataset(datasetId='my-dataset-id', description='Updated description')
   ```

1. 

   ```bash
   aws bedrock-agentcore-control update-dataset \
       --dataset-id my-dataset-id \
       --description "Updated description"
   ```

## Delete dataset
<a name="datasets-delete"></a>

The `DeleteDataset` API deletes a dataset. This is an asynchronous operation.
+  **Full delete** (omit `datasetVersion`) – Deletes all versions, Draft, and the dataset record.
+  **Version-specific delete** (specify `datasetVersion` as an integer) – Deletes only that published version.

The dataset must be in `ACTIVE`, `CREATE_FAILED`, `UPDATE_FAILED`, or `DELETE_FAILED` status.

**Note**  
Only integer version numbers are accepted for version-specific deletion.

The following AgentCore CLI, AgentCore SDK, AWS SDK, and AWS CLI examples show how to delete a dataset:

**Example**  

1. 

   ```bash
   # Delete a specific published version
   agentcore eval dataset delete --id <DATASET_ID> --version 1
   
   # Delete entire dataset
   agentcore eval dataset delete --id <DATASET_ID>
   ```

1. 

   ```python
   from bedrock_agentcore.evaluation import DatasetClient
   
   client = DatasetClient(region_name="us-west-2")
   
   # Delete a specific published version
   client.delete_dataset_and_wait(datasetId="my-dataset-id", datasetVersion="1")
   
   # Delete entire dataset (polls until complete)
   client.delete_dataset_and_wait(datasetId="my-dataset-id")
   ```

1. 

   ```python
   import boto3
   
   client = boto3.client('bedrock-agentcore-control')
   
   # Delete a specific published version
   client.delete_dataset(datasetId='my-dataset-id', datasetVersion='1')
   
   # Delete entire dataset
   client.delete_dataset(datasetId='my-dataset-id')
   ```

1. 

   ```bash
   # Delete a specific published version
   aws bedrock-agentcore-control delete-dataset \
       --dataset-id my-dataset-id \
       --dataset-version 1
   
   # Delete entire dataset
   aws bedrock-agentcore-control delete-dataset \
       --dataset-id my-dataset-id
   ```