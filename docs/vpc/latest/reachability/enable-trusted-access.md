

# Enable trusted access in Reachability Analyzer
<a name="enable-trusted-access"></a>

When you enable trusted access, Reachability Analyzer deploys the [AWSServiceRoleForReachabilityAnalyzer](using-service-linked-roles.md) service-linked role and the required [cross-account access roles](cross-account-access-roles.md) to all accounts in your organization.

**To enable trusted access using the console**

1. Sign in to the management account.

1. Open the Network Manager console at [https://console.aws.amazon.com/networkmanager/home](https://console.aws.amazon.com/networkmanager/home).

1. From the navigation pane, choose **Reachability Analyzer**, **Settings**.

1. For **Trusted Access**, choose **Turn on trusted access**.

1. Do not close or navigate away from this page until you see a success notification indicating that trusted access is turned on. This can take several minutes.

**To enable trusted access using the AWS CLI**  
From the management account, use the [enable-reachability-analyzer-organization-sharing](https://docs.aws.amazon.com/cli/latest/reference/ec2/enable-reachability-analyzer-organization-sharing.html) command.