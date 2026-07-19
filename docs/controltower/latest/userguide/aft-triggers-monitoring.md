# Monitoring and traceability

Each customization execution (whether triggered by an OU change, a manual
invocation, or an account request) writes an audit record to a DynamoDB table. You can
use these records to understand why a customization ran, which accounts were affected,
and how the execution relates to other pipeline activity.

| Field                      | Description                                                                       |
| -------------------------- | --------------------------------------------------------------------------------- |
| `execution_id`             | The Step Functions execution ID                                                   |
| `timestamp`                | When the record was created                                                       |
| `target_accounts`          | List of target account IDs                                                        |
| `bypass_steps`             | Provisioning steps that were skipped                                              |
| `customization_triggers`   | Trigger context (source and destination OU)                                       |
| `trigger_source`           | Why the execution ran: `account_move`,<br>`manual`, or `account_request`          |
| `customization_request_id` | Links the provisioning and customization executions for end-to-end<br>correlation |

The `customization_request_id` allows you to correlate the triggering
event with downstream pipeline execution across both Step Functions state machines. You can use
this identifier to trace a single account move from initial detection through
customization completion.

###### Example Query audit records by trigger source

```
aws dynamodb scan \
  --table-name aft-customizations-audit \
  --filter-expression "trigger_source = :ts" \
  --expression-attribute-values '{":ts": {"S": "account_move"}}'
```
