

# Disabling the flow of findings from a Security Hub CSPM integration
<a name="securityhub-integration-disable"></a>

Choose your preferred method, and follow the steps to disable the flow of findings from an AWS Security Hub CSPM integration.

------
#### [ Security Hub CSPM console ]

**To disable the flow of findings from an integration (console)**

1. Open the AWS Security Hub CSPM console at [https://console.aws.amazon.com/securityhub/](https://console.aws.amazon.com/securityhub/).

1. In the Security Hub CSPM navigation pane, choose **Integrations**.

1. For integrations that send findings, the **Status** information indicates whether Security Hub CSPM is currently accepting findings from that integration.

1. Choose **Stop accepting findings**.

------
#### [ Security Hub CSPM API ]

Use the [DisableImportFindingsForProduct](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_DisableImportFindingsForProduct.html) operation. If you're using the AWS CLI, run the [disable-import-findings-for-product](https://docs.aws.amazon.com/cli/latest/reference/securityhub/disable-import-findings-for-product.html) command. To disable the flow of findings from an integration, you need the subscription ARN for the enabled integration. To obtain the subscription ARN, use the [ListEnabledProductsForImport](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_ListEnabledProductsForImport.html) operation. If you're using the AWS CLI, run the [list-enabled-products-for-import](https://docs.aws.amazon.com/cli/latest/reference/securityhub/list-enabled-products-for-import.html).

For example, the following AWS CLI command disables the flow of findings to Security Hub CSPM from the CrowdStrike Falcon integration. This example is formatted for Linux, macOS, or Unix, and it uses the backslash (\\) line-continuation character to improve readability.

```
$ aws securityhub disable-import-findings-for-product --product-subscription-arn "{{arn:aws:securityhub:us-west-1:123456789012:product-subscription/crowdstrike/crowdstrike-falcon}}"
```

------