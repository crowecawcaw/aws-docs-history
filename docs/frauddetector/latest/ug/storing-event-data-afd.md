

Amazon Fraud Detector is no longer open to new customers as of November 7, 2025. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker, AutoGluon, and AWS WAF.

# Store your event data internally with Amazon Fraud Detector
<a name="storing-event-data-afd"></a>

You can choose to store event data in Amazon Fraud Detector and use the stored data later to train your models. By storing event data in Amazon Fraud Detector, you can train models that use auto-computed variables to improve performance, simplify model retraining, and update fraud labels to close the machine learning feedback loop. Events are stored at the Event Type resource level, so all events of the same event type are stored together in a single event type dataset. As part of defining an event type, you can optionally specify whether to store events for that event type by toggling the *Event Ingestion* setting in the Amazon Fraud Detector console. 

You can either store single events or import large number of event datasets in Amazon Fraud Detector. Single events can be streamed using the [GetEventPrediction](https://docs.aws.amazon.com/frauddetector/latest/api/API_GetEventPrediction.html) API or the [SendEvent](https://docs.aws.amazon.com/frauddetector/latest/api/API_SendEvent.html) API. Large datasets can be quickly and easily imported to Amazon Fraud Detector using the batch import feature in the Amazon Fraud Detector console or using the [CreateBatchImportJob](https://docs.aws.amazon.com/frauddetector/latest/api/API_CreateBatchImportJob.html) API.

You can use the Amazon Fraud Detector console at any time to check the number of events already stored for each event type.