

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# Viewing patch Dashboard summaries
<a name="patch-manager-view-dashboard-summaries"></a>

The **Dashboard** tab in Patch Manager gives you a summary view in the console that you can use to monitor your patching operations in a consolidated view. Patch Manager is a tool in AWS Systems Manager. On the **Dashboard** tab, you can view the following:
+ A snapshot of how many managed nodes are compliant and noncompliant with patching rules.
+ A snapshot of the age of patch compliance results for your managed nodes.
+ A linked count of how many noncompliant managed nodes there are for each of the most common reasons for noncompliance.
+ A linked list of the most recent patching operations.
+ A linked list of the recurring patching tasks that have been set up.

**To view patch Dashboard summaries**

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/).

1. In the navigation pane, choose **Patch Manager**.

1. Choose the **Dashboard** tab.

1. Scroll to the section containing summary data that you want to view:
   + **Amazon EC2 instance management**
   + **Compliance summary**
   + **Noncompliance counts**
   + **Compliance reports**
   + **Non-patch policy-based operations**
   + **Non-patch policy-based recurring tasks**