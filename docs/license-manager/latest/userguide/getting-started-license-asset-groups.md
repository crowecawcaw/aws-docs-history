# Getting started with license asset groups

This section helps you get started with license asset groups in AWS License Manager. You'll learn how to set up the prerequisites, configure source regions, and create your first license asset group.

## Prerequisites

Before you begin using license asset groups, ensure you have the following prerequisites:

- AWS Systems Manager (SSM) agent installed on your EC2 instances
- Cross-account discovery configured if managing licenses across multiple accounts
- If you are onboarding for the first time, follow the [License Manager getting started guide](getting-started.md "getting-started.md") to set up all required permissions

## Set up license asset groups

### Configure source regions

License asset groups are available in all AWS commercial Regions where AWS License Manager is available. Cross-region discovery requires selecting source AWS regions during setup. This allows License Manager to discover all software across your selected regions.

###### To configure source regions using the console

1. Open the License Manager console at [https://console.aws.amazon.com/license-manager/](https://console.aws.amazon.com/license-manager/ "https://console.aws.amazon.com/license-manager/").
2. In the navigation pane, choose **Settings**, then choose **License asset discovery and ruleset**.
3. In the **License asset discovery** section, choose **Edit**.
4. Under **Region discovery**, select the regions from where you want to discover your products.
5. If you are an organization owner and want to discover across all organization accounts, choose **Enable**.
6. Choose **Save changes**.
