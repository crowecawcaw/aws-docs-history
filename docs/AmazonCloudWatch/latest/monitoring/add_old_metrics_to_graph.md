# Graph metrics manually on a CloudWatch dashboard

###### To add a metric that you can't find in search to a graph

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose
   **Dashboards**,
   and
   then
   choose
   a dashboard.
3. The dashboard must already contain a graph where you want to add the metric.
   If it doesn't, create the graph and add any metric to it. For more information,
   see [Adding a graph widget
   to a CloudWatch dashboard](add_graph_dashboard.md "add_graph_dashboard.md") .
4. Choose **Actions**, **View/edit source**.

A JSON block appears. The block specifies the widgets on the dashboard and their contents. The following is an example
of one part of this block, which defines one graph.

```

{
  "type": "metric",
  "x": 0,
  "y": 0,
  "width": 6,
  "height": 3,
  "properties": {
    "view": "singleValue",
    "metrics": [
      [
        "AWS/EBS",
        "VolumeReadOps",
        "VolumeId",
        "vol-1234567890abcdef0"
      ]
    ],
    "region": "us-west-1"
  }
},


```

In this example, the following section defines the metric shown on this graph.

```
[ "AWS/EBS", "VolumeReadOps", "VolumeId", "vol-1234567890abcdef0" ]
```

5. Add a comma after the end bracket if there isn't already one and then add a
   similar bracketed section after the comma. In this new section, specify the
   namespace, metric name, and any necessary dimensions of the metric that you're
   adding to the graph. The following is an example.

```
[ "AWS/EBS", "VolumeReadOps", "VolumeId", "vol-1234567890abcdef0" ],
[ "`MyNamespace`", "`MyMetricName`", "`DimensionName`", "`DimensionValue`" ]
```

For more information about the formatting of metrics in JSON, see
[Properties of a Metric Widget Object](../APIReference/CloudWatch-Dashboard-Body-Structure.md#CloudWatch-Dashboard-Properties-Metric-Widget-Object "../APIReference/CloudWatch-Dashboard-Body-Structure.md#CloudWatch-Dashboard-Properties-Metric-Widget-Object") in the Amazon CloudWatch API Reference. 6. Choose **Update**.
