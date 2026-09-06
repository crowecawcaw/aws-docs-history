

# Create an IAM Access Analyzer external access analyzer
<a name="access-analyzer-create-external"></a>

To enable an external access analyzer in a Region, you must create an analyzer in that Region. You must create an external access analyzer in each Region in which you want to monitor access to your resources.

**Note**  
After you create or update an analyzer, it can take time for findings to be available.

## Create an external access analyzer with the AWS account as the zone of trust
<a name="access-analyzer-create-external-account"></a>

1. Open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

1. Under **Access analyzer**, choose **Analyzer settings**.

1. Choose **Create analyzer**.

1. In the **Analysis** section, choose **Resource analysis - External access**.

1. In the **Analyzer details** section, confirm that the Region displayed is the Region where you want to enable IAM Access Analyzer.

1. Enter a name for the analyzer.

1. Choose **Current account** as the zone of trust for the analyzer.
**Note**  
If your account is not the AWS Organizations management account or [delegated administrator](access-analyzer-delegated-administrator.md) account, you can create only one analyzer with your account as the zone of trust.

1. Optional. Add any tags that you want to apply to the analyzer.

1. Choose **Create analyzer**.

When you create an external access analyzer to enable IAM Access Analyzer, a service-linked role named `AWSServiceRoleForAccessAnalyzer` is created in your account.

## Create an external access analyzer with the organization as the zone of trust
<a name="access-analyzer-create-external-organization"></a>

1. Open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

1. Under **Access analyzer**, choose **Analyzer settings**.

1. Choose **Create analyzer**.

1. In the **Analysis** section, choose **Resource analysis - External access**.

1. In the **Analyzer details** section, confirm that the Region displayed is the Region where you want to enable IAM Access Analyzer.

1. Enter a name for the analyzer.

1. Choose **Current organization** as the zone of trust for the analyzer.

1. Optional. Add any tags that you want to apply to the analyzer.

1. Choose **Submit**.

When you create an external access analyzer with the organization as the zone of trust, a service-linked role named `AWSServiceRoleForAccessAnalyzer` is created in each account of your organization.