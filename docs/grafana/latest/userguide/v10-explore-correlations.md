# Correlations editor in Explore

This documentation topic is designed
for Grafana workspaces that support **Grafana version
10.x**.

For Grafana workspaces that support Grafana version 9.x, see
[Working in Grafana version 9](using-grafana-v9.md "using-grafana-v9.md").

For Grafana workspaces that support Grafana version 8.x, see
[Working in Grafana version 8](using-grafana-v8.md "using-grafana-v8.md").

Correlations allow users to build a link between any two data sources. For more
information, including an overview of correlations, see [Correlations in Grafana version 10](v10-correlations.md "v10-correlations.md").

## Creating a correlation

You can create correlations from the Explore page.

###### To create a correlation

1. In your Amazon Managed Grafana workspace, navigate to the Explore page.
2. Select a data source that you would like to be the source for a new correlation.
3. Run a query producing data in a supported visualization.

###### Note

Supported visualizations are [Logs](v10-panels-logs.md "v10-panels-logs.md")
and [Table](v10-panels-table.md "v10-panels-table.md"). 4. Choose **+ Add** in the top toolbar and
select **Add correlation** (you can also
select **Correlations Editor** from the
[Command Palette](v10-search.md#v10-search-palette "v10-search.md#v10-search-palette").

Explore is now in Correlations Editor mode indicated by a blue border and
top bar. You can exit Correlations Editor by choosing
**Exit** in the top bar. 5. You can now create the following new correlations for the visualization
with links that are attached to the data that you can use to build a new
query:

    * *Logs* – links are displayed next to
     field values inside log details for each log row.
    * *Table* – every table cell is a
     link.

6. Choose a link to add a new correlation. Links are associated with a
   field that is used as a result field of a correlation. For more details,
   see [Correlation configuration](v10-correlations-config.md "v10-correlations-config.md").
7. In the split view that opens, use the right pane to set up the target
   query source of the correlation. For more details, see [Target query](v10-correlations-config.md#v10-correlations-config-target-query "v10-correlations-config.md#v10-correlations-config-target-query").
8. Build a target query using [variables syntax](v10-dash-variable-syntax.md "v10-dash-variable-syntax.md") with variables from the list provided at the top
   of the pane. The list contains sample values from the selected data
   row.
9. Provide a label and description (optional). A label will be used as the
   name of the link inside the visualization and can contain variables.
10. Provide transformations (optional; see below for details).
11. Choose **Save** in the top toolbar to save
    the correlation and exit Correlations Editor mode. The link used to create
    the correlation is replaced with a data link in each row. When the link is
    selected, the query you defined will run in another pane, with the variables
    replaced dynamically with the values from the selected row.

## Transformations

Transformations allow you to extract values that exist in a field with other
data. For example, using a transformation, you can extract one portion of a log line
to use in a correlation. For more details on transformations in correlations, see
[Correlation
Transformations](v10-correlations-config.md#v10-correlations-config-transformations "v10-correlations-config.md#v10-correlations-config-transformations").

After choosing one of the generated links in the editor mode, you can add
transformations by selecting **Add transformation** in
the **Transformations** dropdown menu.

###### To use a transformation in a correlation

1. Select a field to apply the transformation to. Select the portion of the
   field that you want to use for the transformation. For example, a log line.
   Once selected, the value of this field will be used to assist you in
   building the transformation.
2. Select the type of the transformation. See [Correlation
   Transformations](v10-correlations-config.md#v10-correlations-config-transformations "v10-correlations-config.md#v10-correlations-config-transformations") for the options
   and relevant settings.
3. Based on your selection, you might see one or more variables populate,
   or you might need to provide more specifications in options that are
   displayed.
4. Select **Add transformation to correlation** to add the
   specified variables to the list of available variables.

###### Note

For regular expressions in this dialog box, the `mapValue`
referred to in other documentation is called `Variable Name`
here. Grafana highlights any text that matches the expression in the field
value. Use regular expression capture groups to select what portion of the
match should be extracted. When a valid regular expression is provided, the
variable and the value of that variable appear below the `Variable 
 Name` field.

## Correlations examples

The following examples show how to create correlations using the Correlations
Editor in Explore. If you’d like to follow these examples, make sure to set up a
[test data source](testdata-data-source.md "testdata-data-source.md").

### Creating a text to graph

correlation

This example shows how to create a correlation using Correlations Editor in
Explore.

Correlations allow you to use results of one query to run a new query in any
data source. In this example, you will run a query that renders tabular data.
The data will be used to run a different query that yields a graph result.

To follow this example, make sure you have set up a [test data source](testdata-data-source.md "testdata-data-source.md").

###### To create a text to graph correlation

1. In Grafana, navigate to **Explore**.
2. Select the **test data source** from the dropdown
   menu at the top left of the page.
3. Choose **+ Add** in the dropdown menu to the right
   and select **Add correlation**.
4. Explore is now in Correlations Editor mode, indicated by a blue
   border.
5. Select the following scenario from the scenario dropdown menu:
   **CSV File**.
6. Select the file, **population_by_state.csv**. Each
   cell is a link that you can click on to begin creating a new
   correlation.
7. Click on any cell in the `State` column to create a
   new correlation that attaches a data link to that entry. For example,
   select `California`.
8. In the split view, select the same data source you selected in the
   left pane. The helper above the query editor contains all available
   variables you can use the target query. Variables contain all data
   fields (table columns) from the selected row.
9. In the **Scenario** menu, select **CSV
   Metric Values**. The `String Input` field in the
   Query editor provides variables with population values for each year:
   `${1980},${2000},${2020}`. This will generate a graph using
   variable values.
10. In the Query Editor **Alias** field, enter
    `${State}`.

Run a query to see that it produces a graph using sample values from
the variables. 11. Choose **Save** to save the correlation and exit the
Correlations Editor.

After the correlation is saved, Explore will rerun the query in the
left pane. By clicking a state name, the query on the right is rerun
with values from the row being inserted into the CSV, thus changing the
graph. The query is rerun with updated values every time you click on a
state name.

You can apply the same steps to any data source. Correlations allow you to
create links in visualizations to run dynamic queries based on selected data.
In this example we used data returned by a query to build a new query
generating different visualization using the same data source. However, you can
create correlations between any data sources to create custom exploration
flows.

### Creating a logs to table

correlation

In this example, you will create a correlation to demonstrate how to use
transformations to extract values from the log line and another field.

To follow this example, make sure you have set up a [test data source](testdata-data-source.md "testdata-data-source.md").

###### To create a logs to table correlation

1. In Grafana, navigate to **Explore**.
2. Select the **test data source** from the dropdown
   menu at the top left of the page.
3. Choose **+ Add** in the dropdown menu to the right
   and select **Add correlation**.
4. Explore is now in Correlations Editor mode, indicated by a blue
   border.
5. In the **Scenario** menu, select
   **Logs**.
6. Expand a log line to see the correlation links. Select `Correlate 
with hostname`.
7. Explore opens in split view. Select the same data source you selected
   in the left pane. The helper above the query editor contains all
   available variables you can use the target query.
8. Expand the transformations section, and click **Add
   transformation**.
9. In the **Field** dropdown menu, select
   **message**. The log line shows up as example
   data.
10. Under **Type**, select **Logfmt**.
    This populates the list of variables.
11. Choose **Add transformation to correlation**.
12. Choose **Add transformation** again and under
    **Field**, select
    **hostname**.
13. Under **Type**, select **Regular
    expression**.
14. Under **Expression**, enter the following:
    `-([0-9]\*)`. This selects any numbers to the right of the
    dash.
15. Under **Variable Name**, enter the following:
    `hostNumber`. This populates the list of variables.
16. Choose **Add transformation to correlation** to add
    it to the other variables.
17. In the data source editor, open the **Scenario**
    dropdown menu and select **CSV Content**.
18. In the text box below, provide the following and save the
    correlation:

```
time,msg,hostNumber,status
${time},${msg},${hostNumber},${status}
```

This closes the split view and reruns the left query. Expand any log
line to see the correlation button. Chooseing the correlation button
opens the split view with the `time` (a field),
`msg` (extracted with _logfmt_ from the
log line), `host number` (extracted with
_regex_ from the `hostname`) and the
`status` (extracted with _logfmt_ from
the log line).
