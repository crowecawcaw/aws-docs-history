# Reviewing cross-Region aggregation settings

###### Note

The _aggregation Region_ is now called the _home Region_. Some Security Hub CSPM API operations still use the older term aggregation
Region.

You can view the current cross-Region aggregation configuration in AWS Security Hub CSPM from any AWS Region. The
configuration includes the home Region, the linked Regions (if any), and whether to
automatically link new Regions as Security Hub CSPM supports them.

Member accounts can view the cross-Region aggregation settings that the administrator account configured.

Choose your preferred method, and follow the steps to view your current cross-Region aggregation settings.

Security Hub CSPM console

###### To view cross-Region aggregation settings (console)

1. Open the AWS Security Hub CSPM console at [https://console.aws.amazon.com/securityhub/](https://console.aws.amazon.com/securityhub/ "https://console.aws.amazon.com/securityhub/").
2. On the navigation pane, choose **Settings** and then the
   **Regions** tab.

If cross-Region aggregation is not enabled, then the **Regions**
tab displays the option to enable cross-Region aggregation. Only administrator accounts and
standalone accounts can enable cross-Region aggregation.

If cross-Region aggregation is enabled, then the **Regions** tab
displays the following information:

- The home Region
- Whether to automatically aggregate findings, insights, control statuses,
  and security scores from new Regions that Security Hub CSPM supports and that you opt
  into
- The list of linked Regions (if any are selected)

Security Hub CSPM API
**To review cross-Region aggregation settings (Security Hub CSPM API)**

Use the [`GetFindingAggregator`](../../1.0/APIReference/API_GetFindingAggregator.md "../../1.0/APIReference/API_GetFindingAggregator.md") operation of the Security Hub CSPM API. If you use the AWS CLI, run the
[get-finding-aggregator](../../../cli/latest/reference/securityhub/get-finding-aggregator.md "../../../cli/latest/reference/securityhub/get-finding-aggregator.md")
command.

When you make the request, provide the finding aggregator ARN. To obtain the finding
aggregator ARN, use the [`ListFindingAggregators`](../../1.0/APIReference/API_ListFindingAggregators.md "../../1.0/APIReference/API_ListFindingAggregators.md") operation or [list-finding-aggregators](../../../cli/latest/reference/securityhub/list-finding-aggregators.md "../../../cli/latest/reference/securityhub/list-finding-aggregators.md")
command.

The following example shows the cross-Region aggregation settings for the specified finding aggregator ARN. This example is formatted for Linux, macOS, or Unix,
and it uses the backslash (\) line-continuation character to improve readability

```
`$``aws securityhub get-finding-aggregator --finding-aggregator-arn `arn:aws:securityhub:us-east-1:222222222222:finding-aggregator/123e4567-e89b-12d3-a456-426652340000``
```
