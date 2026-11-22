

# Redact sensitive data in generated examples

Set `redactionConfiguration` to mask sensitive data before the service writes any example. Redaction is off unless you configure it. If detection fails, the generation fails and nothing is written.
+  `identifiers` - Managed identifiers. Each one maps to a CloudWatch Logs managed data identifier, for example `EMAIL_ADDRESS`, `NAME`, `ADDRESS`, `PHONE_NUMBER_US`, `CREDIT_CARD_NUMBER`, and `IP_ADDRESS`. The list is unique and holds up to 100 identifiers. For the data types that these identifiers detect, see [Types of data that you can protect](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL-managed-data-identifiers.html) in the *Amazon CloudWatch Logs User Guide*.
+  `customDataIdentifiers` - Up to 10 entries, each `{name, regex}`. The `name` is 1 to 128 characters matching `^[A-Za-z0-9_-]+$` and can’t reuse a managed identifier name. The `regex` is 1 to 200 characters. You can use redaction with custom identifiers only and an empty `identifiers` list.

The service masks each finding with `*` characters of the same length. The mask does not indicate which identifier matched. `GetDatasetGeneration` returns a `redactionSummary` with `scenariosScanned` and a `findingCounts` count for each identifier.

**Note**  
Redaction is best effort. An empty `findingCounts` doesn’t mean that the examples contain no sensitive data. Review the generated examples before you publish a dataset version.

## Example: Redact managed and custom identifiers
<a name="dataset-generation-redaction-example"></a>

The following example masks managed identifiers and a custom pattern before any example is written.

**Example**  

1. 

   ```bash
   agentcore eval dataset-generation start \
     --dataset-id my-dataset-id \
     --name redacted-sessions \
     --scenario-type dynamic \
     --generation-config '{"sourceConfig": {"cloudWatchLogs": {"logGroupNames": ["/aws/bedrock-agentcore/runtimes/my-agent-DEFAULT"], "serviceNames": ["my-agent.DEFAULT"]}}, "redactionConfiguration": {"identifiers": ["EMAIL_ADDRESS", "PHONE_NUMBER_US", "CREDIT_CARD_NUMBER"], "customDataIdentifiers": [{"name": "Internal_Case_ID", "regex": "CASE-[0-9]{6}"}]}}'
   ```

1. 

   ```python
   import boto3
   
   client = boto3.client('bedrock-agentcore')
   
   response = client.start_dataset_generation(
       datasetId='my-dataset-id',
       name='redacted-sessions',
       scenarioType='DYNAMIC',
       source={
           'traceGeneration': {
               'sourceConfig': {
                   'cloudWatchLogs': {
                       'logGroupNames': ['/aws/bedrock-agentcore/runtimes/my-agent-DEFAULT'],
                       'serviceNames': ['my-agent.DEFAULT']
                   }
               },
               'redactionConfiguration': {
                   'identifiers': ['EMAIL_ADDRESS', 'PHONE_NUMBER_US', 'CREDIT_CARD_NUMBER'],
                   'customDataIdentifiers': [
                       {'name': 'Internal_Case_ID', 'regex': 'CASE-[0-9]{6}'}
                   ]
               }
           }
       }
   )
   print(response['generationId'])
   ```

1. 

   ```bash
   aws bedrock-agentcore start-dataset-generation \
       --dataset-id my-dataset-id \
       --name redacted-sessions \
       --scenario-type DYNAMIC \
       --source '{"traceGeneration": {"sourceConfig": {"cloudWatchLogs": {"logGroupNames": ["/aws/bedrock-agentcore/runtimes/my-agent-DEFAULT"], "serviceNames": ["my-agent.DEFAULT"]}}, "redactionConfiguration": {"identifiers": ["EMAIL_ADDRESS", "PHONE_NUMBER_US", "CREDIT_CARD_NUMBER"], "customDataIdentifiers": [{"name": "Internal_Case_ID", "regex": "CASE-[0-9]{6}"}]}}}'
   ```