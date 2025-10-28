# Configuring ServiceNow for integration with Support

This section shows you how to integrate Support in ServiceNow.

###### \*\*To conﬁgure the Support integration System

Properties\*\*

1. In the navigator, enter `AWS Service
Management`.
2. Choose **System Properties**, then **Support**.
3. Set the system property, as required.

| Available settings                                                                                                                                                                                    | Description                                               |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------- |
| **Interval**, in minutes, between the execution of full synchronization                                                                                                                               | Default: **1440 min**                                     |
| **SQS Name** created by the AWS CloudFormation stack. The same name must be used for all accounts                                                                                                     | Default: **AwsServiceManagementConnectorForSupportQueue** |
| **(Advanced mode)** Enable an _intermediate table_ (SMC Support Case table) to synchronize data to and from Support. Use caution; enabling an intermediate table replaces the default Incident table. | Default: **False**                                        |
