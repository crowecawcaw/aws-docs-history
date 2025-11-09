Amazon Fraud Detector is no longer open to new customers as of November 7, 2025. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker, AutoGluon, and AWS WAF.

# Delete an event or event type

When you delete an event, Amazon Fraud Detector permanently deletes that event and the data associated with the event is no longer stored in Amazon Fraud Detector.

###### To delete an event that Amazon Fraud Detector has evaluated through `GetEventPrediction` API

1. Sign in to the AWS Management Console and open the Amazon Fraud Detector console at [https://console.aws.amazon.com/frauddetector](https://console.aws.amazon.com/frauddetector "https://console.aws.amazon.com/frauddetector").
2. In the left navigation pane of the console, choose **Search past
   predictions**.
3. Choose the event that you want to delete.
4. Choose **Actions**, and then choose **Delete
   event**.
5. Enter `delete`, and then choose **Delete
   event**.

###### Note

This deletes all records that are associated to that Event ID, including any event data sent to the `SendEvent` operation and any
prediction data generated through the `GetEventPrediction` operation.

To delete an event that is stored in Amazon Fraud Detector but has not been evaluated (that is, it was stored via the `SendEvent` operation),
you must make a `DeleteEvent` request and specify the Event ID and Event Type ID. If you want to delete both the event and any prediction history
associated with the event, set the value of the `deleteAuditHistory` parameter to “_true_”.
With `deleteAuditHistory` parameter set to “_true_”, the event data is available through search for up to 30 seconds
after the delete operation is completed.

###### To delete all events associated with an event type

1. In the left navigation pane of the console, choose
   **Event types**
2. Choose the event type for which you want all events deleted.
3. Navigate to **Stored events** tab and choose **Delete stored events**
   Depending on the number of stored events for the event type, it might take some time to delete all stored events. For example, a 1 GB dataset
   (approximately 1-2 million events for the average customer) takes around 2 hours to delete. During this time, new events that you send to Amazon Fraud Detector of this
   event type are not stored, but you can continue to generate fraud predictions via the `GetEventPrediction` operation.

###### To delete an event type

You cannot delete an event type that is used in a detector or a model, or has associated stored events. Before deleting an event type, you must
delete all events that are associated with that event type.

When you delete an event type, Amazon Fraud Detector permanently deletes that event type and the data is no longer stored in Amazon Fraud Detector.

1. In the left navigation pane of the Amazon Fraud Detector console, choose
   **Resources**, and then choose
   **Events**.
2. Choose the event type that you want to delete.
3. Choose **Actions**, and then choose **Delete event
   type**.
4. Enter the event type name, and then choose **Delete event
   type**.
