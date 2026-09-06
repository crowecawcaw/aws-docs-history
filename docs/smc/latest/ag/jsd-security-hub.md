

End of support notice: On March 31, 2027, AWS will end support for AWS Service Management Connector. After March 31, 2027, you will no longer be able to access the AWS Service Management Connector console or AWS Service Management Connector resources. For more information, see [AWS Service Management Connector end of support](https://docs.aws.amazon.com/smc/latest/ag/smc-end-of-support.html). 

# Validating AWS Security Hub CSPM integration
<a name="jsd-security-hub"></a>

This section describes how to view AWS Security Hub CSPM Findings, update AWS Systems Manager OpsItems, and view AWS related resources in AWS Systems Manager OpsItems in Jira Service Management.

**To view AWS Security Hub CSPM Findings in Jira Service Management from AWS Systems Manager**

1. Log in to your **Jira Agent **view as an end user.

1. In the **Jira Service Management Jira Agent** view, choose the Jira project associated to the AWS Security Hub CSPM Finding.

1. Choose **Open Issues** and select the **AWS Security Hub CSPM Finding** from AWS that you want to view.

**To update AWS Security Hub CSPM Finding in Jira Service Management**

1. Log in to your **Jira Agent** view as an end user.

1. In the **Jira Service Management Jira Agent** view, choose the Jira project associated to AWS Security Hub CSPM Finding.

1. Choose **Open Issues** and select the AWS Security Hub CSPM Finding from AWS that you want to update.

1. Choose **Edit Issue**.

1. Update the fields available, such as **Severity**, **Priority**, and **Criticality**.

1. Choose **Update** to save the details.

**Note**  
Updates to Security Hub Finding fields from Jira Service Management displays in the AWS account view of Findings on the next sync between AWS and Jira Service Management. Only the fields Severity, Priority, and Criticality update in the AWS account from Jira Service Management.

**To view AWS related resources in AWS Security Hub CSPM Findings through Jira Service Management**

1. Log in to your **Jira Agent** view as an end user.

1. In the **Jira Service Management Jira Agent** view, choose the Jira project associated to AWS Security Hub CSPM Finding.

1. Choose **Open Issues** and select the AWS Security Hub CSPM Finding.

1. In the selected AWS resources section of the AWS Security Hub CSPM Finding, you see the related resource details. If the resources relate and the AWS Config integration is active in the Connector, you can drill down on the Config resource details and relationships. The section remains empty if AWS resources do not relate in AWS Security Hub CSPM.

   AWS Security Hub CSPM findings follow the [AWS Security Finding Format](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-findings-format.html) (ASFF). Here’s a mapping of fields from AWS Security Hub CSPM findings to JSM Incident records.


| JIRA issue field | Security Hub ASFF field | 
| --- | --- | 
| Created | CreatedAt | 
| Updated | UpdatedAt | 
| Summary | Title | 
| Priority | Severity.Label | 
| Status | Workflow.Status | 

**Note**  
Jira does not duplicate findings. If a Security Hub CSPM finding is sent to Jira with the same finding ID as one previously sent to Jira, Jira updates the ticket with the most recent information in the finding.