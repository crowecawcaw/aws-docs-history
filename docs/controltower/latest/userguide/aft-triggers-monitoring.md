

# Monitoring and traceability
<a name="aft-triggers-monitoring"></a>

Each customization execution (whether triggered by an OU change, a manual invocation, or an account request) writes an audit record to a DynamoDB table. You can use these records to understand why a customization ran, which accounts were affected, and how the execution relates to other pipeline activity.


| Field | Description | 
| --- | --- | 
| execution\_id | The Step Functions execution ID | 
| timestamp | When the record was created | 
| target\_accounts | List of target account IDs | 
| bypass\_steps | Provisioning steps that were skipped | 
| customization\_triggers | Trigger context (source and destination OU) | 
| trigger\_source | Why the execution ran: account\_move, manual, or account\_request | 
| customization\_request\_id | Links the provisioning and customization executions for end-to-end correlation | 

The `customization_request_id` allows you to correlate the triggering event with downstream pipeline execution across both Step Functions state machines. You can use this identifier to trace a single account move from initial detection through customization completion.

**Example Query audit records by trigger source**  

```
aws dynamodb scan \
  --table-name aft-customizations-audit \
  --filter-expression "trigger_source = :ts" \
  --expression-attribute-values '{":ts": {"S": "account_move"}}'
```