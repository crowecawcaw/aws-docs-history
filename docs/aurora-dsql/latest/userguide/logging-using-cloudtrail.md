# Logging Aurora DSQL operations using AWS CloudTrail

Amazon Aurora DSQL is integrated with [AWS CloudTrail](../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md "../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md"), a service
that provides a record of actions taken by a user, role, or an AWS service. There are two
types of events in CloudTrail: management events and data events. Management events are emitted to
audit AWS resource configuration changes. Data events capture the AWS resource usage typically
in the service data plane.

CloudTrail captures all API calls for Aurora DSQL as events. Aurora DSQL records console activity as
management events. It also captures authenticated connection attempts to clusters as data
events.

Using the information collected by CloudTrail, you can determine the request that was made to Aurora DSQL, the IP address from which the request was made, when it was made, the user identity making the request, and additional details.

CloudTrail is enabled by default in your AWS account when you create the account and you have
access to the CloudTrail **Event history**. The CloudTrail **Event
history** provides a viewable, searchable, downloadable, and immutable record of the
past 90 days of recorded management events in an AWS Region. For more information, see [Working
with CloudTrail Event history](../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md "../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md") in the _AWS CloudTrail User Guide_. There are no CloudTrail
charges for recording the **Event history**.

To create an ongoing record of events in your AWS account, including events for Aurora DSQL,
create a trail or an AWS CloudTrail Lake event data store (a centralized storage and analysis solution
for AWS CloudTrail events). For more information on creating trails, see [Working with CloudTrail
trails](../../../awscloudtrail/latest/userguide/cloudtrail-trails.md "../../../awscloudtrail/latest/userguide/cloudtrail-trails.md"). To learn about setting up and managing event data stores, see [CloudTrail Lake event data stores](../../../awscloudtrail/latest/userguide/query-event-data-store.md "../../../awscloudtrail/latest/userguide/query-event-data-store.md").

## Aurora DSQL management events in CloudTrail

CloudTrail [Management events](../../../awscloudtrail/latest/userguide/logging-management-events-with-cloudtrail.md#logging-management-events "../../../awscloudtrail/latest/userguide/logging-management-events-with-cloudtrail.md#logging-management-events") provide information about management operations that are performed on resources in your AWS account. These are also known as control plane operations. By default, CloudTrail captures management events in the **Event history**.

Amazon Aurora DSQL logs all Aurora DSQL control plane operations as management events. For a list of
the Amazon Aurora DSQL control plane operations that Aurora DSQL logs to CloudTrail, see the [Aurora DSQL
API reference](CHAP_api_reference.md "CHAP_api_reference.md").

**Control plane logs**

Amazon Aurora DSQL logs the following Aurora DSQL control plane operations to CloudTrail as management events.

- [CreateCluster](../APIReference/API_CreateCluster.md "../APIReference/API_CreateCluster.md")
- [DeleteCluster](../APIReference/API_DeleteCluster.md "../APIReference/API_DeleteCluster.md")
- [GetCluster](../APIReference/API_GetCluster.md "../APIReference/API_GetCluster.md")
- [GetVpcEndpointServiceName](../APIReference/API_GetVpcEndpointServiceName.md "../APIReference/API_GetVpcEndpointServiceName.md")
- [ListClusters](../APIReference/API_ListClusters.md "../APIReference/API_ListClusters.md")
- [ListTagsForResource](../APIReference/API_ListTagsForResource.md "../APIReference/API_ListTagsForResource.md")
- [TagResource](../APIReference/API_TagResource.md "../APIReference/API_TagResource.md")
- [UntagResource](../APIReference/API_UntagResource.md "../APIReference/API_UntagResource.md")
- [UpdateCluster](../APIReference/API_UpdateCluster.md "../APIReference/API_UpdateCluster.md")

**Backup and restore logs**

Amazon Aurora DSQL logs the following Aurora DSQL backup and restore operations to CloudTrail as management
events.

- `StartBackupJob`
- `StopBackupJob`
- `GetBackupJob`
- `StartRestoreJob`
- `StopRestoreJob`
- `GetRestoreJob`

For more on protecting your Aurora DSQL clusters using AWS Backup, see [Backup and restore for Amazon Aurora DSQL](backup-aurora-dsql.md "backup-aurora-dsql.md") .

**AWS KMS** logs

Amazon Aurora DSQL logs the following AWS KMS operations to CloudTrail as management events.

- `GenerateDataKey`
- `Decrypt`

To learn more about how CloudTrail logs track requests that Aurora DSQL sends to AWS KMS on your
behalf, see [Monitoring Aurora DSQL interaction with
AWS KMS](data-encryption.md#monitoring-dsql-kms-interaction "data-encryption.md#monitoring-dsql-kms-interaction").

## Aurora DSQL data events in CloudTrail

CloudTrail [Data events](../../../awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.md#logging-data-events "../../../awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.md#logging-data-events") typically provide information about the resource operations performed
on or in a resource. These are also used to capture the service's data plane operations. Data
events are often high-volume activities. By default, CloudTrail doesn’t log data events. The CloudTrail
**Event history** doesn't record data events.

For more information about how to log data events, see [Logging data events with the AWS Management Console](../../../awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.md#logging-data-events-console "../../../awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.md#logging-data-events-console") and [Logging data events with the AWS Command Line Interface](../../../awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.md#creating-data-event-selectors-with-the-AWS-CLI "../../../awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.md#creating-data-event-selectors-with-the-AWS-CLI") in the
_AWS CloudTrail User Guide_.

Additional charges apply for data events. For more information about CloudTrail pricing, see
[AWS CloudTrail Pricing](https://aws.amazon.com/cloudtrail/pricing/ "https://aws.amazon.com/cloudtrail/pricing/").

For Aurora DSQL, CloudTrail captures any connection attempt made to an Aurora DSQL cluster as a data
event. The following table lists the Aurora DSQL resource types for which you can log data events.
The **Resource type (console)** column shows the value to choose
from the **Resource type** list on the CloudTrail console. The **resources.type value** column shows the `resources.type`
value, which you would specify when configuring advanced event selectors using the AWS CLI or
CloudTrail APIs. The **Data APIs logged to CloudTrail** column shows the API
calls logged to CloudTrail for the resource type.

| Resource type (console) | resources.type value | Data APIs logged to CloudTrail      |
| ----------------------- | -------------------- | ----------------------------------- |
| **Amazon Aurora DSQL**  | `AWS::DSQL::Cluster` | • `DbConnect`<br>• `DbConnectAdmin` |

You can configure advanced event selectors to filter on the `eventName` and
`resources.ARN` fields to log only filtered events. For more information about
these fields, see [AdvancedFieldSelector](../../../awscloudtrail/latest/APIReference/API_AdvancedFieldSelector.md "../../../awscloudtrail/latest/APIReference/API_AdvancedFieldSelector.md") in the
_AWS CloudTrail API Reference_.

The following example shows how to use AWS CLI to configure
`dsql-data-events-trail` to receive data events for Aurora DSQL.

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
