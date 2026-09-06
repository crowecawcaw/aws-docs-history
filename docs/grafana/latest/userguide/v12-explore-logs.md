

# Logs in Explore
<a name="v12-explore-logs"></a>

****  
This documentation topic is designed for Grafana workspaces that support **Grafana version 12.x**.  
For Grafana workspaces that support Grafana version 10.x, see [Working in Grafana version 10](using-grafana-v10.md).  
For Grafana workspaces that support Grafana version 9.x, see [Working in Grafana version 9](using-grafana-v9.md).  
For Grafana workspaces that support Grafana version 8.x, see [Working in Grafana version 8](using-grafana-v8.md).

Explore allows you to investigate your logs in different data sources, including:
+ [OpenSearch](using-opensearch-in-AMG.md)
+ [Amazon CloudWatch](using-amazon-cloudwatch-in-AMG.md)
+ [InfluxDB](using-influxdb-in-AMG.md)
+ [Loki](using-loki-in-AMG.md)

During an infrastructure monitoring and incident response, you can dig deeper into the metrics and logs to find the cause. Explore also allows you to correlate logs with other telemetry signals such as metrics, traces, or profiles, by viewing them side-by-side. You can also add correlations to external URLs directly from Explore, enabling seamless navigation between data sources and external systems.

The logs visualization panel provides improved log rendering with a field selector component for customizing which fields are displayed. Loki queries in Explore support forward direction search, allowing you to search logs from oldest to newest.

The results of log queries are displayed as individual log lines and as a graph showing the logs volume for the selected time period.

## Logs volume
<a name="v12-explore-logs-volume"></a>

When working with data sources that support a full range logs volume, Explore automatically displays a graph showing the log distribution for all the entered log queries. This feature is currently supported by OpenSearch and Loki data sources.

**Note**  
In Loki, this full range log volume is rendered by a metric query which can be expensive depending on the time range queried. This query can be particularly challenging to process for smaller Loki installations. To mitigate this, you can use a proxy like [nginx](https://www.nginx.com/) in front of Loki to set a custom timeout (for example, 10 seconds) for these queries. Log volume histogram queries can be identified by looking for queries with the HTTP header `X-Query-Tags` with value `Source=logvolhist`; these headers are added by Grafana to all log volume histogram queries.

If the data source does not support loading the full range logs volume, the logs model calculates a time series by counting log rows and organizing them into buckets based on an automatically calculated time interval. The timestamp of the first log row is used to anchor the start of the logs volume in the results. The end of the time series is anchored to the time picker’s **To** range. This way, you can still analyze and visualize log data efficiently even when the data source doesn’t offer full range support.

## Logs
<a name="v12-explore-logs-overview"></a>

In the following sections, you will find detailed explanations of how to visualize and interact with individual logs in Explore.

## Logs navigation
<a name="v12-explore-logs-navigation"></a>

Logs navigation, at the right side of the log lines, can be used to easily request additional logs. You can do this by clicking the **Older logs** button at the bottom of the navigation. This is especially useful when you reach the line limit and you want to see more logs. Each request that is run from the navigation is then displayed in the navigation as separate page. Every page shows `from` and `to` timestamps of the incoming log lines. You can see previous results by clicking on each page. Explore caches the last five requests run from the logs navigation, so you’re not re-running the same queries when clicking on the pages, saving time and resources.

## Visualization options
<a name="v12-explore-log-visualization-options"></a>

 You can customize how logs are displayed and select which columns are shown. 


| Option | Description | 
| --- | --- | 
| Time | Shows or hides the time column. This is the timestamp associated with the log line as reported from the data source. | 
| Unique labels | Shows or hides the unique labels column that includes only non-common labels. All common labels are displayed above. | 
| Wrap lines | Set this to true if you want the display to use line wrapping. If set to false, it will result in horizontal scrolling. | 
| Prettify JSON |  Set this to true to pretty print all JSON logs. This setting does not affect logs in any format other than JSON. | 
| Deduplication | Log data can be very repetitive and Explore can help by hiding duplicate log lines. There are a few different deduplication algorithms that you can use. Exact matches are done on the whole line except for date fields. Numbers matches are done on the line after stripping out numbers such as durations, IP addresses, and so on. Signature is the most aggressive deduplication as it strips all letters and numbers and matches on the remaining whitespace and punctuation. | 
| Display results order | You can change the order of received logs from the default descending order (newest first) to ascending order (oldest first). | 

## Download log lines
<a name="v12-explore-download-log-lines"></a>

To download log results in either `txt` or `json` format, use the **Download** button. This feature allows you to save the log data for further analysis or to share it with others in a convenient and accessible format.

## Log result meta information
<a name="v12-explore-log-result-meta-information"></a>

Above the received log lines you can find essential meta information, including:
+ **Number of received logs** – Indicates the total count of logs received for the current query or time range.
+ **Error** – Displays possible error in your log results.
+ **Common labels** – Shows common labels.
+ **Total bytes processed** – Represents the cumulative size of the log data processed in bytes.

**Note**  
The availability of certain meta information may depend on the data source, and as a result, you may only see some of these details for specific data sources.

## Escaping newlines
<a name="v12-explore-log-escaping-newlines"></a>

Explore automatically detects some incorrectly escaped sequences in log lines, such as newlines (`\n`, `\r`) or tabs (`\t`). When it detects such sequences, Explore provides an **Escape newlines** option.

**To automatically fix incorrectly escaped sequences that Explore has detected**

1. Choose **Escape newlines** to replace the sequences.

1. Manually review the replacements to confirm their correctness.

Explore replaces these sequences. When it does so, the option will change from **Escape newlines** to **Remove escaping**. Evaluate the changes as the parsing may not be accurate based on the input received. You can revert the replacements by selecting **Remove escaping**.

## Log level
<a name="v12-explore-log-level"></a>

For the logs where a `level` label is specified, we use the value of this label to determine the log level and update color of each log line accordingly. If the log doesn’t have specified level label, we try to find out if its content matches any of the supported expressions (see the following table for more information). The log level is always determined by the first match. In the case where Grafana is not able to infer a log level field, it will be visualized with an unknown log level.

**Note**  
If you use a Loki data source and the `level` is part of your log line, you can use parsers (JSON, logfmt, regex,..) to extract the level information into a level label that is used to determine the level value. This will allow the histogram to show the various log levels as separate bars.

**Supported log levels and mapping of log level abbreviation and expressions:** 


| Log level | Color | Supported expressions | 
| --- | --- | --- | 
| critical | purple | emerg, fatal, alert, crit, critical | 
| error | red | err, eror, error | 
| warning | yellow | warn, warning | 
| info | green | info, information, informational, notice | 
| debug | blue | dbug, debug | 
| trace | light blue | trace | 
| unknown | grey | \* | 

## Highlight searched words
<a name="v12-explore-highlight-searched-words"></a>

When your query includes specific words or expressions to search for, Explore will highlight these in the log lines for better visibility. This highlighting feature makes it easier to identify and focus on the relevant content in your logs.

**Note**  
The ability to highlight search words may vary depending on the data source. For some data sources, the highlighting of search words may not be available.

## Log details view
<a name="v12-explore-log-details-view"></a>

In Explore, each log line has an expandable section called *Log details* that can be opened by choosing the log line. The Log details view provides additional information and exploration options in the form of *Fields* and *Links* attached to the log lines, enabling a more robust interaction and analysis.

**Fields**

Within the Log details view, you can filter displayed fields in two ways: a positive filter (to focus on an specific field) and a negative filter (to exclude certain fields). These filters will update the corresponding query that produced the log line, adding equality and inequality expressions accordingly. If the data source has support, as is the case for Loki and OpenSearch, log details will check if the field is already present in the current query showing and active state (for positive filters only), allowing you to toggle it off the query, or changing the filter expression from positive to negative.

You can select a subset of fields to visualize in the logs list instead of the complete log line by clicking on the eye icon. Each field has a stats icon to display statistics in relation to all displayed logs.

**Links**

Grafana offers the functionality of data links or correlations, enabling you to convert any part of a log message into an internal or external link. These links can be used to navigate to related data or external resources, providing a seamless and convenient way to explore further information.

## Log context
<a name="v12-explore-log-context"></a>

Log context displays additional lines of context surrounding a log entry that matches a particular search query. This can be helpful in understanding the log entry’s context, and is similar to the `-C` parameter in the `grep` command.

You may encounter long lines of text that make it difficult to read and analyze the context around each log entry. This is where the **Wrap lines** toggle can come in handy. By enabling this toggle, Grafana will automatically wrap long lines of text so that they fit within the visible width of the viewer. This can make it easier to read and understand the log entries. 

 The **Open in split view** button allows you to execute the context query for a log entry in a split screen in the Explore view. Choosing this button will open a new Explore pane with the context query displayed alongside the log entry, making it easier to analyze and understand the surrounding context.

The log context query can also be opened in a new browser tab by pressing the `Ctrl` (or `Cmd`) key while choosing the button to open the context modal. When opened in a new tab, the previously selected filters are applied as well.

## Copy log line
<a name="v12-explore-copy-log-line"></a>

You can easily copy the content of a selected log line to your clipboard by choosing the **Copy log line** button.

## Copy link to log line
<a name="v12-explore-copy-link-to-log-line"></a>

Linking of log lines in Grafana allows you to quickly navigate to specific log entries for precise analysis. By choosing the **Copy shortlink** button for a log line, you can generate and copy a short URL that provides direct access to the exact log entry within an absolute time range. When you open the link, Grafana will automatically scroll to the corresponding log line and highlight it with a blue background, making it easy to identify and focus on the relevant information.

**Note**  
This is only supported in Loki and other data sources that provide an `id` field.