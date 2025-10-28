Amazon Fraud Detector will no longer be open to new customers starting November 7, 2025. If you would like to use Amazon Fraud Detector,
sign up prior to that date. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker, AutoGluon, and AWS WAF.

# Online fraud insights

Online Fraud Insights is a supervised machine learning model, which means that it uses historical examples of fraudulent and legitimate transactions to
train the model. The Online Fraud Insights model can detect fraud based on little historical data. The model’s inputs are flexible, so you can adapt it to detect
a variety of fraud risks including fake reviews, promotion abuse, and guest checkout fraud.

The Online Fraud Insights model uses an ensemble of machine learning algorithms for data enrichment, transformation, and fraud classification. As part of
the model training process, Online Fraud Insights enriches raw data elements like IP address and BIN number with third-party data such as the geolocation of
the IP address or the issuing bank for a credit card. In addition to third-party data, Online Fraud Insights uses deep learning algorithms that take into account fraud
patterns that have been seen at Amazon and AWS. These fraud patterns become input features to your model using a gradient tree boosting algorithm.

To increase performance, Online Fraud Insights optimizes the hyper parameters of the gradient tree boosting algorithm via a Bayesian optimization process. It
sequentially trains dozens of different models with varying model parameters (such as number of trees, depth of trees, and number of samples per leaf). It also uses
different optimization strategies like upweighting the minority fraud population to take care of very low fraud rates.

## Selecting data source

When training an Online Fraud Insights model, you can choose to train the model on event data that is either stored externally (outside of Amazon Fraud Detector) or
stored within Amazon Fraud Detector. The external storage Amazon Fraud Detector currently supports is Amazon Simple Storage Service (Amazon S3). If your are using external storage, your event dataset must be uploaded as a comma-separated values (CSV) format to an Amazon S3 bucket.
These data storage options are referred to within the model training configuration as EXTERNAL_EVENTS (for external storage) and INGESTED_EVENTS (for internal storage).
For more information about the available data sources and how to store data in them, see [Event data storage](event-data-storage.md "event-data-storage.md").

## Preparing data

Regardless of where you choose to store your event data (Amazon S3 or Amazon Fraud Detector), the requirements for Online Fraud Insights model type are the same.

Your dataset must contain the column header EVENT_LABEL. This variable classifies an event as fraudulent or legitimate. When using a CSV file
(external storage), you must include EVENT_LABEL for each event in the file. For internal storage, the EVENT_LABEL field is optional but all events
must be labeled to be included within a training dataset. When configuring your model training, you can choose whether to ignore unlabeled events,
assume a legitimate label for unlabeled events, or assume a fraudulent label for all unlabeled events.

## Selecting data

See [Gather event data](create-event-dataset.md#gather-event-data "create-event-dataset.md#gather-event-data")
for information on selecting data for training your Online Fraud Insights model.

The Online Fraud Insights training process samples and partitions historic data based on EVENT_TIMESTAMP. There is no need to manually sample the data and doing
so may negatively impact your model results.

## Event variables

The Online Fraud Insights model requires at least two variables, apart from the required event metadata, that has passed [data validation](create-event-dataset.md#dataset-validation "create-event-dataset.md#dataset-validation") for model training
and allows up to 100 variables per model. Generally, the more variables you provide, the better the model can differentiate between fraud and legitimate events. While the Online Fraud Insights model can support dozens of variables, including
custom variables, we recommend including IP address and email address because these variables are typically most effective at identifying the entity being evaluated.

## Validating data

As part of the training process, Online Fraud Insights will validate the dataset for data quality issues that may impact model training. After
validating the data, Amazon Fraud Detector will take appropriate action to build the best possible model. This includes issuing warnings for potential data quality
issues, automatically removing variables that have data quality issues, or issuing an error and stopping the model training process. For more information, see
[dataset validation](create-event-dataset.md#dataset-validation "create-event-dataset.md#dataset-validation").
