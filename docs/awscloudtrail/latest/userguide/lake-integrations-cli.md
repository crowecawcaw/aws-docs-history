# Create, update, and manage CloudTrail Lake integrations with the AWS CLI

This section describes the commands you can use to create, update and manage your CloudTrail Lake integrations using the AWS CLI.

When using the AWS CLI,
 remember that your commands run in the AWS Region configured for your profile. If
 you want to run the commands in a different Region, either change the default Region for
 your profile, or use the **--region** parameter with the command.


## Available commands for CloudTrail Lake integrations


Commands for creating, updating, and managing integrations in CloudTrail Lake include:



* `create-event-data-store` to create an event data store for events outside of AWS.
* `delete-channel` to delete a channel used for an integration.
* `delete-resource-policy` to delete the resource policy attached to a channel for a CloudTrail Lake integration.
* `get-channel` to return information about a CloudTrail channel.
* `get-resource-policy` to retrieve the JSON text of the resource-based policy document attached to the CloudTrail channel.
* `list-channels` to list the channels in the current account, and their source names.
* `put-audit-events` to ingest your application events into CloudTrail Lake. A required parameter, `auditEvents`, accepts the JSON records (also called payload) 
 of events that you want CloudTrail to ingest. You can add up to 100 of these events (or up to 1 MB) per `PutAuditEvents` request.
* `put-resource-policy` to attach a resource-based permission policy to a CloudTrail channel that is used for an 
 integration with an event source outside of AWS. For more information about resource-based policies, 
 see [AWS CloudTrail resource-based policy examples](security_iam_resource-based-policy-examples.md "security_iam_resource-based-policy-examples.md").
* `update-channel` to update a channel specified by a required channel ARN or UUID.

For a list of available commands for CloudTrail Lake event data stores, see [Available commands for event data stores](lake-eds-cli.md#lake-eds-cli-commands "lake-eds-cli.md#lake-eds-cli-commands").


For a list of available commands for CloudTrail Lake queries, see [Available commands for CloudTrail Lake queries](lake-queries-cli.md#lake-queries-cli-commands "lake-queries-cli.md#lake-queries-cli-commands").


For a list of available commands for CloudTrail Lake dashboards, see 
 [Available commands for dashboards](lake-dashboard-cli.md#lake-dashboard-cli-commands "lake-dashboard-cli.md#lake-dashboard-cli-commands").
