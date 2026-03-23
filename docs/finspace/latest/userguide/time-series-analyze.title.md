After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see
[Amazon FinSpace end of support](amazon-finspace-end-of-support.md "amazon-finspace-end-of-support.md").

# Analyze operations in Amazon FinSpace

###### Important

Amazon FinSpace Dataset Browser will be discontinued on `March 26,
 2025`. Starting `November 29, 2023`, FinSpace will no longer accept the creation of new Dataset Browser
environments. Customers using [Amazon FinSpace with Managed Kdb Insights](https://aws.amazon.com/finspace/features/managed-kdb-insights/ "https://aws.amazon.com/finspace/features/managed-kdb-insights/") will not be affected. For more information, review the [FAQ](https://aws.amazon.com/finspace/faqs/ "https://aws.amazon.com/finspace/faqs/") or contact [AWS Support](https://aws.amazon.com/contact-us/ "https://aws.amazon.com/contact-us/") to assist with your
transition.

At this stage, a prepared dataset of features is ready for application of technical and statistical indicators. You can bring your own indicator functions
or choose one of the FinSpace functions for this stage.

## Acceleration bands (ABANDS)

```
aws.finspace.timeseries.spark.analytics.abands(tenor, time_col_name, price_col_name, high_col_name, low_col_name)
```

The Acceleration Bands (ABANDS) created by Price Headley plots upper and lower envelope bands around a
simple moving average.

**Parameters**

- `tenor` (int) – window size
- `time_col_name` (str) – name of time column
- `price_col_name` (str) – input array of asset prices, determined by user, default is close for intraday calculations
- `high_col_name` (str) – input array of high asset prices
- `low_col_name` (str) – input array of high asset prices

**Return type**
`Callable[. . . , Column]`

**Returns** pandas/Spark user defined scalar function

## Accumulation/Distribution (AD)

```
aws.finspace.timeseries.spark.analytics.acc_dist_indicator(time_col_name,price_col_name, high_col_name, low_col_name, volume_col_name)
```

The Accumulation/Distribution (AD) study attempts to quantify the amount of volume flowing into or out of an
instrument by identifying the position of the close of the period in relation to that period's high/low range.
The volume for the period is then allocated accordingly to a running continuous total.
In this indicator, if the divisor, high-low is 0, and hence the current money flow volume is nan, then it means that price,
which must fall between high and low is also going to equal high. In that case the numerator is 0 as well
which means that the contribution should really be 0 in this case. Hence below we filter the NANs out in the equation.
[https://www.investopedia.com/terms/a/accumulationdistribution.asp](https://www.investopedia.com/terms/a/accumulationdistribution.asp "https://www.investopedia.com/terms/a/accumulationdistribution.asp")

**Parameters**

- `time_col_name` (str) – name of time column
- `price_col_name` (str) – input array of asset prices, determined by user, default is close for intraday calculations
- `high_col_name` (str) – input array of high asset prices
- `low_col_name` (str) – input array of high asset price
- `volume_col_name` (str) – asset volume for the bar

**Return type**
`Callable[. . . , Column]`

**Returns** pandas/Spark user defined scalar function

## Average directional movement index rating (ADXR)

```
aws.finspace.timeseries.spark.analytics.adrx_indicator(adx_period, period, time_col_name, price_col_name, high_col_name, low_col_name)
```

The Average Directional Movement Index Rating (ADXR) is an element of the Directional Movement System,
developed by J. Welles Wilder. ADXR quantifies the change in momentum of the Average Directional Index (ADX).
This indicator is the result of adding two values of the Average Directional Index (the current ADX value and the ADX value n-periods ago),
after which dividing this sum by two, or: `ADXR = (ADX + ADX n-periods ago) / 2`

**Parameters**

- `adx_period` (int) – look back window for Average Directional Index
- `period` (int) – look back window for Average Directional Index
- `time_col_name` (str) – name of time column
- `price_col_name` (str) – input array of closing prices over bar
- `high_col_name` (str) – input array of high prices over bar
- `low_col_name` (str) – input array of low prices over bar

**Return type**
`Callable[. . . , Column]`

**Returns** pandas/Spark user defined scalar function

## Average directional movement index (ADX)

```
aws.finspace.timeseries.spark.analytics.adx_indicator(tenor, time_col_name, price_col_name, high_col_name, low_col_name)
```

The Average Directional Movement Index (ADX) is designed to quantify trend strength by measuring the amount of price movement
in a single direction. The ADX is part of the Directional Movement system published by J. Welles Wilder, and is the average resulting
from the Directional Movement indicators.

**Parameters**

- `tenor` – window size
- `time_col_name` – name of time column
- `price_col_name` – input array of closing prices over bar
- `high_col_name` – input array of high prices over bar
- `low_col_name` – input array of low prices over bar

**Return type**
`Callable[. . . , Column]`

**Returns** pandas/Spark user defined scalar function

## Moving average convergence divergence (MACD)

```
aws.finspace.timeseries.spark.analytics.apo_indicator(short_tenor, long_tenor, time_col_name, input_array_col_name)
```

The Moving Average Convergence Divergence (MACD) was developed by Gerald Appel, and is based on the
differences between two moving averages of different lengths, a Fast and a Slow moving average. A second line, called the Signal line
is plotted as a moving average of the MACD. A third line, called the MACD Histogram is optionally plotted as a histogram of the
difference between the MACD and the Signal Line. Learn [more](https://www.investopedia.com/terms/m/macd.asp "https://www.investopedia.com/terms/m/macd.asp").

**Parameters**

- `short_tenor` (int) – short window size
- `long_tenor` (int) – long window size
- `time_col_name` (str) – name of time column
- `input_array_col_name` (str) – name of input array column

**Return type**
`Callable[. . . , Column]`

**Returns** pandas/Spark user defined scalar function

## Aroon down indicator

```
aws.finspace.timeseries.spark.analytics.aroon_down_indicator(tenor, time_col_name, price_col_name)
```

`Aroon down indicator = ((Number of periods - Number of periods since lowest low) / Number of periods) * 100`

**Parameters**

- `tenor` (int) – look back period
- `time_col_name` (str) – name of time column
- `price_col_name` (str) – input array of asset prices, determined by user, default is close for intraday calculations

**Return type**
`Callable[. . . , Column]`

**Returns** pandas/Spark user defined scalar function

## Aroon oscillator

```
aws.finspace.timeseries.spark.analytics.aroon_oscillator(tenor, time_col_name, price_col_name)
```

The Aroon Oscillator is a trend-following indicator that uses aspects of the Aroon Indicator
(Aroon Up and Aroon Down)to gauge the strength of a current trend and the likelihood that it will continue.
Readings above zero indicate that an uptrend is present, while readings below zero indicate that a downtrend is present.
Traders watch for zero line crossovers to signal potential trend changes. They also watch for big moves, above 50 or below
-50 to signal strong price moves.

**Parameters**

- `tenor` (int) – look back period
- `time_col_name` (str) – name of time column
- `price_col_name` (str) – input array of asset prices, determined by user, default is close for intraday calculations

**Return type**
`Callable[. . . , Column]`

**Returns** pandas/Spark user defined scalar function

## Aroon up indicator

```
aws.finspace.timeseries.spark.analytics.aroon_up_indicator(tenor, time_col_name, price_col_name)
```

`Aroon up indicator = ((Number of periods - Number of periods since highest high) / Number of periods) * 100`

**Parameters**

- `tenor` (int) – look back period
- `time_col_name` (str) – name of time column
- `price_col_name` (str) – input array of asset prices, determined by user, default is close for intraday calculations

**Return type**
`Callable[. . . , Column]`

**Returns** pandas/Spark user defined scalar function

## Average true range (ATR)

```
aws.finspace.timeseries.spark.analytics.average_true_range(tenor, time_col_name, price_col_name, high_col_name, low_col_name)
```

The Average True Range (ATR) study measures the size of the period's range, and takes into account any gap
from the close of the previous period. Learn [more](https://www.investopedia.com/terms/a/atr.asp "https://www.investopedia.com/terms/a/atr.asp").
**Parameters**

- `tenor` (int) – look back period
- `time_col_name` (str) – name of time column
- `price_col_name` (str) – input array of asset prices, determined by user, default is close for intraday calculations
- `high_col_name` (str) – input array of high asset prices
- `low_col_name` (str) – input array of high asset price

**Return type**
`Callable[. . . , Column]`

**Returns** pandas/Spark user defined scalar function

## Bollinger band (BBANDS)

```
aws.finspace.timeseries.spark.analytics.bollinger_bands(tenor, no_std, time_col_name, price_col_name, high_col_name, low_col_name)
```

The Bollinger Band (BBANDS) study created by John Bollinger plots upper and lower envelope bands around
the price of the instrument. The width of the bands is based on the standard deviation of the closing
prices from a moving average of price. Learn [more](https://www.investopedia.com/terms/b/bollingerbands.asp "https://www.investopedia.com/terms/b/bollingerbands.asp").

**Parameters**

- `tenor` (int) – window to perform the calculation over
- **no_std** (int) – number of standard deviations
- `time_col_name` (str) – name of time column
- `price_col_name` (str) – input array of asset prices, determined by user, default is close for intraday calculations
- `high_col_name` (str) – input array of high asset prices
- `low_col_name` (str) – input array of high asset price

**Return type**
`Callable[. . . , Column]`

**Returns** float

## Chaikin money flow

```
aws.finspace.timeseries.spark.analytics.chaiken_money_flow_indicator(tenor, time_col_name, price_col_name, high_col_name, low_col_name, vol ume_col_name)
```

Developed by Marc Chaikin, Chaikin Money Flow measures the amount of Money Flow Volume over a specific period. Money Flow Volume forms the basis for the
Accumulation Distribution Line. Instead of a cumulative total, Chaikin Money Flow sums Money Flow Volume for a specific look-back period, typically 20
or 21 days. The resulting indicator fluctuates above/below the zero line just like an oscillator. Chartists weigh the balance of buying or selling pressure
with the absolute level of Chaikin Money Flow. Additionally, chartists can look for crosses above or below the zero line to identify changes on money flow.

**Parameters**

- `tenor` (int) – look back window
- `time_col_name` (str) – name of time column
- `price_col_name` (str) – input array of closing prices over bar
- `high_col_name` (str) – input array of high prices over bar
- `low_col_name` (str) – input array of low prices over bar
- `volume_col_name` (str) – input array of low prices over bar

**Return type**
`Callable[. . . , Column]`

**Returns** pandas/Spark user defined scalar function

## Chaikens volatility indicator

```
aws.finspace.timeseries.spark.analytics.chaikens_volatility_indicator(tenor, time_col_name, high_col_name, low_col_name)
```

Marc Chaikin's Volatility indicator compares the spread between a security's high and low prices, quantifying volatility as a widening
of the range between the high and the low price.

**Parameters**

- `tenor` (int) – look back
- `time_col_name` (str) – name of time column
- `price_col_name` – input array of closing prices over bar

**Return type**
`Callable[. . . , Column]`

**Returns** pandas/Spark user defined scalar function

## Chande momentum indicator

```
aws.finspace.timeseries.spark.analytics.cmo_indicator(tenor, time_col_name, price_col_name)
```

The Chande Momentum Oscillator (CMO) developed by Tushar Chande attempts to capture the momentum of the instrument.
The indicator oscillates between -100 and 100 with overbought level of 50 and oversold level of
-50.

**Parameters**

- `tenor` (int) – look back period
- `time_col_name` (str) – name of time column
- `price_col_name` (str) – input array of asset prices, determined by user, default is close for intraday calculations

**Return type**
`Callable[. . . , Column]`

**Returns** pandas/Spark user defined scalar function

## Commodity channel index (CCI)

```
aws.finspace.timeseries.spark.analytics.commodity_channel_index(tenor, time_col_name, price_col_name, high_col_name, low_col_name)
```

The Commodity Channel Index (CCI) compares the current mean price with the average mean price over a typical window of 20 periods.
Learn [more](https://www.investopedia.com/terms/c/commoditychannelindex.asp "https://www.investopedia.com/terms/c/commoditychannelindex.asp").

**Parameters**

- `tenor` (int) – look back period
- `time_col_name` (str) – name of time column
- `price_col_name` (str) – input array of asset prices, determined by user, default is close for intraday calculations
- `high_col_name` (str) – input array of high asset prices
- `low_col_name` (str) – input array of high asset price

**Return type**
`Callable[. . . , Column]`

**Returns** pandas/Spark user defined scalar function

## Coppock curve

```
aws.finspace.timeseries.spark.analytics.coppock_curve_indicator(roc1_period, roc2_period, wma_period,  time_col_name, price_col_name)
```

The Coppock Curve is a long-term price momentum indicator used primarily to recognize major downturns and upturns in a stock market index.
It is calculated as a 10-month weighted moving average of the sum of the 14-month rate of change and the 11-month rate of change for the index. It is also known as the Coppock Guide.

**Parameters**

- **roc1_period** (int) – rate of change 1 look back period
- **roc2_period** (int) – rate of change 2 look back period
- **wma_period** (int) – weighted moving average look back period
- `time_col_name` (str) – name of time column
- `price_col_name` (str) – input array of high prices over bar

**Return type**
`Callable[. . . , Column]`

**Returns** pandas/Spark user defined scalar function

## Debug UDF call

```
aws.finspace.timeseries.spark.analytics.debug_udf_call(tenor, time_col_name, *kwargs)
```

**Return type**
`Callable[. . . , Column]`

## Directional movement indicators (DMI)

```
aws.finspace.timeseries.spark.analytics.dmi_indicator(tenor, time_col_name, price_col_name, high_col_name, low_col_name)
```

The Directional Movement Indicators (DMI) are components of the Directional Movement system published by
J. Welles Wilder, and are computed with the Average Directional Movement Index (ADX). Two indicators are plotted,
a Positive DI ( +DI ) and a Negative DI ( -DI ).

**Parameters**

- `tenor` (int) – window size, typically 2 periods
- `time_col_name` (str) – name of time column
- `price_col_name` (str) – input array of closing prices over bar
- `high_col_name` (str) – input array of high prices over bar
- `low_col_name` (str) – input array of low prices over bar

**Return type**
`Callable[. . . , Column]`

**Returns** pandas/Spark user defined scalar function

## Donchian channels

```
aws.finspace.timeseries.spark.analytics.donchian_channel_indicator(tenor, time_col_name, high_col_name, low_col_name)
```

Donchian Channels are three lines generated by moving average calculations that comprise an indicator formed by
upper and lower bands around a mid-range or median band. The upper band marks the highest price of a security over N periods
while the lower band marks the lowest price of a security over N periods. The area between the upper and lower bands represents the
Donchian Channel. Career futures trader Richard Donchian developed the indicator in the mid-twentieth century to help him identify trends.
He would later be nicknamed **The Father of Trend Following**.

**Parameters**

- `tenor` \*look back
- `time_col_name` \*name of time column
- `high_col_name` \*input array of high prices over bar
- `low_col_name` input array of low prices over bar

**Return type** \*Callabl[. . . , Column]

**Return** pandas/spark user defined scalar function

## Double exponential moving average (DEMA)

```
aws.finspace.timeseries.spark.analytics.double_exponential_moving_average(tenor, time_col_name, price_col_name)
```

The Double Exponential Moving Average (DEMA) by Patrick Mulloy attempts to offer a smoothed average
with less lag than a straight exponential moving average. The calculation is more complex than just a moving average of a moving
average as shown in the formula below.

**Parameters**

- `tenor` (int) – look back period
- `time_col_name` (str) – name of time column
- `price_col_name` (str) – input array of asset prices, determined by user, default is close for intraday calculations

**Return type**
`Callable[. . . , Column]`
**Returns** pandas/Spark user defined scalar function

## Detrended price oscillator (DPO)

```
aws.finspace.timeseries.spark.analytics.dpo_indicator(tenor, time_col_name, price_col_name)
```

A detrended price oscillator is an oscillator that strips out price trends in an effort to estimate the length of price cycles from peak
to peak or trough to trough. Unlike other oscillators, such as the stochastic or moving average convergence divergence (MACD), the DPO is
not a momentum indicator. It highlights peaks and troughs in price, which are used to estimate buy and sell points in line with the
historical cycle.

**Parameters**

- `tenor` – look back period
- `time_col_name` – name of time column
- `high_col_name` – input array of high prices over bar
- `low_col_name` – input array of low prices over bar

**Return type**
`Callable[. . . , Column]`

**Return** pandas/spark user defined scalar function

## Ease of movement indicator

```
aws.finspace.timeseries.spark.analytics.ease_of_movement_indicator(tenor, time_col_name, high_col_name, low_col_name, vol- ume_col_name, scale=1000000)
```

Richard ArmsÃ¢Â€Â™ Ease of Movement indicator is a technical study that attempts to quantify a mix of momentum
and volume information into one value. The intent is to use this value to discern whether prices are able to rise, or fall,
with little resistance in the directional movement. Theoretically, if prices move easily, they will continue to do so for a period of
time that can be traded effectively.

**Parameters**

- `tenor` – look back window
- `time_col_name` – name of time column
- `high_col_name` – input array of high prices over bar
- `low_col_name` – input array of low prices over bar
- `volume_col_name` – input array of total volume over bar
- `scale` – scale multiplier

**Return type**
`Callable[. . . , Column]`

**Returns** pandas/Spark user defined scalar function

## Elder-ray index

```
aws.finspace.timeseries.spark.analytics.elder_ray_index_indicator(tenor, time_col_name, price_col_name)
```

The Elder-Ray Index is a technical indicator developed by Dr. Alexander Elder that measures the amount of buying and selling
pressure in a market. This indicator consists of three separate indicators known as **bull power** and **bear power**,
which are derived from a 13-period exponential moving average (EMA). The three indicator help traders determine the trend direction
and isolate spots to enter and exit trades.

**Parameters**

- `tenor` (int) – look back
- `time_col_name` (str) – name of time column
- `price_col_name` (str) – input array of closing prices over bar

**Return type**
`Callable[. . . , Column]`

**Returns** pandas/Spark user defined scalar function

## Exponential moving average

```
aws.finspace.timeseries.spark.analytics.exponential_moving_average(tenor, time_col_name, input_array_col_name)
```

Compute exponential moving average on entire data set.

**Parameters**

- `tenor` (int) – window size
- `time_col_name` (str) – name of time column
- `input_array_col_name` (str) – name of input array column

**Return type**
`Callable[. . . , Column]`

**Returns** pandas/Spark user defined scalar function

## Stochastic fast (StochF)

```
aws.finspace.timeseries.spark.analytics.fast_stock_oscillator(tenor, time_col_name, price_col_name,  high_col_name, low_col_name)
```

The Stochastic Fast (StochF) normalizes price as a percentage between 0 and 100. Normally two lines are
plotted, the %K line and a 3 day moving average of the %K which is called %D. A fast stochastic is created by not smoothing
the %K line with a moving average before it is displayed.

**Parameters**

- `tenor` (int) – look back period
- `time_col_name` (str) – name of time column
- `price_col_name` (str) – input array of asset prices, determined by user, default is close for intraday calculations
- `high_col_name` (str) – input array of high asset prices
- `low_col_name` (str) – input array of high asset price

**Return type**
`Callable[. . . , Column]`

**Returns** pandas/Spark user defined scalar function

## Fisher transform

```
aws.finspace.timeseries.spark.analytics.fisher_transformation_indicator(tenor, time_col_name, high_col_name, low_col_name)
```

The Fisher Transform is a technical indicator created by J.F. Ehlers that converts prices into a Gaussian normal distribution.
In this way, the indicator highlights when prices have moved to an extreme, based on recent prices. This may help in spotting
turning points in the price of an asset. It also helps show the trend and isolate the price waves within a trend.

**Parameters**

- `time_col_name` (str) – name of time column
- `high_col_name` (str) – input array of high prices over bar
- `low_col_name` (str) – input array of low prices over bar

**Return type**
`Callable[. . . , Column]`

**Returns** pandas/Spark user defined scalar function

## Force index

```
aws.finspace.timeseries.spark.analytics.force_index_indicator(tenor, time_col_name, price_col_name, volume_col_name)
```

The force index is a technical indicator that measures the amount of power used to move the price of an asset.
The term and its formula were developed by psychologist and trader AlexanderElder and published in his 1993 book Trading for a Living.
The force index uses price and volume to determine the amount of strength behind a price move. The index is an oscillator, fluctuating
between positive and negative territory. It is unbounded meaning the index can go up or down indefinitely.

**Parameters**

- `tenor` – look back window
- `time_col_name` – name of time column
- `price_col_name` – input array of closing prices over bar
- `volume_col_name` – input array of total volume over bar

**Return type**
`Callable[. . . , Column]`

**Returns** pandas/Spark user defined scalar function

## Hull moving average (HMA)

```
aws.finspace.timeseries.spark.analytics.hull_moving_average_indicator(tenor, time_col_name, price_col_name)
```

The Hull Moving Average (HMA) was developed by Alan Hull for the purpose of reducing lag, increasing
responsiveness while at the same time eliminating noise. Its calculation is elaborate and makes use of the Weighted Moving Average (WMA).
It emphasizes recent prices over older ones, resulting in a fast-acting yet smooth moving average that can be used to identify the
prevailing market trend.

**Parameters**

- `tenor` (int) – look back
- `time_col_name` (str) – name of time column
- `price_col_name` – input array of closing prices over bar

**Return type**
`Callable[. . . , Column]`

**Returns** pandas/Spark user defined scalar function

## Ichimoku study

```
aws.finspace.timeseries.spark.analytics.ichimoku_indicator(time_col_name, price_col_name, short_period=9, medium_period=26, long_period=52)
```

The Ichimoku study was developed by Goichi Hosoda pre-World War II as a forecasting model for financial markets.
The study is a trend following indicator that identifies mid-points of historical highs and lows at different
lengths of time and generates trading signals similar to that of moving averages/MACD. A key difference between
Ichimoku and moving averages is Ichimoku charts lines are shifted forward in time creating wider support/resistance
areas mitigating the risk of false breakouts. Learn [more](https://www.investopedia.com/terms/i/ichimoku-cloud.asp "https://www.investopedia.com/terms/i/ichimoku-cloud.asp").

**Parameters**

- `time_col_name` (str) – name of time column
- `price_col_name` (str) – input array of asset prices, determined by user, default is close for intraday calculations
- `short_period` (int) – short period window, usually 9
- `medium_period` (int) – long period window, usually 26
- `long_period` (int) – long period window, usually 52

**Return type**
`Callable[. . . , Column]`

**Returns** pandas/Spark user defined scalar function

## Kaufman adaptive moving average (KAMA)

```
aws.finspace.timeseries.spark.analytics.kama_indicator(time_col_name, price_col_name, er_period=10, fast_ema_period=30, slow_ema_period=2)
```

Developed by Perry Kaufman, Kaufman's Adaptive Moving Average (KAMA) is a moving average designed to account for market noise or volatility.
KAMA will closely follow prices when the price swings are relatively small and the noise is low. KAMA will adjust when the price swings
widen and follow prices from a greater distance. This trend-following indicator can be used to identify the overall trend, time turning
points and filter price movements.

**Parameters**

- `time_col_name` (str) – name of time column
- `price_col_name` (str) – input array of prices over bar
- **er_period** (int) – efficiency ratio tenor
- **slow_ema_period** (int)
- **fast_ema_period** (int)

**Return type**
`Callable[. . . , Column]`

**Returns** pandas/Spark user defined scalar function

## Keltner channel

```
aws.finspace.timeseries.spark.analytics.keltner_indicator(time_col_name, price_col_name, high_col_name, low_col_name, atr_factor=2, ewm_tenor=20, atr_tenor=20)
```

The Keltner Channel was introduced in 1960 by Chester W. Keltner in his book **How To Make Money in Commodities**,
and is also explained by Perry Kaufman's book **The New Commodity Trading Systems and Methods**. Keltner Channels plots three lines,
consisting of a exponential moving average (typically of the average price) with upper and lower bands plotted above and below
this moving average.The width of the bands is based on a user defined factor applied to the Average True Range, with this result added
to and subtracted from the middle moving average line.

**Parameters**

- `time_col_name` (str) – name of time column
- `price_col_name` (str) – input array of asset prices, determined by user, default is close for intraday calculations
- `high_col_name` (str) – input array of high asset prices
- `low_col_name` (str) – input array of high asset price
- **atr_factor** (float) – ATR multiplier
- **ewm_tenor** (int) – tenor of expo moving average
- **atr_tenor** (int) – tenor of ATR

**Return type**
`Callable[. . . , Column]`

**Returns** pandas/Spark user defined scalar function

## Klinger oscillator indicator

```
aws.finspace.timeseries.spark.analytics.klinger_oscillator_indicator(short_period, long_period, time_col_name, price_col_name, high_col_name, low_col_name, volume_col_name)
```

The indicator was developed by Stephen Klinger to determine the long-term trend of money flow while remaining sensitive enough to detect
short-term fluctuations. The indicator compares the volume flowing through securities with the security price movements and then converts
the result into an oscillator. The Klinger oscillator shows the difference between two moving averages which are based on more than price.
Traders watch for divergence on the indicator to signal potential price reversals. Like other oscillators, a signal line can be added to
provide additional trade signals.

**Parameters**

- `short_period` (int) – short exponential moving average look back typically 34
- `long_period` (int) – long exponential moving average look back typically 55
- `time_col_name` (str) – name of time column
- `price_col_name` (str) – input array of high prices over bar
- `high_col_name` (str) – input array of high prices over bar
- `low_col_name` (str) – input array of low prices over bar
- `volume_col_name` (str) – input array of total volume over bar

**Return type**
`Callable[. . . , Column]`

**Returns** pandas/Spark user defined scalar function

## Linear regression

```
aws.finspace.timeseries.spark.analytics.linear_regression(tenor, time_col_name, input1_col_name, input2_col_name)
```

Takes two arrays of asset prices and then produces slope and intercept, where input1_col_name is the independent variable and
input2_col_name is the dependent variable.

**Parameters**

- `tenor` (int) – window size
- `time_col_name` (str) – name of time column
- `input1_col_name` (str) – name of input array column
- `input2_col_name` (str) – name of input array column

**Return type**
`Callable[. . . , Column]`

**Returns** pandas/Spark user defined scalar function

## Linear weighted moving average

```
aws.finspace.timeseries.spark.analytics.linear_weighted_moving_average(tenor, time_col_name, price_col_name)
```

Learn [more](https://www.investopedia.com/terms/l/linearlyweightedmovingaverage.asp "https://www.investopedia.com/terms/l/linearlyweightedmovingaverage.asp").

**Parameters**

- `tenor` (int) – interval length
- `time_col_name` (str) – name of time column
- `price_col_name` (str) – input array of asset prices, determined by user, default is close for intraday calculations

**Return type**
`Callable[. . . , Column]`

**Returns** pandas/Spark user defined scalar function

## Mass index

```
aws.finspace.timeseries.spark.analytics.mass_index_indicator(ema_period, sum_period, time_col_name, high_col_name, low_col_name)
```

Mass index is a form of technical analysis that examines the range between high and low stock prices over a period
of time. Mass index, developed by Donald Dorsey in the early 1990s, suggests that a reversal of the current trend will likely
take place when the range widens beyond a certain point and then contracts.

**Parameters**

- `ema_period` – look back for exponential moving average typically 9 periods
- `sum_period` – look back for sum of exponential moving average typically 25 periods
- `time_col_name` – name of time column
- `high_col_name` – input array of high prices over bar
- `low_col_name` – input array of low prices over bar

**Return type**
`Callable[. . . , Column]`
**Returns** pandas/Spark user defined scalar function

## Max indicator

```
aws.finspace.timeseries.spark.analytics.max_indicator(tenor, time_col_name, price_col_name)
```

Compute max over look back period

**Parameters**

- `tenor` (int) – window size
- `time_col_name` (str) – name of time column
- `price_col_name` (str) – input array of prices over bar

**Return type**
`Callable[. . . , Column]`

**Returns** pandas/Spark user defined scalar function

## Money flow indicator

```
aws.finspace.timeseries.spark.analytics.mf_indicator(tenor, time_col_name, price_col_name, high_col_name, low_col_name, vol ume_col_name)
```

The Money Flow Index (MFI) was developed by Gene Quong and Avrum Soudack. It uses both price and volume to measure buying and
selling pressure.

**Parameters**

- `tenor` (int) – look back period
- `time_col_name` (str) – name of time column
- `price_col_name` (str) – input array of asset prices, determined by user, default is close for intraday calculations
- `high_col_name` (str) – input array of high asset prices over bar
- `low_col_name` (str) – input array of low asset price over bar
- `volume_col_name` (str) – input array of total volume over bar

**Return type**
`Callable[. . . , Column]`

**Returns** pandas/Spark user defined scalar function

## MidPoint indicator

```
aws.finspace.timeseries.spark.analytics.midpoint_indicator(tenor, time_col_name, price_col_name)
```

The Midpoint calculation is similar to the Midprice, except the highest and lowest values are returned from the
same input field. The default indicator calculates the highest close and lowest close within the look back period and averages
the two values.

**Parameters**

- `tenor` (int) – window size
- `time_col_name` (str) – name of time column
- `price_col_name` (str) – input array of closing prices over bar

**Return type**
`Callable[. . . , Column]`

**Returns** pandas/Spark user defined scalar function

## MidPrice indicator

```
aws.finspace.timeseries.spark.analytics.midprice_indicator(tenor, time_col_name, high_col_name, low_col_name)
```

The Midprice returns the midpoint value from two different input fields. The default indicator calculates the
highest high and lowest low within the look back period and averages the two values to return the Midprice.

**Parameters**

- `tenor` (int) – window size
- `time_col_name` (str) – name of time column
- `high_col_name` (str) – input array of high prices over bar
- `low_col_name` (str) – input array of low prices over bar

**Return type**
`Callable[. . . , Column]`

**Returns** pandas/Spark user defined scalar function

## Min

```
aws.finspace.timeseries.spark.analytics.*min_indicator*(tenor, time_col_name, price_col_name)
```

Compute minimum value over look back period.

**Parameters**

- `tenor` (int) – window size
- `time_col_name` (str) – name of time column
- `price_col_name` (str) – input array of prices over bar

**Return type**
`Callable[. . . , Column]`

**Returns** pandas/Spark user defined scalar function

## Min and max over period

```
aws.finspace.timeseries.spark.analytics.minmax_indicator(tenor, time_col_name, price_col_name)
```

Min and Max over a tenor period.

**Parameters**

- `tenor` (int) – window size
- `time_col_name` (str) – name of time column
- `price_col_name` (str) – input array of prices over bar

**Return type**
`Callable[. . . , Column]`

**Returns** pandas/Spark user defined scalar function

## Momentum

```
aws.finspace.timeseries.spark.analytics.momentum_indicator(tenor, time_col_name, input_array_col_name)
```

Compute momentum

**Parameters**

- `tenor` (int) – window size
- `time_col_name` (str) – name of time column
- `input_array_col_name` (str) – name of input array column

**Return type**
`Callable[. . . , Column]`

**Returns** pandas/Spark user defined scalar function

## Moving average

```
aws.finspace.timeseries.spark.analytics.moving_average(tenor, time_col_name, input_array_col_name)
```

Compute moving average on window of tenor size utilizing function average_at_point

**Parameters**

- `tenor` (int) – window size
- `time_col_name` (str) – name of time column
- `input_array_col_name` (str) – name of input array column

**Return type**
`Callable[. . . , Column]`

**Returns** pandas/Spark user defined scalar function

## Moving average convergence divergence (MACD)

```
aws.finspace.timeseries.spark.analytics.moving_average_converge_diverge(short_tenor, long_tenor, time_col_name, input_array_col_name)
```

The Moving Average Convergence Divergence (MACD) was developed by Gerald Appel, and is based on the
differences between two moving averages of different lengths, a Fast and a Slow moving average.
A second line, called the Signa line is plotted as a moving average of the MACD. A third line, called the
MACD Histogram is optionally plotted as a histogram of the difference between the MACD and the Signal Line. Learn [more](https://www.investopedia.com/terms/m/macd.asp "https://www.investopedia.com/terms/m/macd.asp").

**Parameters**

- `short_tenor` (int) – short window size
- `long_tenor` (int) – long window size
- `time_col_name` (str) – name of time column
- `input_array_col_name` (str) – name of input array column

**Return type**
`Callable[. . . , Column]`

**Returns** pandas/Spark user defined scalar function

## Moving average convergence divergence historical (MACD)

```
aws.finspace.timeseries.spark.analytics.moving_average_converge_diverge_hist(short_tenor, long_tenor, signal_line_tenor, time_col_name, input_array_col_name)
```

**Parameters**

- `short_tenor` (int) – short window size
- `long_tenor` (int) – long window size
- `signal_line_tenor` (int) – signal line tenor size
- `time_col_name` (str) – name of time column
- `input_array_col_name` (str) – name of input array column

**Return type**
`Callable[. . . , Column]`

**Returns** pandas/Spark user defined scalar function

## Normalized average true range (NATR)

```
aws.finspace.timeseries.spark.analytics.natr_indicator(tenor, time_col_name, price_col_name, high_col_name, low_col_name)
```

Normalized Average True Range (NATR) attempts to normalize the average true range values across instruments by using the formula below.

**Parameters**

- `tenor` (int) – look back period
- `time_col_name` (str) – name of time column
- `price_col_name` (str) – input array of asset prices, determined by user, default is close for intraday calculations
- `high_col_name` (str) – input array of high asset prices
- `low_col_name` (str) – input array of high asset price

**Return type**
`Callable[. . . , Column]`

**Returns** pandas/Spark user defined scalar function

## Directional movement (DM)

```
aws.finspace.timeseries.spark.analytics.neg_dm_indicator(time_col_name, high_col_name, low_col_name)
```

Directional Movement (DM) is defined as the largest part of the current period price range that lies outside the previous period price
range.

**Parameters**

- `time_col_name` (str) – name of time column
- `price_col_name` – input array of closing prices over bar
- `high_col_name` (str) – input array of high prices over bar
- `low_col_name` (str) – input array of low prices over bar

**Return type**
`Callable[. . . , Column]`

**Returns** pandas/Spark user defined scalar function

## Negative volume index (NVI)

```
aws.finspace.timeseries.spark.analytics.negative_volume_indicator(period, time_col_name, price_col_name, volume_col_name)
```

The Negative Volume Index (NVI) is a cumulative indicator that uses the change in volume to decide when the
smart money is active. Paul Dysart first developed this indicator in the 1930s. Dysart's Negative Volume Index works under the
assumption that the smart money is active on days when volume decreases and the not-so-smart money is active on days when volume increases.

**Parameters**

- `period`(int) – returns period typically 1
- `time_col_name` (str) – name of time column
- `price_col_name` (str) – input array of closing prices over bar
- `volume_col_name` (str) – input array of total volume over bar

**Return type**
`Callable[. . . , Column]`

**Returns** pandas/Spark user defined scalar function

## Balance volume (OBV)

```
aws.finspace.timeseries.spark.analytics.on_balance_volume(time_col_name, price_col_name, volume_col_name)
```

On Balance Volume (OBV) maintains a cumulative running total of the amount of volume occurring on up
periods compared to down periods. Learn [more](https://www.investopedia.com/terms/o/onbalancevolume.asp "https://www.investopedia.com/terms/o/onbalancevolume.asp").

**Parameters**

- `time_col_name` (str) – name of time column
- `price_col_name` (str) – array of asset prices
- `volume_col_name` (str) – array of volume associated with prices

**Return type**
`Callable[. . . , Column]`

**Returns** pandas/Spark user defined scalar function

## Pairwise realized correlation

```
aws.finspace.timeseries.spark.analytics.pairwise_realized_correlation(tenor, time_col_name, asset1_col_name,  asset2_col_name)
```

Takes two arrays of asset prices and then produces a pairwise correlation, returns nan if the array is less than window.

**Parameters**

- `tenor` (int) – window size
- `time_col_name` (str) – name of time column
- `asset1_col_name` (str) – name of input array column
- `asset2_col_name` (str) – name of input array column

**Return type**
`Callable[. . . , Column]`

**Returns** pandas/Spark user defined scalar function

## Percent price oscillator (PPO)

```
aws.finspace.timeseries.spark.analytics.percentage_price_oscillator(short_period, long_period,  signal_line_period, time_col_name, price_col_name)
```

Compute Percentage price oscillator. The Percent Price Oscillator (PPO) is based on the differences between two moving averages of
different lengths, a Fast and a Slow moving average. The PPO is the difference of the two averages divided by the slower of the
two moving averages, which tends to normalize the values across different instruments.

**Parameters**

- `short_period` (int) – slow ema period
- `long_period` (int) – slow ema period
- `signal_line_period` (int) – signal line ema period
- `time_col_name` (str) – name of time column
- `price_col_name` (str) – input array of prices

**Return type**
`Callable[. . . , Column]`

**Returns** pandas/Spark user defined scalar function

## Directional movement (DM)

```
aws.finspace.timeseries.spark.analytics.pos_dm_indicator(time_col_name, high_col_name, low_col_name)
```

Directional Movement (DM) is defined as the largest part of the current period's price range that lies outside the previous period's price range.

**Parameters**

- `time_col_name` (str) – name of time column
- `price_col_name` – input array of closing prices over bar
- `high_col_name` (str) – input array of high prices over bar
- `low_col_name` (str) – input array of low prices over bar

**Return type**
`Callable[. . . , Column]`

**Returns** pandas/Spark user defined scalar function

## Price channel

```
aws.finspace.timeseries.spark.analytics.price_channel_indicator(tenor, time_col_name, price_col_name)
```

The Price Channel displays two lines, with the upper line representing the highest price and the lower line
representing the lowest price for a given look back interval. The bands can optionally be smoothed with a moving average,
or shifted to the right with an offset value. Basic uses of the Price Channel are to identify breakouts form the channel and
to determine placement of trailing stops.

**Parameters**

- `tenor` (int) – window size
- `time_col_name` (str) – name of time column
- `price_col_name` (str) – input array of prices

**Return type**
`Callable[. . . , Column]`

**Returns** pandas/Spark user defined scalar function

## Price volume trend (PVT)

```
aws.finspace.timeseries.spark.analytics.pvt_indicator(time_col_name, price_col_name, volume_col_name)
```

Compute price volume indicator. The Price Volume Trend (PVT) study attempts to quantify the amount of
volume flowing into or out of an instrument by identifying the close of the period in relation to the previous period's close.
The volume for the period is then allocated accordingly to a running continuous total.

**Parameters**

- `time_col_name` (str) – name of time column
- `price_col_name` (str) – input array of asset prices, determined by user, default is close for intraday calculations
- `volume_col_name` (str) – input array of volumes at the asset prices

**Return type**
`Callable[. . . , Column]`

**Returns** pandas/Spark user defined scalar function

## Realized correlation matrix

```
aws.finspace.timeseries.spark.analytics.realized_correlation_matrix(tenor, time_col_name, *kwargs)
```

**Return type**
`Callable[. . . , Column]`

**Returns** pandas/Spark user defined scalar function

## Realized volatility

```
aws.finspace.timeseries.spark.analytics.realized_volatility(tenor, time_col_name, asset_price_col_name)
```

Takes in an array of asset prices and computes realized volatility. Learn [more](https://en.wikipedia.org/wiki/Realized_variance "https://en.wikipedia.org/wiki/Realized_variance").

**Parameters**

- `tenor` (int) – window size
- `time_col_name` (str) – name of time column
- **asset_price_col_name** – name of input array column

**Return type**
`Callable[. . . , Column]`

**Returns** pandas/Spark user defined scalar function

## Realized volatiliy spread

```
aws.finspace.timeseries.spark.analytics.realized_volatility_spread(tenor, time_col_name, asset1_col_name, asset2_col_name)
```

Compute realized volatility spread between two assets.

**Parameters**

- `tenor` (int) – window size
- `time_col_name` (str) – name of time column
- `asset1_col_name` (str) – name of input array column
- `asset2_col_name` (str) – name of input array column

**Return type**
`Callable[. . . , Column]`

**Returns** pandas/Spark user defined scalar function

## Rate of change (ROC)

```
aws.finspace.timeseries.spark.analytics.roc_indicator(tenor, time_col_name, input_array_col_name)
```

The Rate of Change (ROC) indicator compares the current price with the previous price from a selected number
of periods ago. The current price is divided by the previous price and expressed as a percentage. This indicator is also commonly known
as a momentum indicator. Learn [more](https://www.investopedia.com/terms/p/pricerateofchange.asp "https://www.investopedia.com/terms/p/pricerateofchange.asp").

**Parameters**

- `tenor` (int) – window size
- `time_col_name` (str) – name of time column
- `input_array_col_name` (str) – name of input array column

**Return type**
`Callable[. . . , Column]`

**Returns** pandas/Spark user defined scalar function

## Relative strength index (RSI)

```
aws.finspace.timeseries.spark.analytics.rsi(tenor, time_col_name, input_array_col_name)
```

The Relative StrengthIndex (RSI) was published by J. Welles Wilder. The current price is normalized as a percentage between 0 and 100.
The name of this oscillator is misleading because it does not compare the instrument relative to another instrument or set of instruments,
but rather represents the current price relative to other recent pieces within the selected look back window length.
Learn [more](https://www.investopedia.com/terms/r/rsi.asp "https://www.investopedia.com/terms/r/rsi.asp").

**Parameters**

- `tenor` (int) – window size
- `time_col_name` (str) – name of time column
- `input_array_col_name` (str) – name of input array column

**Return type**
`Callable[. . . , Column]`

**Returns** pandas/Spark user defined scalar function

## Parabolic stop and reverse (SAR)

```
aws.finspace.timeseries.spark.analytics.sar_indicator(time_col_name, price_col_name, high_col_name, low_col_name, period=2, af=0.02, sar_rising=True)
```

The Parabolic Stop and Reverse (SAR) calculates trailing stop points to use with long and short positions. The SAR was published by
J. Welles Wilderas part of a complete trend following system. The dotted lines above the price designate trailing stops for short positions;
those below the price are sell stops for long positions.

**Parameters**

- `time_col_name` – name of time column
- `price_col_name` – input array of closing prices over bar
- `high_col_name` – input array of high prices over bar
- `low_col_name` – input array of low prices over bar
- `period` – window size

**Return type**
`Callable[. . . , Column]`

**Returns** pandas/Spark user defined scalar function

## Slow stock oscillator

```
aws.finspace.timeseries.spark.analytics.slow_stock_oscillator(tenor, time_col_name, price_col_name, high_col_name, low_col_name)
```

The Stochastic (Stoch) normalizes price as a percentage between 0 and 100. Normally two lines are plotted, the %K line and a
moving average of the %K which is called %D. A slow stochastic can be created by initially smoothing the %K line with a moving
average before it is displayed. The length of this smoothing is set in the Slow K Period. Without the initial smoothing (i.e., setting the
Slow K Period to a valueof 1 ) the %K becomes the **Raw %K** value, and is also known as a fast stochastic. Learn [https://www.investopedia.com/terms/s/stochasticoscillator.asp](https://www.investopedia.com/terms/s/stochasticoscillator.asp "https://www.investopedia.com/terms/s/stochasticoscillator.asp") [more].

**Parameters**

- `tenor` (int) – look back period
- `time_col_name` (str) – name of time column
- `price_col_name` (str) – input array of asset prices, determined by user, default is close for intraday calculations
- `high_col_name` (str) – input array of high asset prices
- `low_col_name` (str) – input array of high asset price

**Return type**
`Callable[. . . , Column]`

**Returns** pandas/Spark user defined scalar function

## Standard deviation indicator

```
aws.finspace.timeseries.spark.analytics.stddev_indicator(tenor, time_col_name, price_col_name)
```

Compute standard deviation over a window.

**Parameters**

- `tenor` (int) – window size
- `time_col_name` (str) – name of time column
- `price_col_name` (str) – input array of closing prices over bar

**Return type**
`Callable[. . . , Column]`

**Returns** pandas/Spark user defined scalar function

## Stochastic RSI (StochRSI)

```
aws.finspace.timeseries.spark.analytics.stoch_rsi_indicator(rsi_tenor, tenor, time_col_name, price_col_name)
```

The Stochastic RSI (StochRSI) is an indicator used in technical analysis that ranges between zero and one
(or zero and 100 on some charting platforms) and is created by applying the Stochastic oscillator formula to a set of
relative strength index (RSI) values rather than to standard price data. Using RSI values within the Stochastic formula gives
traders an idea of whether the current RSI value is overbought or oversold.

**Parameters**

- **rsi_tenor** (int) – window size for rsi
- `tenor` (int) – window size for stoch rsi
- `time_col_name` (str) – name of time column
- `price_col_name` (str) – input array of closing prices over bar

**Return type**
`Callable[. . . , Column]`

**Returns** pandas/Spark user defined scalar function

## Triple exponential moving average (T3)

```
aws.finspace.timeseries.spark.analytics.t3_ema_indicator(tenor, time_col_name, price_col_name)
```

The Triple Exponential Moving Average (T3) by Tim Tillson attempts to offers a moving average with better smoothing
then traditional exponential moving average.

`EMA1 = EMA(x,Period) EMA2 = EMA(EMA1,Period) GD = EMA1*(1+vFactor)) - (EMA2*vFactor) T3 = GD (GD ( GD(t, Period, vFactor), Period, vFactor), Period, vFactor)`

Where vFactor is a volume factor between 0 and 1 which determines how the moving averages responds. A value of 0 returns an EMA.
A value of 1 returns DEMA. Tim Tillson advised or preferred a value of 0.7.

**Parameters**

- `tenor` – window size
- `time_col_name` – name of time column
- `price_col_name` – input array of closing prices over bar

**Return type**
`Callable[. . . , Column]`

**Returns** pandas/Spark user defined scalar function

## Time series forecast (TSF)

```
aws.finspace.timeseries.spark.analytics.time_series_forecast_indicator(tenor, scale, time_col_name, time_axis_col_name, price_col_name)
```

The Time Series Forecast (TSF) indicator displays the statistical trend of a security's price over a specified time period.
The trend is based on linear regression analysis. Rather than plotting a straight linear regression trend line, the Time Series
Forecast plots the last point of multiple linear regression trend lines. The difference between the TSF and the moving linear regression
is that the TSF adds the slope of the linear regression to the linear regression essentially projecting the position of the linear regression
forward one period.

**Parameters**

- `tenor` (str) – look back
- `scale` (str) – time scale, either minutes or seconds or days
- `time_col_name` (str) – name of time column
- `time_axis_col_name` (str) – name of independent time column
- `price_col_name` (str) – input array of closing prices over bar

**Return type**
`Callable[. . . , Column]`

**Returns** pandas/Spark user defined scalar function

## True range

```
aws.finspace.timeseries.spark.analytics.tr_indicator(time_col_name,  price_col_name, high_col_name, low_col_name)
```

Calculate True Range.

**Parameters**

- `time_col_name` (str) – name of time column
- `price_col_name` (str) – input array of closing prices over bar
- `high_col_name` (str) – input array of high prices over bar
- `low_col_name` (str) – input array of low prices over bar

**Return type**
`Callable[. . . , Column]`

**Returns** pandas/Spark user defined scalar function

## Triangular simple moving average

```
aws.finspace.timeseries.spark.analytics.trima_indicator(tenor, time_col_name, price_col_name)
```

Triangular Simple Moving Average.

**Parameters**

- `tenor` (int) – window size
- `time_col_name` (str) – name of time column
- `price_col_name` (str) – input array of prices

**Return type**
`Callable[. . . , Column]`

**Returns** pandas/Spark user defined scalar function

## Triple exponential moving average (TEMA)

```
aws.finspace.timeseries.spark.analytics.triple_exponential_moving_average(tenor,time_col_name, price_col_name)
```

The Triple Exponential Moving Average (TEMA) by Patrick Mulloy offers a moving average with less lag than traditional exponential moving average.

**Parameters**

- `tenor` (int) – look back period
- `time_col_name` (str) – name of time column
- `price_col_name` (str) – input array of asset prices, determined by user, default is close for intraday calculations

**Return type**
`Callable[. . . , Column]`

**Returns** pandas/Spark user defined scalar function

## Triple exponential moving average oscillator (TRIX)

```
aws.finspace.timeseries.spark.analytics.trix_indicator(tenor, time_col_name, price_col_name)
```

The Triple Exponential Moving AverageOscillator (TRIX) by Jack Hutson is a momentum indicator that oscillates around zero. It displays
the percentage rate of change between two triple smoothed exponential moving averages.

**Parameters**

- `tenor` (int) – window size
- `time_col_name` (str) – name of time column
- `price_col_name` (str) – input array of prices

**Return type**
`Callable[. . . , Column]`

**Returns** pandas/Spark user defined scalar function

## Timeseries linear regression

```
aws.finspace.timeseries.spark.analytics.ts_linear_regression(tenor, scale, time_col_name, time_axis_col_name, value_axis_col_name)
```

Takes two arrays, the first is the time axis, and the second is the value axis and then produces slope and intercept,
where time axis is the independent variable and arr2 is the dependent variable.
**Parameters**

- `tenor` (int) – look back period
- `scale`(str) – scale of time axis, can take value of seconds, or minutes
- `time_col_name` (str) – name of time column
- `time_axis_col_name` (str) – input array of datetime
- `value_axis_col_name` (str) input array of values

**Return type**
`Callable[. . . , Column]`

**Returns** pandas/Spark user defined scalar function

## Typical price

```
aws.finspace.timeseries.spark.analytics.typical_price_indicator(tenor, time_col_name, price_col_name, high_col_name, low_col_name)
```

Typical Price calculation defined as `(High + Low + Close) / 3`.

**Parameters**

- `tenor` (int) – look back window
- `time_col_name` (str) – name of time column
- `price_col_name` (str) – input array of closing prices over bar
- `high_col_name` (str) – input array of high prices over bar
- `low_col_name` (str) – input array of low prices over bar

**Return type**
`Callable[. . . , Column]`

**Returns** pandas/Spark user defined scalar function

## Ult oscillator

```
aws.finspace.timeseries.spark.analytics.ult_osc_indicator(time_col_name, price_col_name, high_col_name, low_col_name)
```

**Parameters**

- `time_col_name` (str) – name of time column
- `price_col_name` (str) – input array of asset prices, determined by user, default is close for intraday calculations
- `high_col_name` (str) – input array of high asset prices
- `low_col_name` (str) – input array of high asset price

**Return type**
`Callable[. . . , Column]`

**Returns** pandas/Spark user defined scalar function

## Weighted close price

```
aws.finspace.timeseries.spark.analytics.weighted_close_indicator(tenor, time_col_name, price_col_name, high_col_name, low_col_name)
```

Weighted Close Price calculation defined as `(High+ Low + 2*Close) / 4`

**Parameters**

- `tenor` (int) – look back window
- `time_col_name` (str) – name of time column
- `price_col_name` (str) – input array of closing prices over bar
- `high_col_name` (str) – input array of high prices over bar
- `low_col_name` (str) – input array of low prices over bar

**Return type**
`Callable[. . . , Column]`

**Returns** pandas/Spark user defined scalar function

## Weighted linear regression

```
aws.finspace.timeseries.spark.analytics.weighted_linear_regression(tenor, time_col_name, input_arr1_col_name_, input_arr2_col_name_, weights_col_name)
```

Takes three arrays, the first is the independent axis, and the second is the value axis and third is weights and then
produces slope and intercept.

**Parameters**

- `tenor`(str) – look back period
- `time_col_name` (str) – name of time column
- `input_arr1_col_name` – input array of independent variables
- `input_arr2_col_name` – input array of dependent variables
- `weights_col_name` (str) – input array of weights

**Return type**
`Callable[. . . , Column]`

**Returns** pandas/Spark user defined scalar function

## Weighted TS linear regression

```
aws.finspace.timeseries.spark.analytics.weighted_ts_linear_regression(tenor, scale, time_col_name, time_axis_col_name, value_axis_col_name, weights_axis_col_name)
```

Takes three arrays, the first is the time axis, and the second is the value axis and third is weights and then produces
slope and intercept, where time axis is the independent variable and value_axis is the dependent variable, and weights.

**Parameters**

- `tenor`(str) – look back period
- `scale` (str) – scale of time axis, can take value of seconds, or minutes
- `time_col_name` (str) – name of time column
- `time_axis_col_name` (str) – input array of datetime
- `value_axis_col_name` (str) – input array of values
- `weights_axis_col_name` (str) – input array of weights

**Return type**
`Callable[. . . , Column]`

**Returns** pandas/Spark user defined scalar function

## Welles wilder smoothing average (WWS)

```
aws.finspace.timeseries.spark.analytics.wilder_smoothing_indicator(tenor, time_col_name, price_col_name)
```

The Welles Wilder's Smoothing Average (WWS) was developed by J. Welles Wilder, Jr. and is part of the Wilder's RSI indicator
implementation. This indicator smoothes price movements to help you identify and spot bullish and bearish trends.

**Parameters**

- `tenor` (int) – window size
- `time_col_name` (str) – name of time column
- `price_col_name` (str) – input array of closing prices over bar

**Return type**
`Callable[. . . , Column]`

**Returns** pandas/Spark user defined scalar function

## %R

```
aws.finspace.timeseries.spark.analytics.will_r_indicator(tenor, time_col_name, price_col_name, high_col_name, low_col_name)
```

Compute william %R indicator. The %R indicator was developed by Larry Williams and introduced in his 1979 book **How I Made $1,000,000 Trading Commodities Last Year**.
Williams %R is similar to a stochastic oscillator, as it normalizes price as a percentage between 0 and 100. It is basically an inverted version of the **Raw %K** value of a Fast Stochastic.

**Parameters**

- `tenor` (int) – look back period
- `time_col_name` (str) – name of time column
- `price_col_name` (str) – input array of asset prices, determined by user, default is close for intraday calculations
- `high_col_name` (str) – input array of high asset prices
- `low_col_name` (str) – input array of high asset price

**Return type**
`Callable[. . . , Column]`

**Returns** pandas/Spark user defined scalar function

## Rate of change (ROC100)

```
aws.finspace.timeseries.spark.analytics.ROC100_indicator(tenor, time_col_name, price_col_name)
```

The Rate of Change (ROC100) indicator compares the current price with the previous price from a selected number of periods ago.
The current price is divided by the previous price and multiplied by 100. This indicator is also commonly known as a momentum indicator.

**Parameters**

- `tenor` (int) – window size
- `time_col_name` (str) – name of time column
- `price_col_name` (str) – input array of prices

**Return type**
`Callable[. . . , Column]`

**Returns** pandas/Spark user defined scalar function

## Rate of change percentage (ROCP)

```
aws.finspace.timeseries.spark.analytics.ROCP_indicator(tenor, time_col_name, price_col_name)
```

The Rate of Change Percentage (ROCP) indicator compares the current price with the previous price from a selected number of periods ago.
The current price is divided by the previous price. ROCP is not expressed as a percentage. This indicator is also commonly known as a momentum indicator.

**Parameters**

- `tenor` (int) – window size
- `time_col_name` (str) – name of time column
- `price_col_name` (str) – input array of prices

**Return type**
`Callable[. . . , Column]`

**Returns** pandas/spark user defined scalar function

## Rate of change rate (ROCR)

```
aws.finspace.timeseries.spark.analytics.ROCR_indicator(tenor, time_col_name, price_col_name)
```

The Rate of Change Rate (ROCR) indicator compares the current price with the previous price from a selected number of periods ago.
The current price is divided by the previous price. This indicator is also commonly known as a momentum indicator.

**Parameters**

- `tenor` (int) – window size
- `time_col_name` (str) – name of time column
- `price_col_name` (str) – input array of prices

**Return type**
`Callable[. . . , Column]`

**Returns** pandas/spark user defined scalar function
