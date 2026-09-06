

End of support notice: On March 31, 2027, AWS will end support for AWS Service Management Connector. After March 31, 2027, you will no longer be able to access the AWS Service Management Connector console or AWS Service Management Connector resources. For more information, see [AWS Service Management Connector end of support](https://docs.aws.amazon.com/smc/latest/ag/smc-end-of-support.html). 

# Validating AWS Systems Manager OpsCenter integration
<a name="opscenter"></a>

To validate AWS Systems Manager OpsCenter integration, view or create OpsItems.

**To view OpsItems in Jira Service Management from AWS Systems Manager**

1. Log in to your **Jira Agent** view as an end user.

1. In the **Jira Service Management Jira Agent** view, choose the Jira project associated to OpsCenter 

1. Choose **Open Issues** and select the **OpsItem **from AWS that you want to view.

**To create AWS Systems Manager OpsItems in Jira Service Management**

1. Log in to your **Jira Agent** view as an end user.

1. In the **Jira Service Management Jira Agent** view, choose **Create**. 

1. In the **Create Issue** field input the following details:
   + **Project**: Auto-populated.
   + **Issue Type**: Choose **AWS OpsItem **if you have multiple issue types.
   + **Summary**: Input Summary Details.
   + **Description**: Input Description.
   + **Priority**: Choose the appropriate Priority (default value is Low).
   + **Severity**: Choose the appropriate Severity (required for AWS OpsItem).
   + **Category**: Choose the appropriate Category (required for AWS OpsItem).
   + **Region**: Choose the appropriate AWS Region (required for AWS OpsItem).

1. Choose **Create**.
**Note**  
The newly created OpsItem from Jira Service Management displays in the AWS account view of OpsItem on the next sync between AWS and Jira Service Management.

**To update AWS Systems Manager OpsItems in Jira Service Management**

1. Log in to your** Jira Agent** view as an end user.

1. In the **Jira Service Management Jira Agent** view, choose the Jira project associated to OpsCenter.

1. Choose **Open Issues** and select the **OpsItem** from AWS that you want to update.

1. Choose **Edit Issue**.

1. Update fields available such as Summary, Description, Priority, Severity, Category. The **Resolved **button in the OpsItem issue is also available to select upon resolution.
**Note**  
Updates to OpsItem fields from Jira Service Management displays in the AWS account view of OpsItem on the next sync between AWS and Jira Service Management.

**To view AWS related resources in AWS Systems Manager OpsItems through Jira Service Management**

1. Log in to your **Jira Agent** view as an end user.

1. In the **Jira Service Management Jira Agent** view, choose the Jira project associated to OpsCenter.

1. Choose **Open Issues** and select the **OpsItem** from the OpsItem from AWS. 

1. Choose the AWS related resource section of the OpsItem selected. This section displays the related resource details.

**To execute runbooks on AWS Systems Manager OpsItems through Jira Service Management**

1. Log in to your **Jira Agent** view as an end user.

1. In the **Jira Service Management Jira Agent** view, choose the Jira project associated to OpsCenter.

1. Choose **Open Issues** and select the **OpsItem**.

1. Choose the OpsItem section of AWS Runbooks. The OpsItem that contains the associated runbooks display a list of automation documents available. (See them next to the star shaped symbol.)
   + Choose **Execute** on the desired runbook. An **Execute Runbook from OpsItem** screen displays.
   + Enter the workflow parameter details associated to the runbook. The runbook will not execute successfully without the correct parameter inputs.
   + Enter metadata tags details if applicable.
   + **Select Create**. An **Execute AWS Systems Manager Automation Request** issue generates and provides the execution status.

   OpsItems without associated runbooks are still able to run automated documents.

**To run automated documents not associated with runbooks**

1. In the OpsItem, choose **Show All Runbooks**. A list on AWS Runbooks display.

1. To narrow the list of runbooks available, enter details into the search bar above the first listed runbook.

1. Choose **Execute** on the desired runbook. An **Execute Runbook from OpsItem** screen displays.

1. Enter the workflow parameter details associated to the runbook. The runbook will not execute successfully without the correct parameter inputs. 

1. Enter metadata tags details if applicable.

1. Choose **Create**. An **Execute AWS Systems Manager Automation Request** issue displays and provides the execution status.