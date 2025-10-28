Amazon Fraud Detector will no longer be open to new customers starting November 7, 2025. If you would like to use Amazon Fraud Detector,
sign up prior to that date. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker, AutoGluon, and AWS WAF.

# Entity

An entity represents a person or thing that's performing the event. An entity type classifies the entity. Example classifications include customer, merchant, user, or account. You provide the entity type (ENTITY_TYPE) and an entity identifier (ENTITY_ID) as part of your event dataset to indicate the specific
entity that performed the event.

Amazon Fraud Detector uses the entity type when generating fraud prediction for an event to indicate who performed the event. The entity type you want to use in your fraud predictions must first be created in Amazon Fraud Detector and then added to the event when creating your event type.
