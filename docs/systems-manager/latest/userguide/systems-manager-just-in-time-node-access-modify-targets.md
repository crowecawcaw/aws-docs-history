

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# Modifying targets
<a name="systems-manager-just-in-time-node-access-modify-targets"></a>

When you set up just-in-time node access, you choose the *targets* where you want to set up just-in-time node access. Targets consist of AWS Organizations organizational units (OUs) and AWS Regions. By default, the same targets you chose when setting up the unified Systems Manager console are selected for just-in-time node access. You can choose to set up just-in-time node access for all of the same targets, or a subset of the targets you specified when setting up the unified Systems Manager console. Adding new targets that weren't selected when you set up the unified Systems Manager console isn't supported. You can change the targets you selected after setting up just-in-time node access.

The following procedure describes how to modify the targets for just-in-time node access.

**To modify targets**

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/).

1. Select **Settings** in the navigation pane.

1. Select the **Just-in-time node access** tab.

1. In the **Targets** section, select **Edit**.

1. Select the **Organizational units** and **Regions** where you want to use just-in-time node access.

1. Select **Save**.