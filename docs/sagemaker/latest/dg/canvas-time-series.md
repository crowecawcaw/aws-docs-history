# Time Series Forecasts in Amazon SageMaker Canvas

###### Note

Time series forecasting models are only supported for tabular datasets.

Amazon SageMaker Canvas gives you the ability to use machine learning time series forecasts. Time series
forecasts give you the ability to make predictions that can vary with time.

You can make a time series forecast for the following examples:

- Forecasting your inventory in the coming months.
- The number of items sold in the next four months.
- The effect of reducing the price on sales during the holiday season.
- Item inventory in the next 12 months.
- The number of customers entering a store in the next several hours.
- Forecasting how a 10% reduction in the price of a product affects sales over a
  time period.
  To make a time series forecast, your dataset must have the following:

- A timestamp column with all values having the `datetime` type.
- A target column that has the values that you're using to forecast future
  values.
- An item ID column that contains unique identifiers for each item in your dataset,
  such as SKU numbers.
  The `datetime` values in the timestamp column must use one of the following
  formats:

- `YYYY-MM-DD HH:MM:SS`
- `YYYY-MM-DDTHH:MM:SSZ`
- `YYYY-MM-DD`
- `MM/DD/YY`
- `MM/DD/YY HH:MM`
- `MM/DD/YYYY`
- `YYYY/MM/DD HH:MM:SS`
- `YYYY/MM/DD`
- `DD/MM/YYYY`
- `DD/MM/YY`
- `DD-MM-YY`
- `DD-MM-YYYY`
  You can make forecasts for the following intervals:

- 1 min
- 5 min
- 15 min
- 30 min
- 1 hour
- 1 day
- 1 week
- 1 month
- 1 year

## Future values in your input dataset

Canvas automatically detects columns in your dataset that might potentially
contain future values. If present, these values can enhance the accuracy of predictions.
Canvas marks these specific columns with a `Future values` label.
Canvas infers the relationship between the data in these columns and the target
column that you are trying to predict, and utilizes that relationship to generate more
accurate forecasts.

For example, you can forecast the amount of ice cream sold by a grocery store. To make
a forecast, you must have a timestamp column and a column that indicates how much ice
cream the grocery store sold. For a more accurate forecast, your dataset can also
include the price, the ambient temperature, the flavor of the ice cream, or a unique
identifier for the ice cream.

Ice cream sales might increase when the weather is warmer. A decrease in the price of
the ice cream might result in more units sold. Having a column with ambient temperature
data and a column with pricing data can improve your ability to forecast the number of
units of ice cream the grocery store sells.

While providing future values is optional, it helps you to perform what-if analyses
directly in the Canvas application, showing you how changes in future values could
alter your predictions.

## Handling missing values

You might have missing data for different reasons. The reason for your missing data
might inform how you want Canvas to impute it. For example, your organization might
use an automatic system that only tracks when a sale happens. If you're using a dataset
that comes from this type of automatic system, you have missing values in the target
column.

###### Important

If you have missing values in the target column, we recommend using a dataset that
doesn't have them. SageMaker Canvas uses the target column to forecast future values. Missing
values in the target column can greatly reduce the accuracy of the forecast.

For missing values in the dataset, Canvas automatically imputes the missing values
for you by filling the target column with `0` and other numeric columns with
the median value of the column.

However, you can select your own filling logic for the target column and other numeric
columns in your datasets. Target columns have different filling guidelines and
restrictions than the rest of the numeric columns. Target columns are filled up to the
end of the historical period, whereas numeric columns are filled across both historical
and future periods all the way to the end of the forecast horizon. Canvas only fills
future values in a numeric column if your data has at least one record with a future
timestamp and a value for that specific column.

You can choose one of the following filling logic options to impute missing values in
your data:

- `zero` – Fill with `0`.
- `NaN` – Fill with NaN, or not a number. This is only
  supported for the target column.
- `mean` – Fill with the mean value from the data series.
- `median` – Fill with the median value from the data series.
- `min` – Fill with the minimum value from the data series.
- `max` – Fill with the maximum value from the data series.

When choosing a filling logic, you should consider how your model interprets the
logic. For example, in a retail scenario, recording zero sales of an available item is
different from recording zero sales of an unavailable item, as the latter scenario
doesn’t necessarily imply a lack of customer interest in the unavailable item. In this
case, filling with `0` in the target column of the dataset might cause the
model to be under-biased in its predictions and infer a lack of customer interest in
unavailable items. Conversely, filling with `NaN` might cause the model to
ignore true occurrences of zero items being sold of available items.

## Types of forecasts

You can make one of the following types of forecasts:

- **Single item**
- **All items**

For a forecast on all the items in your dataset, SageMaker Canvas returns a forecast for the
future values for each item in your dataset.

For a single item forecast, you specify the item and SageMaker Canvas returns a forecast for the
future values. The forecast includes a line graph that plots the predicted values over
time.

###### Topics

- [Additional options for forecasting insights](canvas-additional-insights.md "canvas-additional-insights.md")
