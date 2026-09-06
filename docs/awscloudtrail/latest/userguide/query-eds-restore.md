

# Restore an event data store with the console
<a name="query-eds-restore"></a>

**Note**  
AWS CloudTrail Lake will no longer be open to new customers starting May 31, 2026. If you would like to use CloudTrail Lake, sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see [CloudTrail Lake availability change](cloudtrail-lake-service-availability-change.md).

After you delete an event data store in AWS CloudTrail Lake, its status changes to `PENDING_DELETION` and remains in that state for 7 days. During this time, you can restore the event data store by using the AWS Management Console, AWS CLI, or the [RestoreEventDataStore](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_RestoreEventDataStore.html) API operation.

This section describes how to restore an event data store using the console. For information about how to restore an event data store using the AWS CLI, see [Restore an event data store with the AWS CLI](lake-cli-manage-eds.md#lake-cli-restore-eds).

**To restore an event data store**

1. Sign in to the AWS Management Console and open the CloudTrail console at [https://console.aws.amazon.com/cloudtrail/](https://console.aws.amazon.com/cloudtrail/).

1. In the navigation pane, under **Lake**, choose **Event data stores**.

1. Choose the event data store.

1. From **Actions**, choose **Restore**.