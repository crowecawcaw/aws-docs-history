# Connect to a Jaeger data source

The Jaeger data source provides open-source, end-to-end distributed tracing.

## Adding the data source

To access Jaeger settings, choose the **Configuration** (gear) icon, then choose **Data Sources**, and then choose **Jaeger**.

| Name         | Description                                                                                   |
| ------------ | --------------------------------------------------------------------------------------------- |
| `Name`       | The data source name. This is how you see the data source in<br>panels, queries, and Explore. |
| `Default`    | Default data source means that it will be pre-selected for<br>new panels.                     |
| `URL`        | The URL of the Jaeger instance; e.g.,<br>`http://localhost:16686`.                            |
| `Access`     | Server (default) = URL must be accessible from the Grafana<br>backend/server.                 |
| `Basic Auth` | Enable basic authentication to the Jaeger data source.                                        |
| `User`       | User name for basic authentication.                                                           |
| `Password`   | Password for basic authentication.                                                            |

## Query traces

You can query and display traces from Jaeger via Explore. For more
information, see [Explore](explore.md "explore.md").

The Jaeger query editor allows you to query by trace ID directly or selecting
a trace from trace selector. To query by trace ID, insert the ID into the text
input.

Use the trace selector to pick particular trace from all traces logged in the
time range you have selected in Explore. The trace selector has three levels of
nesting: 1. The service you are interested in. 1. Particular operation is part
of the selected service. 1. Specific trace in which the selected operation
occurred, represented by the root operation name and trace duration.

## Linking to the trace ID from

logs

You can link to Jaeger trace from logs in Loki by configuring a derived field
with internal link. For more information, see [Derived fields](using-loki-in-AMG.md#loki-derived-fields "using-loki-in-AMG.md#loki-derived-fields").
