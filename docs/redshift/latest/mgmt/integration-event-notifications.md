

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# Zero-ETL integration event notifications with Amazon EventBridge
<a name="integration-event-notifications"></a>

Zero-ETL integration uses Amazon EventBridge to manage event notifications to keep you up-to-date regarding changes in your integrations. Amazon EventBridge is a serverless event bus service that you can use to connect your applications with data from a variety of sources. In this case, the event source is Amazon Redshift. Events, which are monitored changes in an environment, are sent to EventBridge from your Amazon Redshift data warehouse automatically. Events are delivered in near real time.

EventBridge provides an environment for you to write event rules, which can specify actions to take for specific events. You can also set up targets, which are resources that EventBridge can send an event to. A target can include an API destination, an Amazon CloudWatch log group, and others. For more information about rules, see [Amazon EventBridge rules](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-rules.html). For more information about targets, see [Amazon EventBridge targets](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-targets.html).

Events can be classified into severities and categories. The following filters are available:
+ *Resource filtering* – Receive messages based on the resource that the events are associated with. Resources include a workgroup or a snapshot.
+ *Time window filtering* – Scope events in a specific time period.
+ *Category filtering* – Receive event notifications for all events in specified categories.

The following table includes zero-ETL integration events, with additional metadata:


| Amazon Redshift Category | External Event ID | Event Severity | Message Description | 
| --- | --- | --- | --- | 
| Monitoring | REDSHIFT-INTEGRATION-EVENT-0000 | INFO | Your zero-ETL Integration <integration name> has been created and became ACTIVE at <time in UTC>. | 
| Monitoring | REDSHIFT-INTEGRATION-EVENT-0001 | INFO | Your zero-ETL Integration <integration name> has been deleted at <time in UTC>. | 
| Monitoring | REDSHIFT-INTEGRATION-EVENT-0002 | INFO | Your zero-ETL Integration <integration name> has initiated deletion at <time in UTC>. | 
| Monitoring | REDSHIFT-INTEGRATION-EVENT-0003 | INFO | Your zero-ETL Integration <integration name> is synchronizing transactional data to the Amazon Redshift data warehouse. | 
| Monitoring | REDSHIFT-INTEGRATION-EVENT-0004 | WARNING | Amazon Redshift cannot replicate the table because the table is missing a primary key. Add primary key(s) to the source table and the table will resynchronize automatically. | 
| Monitoring | REDSHIFT-INTEGRATION-EVENT-0005 | WARNING | Amazon Redshift cannot replicate the table because one or more columns use an unsupported data type. Modify your integration to exclude this table in the filter, or drop column(s) from source table and run 'ALTER DATABASE <Redshift database name> INTEGRATION REFRESH TABLE <schema name>.<table name>' to synchronize this table. | 
| Monitoring | REDSHIFT-INTEGRATION-EVENT-0006 | ERROR | Unable to create integration. Delete and recreate the integration. If the error persists, contact AWS Support. | 
| Monitoring | REDSHIFT-INTEGRATION-EVENT-0007 | ERROR | Unable to load data due to an internal error. Delete and recreate the integration. If the error persists, contact AWS Support. | 
| Monitoring | REDSHIFT-INTEGRATION-EVENT-0008 | ERROR | Authorization failed because permissions have been revoked from the source DB cluster. Check the KMS key permission if you're using a customer-managed key (CMK) to encrypt the integration. Then, delete and recreate the integration. | 
| Monitoring | REDSHIFT-INTEGRATION-EVENT-0009 | ERROR | Unable to send data to Amazon Redshift because the number of tables and schemas exceed the Amazon Redshift limit. Delete and recreate the integration. | 
| Monitoring | REDSHIFT-INTEGRATION-EVENT-0012 | ERROR | A restore from recovery point was invoked on the destination serverless namespace. Delete and recreate the integration. | 
| Monitoring | REDSHIFT-INTEGRATION-EVENT-0013 | INFO | Your zero-ETL Integration <integration name> is now ACTIVE. | 
| Monitoring | REDSHIFT-INTEGRATION-EVENT-0014 | ERROR | Your integration <integration name> is in FAILED state because we are unable to modify it due to an internal error. Delete and recreate the integration. If the error persists, contact AWS Support. | 
| Operation | REDSHIFT-INTEGRATION-EVENT-0016 | INFO | Your zero-ETL integration <integration name> is processing a modification request. | 
| Operation | REDSHIFT-INTEGRATION-EVENT-0017 | INFO | Your modification to zero-ETL integration <integration name> has been applied. | 
| Operation | REDSHIFT-INTEGRATION-EVENT-0018 | WARNING | Target Amazon Redshift cluster is being paused. Wait for the cluster to be paused and then resume the cluster to continue streaming data. | 
| Operation | REDSHIFT-INTEGRATION-EVENT-0019 | WARNING | Target Amazon Redshift cluster is paused. The cluster must be resumed in order to continue streaming data. | 
| Operation | REDSHIFT-INTEGRATION-EVENT-0020 | WARNING | Target Amazon Redshift cluster is being resumed. Wait for the cluster to be active to continue streaming data. | 
| Monitoring | REDSHIFT-INTEGRATION-EVENT-0025 | ERROR | A serverless restore was invoked on the destination serverless namespace, and your integration is deactivated because it's not available in the restored snapshot. Restore a snapshot which is created when the integration is available, or delete the integration. | 
| Configuration | REDSHIFT-INTEGRATION-EVENT-1000 | ERROR | One or more parameters on the source Aurora DB cluster are misconfigured. Fix the parameter group and reboot the cluster to apply the changes, then recreate the integration. | 
| Configuration | REDSHIFT-INTEGRATION-EVENT-1001 | ERROR | Integration failed because the value of the enable\_case\_sensitive\_identifier parameter is incorrect. Set the value to true for the source Aurora DB cluster, then delete and recreate the integration. | 
| Configuration | REDSHIFT-INTEGRATION-EVENT-1002 | ERROR | Integration failed because the value of the cdc\_insert\_enabled parameter is incorrect. Set the value to true for the source Aurora DB cluster, then delete and recreate the integration. | 
| Configuration | REDSHIFT-INTEGRATION-EVENT-1003 | ERROR | The binlog\_format parameter in the source DB cluster parameter group must be set to ROW. Fix the parameter group and reboot the cluster to apply the change, then recreate the integration. | 
| Configuration | REDSHIFT-INTEGRATION-EVENT-1004 | ERROR | Unable to load data because the binlog\_transaction\_compression cluster parameter is enabled. Set the parameter value to OFF and reboot the writer instance to apply the change, then recreate the integration. | 
| Configuration | REDSHIFT-INTEGRATION-EVENT-1005 | ERROR | Unable to load data because the binlog\_row\_value\_options cluster parameter is set to PARTIAL\_JSON, which is not supported. Fix the parameter group and reboot the writer instance to apply the change, then recreate the integration. | 
| Configuration | REDSHIFT-INTEGRATION-EVENT-1006 | WARNING | Unable to parse integration filter. Fix the filter syntax. | 