# Connect to an OpenTSDB data source

Amazon Managed Grafana ships with advanced support for OpenTSDB.

## Adding the data source

1. Open the side menu by choosing the Grafana icon in the top header.
2. In the side menu under the **Dashboards** link, you
   should find a **Data Sources** link.
3. Choose the **+ Add data source** button in the top
   header.
4. Select **OpenTSDB** from the
   **Type** dropdown list.

###### Note

If you don't see the **Data Sources** link in your side
menu, it means that your current user does not have the `Admin`
role.

| Name         | Description                                                                                 |
| ------------ | ------------------------------------------------------------------------------------------- |
| `Name`       | The data source name. This is how you see the data source in<br>panels and queries.         |
| `Default`    | Default data source means that it will be pre-selected for<br>new panels.                   |
| `Url`        | The HTTP protocol, ip and port of your opentsdb server<br>(default port is usually 4242).   |
| `Access`     | Server (default) = URL must be accessible from the Grafana<br>backend/server.               |
| `Version`    | Version = opentsdb version, either <=2.1 or 2.2.                                            |
| `Resolution` | Metrics from opentsdb can have data points with either<br>second or millisecond resolution. |

## Query editor

Open a graph in edit mode by choose the title. Query editor will differ if
the data source has version <=2.1 or = 2.2. In the former version, only tags
can be used to query OpenTSDB. But in the latter version, filters as well as
tags can be used to query opentsdb. Fill Policy is also introduced in OpenTSDB
2.2.

###### Note

While using the OpenTSDB 2.2 data source, make sure you use either
Filters or Tags as they are mutually exclusive. If used together, might give
you weird results.

### Using autocomplete

suggestions

As soon as you start typing metric names, tag names and tag values , you
should see highlighted auto complete suggestions for them. The autocomplete
only works if the OpenTSDB suggest API is enabled.

## Templating queries

Instead of hardcoding things such as server, application and sensor name in
your metric queries you can use variables in their place. Variables are shown as
dropdown select boxes at the top of the dashboard. You can use these dropdown
boxes to change the data being displayed in your dashboard.

For more information about templating and template variables, see [Templates and variables](templates-and-variables.md "templates-and-variables.md").

### Query variable

The OpenTSDB data source supports template variable queries. This means
you can create template variables that fetch the values from OpenTSDB. For
example, metric names, tag names, or tag values.

When using OpenTSDB with a template variable of `query` type
you can use following syntax for lookup.

| Query                       | Description                                                                            |
| --------------------------- | -------------------------------------------------------------------------------------- |
| `metrics(prefix)`           | Returns metric names with specific prefix (can be<br>empty).                           |
| `tag_names(cpu)`            | Returns tag names (i.e., keys) for a specific cpu<br>metric.                           |
| `tag_values(cpu, hostname)` | Returns tag values for metric cpu and tag key hostname.                                |
| `suggest_tagk(prefix)`      | Returns tag names (i.e., keys) for all metrics with<br>specific prefix (can be empty). |
| `suggest_tagv(prefix)`      | Returns tag values for all metrics with specific prefix<br>(can be empty).             |

If you do not see template variables being populated in `Preview of
 values` section, you must enable
`tsd.core.meta.enable_realtime_ts` in the OpenTSDB server
settings. Also, to populate metadata of the existing time series data in
OpenTSDB, you must run `tsdb uid metasync` on the OpenTSDB
server.

### Nested templating

One template variable can be used to filter tag values for another
template variable. First parameter is the metric name, second parameter is
the tag key for which you need to find tag values, and after that all other
dependent template variables. Some examples are mentioned below to make
nested template queries work successfully.

| Query                                                    | Description                                                                                                    |
| -------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `tag_values(cpu, hostname, env=$env)`                    | Returns tag values for cpu metric, selected env tag<br>value, and tag key hostname.                            |
| `tag_values(cpu, hostname, env=$env,<br>region=$region)` | Returns tag values for cpu metric, selected env tag<br>value, selected region tag value, and tag key hostname. |

For more information about OpenTSDB metric queries, see [OpenTSDB
documentation](https://opentsdb.net/docs/build/html/index.html "https://opentsdb.net/docs/build/html/index.html")
