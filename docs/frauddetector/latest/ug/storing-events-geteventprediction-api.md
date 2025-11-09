Amazon Fraud Detector is no longer open to new customers as of November 7, 2025. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker, AutoGluon, and AWS WAF.

# Store event data using the GetEventPredictions API operation

By default, all events sent to the `GetEventPrediction` API for evaluation are stored in Amazon Fraud Detector. This means that Amazon Fraud Detector will
automatically store event data when you generate a prediction and use that data to update calculated variables in near-real time. You can disable data storage
by navigating to the event type in the Amazon Fraud Detector console and setting **Event ingestion** OFF or updating the EventIngestion value to DISABLED using the `PutEventType` API operation. For
more information about the `GetEventPrediction` API operation, see [Fraud predictions](getting-fraud-predictions.md "getting-fraud-predictions.md").

###### Important

We highly recommend that once you enable _Event ingestion_ for an Event type, keep it enabled.
Disabling the Event ingestion for the same Event type and then generating predictions might result in inconsistent behavior.
