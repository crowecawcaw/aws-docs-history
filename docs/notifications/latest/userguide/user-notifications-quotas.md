# Quotas for AWS User Notifications

Your AWS account has default quotas, formerly referred to as limits, for each
AWS service. Unless otherwise noted, each quota is Region-specific. You can request
increases for some quotas, while other quotas can't be increased.

Your AWS account has the following quotas related to User Notifications.

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
