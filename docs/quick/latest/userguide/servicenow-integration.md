

# ServiceNow integration
<a name="servicenow-integration"></a>

Use the ServiceNow integration to perform actions within your ServiceNow instances, including managing incidents, problems, change requests, knowledge base articles, and attachments. This integration uses the ServiceNow REST API. For more information, see [REST API](https://docs.servicenow.com/bundle/xanadu-api-reference/page/build/applications/concept/api-rest.html) in the ServiceNow documentation.

Setting up this integration involves two steps. First, you configure an OAuth application in your ServiceNow instance. Then, you create the integration in Amazon Quick and connect it to your ServiceNow app. For information about the authentication methods that Amazon Quick supports, see [Authentication methods](quick-action-auth.md).

## Before you begin
<a name="servicenow-integration-prerequisites"></a>

Before you set up the integration, verify that you have the following.
+ A ServiceNow instance. This integration is validated against the Xanadu release.
+ A ServiceNow user account with permissions to create OAuth applications (`admin` role required).
+ For service authentication (client credentials), your instance must be running the Washington DC release or later.
+ For subscription requirements, see [Set up integrations in the console](integration-console-setup-process.md).

## Configure ServiceNow OAuth
<a name="servicenow-oauth-setup"></a>

Before you configure Amazon Quick, create an OAuth application endpoint in your ServiceNow instance. Complete all of the following steps in ServiceNow before moving to the Amazon Quick console.

For more information, see [Create an endpoint for clients to access the instance](https://www.servicenow.com/docs/bundle/xanadu-platform-security/page/administer/security/task/t_CreateEndpointforExternalClients.html) in the ServiceNow documentation.

### Register the OAuth application
<a name="servicenow-oauth-app-registration"></a>

To register the OAuth application, complete the following steps.

1. In your ServiceNow instance, navigate to **All** > **System OAuth** > **Application Registry** and choose **New**.

1. Choose **Create an OAuth API endpoint for external clients**.

1. Complete the form:
   + **Name** – A descriptive name for the OAuth application.
   + **Redirect URL** – `https://{{{region}}}.quicksight.aws.amazon.com/sn/oauthcallback`

     Replace {{{region}}} with your AWS Region (for example, `us-east-1`).

1. Choose **Submit**.

1. Reopen the application registry entry and choose the lock icon next to **Client Secret** to reveal the value.

1. Copy the **Client ID** and **Client Secret** values. You need these when you configure the integration in Amazon Quick.

### Additional steps for service authentication (client credentials)
<a name="servicenow-oauth-client-credentials"></a>

If you plan to use service authentication, complete these additional steps after registering the OAuth application. The client credentials grant type was introduced in the ServiceNow Washington DC release. For more information, see [Up Your OAuth2.0 Game: Inbound Client Credentials with Washington DC](https://www.servicenow.com/community/developer-blog/up-your-oauth2-0-game-inbound-client-credentials-with-washington/ba-p/2816891) in the ServiceNow Community.

1. Enable the client credentials grant type. Navigate to `sys_properties.list` using the filter navigator and create a new system property with the following values:
   + **Name** – `glide.oauth.inbound.client.credential.grant_type.enabled`
   + **Type** – `true | false`
   + **Value** – `true`

1. Verify that the following plugins are installed (navigate to **Admin** > **Application Manager**):
   + OAuth 2.0 (`com.snc.platform.security.oauth`)
   + REST API Provider (`com.glide.rest`)
   + Authentication scope (`com.glide.auth.scope`)
   + REST API Auth Scope Plugin (`com.glide.rest.auth.scope`)

1. Return to your OAuth application in **System OAuth** > **Application Registry**. Add the **OAuth Application User** field to the form if it isn't visible (use **Configure** > **Form Builder** to add it).

1. Set the **OAuth Application User** to an appropriately permissioned user, such as a user with the System Administrator role.

**Important**  
With service authentication, all actions execute as the configured OAuth application user. Any Amazon Quick user with access to this integration can perform actions using that account's permissions. Configure the account permissions to match your organization's security requirements.

## Set up the integration in Amazon Quick
<a name="servicenow-action-integration-setup"></a>

After you complete the ServiceNow OAuth configuration, create the integration in Amazon Quick.

1. In the Amazon Quick console, choose **Connectors**.

1. Choose the **Create for your team** tab.

1. Find and choose **ServiceNow**.

1. Enter the integration details:
   + **Name** – Descriptive name for your ServiceNow integration.
   + **Description** (Optional) – Purpose of the integration.

1. Choose your connection type and fill in the connection settings:

   1. For **User authentication (OAuth)**, configure the following fields:
      + **Base URL** – `https://{{{your-instance}}}.service-now.com`
      + **Client ID** – Client ID from your ServiceNow OAuth application.
      + **Client Secret** – Client secret from your ServiceNow OAuth application.
      + **Token URL** – `https://{{{your-instance}}}.service-now.com/oauth_token.do`
      + **Auth URL** – `https://{{{your-instance}}}.service-now.com/oauth_auth.do`
      + **Redirect URL** – `https://{{{region}}}.quicksight.aws.amazon.com/sn/oauthcallback`

   1. For **Service authentication (client credentials)**, configure the following fields:
      + **Authentication type** – Service-to-service OAuth
      + **Base URL** – `https://{{{your-instance}}}.service-now.com`
      + **Client ID** – Client ID from your ServiceNow OAuth application.
      + **Client Secret** – Client secret from your ServiceNow OAuth application.
      + **Token URL** – `https://{{{your-instance}}}.service-now.com/oauth_token.do`

1. Choose **Create and continue**.

1. Choose users to share the integration with.

1. Choose **Next**.

For user authentication, navigate to **Connectors** > your ServiceNow connector name, and choose **Sign in** to complete the OAuth authorization flow.

## Available actions
<a name="servicenow-integration-actions"></a>

After you set up the integration, the following actions are available.


**ServiceNow available actions**  

| Category | Action | Description | 
| --- | --- | --- | 
| Incidents | List Incidents | Retrieve existing incidents. | 
| Incidents | Create Incident | Create an incident record to document a deviation from an expected standard of operation. | 
| Incidents | View Incident | Retrieve the details of a specific incident. | 
| Incidents | Update Incident | Update an incident record. | 
| Incidents | Delete Incident | Delete an incident. | 
| Problems | List Problems | Retrieve existing problems. | 
| Problems | Create Problem | Create a new problem record. | 
| Problems | View Problem | Retrieve the details of a specific problem record. | 
| Problems | Update Problem | Update a problem record. | 
| Problems | Delete Problem | Delete a problem. | 
| Change requests | List Change Requests | Retrieve all change requests. | 
| Change requests | Create Change Request | Create a change request to implement a controlled process for modifying approved and supported configuration items (CIs). | 
| Change requests | View Change Request | Retrieve detailed information about a specific change request. | 
| Change requests | Update Change Request | Modify a change request. | 
| Change requests | Delete Change Request | Delete a change request. | 
| Knowledge base articles | Create Knowledge Base Article | Create a knowledge base article. Requires the Knowledge API (sn\_km\_api) plugin. | 
| Knowledge base articles | Update Knowledge Base Article | Modify a knowledge base article. | 
| Knowledge base articles | Delete Knowledge Base Article | Delete a knowledge base article. | 
| Attachments | Retrieve Attachments Metadata | Retrieve metadata for attachment files. | 
| Attachments | Retrieve Attachment Metadata | Retrieve metadata for a specific attachment file. | 
| Attachments | Retrieve Attachment Content | Retrieve the binary file attachment content. | 
| Attachments | Upload Binary Attachment | Upload a binary file as an attachment to a specified record. | 
| Attachments | Upload Multipart Form Attachment | Upload a multipart file attachment. | 
| Attachments | Delete Attachment | Delete an attachment. | 
| Users | List Users | List all user records. | 
| System | List Choices | Retrieve choice list values from the sys\_choice table. | 

**Note**  
The specific actions available depend on the permissions configured in your ServiceNow instance and the authentication method used.

## Limitations
<a name="servicenow-integration-limitations"></a>

This integration interacts with ServiceNow through the REST API, which does not enforce UI policies, UI actions, or client scripts. These rules only apply in the ServiceNow browser interface. Server-side business rules, ACLs, and data policies are enforced. For more information, see [REST API](https://docs.servicenow.com/bundle/xanadu-api-reference/page/integrate/inbound-rest/concept/c_RESTAPI.html) in the ServiceNow documentation.

## Manage and troubleshoot
<a name="servicenow-integration-troubleshooting"></a>

To edit, share, or delete your integration, see [Managing existing integrations](integration-workflows.md#managing-existing-integrations).

### Authentication issues
<a name="servicenow-troubleshooting-auth"></a>
+ **OAuth authorization fails** – Verify that the Client ID and Client Secret match the values in your ServiceNow Application Registry. Confirm the Redirect URL in ServiceNow matches the URL in your Amazon Quick configuration exactly.
+ **Service authentication fails** – Verify that the `glide.oauth.inbound.client.credential.grant_type.enabled` system property is set to `true`. Confirm the **OAuth Application User** field is populated on the application registry record.

### Common error messages
<a name="servicenow-troubleshooting-errors"></a>
+ **Actions return permission errors** – Verify that the ServiceNow user or OAuth application user has the required roles to access the target tables (for example, `itil` role for incident management).
+ **Connection timeout or unreachable instance** – Verify the Base URL uses the correct ServiceNow instance name. Confirm the ServiceNow instance is accessible and not in maintenance mode.