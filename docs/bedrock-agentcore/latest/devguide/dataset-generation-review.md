

# Review generated examples

Generated examples are in the Draft. To list only the examples that a generation produced, call `ListDatasetExamples` with a `generationIds` filter that holds the generation ID. After you review the examples, publish the Draft as a version with `CreateDatasetVersion`. For more information, see [Manage dataset examples](datasets-examples.md) and [Manage dataset versions](datasets-versions.md).

To change the generated examples before you publish, edit or delete them with the standard example operations. To remove every example from a generation, list them with the `generationIds` filter and call `DeleteDatasetExamples`.

**Example**  

1. 

   ```bash
   # Download the Draft, including the generated examples
   agentcore eval dataset get \
     --id my-dataset-id \
     --file-path my_dataset.jsonl
   
   # Publish the Draft as a version after you review the examples
   agentcore eval dataset publish --id my-dataset-id
   ```

   The AgentCore CLI doesn’t filter by generation, so `agentcore eval dataset get --file-path` downloads every example in the Draft. To find the generated examples in the file, look for the generation ID in `metadata.generation_id`.
**Important**  
 `agentcore eval dataset update` replaces the Draft with the contents of your file. If you edit a file that you downloaded before the generation ran, `update` deletes the generated examples. After the generation completes, download the Draft again and edit that file.

1. 

   ```python
   import boto3
   
   client = boto3.client('bedrock-agentcore-control')
   
   generation_id = 'weeknight-sessions-abcd123456'
   
   # A filtered page can be empty and still return a nextToken, so page until nextToken is absent.
   # Send the same filter on every page.
   example_filter = {'generationIds': [generation_id]}
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
   
   # Publish the Draft as a version after you review the examples
   client.create_dataset_version(datasetId='my-dataset-id')
   ```

1. 

   ```bash
   aws bedrock-agentcore-control list-dataset-examples \
       --dataset-id my-dataset-id \
       --filter '{"generationIds": ["weeknight-sessions-abcd123456"]}'
   
   aws bedrock-agentcore-control create-dataset-version \
       --dataset-id my-dataset-id
   ```