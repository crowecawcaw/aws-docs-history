# Reviewing cross-Region aggregation settings

You can view the current cross-Region aggregation configuration in AWS Security Hub from any AWS Region in the administrator account or in a standalone account. Member accounts cannot view cross-Region aggregation configuration. The configuration includes the home Region, and the linked Regions (if any).

Follow the steps to view your current cross-Region aggregation settings

###### To view cross-Region aggregation settings (console)

1. Open the AWS Security Hub console at [https://console.aws.amazon.com/securityhub/v2/home](https://console.aws.amazon.com/securityhub/v2/home "https://console.aws.amazon.com/securityhub/v2/home").
2. On the navigation pane, choose **Settings** and then the **General**.
3. If cross-Region aggregation is not enabled, then the General page displays the option to enable cross-Region aggregation. Only administrator accounts and standalone accounts can enable cross-Region aggregation.
4. If cross-Region aggregation is enabled, then the Regions tab displays the following information:
   - The home Region
   - Whether to automatically aggregate findings, resources, and trends from new Regions that Security Hub supports and that you opt into
   - The list of linked Regions (if any are selected)
