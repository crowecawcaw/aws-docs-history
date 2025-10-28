# Forecast based on demand drivers

To enhance forecast accuracy while configuring your forecast, you can use demand drivers.
_Demand drivers_ are related time series inputs that
capture product trends and seasons. Instead of depending on historical demand, you can use
demand drivers to influence the supply chain based on various factors. For example,
promotions, price changes, and marketing campaigns. Demand Planning supports both historical
and future demand drivers.

## Prequisites to use demand drivers

Before ingesting data for demand drivers, make sure that the data meets the following
conditions:

- Make sure to ingest the demand drivers data in the
  _supplementary_time_series_ data entity. You can provide both
  historical and future demand driver information. For information about the data entities
  that Demand Planning requires, see [Demand Planning](required_entities.md "required_entities.md").

If you cannot locate the _supplementary_time_series_ data
entity, your instance might be using an earlier data model version. You can contact
AWS Support to upgrade your data model version or create a new data
connection.

- Make sure that the following columns are populated in the
  _supplementary_time_series_ data entity.
  - _id_ – This column is the unique record identifier
    and is required for a successful data ingestion.
  - _order_date_ – This column indicates the timestamp
    of the demand driver. It can be both past and future dated.
  - _time_series_name_ – This column is the identifier
    for each demand driver. The value of this column must start with a letter, should
    be 2–56 characters long, and may contain letters, numbers, and underscores.
    Other special characters are not valid.
  - _time_series_value_ – This column provides the data
    point measurement of a particular demand driver at a specific point in time. Only
    numerical values are supported.

- Select a minimum of 1 and a maximum of 13 demand drivers. Make sure that the
  aggregation and filling methods are configured. For more information on filling methods,
  see [Demand drivers data filling
  method](configuration_demand_drivers.md#filling_method_demand_drivers "configuration_demand_drivers.md#filling_method_demand_drivers"). You can modify the settings at any
  time. Demand Planning will apply the changes in the next forecast cycle.

The following example illustrates how a Demand Plan is generated when the required
demand driver columns are ingested in the _supplementary_time_series_
data entity. Demand Planning recommends providing both historical and future demand driver
data (if available). This data helps the learning model to learn and apply the pattern to
the forecast.

![Demand drivers example](images/demand_drivers_example.png)

The following example illustrates how you can set up some common demand drivers in
your dataset.

![Demand drivers example](images/demand_drivers_example2.png)

When you provide leading indicators, Demand Planning highly recommends that you adjust
the time series date. For example, say that a particular metric serves as a 20-day leading
indicator with a 70% conversion rate. In this case, consider shifting the date in the time
series by 20 days and then applying the appropriate conversion factor. While the learning
model can learn patterns without such adjustments, aligning leading indicator data with
corresponding outcome is more effective in pattern recognition. The magnitude of the value
plays a significant role in this process, enhancing the model's ability to learn and
interpret patterns accurately.
