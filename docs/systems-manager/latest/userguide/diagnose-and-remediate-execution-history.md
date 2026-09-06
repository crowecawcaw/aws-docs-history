

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# Viewing execution progress and history for remediations in Systems Manager
<a name="diagnose-and-remediate-execution-history"></a>

You can view a list of all in-progress and completed remediation operations made using the **Diagnose and remediate** feature in Systems Manager.

Data in the execution history list reports the following types of information:
+ The type of execution, `Diagnosis` or `Remediation`.
+ The execution status, such as `Success` or `Failed`.
+ The times that the execution started and ended.

**To view execution progress and history for remediations**

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/).

1. In the navigation pane, choose **Diagnose and remediate**.

1. Choose **View executions**.
**Tip**  
When an execution is running, you can also choose **View progress** to open the **Execution history** page.

1. (Optional) In the search (![The search icon](http://docs.aws.amazon.com/systems-manager/latest/userguide/images/search-icon.png)) box, enter a phrase to help narrow down the execution list, such as **EC2** or **VPC**.

1. (Optional) To view additional details about an execution, in the **Execution name** column, choose an operation name, such as **AWS-DiagnoseUnmanagedEC2NetworkIssues**.

   In the details pane, you can review information about all the steps attempted during the operation. You can also review all the inputs and outputs for the execution.