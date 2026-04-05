End of support notice: On March 31, 2027, AWS
will end support for AWS Service Management Connector. After March 31, 2027, you will
no longer be able to access the AWS Service Management Connector console or AWS Service Management Connector resources.
For more information, see [AWS Service Management Connector end of support](smc-end-of-support.md "smc-end-of-support.md").

# Configuring ServiceNow for integration with Support

This section shows you how to integrate Support in ServiceNow.

###### **To conﬁgure the Support integration System Properties**

1. In the navigator, enter `AWS Service
Management`.
2. Choose **System Properties**, then **Support**.
3. Set the system property, as required.

| Available settings                                                                                                                                                                                               | Description                                               |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------- |
| **Interval**, in minutes, between the execution of full<br>synchronization                                                                                                                                       | Default: **1440 min**                                     |
| \*_SQS Name_<br>• created by the CloudFormation stack. The same name must be used for all<br>accounts                                                                                                            | Default: **AwsServiceManagementConnectorForSupportQueue** |
| \*_(Advanced mode)_<br>• Enable an _intermediate table_<br>(SMC Support Case table) to synchronize data to and from Support. Use caution; enabling<br>an intermediate table replaces the default Incident table. | Default: **False**                                        |
