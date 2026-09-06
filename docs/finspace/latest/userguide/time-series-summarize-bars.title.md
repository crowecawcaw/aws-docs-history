

After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/userguide/amazon-finspace-end-of-support.html). 

# Summarize bars operations in Amazon FinSpace
<a name="time-series-summarize-bars.title"></a>

**Important**  
Amazon FinSpace Dataset Browser will be discontinued on {{March 26, 2025}}. Starting {{November 29, 2023}}, FinSpace will no longer accept the creation of new Dataset Browser environments. Customers using [Amazon FinSpace with Managed Kdb Insights](https://aws.amazon.com/finspace/features/managed-kdb-insights/) will not be affected. For more information, review the [FAQ](https://aws.amazon.com/finspace/faqs/) or contact [AWS Support](https://aws.amazon.com/contact-us/) to assist with your transition.

The objective of this stage is to take collected data in bars from previous stage and summarize it using the events captures within a bar. Collect functions are available in the `aws.finspace.timeseries.spark.summarizer` module and include the following list of functions.

## Bar count
<a name="_bar_count"></a>

```
aws.finspace.timeseries.spark.summarizer.bar_cnt(input_series)
```

 **Returns** the number of items in interval.

 **Parameters** 
+  `input_series` (Series) – a series window produced through groupby

 **Return type** `Series` 

 **Returns** `pandas.Series` 

## Close
<a name="_close"></a>

```
aws.finspace.timeseries.spark.summarizer.close(price)
```

Returns the last row, called close as its the closing price of that interval.

 **Parameters** 
+  `price` (Series) – a series Window produced through group by

 **Return type** `Series` **Returns** `pandas.Series` 

## First last high low
<a name="_first_last_high_low"></a>

```
aws.finspace.timeseries.spark.summarizer.first_last_high_low(sort_col: list, price: list) -> list
```

 **Return type** `list` 

## First last high low presorted
<a name="_first_last_high_low_presorted"></a>

```
aws.finspace.timeseries.spark.summarizer.*first_last_high_low_presorted*(price: list) -> list
```

 **Return type** `list` 

## High
<a name="_high"></a>

```
aws.finspace.timeseries.spark.summarizer.high(price)
```

Returns the highest price in that interval.

 **Parameters** 
+  `price` (Series) – a DataFrame Window produced through groupby

 **Return type** `Series` 

 **Returns** `pandas.Series` 

## Low
<a name="_low"></a>

```
aws.finspace.timeseries.spark.summarizer.low(price)
```

Returns the lowest price in that interval.

 **Parameters** 
+  `price` (Series) – a series Window produced through groupby

 **Return type** `Series` 

 **Returns** `pandas.Series` 

## Low high
<a name="_low_high"></a>

```
aws.finspace.timeseries.spark.summarizer.lowhigh(value) -> list
```

 **Return type** `list` 

## Open high low close (OHLC)
<a name="_open_high_low_close_ohlc"></a>

The first, high, low, and last value over an interval.

```
aws.finspace.timeseries.spark.summarizer.ohlc_func(sort_col: list, price: list) -> list
```

 **Return type** `list` 

## Open high low close pre-sorted (OHLC)
<a name="_open_high_low_close_pre_sorted_ohlc"></a>

The first, high, low, and last value over an interval.

```
aws.finspace.timeseries.spark.summarizer.ohlc_func_pre_sorted(price: list) -> list
```

 **Return type** `list` 

## Open high low close scala (OHLC)
<a name="_open_high_low_close_scala_ohlc"></a>

The first, high, low, and last value over an interval.

```
aws.finspace.timeseries.spark.summarizer.ohlc_scala(timeseries, values)
```

## Open
<a name="_open"></a>

```
aws.finspace.timeseries.spark.summarizer.open(price)
```

Returns the first row, the opening price over that interval.

 **Parameters** 
+  `price` (Series) – a series window produced through groupby

 **Return type** `Series` **Returns** `pandas.Series` 

## Standard deviation
<a name="_standard_deviation"></a>

```
aws.finspace.timeseries.spark.summarizer.std(price)
```

Returns the standard deviation over that interval.

 **Parameters** 
+  `price` (Series) – a series Window produced through groupby

 **Return type** `Series` **Returns** `pandas.Series` 

## Time Delta
<a name="_time_delta"></a>

```
aws.finspace.timeseries.spark.summarizer.*time_delta*(time_series: list, ref_date: datetime.date) -> list
```

 **Return type** `list` 

## Total volume
<a name="_total_volume"></a>

```
aws.finspace.timeseries.spark.summarizer.total_volume(volume)
```

The total volume over that interval.

 **Parameters** 
+  `volume` (Series) – input volume

 **Return type** `DataFrame` 

 **Returns** 

## Volume and close
<a name="_volume_and_close"></a>

```
aws.finspace.timeseries.spark.summarizer.volume_and_close(price: list, vol: list) -> list
```

 **Return type** `list` 

## Volume weighted average price (VWAP)
<a name="_volume_weighted_average_price_vwap"></a>

```
aws.finspace.timeseries.spark.summarizer.vwap(price, volume)
```

The volume weighted average price over that interval.

 **Parameters** 
+  `price` (Series) – input price series
+  `volume` (Series) – input volume

 **Return type** `DataFrame` 

 **Returns** 