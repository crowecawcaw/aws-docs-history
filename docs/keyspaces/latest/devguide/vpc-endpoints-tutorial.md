# Step 5: Configure monitoring with

CloudWatch

This step shows you how to use Amazon CloudWatch to monitor the VPC endpoint connection to
Amazon Keyspaces.

AWS PrivateLink publishes data points to CloudWatch about your interface endpoints. You can
use metrics to verify that your system is performing as expected. The
`AWS/PrivateLinkEndpoints` namespace in CloudWatch includes the metrics for
interface endpoints. For more information, see [CloudWatch metrics for
AWS PrivateLink](../../../vpc/latest/privatelink/privatelink-cloudwatch-metrics.md "../../../vpc/latest/privatelink/privatelink-cloudwatch-metrics.md") in the _AWS PrivateLink Guide_.

###### To create a CloudWatch dashboard with VPC endpoint metrics

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Dashboards**. Then choose
   **Create dashboard**. Enter a name for the dashboard and
   choose **Create**.
3. Under **Add widget**, choose
   **Number**.
4. Under **Metrics**, choose
   **AWS/PrivateLinkEndpoints**.
5. Choose **Endpoint Type, Service Name, VPC Endpoint ID, VPC
   ID**.
6. Select the metrics `ActiveConnections` and
   `NewConnections`, and choose **Create
   Widget**.
7. Save the dashboard.
   The `ActiveConnections` metric is defined as the number of concurrent
   active connections that the endpoint received during the last one-minute period. The
   `NewConnections` metric is defined as the number of new connections that
   were established through the endpoint during the last one-minute period.

For more information about creating dashboards, see [Create
dashboard](../../../AmazonCloudWatch/latest/monitoring/create_dashboard.md "../../../AmazonCloudWatch/latest/monitoring/create_dashboard.md") in the _CloudWatch User Guide_.
