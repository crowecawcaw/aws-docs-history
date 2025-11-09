# Configuring ServiceNow for integration with Support

This section shows you how to integrate Support in ServiceNow.

###### \*\*To conﬁgure the Support integration System

Properties\*\*

1. In the navigator, enter `AWS Service
Management`.
2. Choose **System Properties**, then **Support**.
3. Set the system property, as required.

| Available settings                                                                                                                                                                                               | Description                                               |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------- |
| **Interval**, in minutes, between the execution of full<br>synchronization                                                                                                                                       | Default: **1440 min**                                     |
| \*_SQS Name_<br>• created by the AWS CloudFormation stack. The same name must be used for all<br>accounts                                                                                                        | Default: **AwsServiceManagementConnectorForSupportQueue** |
| \*_(Advanced mode)_<br>• Enable an _intermediate table_<br>(SMC Support Case table) to synchronize data to and from Support. Use caution; enabling<br>an intermediate table replaces the default Incident table. | Default: **False**                                        |
