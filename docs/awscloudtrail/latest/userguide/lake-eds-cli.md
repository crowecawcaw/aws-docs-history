# Create, update, and manage event data stores with the AWS CLI

This section describes the AWS CLI commands you can use to create, update, and manage your CloudTrail Lake event data stores.

When using the AWS CLI,
 remember that your commands run in the AWS Region configured for your profile. If
 you want to run the commands in a different Region, either change the default Region for
 your profile, or use the **--region** parameter with the command.


## Available commands for event data stores


Commands for creating and updating event data stores in CloudTrail Lake include:



* `create-event-data-store` to create an event data store.
* `get-event-data-store` to return information about the event data store 
 including the advanced event selectors configured for the event data store.
* `update-event-data-store` to change the configuration of an
 existing event data store.
* `list-event-data-stores` to list the event data stores.
* `delete-event-data-store` to delete an event data store.
* `restore-event-data-store` to restore an event data store that is pending deletion.
* `start-import` to start an import of trail events to an event data store, or retry a failed import.
* `get-import` to return information about a specific import.
* `stop-import` to stop an import of trail events to an event data store.
* `list-imports` to return information on all imports, or a select set of imports by `ImportStatus` or `Destination`.
* `list-import-failures` to list import failures for the specified import.
* `stop-event-data-store-ingestion` to stop event ingestion on an event data store.
* `start-event-data-store-ingestion` to restart event ingestion on an event data store.
* `enable-federation` to enable federation on an event data store to query the event data store in Amazon Athena.
* `disable-federation` to disable federation on an event data store. After you disable federation, 
 you can no longer query against the event data store's data in Amazon Athena. You can continue to query in CloudTrail Lake.
* `put-insight-selectors` to add or
 modify Insights event selectors for an existing event data store, and enable or disable
 Insights events.
* `get-insight-selectors` to return information about
 Insights event selectors configured for an event data store.
* `add-tags` to add one or more tags (key-value pairs) to
 an existing event data store.
* `remove-tags` to remove one or more tags from a
 event data store.
* `list-tags` to return a list of tags associated with a
 event data store.
* [get-event-configuration](lake-cli-manage-eds.md#lake-cli-get-event-configuration "lake-cli-manage-eds.md#lake-cli-get-event-configuration") to return any resource tag keys and IAM global 
 conditions keys configured for the event data store. The command also returns whether the event 
 data store is configured to collect `Standard` size events or `Large` size events.
* [put-event-configuration](lake-cli-manage-eds.md#lake-cli-put-event-configuration "lake-cli-manage-eds.md#lake-cli-put-event-configuration") to expand the event size and add or remove
 resource tag keys and IAM global condition keys. For more information, see
 [Enrich CloudTrail events by adding resource tag
 keys and IAM global condition keys](cloudtrail-context-events.md "cloudtrail-context-events.md").
* `put-resource-policy` to attach a resource-based policy to an event data store. 
 Resource-based polices allow you to control which principals can perform actions on your event data store.
 For example policies, see [Resource-based policy examples for event data stores](security_iam_resource-based-policy-examples.md#security_iam_resource-based-policy-examples-eds "security_iam_resource-based-policy-examples.md#security_iam_resource-based-policy-examples-eds").
* `get-resource-policy` to get the resource-based policy attached to an event data store.
* `delete-resource-policy` to delete the resource-based policy attached to an event data store.

For a list of available commands for CloudTrail Lake queries, see [Available commands for CloudTrail Lake queries](lake-queries-cli.md#lake-queries-cli-commands "lake-queries-cli.md#lake-queries-cli-commands").


For a list of available commands for CloudTrail Lake dashboards, see 
 [Available commands for dashboards](lake-dashboard-cli.md#lake-dashboard-cli-commands "lake-dashboard-cli.md#lake-dashboard-cli-commands").


For a list of available commands for CloudTrail Lake integrations, see [Available commands for CloudTrail Lake integrations](lake-integrations-cli.md#lake-integrations-cli-commands "lake-integrations-cli.md#lake-integrations-cli-commands").
