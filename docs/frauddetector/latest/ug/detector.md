Amazon Fraud Detector will no longer be open to new customers starting November 7, 2025. If you would like to use Amazon Fraud Detector,
sign up prior to that date. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker, AutoGluon, and AWS WAF.

# Detector

A detector is a container that contains fraud detection logic, such as the models and rules, for one specific business event that you want to evaluate for fraud.
You first create a detector by specifying the event that you have already defined and optionally add a model version that is already created and trained by Amazon Fraud Detector for the event.

You then add rules and rule execution order to a detector to create a version of the detector. A detector version defines the rules and optionally a model that will be run as part of the request for generating fraud predictions.
You can add any of the rules defined within a detector to the detector version. You can also add any model trained on the evaluated event type to the detector version. A detector can have multiple versions, with each version
having different rules and rule execution order to meet multiple use cases.

Each detector version must have a status of `DRAFT`, `ACTIVE`, or `INACTIVE`. Only one detector version can be in `ACTIVE` status at a time. Amazon Fraud Detector uses the detector version with `ACTIVE` status to generate fraud predictions.
