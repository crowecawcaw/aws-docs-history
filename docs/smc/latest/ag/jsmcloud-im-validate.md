# Validating AWS Systems Manager Incident Manager

integration

This section describes how to validate AWS Systems Manager Incident Manager integration in
Jira.

###### To view Incident Manager incidents

1. Log in to your **Jira Agent** view as a Jira agent.
2. In the **Jira Service Management Jira Agent** view, choose the Jira Project associated to
   AWS Systems Manager Incident Manager.
3. Use [Jira filters](https://support.atlassian.com/jira-service-management-cloud/docs/save-your-search-as-a-filter/ "https://support.atlassian.com/jira-service-management-cloud/docs/save-your-search-as-a-filter/") to show only Issues with the Issue Type **AWS Incident**.
   The resulting list displays all synced Incidents.

###### To view Incident Manager incident details

1. Log in to your **Jira Agent** view as a Jira agent.
2. In the **Jira Service Management Jira Agent** view, choose the Jira Project associated to
   AWS Systems Manager Incident Manager.
3. Use [Jira filters](https://support.atlassian.com/jira-service-management-cloud/docs/save-your-search-as-a-filter/ "https://support.atlassian.com/jira-service-management-cloud/docs/save-your-search-as-a-filter/") to show only Issues with the Issue Type **AWS Incident**.
4. Choose **Issue ID (key)** to open the AWS Incident.
5. Review the details of the AWS Incident from the issue.
6. (Optional) Choose the AWS Incident URL to open the incident in the Incident Manager console.
   If AWS Systems Manager integration is enabled, an OpsItem is linked to the AWS Incident.

###### To resolve an Incident Manager Incident

1. Log in to your **Jira Agent** view as a Jira agent.
2. In the **Jira Service Management Jira Agent** view, choose the Jira Project associated to
   AWS Systems Manager Incident Manager.
3. Use [Jira filters](https://support.atlassian.com/jira-service-management-cloud/docs/save-your-search-as-a-filter/ "https://support.atlassian.com/jira-service-management-cloud/docs/save-your-search-as-a-filter/") to show only Issues with the Issue Type **AWS Incident**.
4. Choose **Issue ID (key)**to open the AWS Incident.
5. Choose **Resolve**.
   **Fields mapped from Incident Manager Incidents to Jira Issue records**

The following table displays the mapping between Incident Manager Incidents and Jira Issues.

| AWS Systems Manager Incident status | Jira AWS Issue Status |
| ----------------------------------- | --------------------- |
| Open                                | OPEN                  |
| Resolved                            | RESOLVED              |

Jira Service Management Connector maps **Priority - Impact** of an AWS Incident to the
priority of the corresponding Jira Issue.

| AWS Systems Manager Incident Manager Incident impact | Jira AWS Issue priority |
| ---------------------------------------------------- | ----------------------- |
| Critical                                             | Blocker                 |
| High                                                 | High                    |
| Medium                                               | Medium                  |
| Low                                                  | Low                     |
| No impact                                            | Minor                   |
