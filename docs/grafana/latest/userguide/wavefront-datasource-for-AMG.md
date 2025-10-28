# Connect to a Wavefront data source

(VMware Tanzu Observability by Wavefront)

The Wavefront (VMware Tanzu Observability by Wavefront) data source enables
Amazon Managed Grafana users to query and visualize the data they’re collecting directly from
Wavefront and easily visualize it alongside any other metric, log, tracing, or other
data source. This flexible, single-pane view makes it easier to track system health
and debug issues.

###### Note

This data source is for Grafana Enterprise only. For more information,
see [Manage access to Enterprise plugins](upgrade-to-enterprise-plugins.md "upgrade-to-enterprise-plugins.md").

Additionally, in workspaces that support version 9 or newer, this data source might
require you to install the appropriate plugin. For more information, see [Extend your workspace with plugins](grafana-plugins.md "grafana-plugins.md").

## What is Wavefront?

[Wavefront](https://www.wavefront.com "https://www.wavefront.com") is a cloud monitoring
and analytics tool developed by VMware. Wavefront is a cloud-hosted service
where you send your time-series (metric) data – from CollectD, StatsD, JMX,
Ruby’s logger, AWS, or other tools. With Wavefront, users can perform
mathematical operations on those series, render charts to see anomalies, track
KPIs, and create alerts.

## Maximizing

your tech stack with Wavefront and Grafana

While on the surface, Grafana and Wavefront sound similar, many organizations
use both Wavefront and Grafana as critical parts of their observability
workflows.

**Visualize without Moving Data Sources:**
Grafana’s unique architecture queries data directly where it lives rather than
moving it and paying for redundant storage and ingestion.

**Compose Panels from Varied Sources** With
pre-built and custom dashboards, bring data together from many different data
sources into a single pane of glass.

**Transform and Compute at the User Level:** Users
can transform data and run various computations on data they see, requiring less
data preparation.

**Combine, Compute, and Visualize within Panels:**
Create mixed-data source panels that display related data from Waveferont and
other sources, such as Prometheus and InfluxDB.

## Documentation

### Features

- Timeseries Visualizations
- Table Visualizations
- Heatmap Visualizations
- Single Stat Visualizations
- Guided Query Editor
- Raw WQL Query Editor
- Annotations for event data
- Template Variables
- Ad-Hoc Filters
- Alerting

### Configuration

Configuring the Wavefront data source is relatively straightforward.
There are only two fields required to complete the configuration: `API
 URL` and `Token`.

- `API URL` will be the URL you use to access your
  wavefront environment. Example:
  `https://myenvironment.wavefront.com`.
- `Token` must be generated from a user account or service
  account.
  1.  To create a user account based token, log into your
      Wavefront environment, choose the cog on the top right
      corner of the page, choose your username (for example,
      `me@grafana.com`), select the **API
      Access** tab at the top of the user page, then
      copy an existing key or choose
      **generate**.
  2.  To create a service account based token, log into your
      Wavefront environment, choose the cog on the top right
      corner of the page, choose account management. On the left
      navigation, select **Accounts, Groups, &
      Roles**, choose the **Service
      Accounts** tab at the top, and then choose
      **Create New Account**. Enter a name
      for the service account. This can be anything you want. Copy
      the token that is provided under the
      **Tokens** section.
  3.  The last step is to make sure that the **Accounts,
      Groups, & Roles** check box selected under
      **Permissions**.

After you have the token, add that to the `Token`
configuration field and you should be set!

The finalized configuration page should look similar to this:

### Usage

#### Using the query

editor

The Wavefront query editor has two modes: **Query
Builder** and **Raw Query**. To toggle
between them, use the selector in the top right of the query form:

In **Query Builder** mode, you will presented with
four choices to make:

1. What metric do you want to query?
2. What aggregation do you want to perform on that metric?
3. How do you want to filter the results from that metric query?
4. Do you want to apply any additional functions to the result?

The metric selector is a categorized hierarchy. Select a category,
then choose again to drill into the subcategories. Repeat this process
until you have reached the metric that you want.

After selecting a metric, the available filters and filter values
will be automatically populated for you.

In **Raw Query** mode, you will see a single field
labeled **Query**. This allows you to run any [WQL](#wavefront-references "#wavefront-references") query that you want.

#### Using filters

The Wavefront plugin will dynamically query the appropriate filters
for each metric.

To add a filter, choose the **+** next to the
**Filters** label on the Wavefront query editor,
select which field you want to filter on, and select a value to filter
by.

#### Using functions

Functions provide an additional way to aggregate, manipulate, and
perform calculations on the metric response data. To view the available
functions, choose the dropdown list by the function label on the
**Query Builder**. Based on the function you
select, you will be able to perform further actions such as setting a
group by field or applying thresholds. Users are able to chain multiple
functions together to perform advanced calculations or data
manipulations.

#### Adding a

query template variable

1. To create a new Wavefront template variable for a dashboard,
   choose the settings cog on the top right portion of the
   dashboard.
2. In the panel at the left, choose
   **Variables**.
3. At the top right of the Variables page, choose
   **New**.
4. Enter a **Name** and a
   **Label** for the template variable you
   want to create. **Name** is the value you will
   use inside of queries to reference the template variable.
   **Label** is a human friendly name to
   display for the template variable on the dashboard select panel.
5. Select the type **Query** for the type field
   (it should be selected by default).
6. Under the **Query Options** heading, select
   **Wavefront** in the **Data
   source** dropdown list.
7. See [Template Variable Query Structure](#template-variable-query-structure "#template-variable-query-structure") for details on
   what should be entered into the **Query**
   field.
8. If you want to filter out any of the returned values from
   your query, enter a regular expression in the
   **Regex** input field.
9. Apply any sorting preferences you might have by choosing a
   sort type in the **Sort** dropdown list.
10. After verifying the configuration, choose
    **Add** to add the template variable, then
    choose **Save dashboard** on the left hand
    navigation panel to save your changes.

#### Template variable

query structure

metric lists: metrics: ts(…)

source lists: sources: ts(…)

source tag lists: sourceTags: ts(…)

matching source tag lists: matchingSourceTags: ts(…)

tag name lists: tagNames: ts(…)

tag value lists: tagValues(<tag>): ts(…)

**Notes**

- The s at the end of each query type is optional
- Support for all lowercase. You can use tagnames or tagNames,
  but not TAGNAMES.
- Using spaces around the : is optional

**WARNING**

`Multi-value` and `Include All option` are
currently not supported by the Wavefront plugin.

#### Using template

variables

After completing the steps to [add a new
template variable](#wavefront-adding-a-query-template-variable-1 "#wavefront-adding-a-query-template-variable-1"), you’re now ready to use the template
variable within your dashboard panels to create dynamic visualizations.

1. Add a new dashboard panel using the panel+ icon in the top
   right corner of your dashboard.
2. Select the aggregate you want to use for your query.
3. Choose the + icon beside **Filters** label
   and select the key type that matches your template variable.
   `host=` for a host filter, for example.
4. Enter the name of the template variable you created in the
   **Value** input field of the filter.
5. Save the dashboard.

You should now be able to cycle through different values of your
template variable and have your panel dynamically update!

#### Using Ad-Hoc

filters

To use ad-hoc filters, we must create two template variables. The
first one is a helper variable that will be used to select a metric so
that add-hoc filters can be populated for that metric name. The other
will be the actual ad-hoc filter variable.

###### Important

The helper variable that is required has to be named
`metriclink`. This can be an custom variable with the
list of metrics that you want to use or a query based variable using
the [Template
Variable Query Structure](#template-variable-query-structure "#template-variable-query-structure"). If you want to populate the
ad-hoc filter fields with only the values from a single metric, you
can hide the `metriclink` template variable.

After creating the `metriclink` variable, you can now add
the ad-hoc filter by following the same steps detailed in [Adding a
Query Template Variable](#wavefront-adding-a-query-template-variable-1 "#wavefront-adding-a-query-template-variable-1"). The difference being that you will
select **Ad Hoc Filters** as the
**Type** and no inputs are required for a query.

#### Adding

annotations

1. To create a new Wavefront annotation for a dashboard, choose
   the settings cog on the top right portion of the dashboard.
2. In the panel at the left, choose
   **Annotations**.
3. At the top right of the Annotations page, choose
   **New**.
4. Enter a name for the annotation (this will be used as the
   name of the toggle on the dashboard).
5. Select the **Data source** of Wavefront.
6. By default, annotations have a limit of 100 alert events that
   will be returned. To change that, set the
   **Limit** field to the value that you want.
7. Choose **Add**.

#### Using annotations

When annotations are toggled on, you should now see the alert events
and issues that correlate with a given time period.

If you pause on the bottom of an annotated section of a
visualization, a pop-up window will be displayed that shows the alert
name and provides a direct link to the alert in Wavefront.

#### Using the Display Name

field

This data source uses the Display Name field in the Field tab of the
Options panel to shorten or alter a legend key based on its name,
labels, or values. Other datasources use custom `alias`
functionality to modify legend keys, but the Display Name function is a
more consistent way to do so.

### References

- [WQL (Wavefront Query Language)](https://docs.wavefront.com/query_language_reference.html "https://docs.wavefront.com/query_language_reference.html")
