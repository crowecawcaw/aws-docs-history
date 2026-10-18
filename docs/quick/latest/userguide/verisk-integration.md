

# Verisk Underwriting Intelligence integration
<a name="verisk-integration"></a>

Access Insurance Services Office (ISO) loss cost data directly from Amazon Quick using natural language. With the Verisk Underwriting Intelligence connector, you can retrieve filed loss cost changes, review experience indexes, and analyze indication details without leaving Amazon Quick.

Verisk Underwriting Intelligence is available as a connector in Amazon Quick.

This connector supports Custom OAuth app authentication. For information about the authentication methods that Amazon Quick supports, see [Authentication methods](quick-action-auth.md).

## Prerequisites
<a name="verisk-integration-prerequisites"></a>

Before you set up the integration, verify that you have the following resources and access.
+ An active Verisk account with an ISO Core Lines Services subscription that includes access to Verisk Underwriting Intelligence.
+ Permissions to create and manage OAuth applications in your Verisk developer portal.
+ A subscription that meets the requirements described in [Set up integrations in the console](integration-console-setup-process.md).

## Configuring your Verisk account
<a name="verisk-source-setup"></a>

The Custom OAuth app authentication method in Amazon Quick requires an OAuth app configured in your Verisk developer portal.

### To register an OAuth app
<a name="verisk-configure-oauth"></a>

1. Sign in to your Verisk developer portal, and then create an OAuth application for the Underwriting Intelligence API.

1. For **Redirect URI**, enter `https://{{region}}.quicksight.aws.amazon.com/sn/oauthcallback`. Replace {{region}} with your AWS Region, for example, `us-east-1`.

**Save your credentials**  
When you save the OAuth app in the next step, Verisk displays the client ID and client secret. You cannot retrieve the client secret later. If you lose it, you must generate a new one.

Choose **Save**, and then record the client ID and client secret that Verisk displays.

The client ID and client secret serve as the Client ID and Client Secret when you configure the connector in Amazon Quick with the Custom OAuth app authentication method.

For more information, see [Verisk Underwriting Intelligence](https://www.verisk.com/resources/verisk-underwriting-intelligence/) on the Verisk website.

## Setting up the integration in Amazon Quick
<a name="verisk-integration-setup"></a>

After you configure your Verisk account, create the connector in Amazon Quick.

1. In the Amazon Quick console, choose **Connectors**. On the **Create for your team** tab, choose **Verisk Underwriting Intelligence**.

1. For **Name**, enter a descriptive name for your connector. For **Connection type**, choose **Public network**.

1. For the **Custom OAuth app** authentication method, enter the following fields:
   + **Client ID** – The client ID from your Verisk OAuth app.
   + **Client Secret** – The client secret from your Verisk OAuth app.
   + **Token URL** – The token endpoint provided by Verisk.
   + **Authorization URL** – The authorization endpoint provided by Verisk.
   + **Redirect URL** – Auto-populated with the Amazon Quick callback URL.

1. Choose **Next**, review the actions, specify who can access the connector, and then choose **Publish**.

The connector appears in the **Available** panel with a status of **Connected**.

## Using available actions
<a name="verisk-integration-actions"></a>

After you set up the connector, you can use the following read-only actions to access ISO loss cost data from Verisk.


**Verisk Underwriting Intelligence available actions**  

| Action | Description | 
| --- | --- | 
| Loss cost activity | Retrieves the recent history of filed ISO loss cost revisions with summaries of their impact, so you can compare how loss costs changed across states and lines of business. | 
| Experience index | Returns loss experience trends and premium changes for the segments and rolling period that you choose. Use this action to review the data that feeds future rate indications. | 
| Indications | Returns details from ISO loss cost reviews, including indicated and selected adjustments by coverage, class, and territory segments. | 
| ISO data visualizer | Renders ISO data in a visual format when an answer includes loss cost figures. This action runs automatically alongside the other data actions. | 

**Note**  
This connector supports read-only actions. You can access the ISO products and jurisdictions covered by your Verisk subscription.

## Troubleshooting
<a name="verisk-integration-troubleshooting"></a>

To edit, share, or delete your connector, see [Managing existing integrations](integration-workflows.md#managing-existing-integrations).

### Resolving authentication issues
<a name="verisk-troubleshooting-auth"></a>
+ **Sign-in fails** – Verify that your Verisk account is active and that you can sign in to Verisk directly. Confirm that the redirect URI in your Verisk OAuth app matches the Amazon Quick callback URL.
+ **Invalid client credentials** – Verify that the Client ID and Client Secret match the values in your Verisk OAuth app.
+ **Missing data or access errors** – Verify that your Verisk subscription includes the ISO products that you are trying to access. The connector inherits your existing Verisk entitlements.