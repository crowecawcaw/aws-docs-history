Amazon Fraud Detector will no longer be open to new customers starting November 7, 2025. If you would like to use Amazon Fraud Detector,
sign up prior to that date. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker, AutoGluon, and AWS WAF.

# Event type

With Amazon Fraud Detector you generate fraud predictions for events. An event type defines the structure for an individual event sent to Amazon Fraud Detector. Once defined, you can build models and detectors that evaluate the risk for specific event types.

The structure of an event includes the following:

- Entity Type: Classifies who is performing the event. During prediction, specify the entity type and entity Id to define who performed the event.
- Variables: Defines what variables can be sent as part of the event. Variables are used by models and rules to evaluate fraud risk. Once added, variables cannot be removed from an event type.
- Labels: Classifies an event as fraudulent or legitimate. Used during model training. Once added, labels cannot be removed from an event type.
