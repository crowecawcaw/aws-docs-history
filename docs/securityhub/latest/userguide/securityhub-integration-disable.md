# Disabling the flow of findings from a

Security Hub CSPM integration

Choose your preferred method, and follow the steps to disable the flow of findings
from an AWS Security Hub CSPM integration.

Security Hub CSPM console

###### To disable the flow of findings from an integration (console)

1. Open the AWS Security Hub CSPM console at [https://console.aws.amazon.com/securityhub/](https://console.aws.amazon.com/securityhub/ "https://console.aws.amazon.com/securityhub/").
2. In the Security Hub CSPM navigation pane, choose
   **Integrations**.
3. For integrations that send findings, the
   **Status** information indicates whether Security Hub CSPM
   is currently accepting findings from that integration.
4. Choose **Stop accepting findings**.

Security Hub CSPM API
Use the [DisableImportFindingsForProduct](../../1.0/APIReference/API_DisableImportFindingsForProduct.md "../../1.0/APIReference/API_DisableImportFindingsForProduct.md") operation.
If you're using the AWS CLI, run the [disable-import-findings-for-product](../../../cli/latest/reference/securityhub/disable-import-findings-for-product.md "../../../cli/latest/reference/securityhub/disable-import-findings-for-product.md") command.
To disable the flow of findings from an integration, you need the
subscription ARN for the enabled integration. To obtain the subscription
ARN, use the [ListEnabledProductsForImport](../../1.0/APIReference/API_ListEnabledProductsForImport.md "../../1.0/APIReference/API_ListEnabledProductsForImport.md") operation. If
you're using the AWS CLI, run the [list-enabled-products-for-import](../../../cli/latest/reference/securityhub/list-enabled-products-for-import.md "../../../cli/latest/reference/securityhub/list-enabled-products-for-import.md").

For example, the following AWS CLI command disables the flow of findings to
Security Hub CSPM from the CrowdStrike Falcon integration. This example is formatted for
Linux, macOS, or Unix, and it uses the backslash (\) line-continuation
character to improve readability.

```
`$` `aws securityhub disable-import-findings-for-product --product-subscription-arn "`arn:aws:securityhub:us-west-1:123456789012:product-subscription/crowdstrike/crowdstrike-falcon`"`
```
