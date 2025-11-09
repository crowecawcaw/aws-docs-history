# Connect to a Tempo data source

Tempo is a high-volume, minimal dependency trace storage, OSS tracing solution
from Grafana Labs.

## Adding the data source

To access Tempo settings, choose the **Configuration** (gear) icon, then choose **Data Sources**, and then choose **Tempo**.

| Name         | Description                                                                                |
| ------------ | ------------------------------------------------------------------------------------------ |
| `Name`       | The name using which you will refer to the data source in<br>panels, queries, and Explore. |
| `Default`    | Default data source means that it will be pre-selected for<br>new panels.                  |
| `URL`        | The URL of the Tempo instance; e.g.,<br>`http://tempo`.                                    |
| `Basic Auth` | Enable basic authentication to the Tempo data source.                                      |
| `User`       | User name for basic authentication.                                                        |
| `Password`   | Password for basic authentication.                                                         |

## Trace to logs

This is a configuration for the trace to logs feature. The target data source
currently must be Loki. For more information, see [Tracing integration](explore.md#tracing-integration "explore.md#tracing-integration").

- **Data source** – Target data
  source.
- **Tags** – The tags that will be
  used in the Loki query. The default is `'cluster', 'hostname',
'namespace', pod'`
- **Span start time shift** – Shift
  in the start time for the Loki query based on the span start time. In
  order to extend to the past, you need to use a negative value. Time
  units can be used here, for example, 5s, 1m, 3h. The default is

0.

- **Span end time shift** – Shift in
  the end time for the Loki query based on the span end time. Time units
  can be used here, for example, 5s, 1m, 3h. The default is 0.

## Query traces

You can query and display traces from Tempo via Explore. You can search for
traces if you set up the trace to logs setting in the data source configuration
page. To find traces to visualize, use the Loki query editor. To get search
results, you must have derived fields configured, which point to this data
source.

To query a particular trace, select the TraceID query type, and then put the
ID into the Trace ID field.

## Linking to the trace ID from

logs

You can link to Tempo trace from logs in Loki or Elastic by configuring an
internal link. For more information, see [Derived fields](using-loki-in-AMG.md#loki-derived-fields "using-loki-in-AMG.md#loki-derived-fields").
