

End of support notice: On March 31, 2027, AWS will end support for AWS Service Management Connector. After March 31, 2027, you will no longer be able to access the AWS Service Management Connector console or AWS Service Management Connector resources. For more information, see [AWS Service Management Connector end of support](https://docs.aws.amazon.com/smc/latest/ag/smc-end-of-support.html). 

# Validating AWS Systems Manager OpsCenter integration in ServiceNow
<a name="sn-opscenter-validate"></a>

This section describes how to validate AWS Systems Manager OpsCenter integration in ServiceNow.

****To view OpsItems from AWS Systems Manager - OpsCenter****

To view AWS OpsItem, you must have the role, `x_126749_aws_sc.opscenter_manager`, with the Connector scope app. 

1. Log in to your ServiceNow instance as a user (for example, System Administrator) in the fulfiller view (Standard user interface view). 

1. In the navigator, enter **AWS Service Management**. 

1. Choose **AWS Systems Manager - OpsCenter**. 

1. Choose **OpsItems** to show a list of all synced Findings. 

1. Choose an OpsItems to open the record. 

   The **Incident** and **Problem** fields show the Incident for the OpsItems, if these exist. 

1. Choose the ⓘ icon to the right of the field to preview the Incident. 

1. Choose **Open Record** on the preview form to open the Incident. 

   If the Connector configuration does not to automatically create a ServiceNow Incident when a new Finding syncs, you can create one manually. To do so, choose the link at the bottom of the form. 

****To execute an AWS Systems Manager – Automation Document from an AWS OpsItems associated to a ServiceNow Incident****

One of the following conditions must be true to view or execute automation documents (runbooks): 
+ The user has the role Account Manager or Automation Manager. 
+ The user has a linked Incident.
+ The system parameter **Assignment Group (SYS\_ID) for created incidents** is set to a valid group and a linked Incident whose Assignment group is set to that group, and the user is a member of that group. 
**Note**  
To enable this feature, you must activate AWS Systems Manager Automation in the AWS Account and opt in to the Connector.

1. Log in to your ServiceNow instance as a user (for example, System Administrator) in the fulfiller view (standard user interface view). 

1. In the navigator, enter **AWS Service Management**. Then choose **AWS Systems Manager - OpsCenter**. 

1. Choose OpsItems to show a list of all synced Findings. Then choose **Execute Automation Document**.

1. Choose your Automation Document.
**Note**  
You can configure an OpsItem with Automation Documents and mark it as *Associated*. 

1. Choose **Order Execution** next to the Automation Document you want to execute. You’ll see the ServiceNow catalog item associated with the Automation Document. 

1. Enter the necessary AWS parameters and choose **Order Now**. 

1. In OpsItems in the scoped app, choose the OpsItem in the Automation Document where you executed it. 

1. In **OpsItem Automation Executions**, review the success or failure status.

1. Follow your organization's Incident management procedures to determine related Incident resolution actions.