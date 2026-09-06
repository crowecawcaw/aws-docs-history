

# Getting started with license asset groups
<a name="getting-started-license-asset-groups"></a>

This section helps you get started with license asset groups in AWS License Manager. You'll learn how to set up the prerequisites, configure source regions, and create your first license asset group.

## Prerequisites
<a name="license-asset-groups-prerequisites"></a>

Before you begin using license asset groups, ensure you have the following prerequisites:
+ AWS Systems Manager (SSM) agent installed on your EC2 instances
+ Cross-account discovery configured if managing licenses across multiple accounts
+ If you are onboarding for the first time, follow the [License Manager getting started guide](https://docs.aws.amazon.com/license-manager/latest/userguide/getting-started.html) to set up all required permissions

## Set up license asset groups
<a name="license-asset-groups-setup"></a>

### Configure source regions
<a name="configure-source-regions"></a>

License asset groups are available in all AWS commercial Regions where AWS License Manager is available. Cross-region discovery requires selecting source AWS regions during setup. This allows License Manager to discover all software across your selected regions.

**To configure source regions using the console**

1. Open the License Manager console at [https://console.aws.amazon.com/license-manager/](https://console.aws.amazon.com/license-manager/).

1. In the navigation pane, choose **Settings**, then choose **License asset discovery and ruleset**.

1. In the **License asset discovery** section, choose **Edit**.

1. Under **Region discovery**, select the regions from where you want to discover your products.

1. If you are an organization owner and want to discover across all organization accounts, choose **Enable**.

1. Choose **Save changes**.