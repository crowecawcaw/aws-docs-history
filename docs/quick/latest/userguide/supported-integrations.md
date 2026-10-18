

# Supported integrations
<a name="supported-integrations"></a>

Amazon Quick supports integrations with various third-party applications and services. Each integration supports different combinations of actions and knowledge base creation capabilities. The following table shows the supported integrations and their capabilities.


**Supported Integration Capabilities**  

| Integration | Actions | Knowledge Base | 
| --- | --- | --- | 
| Adobe Marketing Agent | Yes | No | 
| Airtable | Yes | No | 
| Amazon S3 | Yes | Yes | 
| Asana | Yes | No | 
| Atlassian Confluence Cloud | Yes | Yes | 
| Atlassian Jira Cloud | Yes | No | 
| AWS Agent Registry | Yes | No | 
| BambooHR | Yes | No | 
| Box | Yes | No | 
| Canva | Yes | No | 
| Cisco Webex Meetings | Yes | No | 
| Cisco Webex Video Messaging | Yes | No | 
| Dropbox | Yes | No | 
| Dun & Bradstreet | Yes | No | 
| Figma | Yes | No | 
| GitHub | Yes | No | 
| Gong | Yes | No | 
| Gmail | Yes | No | 
| Google Analytics | Yes | No | 
| Google Calendar | Yes | No | 
| Google Chat | Yes | No | 
| Google Docs | Yes | No | 
| Google Drive | Yes | Yes | 
| Google Meet | Yes | No | 
| Google Sheets | Yes | No | 
| Google Slides | Yes | No | 
| HG Insights | Yes | No | 
| HubSpot | Yes | No | 
| HuggingFace | Yes | No | 
| Intercom | Yes | No | 
| Linear | Yes | No | 
| Microsoft OneDrive | Yes | Yes | 
| Microsoft OneNote | Yes | No | 
| Microsoft Outlook | Yes | No | 
| Microsoft SharePoint Online | Yes | Yes | 
| Microsoft Teams | Yes | No | 
| Model Context Protocol (MCP) | Yes | No | 
| Monday.com | Yes | No | 
| Moodys GenAI Ready Data | Yes | No | 
| New Relic | Yes | No | 
| Notion | Yes | No | 
| OpenAPI Specification | Yes | No | 
| PagerDuty | Yes | No | 
| QuickBooks | Yes | No | 
| REST API | Yes | No | 
| Salesforce | Yes | No | 
| SAP Bill of Materials | Yes | No | 
| SAP Business Partner | Yes | No | 
| SAP Material Stock | Yes | No | 
| SAP Physical Inventory Docs | Yes | No | 
| SAP Product Master | Yes | No | 
| ServiceNow | Yes | No | 
| Shopify | Yes | No | 
| Slack | Yes | No | 
| Smartsheet | Yes | No | 
| Snowflake Cortex Agent | Yes | No | 
| Visier Agent | Yes | No | 
| Verisk Underwriting Intelligence | Yes | No | 
| Web Crawler | No | Yes | 
| WhatsApp | Yes | No | 
| Zapier | Yes | No | 
| Zendesk Suite | Yes | No | 
| Zoom | Yes | No | 
| ZoomInfo | Yes | No | 

**Note**  
Not all applications support all integration types. The available options depend on the capabilities of each specific application and your user role.

## Integration capability definitions
<a name="integration-capability-definitions"></a>

**Actions**  
Call APIs and perform actions in external applications directly from Amazon Quick. You can share connectors with other users and use them in automated workflows.

**Knowledge base**  
Create searchable repositories of information from external sources. Knowledge bases are children of data access integrations. Add them to spaces or use them directly in chat agents.

## Authentication method definitions
<a name="authentication-method-definitions"></a>

**User auth**  
Custom user-based OAuth authentication requiring base URL, client ID, client secret, token URL, auth URL, and redirect URL.

**Service auth**  
Service-to-service authentication using either API key (with base URL and email) or service-to-service OAuth (with base URL, client ID, client secret, and token URL).

**Managed OAuth 2.0**  
Managed OAuth 2.0 authentication flow with provider-specific sign-in interface.

**AWS credentials**  
AWS-specific authentication using AWS access keys and permissions.

**Basic auth**  
Username and password authentication.

**Form/SAML auth**  
Form-based or SAML authentication with configurable field selectors.

**JSON schema**  
Schema-based authentication for OpenAPI specifications.