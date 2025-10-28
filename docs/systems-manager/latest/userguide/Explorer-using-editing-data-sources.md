# Editing Systems Manager Explorer data

sources

For AWS Regions that are available [by default](../../../global-infrastructure/latest/regions/aws-regions.md "../../../global-infrastructure/latest/regions/aws-regions.md"),
AWS Systems Manager Explorer displays data from the following sources. You can edit Explorer settings
to add or remove data sources:

- Amazon Elastic Compute Cloud (Amazon EC2)
- AWS Systems Manager Inventory
- AWS Systems Manager OpsCenter OpsItems
- AWS Systems Manager Patch Manager patch compliance
- AWS Systems Manager State Manager association compliance
- AWS Trusted Advisor
- AWS Compute Optimizer
- AWS Support Center cases
- AWS Config rule and resource compliance
- AWS Security Hub findings

###### Note

For the Asia Pacific (Osaka) Region, Explorer doesn't display data from
AWS Compute Optimizer and AWS Security Hub findings.

For the [AWS opt-in Regions](../../../global-infrastructure/latest/regions/aws-regions.md#regions-opt-in-status "../../../global-infrastructure/latest/regions/aws-regions.md#regions-opt-in-status"), Explorer displays data from the following
sources:

- Amazon Elastic Compute Cloud (Amazon EC2)
- AWS Systems Manager Inventory
- AWS Systems Manager OpsCenter OpsItems
- AWS Systems Manager Patch Manager patch compliance
- AWS Systems Manager State Manager association compliance
- AWS Trusted Advisor
- AWS Support Center cases
- AWS Config rule and resource compliance

###### Note

- To view Support Center cases in Explorer, you must have either an
  Enterprise or Business account set up with Support.
- You can't configure Explorer to stop displaying OpsCenter OpsItem
  data.

###### Before you begin

Verify that you set up and configured services that populate Explorer widgets
with data. For more information, see [Setting up related services for
Explorer](Explorer-setup-related-services.md "Explorer-setup-related-services.md").

###### To edit data sources

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2. In the navigation pane, choose **Explorer**.
3. Choose **Settings**, and then choose the
   **Configure Dashboard** tab.
4. In the **OpsData sources** section, in the
   **Status** column, turn on or turn off sources
   according to the data you want to view.
