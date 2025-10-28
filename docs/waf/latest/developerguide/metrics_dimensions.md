**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the updated console experience](working-with-console.md "working-with-console.md").

# Viewing metrics and dimensions

Metrics are grouped first by the service namespace, and then by the various
dimension combinations within each namespace. AWS Firewall Manager doesn't record metrics.

- The AWS WAF namespace is `AWS/WAFV2`
- The Shield Advanced namespace is `AWS/DDoSProtection`

###### Note

AWS WAF reports metrics once a minute.

Shield Advanced reports metrics once a minute during an event and less frequently
other times.

Use the following procedures to view the metrics for AWS WAF and
AWS Shield Advanced.

###### To view metrics using the CloudWatch console

1. Sign in to the AWS Management Console and open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. If necessary, change the Region to the one where your AWS resources
   are located. For CloudFront, choose the US East (N. Virginia) Region.
3. In the navigation pane, under **Metrics**, choose
   **All metrics** and then search under the
   **Browse** tab for the service.

###### To view metrics using the AWS CLI

- For AWS/WAFV2, at a command prompt use the following command:

```
`aws cloudwatch list-metrics --namespace "AWS/WAFV2"`

```

For Shield Advanced, at a command prompt use the following command:

```
`aws cloudwatch list-metrics --namespace "AWS/DDoSProtection"`

```
