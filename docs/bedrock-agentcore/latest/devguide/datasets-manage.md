

# Manage datasets
<a name="datasets-manage"></a>

This topic covers creating, retrieving, listing, updating, and deleting datasets.

## Create dataset
<a name="datasets-create"></a>

The `CreateDataset` API creates a new evaluation dataset. This is an asynchronous operation (HTTP 202) — the dataset transitions from `CREATING` to `ACTIVE` once ingestion completes.

 **Required parameters:** `datasetName` (alphanumeric and underscores only, `^[a-zA-Z][a-zA-Z0-9_]{0,47}$`), `schemaType`, and `source` (inline examples or S3 URI).

 **Optional parameters:** `description`, `kmsKeyArn` (customer managed encryption key, immutable after creation — see [Dataset encryption](datasets-encryption.md)), `tags`.

The following examples show how to create a dataset:

**Example**  

1. 

   ```
   # Create a dataset from a JSONL file
   agentcore eval dataset create \
     --name my_eval_dataset \
     --schema-type predefined \
     --source file://my_eval_dataset.jsonl
   ```

   The command returns the dataset ID while the dataset is still `CREATING`. Run `agentcore eval dataset get --id <DATASET_ID>` until the status is `ACTIVE` before you change the dataset.

1. 

   ```
   from bedrock_agentcore.evaluation import DatasetClient
   
   client = DatasetClient(region_name="us-west-2")
   
   # Create with inline examples (polls until ACTIVE)
   ds = client.create_dataset_and_wait(
       datasetName="customer_support_scenarios",
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
   print(f"Dataset ID: {ds['datasetId']}, Status: {ds['status']}")
   
   # Create with S3 source
   ds = client.create_dataset_and_wait(
       datasetName="my_s3_dataset",
       schemaType="AGENTCORE_EVALUATION_PREDEFINED_V1",
       source={"s3Source": {"s3Uri": "s3://my-bucket/scenarios.jsonl"}},
   )
   ```
**Note**  
For S3 ingestion, each line in the JSONL file must include an `exampleId` field. The S3 bucket must be accessible using the caller’s credentials.

1. 

   ```
   import boto3
   import time
   
   client = boto3.client('bedrock-agentcore-control')
   
   response = client.create_dataset(
       datasetName='customer_support_scenarios',
       schemaType='AGENTCORE_EVALUATION_PREDEFINED_V1',
       source={
           'inlineExamples': {
               'examples': [
                   {
                       'scenario_id': 'TC-01',
                       'turns': [{'input': 'What is my balance?', 'expected_response': 'Your balance is $50.'}],
                       'assertions': ['Response includes a dollar amount'],
                   }
               ]
           }
       }
   )
   dataset_id = response['datasetId']
   
   # Create with S3 source
   response = client.create_dataset(
       datasetName='my_s3_dataset',
       schemaType='AGENTCORE_EVALUATION_PREDEFINED_V1',
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

   ```
   # Create with inline examples
   aws bedrock-agentcore-control create-dataset \
       --dataset-name "customer_support_scenarios" \
       --schema-type AGENTCORE_EVALUATION_PREDEFINED_V1 \
       --source '{"inlineExamples": {"examples": [{"scenario_id": "TC-01", "turns": [{"input": "What is my balance?", "expected_response": "Your balance is $50."}], "assertions": ["Response includes a dollar amount"]}]}}'
   
   # Create with S3 source
   aws bedrock-agentcore-control create-dataset \
       --dataset-name "my_s3_dataset" \
       --schema-type AGENTCORE_EVALUATION_PREDEFINED_V1 \
       --source '{"s3Source": {"s3Uri": "s3://my-bucket/scenarios.jsonl"}}'
   
   # Poll until ACTIVE
   aws bedrock-agentcore-control get-dataset \
       --dataset-id my-dataset-id
   ```

## Get dataset
<a name="datasets-get"></a>

The `GetDataset` API retrieves dataset metadata, status, example count, and a presigned download URL for the dataset content. By default reads the Draft; specify `datasetVersion` for a published version.

The `downloadUrl` is a presigned S3 URL for the full `dataset.jsonl` file. You can download it with a plain HTTP GET request without authentication headers.

The following examples show how to get a dataset:

**Example**  

1. 

   ```
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

   ```
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

   ```
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

   ```
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

The `ListDatasets` API returns a paginated list of datasets in your account and Region.

The following examples show how to list datasets:

**Example**  

1. 

   ```
   agentcore eval dataset list
   ```

1. 

   ```
   from bedrock_agentcore.evaluation import DatasetClient
   
   client = DatasetClient(region_name="us-west-2")
   
   response = client.list_datasets()
   for dataset in response["datasets"]:
       print(f"  {dataset['datasetName']} ({dataset['status']})")
   ```

1. 

   ```
   import boto3
   
   client = boto3.client('bedrock-agentcore-control')
   
   response = client.list_datasets()
   for dataset in response['datasets']:
       print(f"  {dataset['datasetName']} ({dataset['status']})")
   ```

1. 

   ```
   aws bedrock-agentcore-control list-datasets
   ```

## Update dataset
<a name="datasets-update"></a>

The `UpdateDataset` API updates dataset metadata. This is a synchronous operation (HTTP 200). Only `description` can be updated. To change tags, use the `TagResource` and `UntagResource` APIs. `datasetName`, `schemaType`, and `kmsKeyArn` are immutable after creation.

The dataset must be in `ACTIVE`, `UPDATE_FAILED`, or `CREATE_FAILED` status.

The following examples show how to update dataset metadata:

**Example**  

1.  `agentcore eval dataset update` changes DRAFT examples, not dataset metadata. To change the description, use the AgentCore SDK or AWS SDK.

1. 

   ```
   from bedrock_agentcore.evaluation import DatasetClient
   
   client = DatasetClient(region_name="us-west-2")
   
   client.update_dataset(datasetId="my-dataset-id", description="Updated description")
   ```

1. 

   ```
   import boto3
   
   client = boto3.client('bedrock-agentcore-control')
   
   client.update_dataset(datasetId='my-dataset-id', description='Updated description')
   ```

1. 

   ```
   aws bedrock-agentcore-control update-dataset \
       --dataset-id my-dataset-id \
       --description "Updated description"
   ```

## Delete dataset
<a name="datasets-delete"></a>

The `DeleteDataset` API deletes a dataset. This is an asynchronous operation (HTTP 202).
+  **Full delete** (omit `datasetVersion`): Deletes all versions, Draft, and the dataset record.
+  **Version-specific delete** (specify `datasetVersion` as an integer): Deletes only that published version.

The dataset must be in `ACTIVE`, `CREATE_FAILED`, `UPDATE_FAILED`, or `DELETE_FAILED` status.

**Note**  
Only integer version numbers are accepted for version-specific deletion.

The following examples show how to delete a dataset:

**Example**  

1. 

   ```
   # Delete a specific published version
   agentcore eval dataset delete --id <DATASET_ID> --version 1
   
   # Delete entire dataset
   agentcore eval dataset delete --id <DATASET_ID>
   ```

1. 

   ```
   from bedrock_agentcore.evaluation import DatasetClient
   
   client = DatasetClient(region_name="us-west-2")
   
   # Delete a specific published version
   client.delete_dataset_and_wait(datasetId="my-dataset-id", datasetVersion="1")
   
   # Delete entire dataset (polls until complete)
   client.delete_dataset_and_wait(datasetId="my-dataset-id")
   ```

1. 

   ```
   import boto3
   
   client = boto3.client('bedrock-agentcore-control')
   
   # Delete a specific published version
   client.delete_dataset(datasetId='my-dataset-id', datasetVersion='1')
   
   # Delete entire dataset
   client.delete_dataset(datasetId='my-dataset-id')
   ```

1. 

   ```
   # Delete a specific published version
   aws bedrock-agentcore-control delete-dataset \
       --dataset-id my-dataset-id \
       --dataset-version 1
   
   # Delete entire dataset
   aws bedrock-agentcore-control delete-dataset \
       --dataset-id my-dataset-id
   ```