# Restore an event data store with the console

After you delete an event data store in AWS CloudTrail Lake, its status changes to
`PENDING_DELETION` and remains in that state for 7 days. During this
time, you can restore the event data store by using the AWS Management Console, AWS CLI, or the
[RestoreEventDataStore](../APIReference/API_RestoreEventDataStore.md "../APIReference/API_RestoreEventDataStore.md") API operation.

This section describes how to restore an event data store using the console. For
information about how to restore an event data store using the AWS CLI, see [Restore an event data store with the AWS CLI](lake-cli-manage-eds.md#lake-cli-restore-eds "lake-cli-manage-eds.md#lake-cli-restore-eds").

###### To restore an event data store

1. Sign in to the AWS Management Console and open the CloudTrail console at
   [https://console.aws.amazon.com/cloudtrail/](https://console.aws.amazon.com/cloudtrail/ "https://console.aws.amazon.com/cloudtrail/").
2. In the navigation pane, under **Lake**, choose
   **Event data stores**.
3. Choose the event data store.
4. From **Actions**, choose
   **Restore**.
