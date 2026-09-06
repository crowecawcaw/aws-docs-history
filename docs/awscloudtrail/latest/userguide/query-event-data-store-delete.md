

# Delete an event data store with the console
<a name="query-event-data-store-delete"></a>

**Note**  
AWS CloudTrail Lake will no longer be open to new customers starting May 31, 2026. If you would like to use CloudTrail Lake, sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see [CloudTrail Lake availability change](cloudtrail-lake-service-availability-change.md).

This section describes how to delete an event data store using the CloudTrail console. For information about how to delete an event data store using the AWS CLI, see [Delete an event data store with the AWS CLI](lake-cli-delete-eds.md).

**Note**  
You can't delete an event data store if either [termination protection](query-eds-termination-protection.md) or [Lake query federation](query-enable-federation.md) is enabled. By default, CloudTrail enables termination protection to protect an event data store from being accidentally deleted.  
To delete an event data store with an event type of **Events from integration**, you must first delete the integration's channel. You can delete the channel from the integration's details page or by using the **aws cloudtrail delete-channel** command. For more information, see [Delete a channel to delete an integration with the AWS CLI](lake-cli-delete-integration.md)

**To delete an event data store**

1. Sign in to the AWS Management Console and open the CloudTrail console at [https://console.aws.amazon.com/cloudtrail/](https://console.aws.amazon.com/cloudtrail/).

1. In the navigation pane, under **Lake**, choose **Event data stores**.

1. Choose the event data store.

1. From **Actions**, choose **Delete**.

1. Type the name of the event data store to confirm that you want to delete it.

1. Choose **Delete**.

After you delete an event data store, the event data store's status changes to `PENDING_DELETION` and remains in that state for 7 days. You can [restore](query-eds-restore.md) an event data store during the 7-day wait period. While in the `PENDING_DELETION` state, an event data store isn't available for queries, and no other operations can be performed on the event data store except restore operations. An event data store that is pending deletion does not ingest events and does not incur costs. Event data stores that are pending deletion count toward the quota of event data stores that can exist in one AWS Region.