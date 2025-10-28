# Validating AWS Systems Manager Incident Manager

integration

This section describes how to validate AWS Systems Manager Incident Manager integration
in Jira.

###### To view Incident Manager incidents

1. Log in to your **Jira Agent** view
   as an end user.
2. In the **Jira Service Management Jira Agent** view, choose the Jira project associated to
   AWS Systems Manager Incident Manager
3. Use [Jira filters](https://confluence.atlassian.com/servicemanagementserver/saving-your-search-as-a-filter-939937027.html "https://confluence.atlassian.com/servicemanagementserver/saving-your-search-as-a-filter-939937027.html") to show only issues with the Issue Type
   **AWS Incident**
   The resulting list displays all synced Incidents.

###### To view Incident Manager incident details

1. Log in to your **Jira Agent view**
   as an end user.
2. In the **Jira Service Management Jira Agent
   view**, choose the Jira project associated to
   AWS Systems Manager Incident Manager.
3. Use [Jira filters](https://confluence.atlassian.com/servicemanagementserver/saving-your-search-as-a-filter-939937027.html "https://confluence.atlassian.com/servicemanagementserver/saving-your-search-as-a-filter-939937027.html") to show only issues with the Issue Type
   **AWS Incident**.
4. Choose **Issue Id (Key)** to open
   the AWS Incident.
5. Review the details of the AWS Incident from the issue.
6. (Optional) Chose the AWS Incident URL to open the incident in
   the AWS Incident Manager console.
   If AWS Systems Manager integration is enabled, an OpsItem is linked to the
   AWS Incident.

###### To resolve an Incident Manager incident

1. Log in to your **Jira Agent view**
   as an end user.
2. In the **Jira Service Management Jira Agent
   view**, choose the Jira project associated to
   AWS Systems Manager Incident Manager.
3. Use [Jira filters](https://confluence.atlassian.com/servicemanagementserver/saving-your-search-as-a-filter-939937027.html "https://confluence.atlassian.com/servicemanagementserver/saving-your-search-as-a-filter-939937027.html") to show only issues with the Issue Type
   **AWS Incident**.
4. Choose **Issue Id (Key)** to open
   the AWS Incident you want to resolve.
5. Choose **Resolve**.
   **Fields mapped from Incident Manager incidents
   to Jira issue records**

This table shows how AWS Incident Manager Incidents map to a Jira
issue.

| AWS Incident Management Incident        | Jira AWS Incident          |
| --------------------------------------- | -------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| TITLE                                   | Summary                    |
| SUMMARY                                 | Description                |
| INCIDENT ARN                            | AWS Incident ARN           |
| AWS ACCOUNT                             | AWS Account ID             |
| AWS REGION                              | AWS Region                 |
| STATUS                                  | AWS Incident Status        |
| START TIME                              | AWS Creation Time          |
| RESOLVED TIME                           | AWS Resolved Time          |
| UPDATED TIME                            | AWS Last Updated Time      |
| AWS INCIDENT URL                        | AWS Incident URL           |
| IMPACT                                  | Priority                   | Incident Status is an integer in Jira Service Management. Jira Service Management Connector maps Incident Manager incident status values to Jira status values. |
| AWS Incident Management Incident Status | Jira AWS Incident Status   |
| ---                                     | ---                        |
| Open                                    | OPEN                       |
| Resolved                                | RESOLVED                   | Jira Service Management Connector maps **Priority - Imact** of an AWS Incident to the priority of the corresponding JIRA issue.                                 |
| AWS Incident Management Incident Impact | Jira AWS Incident Priority |
| ---                                     | ---                        |
| Critical                                | Blocker                    |
| High                                    | High                       |
| Medium                                  | Medium                     |
| Low                                     | Low                        |
| No Impact                               | Minor                      |
