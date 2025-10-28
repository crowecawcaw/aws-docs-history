Amazon Fraud Detector will no longer be open to new customers starting November 7, 2025. If you would like to use Amazon Fraud Detector,
sign up prior to that date. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker, AutoGluon, and AWS WAF.

# Troubleshoot

The following sections help you troubleshoot issues that you might encounter when working with Amazon Fraud Detector

## Troubleshoot training data issues

Use information in this section to help diagnose and resolve issues you might see in the **Model training diagnostic** pane
in the Amazon Fraud Detector console when you train your model.

The issues displayed in the **Model training diagnostic** pane are categorized as follows.
The requirement to address the issue is dependent on the category of the issue.

- ![Error icon](images/Error icon.png)

**Error**- causes the model training to fail. These issues must be addressed for the model to train successfully.

- ![Warning icon](images/Warning icon.png)

**Warning**- causes the model training to continue, however, some of the variables might be getting excluded in the training process.
Check for the relevant guidance in this section to improve the quality of your dataset.

- ![Information icon](images/Info icon.png)

**Information (Info)**- has no impact on model training and all the variables are used for training.
We recommend that you check the relevant guidance in this section to further improve the quality of your dataset and model performance.

###### Topics

- [Unstable fraud rate in the given dataset](#unstable-fraud-rate "#unstable-fraud-rate")
- [Insufficient data](#insufficient-data "#insufficient-data")
- [Missing or different EVENT_LABEL values](#missing-different-event-label-values "#missing-different-event-label-values")
- [Missing or incorrect EVENT_TIMESTAMP values](#missing-incorrect-timestamp-values "#missing-incorrect-timestamp-values")
- [Data not ingested](#data-not-ingested "#data-not-ingested")
- [Insufficient variables](#insufficient-variables "#insufficient-variables")
- [Missing or incorrect variable type](#missing-incorrect-variable-type "#missing-incorrect-variable-type")
- [Missing variable values](#missing-variable-values "#missing-variable-values")
- [Insufficient unique variable values](#insufficient-unique-variable-values "#insufficient-unique-variable-values")
- [Incorrect variable expression](#incorrect-variable-expression "#incorrect-variable-expression")
- [Insufficient unique entities](#insufficient-unique-entities "#insufficient-unique-entities")

### Unstable fraud rate in the given dataset

**Issue type : Error**

**Description**

Fraud rate in the given data is too unstable through time. Please make sure your fraud and legitimate events are sampled uniformly over time.

**Cause**

This error occurs if the fraud and legitimate events in your dataset are distributed unevenly and are taken from different time slots.
Amazon Fraud Detector model training process samples and partitions your dataset based on EVENT_TIMESTAMP. For example, if your dataset consists of fraud
events pulled from last 6 months, but only the last month of legitimate events are included, the dataset is considered unstable. An unstable
dataset might lead to biases in model performance evaluation.

**Solution**

Make sure to provide the fraudulent and legitimate events data from same time slot and
the fraud rate does not change dramatically over time.

### Insufficient data

1. **Issue type : Error**

**Description**

Fewer than 50 rows are labeled as fraudulent events. Ensure that both fraudulent and
legitimate events exceed the minimum count of 50 and re-train the model.

**Cause**

This error occurs if your dataset has fewer events labeled as fraudulent than required
for model training. Amazon Fraud Detector requires at least 50 fraudulent events to train
your model.

**Solution**

Make sure that your dataset includes a minimum of 50 fraudulent events. You can ensure
this by covering a longer time period, if needed. 2. **Issue type : Error**

**Description**

Fewer than 50 rows are labeled as legitimate events. Ensure that both fraudulent and
legitimate events exceed the minimum count of $threshold and re-train the
model.

**Cause**

This error occurs if your dataset has fewer events labeled as legitimate than required
for model training. Amazon Fraud Detector requires at least 50 legitimate events to train
your model.

**Solution**

Make sure that your dataset includes a minimum of 50 legitimate events. You can ensure
this by covering a longer time period, if needed. 3. **Issue type : Error**

**Description**

The number of unique entities associated with fraud is less than 100. Consider including more examples of fraudulent entities to improve performance.

**Cause**

This error occurs if your dataset has fewer entities with fraudulent events than required for model training. The Transaction Fraud Insights (TFI) model requires
at least 100 entities with fraud events to ensure maximum coverage of the fraud space. The model may not generalize well if all fraud events are performed
by a small group of entities.

**Solution**

Make sure that your dataset includes at least 100 entities with fraudulent events. You can ensure this be covering a longer time period, if needed. 4. **Issue type : Error**

**Description**

The number of unique entities associated with legitimate is less than 100. Consider including more examples of legitimate entities to improve performance.

**Cause**

This error occurs if your dataset has fewer entities with legitimate events than required for model training. The Transaction Fraud Insights (TFI) model requires
at least 100 entities with legitimate events to ensure maximum coverage of the fraud space. The model may not generalize well if all legitimate events are performed
by a small group of entities.

**Solution**

Make sure that your dataset includes at least 100 entities with legitimate events. You can ensure this be covering a longer time period, if needed. 5. **Issue type : Error**

**Description**

Less than 100 rows are in the dataset. Ensure there are more than 100 rows in the
total dataset and at least 50 rows are labeled as fraudulent.

**Cause**

This error occurs if your dataset contains fewer than 100 records. Amazon Fraud Detector requires data
from at least 100 events (records) in your dataset for model training.

**Solution**

Make sure that you have data from more than 100 events in your dataset.

### Missing or different EVENT_LABEL values

1. **Issue type : Error**

**Description**

Greater than 1% of your EVENT_LABEL column are null or are values other than those defined in the model configuration `$label_values`.
Ensure you have less than 1% of missing values in your EVENT_LABEL column and the values are those defined in the model configuration `$label_values`.

**Cause**

This error occurs because of one of the following reasons:

    * More than 1% of the records in the CSV file containing your training data have missing values in the EVENT\_LABEL column.
    * More than 1% of the records in the CSV file containing your training data have values in the EVENT\_LABEL column that are different than those associated with your event type.

Online Fraud Insights (OFI) model requires that the EVENT_LABEL column in each record be populated with one of the labels that’s associated with your event type (or, mapped in `CreateModelVersion`).

**Solution**

If this error is due to the missing EVENT_LABEL values, consider assigning proper labels to those records or dropping those records from your dataset.
If this error is because labels of some records are not among `label_values`, make sure to add all the values in EVENT_LABEL column
to labels of the event type and mapped to either fraudulent or legitimate (fraud, legit) in model creation. 2. **Issue type : Information**

**Description**

Your EVENT_LABEL column contains null values or label values other than those defined in the model configuration `$label_values`. These inconsistent values were converted to 'not fraud' prior to training.

**Cause**

You get this information because of one of the following reasons:

    * Less than 1% of the records in the CSV file containing your training data have missing values in the EVENT\_LABEL column
    * Less than 1% of the records in the CSV file containing your training data have values in the EVENT\_LABEL column that are different than those associated with your event type.

The model training in both the cases will succeed. However, the label values of those events that have missing or unmapped label values are converted to legitimate. If you consider this to be an issue, follow solution provided below.

**Solution**

If there are missing EVENT_LABEL values in your dataset, consider dropping those records from your dataset. If the values provided for
those EVENT_LABELS are not mapped, make sure that all those values are mapped to either fraudulent or legitimate (fraud, legit) for each event.

### Missing or incorrect EVENT_TIMESTAMP values

1. **Issue type : Error**

**Description**

Your training data set contains EVENT_TIMESTAMP with timestamps that do not conform to accepted formats. Ensure the format is one of the accepted date/timestamp formats.

**Cause**

This error occurs if the EVENT_TIMESTAMP column contains value that doesn’t comply with the [timestamp formats](online-fraud-insights.md#timestamp-formats "online-fraud-insights.md#timestamp-formats") that are supported by Amazon Fraud Detector.

**Solution**

Ensure that the values provided for the EVENT_TIMESTAMP column is compliant with the supported [timestamp formats](online-fraud-insights.md#timestamp-formats "online-fraud-insights.md#timestamp-formats"). If you have missing values in
the EVENT_TIMESTAMP column, you can either backfill those with values using the supported timestamp format or consider dropping the event completely instead of entering strings such as `none`, `null`, or `missing`. 2. **Issue type : Error**

Your training data set contains EVENT_TIMESTAMP with missing values. Ensure you have no missing values.

**Cause**

This error occurs if the EVENT_TIMESTAMP column in your dataset has missing values. Amazon Fraud Detector requires that the EVENT_TIMESTAMP column in your dataset
have values.

**Solution**

Ensure that the EVENT_TIMESTAMP column in your dataset has values and those values are compliant with the supported [timestamp formats](online-fraud-insights.md#timestamp-formats "online-fraud-insights.md#timestamp-formats").
If you have missing values in the EVENT_TIMESTAMP column, you can either backfill those with values using the supported timestamp format or consider dropping the event completely instead of entering strings such as `none`, `null`, or `missing`.

### Data not ingested

**Issue type : Error**

**Description**

No ingested events found for training, please check your training configuration.

**Cause**

This error occurs if you are creating a model with event data stored with Amazon Fraud Detector but did not import your dataset to Amazon Fraud Detector before you started to train your model.

**Solution**

Use the `SendEvent` API operation, the `CreateBatchImportJob` API operation, or batch
import feature in the Amazon Fraud Detector console, to first import your event data and then train your model. See [Stored event datasets](storing-event-data-afd.md "storing-event-data-afd.md") for more information.

###### Note

We recommend waiting 10 minutes after you have finished importing your data before using it to train your model.

You can use Amazon Fraud Detector console to check number of events already stored for each event type. See [Viewing metrics of your stored events](storing-event-data-afd.md#view-stored-event-metrics "storing-event-data-afd.md#view-stored-event-metrics") for more information.

### Insufficient variables

**Issue type : Error**

**Description**

Dataset must contain at least 2 variables suitable for training.

**Cause**

This error occurs if your dataset contains less than 2 variables that are suitable for model training. Amazon Fraud Detector considers a variable
suitable for model training only if it passes all validations.
If a variable fails validation, it is excluded in model training and you will see a message in **Model training diagnostic**.

**Solution**

Ensure that your dataset has at least two variables populated with values and passed all data validations. Note that the event metadata row where you have provided your column
headers (EVENT_TIMESTAMP, EVENT_ID, ENTITY_ID, EVENT_LABEL, etc.) aren’t considered as variable.

### Missing or incorrect variable type

**Issue type : Warning**

**Description**

The expected data type for `$variable_name` is NUMERIC. Review and update `$variable_name` in your dataset and re-train the model.

**Cause**

You get this warning if a variable is defined as a NUMERIC variable, but in the dataset, it has values that can’t be converted to NUMERIC.
As a result, that variable is excluded in model training.

**Solution**

If you want to keep it as a NUMERIC variable, make sure that values you provide can be converted to float number. Note that if the variable
contains missing values, don’t fill them with strings such as `nonene`, `null`, or `missing`. If the variable
does contain non-numeric values, re-create it as a CATEGORICAL or FREE_FORM_TEXT variable type.

### Missing variable values

**Issue type : Warning**

**Description**

Greater than `$threshold` values for `$variable_name` are missing from your training dataset.
Consider modifying `$variable_name` in your dataset and re-training to improve performance.

**Cause**

You get this warning if the specified variable is being dropped due to too many missing values. Amazon Fraud Detector allows missing values for a variable. However, if one variable has too many missing values,
it doesn’t contribute much to the model and that variable is dropped in model training.

**Solution**

First, verify that those missing values aren’t due to mistakes in data collection and preparation.
If they are mistakes, then you can consider dropping them from your model training.
However, if you do believe those missing values are valuable and still want to keep that variable, you can manually fill missing values with a constant in both model training and real-time inference.

### Insufficient unique variable values

**Issue type : Warning**

**Description**

The count of unique values of `$variable_name` is lower than 100. Review and update `$variable_name` in your dataset and re-train the model.

**Cause**

You get this warning if the number of unique values of the specified variable is less than the 100. The thresholds differ depending on the variable type.
With very few unique values, there’s a risk that the dataset isn’t general enough to cover the feature space of that variable. As a result, the model might not generalize well on real-time predictions.

**Solution**

First, make sure the variable distribution is representative of the real business traffic. Then, you can either adopt more fine-trained variables with higher cardinality, such as using `full_customer_name` instead of `first_name` and `last_name` separately or
change the variable type to CATEGORICAL, which allows lower cardinality.

### Incorrect variable expression

1. **Issue type : Information**

**Description**

Greater than 50% of `$email_variable_name` values do not match the expected regular expression http://emailregex.com. Consider modifying `$email_variable_name` in your dataset and re-training to improve performance.

**Cause**

This information is displayed if more than 50% records in your dataset has email values that do not comply with a regular email expression and are therefore failing validation.

**Solution**

Format the email variable values to comply with the regular expression. If there are missing email values, we recommend to leave them empty instead of filling them with strings such as `none`, `null`, or `missing`. 2. **Issue type : Information**

**Description**

Greater than 50% of `$IP_variable_name` values do not match regular expression for IPv4 or IPv6 addresses https://digitalfortress.tech/tricks/top-15-commonly-used-regex/. Consider modifying `$IP_variable_name` in your dataset and re-training to improve performance.

**Cause**

This information is displayed if more than 50% records in your dataset has IP values that do not comply with a regular IP expression and are therefore failing validation.

**Solution**

Format the IP values to comply with the regular expression. If there are missing IP values, we recommend to leave them empty instead of filling them with strings such as `none`, `null`, or `missing`. 3. **Issue type : Information**

**Description**

Greater than 50% of `$phone_variable_name` values do not match basic phone regular expression /$pattern/. Consider modifying `$phone_variable_name` in your dataset and re-training to improve performance .

**Cause**

This information is displayed if more than 50% records in your dataset has phone numbers that do not comply with a regular phone number expression and are therefore failing validation.

**Solution**

Format the phone numbers to comply with the regular expression. If there are missing phone numbers, we recommend to leave them empty instead of filling them with strings such as `none`, `null`, or `missing`.

### Insufficient unique entities

**Issue type : Information**

**Description**

The number of unique entities is less than 1500. Consider including more data to improve performance.

**Cause**

This information is displayed if your dataset has a smaller number of unique entities than the recommended number. The Transaction Fraud Insights (TFI)
model uses both time-series aggregates and generic transaction features to provide the best performance. If your dataset has too few unique entities,
then most of your generic data such as IP_ADDRESS, EMAIL_ADDRESS, might not have unique values. Then, there’s also a risk that this dataset isn’t
general enough to cover the feature space of that variable. As a result, the model might not generalize well on transactions from fresh new entities.

**Solution**

Include more entities. Extend your training data time range, if needed.
