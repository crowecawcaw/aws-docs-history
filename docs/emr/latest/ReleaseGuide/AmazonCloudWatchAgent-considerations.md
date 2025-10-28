# Considerations and limitations

- The native Amazon CloudWatch agent is available for clusters that you create with Amazon EMR
  releases 7.0.0 and higher.
- The configuration for CloudWatch agent in Amazon EMR 7.0.0 requires the use of [bootstrap actions](AmazonCloudWatchAgent-config-700.md "AmazonCloudWatchAgent-config-700.md"). In an upcoming
  release, Amazon EMR will provide additional configuration options through the Amazon EMR
  API.
- You can't install the Amazon EMR CloudWatch agent if you've already deployed the CloudWatch agent
  by another method such as AWS Systems Manager Agent (SSM Agent) in the Region where you
  create your cluster. Doing so will result in your cluster terminating with
  errors.
- The CloudWatch GetMetricData API supports up to 500 metrics per request. If your Amazon EMR cluster contains more than 250 nodes
  in an instance group or fleet, the corresponding graphs in the CloudWatch embedded dashboard in EMR will appear blank with
  the error **Too many metrics** because these metrics require two data points per metric in
  the **Cluster Overview** dashboard. However, by filtering the **Core** or **Task Instance Group** (or fleet) dashboards, you
  will be able to view the graphs for up to 500 nodes per instance group or fleet. This is because these do not require two data points per metric. Beyond 500 nodes per
  instance group or fleet, the **Too many metrics** error also occurs for the metrics in these dashboards.
