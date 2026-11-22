

# Run an automation on Azure or Google Cloud resources (console)

The following procedure describes how to use the Systems Manager console to run an automation on Microsoft Azure or Google Cloud resources that a Cloud Connector can reach.

**To run an automation on Azure or Google Cloud resources**

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/).

1. In the navigation pane, choose **Automation**, and then choose **Execute automation**.

1. In the **Automation document** list, choose a runbook. Choose one or more options in the **Document categories** pane to filter SSM documents according to their purpose. To view a runbook that you own, choose the **Owned by me** tab. To view a runbook that is shared with your account, choose the **Shared with me** tab. To view all runbooks, choose the **All documents** tab.
**Note**  
You can view information about a runbook by choosing the runbook name.

1. In the **Document details** section, verify that **Document version** is set to the version that you want to run. The system includes the following version options: 
   + **Default version at runtime** – Choose this option if the Automation runbook is updated periodically and a new default version is assigned.
   + **Latest version at runtime** – Choose this option if the Automation runbook is updated periodically, and you want to run the version that was most recently updated.
   + **1 (Default)** – Choose this option to run the first version of the document, which is the default.

1. Choose **Next**.

1. In the **Execution Mode** section, choose **Rate control**.

1. In the **Targets** section, for **Targets**, choose **Cloud Connector**. For a runbook that doesn't target AWS, **Cloud Connector** is selected for you.

1. For **Cloud Connector**, choose the connector that reaches your Azure or Google Cloud resources. Each connector shows its cloud (**Azure** or **Google Cloud**). If you don't have a connector, choose **Create Cloud Connector** to open the **Onboard hybrid nodes** page in a new tab. When you return, the list refreshes.

1. Review **Connector details** to confirm the provider, scope, and access of the connector.

1. (Optional) Set filters to narrow the resources that the connector finds. All filters are optional.

   For an Azure connector, the following filters are available, in the order that they appear on the page:


<table>
<thead>
  <tr><th>Filter</th><th>Description</th></tr>
</thead>
<tbody>
  <tr><td><b>Subscriptions</b></td><td>The subscriptions to search. This field is hidden for a connector that lists only one subscription.</td></tr>
  <tr><td><b>Resource groups</b></td><td>The resource groups to search.</td></tr>
  <tr><td><b>Resource type</b></td><td>The resource type to find. The console hides this field when the runbook's target input takes virtual machine (VM) IDs.</td></tr>
  <tr><td><b>VM state</b></td><td>Choose <b>Running</b>, <b>Stopped</b>, or <b>Running and stopped</b>.</td></tr>
  <tr><td><b>Managed node filter</b></td><td>Choose <b>All</b>, <b>Managed</b>, or <b>Unmanaged</b>.</td></tr>
  <tr><td><b>Azure regions</b></td><td>The Azure regions to search.</td></tr>
  <tr><td><b>Tag</b></td><td>Enter a key and an optional value, and then choose <b>Add</b>.</td></tr>
</tbody>
</table>


   For a Google Cloud connector, the following filters are available, in the order that they appear on the page:


<table>
<thead>
  <tr><th>Filter</th><th>Description</th></tr>
</thead>
<tbody>
  <tr><td><b>Projects</b></td><td>The projects to search. This field is hidden for a connector that covers a whole organization or lists only one project.</td></tr>
  <tr><td><b>Asset type</b></td><td>The asset type to find.</td></tr>
  <tr><td><b>VM state</b></td><td>Choose <b>Running</b>, <b>Stopped</b>, or <b>Running and stopped</b>.</td></tr>
  <tr><td><b>Managed node filter</b></td><td>Choose <b>All</b>, <b>Managed</b>, or <b>Unmanaged</b>.</td></tr>
  <tr><td><b>Zones</b></td><td>The zones to search.</td></tr>
  <tr><td><b>Labels to include</b></td><td>The labels that a resource must have.</td></tr>
  <tr><td><b>Labels to exclude</b></td><td>The label keys that cause a resource to be skipped.</td></tr>
  <tr><td><b>OS policy compliance</b></td><td>Choose <b>All VMs</b> or <b>Skip VMs that are already compliant</b>. If you choose to skip compliant VMs, enter a <b>Policy orchestrator ID</b>.</td></tr>
</tbody>
</table>


1. For **Parameter**, choose the runbook input that receives the ID of each resource that the Cloud Connector target finds. The console picks the input when only one fits.

1. In the **Input parameters** section, for the assume-role input (for example, `AutomationAssumeRole`), use the connector's automation assume role. Automation uses this role to get Azure or Google Cloud credentials through the connector. The role's name starts with `SSM-AzureAssumeRole-` or `SSM-GCPAssumeRole-` and ends with the first 8 characters of the connector ID.
   + When your AWS account has exactly one such role for the connector, the console fills it in. If you choose a different role, the console keeps your choice.
   + If the console doesn't fill in the role, choose it yourself. The console doesn't fill it in when it finds no matching role or more than one, or when you don't have permission to list IAM roles (`iam:ListRoles`). The list shows only roles that Systems Manager can assume. If the input's type is `AWS::IAM::Role::Arn`, you can also choose **Enter the ARN of an existing IAM Role**.
   + If your account doesn't have the role, create it. Systems Manager creates the role only when you enable node management for the connector and keep the default **Automation execution role**. For how to create the role, see [Create the automation assume role](automation-cloud-connector-permissions.md#automation-cloud-connector-permissions-create-role).
   + You can also choose another role that the connector's federation role trusts, such as a role that you chose under **Additional trusted roles** when you created the connector. For more information, see [Use another role](automation-cloud-connector-permissions.md#automation-cloud-connector-permissions-other-role).

1. An input named `CloudConnector` is read-only and is set from the Cloud Connector in **Targets**. Enter the other inputs that the runbook requires.

1. Use the options in the **Rate control** section to restrict the number of AWS resources that can run the Automation within each account-Region pair. 

   In the **Concurrency** section, choose an option: 
   + Choose **targets** to enter an absolute number of targets that can run the Automation workflow simultaneously.
   + Choose **percentage** to enter a percentage of the target set that can run the Automation workflow simultaneously.

1. In the **Error threshold** section, choose an option:
   + Choose **errors** to enter an absolute number of errors allowed before Automation stops sending the workflow to other resources.
   + Choose **percentage** to enter a percentage of errors allowed before Automation stops sending the workflow to other resources.

1. (Optional) Choose a CloudWatch alarm to apply to your automation for monitoring. If your alarm enters `ALARM` state, the automation is canceled and any defined `onCancel` steps run. If you use AWS CloudTrail, you see the `StopAutomationExecution` API call in your trail.

1. Choose **Execute**.

## View the results
<a name="running-automations-cloud-connector-console-results"></a>

To view the child automations that your automation started, in the navigation pane, choose **Automation**, and then choose **Show child automations**.

On the execution details page of the parent automation, the **Targets** section shows the connector and the filters that you used.

After an automation completes, you can rerun it with the same or modified parameters. Choose **Copy to new** to carry the whole Cloud Connector target into a new execution. For more information, see [Rerunning automation executions](automation-rerun-executions.md).

## Simple execution and Manual execution with a connector input
<a name="running-automations-cloud-connector-console-connector-input"></a>

For a runbook that takes a Cloud Connector ID as an input, you can choose **Simple execution** or **Manual execution** and run the runbook on the resources whose IDs you enter.
+ The connector input is a list. Choose or enter a Cloud Connector ID. The same **Connector details** appear as in the Rate control procedure.
+ For an Azure VM input, enter the ID in the format `/subscriptions/{subscription-id}/resourceGroups/{resource-group}/providers/Microsoft.Compute/virtualMachines/{vm-name}`.
+ (Optional, Azure connectors only) Use Azure sign-in to pick resources from a list instead of typing their IDs. For more information, see [Choosing Azure resources with Azure sign-in](automation-azure-sign-in.md).

## Rate control with Parameter Values
<a name="running-automations-cloud-connector-console-parameter-values"></a>

To run the runbook on VMs that you choose, in the **Targets** section choose **Parameter Values**, and then enter up to 50 VM IDs.