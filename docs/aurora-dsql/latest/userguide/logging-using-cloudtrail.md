

# Logging Aurora DSQL operations using AWS CloudTrail
<a name="logging-using-cloudtrail"></a>

Amazon Aurora DSQL is integrated with [AWS CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html), a service that provides a record of actions taken by a user, role, or an AWS service. There are two types of events in CloudTrail: management events and data events. Management events are emitted to audit AWS resource configuration changes. Data events capture the AWS resource usage typically in the service data plane.

 CloudTrail captures all API calls for Aurora DSQL as events. Aurora DSQL records console activity as management events. It also captures authenticated connection attempts to clusters as data events.

Using the information collected by CloudTrail, you can determine the request that was made to Aurora DSQL, the IP address from which the request was made, when it was made, the user identity making the request, and additional details.

CloudTrail is enabled by default in your AWS account when you create the account and you have access to the CloudTrail **Event history**. The CloudTrail **Event history** provides a viewable, searchable, downloadable, and immutable record of the past 90 days of recorded management events in an AWS Region. For more information, see [Working with CloudTrail Event history](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/view-cloudtrail-events.html) in the *AWS CloudTrail User Guide*. There are no CloudTrail charges for recording the **Event history**.

To create an ongoing record of events in your AWS account, including events for Aurora DSQL, create a trail or an AWS CloudTrail Lake event data store (a centralized storage and analysis solution for AWS CloudTrail events). For more information on creating trails, see [Working with CloudTrail trails](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-trails.html). To learn about setting up and managing event data stores, see [CloudTrail Lake event data stores](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/query-event-data-store.html).

## Aurora DSQL management events in CloudTrail
<a name="cloudtrail-management-events"></a>

 CloudTrail [Management events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-management-events-with-cloudtrail.html#logging-management-events) provide information about management operations that are performed on resources in your AWS account. These are also known as control plane operations. By default, CloudTrail captures management events in the **Event history**. 

Amazon Aurora DSQL logs all Aurora DSQL control plane operations as management events. For a list of the Amazon Aurora DSQL control plane operations that Aurora DSQL logs to CloudTrail, see the [Aurora DSQL API reference](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/CHAP_api_reference.html).

**Control plane logs**

Amazon Aurora DSQL logs the following Aurora DSQL control plane operations to CloudTrail as management events.
+ [CreateCluster](https://docs.aws.amazon.com/aurora-dsql/latest/APIReference/API_CreateCluster.html)
+ [DeleteCluster](https://docs.aws.amazon.com/aurora-dsql/latest/APIReference/API_DeleteCluster.html)
+ [GetCluster](https://docs.aws.amazon.com/aurora-dsql/latest/APIReference/API_GetCluster.html)
+ [GetVpcEndpointServiceName](https://docs.aws.amazon.com/aurora-dsql/latest/APIReference/API_GetVpcEndpointServiceName.html)
+ [ListClusters](https://docs.aws.amazon.com/aurora-dsql/latest/APIReference/API_ListClusters.html)
+ [ListTagsForResource](https://docs.aws.amazon.com/aurora-dsql/latest/APIReference/API_ListTagsForResource.html)
+ [TagResource](https://docs.aws.amazon.com/aurora-dsql/latest/APIReference/API_TagResource.html)
+ [UntagResource](https://docs.aws.amazon.com/aurora-dsql/latest/APIReference/API_UntagResource.html)
+ [UpdateCluster](https://docs.aws.amazon.com/aurora-dsql/latest/APIReference/API_UpdateCluster.html)

**CDC stream logs**

Amazon Aurora DSQL logs the following CDC stream operations to CloudTrail as management events. For more information about CDC streams, see [Change data capture (CDC) streams](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/cdc-streams.html).
+ [CreateStream](https://docs.aws.amazon.com/aurora-dsql/latest/APIReference/API_CreateStream.html)
+ [DeleteStream](https://docs.aws.amazon.com/aurora-dsql/latest/APIReference/API_DeleteStream.html)
+ [GetStream](https://docs.aws.amazon.com/aurora-dsql/latest/APIReference/API_GetStream.html)
+ [ListStreams](https://docs.aws.amazon.com/aurora-dsql/latest/APIReference/API_ListStreams.html)

**Backup and restore logs**

Amazon Aurora DSQL logs the following Aurora DSQL backup and restore operations to CloudTrail as management events. 
+ `StartBackupJob`
+ `StopBackupJob`
+ `GetBackupJob`
+ `StartRestoreJob`
+ `StopRestoreJob`
+ `GetRestoreJob`

For more on protecting your Aurora DSQL clusters using AWS Backup, see [Backup and restore for Amazon Aurora DSQL](backup-aurora-dsql.md) .

**AWS KMS** logs

Amazon Aurora DSQL logs the following AWS KMS operations to CloudTrail as management events.
+ `GenerateDataKey`
+ `Decrypt`

To learn more about how CloudTrail logs track requests that Aurora DSQL sends to AWS KMS on your behalf, see [Monitoring Aurora DSQL interaction with AWS KMS](data-encryption.md#monitoring-dsql-kms-interaction).

## Aurora DSQL data events in CloudTrail
<a name="CloudTrail-data-events"></a>

CloudTrail [Data events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html#logging-data-events) typically provide information about the resource operations performed on or in a resource. These are also used to capture the service's data plane operations. Data events are often high-volume activities. By default, CloudTrail doesn’t log data events. The CloudTrail **Event history** doesn't record data events.

For more information about how to log data events, see [Logging data events with the AWS Management Console](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html#logging-data-events-console) and [Logging data events with the AWS Command Line Interface](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html#creating-data-event-selectors-with-the-AWS-CLI) in the *AWS CloudTrail User Guide*.

Additional charges apply for data events. For more information about CloudTrail pricing, see [AWS CloudTrail Pricing](https://aws.amazon.com/cloudtrail/pricing/).

For Aurora DSQL, CloudTrail captures any connection attempt made to an Aurora DSQL cluster as a data event. The following table lists the Aurora DSQL resource types for which you can log data events. The **Resource type (console)** column shows the value to choose from the **Resource type** list on the CloudTrail console. The **resources.type value** column shows the `resources.type` value, which you would specify when configuring advanced event selectors using the AWS CLI or CloudTrail APIs. The **Data APIs logged to CloudTrail** column shows the API calls logged to CloudTrail for the resource type. 


| Resource type (console) | resources.type value | Data APIs logged to CloudTrail | 
| --- | --- | --- | 
| Amazon Aurora DSQL | `AWS::DSQL::Cluster` |  +  `DbConnect` <br />+  `DbConnectAdmin`   | 

You can configure advanced event selectors to filter on the `eventName` and `resources.ARN` fields to log only filtered events. For more information about these fields, see [AdvancedFieldSelector](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_AdvancedFieldSelector.html) in the *AWS CloudTrail API Reference*.

The following example shows how to use AWS CLI to configure `dsql-data-events-trail` to receive data events for Aurora DSQL.

```
aws cloudtrail put-event-selectors \
--region us-east-1 \
--trail-name dsql-data-events-trail \
--advanced-event-selectors '[{
"Name": "Log DSQL Data Events",
    "FieldSelectors": [
       { "Field": "eventCategory", "Equals": ["Data"] },
       { "Field": "resources.type", "Equals": ["AWS::DSQL::Cluster"] } ]}]'
```