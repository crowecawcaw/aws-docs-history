

# Connect to a Loki data source
<a name="using-loki-in-AMG"></a>

 The Loki data source provides access to Loki, Grafana’s log aggregation system. 

## Adding the data source
<a name="loki-adding-the-data-source"></a>

1.  Open the Grafana workspace and make sure you are logged in. 

1.  In the side menu under the **Configuration** link you should find a **Data Sources** link. 

1.  choose the **Add data source** button at the top. 

1.  Select **Loki** from the list of data sources. 

**Note**  
 If you don't see the **Data Sources** link in your side menu, it means that your current user does not have the `Admin` role. 


|  Name  |  Description  | 
| --- | --- | 
|  Name  |  The data source name. This is how you see the data source in panels, queries, and Explore.  | 
|  Default  |  Default data source means that it will be pre-selected for new panels.  | 
|  URL  | The URL of the Loki instance; e.g., http://localhost:3100. This could be the URL for an Amazon EC2 host, or an Application Load Balancer in front of an Amazon EKS cluster, or any other URL for a Loki instance. | 
|  Maximum lines  |  Upper limit for number of log lines returned by Loki (default is 1000). Decrease if your browser is sluggish when displaying logs in Explore.  | 

### Derived fields
<a name="loki-derived-fields"></a>

 You can use the *derived fields* configuration to do the following: 
+  Add fields parsed from the log message. 
+  Add a link that uses the value of the field. 

 You can use this functionality to link to your tracing backend directly from your logs, or link to a user profile page if a userId is present in the log line. These links appear in the log details. For more information, see [Labels and detected fields](explore.md#labels-and-detected-fields). 

Each derived field consists of the following: 
+  **Name** – Shown in the log details as a label. 
+  **Regex** – A Regex pattern that runs on the log message and captures part of it as the value of the new field. Can only contain a single capture group. 
+  **URL/query** – If the link is external, then enter the full link URL. If the link is internal link, then this input serves as query for the target data source. In both cases, you can interpolate the value from the field with `${__value.raw }` macro. 
+  **Internal link** – Select if the link is internal or external. In case of internal link, a data source selector allows you to select the target data source. Only tracing data sources are supported. 

 You can use a debug section to see what your fields extract and how the URL is interpolated. choose **Show example log message** to show the text area where you can enter a log message. 

 The new field with the link shown in log details. 

## Querying logs
<a name="loki-querying-logs"></a>

 Querying and displaying log data from Loki is available via Explore and with the logs panel in visualizations. Select the Loki data source, and then enter a LogQL query to display your logs. For more information about LogQL, see [LogQL](https://grafana.com/docs/loki/latest/logql/). 

### Log queries
<a name="loki-log-queries"></a>

 A log query consists of two parts: **log stream selector**, and a **search expression**. For performance reasons, you must start by choosing a log label for a log stream. 

 The Logs Explorer (the **Log labels** button) next to the query field shows a list of labels of available log streams. An alternative way to write a query is to use the query field’s automatic completion. You start by typing a left curly brace `{` and the autocomplete menu will suggest a list of labels. Press the **Enter** key to run the query. 

 After the result is returned, the log panel shows a list of log rows and a bar chart where the x-axis shows the time and the y-axis shows the frequency/count. 

### Log Stream Selector
<a name="log-stream-selector"></a>

 For the label part of the query expression, wrap it in curly braces `{}` and then use the key value syntax for selecting labels. Multiple label expressions are separated by a comma: 

 `{app="mysql",name="mysql-backup"}` 

 The following label matching operators are currently supported: 
+  `=` exactly equal. 
+  `!=` not equal. 
+  `=~` regex-match. 
+  `!~` do not regex-match. 

 Examples: 
+  `{name=~"mysql.+"}` 
+  `{name!~"mysql.+"}` 

 Another way to add a label selector is in the table section. choose **Filter** beside a label to add the label to the query expression. This even works for multiple queries and will add the label selector to each query. 

### Search expressions
<a name="loki-search-expression"></a>

 After writing the Log Stream Selector, you can filter the results further by writing a search expression. The search expression can be just text or a regex expression. 

 Example queries: 
+  `{job="mysql"} |= "error"` 
+  `{name="kafka"} |~ "tsdb-ops.*io:2003"` 
+  `{instance=~"kafka-[23]",name="kafka"} != "kafka.server:type=ReplicaManager"` 

 Filter operators can be chained and will sequentially filter down the expression. The resulting log lines will satisfy every filter. 

 Example 

 `{job="mysql"} |= "error" != "timeout"` 

 The following filter types are currently supported: 
+  `|=` line contains string. 
+  `!=` line doesn’t contain string. 
+  `|~` line matches regular expression. 
+  `!~` line does not match regular expression. 

**Note**  
 For more information about LogQL, Loki’s query language, see [Loki LogQL](https://grafana.com/docs/loki/latest/logql/). 

## Log context
<a name="loki-log-context"></a>

 When using a search expression as detailed above, you now have the ability to retrieve the context surrounding your filtered results. By choosing the `Show Context` link on the filtered rows, you’ll be able to investigate the log messages that came before and after the log message you’re interested in. 

## Templating
<a name="loki-templating"></a>

 Instead of hardcoding things such as server, application and sensor name in your metric queries, you can use variables in their place. Variables are shown as dropdown select boxes at the top of the dashboard. You can use these dropdown boxes to change the data being displayed in your dashboard. 

 For more information about templating and template variables, see [Templates and variables](templates-and-variables.md). 

## Annotations
<a name="loki-annotations"></a>

 You can use any non-metric Loki query as a source for annotations. Log content will be used as annotation text and your log stream labels as tags, so there is no need for additional mapping. 