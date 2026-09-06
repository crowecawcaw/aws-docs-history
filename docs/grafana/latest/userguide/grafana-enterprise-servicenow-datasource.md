

# Connect to a ServiceNow data source
<a name="grafana-enterprise-servicenow-datasource"></a>

This is the ServiceNow data source that is used to connect to ServiceNow instances.

**Note**  
This data source is for Grafana Enterprise only. For more information, see [Manage access to Enterprise plugins](upgrade-to-enterprise-plugins.md).  
Additionally, in workspaces that support version 9 or newer, this data source might require you to install the appropriate plugin. For more information, see [Extend your workspace with plugins](grafana-plugins.md).

## Features
<a name="features-1"></a>
+  Queries 
  +  Stat API Queries 
  +  Table API Queries 
    +  Incidents, Changes, and any other table 
+  Alerts 
+  Annotations (beta feature) 
+  Template Variables 

## Configuration
<a name="configuration-2"></a>

 Select data sources on the left panel of Grafana. 

 Select Add Datasource: 

 Enter **servicenow** to find the data source plugin: 

 Enter ServiceNow URL: 

 Choose **Save & Test**. You should see a green message with "ServiceNow Connection OK". 

### Example dashboards
<a name="example-dashboards"></a>

 Pre-made dashboards are included with the plugin and can be imported through the data source configuration page, under the dashboards tab. 

## Usage
<a name="usage-2"></a>

 There are two ways to return data in the query editor. 
+  TableAPI 
+  AggregateAPI 

 Users can currently choose between querying pre-defined tables, such as the following: 
+  Changes 
+  Incidents 

 Or, as of `v1.4.0`, an API-driven list of tables and fields using the **Other (Custom Table)** option. This option will allow you to query data that is in any table available to the user used to set up the ServiceNow data source. 

 The **Custom Table** option should support all of the same features as the pre-defined table lists. 

### TableAPI queries
<a name="tableapi-queries"></a>

 The TableAPI returns data suitable for displaying in a table panel. It allows for an ordered selection of fields to display plus filtering options. The query editor also provides a field to limit the number of rows returned by a query. 

 Example table panel showing results from the previous query. 

#### Show
<a name="show"></a>

 The *Show* row provides a selector for a field to be displayed. Multiple fields can be also be specified. The fields will be returned in the exact order specified. 

#### Display Values
<a name="display-values"></a>

 The *Display Values* flag will cause the query to return human-friendly values, or display vaules, instead of numeric values. 

 For example, a severity of `1` without this flag would only display `1`. If the flag is enabled, the value displayed will be `1 - High`. 

 According to the [ServiceNow API documentation](https://developer.servicenow.com/dev.do#!/reference/api/orlando/rest/c_TableAPI), this can have a negative performance impact. 

**Note**  
 […] specifying the display value can cause performance issues since it is not reading directly from the database and could include referencing other fields and records. 

#### Filters (general)
<a name="filters-general"></a>

 The *Filters* row provides the ability to narrow down the displayed rows based on multiple field and value criteria. 

 All filters are combined with an *AND* or an *OR* operation. 

 The following fields are available when not using a custom table (this list will expand in the future).

```
Active
Asset
Group
Assigned To
Escalation
Issue Number
Description
Priority
State
Type
Change Risk
Change State
Start Date
End Date
On Hold
```

 When selecting a custom table, fields are automatically populated from the Service Now API. 

##### Date filters
<a name="date-filters"></a>


|  Time Field  |  Operators  |  Value  | 
| --- | --- | --- | 
|  Opened At  |  At or Before Today Not Today Before At or Before After At or After  |  timestamp javascript:gs.daysAgo(30)  | 
|  Activity Due  |   |   | 
|  Closed At  |   |   | 
|  Due Date  |   |   | 
|  Expected Start  |   |   | 
|  Reopened Time  |   |   | 
|  Resolved At  |   |   | 
|  Work End  |   |   | 
|  Work Start  |   |   | 
|  Ignore Time  |   |   | 

 For additional date values, see: https://developer.servicenow.com/app.do\#\!/api\_doc?v=newyork&id=r\_SGSYS-dateGenerate\_S\_S 

##### Operators (general, string-based)
<a name="operators-generalstring-based"></a>
+  Starts With 
+  Ends With 
+  Like 
+  Not Like 
+  Equals 
+  Not Equals 
+  Is Empty 

##### Operators (time-based)
<a name="operators-time-based"></a>
+  Today 
+  Not Today 
+  Before 
+  At or Before 
+  After 
+  At or After 

##### Values
<a name="values"></a>

 Value selection depends on the type of filter selected. 
+  Boolean filters have True/False options 
+  Text filters will allow typing any value 
+  Escalation, Priority has a fixed set of numerical values 

#### Sort By
<a name="sort-by"></a>

 The *Sort By* row provides the ability to narrow down the displayed rows based on multiple field and value criteria. 

 All filters are combined with an *AND* operation. Support for additional operators will be added. 

#### Limit
<a name="limit"></a>

 A row limit can be specified to prevent returning too much data. The default value is 25. 

#### Time Field
<a name="time-field"></a>

 The `Time Field` is what turns your queried data into a time series. Your data being handled as a time series means that values in your selected "time field" that do not fall within your dashboard / panel’s time range will not be displayed. 

 The default time field used is "Opened At", but can be changed to any available field that holds a time value. 

 A special value "Ignore Time" is provided to allow results "up until now" and also to enable the filters to control what data is displayed. 

### AggregateAPI queries (Stats)
<a name="aggregateapi-queries-stats"></a>

 The AggregateAPI will always return metrics, with the following aggregations: avg, min, max, sum. Filtering is also available to narrow queries. 

#### Show
<a name="show-1"></a>

 The *Show* row provides a selector for a metric to be displayed. Multiple metrics can be also be specified. 

#### Filters (general)
<a name="filters-general-1"></a>

 Aggregate *Filters* provide the ability to narrow down the displayed metrics based on field and value criteria, similar to the table option. 

 All filters are combined with an *AND* operation. Support for additional operators will be added. 

 Stat filter options are the same as the TableAPI. 

#### Aggregation
<a name="aggregation"></a>

 There are four types of metric aggregations, plus a "count": 
+  Average 
+  Minimum 
+  Maximum 
+  Sum 
+  Count - this returns the "number" of metrics returned by a query 

##### Group By
<a name="group-by"></a>

 This selector provides the ability to split metrics into lesser aggregates. Grouping by "priority" would return the metrics with a "tag" of priority and the unique values separated. 

### Templating
<a name="templating-2"></a>

 Instead of hardcoding names in your queries, you can use variables in their place. Variables are shown as dropdown select boxes at the top of the dashboard. You can use these dropdown boxes to change the data being displayed on your dashboard. 

 See the example in the **Query Variable** section on how to add a query variable and reference that with a Template value. 

#### Query variable
<a name="query-variable"></a>

 If you add a template variable of the type `Query`, you can write a query that can return items such as category names, key names, or key values that are shown as a dropdown select box. 

 For example, you can have a variable that contains all values for `categories` by specifying a query such as this in the templating variable *Query* setting. 

 When choosing the **Query** setting, a **Filter** section is displayed, allowing you to choose a **Type** and **Field**. Currently, **Type** is limited to Incidents and Changes. When selecting a type, you are provided with a list of fields applicable to that Type. Once a **Type** and **Field** are selected, a preview of values will be displayed at the bottom showing the options available for that Type/Field. Those values will be displayed in a dropdown list on the Dashboard, which you can use along with Templating to filter data on your Dashboard Panels. 

 For example, if you add a Variable named *category* then select Type = Incidents and Field = Category, you will see a list of options for Category. If you then add a Filter to a panel, and select Category Equals ${category}, the panel data will show only data for that Category that is selected from the Dashboard dropdown list. 

 Import the **Incidents By Category** dashboard to see an example. 

#### Using variables in queries
<a name="using-variables-in-queries"></a>

 There are two syntaxes: 

 `$<varname>` Example with a template variable named `hostname`: 

 `[[varname]]` Example with a template variable named `hostname`: 

## Alerting
<a name="servicenow-alerting"></a>

 Standard Grafana alerting is supported. Any queries defined in a graph panel can be used to generate alerts. 

 The following is an example query and an alert. This query will return a graph of all open critical high priority incidents: 

 This alert will be initiated when there are more than five open critical high priority incidents: 

 Testing the alert rule will display output from the alert rule, and selecting the state history will show the alert transitioning from ok to pending to alerting. 

 The graph view will show a vertical line and the heart icon at the top will turn orange while the alert is pending. 

 Once the criteria for alerting has been met, the rule transitions to red.

 In the graph view, the red vertical line will appear and the heart icon at the top will turn red. 

### Writing incidents for alerts
<a name="writing-incidents-for-alerts"></a>

 **Beta feature** 
+  Configure a Notification Channel for your ServiceNow data source. 

 This will configure a [Grafana Notification Channel](https://grafana.com/docs/grafana/latest/alerting/notifications/) which uses your configured user to create incidents on the ServiceNow instance for this data source. 

 This action requires that the ServiceNow data source user has permissions for writing incidents. 

## Annotations
<a name="annotations-1"></a>

 Grafana Annotations are a **beta feature** as of `v1.4.0` of this data source. Annotations give you the ability to overlay events on graphs. 

 The Annotations query supports the same options as the standard query editor with a few minor differences: 
+  Only one "Show" column is selectable. This is likely going to be fixed in a future improvement. 
+  The time field is required. 

## FAQ
<a name="faq-1"></a>

### What if we don’t have the ITSM Roles Plugin?
<a name="what-if-we-dont-have-the-itsm-roles-plugin"></a>

 **Administrator access is required to perform the following actions** 

 Option 1: Grant Grafana user admin permissions to allow access to all tables. 

 Option 2: Create a role and apply ACLs to all tables that must be accessed by Grafana.

 Administrator access is required to perform the following actions.

1.  The logged in administrator needs to elevate access to security\_admin.

   1.  In the top right navigation pane, choose the profile icon. The profile icon has dropdown caret indicator. 

   1.  From the dropdown list, choose **Elevate Roles**. 

   1.  From the modal that is shown, select the **security\_admin** check box.

   1.  Choose OK. 

1. Create a new role with whatever naming convention you want.

   1.  Navigate to the roles section in the left hand navigation System Security => Users and Groups => Roles 

   1.  Choose **New** at the top.

   1.  Enter a name for the role and a relevant description. 

   1.  Choose **Submit**. 

1.  Create a new user or modify an existing user with the needed roles. 

   1.  The role you create in Step 2 

   1.  personalize\_dictionary 

   1.  personalize\_choices 

   1.  cmdb\_read (this will grant read access to all cmdb tables) 

1.  Create Table ACLs for the required tables and fields. 

   1.  Create an ACL for the sys\_db\_object table. 

     1.  In the second search header column **Name**, enter **sys\_db\_object**, and press **Enter**. 

     1.  The filtered result should show **Table**. Choose **Table** to navigate into the record. 

     1.  On the tab section, choose **Controls**.

     1.  On the lower portion of the page, make sure that **Access Controls** is the selected tab. 

     1.  Choose **New** to create a new ACL. 

     1.  Change the **Operation** selection to read. 

     1.  In the **Requires Role** section in the lower part of the screen, choose (double-click) **Insert New Row**, and search for the role that you created. 

     1. After you select the role you created, choose the green check mark. 

     1.  Choose **Submit** in the lower part of the screen to create the ACL, and then choose **Continue** when the modal appears. 

1.  Create ACLs for specific sys\_db\_object fields. The following steps must be repeated for each of the following fields: Name, Label, Display Name, and Extends table. 

   1.  While still on the table record view for sys\_db\_object, select the **Columns** tab in the tab group closest to the top of the screen.

   1.  Locate the field name and select it. 

   1.  In the lower tab section, choose **New** on the **Access Controls** tab. 

   1.  Change the operation to read 

   1.  Choose (double-click) the insert a row text in the bottom "Requires role" table. 

   1.  Search for the role that you created, and choose the green check mark. 

   1.  Choose **Submit**. 

   1.  Make sure that you’ve repeated these steps for all required fields: Name, Label, Display Name, and Extends table. 

1.  Repeat the steps from 4.1 on Change, Incident, and any other non-CMDB tables that you want to query from Grafana. Do not repeat the steps from 4.2; that step is only required for sys\_db\_object. 