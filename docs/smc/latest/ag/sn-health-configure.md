# Synchronizing AWS Health events with ServiceNow

This section shows you how to synchronize AWS Health events with ServiceNow.

1. In the ServiceNow filter navigator in the fulfiller (stand user interface)
   view, enter `AWS Service Management Connector`.
2. Choose **System Properties** and then **AWS Health**.

Configure the SQS name created by the CloudFormation stack. Note that a queue with
this name must exist in all Regions defined in any AWS accounts with the
AWS Health integration enabled. The default value is **AwsServiceManagementConnectorForHealthDashboardQueue**.

###### Note

Unless you change the SQS name in the AWS account, don't change the Amazon SQS name in the
ServiceNow scoped app (`AwsServiceManagementConnectorForHealthDashboardQueue`). 3. Review and modify the following settings as needed:

| ServiceNow settings                                  | Setting                                                                                                                                                                                                     | Description                                            | Default value |
| ---------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------ | ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| SQS queue name                                       | Name of the queue to fetch messages from. Only change this setting if you change the CloudFormation template that creates the queue.                                                                        | `AwsServiceManagementConnectorForHealthDashboardQueue` |               |
| Enable auto-creation for `issue` and `investigation` | Automatically creates a ServiceNow incident for new health events for `issue` and `investigation` types. If this setting is disabled, users can manually create incidents through the health dashboard.     | _none_                                                 |               |
| Enable auto-creation for `accountNotification`       | Automatically creates a ServiceNow change request for new health events of type `accountNotification`. If this setting is disabled, users can manually create change requests through the health dashboard. | _none_                                                 |               |
| Enable auto-creation for `scheduledChange`           | Automatically creates a ServiceNow change request for new health events of type `scheduledChange`. If this setting is disabled, users can manually create change requests through the health dashboard.     | _none_                                                 |               |
| Assignment group                                     | System ID of the default assignment group, which is the ServiceNow group that automatically assigns incidents and change requests. If this field is blank, no default group is assigned.                    | _none_                                                 |               | ###### Note The types of change requests are `Standard`, `Normal`, and `Emergency`, but custom types are also available. The default type is `Standard`. |
