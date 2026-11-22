

# List and delete dataset generations

 `ListDatasetGenerations` returns the generations for a dataset, with `maxResults` from 1 to 100 (the default is 20) and a `nextToken` for paging. Each summary has `generationId`, `datasetId`, `name`, `description`, `scenarioType`, `status`, `createdAt`, and `completedAt`. The service keeps records until you delete them or delete the dataset.

 `DeleteDatasetGeneration` deletes only the generation record, and only when the generation is in a terminal state. Deleting a generation that is still running returns `ConflictException`. The generated examples stay in the Draft. To remove them, list them with the `generationIds` filter and call `DeleteDatasetExamples`.

**Example**  

1. 

   ```bash
   # List the generations for a dataset
   agentcore eval dataset-generation list \
     --dataset-id my-dataset-id
   
   # Delete a generation record (terminal state only)
   agentcore eval dataset-generation delete \
     --dataset-id my-dataset-id \
     --id weeknight-sessions-abcd123456
   ```

1. 

   ```python
   import boto3
   
   client = boto3.client('bedrock-agentcore')
   
   # List the generations for a dataset
   resp = client.list_dataset_generations(datasetId='my-dataset-id')
   for gen in resp['datasetGenerations']:
       print(f"  {gen['generationId']}: {gen['status']}")
   
   # Delete a generation record (terminal state only)
   client.delete_dataset_generation(
       datasetId='my-dataset-id',
       generationId='weeknight-sessions-abcd123456'
   )
   ```

1. 

   ```bash
   aws bedrock-agentcore list-dataset-generations \
       --dataset-id my-dataset-id
   
   aws bedrock-agentcore delete-dataset-generation \
       --dataset-id my-dataset-id \
       --generation-id weeknight-sessions-abcd123456
   ```