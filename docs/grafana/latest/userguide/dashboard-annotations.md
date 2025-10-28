# Annotations

This documentation topic is designed
for Grafana workspaces that support **Grafana version
8.x**.

For Grafana workspaces that support Grafana version 10.x, see
[Working in Grafana version 10](using-grafana-v10.md "using-grafana-v10.md").

For Grafana workspaces that support Grafana version 9.x, see
[Working in Grafana version 9](using-grafana-v9.md "using-grafana-v9.md").

Annotations provide a way to mark points on the graph with rich events. When you
pause on an annotation, you can see an event description and event tags. The text field
can include links to other systems for more detail.

## Native annotations

Amazon Managed Grafana comes with a native annotation store and the ability to add annotation
events directly from the graph panel.

## Adding annotations

To add an annotation, press **Ctrl** or **Cmd** and choose where you want to add the annotation. To
make the annotation searchable from other dashboards, add tags to it.

### Adding region annotations

To create an annotation for a region, press **Ctrl** or **Cmd** while you choose
the region.

### Built-in query

After you add an annotation, it remains visible. This is because a built-in
annotation query exists on all dashboards. This annotation query fetches all
annotation events that originate from the current dashboard and displays them on
the panel where they were created. This includes alert state history
annotations. You can stop annotations from being fetched and displayed by
choosing the **Dashboard settings** (gear) icon, choosing
**Annotations**, and then modifying the query named
`Annotations & Alerts (Built-in)`.

When you copy a dashboard using the **Save As** feature, the
new dashboard has a new dashboard ID, so annotations created on the source
dashboard are not visible on the copy. If the source dashboard annotations have
tags to filter by, you can show the annotations on the copy by adding a new
**Annotation Query** and filtering by the tags.

### Query by tag

You can create new annotation queries that fetch annotations from the native
annotation store by using the `-- Grafana --` data source and setting
**Filter by** to **Tags**. Specify at
least one tag. For example, create an annotation query named
`outages`, and specify a tag named `outage`. This
query will show all annotations that you create (from any dashboard or via API)
that have the `outage` tag.

By default, if you add multiple tags in the annotation query, Amazon Managed Grafana will
show only annotations that have all the tags you supplied. To show annotations
that contain at least one of the tags you supplied, turn on **Match
any**.

In Amazon Managed Grafana, it’s possible to use template variables in the tag query. For
example, if you have a dashboard showing stats for different services and a
template variable that controls which services to show, you can use the same
template variable in your annotation query to show annotations for only those
services.

## Querying other data sources

Annotation events are fetched by using annotation queries. To add a new
annotation query to a dashboard, choose the **Dashboard settings**
(gear) icon, choose `Annotations`, and then choose
**New**.

Specify a name for the annotation query. This name is displayed by the check box
for showing or hiding annotation events for this query. For example, you might have
two annotation queries named `Deploys` and `Outages`. You can
select or clear the check boxes to specify which annotations to show.

### Annotation query details

The annotation query options are different for each data source.

- [Annotations using Graphite query editor](../../../en_us/grafana/latest/userguide/using-graphite-in-AMG.md#graphite-annotations "../../../en_us/grafana/latest/userguide/using-graphite-in-AMG.md#graphite-annotations")
- [Annotations using OpenSearch data source](../../../en_us/grafana/latest/userguide/ES-use-datasource.md#ES-annotations "../../../en_us/grafana/latest/userguide/ES-use-datasource.md#ES-annotations")
- [Annotations using Prometheus](../../../en_us/grafana/latest/userguide/using-prometheus-datasource.md#p-annotations "../../../en_us/grafana/latest/userguide/using-prometheus-datasource.md#p-annotations")
- [Annotations using MySQL](../../../en_us/grafana/latest/userguide/using-mysql-in-AMG.md#mysql-annotations "../../../en_us/grafana/latest/userguide/using-mysql-in-AMG.md#mysql-annotations")
- [Annotations using PostgreSQL](../../../en_us/grafana/latest/userguide/using-postgresql-in-AMG.md#postgresql-annotations "../../../en_us/grafana/latest/userguide/using-postgresql-in-AMG.md#postgresql-annotations")
