# Importing interactions

individually

After you complete [Creating a schema and a dataset](data-prep-creating-datasets.md "data-prep-creating-datasets.md") to create an Item interactions dataset, you can individually import one or
more new events into the dataset.
To import interaction _[events](../../../glossary/latest/reference/glos-chap.md#event "../../../glossary/latest/reference/glos-chap.md#event")_ individually, you create an _[event tracker](../../../glossary/latest/reference/glos-chap.md#event-tracker "../../../glossary/latest/reference/glos-chap.md#event-tracker")_
and then import one or more events into your Item interactions dataset. You can
import historical individual interaction events using the Amazon Personalize console,
or import historical or real-time events using the AWS Command Line Interface (AWS CLI), or the
AWS SDKs.

This section includes information about importing events with the
Amazon Personalize console. We recommend using the Amazon Personalize console to
import _only_ historical events. For
information about using the AWS CLI or the AWS SDKs to record events in
real-time, see [Recording real-time events to influence recommendations](recording-events.md "recording-events.md").

For information about how Amazon Personalize updates filters for new records and how
new records influence recommendations, see [Importing individual records into an Amazon Personalize dataset](incremental-data-updates.md "incremental-data-updates.md").

###### Topics

- [Creating an event tracker
  (console)](#event-tracker-console "#event-tracker-console")
- [Importing events
  individually (console)](#importing-interactions-console "#importing-interactions-console")

## Creating an event tracker

(console)

###### Note

If you've created an event tracker, you can skip to [Importing events
individually (console)](#importing-interactions-console "#importing-interactions-console").

Before you can import an event to an Interactions
dataset, you must create an _[event
tracker](../../../glossary/latest/reference/glos-chap.md#event-tracker "../../../glossary/latest/reference/glos-chap.md#event-tracker")_ for the dataset group.

###### To create an event tracker (console)

1. Open the Amazon Personalize console at [https://console.aws.amazon.com/personalize/home](https://console.aws.amazon.com/personalize/home "https://console.aws.amazon.com/personalize/home") and sign in to your
   account.
2. On the **Dataset groups** page, choose the
   dataset group with the Item interactions dataset that you want to import
   events to.
3. On the **Dashboard** for the dataset group, in
   **Install event ingestion SDK**, choose
   **Start**.
4. On the **Configure tracker** page, in
   **Tracker configurations**, for **Tracker
   name**, provide a name for the event tracker, and choose
   **Next**.
5. The **Install the SDK** page shows the
   **Tracking ID** for the new event tracker and
   instructions for using AWS Amplify or AWS Lambda to stream event
   data.

You can ignore this information because you're using the Amazon Personalize
console to upload event data. If you want to stream event data using
AWS Amplify or AWS Lambda in the future, you can view this
information by choosing the event tracker on the **Event
trackers** page. 6. Choose **Finish**. You can now
import events with the console (see [Importing events
individually (console)](#importing-interactions-console "#importing-interactions-console") or record events in
real time using the `PutEvents` operation (see [Recording real-time events to influence recommendations](recording-events.md "recording-events.md")).

## Importing events

individually (console)

After you create an event tracker, you can import
events individually into an Item interactions dataset. This procedure assumes you have already
created an Item interactions dataset. For information about creating datasets,
see [Creating a schema and a dataset](data-prep-creating-datasets.md "data-prep-creating-datasets.md").

###### To import events individually (console)

1. Open the Amazon Personalize console at [https://console.aws.amazon.com/personalize/home](https://console.aws.amazon.com/personalize/home "https://console.aws.amazon.com/personalize/home") and sign in to your
   account.
2. On the **Dataset groups** page, choose the
   dataset group with the Item interactions dataset that you want to import
   events to.
3. In the navigation pane, choose **datasets**.
4. On the **Datasets** page, choose the Interactions
   dataset.
5. At the top right of the dataset details page, choose
   **Modify dataset**, and choose **Create
   record**.
6. In **Create user-item interaction record(s)**
   page, for **Record input**, enter the event details
   in JSON format. The event's field names and values must match the
   schema that you used when you created the Item interactions dataset. Amazon Personalize
   provides a JSON template with field names and data types from this
   schema. You can import up to 10 events at a time.
7. Choose **Create record(s)**. In
   **Response**, the result of the import is listed
   and a success or failure message is displayed.
