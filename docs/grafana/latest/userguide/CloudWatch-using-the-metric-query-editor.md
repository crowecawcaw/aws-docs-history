

# Using the metric query editor
<a name="CloudWatch-using-the-metric-query-editor"></a>

The metric query editor allows you to build two types of queries - **Metric Search** and **Metric Query**. The **Metric Query** option queries data using CloudWatch Metrics Insights.

## Common query editor fields
<a name="metrics-insights-common-fields"></a>

 There are three fields that are common to both **Metric Search** and **Metric Query** modes.

 **Common fields**

**Id**  
The `GetMetricData` API requires that all queries have a unique ID. Use this field to specify an ID of choice. The ID can include numbers, letters, and underscores, and must start with a lowercase letter. If no ID is specified, Amazon Managed Grafana generates an ID using the following pattern: `query[refId of the current query row]`. For example, `queryA` represents the first query row in the panel editor.

**Period**  
A period is the length of time associated with a specific CloudWatch statistic. Periods are defined in numbers of seconds. Valid values include 1, 5, 10, 30, or any multiple of 60. If you keep the period field blank or set to `auto`, then it calculates automatically based on the time range and the CloudWatch retention policy. The formula used is `time range in seconds / 2000`, and then it moves on to the next higher value in an array of predefined periods [60, 300, 900, 3600, 21600, 86400] after removing periods based on retention. To see which period Amazon Managed Grafana is using, choose **Show Query Preview** in the query editor.

**Alias**  
The following alias patterns apply.  


<table>
<thead>
  <tr><th> Alias pattern </th><th> Description </th><th> Example result </th></tr>
</thead>
<tbody>
  <tr><td> <code>{{region}}</code> </td><td> Returns the Region.</td><td> <code>us-east-1</code> </td></tr>
  <tr><td> <code>{{period}}</code> </td><td> Returns the period. </td><td> <code>3000</code> </td></tr>
  <tr><td> <code>{{metric}}</code> </td><td> Returns the metric. </td><td> <code>CPUUtilization</code> </td></tr>
  <tr><td> <code>{{label}}</code> </td><td>Returns the label returned by the API operation (<b>Metric Search</b> only). </td><td> <code>i-01343</code> </td></tr>
  <tr><td> <code>{{namespace}}</code> </td><td> Returns the namespace (<b>Metric Search</b> only). </td><td> <code>AWS/EC2</code> </td></tr>
  <tr><td> <code>{{stat}}</code> </td><td> Returns the statistic (<b>Metric Search</b> only). </td><td> <code>Average</code> </td></tr>
  <tr><td> <code>{{[dimension name]}}</code> </td><td> Returns the dimension name (<b>Metric Search</b> only). </td><td> <code>i-01343</code> </td></tr>
</tbody>
</table>
