# Aggregate data from properties and other assets (metrics)

Metrics are mathematical expressions that use aggregation functions to process all
input data points and output a single data point per specified time interval. For example,
a metric can calculate the average hourly temperature from a temperature data
stream.

Metrics can input data from associated assets' metrics, so you can calculate
statistics that provide insight to your operation or a subset of your operation. For
example, a metric can calculate the average hourly temperature across all wind turbines in
a wind farm. For more information about how to define associations between assets, see
[Define asset model hierarchies](define-asset-hierarchies.md "define-asset-hierarchies.md").

Metrics can also input data from other properties without aggregating data over each
time interval. If you specify an [attribute](attributes.md "attributes.md") in a formula,
AWS IoT SiteWise uses the [latest](expression-temporal-functions.md#latest-definition "expression-temporal-functions.md#latest-definition") value for that attribute
when it computes the formula. If you specify a metric in a formula, AWS IoT SiteWise uses the [last](expression-temporal-functions.md#last-definition "expression-temporal-functions.md#last-definition") value for the time interval over which it computes
the formula. This means you can define metrics like `OEE = Availability * Quality *
 Performance`, where `Availability`, `Quality`, and
`Performance` are all other metrics on the same asset model.

AWS IoT SiteWise also automatically computes a set of basic aggregation metrics for all asset
properties. To reduce computation costs, you can use these aggregates instead of defining
custom metrics for basic computations. For more information, see [Query asset property aggregates in AWS IoT SiteWise](aggregates.md "aggregates.md").

###### Topics

- [Define metrics (console)](#define-metrics-console "#define-metrics-console")
- [Define metrics (AWS CLI)](#define-metrics-cli "#define-metrics-cli")

## Define metrics (console)

When you define a metric for an asset model in the AWS IoT SiteWise console, you specify the
following parameters:

- **Name** – The property's name.
- **Data type** – The data type of the transform, which
  can be **Double** or **String**.
- **External ID** – (Optional) This is a user-defined ID.
  For more information, see [Reference objects with external IDs](object-ids.md#external-id-references "object-ids.md#external-id-references") in the _AWS IoT SiteWise User Guide_.
- **Formula** – The metric expression. Metric expressions
  can use [aggregation
  functions](expression-aggregation-functions.md "expression-aggregation-functions.md") to input data from a property for all associated assets in a
  hierarchy. Start typing or press the down arrow key to open the auto complete
  feature. For more information, see [Use formula expressions](formula-expressions.md "formula-expressions.md").

###### Important

Metrics can only be properties that are integer, double, Boolean, or string type. Booleans
convert to `0` (false) and `1` (true).

If you define any metric input variables in a metric's expression, those inputs must have
the same time interval as the output metric.

Formula expressions can only output double or string values. Nested
expressions can output other data types, such as strings, but the formula as a whole must
evaluate to a number or string. You can use the [jp function](expression-string-functions.md#jp-definition "expression-string-functions.md#jp-definition") to
convert a string to a number. The Boolean value must be 1 (true) or 0 (false).
For more information, see [Undefined, infinite, and overflow values](expression-tutorials.md#undefined-values "expression-tutorials.md#undefined-values").

- **Time interval** – The metric time interval.
  AWS IoT SiteWise supports the
  following tumbling window time intervals, where each interval starts when the previous one
  ends:
  - **1 minute** – 1 minute, computed at the end
    of each minute (12:00:00 AM, 12:01:00 AM, 12:02:00 AM, and so on).
  - **5 minutes** – 5 minutes, computed at the
    end of every five minutes starting on the hour (12:00:00 AM, 12:05:00 AM, 12:10:00 AM,
    and so on).
  - **15 minutes** – 15 minutes, computed at the
    end of every fifteen minutes starting on the hour (12:00:00 AM, 12:15:00 AM, 12:30:00
    AM, and so on).
  - **1 hour** – 1 hour (60 minutes), computed
    at the end of every hour in UTC (12:00:00 AM, 01:00:00 AM, 02:00:00 AM, and so
    on).
  - **1 day** – 1 day (24 hours), computed at
    the end of every day in UTC (12:00:00 AM Monday, 12:00:00 AM Tuesday, and so
    on).
  - **1 week** – 1 week (7 days), computed at
    the end of every Sunday in UTC (every 12:00:00 AM Monday).
  - **Custom interval** – You can enter any time
    interval between a minute and a week.

- **Offset date** – (Optional) The reference date from
  which to aggregate data.
- **Offset time** – (Optional) The reference time from
  which to aggregate data. The offset time must be between 00:00:00 and
  23:59:59.
- **Offset time zone** – (Optional) The time zone for the
  offset. If it isn't specified, the default offset time zone is the Universal
  Coordinated Time (UTC). See the following supported time zones.

- (UTC+00:00) Universal Coordinated Time
- (UTC+01:00) European Central Time
- (UTC+02:00) Eastern European
- (UTC03+:00) Eastern African Time
- (UTC+04:00) Near East Time
- (UTC+05:00) Pakistan Lahore Time
- (UTC+05:30) India Standard Time
- (UTC+06:00) Bangladesh Standard Time
- (UTC+07:00) Vietnam Standard Time
- (UTC+08:00) China Taiwan Time
- (UTC+09:00) Japan Standard Time
- (UTC+09:30) Australia Central Time
- (UTC+10:00) Australia Eastern Time
- (UTC+11:00) Solomon Standard Time
- (UTC+12:00) New Zealand Standard Time
- (UTC-11:00) Midway Islands Time
- (UTC-10:00) Hawaii Standard Time
- (UTC-09:00) Alaska Standard Time
- (UTC-08:00) Pacific Standard Time
- (UTC-07:00) Phoenix Standard Time
- (UTC-06:00) Central Standard Time
- (UTC-05:00) Eastern Standard Time
- (UTC-04:00) Puerto Rico and US Virgin Islands Time
- (UTC-03:00) Argentina Standard Time
- (UTC-02:00) South Georgia Time
- (UTC-01:00) Central African Time

###### Example custom time interval with an offset (console)

The following example shows you how to define a 12-hour time interval with an
offset on February 20, 2021, at 6:30:30 PM (PST).

###### To define a custom interval with an offset

1. For **Time interval**, choose **Custom
   interval**.
2. For **Time interval**, do one of the following:
   - Enter `12`, and then choose
     **hours**.
   - Enter `720`, and then choose
     **minutes**.
   - Enter `43200`, and then choose
     **seconds**.

###### Important

The **Time interval** must be an integer regardless of the
unit. 3. For **Offset date**, choose
**2021/02/20**. 4. For **Offset time**, enter
`18:30:30`. 5. For **Offset timezone**, choose **(UTC-08:00) Pacific
Standard Time**.
If you create the metric on July 1, 2021, before or at 06:30:30 PM (PST), you get the
first aggregation result on July 1, 2021, at 06:30:30 PM (PST). The second aggregation
result is on July 2, 2021, at 06:30:30 AM (PST), and so on.

## Define metrics (AWS CLI)

When you define a metric for an asset model with the AWS IoT SiteWise API, you specify the
following parameters:

- `name` – The property's name.
- `dataType` – The data type of the metric, which can be
  `DOUBLE` or `STRING`.
- `externalId` – (Optional) This is a user-defined ID. For more information, see [Reference objects with external IDs](object-ids.md#external-id-references "object-ids.md#external-id-references") in the _AWS IoT SiteWise User Guide_.
- `expression` – The metric expression. Metric expressions can
  use [aggregation functions](expression-aggregation-functions.md "expression-aggregation-functions.md") to
  input data from a property for all associated assets in a hierarchy. For more
  information, see [Use formula expressions](formula-expressions.md "formula-expressions.md").
- `window` – The time interval and offset for the metric's
  tumbling window, where each interval starts when the previous one ends:

      + `interval` – The time interval for the tumbling window.
       The time interval must be between a minute and a week.
      + `offsets` – The offset for the tumbling window.

  For more information, see [TumblingWindow](../APIReference/API_TumblingWindow.md "../APIReference/API_TumblingWindow.md") in the _AWS IoT SiteWise API Reference_.

###### Example custom time interval with an offset (AWS CLI)

The following example shows you how to define a 12-hour time interval with an
offset on February 20, 2021, at 06:30:30 PM (PST).

```

{
    "window": {
        "tumbling": {
            "interval": "12h",
            "offset": " 2021-07-23T18:30:30-08"
        }
    }
}

```

If you create the metric on July 1, 2021, before or at 06:30:30 PM (PST), you get
the first aggregation result on July 1, 2021, at 06:30:30 PM (PST). The second
aggregation result is on July 2, 2021, at 06:30:30 AM (PST), and so on.

- `variables` – The list of variables that defines the other
  properties of your asset or child assets to use in the expression. Each variable
  structure contains a simple name for use in the expression and a `value`
  structure that identifies which property to link to that variable. The
  `value` structure contains the following information:
  - `propertyId` – The ID of the property from which to pull
    values. You can use the property's name instead of its ID if the property is
    defined in the current model (rather than defined in a model from a
    hierarchy).
  - `hierarchyId` – (Optional) The ID of the hierarchy from
    which to query child assets for the property. You can use the hierarchy
    definition's name instead of its ID. If you omit this value, AWS IoT SiteWise finds the
    property in the current model.

###### Important

Metrics can only be properties that are integer, double, Boolean, or string type. Booleans
convert to `0` (false) and `1` (true).

If you define any metric input variables in a metric's expression, those inputs must have
the same time interval as the output metric.

Formula expressions can only output double or string values. Nested
expressions can output other data types, such as strings, but the formula as a whole must
evaluate to a number or string. You can use the [jp function](expression-string-functions.md#jp-definition "expression-string-functions.md#jp-definition") to
convert a string to a number. The Boolean value must be 1 (true) or 0 (false).
For more information, see [Undefined, infinite, and overflow values](expression-tutorials.md#undefined-values "expression-tutorials.md#undefined-values").

- `unit` – (Optional) The scientific unit for the property, such as mm or Celsius.

###### Example metric definition

The following example demonstrates a metric property that aggregates an asset's
temperature measurement data to calculate maximum hourly temperature in Fahrenheit.
This object is an example of an [AssetModelProperty](../APIReference/API_AssetModelProperty.md "../APIReference/API_AssetModelProperty.md") that contains a [Metric](../APIReference/API_Metric.md "../APIReference/API_Metric.md").
You can specify this object as a part of the [CreateAssetModel](../APIReference/API_CreateAssetModel.md "../APIReference/API_CreateAssetModel.md") request payload to
create a metric property. For more information, see [Create an asset model (AWS CLI)](create-asset-models.md#create-asset-model-cli "create-asset-models.md#create-asset-model-cli").

```

{
      `...`
      "assetModelProperties": [
      `...`
      {
        "name": "Max temperature",
        "dataType": "DOUBLE",
        "type": {
          "metric": {
            "expression": "max(temp_f)",
            "variables": [
              {
                "name": "temp_f",
                "value": {
                  "propertyId": "Temperature F"
                }
              }
            ],
            "window": {
              "tumbling": {
                "interval": "1h"
              }
            }
          }
        },
        "unit": "Fahrenheit"
      }
    ],
    `...`
}

```

###### Example metric definition that inputs data from associated assets

The following example demonstrates a metric property that aggregates multiple wind
turbines' average power data to calculate total average power for a wind farm. This object
is an example of an [AssetModelProperty](../APIReference/API_AssetModelProperty.md "../APIReference/API_AssetModelProperty.md") that contains a [Metric](../APIReference/API_Metric.md "../APIReference/API_Metric.md"). You can specify
this object as a part of the [CreateAssetModel](../APIReference/API_CreateAssetModel.md "../APIReference/API_CreateAssetModel.md") request payload to create a metric
property.

```
{
      `...`
      "assetModelProperties": [
      `...`
      {
          "name": "Total Average Power",
          "dataType": "DOUBLE",
          "type": {
            "metric": {
              "expression": "avg(power)",
              "variables": [
                {
                  "name": "power",
                  "value": {
                    "propertyId": "a1b2c3d4-5678-90ab-cdef-11111EXAMPLE",
                    "hierarchyId": "Turbine Asset Model"
                  }
                }
              ],
              "window": {
                "tumbling": {
                  "interval": "5m"
                }
              }
            }
        },
        "unit": "kWh"
      }
    ],
    `...`
}
```
