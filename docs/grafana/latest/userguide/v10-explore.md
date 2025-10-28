# Explore in Grafana version 10

This documentation topic is designed
for Grafana workspaces that support **Grafana version
10.x**.

For Grafana workspaces that support Grafana version 9.x, see
[Working in Grafana version 9](using-grafana-v9.md "using-grafana-v9.md").

For Grafana workspaces that support Grafana version 8.x, see
[Working in Grafana version 8](using-grafana-v8.md "using-grafana-v8.md").

Grafana’s dashboard UI provides functionality to build dashboards for visualization.
_Explore_ strips away the dashboard and panel options so that you
can focus on the query. It helps you iterate until you have a working query and then
you can build a dashboard from the query.

###### Note

If you just want to explore your data and do not want to create a dashboard, then
Explore makes this much easier. If your data source supports graph and table data, then
Explore shows the results both as a graph and a table. This allows you to see trends in
the data and more details at the same time.

This page will get you started exploring your data. The following
topics give you more details on specific features and uses for Explore.

- [Query management in Explore](v10-explore-manage.md "v10-explore-manage.md")
- [Logs in Explore](v10-explore-logs.md "v10-explore-logs.md")
- [Tracing in Explore](v10-explore-tracing.md "v10-explore-tracing.md")
- [Correlations editor in Explore](v10-explore-correlations.md "v10-explore-correlations.md")
- [Inspector in Explore](v10-explore-inspector.md "v10-explore-inspector.md")

## Start exploring

###### Note

In order to access Explore, you must have an editor or an administrator
role.

###### To access Explore

1. In your Grafana workspace, choose the Explore menu item from the left
   menu bar.

An empty Explore tab opens.

Alternately, to start with an existing query in a panel, choose the
Explore option from the Panel menu. This opens an Explore tab with the
query from the panel and allows you to tweak or iterate in the query
outside of your dashboard. 2. Choose your data source from the dropdown in the top left.

You can also choose **Open advanced data source picker**
to see more options, including adding a data source (for Admins only). 3. Write the querying using the query editor provided by the selected data
source.

For more details about queries, see [Query and transform data](v10-panels-query-xform.md "v10-panels-query-xform.md"). 4. Run the query using the button in the top right corner.

## Split and compare

The split view provides an easy way to compare visualizations side-by-side or
to look at related data together on one page.

###### Top open the split view

1. In the Explore view, choose the **Split** button to
   duplicate the current query and split the page into two side-by-side
   queries.

###### Note

It is possible to select another data source for the new query which, for
example, allows you to compare the same query for two different servers or
to compare the staging environment to the production environment.

In split view, timepickers for both panels can be linked (if you change one, the
other gets changed as well) by selecting a time-sync button attached to one of
the timepickers. Linking timepickers keeps the start and the end times of the
split view queries in sync. It ensures that you’re looking at the same time
interval in both split panels. 2. To close the newly created query, choose the **Close Split**
button.

## Content outline

The content outline is a side navigation bar that keeps track of the queries and
visualizations you created in Explore. It allows you to navigate between them
quickly.

The content outline also works in a split view. When you are in split view, the
content outline is generated for each pane.

###### To open the content outline

1. Select the **Outline** button in the top left corner of the
   **Explore** screen.
2. Select any panel icon in the content outline to navigate to that panel.

## Share Explore URLs

When using Explore, the URL in the browser address bar updates as you make changes to
the queries. You can share or bookmark this URL.

###### Note

Explore may generate relatively long URLs. You can also generate and share a
[shortened link](#v10-explore-share "#v10-explore-share") if the URL is too long for
your tools.

**Generating Explore URLs from external tools**

Because Explore URLs have a defined structure, you can build a URL from external
tools and open it in Grafana. The url structure is:

```
http://<workspace_url>/explore?panes=<panes>&schemaVersion=<schema_version>&orgId=<org_id>
```

where:

- `org_id` is the organization ID
- `schema_version` is the schema version (should be set to the
  latest version, which is `1`.
- `panes` is a url-encoded JSON object of panes, where each key is
  the pane ID and each value is an object matching the following schema:

```
{
  datasource: string; // the pane's root datasource UID, or `-- Mixed --` for mixed datasources
  queries: {
    refId: string; // an alphanumeric identifier for this query, must be unique within the pane, i.e. "A", "B", "C", etc.
    datasource: {
      uid: string; // the query's datasource UID ie: "AD7864H6422"
      type: string; // the query's datasource type-id, i.e: "loki"
    }
    // ... any other datasource-specific query parameters
  }[]; // array of queries for this pane
  range: {
    from: string; // the start time, in milliseconds since epoch
    to: string; // the end time, in milliseconds since epoch
  }
}
```

###### Note

The `from` and `to` fields also accept relative
ranges as described in the [Setting dashboard time
range](v10-dash-using-dashboards.md#v10-dash-setting-dashboard-time-range "v10-dash-using-dashboards.md#v10-dash-setting-dashboard-time-range") topic.

## Share shortened link

The Share shortened link capability allows you to create smaller and simpler URLs
of the format /goto/:uid instead of using longer URLs with query parameters. To
create a shortened link to the query results, select the **Share** option in the Explore toolbar. A shortened link that is never
used will automatically get deleted after seven (7) days. If a link is used at least
once, it won't get deleted.

**Sharing shortened links with absolute time**

Short links have two options: keeping relative time (for example, from two hours ago
to the current time) or absolute time (for example, from 8am to 10am). Sharing a
shortened link by default will copy the time range selected, relative or absolute.
Choosing the dropdown button next to the share shortened link button and selecting
one of the options under **Time-Sync URL Links** will allow you to
create a short link with the absolute time, meaning anyone receiving the link will see
the same data you are seeing, even if they open the link at another time. This option
will not affect the time range selected in your Explore view.
