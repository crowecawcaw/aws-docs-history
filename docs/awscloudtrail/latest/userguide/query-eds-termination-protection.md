# Change termination protection with the console

###### Note

AWS CloudTrail Lake will no longer be open to new customers starting May 31, 2026.
If you would like to use CloudTrail Lake, sign up prior to that date. Existing customers
can continue to use the service as normal. For more information, see
[CloudTrail Lake availability change](cloudtrail-lake-service-availability-change.md "cloudtrail-lake-service-availability-change.md").

By default, event data stores in AWS CloudTrail Lake are configured with termination
protection enabled. Termination protection prevents an event data store from
accidental deletion. If you want to delete the event data store, you must
disable termination protection. You can disable termination protection by using
the AWS Management Console, AWS CLI, or API operations.

###### To turn off termination protection

1. Sign in to the AWS Management Console and open the CloudTrail console at
   [https://console.aws.amazon.com/cloudtrail/](https://console.aws.amazon.com/cloudtrail/ "https://console.aws.amazon.com/cloudtrail/").
2. In the navigation pane, under **Lake**, choose
   **Event data stores**.
3. Choose the event data store.
4. From **Actions**, choose **Change termination
   protection**.
5. Choose **Disabled**.
6. Choose **Save**. You can now [delete the event data
   store](query-event-data-store-delete.md "query-event-data-store-delete.md").

###### To turn on termination protection

1. Sign in to the AWS Management Console and open the CloudTrail console at
   [https://console.aws.amazon.com/cloudtrail/](https://console.aws.amazon.com/cloudtrail/ "https://console.aws.amazon.com/cloudtrail/").
2. In the navigation pane, under **Lake**, choose
   **Event data stores**.
3. Choose the event data store.
4. From **Actions**, choose **Change termination
   protection**.
5. To turn on termination protection, choose
   **Enabled**.
6. Choose **Save**.
