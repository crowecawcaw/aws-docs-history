

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# Register a delegated administrator for Quick Setup
<a name="quick-setup-register-delegated-administrator"></a>

Use the following procedure to register a delegated administrator for Quick Setup.

**To register a Quick Setup delegated administrator**

1. Log into your AWS Organizations management account.

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/).

1. In the navigation pane, choose **Quick Setup**.

1. Choose **Settings**.

1. In the **Delegated administrator for Quick Setup** section, verify that you have configured the required service-linked role and service access options. If necessary, choose the **Create role** and **Enable access** buttons to configure these options.

1. For **Account ID**, enter the AWS account ID. This account must be a member account in AWS Organizations.

1. Choose **Register delegated administrator**.