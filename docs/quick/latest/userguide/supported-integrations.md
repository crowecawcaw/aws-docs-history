# Supported integrations

Amazon Quick supports integrations with various third-party applications and services. Each integration supports different combinations of actions and knowledge base creation capabilities. The following table shows the supported integrations and their capabilities.

| Supported Integration Capabilities | Integration | Actions | Knowledge Base |
| ---------------------------------- | ----------- | ------- | -------------- |
| Amazon S3                          | ✓           | ✓       |
| Asana                              | ✓           | —       |
| Atlassian Confluence Cloud         | ✓           | ✓       |
| BambooHR                           | ✓           | —       |
| Box                                | ✓           | —       |
| Canva                              | ✓           | —       |
| GitHub                             | ✓           | —       |
| Google Drive                       | —           | ✓       |
| HubSpot                            | ✓           | —       |
| HuggingFace                        | ✓           | —       |
| Intercom                           | ✓           | —       |
| Atlassian Jira Cloud               | ✓           | —       |
| Linear                             | ✓           | —       |
| Microsoft Outlook                  | ✓           | —       |
| Microsoft OneDrive                 | ✓           | ✓       |
| Microsoft SharePoint Cloud         | ✓           | ✓       |
| Microsoft Teams                    | ✓           | —       |
| Model Context Protocol (MCP)       | ✓           | —       |
| Monday.com                         | ✓           | —       |
| Notion                             | ✓           | —       |
| OpenAPI Specification              | ✓           | —       |
| PagerDuty                          | ✓           | —       |
| REST API                           | ✓           | —       |
| Salesforce                         | ✓           | —       |
| SAP Bill of Materials              | ✓           | —       |
| SAP Business Partner               | ✓           | —       |
| SAP Material Stock                 | ✓           | —       |
| SAP Physical Inventory Docs        | ✓           | —       |
| SAP Product Master                 | ✓           | —       |
| ServiceNow                         | ✓           | —       |
| Slack                              | ✓           | —       |
| Smartsheet                         | ✓           | —       |
| Web Crawler                        | —           | ✓       |
| Zendesk Suite                      | ✓           | —       |

###### Note

Not all applications support all integration types. The available options depend on the capabilities of each specific application and your user role.

## Integration capability definitions

**Actions**

Call APIs and perform actions in external applications directly from Amazon Quick. You can share action connectors with other users and use them in automated workflows.

**Knowledge base**

Create searchable repositories of information from external sources. Knowledge bases are children of data access integrations. Add them to spaces or use them directly in chat agents.

## Authentication method definitions

**User auth**

Custom user-based OAuth authentication requiring base URL, client ID, client secret, token URL, auth URL, and redirect URL.

**Service auth**

Service-to-service authentication using either API key (with base URL and email) or service-to-service OAuth (with base URL, client ID, client secret, and token URL).

**Managed OAuth 2.0**

Managed OAuth 2.0 authentication flow with provider-specific sign-in
interface.

**AWS credentials**

AWS-specific authentication using AWS access keys and permissions.

**Basic auth**

Username and password authentication.

**Form/SAML auth**

Form-based or SAML authentication with configurable field selectors.

**JSON schema**

Schema-based authentication for OpenAPI specifications.
