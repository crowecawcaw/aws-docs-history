# Demand driver configuration

To use demand drivers, you must configure them. You can configure demand drivers only
when you've ingested data in the _supplementary_time_series_ data
entity.

###### Note

If you don't configure the demand drivers, you can still generate a forecast.
However, Demand Planning won't use the demand drivers.

## Demand drivers data filling

method

A _filling method_ represents (or "fills") missing
values in a time series. Demand Planning supports the following filling methods. The
filling method that Demand Planning applies depends on the location of the gap in the
data.

- Back filling – Applied when the gap is between a product's earlier
  recorded date and the last recorded date.
- Middle filling – Applied when the gap is between the last recorded data
  point for a given product and the global last recorded date.
- Future filling – Applied when the demand driver has at least one data
  point in the future and there is a gap in the future time horizon.

![Demand drivers filling method](images/filling_method.png)

Demand Planning utilizes the last 64 data points from the
_supplementary_time_series_ data entity corresponding to the demand
driver for consideration. Demand Planning supports _zero_,
_median_, _mean_, _maximum_,
and _minimum_ options for all three filling methods.

The following example illustrates how demand drivers handle missing data when data is ingested to the _price_ column in the _supplementary_time_series_ data entity for Product 1, that includes both history and future data.

![Demand drivers filling method](images/filling_method_example1.png)

## Aggregation method

Demand Planning uses the aggregation method to facilitate the integration of demand
drivers at various levels of granularity by consolidating data over specific periods and
granularity levels.

Time period aggregation – For example, when the
_Inventory_ demand driver is available at daily level but the
forecast is at weekly level, demand planning will apply the aggregation method
configured under the demand plan settings for inventory to use the information for
forecasting.

![Aggregation method used by Demand Planning](images/aggregation_example1.png)

Granularity level aggregation – Here is an example of how demand planning
uses the granularity level aggregation. _out_of_stock_indicator_ is
available daily at product-site level but forecast granularity is only available at
product level. Demand Planning will apply the aggregation method configured under the
demand plan settings for this demand driver.

![Granularity method used by Demand Planning](images/granularity_example.png)
