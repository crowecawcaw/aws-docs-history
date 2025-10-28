# View NAT gateway CloudWatch metrics

NAT gateway metrics are sent to CloudWatch at 1-minute intervals. Metrics are grouped first
by the service namespace, and then by the possible combinations of dimensions within
each namespace. You can view the metrics for your NAT gateways as follows.

###### To view metrics using the CloudWatch console

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Metrics**, **All
   metrics**.
3. Choose the **NATGateway** metric namespace.
4. Choose a metric dimension.

###### To view metrics using the AWS CLI

At a command prompt, use the following command to list the metrics that are
available for the NAT gateway service.

```
`aws cloudwatch list-metrics --namespace "AWS/NATGateway"`
```
