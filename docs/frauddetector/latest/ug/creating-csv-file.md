Amazon Fraud Detector will no longer be open to new customers starting November 7, 2025. If you would like to use Amazon Fraud Detector,
sign up prior to that date. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker, AutoGluon, and AWS WAF.

# Create CSV file

Amazon Fraud Detector requires that the first row of your CSV file contain column headers. The column headers in your CSV file must map to the
variables that are defined in the event type. For an example dataset, see [Get and upload example dataset](step-1-get-s3-data.md "step-1-get-s3-data.md")

The Online Fraud Insights model requires a training dataset that has at least 2 variables and up to 100 variables. In addition to the event variables, the
training dataset must contain the following headers:

- EVENT_TIMESTAMP - Defines when the event occurred
- EVENT_LABEL - Classifies the event as fraudulent or legitimate. The values in the column must correspond to the values defined in the event type.
  The following sample CSV data represents historical registration events from an online merchant:

```
EVENT_TIMESTAMP,EVENT_LABEL,ip_address,email_address
4/10/2019 11:05,fraud,209.146.137.48,fake_burtonlinda@example.net
12/20/2018 20:04,legit,203.0.112.189,fake_davidbutler@example.org
3/14/2019 10:56,legit,169.255.33.54,fake_shelby76@example.net
1/3/2019 8:38,legit,192.119.44.26,fake_curtis40@example.com
9/25/2019 3:12,legit,192.169.85.29,fake_rmiranda@example.org

```

###### Note

The CSV data file can contain double quotes and commas as part of your data.

A simplified version of the corresponding event type is represented below. The event variables correspond to the headers in the CSV file and the values in `EVENT_LABEL` correspond to the values in the labels list.

```
(
name = 'sample_registration',
eventVariables = ['ip_address', 'email_address'],
labels = ['legit', 'fraud'],
entityTypes = ['sample_customer']
)

```

## Event Timestamp formats

Ensure that your event timestamp is in the required format. As part of the model build process, the Online Fraud Insights model type
orders your data based on the event timestamp, and splits your data for training and testing purposes. To get a fair estimate of performance,
the model first trains on the training dataset, and then tests this model on the test dataset.

Amazon Fraud Detector supports the following date/timestamp formats for the values in `EVENT_TIMESTAMP` during model training:

- %yyyy-%mm-%ddT%hh:%mm:%ssZ (ISO 8601 standard in UTC only with no milliseconds)

Example: 2019-11-30T13:01:01Z

- %yyyy/%mm/%dd %hh:%mm:%ss (AM/PM)

Examples: 2019/11/30 1:01:01 PM, or 2019/11/30 13:01:01

- %mm/%dd/%yyyy %hh:%mm:%ss

Examples: 11/30/2019 1:01:01 PM, 11/30/2019 13:01:01

- %mm/%dd/%yy %hh:%mm:%ss

Examples: 11/30/19 1:01:01 PM, 11/30/19 13:01:01

Amazon Fraud Detector makes the following assumptions when parsing date/timestamp formats for event timestamps:

- If you are using the ISO 8601 standard, it must be an exact match of the preceding specification
- If you are using one of the other formats, there is additional flexibility:
  - For months and days, you can provide single or double digits. For example, 1/12/2019 is a valid date.
  - You do not need to include hh:mm:ss if you do not have them (taht is, you can simply provide a date). You can also provide a subset
    of just the hour and minutes (for example, hh:mm). Just providing hour is not supported. Milliseconds are also not supported.
  - If you provide AM/PM labels, a 12-hour clock is assumed. If there is no AM/PM information, a 24-hour clock is assumed.
  - You can use “/” or “-” as delimiters for the date elements. “:” is assumed for the timestamp elements.

## Sampling your dataset across time

We recommend that you provide examples of fraud and legitimate samples from the same time range. For example, if you provide fraud events from the past 6 months,
you should also provide legitimate events that evenly span the same time period. If your dataset contains a highly uneven distribution of fraud and legitimate events,
you might receive the following error: _"The fraud distribution across time is unacceptably fluctuant. Cannot split dataset properly."_ Typically,
the easiest fix for this error is to ensure that the fraud events and legitimate events are sampled evenly across the same timeframe. You also might need to remove data if
you experienced a large spike in fraud within a short time period.

If you cannot generate enough data to create an evenly distributed dataset, one approach is to randomize the EVENT_TIMESTAMP of your events such that they are evenly
distributed. However, this often results in performance metrics being unrealistic because Amazon Fraud Detector uses EVENT_TIMESTAMP to evaluate models on the
appropriate subset of events in your dataset.

## Null and missing values

Amazon Fraud Detector handles null and missing values. However, the percentage of nulls for variables should be limited. EVENT_TIMESTAMP and EVENT_LABEL columns should
not contain any missing values.

## File validation

Amazon Fraud Detector will fail to train a model if any of the following conditions are triggered:

- If the CSV is unable to be parsed
- If the datatype for a column is incorrect
