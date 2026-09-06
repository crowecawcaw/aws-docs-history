

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# Amazon Redshift Serverless event notifications with Amazon EventBridge
<a name="serverless-event-notifications-eventbridge"></a>

Amazon Redshift Serverless uses Amazon EventBridge to manage event notifications to keep you up-to-date regarding changes in your data warehouse. Amazon EventBridge is a serverless event bus service that you can use to connect your applications with data from a variety of sources. In this case, the event source is Amazon Redshift. Events, which are monitored changes in an environment, are sent to EventBridge from your Amazon Redshift data warehouse automatically. Events are delivered in near-real time.

Capabilities of EventBridge include providing an environment for you to write event rules, which can specify actions to take for specific events. You can also set up targets, which are resources that EventBridge can send an event to. A target can include an API destination, an Amazon CloudWatch log group, and others. For more information about rules, see [Amazon EventBridge rules](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-rules.html). For more information about targets, see [Amazon EventBridge targets](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-targets.html).

Events can be classified into severities and categories. The following filters are available:
+ *Resource filtering* – Receive messages based on the resource the events are associated with. Resources include a workgroup, a snapshot, and so on.
+ *Time window filtering* – Scope events in a specific time period.
+ *Category filtering* – Receive event notifications for all events in specified categories.

The following table includes Amazon Redshift Serverless events, with additional metadata:


| Amazon Redshift Category | External Event ID | Event Severity | Message Description | 
| --- | --- | --- | --- | 
| RateChange | REDSHIFT-SERVERLESS-EVENT-1001 | INFO | Workgroup base RPU change completed successfully at <time in UTC>. | 
| RateChange | REDSHIFT-SERVERLESS-EVENT-1002 | ERROR | Workgroup base RPU change failed to complete at <time in UTC>. | 
| Monitoring | REDSHIFT-SERVERLESS-EVENT-1003 | INFO | The software was updated on your Amazon Redshift Data Warehouse <endpoint name> at <time in UTC>. | 
| Configuration | REDSHIFT-SERVERLESS-EVENT-1011 | ERROR | Amazon Redshift Serverless couldn't create workgroup [workgroup name] because the Service Linked Role (SLR) necessary for this operation is inaccessible. Try creating it again on the Amazon Redshift console. Amazon Redshift will create the SLR automatically. | 
| Monitoring | REDSHIFT-SERVERLESS-EVENT-1029 | ERROR | Workgroup base RPU change failed to complete at [time in UTC] because it doesn't have enough disk space available. Try again with a different configuration. | 
| Monitoring | REDSHIFT-SERVERLESS-EVENT-1500 | ERROR | Workgroup <workgroup name> cannot be created or updated because you exceeded your account's limit of Elastic IP addresses. Delete unused Elastic IP addresses or request a limit increase with Amazon EC2. | 
| Monitoring | REDSHIFT-SERVERLESS-EVENT-1501 | ERROR | Subnet <subnet id> has no available IP addresses. This will prevent the following query types from running successfully on workgroup <workgroup name>: EMR, federated queries, COPY/UNLOAD from Amazon EC2. To correct the issue, free up IPs in your subnet by deleting ENIs. | 
| Monitoring | REDSHIFT-SERVERLESS-EVENT-1502 | ERROR | Subnet <subnet id> has no available IP addresses. This will prevent the Amazon EMR, Redshift federated queries, Redshift COPY/UNLOAD, Redshift ML query types from running successfully in workgroup <workgroup name>. To correct the issue, free up IPs in your subnet by deleting unused elastic network interfaces (ENIs). | 
| Management | REDSHIFT-SERVERLESS-EVENT-1008 | INFO | Your Amazon Redshift workgroup <workgroup name> has been created and is ready for use. | 
| Management | REDSHIFT-SERVERLESS-EVENT-1009 | INFO | Your Amazon Redshift workgroup <workgroup name> was deleted at <time in UTC>. | 
| Monitoring | REDSHIFT-SERVERLESS-EVENT-1000 | INFO | Snapshot <snapshot name> completed successfully at <time in UTC>. | 
| Management | REDSHIFT-SERVERLESS-EVENT-1004 | INFO | Restore from snapshot on namespace <namespace name> completed successfully at <time in UTC>. | 
| Management | REDSHIFT-SERVERLESS-EVENT-1005 | ERROR | Restore from snapshot on namespace <namespace name> failed at <time in UTC>. | 
| Management | REDSHIFT-SERVERLESS-EVENT-1006 | INFO | Restore from recovery point on namespace <namespace name> completed successfully at <time in UTC>. | 
| Management | REDSHIFT-SERVERLESS-EVENT-1007 | INFO | Restore from recovery point on namespace <namespace name> failed at <time in UTC>. | 
| Security | REDSHIFT-SERVERLESS-EVENT-1012 | ERROR | Amazon Redshift can't access the secret for your namespace <namespace name>. | 
| Security | REDSHIFT-SERVERLESS-EVENT-1013 | ERROR | Amazon Redshift can't access the KMS key that was used to encrypt the admin credentials secret for your namespace <namespace name>. | 
| Security | REDSHIFT-SERVERLESS-EVENT-1014 | ERROR | Amazon Redshift can't rotate the secret for your namespace <namespace name> because there's an ongoing operation on the workgroup. | 
| Security | REDSHIFT-SERVERLESS-EVENT-1015 | ERROR | Your namespace <namespace name> doesn't have a workgroup attached to it. Amazon Redshift can only rotate secrets for namespaces with workgroups attached to them. | 
| Security | REDSHIFT-SERVERLESS-EVENT-1016 | INFO | Admin credentials updated for your namespace <namespace name> at <time in UTC>. | 
| Security | REDSHIFT-SERVERLESS-EVENT-1030 | INFO | The operation to register your Amazon Redshift namespace <namespace name> to Glue Data Catalog account <account id> was started at <time in UTC>. | 
| Security | REDSHIFT-SERVERLESS-EVENT-1031 | INFO | The operation to register your Amazon Redshift namespace <namespace name> to Glue Data Catalog account <account id> has successfully completed at <time in UTC<. | 
| Security | REDSHIFT-SERVERLESS-EVENT-1032 | INFO | The operation to register your Amazon Redshift namespace <namespace name> to Glue Data Catalog account <account id> has failed at <time in UTC>.. | 
| Security | REDSHIFT-SERVERLESS-EVENT-1033 | INFO | The operation to deregister your Amazon Redshift namespace <namespace name> from Glue Data Catalog account <account id> was started at <time in UTC>. | 
| Security | REDSHIFT-SERVERLESS-EVENT-1034 | INFO | The operation to deregister your Amazon Redshift namespace <namespace name> from Glue Data Catalog account <account id> has successfully completed at <time in UTC>. | 
| Security | REDSHIFT-SERVERLESS-EVENT-1035 | INFO | The operation to deregister your Amazon Redshift namespace <namespace name> from Glue Data Catalog account <account id> has failed at <time in UTC>. | 
| Management | REDSHIFT-SERVERLESS-EVENT-1036 | ERROR | The customer-initiated track update failed on your Redshift Serverless workgroup <workgroup name>. Returning the workgroup back to its original track. | 
| Management | REDSHIFT-SERVERLESS-EVENT-1037 | ERROR | The track update failed on your Redshift Serverless workgroup <workgroup name>. The track update failed for your Amazon Redshift Serverless workgroup because the workgroup was busy at the time. As a result, the workgroup has been returned to its original track. To retry the track update, please wait for a time of lower activity on the workgroup, and then attempt to update the track again. | 
| Management | REDSHIFT-SERVERLESS-EVENT-1038 | INFO | Your Amazon Redshift workgroup <workgroup name> track has been modified. The track change completed. | 
| Namespace | REDSHIFT-SERVERLESS-EVENT-1039 | ERROR | Namespace <namespace name> has invalid AWS KMS key permissions. Your namespace will enter an "INACCESSIBLE\_KMS\_KEY" state and you will no longer be able to access it. | 
| Namespace | REDSHIFT-SERVERLESS-EVENT-1040 | INFO | Namespace <namespace name> has now been restored to its previous state because AWS KMS key permissions have been restored. | 
| Namespace | REDSHIFT-SERVERLESS-EVENT-1045 | INFO | Datashare <datashare name> on your Redshift Serverless namespace <namespace name> was dropped due to serverless restore. | 
| Namespace | REDSHIFT-SERVERLESS-EVENT-1046 | INFO | Consumer <consumer principle id> for datashare <datashare name> on your Redshift Serverless namespace <namespace name> was revoked due to serverless restore. | 
| Namespace | REDSHIFT-SERVERLESS-EVENT-1047 | INFO | Public accessibility changed for datashare <datashare name> on your Redshift Serverless namespace <namespace name> due to serverless restore. | 
| Security | REDSHIFT-SERVERLESS-EVENT-1048 | ERROR | Your request to opt-out of the Redshift-Secrets Manager integration for namespace <namespace name> failed because of an internal issue. Retry the opt-out operation manually to resolve this issue. | 
| Security | REDSHIFT-SERVERLESS-EVENT-1049 | ERROR | Your request to opt-in to the Redshift-Secrets Manager integration for namespace <namespace name> could not complete successfully due to an internal issue. Rotate the secret associated with your Redshift Serverless namespace manually to resolve this issue. | 
| Security | REDSHIFT-SERVERLESS-EVENT-1050 | ERROR | Your request to reset the admin credentials on namespace <namespace name> failed because of an internal issue. Retry the operation to reset the admin user credentials. | 