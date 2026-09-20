

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# Disabling just-in-time access with Systems Manager
<a name="systems-manager-just-in-time-node-access-disable"></a>

**Important**  
After you disable just-in-time node access, users might be unable to connect to your nodes unless you have other connection methods already set up.

**To disable just-in-time node access**

1. Depending on your setup, do one of the following:
   + For an organization setup, sign in to the Systems Manager delegated administrator account for your organization.
   + For a single-account setup, sign in to the account where you set up just-in-time node access.

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/).

1. Choose **Settings** in the navigation pane.

1. On the **Just-in-time node access** tab, choose **Disable**.