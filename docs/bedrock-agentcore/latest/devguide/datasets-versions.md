

# Manage dataset versions
<a name="datasets-versions"></a>

Use `CreateDatasetVersion` to publish the current Draft as an immutable numbered version. The Draft persists unchanged after publishing — `draftStatus` changes from `MODIFIED` to `UNMODIFIED`.

## CreateDatasetVersion
<a name="datasets-create-version"></a>

The following examples show how to publish a version:

**Example**  

1. 

   ```
   agentcore dataset publish-version --name my_eval_dataset
   ```

1. 

   ```
   from bedrock_agentcore.evaluation import DatasetClient
   
   client = DatasetClient(region_name="us-west-2")
   
   ds = client.create_dataset_version_and_wait(datasetId="my-dataset-id")
   print(f"Published, draftStatus: {ds.get('draftStatus')}")
   ```

1. 

   ```
   import boto3
   
   client = boto3.client('bedrock-agentcore-control')
   
   client.create_dataset_version(datasetId='my-dataset-id')
   ```

1. 

   ```
   aws bedrock-agentcore-control create-dataset-version \
       --dataset-id my-dataset-id
   ```

## ListDatasetVersions
<a name="datasets-list-versions"></a>

Returns published versions sorted newest first. Each version summary includes `datasetVersion`, `exampleCount`, and `createdAt`.

The following examples show how to list versions:

**Example**  

1. 

   ```
   agentcore status --type dataset
   ```

1. 

   ```
   from bedrock_agentcore.evaluation import DatasetClient
   
   client = DatasetClient(region_name="us-west-2")
   
   resp = client.list_dataset_versions(datasetId="my-dataset-id")
   for v in resp["versions"]:
       print(f"  Version {v['datasetVersion']}: {v['exampleCount']} examples")
   ```

1. 

   ```
   import boto3
   
   client = boto3.client('bedrock-agentcore-control')
   
   resp = client.list_dataset_versions(datasetId='my-dataset-id')
   for v in resp['versions']:
       print(f"  Version {v['datasetVersion']}: {v['exampleCount']} examples")
   ```

1. 

   ```
   aws bedrock-agentcore-control list-dataset-versions \
       --dataset-id my-dataset-id
   ```