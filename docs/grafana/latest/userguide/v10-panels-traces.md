# Traces

This documentation topic is designed
for Grafana workspaces that support **Grafana version
10.x**.

For Grafana workspaces that support Grafana version 9.x, see
[Working in Grafana version 9](using-grafana-v9.md "using-grafana-v9.md").

For Grafana workspaces that support Grafana version 8.x, see
[Working in Grafana version 8](using-grafana-v8.md "using-grafana-v8.md").

Traces visualizations let you follow a request as it traverses the services in your
infrastructure. The traces visualization displays traces data in a diagram that allows
you to easily interpret it.

For more information about traces and how to use them, refer to the following
documentation:

- [Tracing in Explore](v10-explore-tracing.md "v10-explore-tracing.md")
- [Tempo data source](tempo-data-source.md "tempo-data-source.md")
- [Getting
  started with Tempo](https://grafana.com/docs/tempo/latest/getting-started/ "https://grafana.com/docs/tempo/latest/getting-started/") in the _Grafana Labs Tempo
  Documentation_.

## Adding a panel with tracing visualizations

Once you have tracing data available in your Grafana stack, you can add tracing
panels to your Grafana dashboards.

Using a dashboard variable, `traceID`, lets you create a query
to show specific traces for a given trace ID. For more information about dashboard
variables, refer to the [Variables documentation](v10-dash-variables.md "v10-dash-variables.md").

**Prerequisites**

Before you begin, you need:

- An Amazon Managed Grafana workspace.
- A [Tempo data source](tempo-data-source.md "tempo-data-source.md") connected to
  your workspace.

To view and analyze traces data in a dashboard, you need to add the traces
visualization to your dashboard and define a query using the panel editor. The
query determines the data that is displayed in the visualization. For more
information on the panel editor, refer to the [Panel editor documentation](v10-panels-editor-overview.md "v10-panels-editor-overview.md").

This procedure uses dashboard variables and templates to allow you to enter
trace IDs which can then be visualized. You’ll use a variable called
`traceId` and add it as a template query.

###### To add a traces visualization query

1. In your workspace, create a new dashboard or go to an existing
   dashboard where you’d like to add traces visualizations.
2. Choose **Add visualization** from a new dashboard or
   choose **Add Panel** on an existing dashboard.
3. Select the appropriate tracing data source.
4. In the top-right of the panel editor, choose the
   **Visualizations** tab, and select
   **Traces**.
5. Under the **Panel options**, enter a
   **Title** for your trace panel. For more information on
   the panel editor, see [Configure panel options](v10-panels-configure-panel-options.md "v10-panels-configure-panel-options.md").
6. In the query editor, select the **TraceQL** query type
   tab.
7. Enter `${traceId}` in the TraceQL query field to
   create a dashboard variable. This variable is used as the template
   query.
8. Choose **Apply** in the panel editor to add the panel to
   the dashboard.
9. Go to the dashboard **Settings** and add a new variable
   called `traceId`, of variable type **Custom**,
   giving it a label, if required. Choose **Apply** to add
   the variable to the dashboard.
10. Verify that the panel works by using a valid trace ID for the data
    source used for the trace panel and editing the ID in the dashboard
    variable.

## Adding TraceQL with table visualizations

While you can add a trace visualization to a dashboard, having to manually add
trace IDs as a dashboard variable is cumbersome. It’s more useful to instead be able
to use TraceQL queries to search for specific types of traces and then select
appropriate traces from matching results.

**Prerequisites**

This procedure assumes you have completed the previous procedure.

###### To add TraceQL with table visualizations

1. In the same dashboard where you added the trace visualization, choose
   **Add panel** to add a new visualization panel.
2. Select the same trace data source you used in the previous section.
3. In the top-right of the panel editor, select the
   **Visualizations** tab, then choose
   **Table**.
4. In the query editor, choose the **TraceQL** tab.
5. Under the **Panel options**, enter a
   **Title** for your trace panel.
6. Add an appropriate TraceQL query to search for traces that you would like
   to visualize in the dashboard. For example, here is a simple, static query
   from a server called `my-server`.

```
{ .service.name = "`my-server`" && .http.status_code=500 }
```

You can write the TraceQL query as a template query to take advantage of other
dashboard variables, if they exist. This lets you create dynamic queries
based on these variables.

When results are returned from a query, the results are rendered in the panel’s
table.

The results in the traces visualization include links to the
**Explore** page that renders the trace. You can add
other links to traces in the table that fill in the `traceId`
dashboard variable when selected, so that the trace is visualized in the same
dashboard.

To create a set of data links in the panel, use the following procedure.

###### To use a variable to add other links to traces

1. In the right-side menu, under **Data links**, choose
   **Add link**.
2. Add a **Title** for the data link.
3. Find the path to the dashboard by looking in your browser’s address
   bar when the full dashboard is being rendered. Because this is a link to
   a dashboard in the same Grafana stack, only the path of the dashboard is
   required.

For example, if your path is:

```
https://g-example.grafana-workspace.us-east-1.amazonaws.com`/d/1234abcd5/my-dashboard?orgId=1`
```

Then the path to the dashboard is:

```
/d/1234abcd5/my-dashboard?orgId=1
```

4. In the **URL** field, make a self-reference to the
   dashboard that contains both of the panels. This self-reference uses the
   value of the selected trace in the table to fill in the dashboard variable.
   Use the path for the dashboard from the previous step and then fill in the
   value of `traceId` using the selected results from the TraceQL
   table. The trace ID is exposed using the `traceID` data field in
   the returned results, so use that as the value for the dashboard
   variable. For example:

```
/d/1234abcd5/my-dashboard?orgId=1&var-traceId=${__data.fields["traceID"]}
```

5. Choose **Save** to save the data link.
6. Choose **Apply** from the panel editor to apply the
   panel to the dashboard.
7. Save the dashboard.

You should now see a list of matching traces in the table visualization. While
selecting the **TraceID** or **SpanID** fields
will give you the option to either open the **Explore** page to
visualize the trace or following the data link, selecting any other field (such as
`Start time`, `Name`, or `Duration`) automatically
follows the data link, filling in the `traceId` dashboard variable, and
then shows the relevant trace in the trace panel.
