Amazon Fraud Detector will no longer be open to new customers starting November 7, 2025. If you would like to use Amazon Fraud Detector,
sign up prior to that date. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker, AutoGluon, and AWS WAF.

# Prepare event data for storage

Event data that is stored internally with Amazon Fraud Detector is stored at the `Event Type` resource level.
So, all event data that are from the same event are stored in a single `Event Type`.
The stored events can later be used to train a new model or re-train an existing model. When training a model using the
stored event data, you can optionally specify a time range of events to limit the size of your training dataset.

Each time you store your data in Amazon Fraud Detector, using the Amazon Fraud Detector console, the `SendEvent` API, or the `CreateBatchImportJob` API,
Amazon Fraud Detector validates your data before storing. If your data fails validation, the event data is not stored.

**Prerequisites for storing data internally with Amazon Fraud Detector**

- To ensure that your event data passes validation and the dataset gets stored successfully, make sure you have used the
  insights provided by [Data models explorer](create-event-dataset.md#prepare-event-dataset "create-event-dataset.md#prepare-event-dataset")
  to prepare your dataset.
- Created an event type for the event data you want to store with Amazon Fraud Detector. If you haven't, follow intstructions to
  [Create an event type](create-event-type.md "create-event-type.md").

## Smart Data Validation

When you upload your dataset in Amazon Fraud Detector console for batch import, Amazon Fraud Detector uses Smart Data Validation (SDV) to validate your dataset before
importing your data. SDV scans the uploaded data file and identifies issues such as missing data, and incorrect format or data types.
In addition to validating your dataset, SDV also provides a validation report that lists all issues that were identified and suggests
actions to fix issues that are most impactful. Some of the issues identified by SDV might be critical and must be addressed before Amazon Fraud Detector
can successfully import your dataset. For more information, see [Smart Data Validation report](storing-events-batch-import.md#sdv-validation-report "storing-events-batch-import.md#sdv-validation-report").

The SDV validates your dataset at the file level and at the data (row) level. At the file level, SDV scans your data file and identifies
issues such as inadequate permissions to access the file, incorrect file size, file format, and headers (event metadata and event variables).
At the data level, SDV scans each event data (row) and identifies issues such as incorrect data format, data length, timestamp format, and
null values.

Smart Data Validation is currently available in the Amazon Fraud Detector console only and the validation is turned on by default. If you don't want Amazon Fraud Detector to use the
Smart Data Validation before importing your dataset, turn off the validation in the Amazon Fraud Detector console when uploading your dataset.

## Validating stored data when using APIs or AWS SDK

When uploading events via the `SendEvent`, `GetEventPrediction`, or `CreateBatchImportJob` API operation, Amazon Fraud Detector validates the following:

- The EventIngestion setting for that event type is ENABLED.
- Event timestamps cannot be updated. An event with a repeated event ID and different EVENT_TIMESTAMP will be treated as an error.
- Variable names and values match their expected format. For more information, see [Create a variable](create-a-variable.md "create-a-variable.md")
- Required variables are populated with a value.
- All event timestamps are not older than 18 months and are not in the future.
