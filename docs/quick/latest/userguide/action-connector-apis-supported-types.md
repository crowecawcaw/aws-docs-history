

# Supported connector types and available actions
<a name="action-connector-apis-supported-types"></a>

Amazon Quick supports multiple connector types, each with specific actions available:

## External service connectors
<a name="action-connector-apis-external-services"></a>
+ **Adobe Marketing Agent** - Work with Adobe Experience Platform marketing data and AI-powered marketing capabilities.
+ **Airtable** - Create and update records, manage bases and tables, filter views, and perform relational data operations.
+ **Asana** - Manage tasks, workspace operations, and project handling.
+ **Atlassian Confluence Cloud** - Create, update, and manage pages, spaces, and other Confluence objects.
+ **Atlassian Jira Cloud** - Create issues, update tickets, search projects, manage workflows.
+ **BambooHR** - Access employee data, manage time-off requests.
+ **Box** - Manage files, folders, and collaborate on documents.
+ **Canva** - Create and edit designs, manage templates and assets.
+ **Cisco Webex Meetings** - Schedule meetings, retrieve recordings, and manage participants.
+ **Cisco Webex Video Messaging** - Manage video updates, retrieve transcripts, and access video metadata in Cisco Webex (Vidcast).
+ **Dropbox** - Upload files, manage folder structures, generate sharing links, and control access permissions.
+ **Dun & Bradstreet** - Look up company profiles, credit risk data, and business intelligence.
+ **GitHub** - Manage repositories, issues, pull requests, and code collaboration.
+ **Gmail** - Read emails, search inbox, draft messages, manage labels, and organize threads.
+ **Google Analytics** - Query traffic reports, retrieve audience data, monitor conversion events, and access performance metrics.
+ **Google Calendar** - Create and update events, check availability, manage invites, and retrieve schedules.
+ **Google Chat** - Send messages, manage spaces, and interact with chat threads.
+ **Google Docs** - Create and edit documents, read content, and collaborate on text-based files.
+ **Google Drive** - Upload files, manage folders, search content, and perform file operations.
+ **Google Meet** - Schedule video meetings, list hosted meetings, retrieve transcripts, and update access settings.
+ **Google Sheets** - Create and edit spreadsheets, read and write cell ranges, and perform data operations.
+ **Google Slides** - Create presentations, edit slides, manage layouts, and add speaker notes.
+ **HG Insights** - Access technographic data, query company technology profiles, and retrieve market intelligence.
+ **HubSpot** - Manage contacts, deals, marketing campaigns, and CRM data.
+ **HuggingFace** - Access AI models, datasets, and machine learning workflows.
+ **Intercom** - Manage customer conversations, support tickets, and messaging.
+ **Linear** - Create and manage issues, projects, and development workflows.
+ **Microsoft OneDrive** - Create, update, delete, and manage OneDrive files and folders.
+ **Microsoft OneNote** - Create and edit notebooks, manage sections, and organize notes.
+ **Microsoft Outlook** - Send emails, manage calendar events, access contacts.
+ **Microsoft SharePoint** - Perform actions on SharePoint lists, items, files, and Excel workbooks.
+ **Microsoft Teams** - Send messages, manage channels, schedule meetings, and manage team collaboration.
+ **Monday.com** - Manage projects, tasks, and team collaboration workflows.
+ **Moodys GenAI Ready Data** - Access Moody's credit ratings, financial research, and risk analytics data.
+ **New Relic** - Access observability data, query metrics, and manage monitoring workflows.
+ **Notion** - Create and manage pages, databases, and collaborative workspaces.
+ **PagerDuty** - Create incidents, manage escalations, update on-call schedules.
+ **QuickBooks** - Manage invoices, track expenses, generate financial reports, and handle vendor records.
+ **Salesforce** - Create records, update opportunities, search accounts, manage leads.
+ **SAP** - Access SAP S/4HANA systems to perform read operations on enterprise data.
+ **ServiceNow** - Create incidents, update requests, manage workflows.
+ **Shopify** - Manage products, orders, customers, and store operations.
+ **Slack** - Send messages, create channels, manage notifications.
+ **Smartsheet** - Update sheets, manage project data.
+ **Snowflake Cortex Agent** - Query Snowflake data and run AI-powered analytics through Cortex Agent.
+ **Visier Agent** - Access workforce analytics, query people data, and generate HR insights.
+ **WhatsApp** - Send and manage messages through WhatsApp Business.
+ **Zapier** - Trigger workflows across thousands of connected applications.
+ **Zendesk** - Create tickets, update cases, search knowledge base.
+ **Zoom** - Schedule meetings, add webinar registrants, summarize recorded meetings, and list participants.
+ **ZoomInfo** - Look up company and contact data, and query firmographic and intent data.

## AWS service connectors
<a name="action-connector-apis-aws-services"></a>
+ **Amazon S3** - Upload files, manage buckets, retrieve objects.
+ **Amazon Bedrock** - Generate content, analyze data, process requests.
+ **Amazon Textract** - Extract text and data from documents.
+ **Amazon Comprehend** - Natural language processing and sentiment analysis.
+ **Amazon Comprehend Medical** - Medical text analysis and entity extraction.

## Connector compatibility matrix
<a name="action-connector-compatibility-matrix"></a>

The following table shows which Amazon Quick features each connector type supports:


**Connector feature compatibility**  

<table>
<thead>
  <tr><th>Connector</th><th>Chat Agents</th><th>Flows</th><th>Dashboard Visuals</th><th>Dashboard Alerts</th><th>Automations</th><th>Companions</th></tr>
</thead>
<tbody>
  <tr><td colspan="7"><b>AWS Built-in Services</b></td></tr>
  <tr><td>AWS Bedrock Agent Runtime</td><td>—</td><td>—</td><td>—</td><td>—</td><td>✓</td><td>—</td></tr>
  <tr><td>AWS Bedrock Data Automation Runtime</td><td>—</td><td>—</td><td>—</td><td>—</td><td>✓</td><td>—</td></tr>
  <tr><td>AWS Bedrock Runtime</td><td>—</td><td>—</td><td>—</td><td>—</td><td>✓</td><td>—</td></tr>
  <tr><td>Amazon Comprehend</td><td>—</td><td>—</td><td>—</td><td>—</td><td>✓</td><td>—</td></tr>
  <tr><td>Amazon Comprehend Medical</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td></tr>
  <tr><td>Amazon S3</td><td>—</td><td>—</td><td>—</td><td>—</td><td>✓</td><td>—</td></tr>
  <tr><td>Amazon Textract</td><td>—</td><td>—</td><td>—</td><td>—</td><td>✓</td><td>—</td></tr>
  <tr><td colspan="7"><b>External Service Connectors</b></td></tr>
  <tr><td>Adobe Marketing Agent</td><td>✓</td><td>✓</td><td>—</td><td>—</td><td>—</td><td>—</td></tr>
  <tr><td>Airtable</td><td>✓</td><td>✓</td><td>✓</td><td>—</td><td>—</td><td>—</td></tr>
  <tr><td>Asana</td><td>✓</td><td>✓</td><td>—</td><td>—</td><td>—</td><td>✓</td></tr>
  <tr><td>Atlassian Confluence Cloud</td><td>✓</td><td>✓</td><td>—</td><td>—</td><td>✓</td><td>✓</td></tr>
  <tr><td>Atlassian Jira Cloud</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td></tr>
  <tr><td>BambooHR</td><td>✓</td><td>✓</td><td>—</td><td>—</td><td>—</td><td>✓</td></tr>
  <tr><td>Box</td><td>✓</td><td>✓</td><td>—</td><td>—</td><td>—</td><td>—</td></tr>
  <tr><td>Canva</td><td>✓</td><td>✓</td><td>—</td><td>—</td><td>—</td><td>—</td></tr>
  <tr><td>Cisco Webex Meetings</td><td>✓</td><td>✓</td><td>—</td><td>—</td><td>—</td><td>—</td></tr>
  <tr><td>Cisco Webex Video Messaging</td><td>✓</td><td>✓</td><td>—</td><td>—</td><td>—</td><td>—</td></tr>
  <tr><td>Dropbox</td><td>✓</td><td>✓</td><td>✓</td><td>—</td><td>—</td><td>—</td></tr>
  <tr><td>Dun &amp; Bradstreet</td><td>✓</td><td>✓</td><td>—</td><td>—</td><td>—</td><td>—</td></tr>
  <tr><td>GitHub</td><td>✓</td><td>✓</td><td>—</td><td>—</td><td>—</td><td>—</td></tr>
  <tr><td>Gmail</td><td>✓</td><td>✓</td><td>✓</td><td>—</td><td>—</td><td>—</td></tr>
  <tr><td>Google Analytics</td><td>✓</td><td>✓</td><td>✓</td><td>—</td><td>—</td><td>—</td></tr>
  <tr><td>Google Calendar</td><td>✓</td><td>✓</td><td>✓</td><td>—</td><td>—</td><td>—</td></tr>
  <tr><td>Google Chat</td><td>✓</td><td>✓</td><td>—</td><td>—</td><td>—</td><td>—</td></tr>
  <tr><td>Google Docs</td><td>✓</td><td>✓</td><td>✓</td><td>—</td><td>—</td><td>—</td></tr>
  <tr><td>Google Drive</td><td>✓</td><td>✓</td><td>✓</td><td>—</td><td>—</td><td>—</td></tr>
  <tr><td>Google Meet</td><td>✓</td><td>✓</td><td>✓</td><td>—</td><td>—</td><td>—</td></tr>
  <tr><td>Google Sheets</td><td>✓</td><td>✓</td><td>✓</td><td>—</td><td>—</td><td>—</td></tr>
  <tr><td>Google Slides</td><td>✓</td><td>✓</td><td>✓</td><td>—</td><td>—</td><td>—</td></tr>
  <tr><td>HG Insights</td><td>✓</td><td>✓</td><td>—</td><td>—</td><td>—</td><td>—</td></tr>
  <tr><td>HubSpot</td><td>✓</td><td>✓</td><td>—</td><td>—</td><td>—</td><td>—</td></tr>
  <tr><td>HuggingFace</td><td>✓</td><td>✓</td><td>—</td><td>—</td><td>—</td><td>—</td></tr>
  <tr><td>Intercom</td><td>✓</td><td>✓</td><td>—</td><td>—</td><td>—</td><td>—</td></tr>
  <tr><td>Linear</td><td>✓</td><td>✓</td><td>—</td><td>—</td><td>—</td><td>—</td></tr>
  <tr><td>Microsoft OneDrive</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td></tr>
  <tr><td>Microsoft OneNote</td><td>✓</td><td>✓</td><td>—</td><td>—</td><td>—</td><td>—</td></tr>
  <tr><td>Microsoft Outlook</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td></tr>
  <tr><td>Microsoft SharePoint</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td></tr>
  <tr><td>Microsoft Teams</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td></tr>
  <tr><td>Monday.com</td><td>✓</td><td>✓</td><td>—</td><td>—</td><td>—</td><td>—</td></tr>
  <tr><td>Moodys GenAI Ready Data</td><td>✓</td><td>✓</td><td>—</td><td>—</td><td>—</td><td>—</td></tr>
  <tr><td>New Relic</td><td>✓</td><td>✓</td><td>—</td><td>—</td><td>—</td><td>—</td></tr>
  <tr><td>Notion</td><td>✓</td><td>✓</td><td>—</td><td>—</td><td>—</td><td>—</td></tr>
  <tr><td>PagerDuty</td><td>✓</td><td>✓</td><td>—</td><td>—</td><td>✓</td><td>✓</td></tr>
  <tr><td>QuickBooks</td><td>✓</td><td>✓</td><td>✓</td><td>—</td><td>—</td><td>—</td></tr>
  <tr><td>Salesforce</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td></tr>
  <tr><td>SAP</td><td>✓</td><td>—</td><td>—</td><td>—</td><td>✓</td><td>✓</td></tr>
  <tr><td>ServiceNow</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td></tr>
  <tr><td>Shopify</td><td>✓</td><td>✓</td><td>—</td><td>—</td><td>—</td><td>—</td></tr>
  <tr><td>Slack</td><td>✓</td><td>✓</td><td>✓</td><td>—</td><td>—</td><td>✓</td></tr>
  <tr><td>Smartsheet</td><td>✓</td><td>✓</td><td>—</td><td>—</td><td>—</td><td>✓</td></tr>
  <tr><td>Snowflake Cortex Agent</td><td>✓</td><td>✓</td><td>—</td><td>—</td><td>—</td><td>—</td></tr>
  <tr><td>Visier Agent</td><td>✓</td><td>✓</td><td>—</td><td>—</td><td>—</td><td>—</td></tr>
  <tr><td>WhatsApp</td><td>✓</td><td>✓</td><td>—</td><td>—</td><td>—</td><td>—</td></tr>
  <tr><td>Zapier</td><td>✓</td><td>✓</td><td>—</td><td>—</td><td>—</td><td>—</td></tr>
  <tr><td>Zendesk</td><td>✓</td><td>✓</td><td>—</td><td>—</td><td>—</td><td>✓</td></tr>
  <tr><td>Zoom</td><td>✓</td><td>✓</td><td>✓</td><td>—</td><td>—</td><td>—</td></tr>
  <tr><td>ZoomInfo</td><td>✓</td><td>✓</td><td>—</td><td>—</td><td>—</td><td>—</td></tr>
  <tr><td colspan="7"><b>Custom Connector Types</b></td></tr>
  <tr><td>Model Context Protocol (MCP)</td><td>✓</td><td>✓</td><td>—</td><td>—</td><td>✓</td><td>—</td></tr>
  <tr><td>OpenAPI</td><td>✓</td><td>✓</td><td>—</td><td>—</td><td>—</td><td>—</td></tr>
  <tr><td>REST API</td><td>—</td><td>—</td><td>—</td><td>—</td><td>✓</td><td>—</td></tr>
</tbody>
</table>


**Authentication Support:**
+ **Chat Agents and Companions** - Support user authentication (Default OAuth app, Custom OAuth app, Basic)
+ **Dashboard Visuals** - Support user authentication (Default OAuth app, Custom OAuth app)
+ **Dashboard Alerts** - Support system authentication (Service-to-Service OAuth or API Key)
+ **Automations** - Support system authentication (Service-to-Service OAuth)