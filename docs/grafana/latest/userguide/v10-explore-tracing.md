# Tracing in Explore

This documentation topic is designed
for Grafana workspaces that support **Grafana version
10.x**.

For Grafana workspaces that support Grafana version 9.x, see
[Working in Grafana version 9](using-grafana-v9.md "using-grafana-v9.md").

For Grafana workspaces that support Grafana version 8.x, see
[Working in Grafana version 8](using-grafana-v8.md "using-grafana-v8.md").

You can use Explore to visualize traces from tracing data sources.

The following data sources are supported.

- [Tempo](tempo-data-source.md "tempo-data-source.md") (supported ingestion formats:
  OpenTelemetry, Jaeger, and Zipkin)
- [Jaeger](jaeger-data-source.md "jaeger-data-source.md")
- [AWS X-Ray](x-ray-data-source.md "x-ray-data-source.md")
- [Zipkin](zipkin-data-source.md "zipkin-data-source.md")
  For information on how to configure queries for the data sources listed above, refer
  to the documentation for specific data source.

## Query editor

You can query and search tracing data using a data source's query editor.

Each data source can have its own query editor. The query editor for the Tempo
data source is slightly different than the query editor for the Jaeger data
source.

For information on querying each data source, refer to their documentation.

- [Tempo](tempo-data-source.md "tempo-data-source.md")
- [Jaeger](jaeger-data-source.md "jaeger-data-source.md")
- [AWS X-Ray](x-ray-data-source.md "x-ray-data-source.md")
- [Zipkin](zipkin-data-source.md "zipkin-data-source.md")

## Trace View explanation

This section explains the elements of the Trace View dashboard.

**Header**

The header of the trace view has the following elements:

- Header title – Shows the name of the root span and trace ID.
- Search – Highlights spans containing the searched text.
- Metadata – Various metadata about the trace.

**Minimap**

Shows condensed view or the trace timeline. Drag your pointer over the minimap to
zoom into smaller time range. Zooming will also update the main timeline, so it is
easy to see shorter spans. Hovering over the minimap, when zoomed, will show the
**Reset Selection** button which resets the zoom.

**Span filters**

Using span filters, you can filter your spans in teh trace timeline viewer. The
more filters you add, the more specific are the filtered spans.

You can add one or more of the following filters:

- Resource service name
- Span name
- Duration
- Tags (which include tags, process tags, and log fields)

To show only the spans you have matched, choose the **Show matches
only** toggle.

**Timeline**

Shows list of spans within the trace. Each span row consists of these
components:

- Expand children button – Expands or collapses all the children
  spans of the selected span.
- Service name – Name of the service that logged the span.
- Operation name – Name of the operation that this span
  represents.
- Span duration bar – Visual representation of the operation duration
  within the trace.

**Span details**

Choosing the span row shows span details, including the following.

- Operation name
- Span metadata
- Tags – Any tags associated with this span.
- Process metadata – Metadata about the process that logged
  this span.
- Logs – List of logs logged by this span and associated key
  values. In case of Zipkin logs section shows Zipkin annotations.

**Trace to logs**

You can navigate from a span in a trace view directly to logs relevant for
that span. This is available for Tempo, Jaeger, and Zipkin data sources. Refer
to their relevant documentation for instructions on how to
configure each data source.

Choose the document icon to open a split view in Explore with the configured
data source and query relevant logs for the span.

**Trace to metrics**

###### Note

This feature is currently in beta

You can navigate form a span in a trace view directly to metrics relevant for
that span. This feature is available for Tempo, Jaeger, and Zipkin data sources.
Refer to their relevant documentation for details on configuration.

**Trace to profiles**

Using Trace to profiles, you can use Grafana's ability to correlate different
signales by adding the functionality to link between traces and profiles.

## Node graph

You can optionally expand the node graph for the displayed trace. Depending on
the data source, this can show spans of the trace as nodes in the graph, or add
some additional context, including the service graph based on the current trace.

## Service Graph view

The Service Graph view visualizes the span metrics (traces data for rates, error
rates, and durations (RED)) and service graphs. Once the requirements are set up,
this pre-configured view is immediately available.

For more information, see [Tempo](tempo-data-source.md "tempo-data-source.md") data
source page. You can also see the [service graph view page](https://grafana.com/docs/tempo/latest/metrics-generator/service-graph-view/ "https://grafana.com/docs/tempo/latest/metrics-generator/service-graph-view/") in the _Grafana Labs Tempo
documentation_.

## Data API

This visualization needs a specific shape of the data to be returned from the
data source in order to correctly display it.

The data source needs to return data frame and set
`frame.meta.preferredVisualisationType = 'trace'`.

**Data frame structure**

Required fields;

| Field name   | Type                | Description                                                                                                                               |
| ------------ | ------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| traceID      | string              | Identifier for the entire trace. There should be only one<br>trace in the data frame.                                                     |
| spanID       | string              | Identifier for the current span. SpanIDs should be unique<br>per trace.                                                                   |
| parentSpanID | string              | SpanID of the parent span to create child parent<br>relationship in the trace view. Can be<br>`undefined` for root span without a parent. |
| serviceName  | string              | Name of the service this span is part of.                                                                                                 |
| serviceTags  | TraceKeyValuePair[] | List of tags relevant for the service.                                                                                                    |
| startTime    | number              | Start time of the span in millisecond epoch time.                                                                                         |
| duration     | number              | Duration of the span in milliseconds.                                                                                                     |

Optional fields:

| Field name     | Type                | Description                                                           |
| -------------- | ------------------- | --------------------------------------------------------------------- |
| logs           | TraceLog[]          | List of logs associated with the current span.                        |
| tags           | TraceKeyValuePair[] | List of tags associated with the current span.                        |
| warnings       | string[]            | List of warnings associated with the current span.                    |
| stackTraces    | string[]            | List of stack traces associated with the current span.                |
| errorIconColor | string              | Color of the error icon in case span is tagged with `error:<br>true`. |

For details about the types see [TraceSpanRow](https://github.com/grafana/grafana/blob/main/packages/grafana-data/src/types/trace.ts#L28 "https://github.com/grafana/grafana/blob/main/packages/grafana-data/src/types/trace.ts#L28"), [TraceKeyValuePair](https://github.com/grafana/grafana/blob/main/packages/grafana-data/src/types/trace.ts#L4 "https://github.com/grafana/grafana/blob/main/packages/grafana-data/src/types/trace.ts#L4") and [TraceLog](https://github.com/grafana/grafana/blob/main/packages/grafana-data/src/types/trace.ts#L12 "https://github.com/grafana/grafana/blob/main/packages/grafana-data/src/types/trace.ts#L12") on GitHub.
