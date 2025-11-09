AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

# Viewing execution progress

and history for remediations in Systems Manager

You can view a list of all in-progress and completed remediation operations made using
the **Diagnose and remediate** feature in Systems Manager.

Data in the execution history list reports the following types of information:

- The type of execution, `Diagnosis` or
  `Remediation`.
- The execution status, such as `Success` or
  `Failed`.
- The times that the execution started and ended.

###### To view execution progress and history for remediations

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2. In the navigation pane, choose **Diagnose and
   remediate**.
3. Choose **View executions**.

###### Tip

When an execution is running, you can also choose **View
progress** to open the **Execution history**
page. 4. (Optional) In the search (
![The search icon](images/search-icon.png)
) box, enter a phrase to help narrow down the execution
list, such as `EC2` or `VPC`. 5. (Optional) To view additional details about an execution, in the
**Execution name** column, choose an operation name, such
as **AWS-DiagnoseUnmanagedEC2NetworkIssues**.

In the details pane, you can review information about all the steps attempted
during the operation, and about all the inputs and outputs for the
execution.
