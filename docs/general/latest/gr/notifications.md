# AWS User Notifications endpoints and quotas

The following are the service quotas for this service. Service quotas, also referred to as limits, are the maximum number
of service resources or operations for your AWS account. For more information, see [AWS service quotas](aws_service_limits.md "aws_service_limits.md").

###### Note

Service endpoints are not currently available for this service.

## Service quotas

| Name                                                   | Default                                                                                    | Adjustable | Description                                                                                                         |
| ------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ---------- | ------------------------------------------------------------------------------------------------------------------- |
| Notification configurations total for an AWS account   | 50 notification configurations.                                                            | No         | The maximum number of notification configurations that you can create in an AWS account.                            |
| Notification configurations for a single Service       | 20 notification configurations for any specific service for an AWS account.                | No         | The maximum number of notification configurations that you can create for a given service in an AWS account.        |
| Notification configurations per Service and Event type | 10 notification configurations for each service and event type for an AWS account.         | No         | The maximum number of notification configurations by Service and Event type you can create for a given AWS account. |
| Event rules for a given notification configuration     | 10 event rules                                                                             | No         | The maximum number of event rules that you can create for each notification configuration in your AWS account.      |
| Channels for a given notification configuration        | 50 channels (email, mobile devices, or chat channels) for each notification configuration. | No         | The maximum number of channels for each notification configuration that you can create in your AWS account.         |
| Email contacts                                         | 500 email contacts for each AWS account.                                                   | No         | The maximum number of email contacts that you can add for each AWS account.                                         |
| Notification hubs                                      | 3 hubs for each AWS account.                                                               | No         | The maximum number of notification hubs you can add to each AWS account.                                            |
| Rate of source events for a given AWS account          | 1 per second.                                                                              | No         | The maximum number of source events per second you can receive in each AWS account.                                 |
