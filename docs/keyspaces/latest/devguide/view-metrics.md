# Viewing Amazon Keyspaces metrics in CloudWatch

When you interact with Amazon Keyspaces, it sends the following metrics and dimensions to Amazon CloudWatch.
All metrics are aggregated and reported every minute. You can use the following procedures
to view the metrics for Amazon Keyspaces.

###### To view metrics using the CloudWatch console

Metrics are grouped first by the service namespace, and then by the various dimension
combinations within each namespace.

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. If necessary, change the AWS Region. On the navigation bar, choose the Region where your
   AWS resources reside. For more information, see [AWS service
   endpoints](../../../general/latest/gr/rande.md "../../../general/latest/gr/rande.md").
3. In the navigation pane, choose **Metrics**.
4. Under the **All metrics** tab, choose
   `AWS/Cassandra.`

###### To view metrics using the AWS CLI

- At a command prompt, use the following command.

```
`aws cloudwatch list-metrics --namespace "AWS/Cassandra"`
```
