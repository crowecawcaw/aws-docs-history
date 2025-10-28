Amazon Forecast is no longer available to new customers. Existing customers of
Amazon Forecast can continue to use the service as normal.
[Learn more"](https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/ "https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/")

# Importing Datasets

_Datasets_ contain the data used to train a [predictor](howitworks-predictor.md "howitworks-predictor.md"). You create one or more Amazon Forecast datasets and
import your training data into them. A _dataset group_ is a
collection of complementary datasets that detail a set of changing parameters over a series of
time. After creating a dataset group, you use it to train a predictor.

Each dataset group can have up to three datasets, one of each [dataset](#howitworks-dataset-domainstypes "#howitworks-dataset-domainstypes") type: target time series, related
time series, and item metadata.

To create and manage Forecast datasets and dataset groups, you can use the Forecast console,
AWS Command Line Interface (AWS CLI), or AWS SDK.

For example Forecast datasets, see the [Amazon Forecast Sample GitHub
repository](https://github.com/aws-samples/amazon-forecast-samples "https://github.com/aws-samples/amazon-forecast-samples").

###### Topics

- [Datasets](#howitworks-dataset "#howitworks-dataset")
- [Dataset Groups](#howitworks-datasetgroup "#howitworks-datasetgroup")
- [Resolving Conflicts in Data Collection
  Frequency](#howitworks-data-alignment "#howitworks-data-alignment")
- [Using Related Time Series Datasets](related-time-series-datasets.md "related-time-series-datasets.md")
- [Using Item Metadata Datasets](item-metadata-datasets.md "item-metadata-datasets.md")
- [Predefined Dataset Domains and Dataset Types](howitworks-domains-ds-types.md "howitworks-domains-ds-types.md")
- [Updating Data](updating-data.md "updating-data.md")
- [Handling Missing Values](howitworks-missing-values.md "howitworks-missing-values.md")
- [Dataset Guidelines for Forecast](dataset-import-guidelines-troubleshooting.md "dataset-import-guidelines-troubleshooting.md")

## Datasets

To create and manage Forecast datasets, you can use the Forecast APIs, including the [CreateDataset](API_CreateDataset.md "API_CreateDataset.md") and [DescribeDataset](API_DescribeDataset.md "API_DescribeDataset.md") operations. For a
complete list of Forecast APIs, see [API Reference](api-reference.md "api-reference.md").

When creating a dataset, you provide information, such as the following:

- The frequency/interval at which you recorded your data. For example, you might
  aggregate and record retail item sales every week. In the [Getting Started](getting-started.md "getting-started.md") exercise, you use the average electricity used per
  hour.
- The prediction format (the _domain_) and dataset type (within the
  domain). A dataset domain specifies which type of forecast you'd like to perform, while a
  dataset type helps you organize your training data into Forecast-friendly categories.
- The dataset _schema_. A schema maps the column headers of your
  dataset. For instance, when monitoring demand, you might have collected hourly data on the
  sales of an item at multiple stores. In this case, your schema would define the order,
  from left to right, in which timestamp, location, and hourly sales appear in your training
  data file. Schemas also define each column's data type, such as `string` or
  `integer`.
- Geolocation and time zone information. The geolocation attribute is defined within the
  schema with the attribute type `geolocation`. Time zone information is defined
  with the [CreateDatasetImportJob](API_CreateDatasetImportJob.md "API_CreateDatasetImportJob.md")
  operation. Both geolocation and time zone data must be included to enable the [Weather Index.](weather.md "weather.md")

Each column in your Forecast dataset represents either a forecast
_dimension_ or _feature_. Forecast dimensions describe
the aspects of your data that do not change over time, such a `store` or
`location`. Forecast features include any parameters in your data that vary
across time, such as `price` or `promotion`. Some dimensions, like
`timestamp` or `itemId`, are required in target time series and
related time series datasets.

### Dataset Domains and Dataset Types

When you create a Forecast dataset, you choose a domain and a dataset type. Forecast provides
domains for a number of use cases, such as forecasting retail demand or web traffic. You can
also create a custom domain. For a complete list of Forecast domains, see [Predefined Dataset Domains and Dataset Types](howitworks-domains-ds-types.md "howitworks-domains-ds-types.md").

Within each domain, Forecast users can specify the following types of datasets:

- Target time series dataset (required) – Use this dataset type when your
  training data is a time series _and_ it includes the
  field that you want to generate a forecast for. This field is called the
  _target field_.
- Related time series dataset (optional) – Choose this dataset type when your
  training data is a time series, but it _doesn't_ include the target
  field. For instance, if you're forecasting item demand, a related time series dataset
  might have `price` as a field, but not `demand`.
- Item metadata dataset (optional) – Choose this dataset type when your
  training data _isn't_ time-series data, but includes
  metadata information about the items in the target time series or related time series
  datasets. For instance, if you're forecasting item demand, an item metadata dataset
  might have `color` or `brand` as dimensions.

Forecast only considers the data provided by an item metadata dataset type when you use the [CNN-QR](aws-forecast-algo-cnnqr.md "aws-forecast-algo-cnnqr.md") or [DeepAR+](aws-forecast-recipe-deeparplus.md "aws-forecast-recipe-deeparplus.md") algorithm.

Item metadata is especially useful in coldstart forecasting scenarios, in which you have
little direct historical data with which to make predictions, but do have historical data on
items with similar metadata attributes. When you include item metadata, Forecast creates coldstart forecasts based on similar time series, which can create a more accurate forecast.

Depending on the information in your training data and what you want to forecast, you
might create more than one dataset.

For example, suppose that you want to generate a forecast for the demand of retail
items, such as shoes and socks. You might create the following datasets in the RETAIL
domain:

- Target time series dataset – Includes the historical time-series demand data
  for the retail items (`item_id`, `timestamp`, and the target field
  `demand`). Because it designates the target field that you want to
  forecast, you must have at least one target time series dataset in a dataset
  group.

You can also add up to ten other dimensions to a target time series dataset. If you
include only a target time series dataset in your dataset group, you can create
forecasts at either the item level or the forecast dimension level of granularity only.
For more information, see [CreatePredictor](API_CreatePredictor.md "API_CreatePredictor.md").

- Related time series dataset – Includes historical time-series data other than
  the target field, such as `price` or `revenue`. Because related
  time series data must be mappable to target time series data, each related time series
  dataset must contain the same identifying fields. In the RETAIL domain, these would be
  `item_id` and `timestamp`.

A related time series dataset might contain data that refines the forecasts made off
of your target time series dataset. For example, you might include `price`
data in your related time series dataset on the future dates that you want to generate a
forecast for. This way, Forecast can make predictions with an additional dimension of
context. For more information, see [Using Related Time Series Datasets](related-time-series-datasets.md "related-time-series-datasets.md").

- Item metadata dataset – Includes metadata for the retail items. Examples of
  metadata include `brand`, `category`,`color`, and
  `genre`.

**Example Dataset with a Forecast Dimension**

Continuing with the preceding example, imagine that you want to forecast the demand for
shoes and socks based on a store's previous sales. In the following target time series
dataset, `store` is a time-series forecast dimension, while `demand`
is the target field. Socks are sold in two store locations (NYC and SFO), and shoes are sold
only in ORD.

The first three rows of this table contain the first available sales data for the NYC,
SFO, and ORD stores. The last three rows contain the last recorded sales data for each
store. The `...` row represents all of the item sales data recorded between the
first and last entries.

| `timestamp`  | `item_id` | `store` | `demand` |
| ------------ | --------- | ------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `2019-01-01` | `socks`   | `NYC`   | `25`     |
| `2019-01-05` | `socks`   | `SFO`   | `45`     |
| `2019-02-01` | `shoes`   | `ORD`   | `10`     |
| `...`        |
| `2019-06-01` | `socks`   | `NYC`   | `100`    |
| `2019-06-05` | `socks`   | `SFO`   | `5`      |
| `2019-07-01` | `shoes`   | `ORD`   | `50`     | ### Dataset Schema Each dataset requires a schema, a user-provided JSON mapping of the fields in your training data. This is where you list both the required and optional dimensions and features that you want to include in your dataset. If your dataset includes a geolocation attribute, define the attribute within the schema with the attribute type `geolocation`. For more information, see [Adding Geolocation information](weather.md#adding-geolocation "weather.md#adding-geolocation"). In order to apply the [Weather Index](weather.md "weather.md"), you must include a geolocation attribute in your target time series and any related time series datasets. Some domains have optional dimensions that we recommend including. Optional dimensions are listed in the descriptions of each domain later in this guide. For an example, see [RETAIL Domain](retail-domain.md "retail-domain.md"). All optional dimensions take the data type `string`. A schema is required for every dataset. The following is the accompanying schema for the example target time series dataset above. `{ "attributes": [ { "AttributeName": "timestamp", "AttributeType": "timestamp" }, { "AttributeName": "item_id", "AttributeType": "string" }, { "AttributeName": "store", "AttributeType": "string" }, { "AttributeName": "demand", "AttributeType": "float" } ] }` When you upload your training data to the dataset that uses this schema, Forecast assumes that the `timestamp` field is column 1, the `item_id` field is column 2, the `store` field is column 3, and the `demand` field, the _target_ field, is column 4. For the related time series dataset type, all related features must have a float or integer attribute type. For the item metadata dataset type, all features must have a string attribute type. For more information, see [SchemaAttribute](API_SchemaAttribute.md "API_SchemaAttribute.md"). ###### Note An `attributeName` and `attributeType` pair is required for every column in the dataset. Forecast reserves a number of names that can't be used as the name of a schema attribute. For the list of reserved names, see [Reserved Field Names](reserved-field-names.md "reserved-field-names.md"). ## Dataset Groups A _dataset group_ is a collection of one to three complimentary datasets, one of each dataset type. You import datasets to a dataset group, then use the dataset group to train a predictor. Forecast includes the following operations to create dataset groups and add datasets to them: <br>• [CreateDatasetGroup](API_CreateDatasetGroup.md "API_CreateDatasetGroup.md") <br>• [UpdateDatasetGroup](API_UpdateDatasetGroup.md "API_UpdateDatasetGroup.md") ## Resolving Conflicts in Data Collection Frequency Forecast can train predictors with data that doesn't align with the data frequency you specify in the [CreateDataset](API_CreateDataset.md "API_CreateDataset.md") operation. For example, you can import data in recorded in hourly intervals even though some of the data isn't timestamped at the top of the hour (02:20, 02:45). Forecast uses the data frequency you specify to learn about your data. Then Forecast aggregates the data during predictor training. For more information see [Data aggregation for different forecast frequencies](data-aggregation.md "data-aggregation.md"). |
