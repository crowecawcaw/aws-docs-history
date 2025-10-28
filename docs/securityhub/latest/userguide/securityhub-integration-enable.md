# Enabling the flow of findings from a

Security Hub CSPM integration

On the **Integrations** page of the AWS Security Hub CSPM console, you can see
the required steps to enable each integration.

For most of the integrations with other AWS services, the only required step to
enable the integration is to enable the other service. The integration information
includes a link to the other service's home page. When you enable the other service, a
resource-level permission that allows Security Hub CSPM to receive findings from the service is then
automatically created and applied.

For third-party product integrations, you may need to purchase the integration from
the AWS Marketplace, and then configure the integration. The integration information provides
links to complete these tasks.

If more than one version of a product is available in AWS Marketplace, select the version that
you wan to subscribe to, and then choose **Continue to Subscribe**. For
example, some products offer a standard version and an AWS GovCloud (US) version.

When you enable a product integration, a resource policy is automatically attached to
that product subscription. This resource policy defines the permissions that Security Hub CSPM needs
to receive findings from that product.

After you complete any preliminary steps to enable an integration, you can then
disable and re-enable the flow of findings from that integration. On the
**Integrations** page, for integrations that send findings, the
**Status** information indicates whether you are currently
accepting findings.

Security Hub CSPM console

###### To enable the flow of findings from an integration (console)

1. Open the AWS Security Hub CSPM console at [https://console.aws.amazon.com/securityhub/](https://console.aws.amazon.com/securityhub/ "https://console.aws.amazon.com/securityhub/").
2. In the Security Hub CSPM navigation pane, choose
   **Integrations**.
3. For integrations that send findings, the
   **Status** information indicates whether Security Hub CSPM
   is currently accepting findings from that integration.
4. Choose **Accept findings**.

Security Hub CSPM API
Use the [EnableImportFindingsForProduct](../../1.0/APIReference/API_EnableImportFindingsForProduct.md "../../1.0/APIReference/API_EnableImportFindingsForProduct.md") operation. If
you're using the AWS CLI, run the [enable-import-findings-for-product](../../../cli/latest/reference/securityhub/enable-import-findings-for-product.md "../../../cli/latest/reference/securityhub/enable-import-findings-for-product.md") command.
To enable Security Hub to receive findings from an integration, you need the
product ARN. To obtain the ARNs for the available integrations, use the
[DescribeProducts](../../1.0/APIReference/API_DescribeProducts.md "../../1.0/APIReference/API_DescribeProducts.md") operation. If you're using
the AWS CLI, run the [describe-products](../../../cli/latest/reference/securityhub/describe-products.md "../../../cli/latest/reference/securityhub/describe-products.md").

For example, the following AWS CLI command enables Security Hub CSPM to receive findings
from the CrowdStrike Falcon integration. This example is formatted for
Linux, macOS, or Unix, and it uses the backslash (\) line-continuation
character to improve readability.

```
`$` `aws securityhub enable-import-findings-for product --product-arn "`arn:aws:securityhub:us-east-1:123456789333:product/crowdstrike/crowdstrike-falcon`"`
```
