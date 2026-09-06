

End of support notice: On March 31, 2027, AWS will end support for AWS Service Management Connector. After March 31, 2027, you will no longer be able to access the AWS Service Management Connector console or AWS Service Management Connector resources. For more information, see [AWS Service Management Connector end of support](https://docs.aws.amazon.com/smc/latest/ag/smc-end-of-support.html). 

# Validating AWS Security Hub CSPM integration in Jira Service Management Cloud
<a name="jsmcloud-security-hub-validate"></a>

This section describes how to validate AWS Security Hub CSPM Findings, update AWS Systems Manager OpsItems, and view AWS related resources in Jira Service Management.

**To view AWS Security Hub CSPM Findings in Jira Service Management from AWS Systems Manager**

1. Log in to your **Jira Agent** view as an internal customer or Jira agent.

1. In the **Jira Service Management Jira Agent** view, choose the Jira project associated with the AWS Security Hub CSPM Finding.

1. Use [Jira filters](https://support.atlassian.com/jira-service-management-cloud/docs/save-your-search-as-a-filter/) to show only issues with the Issue Type **AWS Security Hub CSPM Finding**. 

**To update AWS Security Hub CSPM Findings in Jira Service Management**

1. Log in to your **Jira Agent** view as an internal customer or Jira agent. 

1. In the **Jira Service Management Jira Agent** view, choose the Jira project associated to the AWS Security Hub CSPM Finding. 

1. Use [Jira filters](https://support.atlassian.com/jira-service-management-cloud/docs/save-your-search-as-a-filter/) to show only issues with the Issue Type **AWS Security Hub CSPM Finding**. 

1. Choose **Edit Issue**. 

1. Update the available fields, including **Severity**, **Priority**, and **Criticality**. 

1. Choose **Update** to save the details. 

**Note**  
Updates to Security Hub CSPM Finding fields from Jira Service Management display in the AWS account view of Findings on the next sync between AWS and Jira Service Management. Only the fields Severity, Priority, and Criticality update in the AWS account from Jira Service Management. 

**To view AWS related resources in AWS Security Hub CSPM Findings through Jira Service Management**

1. Log in to your **Jira Agent** view as an internal customer or Jira agent. 

1. In the **Jira Service Management Jira Agent** view, choose the Jira project associated to the AWS Security Hub CSPM Finding. 

1. Use [Jira filters](https://support.atlassian.com/jira-service-management-cloud/docs/save-your-search-as-a-filter/) to show only issues with the Issue Type **AWS Security Hub CSPM Finding**. 

1. Choose the **Security Hub CSPM Findings** panel. 

1. In the selected AWS resources section of the AWS Security Hub CSPM Finding, you can review the related resource details. If the resources relate and the AWS Config integration is active in the Connector, you can filter on the AWS Config-specific resource details and relationships. The section remains empty if AWS resources do not relate in AWS Security Hub CSPM. Security Hub CSPM Findings follow the [AWS Security Finding format](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-findings-format.html) (ASFF). Review the following mapping of fields from AWS Security Hub CSPM Findings to Jira Service Management Incident records. 


| Jira Issue field | Security Hub CSPM ASFF field | 
| --- | --- | 
| Created | CreatedAt | 
| Updated | UpdatedAt | 
| Summary | Title | 
| Priority | Severity.Label | 
| Status | Workflow.Status | 