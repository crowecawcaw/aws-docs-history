# Supported connector types and available actions

Amazon Quick supports multiple connector types, each with specific actions available:

## External service connectors

- **Adobe Marketing Agent** - Work with
  Adobe Experience Platform marketing data and AI-powered marketing
  capabilities.
- **Airtable** - Create and update records, manage bases and tables, filter views, and perform relational data operations.
- **Asana** - Manage tasks, workspace operations, and project handling.
- **Atlassian Confluence Cloud** - Create, update, and manage pages, spaces, and other Confluence objects.
- **Atlassian Jira Cloud** - Create issues, update tickets, search projects, manage workflows.
- **BambooHR** - Access employee data, manage time-off requests.
- **Box** - Manage files, folders, and collaborate on documents.
- **Canva** - Create and edit designs, manage templates and assets.
- **Cisco Webex Meetings** - Schedule
  meetings, retrieve recordings, and manage participants.
- **Cisco Webex Video Messaging** -
  Manage video updates, retrieve transcripts, and access video metadata
  in Cisco Webex (Vidcast).
- **Dropbox** - Upload files, manage folder structures, generate sharing links, and control access permissions.
- **Dun & Bradstreet** - Look up
  company profiles, credit risk data, and business intelligence.
- **GitHub** - Manage repositories, issues, pull requests, and code collaboration.
- **Gmail** - Read emails, search inbox, draft messages, manage labels, and organize threads.
- **Google Analytics** - Query traffic reports, retrieve audience data, monitor conversion events, and access performance metrics.
- **Google Calendar** - Create and update events, check availability, manage invites, and retrieve schedules.
- **Google Chat** - Send messages,
  manage spaces, and interact with chat threads.
- **Google Docs** - Create and edit documents, read content, and collaborate on text-based files.
- **Google Drive** - Upload files, manage folders, search content, and perform file operations.
- **Google Meet** - Schedule video meetings, list hosted meetings, retrieve transcripts, and update access settings.
- **Google Sheets** - Create and edit spreadsheets, read and write cell ranges, and perform data operations.
- **Google Slides** - Create presentations, edit slides, manage layouts, and add speaker notes.
- **HG Insights** - Access
  technographic data, query company technology profiles, and retrieve
  market intelligence.
- **HubSpot** - Manage contacts, deals, marketing campaigns, and CRM data.
- **HuggingFace** - Access AI models, datasets, and machine learning workflows.
- **Intercom** - Manage customer conversations, support tickets, and messaging.
- **Linear** - Create and manage issues, projects, and development workflows.
- **Microsoft OneDrive** - Create, update, delete, and manage OneDrive files and folders.
- **Microsoft OneNote** - Create and
  edit notebooks, manage sections, and organize notes.
- **Microsoft Outlook** - Send emails, manage calendar events, access contacts.
- **Microsoft SharePoint** - Perform actions on SharePoint lists, items, files, and Excel workbooks.
- **Microsoft Teams** - Send messages, manage channels, schedule meetings, and manage team collaboration.
- **Monday.com** - Manage projects, tasks, and team collaboration workflows.
- **Moodys GenAI Ready Data** - Access
  Moody's credit ratings, financial research, and risk analytics
  data.
- **New Relic** - Access observability data, query metrics, and manage monitoring workflows.
- **Notion** - Create and manage pages, databases, and collaborative workspaces.
- **PagerDuty** - Create incidents, manage escalations, update on-call schedules.
- **QuickBooks** - Manage invoices, track expenses, generate financial reports, and handle vendor records.
- **Salesforce** - Create records, update opportunities, search accounts, manage leads.
- **SAP** - Access SAP S/4HANA systems to perform read operations on enterprise data.
- **ServiceNow** - Create incidents, update requests, manage workflows.
- **Shopify** - Manage products,
  orders, customers, and store operations.
- **Slack** - Send messages, create channels, manage notifications.
- **Smartsheet** - Update sheets, manage project data.
- **Snowflake Cortex Agent** - Query
  Snowflake data and run AI-powered analytics through Cortex
  Agent.
- **Visier Agent** - Access workforce analytics, query people data, and generate HR insights.
- **WhatsApp** - Send and manage
  messages through WhatsApp Business.
- **Zapier** - Trigger workflows
  across thousands of connected applications.
- **Zendesk** - Create tickets, update cases, search knowledge base.
- **Zoom** - Schedule meetings, add webinar registrants, summarize recorded meetings, and list participants.
- **ZoomInfo** - Look up company and
  contact data, and query firmographic and intent data.

## AWS service connectors

- **Amazon S3** - Upload files, manage buckets, retrieve objects.
- **Amazon Bedrock** - Generate content, analyze data, process requests.
- **Amazon Textract** - Extract text and data from documents.
- **Amazon Comprehend** - Natural language processing and sentiment analysis.
- **Amazon Comprehend Medical** - Medical text analysis and entity extraction.

## Connector compatibility matrix

The following table shows which Amazon Quick features each connector type supports:

Connector feature compatibility| Connector | Chat Agents | Flows | Dashboard Visuals | Dashboard Alerts | Automations | Companions |
| --- | --- | --- | --- | --- | --- | --- |
| **AWS Built-in Services** |
| AWS Bedrock Agent Runtime | — | — | — | — | ✓ | — |
| AWS Bedrock Data Automation Runtime | — | — | — | — | ✓ | — |
| AWS Bedrock Runtime | — | — | — | — | ✓ | — |
| Amazon Comprehend | — | — | — | — | ✓ | — |
| Amazon Comprehend Medical | — | — | — | — | — | — |
| Amazon S3 | — | — | — | — | ✓ | — |
| Amazon Textract | — | — | — | — | ✓ | — |
| **External Service Connectors** |
| Adobe Marketing Agent | ✓ | ✓ | — | — | — | — |
| Airtable | ✓ | ✓ | ✓ | — | — | — |
| Asana | ✓ | ✓ | — | — | — | ✓ |
| Atlassian Confluence Cloud | ✓ | ✓ | — | — | ✓ | ✓ |
| Atlassian Jira Cloud | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| BambooHR | ✓ | ✓ | — | — | — | ✓ |
| Box | ✓ | ✓ | — | — | — | — |
| Canva | ✓ | ✓ | — | — | — | — |
| Cisco Webex Meetings | ✓ | ✓ | — | — | — | — |
| Cisco Webex Video Messaging | ✓ | ✓ | — | — | — | — |
| Dropbox | ✓ | ✓ | ✓ | — | — | — |
| Dun & Bradstreet | ✓ | ✓ | — | — | — | — |
| GitHub | ✓ | ✓ | — | — | — | — |
| Gmail | ✓ | ✓ | ✓ | — | — | — |
| Google Analytics | ✓ | ✓ | ✓ | — | — | — |
| Google Calendar | ✓ | ✓ | ✓ | — | — | — |
| Google Chat | ✓ | ✓ | — | — | — | — |
| Google Docs | ✓ | ✓ | ✓ | — | — | — |
| Google Drive | ✓ | ✓ | ✓ | — | — | — |
| Google Meet | ✓ | ✓ | ✓ | — | — | — |
| Google Sheets | ✓ | ✓ | ✓ | — | — | — |
| Google Slides | ✓ | ✓ | ✓ | — | — | — |
| HG Insights | ✓ | ✓ | — | — | — | — |
| HubSpot | ✓ | ✓ | — | — | — | — |
| HuggingFace | ✓ | ✓ | — | — | — | — |
| Intercom | ✓ | ✓ | — | — | — | — |
| Linear | ✓ | ✓ | — | — | — | — |
| Microsoft OneDrive | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Microsoft OneNote | ✓ | ✓ | — | — | — | — |
| Microsoft Outlook | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Microsoft SharePoint | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Microsoft Teams | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Monday.com | ✓ | ✓ | — | — | — | — |
| Moodys GenAI Ready Data | ✓ | ✓ | — | — | — | — |
| New Relic | ✓ | ✓ | — | — | — | — |
| Notion | ✓ | ✓ | — | — | — | — |
| PagerDuty | ✓ | ✓ | — | — | ✓ | ✓ |
| QuickBooks | ✓ | ✓ | ✓ | — | — | — |
| Salesforce | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| SAP | ✓ | — | — | — | ✓ | ✓ |
| ServiceNow | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Shopify | ✓ | ✓ | — | — | — | — |
| Slack | ✓ | ✓ | ✓ | — | — | ✓ |
| Smartsheet | ✓ | ✓ | — | — | — | ✓ |
| Snowflake Cortex Agent | ✓ | ✓ | — | — | — | — |
| Visier Agent | ✓ | ✓ | — | — | — | — |
| WhatsApp | ✓ | ✓ | — | — | — | — |
| Zapier | ✓ | ✓ | — | — | — | — |
| Zendesk | ✓ | ✓ | — | — | — | ✓ |
| Zoom | ✓ | ✓ | ✓ | — | — | — |
| ZoomInfo | ✓ | ✓ | — | — | — | — |
| **Custom Connector Types** |
| Model Context Protocol (MCP) | ✓ | ✓ | — | — | ✓ | — |
| OpenAPI | ✓ | ✓ | — | — | — | — |
| REST API | — | — | — | — | ✓ | — |

**Authentication Support:**

- **Chat Agents and Companions** - Support user authentication (Default OAuth app, Custom OAuth app, Basic)
- **Dashboard Visuals** - Support user authentication (Default OAuth app, Custom OAuth app)
- **Dashboard Alerts** - Support system authentication (Service-to-Service OAuth or API Key)
- **Automations** - Support system authentication (Service-to-Service OAuth)
