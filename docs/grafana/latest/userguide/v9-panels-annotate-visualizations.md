# Annotating visualizations

This documentation topic is designed
for Grafana workspaces that support **Grafana version
9.x**.

For Grafana workspaces that support Grafana version 10.x, see
[Working in Grafana version 10](using-grafana-v10.md "using-grafana-v10.md").

For Grafana workspaces that support Grafana version 8.x, see
[Working in Grafana version 8](using-grafana-v8.md "using-grafana-v8.md").

Annotations provide a way to mark points on the graph with rich events. When you hover
over an annotation, you can get event description and event tags. The text field can include
links to other systems with more detail.

**Native annotations**

Grafana comes with a native annotation store and the ability to add annotation events
directly from the graph panel or through the HTTP API.

**Adding an annotation**

1. In the dashboard, click on the **Time series** panel.
   A context menu will appear.
2. In the context menu, click **Add annotation**.
3. Add an annotation description, and optionally, tags.
4. Click **Save**.
   Alternatively, to add an annotation, `Ctrl+Click` or `Cmd+Click` on
   the **Time series** panel and the **Add
   annotation** popover will appear.

**Adding region annotation**

1. In the dashboard, `Ctrl+Click` or `Cmd+Click`on the
   **Time series** panel.
2. In the context menu, click on **Add
   annotation**.
3. Add an annotation description, and optionally, tags.
4. Click **Save**.
   **Editing an annotation**

5. In the dashboard, hover over an annotation indicator on the **Time series** panel.
6. Click on the edit (pencil) icon in the annotation tooltip.
7. Modify the description, and optionally, tags.
8. Click **Save**.
   **Deleting an annotation**

9. In the dashboard, hover over an annotation indicator on the **Time series** panel.
10. Click on the trash icon in the annotation tooltip.
    **Built-in query**

After you added an annotation, they will still be visible. This is due to the built in
annotation query that exists on all dashboards. This annotation query will fetch all
annotation events that originate from the current dashboard and show them on the panel where
they were created. This includes alert state history annotations. You can stop annotations
from being fetched and drawn by opening the **Annotations**
settings (through Dashboard cogs menu) and modifying the query named `Annotations &
 Alerts (Built-in)`.

When you copy a dashboard using the **Save As** feature, it
will get a new dashboard id so annotations created on source dashboard will no longer be
visible on the copy. You can still show them if you add a new **Annotation Query** and filter by tags. This only works if the annotations on
the source dashboard had tags to filter by.

**Querying by tag**

You can create new queries to fetch annotations from the native annotation store through
the `-- Grafana --` data source by setting **Filter
by** to `Tags`.

Grafana v8.1 and later versions also support typeahead of existing tags, provide at least
one tag.

For example, create an annotation query name `outages` and specify a tag
`outage`. This query will show all annotations (from any dashboard or through
API) with the outage tag. If multiple tags are defined in an annotation query, then Grafana
will only show annotations matching all the tags. To modify the behavior, enable `Match
 any`, and Grafana will show annotations that contain any one of the tags you
provided.

In Grafana v5.3+ it’s possible to use template variables in the tag query. So if you have
a dashboard showing stats for different services and a template variable that dictates which
services to show, you can now use the same template variable in your annotation query to
only show annotations for those services.

**Querying other data sources**

Annotation events are fetched through annotation queries. To add a new annotation query to
a dashboard open the dashboard settings menu, then select **Annotations**. This will open the dashboard annotations settings view. To
create a new annotation query hit the **New** button.

Specify a name for the annotation query. This name is given to the toggle (check box) that
will allow you to enable or disable showing annotation events from this query. For example
you might have two annotation queries named `Deploys` and `Outages`.
The toggle will allow you to decide what annotations to show.

**Annotation query details**

The annotation query options are different for each data source. For information about
annotations in a specific data source, see the specific [data source](AMG-data-sources.md "AMG-data-sources.md") topic.
