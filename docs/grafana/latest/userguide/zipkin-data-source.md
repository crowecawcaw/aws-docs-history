# Connect to a Zipkin data source

Zipkin is an open source, distributed tracing system. Add the Zipkin data source
to be able to query your traces in Explore in Amazon Managed Grafana

## Adding the data source

To access Zipkin settings, choose the **Configuration** (gear) icon, then choose **Data Sources**, and then choose **Zipkin**.

| Name         | Description                                                                                   |
| ------------ | --------------------------------------------------------------------------------------------- |
| `Name`       | The data source name. This is how you see the data source in<br>panels, queries, and Explore. |
| `Default`    | Default data source means that it will be pre-selected for<br>new panels.                     |
| `URL`        | The URL of the Zipkin instance; e.g.,<br>`http://localhost:9411`.                             |
| `Access`     | Server (default) = URL needs to be accessible from the<br>Grafana backend/server.             |
| `Basic Auth` | Enable basic authentication to the Zipkin data source.                                        |
| `User`       | User name for basic authentication.                                                           |
| `Password`   | Password for basic authentication.                                                            |

## Query traces

Querying and displaying traces from Zipkin is available via Explore.

The Zipkin query editor allows you to query by trace ID directly or selecting
a trace from trace selector. To query by trace ID, insert the ID into the text
input.

Use the trace selector to pick particular trace from all traces logged in the
time range you have selected in Explore. The trace selector has three levels of
nesting: 1. The service you are interested in. 1. Particular operation is part
of the selected service 1. Specific trace in which the selected operation
occurred, represented by the root operation name and trace duration.

## Data mapping in the trace

UI

Zipkin annotations are shown in the trace view as logs with annotation value
shown under annotation key.

## Linking to the trace ID from

logs

You can link to Zipkin trace from logs in Loki by configuring a derived field
with internal link. For more information, see [Derived fields](using-loki-in-AMG.md#loki-derived-fields "using-loki-in-AMG.md#loki-derived-fields").
