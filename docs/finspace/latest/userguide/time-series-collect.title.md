After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see
[Amazon FinSpace end of support](amazon-finspace-end-of-support.md "amazon-finspace-end-of-support.md").

# Collect time bars operations in Amazon FinSpace

###### Important

Amazon FinSpace Dataset Browser will be discontinued on `March 26,
 2025`. Starting `November 29, 2023`, FinSpace will no longer accept the creation of new Dataset Browser
environments. Customers using [Amazon FinSpace with Managed Kdb Insights](https://aws.amazon.com/finspace/features/managed-kdb-insights/ "https://aws.amazon.com/finspace/features/managed-kdb-insights/") will not be affected. For more information, review the [FAQ](https://aws.amazon.com/finspace/faqs/ "https://aws.amazon.com/finspace/faqs/") or contact [AWS Support](https://aws.amazon.com/contact-us/ "https://aws.amazon.com/contact-us/") to assist with your
transition.

The objective of functions at this stage is to collect the series of events that arrive at an irregular frequency into uniform intervals called bars.
You can perform collection with your functions or use the Amazon FinSpace functions to calculate bars.
Collect functions are available in the `aws.finspace.timeseries.spark.windows` module and include the following list of functions.

## Compute analytics on features

```
aws.finspace.timeseries.spark.windows.compute_analytics_on_features(data, new_column, func, partition_col_list=None, add_intermediate=False)
```

Appends to data Dataframe, a new column whose value is computed by executing pandas user defined function (UDF) on a
window of rows as specified by the function window dependency member.

**Parameters**

- `data` (DataFrame) – input dataframe
- `new_column` (str) – name of new column to add
- `input_spec` – input specification
- `func` (Callable[…​, Column]) – function to calculate over data
- `grouping_col_list` – a single or list of columns to group window on
- `add_intermediate` (Optional[bool]) – include intermediate data used in the calculation

**Return type**
`DataFrame`

**Returns**

## Compute features on time bars

```
aws.finspace.timeseries.spark.windows.compute_features_on_time_bars(data, new_column, func, force_ordering=False,*ordering_cols)
```

Reduces data by applying function preserving all other columns.

**Parameters**

- `data` (DataFrame) – input DataFrame
- `new_column` (str) – new column name
- `func` (Callable[…​, Column]) – function to calculate over data
- `force_ordering` (Optional[bool]) – return data in sort in timecolumn order
- `ordering_cols` (str) – list of cols to orderBy on

**Return type**
`DataFrame`

**Returns**
`DataFrame`

## Create time bars

```
aws.finspace.timeseries.spark.windows.create_time_bars(data, timebar_column, grouping_col_list, input_spec, timebar_spec, force_ordering=False)
```

Appends a column to the data frame in data with a rolling window of data. An optional `force_ordering` flag
ensures that the rolling data is order by the `timebar_column`.

**Parameters**

- `data` (Union[Column, DataFrame]) – input dataframe
- `timebar_column` (str) – new timebar column name
- `grouping_col_list` (Union[str, List[str]]) – list of columns to group results on
- `input_spec` (BarInputSpec) – the input spec used to generate the time bars
- `timebar_spec` (Union[TimeBarSpec, Column]) – the timebar spec used to generate the time bars
- `force_ordering` (Optional[bool]) – optional force ordering in windows

**Return type**
`DataFrame`

**Returns**
`DataFrame`

## Spark spec module

### Bar input spec

```
class aws.finspace.timeseries.spark.spec.BarInputSpec(bar_structure_name, *bar_value_columns)
```

Bases: object

This class is responsible for modeling the input specification of bar operations.

### Calc input spec

```
class aws.finspace.timeseries.spark.spec.CalcInputSpec(timestamp_column, holiday_calendar=<aws.finspace.finance.calendars.USEndOfDayCalenobject>, **kwargs_func_to_column)`
```

Bases: object

This class is responsible for modeling the input specification of calculation operations.

### Time bar spec

```
class aws.finspace.timeseries.spark.spec.TimeBarSpec(timestamp_column, window_duration, slide_duration=None, start_time=None)
```

Bases: object

This class models the input time window specification, and associated calendar.

### to_window()

Create an equivalent spark window from TimeBarSpec.
