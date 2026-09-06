

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# Viewing OpsCenter summary reports
<a name="OpsCenter-reports"></a>

AWS Systems Manager OpsCenter includes a summary page that automatically displays the following information:
+ **OpsItem status summary** – A summary of OpsItems by status, such as `Open` and `In progress`.
+ **Sources with most open OpsItems** – A breakdown of the top AWS services that have open OpsItems.
+ **OpsItems by source and age** – A count of OpsItems, grouped by source and number of days since creation.

**To view OpsCenter summary reports**

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/).

1. In the navigation pane, choose **OpsCenter**, and then choose the **Summary** tab.

1. In the **OpsItems by source and age** section, do the following:

   1. (Optional) In the filter field, choose **Source**, select `Equal`, `Begin With`, or `Not Equal`, and then enter a search parameter.

   1. In the adjacent list, select one of the following status values:
      + `Open`
      + `In progress`
      + `Resolved`
      + `Open and in progress`
      + `All`