Amazon Forecast is no longer available to new customers. Existing customers of
Amazon Forecast can continue to use the service as normal.
[Learn more"](https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/ "https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/")

# WORK_FORCE Domain

Use the WORK_FORCE domain to forecast workforce demand. It supports the following dataset
types. For each dataset type, we list required and optional fields. For information on how to map
the fields to columns in your training data, see [Dataset Domains and Dataset Types](howitworks-datasets-groups.md#howitworks-dataset-domainstypes "howitworks-datasets-groups.md#howitworks-dataset-domainstypes").

###### Topics

- [Target Time Series Dataset
  Type](#target-time-series-type-workforce-domain "#target-time-series-type-workforce-domain")
- [Related Time Series Dataset
  Type](#related-time-series-type-workforce-domain "#related-time-series-type-workforce-domain")
- [Item Metadata Dataset Type](#item-metadata-type-workforce-domain "#item-metadata-type-workforce-domain")

## Target Time Series Dataset

Type

The following fields are required:

- `workforce_type` (string) – The type of work force labor being
  forecast. For example, call center demand or fulfillment center labor demand.
- `timestamp` (timestamp)
- `workforce_demand` (floating-point integer) – This is the
  `target` field for which Amazon Forecast generates a forecast.

The following dimension is optional and can be used to change forecasting
granularity:

- `location` (string) – The location where the work force resources are
  sought. This should be used if you have multiple stores/locations.

Ideally, only these required fields and optional dimensions should be included. Other
additional time series information should be included in a related time series dataset.

## Related Time Series Dataset

Type

The following fields are required:

- `workforce_type` (string)
- `timestamp` (timestamp)

In addition to the required fields, your training data can include other fields. To include
other fields in the dataset, provide the fields in a schema when you create the dataset.

## Item Metadata Dataset Type

The following field is required:

- `workforce_type` (string)

The following fields are optional and might be useful in improving forecast results:

- `wages` (float) – The average wages for that particular workforce
  type.
- `shift_length` (string) – The length of the shift.
- `location` (string) – The location of the workforce.

In addition to the required and suggested optional fields, your training data can include
other fields. To include other fields in the dataset, provide the fields in a schema when you
create the dataset.
