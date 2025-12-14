# Validating AWS Security Hub CSPM integration in

Jira Service Management Cloud

This section describes how to validate AWS Security Hub CSPM Findings, update AWS Systems Manager OpsItems, and view
AWS related resources in Jira Service Management.

###### To view AWS Security Hub CSPM Findings in Jira Service Management from AWS Systems Manager

1. Log in to your **Jira Agent** view as an internal customer or Jira agent.
2. In the **Jira Service Management Jira Agent** view, choose the Jira project associated with the
   AWS Security Hub CSPM Finding.
3. Use [Jira filters](https://support.atlassian.com/jira-service-management-cloud/docs/save-your-search-as-a-filter/ "https://support.atlassian.com/jira-service-management-cloud/docs/save-your-search-as-a-filter/") to show only issues with the Issue Type **AWS Security Hub CSPM Finding**.

###### To update AWS Security Hub CSPM Findings in Jira Service Management

1. Log in to your **Jira Agent** view as an internal customer or Jira agent.
2. In the **Jira Service Management Jira Agent** view, choose the Jira project associated to the AWS Security Hub CSPM
   Finding.
3. Use [Jira filters](https://support.atlassian.com/jira-service-management-cloud/docs/save-your-search-as-a-filter/ "https://support.atlassian.com/jira-service-management-cloud/docs/save-your-search-as-a-filter/") to show only issues with the Issue Type **AWS Security Hub CSPM Finding**.
4. Choose **Edit Issue**.
5. Update the available fields, including **Severity**, **Priority**, and
   **Criticality**.
6. Choose **Update** to save the details.

###### Note

Updates to Security Hub CSPM Finding fields from Jira Service Management display in the AWS account view of Findings on the next sync between
AWS and Jira Service Management. Only the fields Severity, Priority, and Criticality update in the AWS account from
Jira Service Management.

###### To view AWS related resources in AWS Security Hub CSPM Findings through Jira Service Management

1. Log in to your **Jira Agent** view as an internal customer or Jira agent.
2. In the **Jira Service Management Jira Agent** view, choose the Jira project associated to the AWS Security Hub CSPM
   Finding.
3. Use [Jira filters](https://support.atlassian.com/jira-service-management-cloud/docs/save-your-search-as-a-filter/ "https://support.atlassian.com/jira-service-management-cloud/docs/save-your-search-as-a-filter/") to show only issues with the Issue Type **AWS Security Hub CSPM Finding**.
4. Choose the **Security Hub CSPM Findings** panel.
5. In the selected AWS resources section of the AWS Security Hub CSPM Finding, you can review the related resource details.
   If the resources relate and the AWS Config integration is active in the Connector, you can filter on the AWS Config-specific resource
   details and relationships. The section remains empty if AWS resources do not relate in AWS Security Hub CSPM.
   Security Hub CSPM Findings follow the [AWS Security Finding format](../../../securityhub/latest/userguide/securityhub-findings-format.md "../../../securityhub/latest/userguide/securityhub-findings-format.md") (ASFF). Review the following mapping of fields from AWS Security Hub CSPM Findings to
   Jira Service Management Incident records.

| Jira Issue field | Security Hub CSPM ASFF field |
| ---------------- | ---------------------------- |
| Created          | CreatedAt                    |
| Updated          | UpdatedAt                    |
| Summary          | Title                        |
| Priority         | Severity.Label               |
| Status           | Workflow.Status              |
