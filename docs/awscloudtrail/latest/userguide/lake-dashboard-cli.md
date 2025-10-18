# Create, update, and manage dashboards with the AWS CLI

This section describes the AWS CLI commands you can use to create, update, and manage your CloudTrail Lake dashboards.

When using the AWS CLI,
 remember that your commands run in the AWS Region configured for your profile. If
 you want to run the commands in a different Region, either change the default Region for
 your profile, or use the `--region` parameter with the command.


## Available commands for dashboards


Commands for creating and updating dashboards in CloudTrail Lake include:



* `create-dashboard` to create a custom dashboard or enable the Highlights dashboard.
* `update-dashboard` to update a custom dashboard or the Highlights dashboard.
* `delete-dashboard` to delete a custom dashboard or the Highlights dashboard.
* `get-dashboard` returns information about the specified dashboard.
* `list-dashboards` lists all dashboards for your AWS account, or for the specified filter.
* `start-dashboard-refresh` starts a refresh of the dashboard.
* `get-resource-policy` gets the resource-based policy attached to the dashboard.
* `put-resource-policy` attaches a resource-based policy to a dashboard to allow CloudTrail to refresh the dashboard asynchronously on your behalf. 
 You also attach a resource-based policy to an event data store to allow CloudTrail 
 to run queries on the event data store to populate the data for dashboard widgets.
* `delete-resource-policy` removes the resource-based policy attached to a dashboard.
* `add-tags` adds tags to identify the dashboard.
* `remove-tags` removes tags from a dashboard.
* `list-tags` lists tags for a dashboard.

For a list of available commands for CloudTrail Lake event data stores, see [Available commands for event data stores](lake-eds-cli.md#lake-eds-cli-commands "lake-eds-cli.md#lake-eds-cli-commands").


For a list of available commands for CloudTrail Lake queries, see [Available commands for CloudTrail Lake queries](lake-queries-cli.md#lake-queries-cli-commands "lake-queries-cli.md#lake-queries-cli-commands").


For a list of available commands for CloudTrail Lake integrations, see [Available commands for CloudTrail Lake integrations](lake-integrations-cli.md#lake-integrations-cli-commands "lake-integrations-cli.md#lake-integrations-cli-commands").


**Topics:**



* [Create a dashboard with the AWS CLI](lake-dashboard-cli-create.md "lake-dashboard-cli-create.md")
* [Manage dashboards with the AWS CLI](lake-dashboard-cli-manage.md "lake-dashboard-cli-manage.md")
* [Delete a dashboard with the AWS CLI](lake-dashboard-cli-delete.md "lake-dashboard-cli-delete.md")
