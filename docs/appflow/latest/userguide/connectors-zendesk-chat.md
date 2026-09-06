

# Zendesk Chat connector for Amazon AppFlow
<a name="connectors-zendesk-chat"></a>

Zendesk Chat is a live chat service that Zendesk offers as part of its platform. Zendesk Chat helps businesses automate and enhance customer support interactions across web, mobile, and social channels. In a Zendesk Chat account, you store data related to customer conversations. If you use Zendesk Chat, you can also use Amazon AppFlow to transfer this data to certain AWS services or other supported applications.

## Amazon AppFlow support for Zendesk Chat
<a name="zendesk-chat-support"></a>

Amazon AppFlow supports Zendesk Chat as follows.

**Supported as a data source?**  
Yes. You can use Amazon AppFlow to transfer data from Zendesk Chat.

**Supported as a data destination?**  
No. You can't use Amazon AppFlow to transfer data to Zendesk Chat.

## Before you begin
<a name="zendesk-chat-prereqs"></a>

To use Amazon AppFlow to transfer data from Zendesk Chat to supported destinations, you must meet these requirements:
+ You have a Zendesk Chat account.
+ In the Zendesk Chat account settings, you've registered Amazon AppFlow with an *API client*. The API client provides the client credentials that Amazon AppFlow uses to access your data securely with authenticated calls to your account.
+ You've configured your API client with one or more redirect URLs for Amazon AppFlow.

  Redirect URLs have the following format:

  ```
  https://{{region}}.console.aws.amazon.com/appflow/oauth
  ```

  In this URL, *region* is the code for the AWS Region where you use Amazon AppFlow to transfer data from Zendesk Chat. For example, the code for the US East (N. Virginia) Region is `us-east-1`. For that Region, the URL is the following:

  ```
  https://us-east-1.console.aws.amazon.com/appflow/oauth
  ```

  For the AWS Regions that Amazon AppFlow supports, and their codes, see [Amazon AppFlow endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/appflow.html) in the *AWS General Reference.*

In the settings for your API client, note the client ID and client secret because you will need them to create a connection in Amazon AppFlow.

## Connecting Amazon AppFlow to your Zendesk Chat account
<a name="zendesk-chat-connecting"></a>

To connect Amazon AppFlow to your Zendesk Chat account, provide your Zendesk subdomain and the client credentials that authorize Amazon AppFlow to access your data. If you haven't yet configured your Zendesk Chat account to integrate with Amazon AppFlow, see [Before you begin](#zendesk-chat-prereqs).

**To connect to Zendesk Chat**

1. Sign in to the AWS Management Console and open the Amazon AppFlow console at [https://console.aws.amazon.com/appflow/](https://console.aws.amazon.com/appflow/).

1. In the navigation pane on the left, choose **Connections**.

1. On the **Manage connections** page, for **Connectors**, choose **Zendesk Chat**.

1. Choose **Create connection**.

1. In the **Connect to Zendesk Chat** window, enter the following information:
   + **Custom authorization code URL** – Your Zendesk subdomain. You can find this value in the URL that you visit when you sign in to Zendesk Chat. For example, in the account URL `https://my-account.zendesk.com`, the subdomain is `my-account`.
   + **Client ID** and **Client secret** – The client credentials that Zendesk assigned to your API client.

1. Optionally, under **Data encryption**, choose **Customize encryption settings (advanced)** if you want to encrypt your data with a customer managed key in the AWS Key Management Service (AWS KMS).

   By default, Amazon AppFlow encrypts your data with a KMS key that AWS creates, uses, and manages for you. Choose this option if you want to encrypt your data with your own KMS key instead.

   Amazon AppFlow always encrypts your data during transit and at rest. For more information, see [Data protection in Amazon AppFlow](data-protection.md).

   If you want to use a KMS key from the current AWS account, select this key under **Choose an AWS KMS key**. If you want to use a KMS key from a different AWS account, enter the Amazon Resource Name (ARN) for that key.

1. For **Connection name**, enter a name for your connection.

1. Choose **Continue**. A window appears that asks if you want to allow Amazon AppFlow to access your Zendesk Chat account.

1. Choose **Allow**.

On the **Manage connections** page, your new connection appears in the **Connections** table. When you create a flow that uses Zendesk Chat as the data source, you can select this connection.

## Transferring data from Zendesk Chat with a flow
<a name="zendesk-chat-transfer-data"></a>

To transfer data from Zendesk Chat, create an Amazon AppFlow flow, and choose Zendesk Chat as the data source. For the steps to create a flow, see [Creating flows in Amazon AppFlow](create-flow.md).

When you configure the flow, choose the data object that you want to transfer. For the objects that Amazon AppFlow supports for Zendesk Chat, see [Supported objects](#zendesk-chat-objects).

Also, choose the destination where you want to transfer the data object that you selected. For more information about how to configure your destination, see [Supported destinations](#zendesk-chat-destinations).

## Supported objects
<a name="zendesk-chat-objects"></a>

When you create a flow that uses Zendesk Chat as the data source, you can transfer any of the following data objects to supported destinations:
+ Chat Offline Message
+ Chat Support Chat
+ Agent
+ Agent Event
+ Account
+ Department
+ Trigger
+ Shortcut
+ Ban
+ Goal
+ Skill
+ Role
+ Route Setting Account
+ Route Setting Agent

## Supported destinations
<a name="zendesk-chat-destinations"></a>

When you create a flow that uses Zendesk Chat as the data source, you can set the destination to any of the following connectors: 
+ [Amazon Lookout for Metrics](lookout.md)
+ [Amazon Redshift](redshift.md)
+ [Amazon RDS for PostgreSQL](connectors-amazon-rds-postgres-sql.md)
+ [Amazon S3](s3.md)
+ [HubSpot](connectors-hubspot.md)
+ [Marketo](marketo.md)
+ [Salesforce](salesforce.md)
+ [SAP OData](sapodata.md)
+ [Snowflake](snowflake.md)
+ [Upsolver](upsolver.md)
+ [Zendesk](zendesk.md)
+ [Zoho CRM](connectors-zoho-crm.md)