Amazon Forecast is no longer available to new customers. Existing customers of
Amazon Forecast can continue to use the service as normal.
[Learn more"](https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/ "https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/")

# METRICS Domain

Use the METRICS domain for forecasting metrics, such as revenue, sales, and cash flow. It
supports the following dataset types. For each dataset type, we list required and optional
fields. For information on how to map the fields to columns in your training data, see [Dataset Domains and Dataset Types](howitworks-datasets-groups.md#howitworks-dataset-domainstypes "howitworks-datasets-groups.md#howitworks-dataset-domainstypes").

###### Topics

- [Target Time Series Dataset
  Type](#target-time-series-type-metrics-domain "#target-time-series-type-metrics-domain")
- [Related Time Series Dataset
  Type](#related-time-series-type-metrics-domain "#related-time-series-type-metrics-domain")
- [Item Metadata Dataset Type](#item-metadata-type-metrics-domain "#item-metadata-type-metrics-domain")

## Target Time Series Dataset

Type

The following fields are required:

- `metric_name` (string)
- `timestamp` (timestamp)
- `metric_value` (floating-point integer) – This is the
  `target` field for which Amazon Forecast generates a forecast (for example, the
  amount of revenue generated on a particular day).

Ideally, only these required fields should be included. Other additional time series
information should be included in a related time series dataset.

## Related Time Series Dataset

Type

The following fields are required:

- `metric_name` (string)
- `timestamp` (timestamp)

In addition to the required fields, your training data can include other fields. To include
other fields in the dataset, provide the fields in a schema when you create the dataset.

## Item Metadata Dataset Type

The following field is required:

- `metric_name` (string)

The following field is optional and might be useful in improving forecast results:

- `category` (string)

In addition to the required and suggested optional fields, your training data can include
other fields. To include other fields in the dataset, provide the fields in a schema when you
create the dataset.
