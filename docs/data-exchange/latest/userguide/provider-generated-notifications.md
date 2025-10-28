# Provider-generated notifications in

AWS Data Exchange

As a provider in AWS Data Exchange, you can send provider-generated notifications to inform your
subscribers about important events related to your data sets. You can contact your subscribers in
a structured manner and help them to process their entitled data related events in a consistent
manner across providers.

Using provider-generated notifications, you do the following to help your subscribers:

- Send notifications for data updates, delays, schema changes, and deprecations using the
  AWS Data Exchange Console or the AWS SDK.
- Include comments and expected actions for subscribers to follow.

###### To send provider-generated notifications to subscribers, follow these steps:

1. Open and sign in to the [AWS Data Exchange
   console](https://console.aws.amazon.com/dataexchange "https://console.aws.amazon.com/dataexchange").
2. From the left navigation pane, choose **Send notification**.
3. Select your **Notification type** from the dropdown menu. Notification
   types include:
   - **Data update** – the data source has been updated.
   - **Data delay** – the data source hasn’t updated as
     expected.
   - **Schema change** – the data source will include a structural
     change.
   - **Deprecation** – the data source will no longer be
     updated.

4. Select the impacted data set from the dropdown menu and view your **Notification
   details** for the **date**, **time**, and
   **list** of subscriber actions. You can also provide location metadata for
   specifying what is affected by this event.
5. Choose **Preview notification** and publish your notification.
