

# Reviewing a list of Security Hub CSPM integrations
<a name="securityhub-integrations-view-filter"></a>

Choose your preferred method, and follow the steps to review a list of integrations in AWS Security Hub CSPM or details about a specific integration.

------
#### [ Security Hub CSPM console ]

**To review integration options and details (console)**

1. Open the AWS Security Hub CSPM console at [https://console.aws.amazon.com/securityhub/](https://console.aws.amazon.com/securityhub/).

1. In the Security Hub CSPM navigation pane, choose **Integrations**.

On the **Integrations** page, integrations with other AWS services are listed first, followed by integrations with third-party products.

For each integration, the **Integrations** page provides the following information:
+ The name of the company
+ The name of the product
+ A description of the integration
+ The categories that the integration applies to
+ How to enable the integration
+ The current status of the integration

You can filter the list by entering text from the following fields:
+ Company name
+ Product name
+ Integration description
+ Categories

------
#### [ Security Hub CSPM API ]

**To review integration options and details (API)**

To get a list of integrations, use the [DescribeProducts](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_DescribeProducts.html) operation. If you're using the AWS CLI, run the [describe-products](https://docs.aws.amazon.com/cli/latest/reference/securityhub/describe-products.html) command.

To retrieve details for a specific product integration, use the `ProductArn` parameter to specify the Amazon Resource Name (ARN) of the integration.

For example, the following AWS CLI command retrieves details about the Security Hub CSPM integration with 3CORESec.

```
$ aws securityhub describe-products --product-arn "{{arn:aws:securityhub:us-east-1::product/3coresec/3coresec}}"
```

------