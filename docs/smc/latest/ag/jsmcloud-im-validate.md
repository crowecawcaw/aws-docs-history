

End of support notice: On March 31, 2027, AWS will end support for AWS Service Management Connector. After March 31, 2027, you will no longer be able to access the AWS Service Management Connector console or AWS Service Management Connector resources. For more information, see [AWS Service Management Connector end of support](https://docs.aws.amazon.com/smc/latest/ag/smc-end-of-support.html). 

# Validating AWS Systems Manager Incident Manager integration
<a name="jsmcloud-im-validate"></a>

This section describes how to validate AWS Systems Manager Incident Manager integration in Jira.

**To view Incident Manager incidents**

1. Log in to your **Jira Agent** view as a Jira agent. 

1. In the **Jira Service Management Jira Agent** view, choose the Jira Project associated to AWS Systems Manager Incident Manager. 

1. Use [Jira filters](https://support.atlassian.com/jira-service-management-cloud/docs/save-your-search-as-a-filter/) to show only Issues with the Issue Type **AWS Incident**. 

The resulting list displays all synced Incidents. 

**To view Incident Manager incident details**

1. Log in to your **Jira Agent** view as a Jira agent. 

1. In the **Jira Service Management Jira Agent** view, choose the Jira Project associated to AWS Systems Manager Incident Manager. 

1. Use [Jira filters](https://support.atlassian.com/jira-service-management-cloud/docs/save-your-search-as-a-filter/) to show only Issues with the Issue Type **AWS Incident**. 

1. Choose **Issue ID (key)** to open the AWS Incident. 

1. Review the details of the AWS Incident from the issue.

1. (Optional) Choose the AWS Incident URL to open the incident in the Incident Manager console. 

If AWS Systems Manager integration is enabled, an OpsItem is linked to the AWS Incident. 

**To resolve an Incident Manager Incident**

1. Log in to your **Jira Agent** view as a Jira agent. 

1. In the **Jira Service Management Jira Agent** view, choose the Jira Project associated to AWS Systems Manager Incident Manager. 

1. Use [Jira filters](https://support.atlassian.com/jira-service-management-cloud/docs/save-your-search-as-a-filter/) to show only Issues with the Issue Type **AWS Incident**. 

1. Choose **Issue ID (key)**to open the AWS Incident. 

1. Choose **Resolve**. 

**Fields mapped from Incident Manager Incidents to Jira Issue records**

The following table displays the mapping between Incident Manager Incidents and Jira Issues. 


| AWS Systems Manager Incident status | Jira AWS Issue Status | 
| --- | --- | 
| Open | OPEN | 
| Resolved | RESOLVED | 

Jira Service Management Connector maps **Priority - Impact** of an AWS Incident to the priority of the corresponding Jira Issue. 


| AWS Systems Manager Incident Manager Incident impact | Jira AWS Issue priority | 
| --- | --- | 
| Critical | Blocker | 
| High | High | 
| Medium | Medium | 
| Low | Low | 
| No impact | Minor | 