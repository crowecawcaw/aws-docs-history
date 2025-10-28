Amazon Fraud Detector will no longer be open to new customers starting November 7, 2025. If you would like to use Amazon Fraud Detector,
sign up prior to that date. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker, AutoGluon, and AWS WAF.

# Fraud predictions

You can use Amazon Fraud Detector to get fraud predictions for single event in real time or get fraud predictions offline for a set of events. To generate fraud predictions for either a single event or a set of events, you will need to provide Amazon Fraud Detector with the following information:

- Fraud prediction logic
- Event metadata
  **Fraud detection logic**

Fraud prediction logic uses one or more rules to evaluate data associated with an event and then provides result and a fraud prediction score. You create your fraud prediction logic
using the following components:

- Event types - Defines structure of the event
- Models - Defines algorithm and data requirements for predicting fraud
- Variables - Represents a data element associated with the event
- Rules - Tells Amazon Fraud Detector how to interpret the variable values during fraud prediction
- Outcomes - Results generated from a fraud prediction
- Detector version - Contains fraud prediction logic for a particular event
  For more information about the components used to create fraud detection logic, see [Amazon Fraud Detector concepts](frauddetector-ml-concepts.md "frauddetector-ml-concepts.md").
  Before you start generating fraud predictions, make sure you have created and published the detector version that contains your fraud prediction logic. You can create and publish detector version using
  the Fraud Detector Console or API. For instructions on using the console, see [Get started (console)](get-started.md "get-started.md"). For instructions
  on using the API, see [Create a detector version](create-a-detector-version.md "create-a-detector-version.md").

**Event metadata**

Event metadata provides details of the event being evaluated. Each event you want to evaluate must include value for each variable in the event type associated with your detector version. In addition, your event metadata
must include the following:

- EVENT_ID – An identifier for the event. For example, if your event is an online transaction the EVENT_ID might be the transaction reference number provided to your customer.

**Important notes about EVENT_ID**

    + Must be unique for that event
    + Should represent information that is meaningful to your business
    + Must satisy the regular expression pattern : `^[0-9a-z_-]+$.`
    + Must be saved. EVENT\_ID is the reference for the event and is used to perform operations on the event such as deleting the event.
    + Appending timestamp to the EVENT\_ID is not recommended as it might cause issues when later you want to update the event, since you will need to provide the exact same EVENT\_ID.

- ENTITY_TYPE – The entity that performs the event, such as a merchant or a customer.
- ENTITY_ID - An identifier for the entity performing the event. The ENTITY_ID must satisfy the following regular expression pattern: `^[0-9a-z_-]+$`. If the ENTITY_ID is not
  available at the time of evaluation, pass the string unknown.
- EVENT_TIMESTAMP - The timestamp when the event occurred. The timestamp must be in ISO 8601 standard in UTC.
