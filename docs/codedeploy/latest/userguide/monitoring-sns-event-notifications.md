# Monitoring deployments with Amazon SNS event

notifications

You can add triggers to a CodeDeploy deployment group to receive notifications about events
related to deployments or instances in that deployment group. These notifications are sent
to recipients who are subscribed to an Amazon SNS topic you have made part of the trigger's
action.

You can receive notifications for CodeDeploy events in SMS messages or email messages. You can
also use the JSON data that is created when a specified event occurs in other ways, such as
sending messages to Amazon SQS queues or invoking a function in AWS Lambda. For a look at the
structure of the JSON data provided for deployment and instance triggers, see [JSON data formats for
CodeDeploy triggers](monitoring-sns-event-notifications-json-format.md "monitoring-sns-event-notifications-json-format.md").

You might choose to use triggers to receive notifications if:

- You are a developer who needs to know when a deployment fails or stops so you can
  troubleshoot it.
- You are a system administrator who needs to know how many instances fail in order
  to monitor the health of your Amazon EC2 fleet.
- You are a manager who wants an at-a-glance count of deployment and instance
  events, which you can get through filtering rules that route different types of
  notifications into folders in your desktop email client.
  You can create up to 10 triggers for each CodeDeploy deployment group, for any of the following
  event types.

| Deployment events                                                                                                                                                                                                                                                                                                                              | Instance events                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| <br>• Success <br>• Failure <br>• Started <br>• Stopped <br>• Rollback <br>• Ready¹ <br>• All deployment events                                                                                                                                                                                                                                | <br>• Success <br>• Failure <br>• Started <br>• Ready¹ <br>• All instance events                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ¹Applies to blue/green deployments only. Indicates that the latest application revision has been installed on instances in a replacement environment and traffic from the original environment can now be rerouted behind a load balancer. For more information see [Working with deployments in CodeDeploy](deployments.md "deployments.md"). | ###### Topics <br>• [Grant Amazon SNS permissions to a service role](monitoring-sns-event-notifications-permisssions.md "monitoring-sns-event-notifications-permisssions.md") <br>• [Create a trigger for a CodeDeploy event](monitoring-sns-event-notifications-create-trigger.md "monitoring-sns-event-notifications-create-trigger.md") <br>• [Edit a trigger in a deployment group](monitoring-sns-event-notifications-edit-trigger.md "monitoring-sns-event-notifications-edit-trigger.md") <br>• [Delete a trigger from a deployment group](monitoring-sns-event-notifications-delete-trigger.md "monitoring-sns-event-notifications-delete-trigger.md") <br>• [JSON data formats for triggers](monitoring-sns-event-notifications-json-format.md "monitoring-sns-event-notifications-json-format.md") |
