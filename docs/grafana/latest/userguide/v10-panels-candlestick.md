

# Candlestick
<a name="v10-panels-candlestick"></a>

****  
This documentation topic is designed for Grafana workspaces that support **Grafana version 10.x**.  
For Grafana workspaces that support Grafana version 12.x, see [Working in Grafana version 12](using-grafana-v12.md).  
For Grafana workspaces that support Grafana version 9.x, see [Working in Grafana version 9](using-grafana-v9.md).  
For Grafana workspaces that support Grafana version 8.x, see [Working in Grafana version 8](using-grafana-v8.md).

The Candlestick visualization allows you to visualize data that includes a number of consistent dimensions focused on price movement. The Candlestick panel includes an Open-High-Low-Close (OHLC) mode, as well as support for additional dimensions based on time series data.

![An image showing an example of a candlestick visualization in Grafana.](http://docs.aws.amazon.com/grafana/latest/userguide/images/viz/candlestick-panel-example.png)


Candlestick visualizations build upon the foundation of the [Time series](v10-panels-time-series.md) and includes many common configuration settings.

## Mode
<a name="v10-panels-candlestick-mode"></a>

The mode options allow you to toggle which dimensions are used for the visualization.
+ **Candles** – Limit the panel dimensions to the open, high, low, and close dimensions used by candlestick visualizations.
+ **Volume** – Limit the panel dimension to the volume dimension.
+ **Both** – The default behavior for the candlestick panel. It includes both candlestick and volume visualizations.

## Candle style
<a name="v10-panels-candlestick-style"></a>
+ **Candles** – The default display style, creates candle-style visualizations between the open and close dimensions.
+ **OHLC Bars** – Display the four core dimensions open, high, low, and close values.

## Color strategy
<a name="v10-panels-candlestick-color"></a>
+ **Since Open** – The default behavior. This mode will utilize the *Up* color (below) if the intra-period price movement is positive. In other words, if the value on close is greater or equal to the value on open, the *Up* color is used.
+ **Since Prior Close** – An alternative display method where the color of the candle is based on the inter-period price movement or change in value. In other words, if the value on open is greater than the previous value on close, the *Up* color is used. If the value on open is lower than the previous value on close, the *Down* color is used. *This option also triggers the hollow candlestick visualization mode*. Hollow candlesticks indicate that the intra-period movement is positive (value is higher on close than on open), filled candlesticks indicate the intra-period change is negative (value is lower on close than on open). To learn more, see the [explanation of the differences](https://thetradingbible.com/how-to-read-hollow-candlesticks).

## Up & down colors
<a name="v10-panels-candlestick-updown"></a>

The **Up color** and **Down color** options select which colors are used when the price movement is up or down. The *Color strategy* above will determine if intra-period or inter-period price movement is used to select the candle or OHLC bar color.

## Open, high, low, close
<a name="v10-panels-candlestick-ohlc"></a>

The candlestick panel will attempt to map fields to the appropriate dimension.
+ **Open** corresponds to the starting value of the given period.
+ **High** corresponds to the highest value of the given period.
+ **Low** corresponds to the lowest value of the given period.
+ **Close** corresponds to the final (end) value of the given period.
+ **Volume** corresponds to the sample count in the given period. (e.g. number of trades)

**Note**  
The candlestick legend doesn't display these values.

To properly map these dimensions, the query results table from your data must include *at least* the following columns.
+ `timestamp`
+ `open`
+ `high`
+ `low`
+ `close`

If your data can't be mapped to these dimensions for some reason (for example, because the column names aren't the same), you can map them manually using the **Open**, **High**, **Low**, and **Close** fields under the **Candlestick** options in the panel editor.

## Additional fields
<a name="v10-panels-candlestick-other"></a>

**Additional fields**

The candlestick panel is based on the time series visualization. It can visualize additional data dimensions beyond open, high, low, close, and volume. The **Include** and **Ignore** options allow it to visualize other included data such as simple moving averages, Bollinger bands and more, using the same styles and configurations available in the [Time series](v10-panels-time-series.md).