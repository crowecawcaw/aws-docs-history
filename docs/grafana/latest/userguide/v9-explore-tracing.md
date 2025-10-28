# Tracing in Explore

This documentation topic is designed
for Grafana workspaces that support **Grafana version
9.x**.

For Grafana workspaces that support Grafana version 10.x, see
[Working in Grafana version 10](using-grafana-v10.md "using-grafana-v10.md").

For Grafana workspaces that support Grafana version 8.x, see
[Working in Grafana version 8](using-grafana-v8.md "using-grafana-v8.md").

Explore allows you to visualize traces from tracing data sources.

The following data sources are supported.

- [Jaeger](jaeger-data-source.md "jaeger-data-source.md")
- [Tempo](tempo-data-source.md "tempo-data-source.md")
- [AWS X-Ray](x-ray-data-source.md "x-ray-data-source.md")
- [Zipkin](zipkin-data-source.md "zipkin-data-source.md")
  For information on how to configure queries for the data sources listed above, refer
  to the documentation for specific data source.

## Trace View explanation

This section explains the elements of the Trace View dashboard.

**Header**

The header of the trace view has the following elements

- Header title: Shows the name of the root span and trace ID.
- Search: Highlights spans containing the searched text.
- Metadata: Various metadata about the trace.

**Minimap**

Shows condensed view or the trace timeline. Drag your pointer over the minimap to
zoom into smaller time range. Zooming will also update the main timeline, so it is
easy to see shorter spans. Hovering over the minimap, when zoomed, will show Reset
Selection button which resets the zoom.

**Timeline**

Shows list of spans within the trace. Each span row consists of these
components:

- Expand children button: Expands or collapses all the children
  spans of selected span.
- Service name: Name of the service logged the span.
- Operation name: Name of the operation that this span
  represents.
- Span duration bar: Visual representation of the operation duration
  within the trace.

**Span details**

Clicking anywhere on the span row shows span details, including the following.

- Operation name
- Span metadata
- Tags: Any tags associated with this span.
- Process metadata: Metadata about the process that logged this
  span.
- Logs: List of logs logged by this span and associated key values.
  In case of Zipkin logs section shows Zipkin annotations.

**Node graph**

You can optionally expand the node graph for the displayed trace. Depending on
the data source, this can show spans of the trace as nodes in the graph, or add
some additional context, including the service graph based on the current trace.

**Trace to logs**

You can navigate from a span in a trace view directly to logs relevant for
that span. This is available for Tempo, Jaeger, and Zipkin data sources. Refer
to their relevant documentation for instructions on how to
configure each data source.

Click the document icon to open a split view in Explore with the configured
data source and query relevant logs for the span.

## Service Graph view

The Service Graph view visualizes the span metrics (traces data for rates, error
rates, and durations (RED)) and service graphs. Once the requirements are set up,
this pre-configured view is immediately available.

For more information, see [Tempo](tempo-data-source.md "tempo-data-source.md") data
source page. You can also see the [service graph view page](https://grafana.com/docs/tempo/latest/metrics-generator/service-graph-view/ "https://grafana.com/docs/tempo/latest/metrics-generator/service-graph-view/") in the _Tempo
documentation_.
