Amazon Fraud Detector will no longer be open to new customers starting November 7, 2025. If you would like to use Amazon Fraud Detector,
sign up prior to that date. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker, AutoGluon, and AWS WAF.

# Core concepts and terms

The following is a list of core concepts and terms that are used in Amazon Fraud Detector:

**Event**

An event is your organization’s business activity
that's evaluated for fraud risk. Amazon Fraud Detector generates fraud predictions for events.

**Label**

A label classifies a single event as fraudulent or legitimate. Labels are used to train machine learning models in Amazon Fraud Detector.

**Entity**

An entity represents who is performing the event. You provide entity ID as part of your company’s fraud data to indicate the specific entity who performed the event.

**Event type**

An event type defines the structure for an event sent to Amazon Fraud Detector. This includes the data sent as part of the event, the entity
performing the event (such as a customer), and the labels that classify the event. Example event types include online payment
transactions, account registrations, and authentication.

**Entity type**

An entity type classifies the entity. Example classifications include customer, merchant, or account.

**Event dataset**

The event dataset is your company’s historical data of a specific business activity or an event. For example, your
company’s event might be online account registration. Data from a single event (registration) might include the
associated IP address, email address, billing address, and event timestamp. You provide event dataset to Amazon Fraud Detector to create and train
fraud detection models.

**Model**

A model is an output of machine learning algorithms. These algorithms are implemented in code and run on event data you provide.

**Model type**

The model type defines the algorithms, enrichments, and feature transformations that are
used during model training. It also defines the data requirements to train the model.
These definitions function to optimize your model for a specific type of
fraud. You specify the model type to use when you create your model.

**Model training**

Model training is the process of using a provided event dataset to create a model that can
predict fraudulent events. All steps in the model training process are fully automated. These steps include data validation,
data transformation, feature engineering, algorithm selection, and model optimization.

**Model score**

Model score is the evaluation result of your company’s historical fraud data. During the model training process, Amazon Fraud Detector evaluates
the dataset for fraudulent activities and generates a score between 0 and 1000. For this score, 0 represents low fraud risk whereas
1000 represents the highest fraud risk. The score itself is directly related to false positive rate (FPR).

**Model version**

A model version is an output from training a model.

**Model deployment**

Model deployment is a process for activating a model version and making it available for generating fraud predictions.

**Amazon SageMaker AI model endpoint**

In addition to building models using Amazon Fraud Detector, you can optionally use SageMaker AI-hosted model endpoints in Amazon Fraud Detector evaluations.

For more information about building a model in SageMaker AI, see [Train a
Model with Amazon SageMaker AI](../../../en_pv/sagemaker/latest/dg/train-model.md "../../../en_pv/sagemaker/latest/dg/train-model.md").

**Detector**

A detector contains the detection logic such as the model and rules
for a particular event that you want to evaluate for fraud. You create a detector using a model version.

**Detector version**

A detector can have multiple versions, with each version having a status of `Draft`,
`Active`, or `Inactive`. Only one detector version can be in `Active` status at a time.

**Variable**

A variable represents a data element associated with an event that you want to use in a fraud prediction. Variables can either
be sent with an event as part of a fraud prediction or derived, such as the output of an Amazon Fraud Detector model or Amazon SageMaker AI.

**Rule**

A rule is a condition that tells Amazon Fraud Detector how to interpret variable values during a fraud prediction. A rule consists of one or
more variables, a logic expression, and one or more outcomes. The variables used in the rule must be part of the event dataset
that the detector evaluates. Moreover each detector must have at least one rule associated with it.

**Outcome**

This is the result, or output, from a fraud prediction. Each rule that is used in a fraud prediction must specify one or more outcomes.

**Fraud prediction**

Fraud prediction is an evaluation of fraud for either a single event or a set of events. Amazon Fraud Detector generates fraud predictions for a single online event
in real time by synchronously providing a model score and an outcome based on the rules. Amazon Fraud Detector generates fraud predictions for a set of events offline.
You can use the predictions to perform an offline proof-of-concept, or to retrospectively evaluate fraud risk on an hourly, daily, or weekly basis.

**Fraud prediction explanation**

Fraud prediction explanations provide insight into how each variable impacted your model’s fraud prediction score. It provides
information about how each variable influences the risk scores in terms of magnitude (ranging from 0 to 5 with 5 being highest) and
direction (driving the score higher or lower).
