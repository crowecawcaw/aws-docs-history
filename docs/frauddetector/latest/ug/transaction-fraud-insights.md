Amazon Fraud Detector will no longer be open to new customers starting November 7, 2025. If you would like to use Amazon Fraud Detector,
sign up prior to that date. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker, AutoGluon, and AWS WAF.

# Transaction fraud insights

The Transaction Fraud Insights model type is designed to detect online, or card-not-present, transaction fraud.
Transaction Fraud Insights is a supervised machine learning model, which means that it uses historical examples of fraudulent and legitimate
transactions to train the model.

The Transaction Fraud Insights model uses an ensemble of machine learning algorithms for data enrichment, transformation, and fraud classification.
It leverages a feature engineering engine to create entity-level and event-level aggregates. As part of the model training process, Transaction Fraud Insights
enriches raw data elements like IP address and BIN number with third-party data such as the geolocation of the IP address or the issuing bank for a credit card.
In addition to third-party data, Transaction Fraud Insights uses deep learning algorithms that take into account fraud patterns that have been seen at Amazon and AWS
These fraud patterns become input features to your model using a gradient tree boosting algorithm.

To increase performance, Transaction Fraud Insights optimizes the hyper parameters of the gradient tree boosting algorithm via a Bayesian optimization process,
sequentially training dozens of different models with varying model parameters (such as number of trees, depth of trees, number of samples per leaf) as well as
different optimization strategies like upweighting the minority fraud population to take care of very low fraud rates.

As part of the model training process, the Transaction Fraud model’s feature engineering engine calculates values for each unique entity within your training
dataset to help improve fraud predictions. For example, during the training process, Amazon Fraud Detector computes and stores the last time an entity made a purchase
and dynamically updates this value each time you call the `GetEventPrediction` or `SendEvent` API. During a fraud prediction,
the event variables are combined with other entity and event metadata to predict whether the transaction is fraudulent.

## Selecting data source

Transaction Fraud Insights models are trained on dataset stored internally with Amazon Fraud Detector (INGESTED_EVENTS) only. This allows Amazon Fraud Detector to continuously update calculated values about
the entities you are evaluating. For more information about the available data sources, see [Event data storage](event-data-storage.md "event-data-storage.md")

## Preparing data

Before you train a Transaction Fraud Insights model, ensure that your data file contains all headers as mentioned in [Prepare event dataset](create-event-dataset.md#prepare-event-dataset "create-event-dataset.md#prepare-event-dataset").
The Transaction Fraud Insights model compares new entities that are received with the examples of fraudulent and legitimate entities in the dataset,
so it is helpful to provide many examples for each entity.

Amazon Fraud Detector automatically transforms the stored event dataset into the correct format for training. After the model has completed training,
you can review the performance metrics and determine whether you should add entities to your training dataset.

## Selecting data

By default, Transaction Fraud Insights trains on your entire stored dataset for the Event Type that you select. You can optionally set a time range to reduce
the events that are used to train your model. When setting a time range, ensure that the records that are used to train the model have had sufficient time to mature.
That is, enough time has passed to ensure legitimate and fraud records have been correctly identified. For example, for chargeback fraud, it often takes 60 days or
more to correctly identify fraudulent events. For the best model performance, ensure that all records in your training dataset are mature.

There is no need to select a time range that represents an ideal fraud rate. Amazon Fraud Detector automatically samples your data to achieve balance between
fraud rates, time range, and entity counts.

Amazon Fraud Detector returns a validation error during model training if you select a time range for which there are not enough events to successfully train a model.
For stored datasets, the EVENT_LABEL field is optional, but events must be labeled to be included in your training dataset. When configuring your model training,
you can choose whether to ignore unlabeled events, assume a legitimate label for unlabeled events, or assume a fraudulent label for unlabeled events.

## Event variables

The event type used to train the model must contain at least 2 variables, apart from required event metadata, that has passed [data validation](create-event-dataset.md#dataset-validation "create-event-dataset.md#dataset-validation")
and can contain up to 100 variables. Generally, the more variables you provide, the better the model can differentiate between fraud and legitimate events. Although the Transaction Fraud Insight model can support dozens of variables,
including custom variables, we recommend that you include IP address, email address, payment instrument type, order price, and card BIN.

## Validating data

As part of the training process, Transaction Fraud Insights validates the training dataset for data quality issues that might impact model training.
After validating the data, Amazon Fraud Detector takes appropriate action to build the best possible model. This includes issuing warnings for potential
data quality issues, automatically removing variables that have data quality issues, or issuing an error and stopping the model training process.
For more information, see [Dataset validation](create-event-dataset.md#dataset-validation "create-event-dataset.md#dataset-validation").

Amazon Fraud Detector will issue a warning but continue training a model if the number of unique entities is less than 1,500 because this can impact the quality
of the training data. If you receive a warning, review the [performance metric](training-performance-metrics.md "training-performance-metrics.md").
