

# The panel inspect view
<a name="v9-panels-panel-inspector"></a>

****  
This documentation topic is designed for Grafana workspaces that support **Grafana version 9.x**.  
For Grafana workspaces that support Grafana version 12.x, see [Working in Grafana version 12](using-grafana-v12.md).  
For Grafana workspaces that support Grafana version 10.x, see [Working in Grafana version 10](using-grafana-v10.md).  
For Grafana workspaces that support Grafana version 8.x, see [Working in Grafana version 8](using-grafana-v8.md).

 The panel inspect view, which you can open via the panel menu, helps you understand and troubleshoot your panels. You can inspect the raw data for any Grafana panel, export that data to a comma-separated values (CSV) file, view query requests, and export panel and data JSON. 

**Note**  
 Not all panel types include all tabs. For example, dashboard list panels do not have raw data to inspect, so they do not display the Stats, Data, or Query tabs. 

 The panel inspector consists of the following options: 

1.  The panel inspector displays **Inspect: [NameOfPanelBeingInspected]** at the top of the pane. Click the arrow in the upper right corner to expand or reduce the pane. 

1.  **Data tab -** Shows the raw data returned by the query with transformations applied. Field options such as overrides and value mappings are not applied by default. 

1.  **Stats tab -** Shows how long your query takes and how much it returns. 

1.  **JSON tab -** Allows you to view and copy the panel JSON, panel data JSON, and data frame structure JSON. This is useful if you are provisioning or administering Grafana. 

1.  **Query tab -** Shows you the requests to the server sent when Grafana queries the data source. 

1.  **Error tab -** Shows the error. Only visible when query returns error. 

## Download raw query results
<a name="v9-panels-raw-query-results"></a>

 Grafana generates a CSV file that contains your data, including any transformations to that data. You can choose to view the data before or after the panel applies field options or field option overrides. 

1.  Edit the panel that contains the query data you want to download. 

1.  In the query editor, click **Query Inspector**. 

1.  Click **Data**. 

    If your panel contains multiple queries or queries multiple nodes, then you have additional options. 
   +  **Select result**: Choose which result set data you want to view. 
   +  **Transform data** 
   +  **Join by time**: View raw data from all your queries at once, one result set per column. Click a column heading to reorder the data. 

1.  To see data before the system applies field overrides, click the **Formatted data** toggle. 

1.  To download a CSV file specifically formatted for Excel, click the **Download for Excel** toggle . 

1.  Click **Download CSV**. 

## Inspect query performance
<a name="v9-panels-query-performance"></a>

 The **Stats** tab displays statistics that tell you how long your query takes, how many queries you send, and the number of rows returned. This information can help you troubleshoot your queries, especially if any of the numbers are unexpectedly high or low. 

1.  Edit the panel that contains the query with performance you want to inspect. 

1.  In the query editor, click **Query Inspector**. 

1.  Click **Stats**. 

 Statistics are displayed in read-only format. 

## Inspect query request and response
<a name="v9-panels-query-request-response"></a>

 Inspect query request and response data when you want to troubleshoot a query that returns unexpected results, or fails to return expected results. 

1.  Edit the panel that contains the query you want to export. 

1.  In the query editor, click **Query Inspector**. 

1.  Click **Refresh**. 

    The panel populates with response data. 

1.  Make adjustments, as necessary and re-run the query. 

1.  To download the query request and response data, click the **Copy to clipboard** icon and paste the results into another application. 