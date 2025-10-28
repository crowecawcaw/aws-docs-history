# Traces support

The OpenSearch plugin has support for viewing a list of traces in table form,
and a single trace in **Trace View**, which shows the timeline
of trace spans.

###### Note

Querying OpenSearch traces is only available using Lucene queries.

Trace support is only available for Grafana workspaces that support
version 9.4 or newer.

To create a query showing all traces, use the Lucene query type
`Traces` with a blank query. If necessary, select the
**Table** visualization type.

Selecting a trace ID in the table will open that trace in the trace
view.

To create a query showing a single trace, use the query `traceid:
 {`traceId`}`, and, if necessary, select
the **Traces** visualization type.
