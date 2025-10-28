# Supported action connector types and available actions

Amazon Quick Suite supports multiple connector types, each with specific actions available:

## External service connectors

- **Salesforce** - Create records, update opportunities, search accounts, manage leads.
- **JIRA** - Create issues, update tickets, search projects, manage workflows.
- **Microsoft Outlook** - Send emails, manage calendar events, access contacts.
- **Slack** - Send messages, create channels, manage notifications.
- **ServiceNow** - Create incidents, update requests, manage workflows.
- **Zendesk** - Create tickets, update cases, search knowledge base.
- **PagerDuty** - Create incidents, manage escalations, update on-call schedules.
- **Asana** - Create actions, update projects,
  manage team workflows.
- **BambooHR** - Access employee data, manage time-off requests.
- **Smartsheet** - Update sheets, manage project data.
- **Factset** - Access financial data, generate reports.
- **Confluence** - Create, update, and manage pages, spaces, and other Confluence objects.
- **SharePoint** - Perform actions on SharePoint lists, items, and Excel files with 19 available actions for creating, updating, deleting, and retrieving SharePoint content.
- **OneDrive** - Create, update, delete, and manage OneDrive files and folders.
- **SAP** - Access SAP S/4HANA systems to perform Read only operation on enterprise data.

## AWS service connectors

- **Amazon S3** - Upload files, manage buckets, retrieve objects.
- **Amazon Bedrock** - Generate content, analyze data, process requests.
- **Amazon Textract** - Extract text and data from documents.
- **Amazon Comprehend** - Natural language processing and sentiment analysis.
- **Amazon Comprehend Medical** - Medical text analysis and entity extraction.

## Action connector compatibility matrix

The following table shows which Amazon Quick Suite features each action connector type supports:

| Action Connector Feature Compatibility | Action Connector | Chat Agents | Flows | Dashboard Visuals | Dashboard Alerts | Automations | Companions                                                                                                                                                                                                                                                                                                          |
| -------------------------------------- | ---------------- | ----------- | ----- | ----------------- | ---------------- | ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **AWS Built-in Services**              |
| AWS Bedrock Agent Runtime              | —                | —           | —     | —                 | ✓                | —           |
| AWS Bedrock Data Automation Runtime    | —                | —           | —     | —                 | ✓                | —           |
| AWS Bedrock Runtime                    | —                | —           | —     | —                 | ✓                | —           |
| Amazon Comprehend                      | —                | —           | —     | —                 | ✓                | —           |
| Amazon Comprehend Medical              | —                | —           | —     | —                 | —                | —           |
| Amazon S3                              | —                | —           | —     | —                 | ✓                | —           |
| Amazon Textract                        | —                | —           | —     | —                 | ✓                | —           |
| **External Service Connectors**        |
| Asana                                  | ✓                | ✓           | —     | —                 | —                | ✓           |
| Atlassian Confluence Cloud             | ✓                | ✓           | —     | —                 | ✓                | ✓           |
| Atlassian Jira Cloud                   | ✓                | ✓           | ✓     | ✓                 | ✓                | ✓           |
| BambooHR                               | ✓                | ✓           | —     | —                 | —                | ✓           |
| Microsoft OneDrive                     | ✓                | ✓           | —     | —                 | ✓                | ✓           |
| Microsoft Outlook                      | ✓                | ✓           | ✓     | ✓                 | ✓                | ✓           |
| Microsoft SharePoint                   | ✓                | ✓           | —     | —                 | ✓                | ✓           |
| Microsoft Teams                        | ✓                | ✓           | ✓     | ✓                 | ✓                | ✓           |
| PagerDuty                              | ✓                | ✓           | —     | —                 | ✓                | ✓           |
| Salesforce                             | ✓                | ✓           | ✓     | ✓                 | ✓                | ✓           |
| SAP                                    | ✓                | —           | —     | —                 | ✓                | ✓           |
| ServiceNow                             | ✓                | ✓           | ✓     | ✓                 | ✓                | ✓           |
| Slack                                  | ✓                | ✓           | ✓     | —                 | —                | ✓           |
| Smartsheet                             | ✓                | ✓           | —     | —                 | —                | ✓           |
| Zendesk                                | ✓                | ✓           | —     | —                 | —                | ✓           |
| **Custom Connector Types**             |
| Model Context Protocol (MCP)           | ✓                | ✓           | —     | —                 | ✓                | —           |
| OpenAPI                                | ✓                | ✓           | —     | —                 | —                | —           |
| REST API                               | —                | —           | —     | —                 | ✓                | —           | **Authentication Support:** <br>• **Chat Agents and Companions** - Support user authentication (3LO, Basic) <br>• **Dashboard Visuals** - Support user authentication (3LO) <br>• **Dashboard Alerts** - Support system authentication (2LO or API Key) <br>• **Automations** - Support system authentication (2LO) |
