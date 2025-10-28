# Annotate visualizations

This documentation topic is designed
for Grafana workspaces that support **Grafana version
10.x**.

For Grafana workspaces that support Grafana version 9.x, see
[Working in Grafana version 9](using-grafana-v9.md "using-grafana-v9.md").

For Grafana workspaces that support Grafana version 8.x, see
[Working in Grafana version 8](using-grafana-v8.md "using-grafana-v8.md").

Annotations provide a way to mark points on a visualization with rich events. They
are visualized as vertical lines and icons on all graph panels. When you hover over an
annotation, you can get event description and event tags. The text field can include
links to other systems with more detail.

You can annotate visualizations in three ways:

- Directly in the panel, using the [built-in annotations query](#v10-dash-built-in-query "#v10-dash-built-in-query").
- Using the Grafana HTTP API.
- Configuring annotation queries in the dashboard settings.
  In the first two cases, you’re creating new annotations, while in the last you’re
  querying existing annotations from data sources. The built-in annotation query also
  supports this.

This section explains the first and third options; for information about using the
Grafana HTTP API, refer to [Annotations API](Grafana-API-Annotations.md "Grafana-API-Annotations.md").

Annotations are supported for the following visualization types:

- Time series
- State timeline
- Candlestick

## Create annotations in

panels

Grafana comes with the ability to add annotation events directly from a panel
using the [built-in annotations query](#v10-dash-built-in-query "#v10-dash-built-in-query") that
exists on all dashboards. Annotations that you create this way are stored in
Grafana.

To add annotations directly in the panel:

- The dashboard must already be saved.
- The built-in query must be enabled.

###### To add an annotation

1. In the dashboard select the panel to which you’re adding the
   annotation. A context menu will appear.
2. In the context menu, select **Add
   annotation**.
3. (Optional) Add an annotation description and tags.
4. Select **Save**.

Alternatively, to add an annotation, press `Ctrl` (or
`Cmd`) while selecting the panel, and the **Add
annotation** popover will appear.

**Region annotations**

You can also create annotations that cover a region, or period of time in
a visualization.

###### To add a region annotation

1. In the dashboard press `Ctrl` (or
   `Cmd`) while selecting an area of the panel.
2. Add an annotation description and tags (optional).
3. Click **Save**.

###### To edit an annotation

1. In the dashboard, hover over an annotation indicator on a
   panel.
2. Select the **Edit** (pencil) icon in the
   annotation tooltip.
3. Modify the description and/or tags.
4. Select **Save**.

###### To delete an annotation

1. In the dashboard, hover over an annotation indicator on a panel.
2. Select the **Delete** (trash) icon in the
   annotation tooltip.

## Fetch annotations through

dashboard settings

In the dashboard settings, under **Annotations**,
you can add new queries to fetch annotations using any data source,
including the built-in data annotation data source. Annotation queries
return events that can be visualized as event markers in graphs across
the dashboard.

###### To add a new annotation query

1. Select the **Settings** (gear) icon in the
   dashboard header to open the settings menu.
2. Select **Annotations**.
3. Click **Add annotation query**.
4. Enter a name for the annotation query.

This name is given to the toggle (checkbox) that will allow you to
enable showing annotation events from this query. 5. Select the data source for the annotations.

You can also choose **Open advanced data source
picker** to see more options, including adding a new
data source (available for Admins only). 6. If you don’t want to use the annotation query right away, clear the
**Enabled** checkbox. 7. If you don’t want the annotation query toggle to be displayed in the
dashboard, select the **Hidden**
checkbox. 8. Select a color for the event markers. 9. In the **Show in** drop-down, choose
one of the following options:

    * **All panels** – The annotations
     are displayed on all panels that support annotations.
    * **Selected panels** – The
     annotations are displayed on all the panels you select.
    * **All panels except** – The
     annotations are displayed on all panels except the ones you
     select.

10. Configure the query.

The annotation query options are different for each data source. For
information about annotations in a specific data source, see
[Connect to data sources](AMG-data-sources.md "AMG-data-sources.md").

## Built-in query

After you add an annotation, they will still be visible. This is due to the
built-in annotation query that exists on all dashboards. This annotation query will
fetch all annotation events that originate from the current dashboard, which are
stored in Grafana, and show them on the panel where they were created. This includes
alert state history annotations.

By default, the built-in annotation query uses the `Grafana`
special data source, and manual annotations are only supported
using this data source. You can use another data source in the built-in annotation
query, but you’ll only be able to create automated annotations using the query
editor for that data source.

To add annotations directly to the dashboard, this query must be enabled.

###### To confirm the built-in query is enabled

1. Select the dashboard **settings** (gear) icon in
   the dashboard header to open the dashboard settings menu.
2. Select **Annotations**.
3. Find the **Annotations & Alerts (Built-in)**
   query.

If it shows **Disabled** before the name of
the query, then you’ll need to select the query name to open it and
update the setting.

###### To stop annotations from being fetched and drawn

1. Select the dashboard **settings** (gear) icon in
   the dashboard header to open the dashboard settings menu.
2. Select **Annotations**.
3. Select the **Annotations & Alerts (Built-in)**
   query.
4. Select the **Enabled** toggle to turn it off.

When you copy a dashboard using the **Save As**
feature it will get a new dashboard id, so annotations created on the source
dashboard will no longer be visible on the copy. You can still show them if you add
a new **Annotation Query** and filter by tags.
However, this only works if the annotations on the source dashboard had tags to
filter by.

**Filtering queries by tag**

You can create new queries to fetch annotations from the built-in annotation
query using the `Grafana` data source by setting
**Filter by** to `Tags`.

For example, create an annotation query name `outages` and
specify a tag `outage`. This query will show all annotations
(from any dashboard or via API) with the `outage` tag. If
multiple tags are defined in an annotation query, then Grafana will only show
annotations matching all the tags. To modify the behavior, enable
**Match any**, and Grafana will show annotations that
contain any one of the tags you provided.

You can also use template variables in the tag query. This means if you have
a dashboard showing stats for different services and a template variable that
dictates which services to show, you can use the same template variable in your
annotation query to only show annotations for those services.
