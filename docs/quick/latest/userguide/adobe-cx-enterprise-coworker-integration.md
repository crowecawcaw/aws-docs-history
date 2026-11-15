

# Adobe CX Enterprise Coworker integration
<a name="adobe-cx-enterprise-coworker-integration"></a>

Retrieve data and take actions across Adobe Experience Cloud products directly from AWS Quick using natural language. With the Adobe CX Enterprise Coworker connector, you can access Adobe Real-Time Customer Data Platform (Real-Time CDP), Customer Journey Analytics (CJA), and Workfront without leaving AWS Quick. The connector uses the Adobe CX Coworker Gateway, a single Model Context Protocol (MCP) endpoint that provides tools across multiple Adobe products.

This connector supports user authentication (OAuth). Each user signs in with their own Adobe credentials. Tool calls run with that user's Adobe permissions. For more information about the authentication methods that AWS Quick supports, see [Authentication methods](quick-action-auth.md).

## Prerequisites
<a name="adobe-cx-prerequisites"></a>

Before you set up the connector, verify that you have the following resources and access.
+ An AWS Quick subscription.
+ Adobe CX Enterprise Coworker provisioned for your organization and an Adobe account with access to it.
+ Adobe Experience Platform and at least one of the following applications: Adobe Real-Time CDP, Adobe Journey Optimizer, or Adobe Customer Journey Analytics.

## Configuring Adobe CX Enterprise Coworker
<a name="adobe-cx-source-setup"></a>

No configuration in Adobe is required. AWS Quick uses the Adobe-hosted OAuth endpoints, so you do not need to register an OAuth application or create a client ID or client secret. Make sure that each user has access to the Adobe products and sandboxes that they want to use.

If you configure custom OAuth settings, use the AWS Quick callback URL as the redirect URI: `https://{{region}}.quicksight.aws.amazon.com/sn/oauthcallback`. Replace {{region}} with your AWS Region, for example, `us-east-1`.

## Setting up the integration in AWS Quick
<a name="adobe-cx-integration-setup"></a>

Create the connector in AWS Quick after you verify your Adobe access.

1. In the AWS Quick console, choose **Connectors**. Choose the **Create for your team** tab, find **Model Context Protocol**, and choose **New connection**.

1. For **Name**, enter a descriptive name such as `Adobe CX Enterprise Coworker`. For **MCP server endpoint**, enter `https://mcp.coworker.experience.adobe.io`. For **Connection type** and **Auth server connection type**, choose **Public network**.

1. Choose **Next**. For authentication method, choose **User authentication**. When prompted, sign in with your Adobe account and authorize the connection.

1. On the **Manage Write Permissions** and **Manage Read Permissions** pages, review the available actions and choose whether users are asked for approval before each action runs. Choose **Next**.

1. On the **Publish** page, specify who can access the connector. Each user signs in with their own Adobe credentials the first time they use it. Choose **Publish**.

## Using available actions
<a name="adobe-cx-integration-actions"></a>

After you set up the connector, you can use the following actions. The actions available to you depend on your Adobe entitlements.


**Adobe CX Enterprise Coworker available actions**  

| Action | Description | 
| --- | --- | 
| ask\_aep\_agent | Sends a request to the Adobe Experience Platform AI Assistant to explore audiences, segments, schemas, datasets, and journeys. | 
| core\_list\_orgs | Lists the Adobe organizations that the user belongs to. | 
| core\_list\_sub\_orgs | Lists the sub-organizations under the current organization. | 
| core\_list\_sandboxes | Lists the sandboxes available in the current organization. | 
| core\_list\_dataviews | Lists the Customer Journey Analytics data views available in the current organization. | 

To see the current set of actions for your connector, open the connector's **Available actions** view in the AWS Quick console.

## Troubleshooting
<a name="adobe-cx-troubleshooting"></a>

To edit, share, or delete your connector, see [Managing existing integrations](integration-workflows.md#managing-existing-integrations).

The following issues can occur when you set up or use the connector.

### Sign-in fails
<a name="adobe-cx-troubleshoot-signin"></a>

Verify that your Adobe account is active and that you can sign in to Adobe Experience Cloud directly. Confirm that your organization is licensed for Adobe CX Enterprise Coworker.

### Sign-in succeeds but no actions appear
<a name="adobe-cx-troubleshoot-no-actions"></a>

Verify that you have access to the required Adobe products, and then sync the connector.

### Results are missing or empty
<a name="adobe-cx-troubleshoot-missing-data"></a>

Actions run with your Adobe permissions. Ask your Adobe administrator to grant access to the required organization, sandbox, or data view.

### Authorization expired
<a name="adobe-cx-troubleshoot-expired"></a>

Sign out of the connector and sign in again with your Adobe credentials.