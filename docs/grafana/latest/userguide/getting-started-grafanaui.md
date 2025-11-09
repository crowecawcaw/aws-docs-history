# Create your first dashboard

## Creating a dashboard

Follow these steps to create a dashboard in the Grafana console.

###### To create your first dashboard

1. Choose the + icon on the left panel, choose **Create
   Dashboard**, and then choose **Add new
   panel**.
2. In the **New Dashboard/Edit Panel** view, choose the
   **Query** tab.
3. Configure your query by selecting the data source that you'd like to query.
   For example, if you have **TestDB** added as a data source,
   this generates a sample dashboard called the Random Walk dashboard.

### Introduction to time series

Imagine that you wanted to know how the temperature outside changes throughout
the day. Once every hour, you’d check the thermometer and write down the time along
with the current temperature. After a while, you’d have something like the following
data.

| Time  | Value |
| ----- | ----- |
| 09:00 | 24°C  |
| 10:00 | 26°C  |
| 11:00 | 27°C  |

Temperature data such as this are one example of a _time
series_—a sequence of measurements, ordered in time. Every row in the
table represents one individual measurement at a specific time.

Tables are useful when you want to identify individual measurements, but they can
make it difficult to see the big picture. A more common visualization for time
series is the _graph_, which instead places each measurement
along a time axis. Visual representations such as the graph make it easier to
discover patterns and features of the data that otherwise would be difficult to see.

Other examples of time series are:

- CPU and memory usage
- Sensor data
- Stock market index

While each of these examples is a sequence of chronologically ordered
measurements, they also share other attributes:

- New data are appended at the end, at regular intervals—for example,
  hourly at 09:00, 10:00, 11:00, and so on.
- Measurements are seldom updated after they are added. For example,
  yesterday’s temperature doesn’t change.

Time series are powerful. They help you understand the past by letting you
analyze the state of the system at any point in time. Time series could tell you
that the server crashed moments after the free disk space went down to zero.

Time series can also help you predict the future by uncovering trends in your
data. For example, if the number of registered users has been increasing monthly by
4 percent for the past few months, you can predict how large your user base will be
at the end of the year.

Some time series have patterns that repeat themselves over a known period. For
example, the temperature is typically higher during the day, before it dips down at
night. By identifying these periodic, or _seasonal_, time series,
you can make confident predictions about the next period. If you know that the
system load peaks every day around 18:00, you can add more machines right before.

#### Aggregating time series

Depending on what you’re measuring, the data can vary greatly. What if you
wanted to compare periods longer than the interval between measurements? If
you’d measure the temperature once every hour, you’d end up with 24 data points
per day. To compare the temperature in August over the years, you’d have to
combine the 31 times 24 data points into one.

Combining a collection of measurements is called
_aggregation_. There are several ways to aggregate time
series data. Here are some common ones:

- **Average** returns the sum of all values
  divided by the total number of values.
- **Min** and **Max** return the smallest, and largest value in the
  collection.
- **Sum** returns the sum of all values in
  the collection.
- **Count** returns the number of values in
  the collection.

For example, by aggregating the data in a month, you can determine that
August 2017 was, on average, warmer than the year before. If you wanted to see
which month had the highest temperature, you’d compare the maximum temperature
for each month.

How you aggregate your time series data is an important decision, and it
depends on the story that you want to tell with your data. It’s common to use
different aggregations to visualize the same time series data in different ways.

#### Time series and monitoring

In the IT industry, time series data are often collected to monitor things
such as infrastructure, hardware, or application events. Machine-generated time
series data are typically collected with short intervals, so that you can react
to any unexpected changes, moments after they occur. The data accumulate at a
rapid pace, making it vital to have a way to store and query data efficiently.
As a result, databases that are optimized for time series data have seen a rise
in popularity in recent years.

##### Time series databases

A time series database (TSDB) is a database explicitly designed for time
series data. While it’s possible to use any regular database to store
measurements, a TSDB comes with some useful optimizations.

Modern TSDBs take advantage of the fact that measurements are only ever
appended, and rarely updated or removed. For example, the timestamps for
each measurement change little over time, which results in redundant data
being stored.

The following example shows a sequence of Unix timestamps.

```
1572524345, 1572524375, 1572524404, 1572524434, 1572524464
```

Looking at these timestamps, they all start with `1572524`,
leading to poor use of disk space. Instead, you could store each subsequent
timestamp as the difference, or _delta_, from the first
one, as shown in the following example.

```
1572524345, +30, +29, +30, +30
```

You could even take it a step further by calculating the deltas of these
deltas, as shown in the following example.

```
1572524345, +30, -1, +1, +0
```

If measurements are taken at regular intervals, most of these
delta-of-deltas will be 0. Because of optimizations like these, TSDBs use
drastically less space than other databases.

Another feature of a TSDB is the ability to filter measurements by using
_tags_. Each data point is labeled with a tag that
adds context information, such as where the measurement was taken.

The following TSDBs are supported by Grafana:

- [Graphite](https://graphiteapp.org/ "https://graphiteapp.org/")
- [InfluxDB](https://www.influxdata.com/products/influxdb-overview/ "https://www.influxdata.com/products/influxdb-overview/")
- [Prometheus](https://prometheus.io/ "https://prometheus.io/")

```
weather,location=us-midwest temperature=82 1465839830100400200
  |    -------------------- --------------  |
  |             |             |             |
  |             |             |             |
+-----------+--------+-+---------+-+---------+
|measurement|,tag_set| |field_set| |timestamp|
+-----------+--------+-+---------+-+---------+
```

##### Collecting time series

data

Now that you have a place to store your time series, how do you actually
gather the measurements? To collect time series data, you’d typically
install a _collector_ on the device, machine, or instance
that you want to monitor. Some collectors are made with a specific database
in mind, and some support different output destinations.

Here are some examples of collectors:

- [collectd](https://collectd.org/ "https://collectd.org/")
- [statsd](https://github.com/statsd/statsd "https://github.com/statsd/statsd")
- [Prometheus exporters](https://prometheus.io/docs/instrumenting/exporters/ "https://prometheus.io/docs/instrumenting/exporters/")
- [Telegraf](https://github.com/influxdata/telegraf "https://github.com/influxdata/telegraf")

A collector either _pushes_ data to a database or lets
the database _pull_ the data from the collector. Each
approach comes with its own set of pros and cons.

|      | Pros                                                                        | Cons                                                                         |
| ---- | --------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| Push | Easier to replicate data to multiple destinations.                          | The TSDB has no control over how much data gets sent.                        |
| Pull | More control over how the amount of data ingested and<br>data authenticity. | Firewalls, VPNs, or load balancers can make it hard to<br>access the agents. |

Because it's inefficient to write every measurement to the database,
collectors pre-aggregate the data and write to the TSDB at regular
intervals.

### Time series dimensions

With time series data, the data is often a set of multiple time series. Many
Grafana data sources support this type of data.

The common case is issuing a single query for a measurement with one or more
additional properties as dimensions. For example, you might query a temperature
measurement along with a location property. In this case, multiple series are
returned back from that single query, and each series has unique location as a
dimension.

To identify unique series within a set of time series, Grafana stores dimensions
in _labels_.

#### Labels

Each time series in Grafana optionally has labels. Labels are a set of
key-value pairs for identifying dimensions. Example labels are
`{location=us}` or
`{country=us,state=ma,city=boston}`. Within a set of time series, the
combination of its name and labels identifies each series. For example,
`temperature {country=us,state=ma,city=boston}`.

Different sources of time series data have dimensions stored natively, or
common storage patterns that enable the data to be extracted into dimensions.

Usually, TSDBs natively support dimensionality. Prometheus stores dimensions
in _labels_. In TSDBs such as Graphite or OpenTSDB, the term
_tags_ is used instead.

In table databases such SQL, these dimensions are generally the `GROUP
 BY` parameters of a query.

#### Multiple dimensions in

table format

In SQL or SQL-like databases that return table responses, additional
dimensions usually are columns in the query response table.

##### Single dimension

For example, consider a query like the following example.

```
SELECT BUCKET(StartTime, 1h), AVG(Temperature) AS Temp, Location FROM T
  GROUP BY BUCKET(StartTime, 1h), Location
  ORDER BY time asc
```

The query might return a table with three columns.

| StartTime | Temp | Location |
| --------- | ---- | -------- |
| 09:00     | 24   | LGA      |
| 09:00     | 20   | BOS      |
| 10:00     | 26   | LGA      |
| 10:00     | 22   | BOS      |

The table format is _long_ formatted time series, also
called _tall_. It has repeated timestamps, and repeated
values in Location. In this case, two time series in the set would be
identified as `Temp {Location=LGA}` and `Temp
 {Location=BOS}`.

Individual time series from the set are extracted by using the following
dimensions:

- The time typed column `StartTime` as the time index of
  the time series
- The numeric typed column `Temp` as the series
  name
- The name and values of the string typed `Location`
  column to build the labels, such as Location=LGA

##### Multiple dimensions

If the query is updated to select and group by more than one string
column (for example, `GROUP BY BUCKET(StartTime, 1h), Location,
 Sensor`), an additional dimension is added.

| StartTime | Temp | Location | Sensor |
| --------- | ---- | -------- | ------ |
| 09:00     | 24   | LGA      | A      |
| 09:00     | 24.1 | LGA      | B      |
| 09:00     | 20   | BOS      | A      |
| 09:00     | 20.2 | BOS      | B      |
| 10:00     | 26   | LGA      | A      |
| 10:00     | 26.1 | LGA      | B      |
| 10:00     | 22   | BOS      | A      |
| 10:00     | 22.2 | BOS      | B      |

In this case, the labels that represent the dimensions have two keys
based on the two string typed columns, `Location` and
`Sensor`. The data result in four series:

- `Temp {Location=LGA,Sensor=A}`
- `Temp {Location=LGA,Sensor=B}`
- `Temp {Location=BOS,Sensor=A}`
- `Temp {Location=BOS,Sensor=B}`

###### Note

**Note:** Multiple dimensions are not
supported in a way that maps to multiple alerts in Grafana. Instead,
they are treated as multiple conditions to a single alert.

##### Multiple values

In the case of SQL-like data sources, more than one numeric column can be
selected, with or without additional string columns to be used as
dimensions; for example, `AVG(Temperature) AS AvgTemp, MAX(Temperature)
 AS MaxTemp`. This, if combined with multiple dimensions, can
result in numerous series. Selecting multiple values is currently designed
to be used only with visualization.

### Introduction to histograms

and heatmaps

A histogram is a graphical representation of the distribution of numerical data.
It groups values into buckets (sometimes also called bins). Then it counts how many
values fall into each bucket.

Instead of graphing the actual values, histograms graph the buckets. Each bar
represents a bucket, and the bar height represents the frequency (such as count) of
values that fell into the interval of that bucket.

Histograms look only at _value distributions_ over a specific
time range. The problem with histograms is that you cannot see any trends or changes
in the distribution over time. This is where heatmaps become useful.

#### Heatmaps

A _heatmap_ is like a histogram over time, where each time
slice represents its own histogram. Instead of using bar height as a
representation of frequency, it uses cells, coloring a cell proportional to the
number of values in the bucket.

#### Pre-bucketed data

A number of data sources support histogram over time, including the
following:

- Amazon OpenSearch Service (by using a histogram bucket aggregation)
- Prometheus (with the [histogram](https://prometheus.io/docs/concepts/metric_types/#histogram "https://prometheus.io/docs/concepts/metric_types/#histogram") metric type and the _Format
  as_ option set to **Heatmap**)

Generally, you can use any data source that returns series with names
representing bucket bound or returns series sorted by the bound in ascending
order.

#### Raw data vs. aggregated data

If you use the heatmap with regular time series data (not pre-bucketed), it’s
important to remember that your data are often already aggregated by your time
series backend. Most time series queries don't return raw sample data. Instead,
they include a group by time interval or maxDataPoints limit coupled with an
aggregation function (usually average).

It depends on the time range of your query. The important point is to know
that the histogram bucketing that Grafana performs might be done on already
aggregated and averaged data. For more accurate heatmaps, it's better to do the
bucketing during metric collection or to store the data in OpenSearch, or in the
other data source that supports doing histogram bucketing on the raw data.

If you remove or lower the group by time (or raise maxDataPoints) in your
query to return more data points, your heatmap is more accurate. But this can
also put a heavy load on your CPU and memory. If the number of data points
becomes unreasonably large, it might cause stalls and crashes.
