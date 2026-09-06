

# anomaly
<a name="CWL_QuerySyntax-Anomaly"></a>

 Use `anomaly` to automatically identify unusual patterns and potential issues within your log data using machine learning. 

The `anomaly` command extends the existing `pattern` functionality and uses advanced analytics to help identify potential anomalies in log data. You can use `anomaly` to reduce the time it takes to identify and resolve operational issues by automatically surfacing unusual patterns or behaviors in your logs.

The `anomaly` command works with the ` pattern` command to first identify log patterns, then detect anomalies within those patterns. You can also combine `anomaly` with the ` filter` or ` sort` commands to focus anomaly detection on specific subsets of your data. 

**Anomaly Command Input**

 The `anomaly` command is typically used after the ` pattern` command to analyze the patterns identified in your log data. The command does not require additional parameters and analyzes the output from preceding commands in your query. 

**Types of Anomalies Identified**

 The `anomaly` command identifies five distinct types of anomalies:
+ *Pattern Frequency Anomalies*: Unusual frequencies of specific log patterns, such as when an application starts generating more error messages than usual.
+ *New Pattern Anomalies*: Previously unseen log patterns that may indicate new types of errors or messages appearing in your logs.
+ *Token Variation Anomalies*: Unexpected changes in log message contents that may indicate unusual variations in expected log formats.
+ *Numerical Token Anomalies*: Unusual changes in numerical values within logs that can help detect potential performance issues or unexpected metric variations.
+ *HTTP Error Code Anomalies*: Patterns related to HTTP error responses, particularly useful when monitoring web applications and APIs.

**Anomaly Command Output**

 The `anomaly` command preserves all fields from the input data and adds anomaly detection results to help identify unusual patterns in your log data.

**Examples**

The following command identifies patterns in your log data and then detects anomalies within those patterns:

```
fields @timestamp, @message
| pattern @message
| anomaly
```

The `anomaly` command can be used with filtering to focus on specific log types:

```
fields @timestamp, @message
| filter @type = "REPORT"
| pattern @message
| anomaly
```

The `anomaly` command can be combined with sorting to organize results:

```
fields @timestamp, @message
| filter @type = "ERROR"
| pattern @message
| anomaly
| sort @timestamp desc
```