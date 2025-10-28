# View Amazon CloudWatch Logs metrics for AWS Site-to-Site VPN

When you create a Site-to-Site VPN connection, the VPN service sends metrics
about your VPN connection to CloudWatch, as they become available. You can view the metrics for
your VPN connection as follows.

###### To view metrics using the CloudWatch console

Metrics are grouped first by the service namespace, and then by the various
dimension combinations within each namespace.

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Metrics**.
3. Under **All metrics**, choose the
   **VPN** metric namespace.
4. Select the metric dimension to view the metrics— for example,
   **VPN Tunnel Metrics**.

###### Note

The VPN namespace will not appear in the CloudWatch console until after a Site-to-Site VPN connection has been created in the AWS region you are viewing.

###### To view metrics using the AWS CLI

At a command prompt, use the following command:

```
`aws cloudwatch list-metrics --namespace "AWS/VPN"`
```
