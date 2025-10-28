# Zendesk Sell connector for Amazon AppFlow

Zendesk Sell is a customer relationship management (CRM) service that Zendesk offers as
part of its platform. Zendesk Sell automates sales workflows to help its users engage leads
and close deals. In a Zendesk Sell account, you store data related to sales opportunities,
such as contacts, deals, and leads. If you use Zendesk Sell, you can also use Amazon AppFlow to
transfer this data to certain AWS services or other supported applications.

## Amazon AppFlow support for Zendesk Sell

Amazon AppFlow supports Zendesk Sell as follows.

**Supported as a data source?**
Yes. You can use Amazon AppFlow to transfer data from Zendesk Sell.

**Supported as a data destination?**
No. You can't use Amazon AppFlow to transfer data to Zendesk Sell.

## Before you begin

To use Amazon AppFlow to transfer data from Zendesk Sell to supported destinations, you must meet these
requirements:

- You have a Zendesk Sell account.
- In the OAuth settings for your Zendesk Sell account, you've registered Amazon AppFlow with a
  _developer app_. The developer app provides the client
  credentials that Amazon AppFlow uses to access your data securely with authenticated calls to the
  Zendesk Sell API.
- You've configured the developer app with a redirect URL for Amazon AppFlow.

Redirect URLs have the following format:

```
https://`region`.console.aws.amazon.com/appflow/oauth
```

In this URL, _region_ is the code for the AWS Region
where you use Amazon AppFlow to transfer data from Zendesk Sell. For example, the code for the US East (N. Virginia)
Region is `us-east-1`. For that Region, the URL is the following:

```
https://us-east-1.console.aws.amazon.com/appflow/oauth
```

For the AWS Regions that Amazon AppFlow supports, and their codes, see [Amazon AppFlow endpoints and quotas](../../../general/latest/gr/appflow.md "../../../general/latest/gr/appflow.md")
in the _AWS General Reference._

In the settings for your developer app, note the client ID and client secret because you
will need them to create a connection in Amazon AppFlow.

## Connecting Amazon AppFlow to your Zendesk Sell

account

To connect Amazon AppFlow to your Zendesk Sell account, provide the client credentials from
the developer app that authorizes Amazon AppFlow to access your data. If you haven't yet configured your
Zendesk Sell account to integrate with Amazon AppFlow, see [Before you begin](#zendesk-sell-prereqs "#zendesk-sell-prereqs").

###### To connect to Zendesk Sell

1. Sign in to the AWS Management Console and open the Amazon AppFlow console at [https://console.aws.amazon.com/appflow/](https://console.aws.amazon.com/appflow/ "https://console.aws.amazon.com/appflow/").
2. In the navigation pane on the left, choose **Connections**.
3. On the **Manage connections** page, for **Connectors**,
   choose **Zendesk Sell**.
4. Choose **Create connection**.
5. In the **Connect to Zendesk Sell** window, enter values for
   **Client ID** and **Client secret**. Zendesk assigns these
   client credentials to the developer app in your Zendesk Sell account.
6. Optionally, under **Data encryption**, choose **Customize
   encryption settings (advanced)** if you want to encrypt your data with a customer
   managed key in the AWS Key Management Service (AWS KMS).

By default, Amazon AppFlow encrypts your data with a KMS key that AWS creates, uses, and manages
for you. Choose this option if you want to encrypt your data with your own KMS key instead.

Amazon AppFlow always encrypts your data during transit and at rest. For more information, see
[Data protection in Amazon AppFlow](data-protection.md "data-protection.md").

If you want to use a KMS key from the current AWS account, select this key under
**Choose an AWS KMS key**. If you want to use a KMS key from a different
AWS account, enter the Amazon Resource Name (ARN) for that key. 7. For **Connection name**, enter a name for your connection. 8. Choose **Continue**. An **Authorize Application** window
opens. The window prompts you to give Amazon AppFlow read-only access to your data. 9. Choose **Authorize**.

On the **Manage connections** page, your new connection appears in the
**Connections** table. When you create a flow
that uses Zendesk Sell as the data source, you can select this connection.

## Transferring data from Zendesk Sell with a flow

To transfer data from Zendesk Sell, create an Amazon AppFlow flow, and choose Zendesk Sell as the data
source. For the steps to create a flow, see [Creating flows in Amazon AppFlow](create-flow.md "create-flow.md").

When you configure the flow, choose the data object that you want to transfer. For the objects
that Amazon AppFlow supports for Zendesk Sell, see [Supported objects](#zendesk-sell-objects "#zendesk-sell-objects").

Also, choose the destination where you want to transfer the data object that you selected.
For more information about how to configure your destination, see [Supported destinations](#zendesk-sell-destinations "#zendesk-sell-destinations").

## Supported objects

When you create a flow that uses Zendesk Sell as the data source, you can transfer any of the
following data objects to supported destinations:

- Contact
- Deal
- Lead
- Note
- Task

## Supported destinations

When you create a flow that uses Zendesk Sell as the data source, you can set the destination to any of the following connectors:

- [Amazon Lookout for Metrics](lookout.md "lookout.md")
- [Amazon Redshift](redshift.md "redshift.md")
- [Amazon RDS for PostgreSQL](connectors-amazon-rds-postgres-sql.md "connectors-amazon-rds-postgres-sql.md")
- [Amazon S3](s3.md "s3.md")
- [HubSpot](connectors-hubspot.md "connectors-hubspot.md")
- [Marketo](marketo.md "marketo.md")
- [Salesforce](salesforce.md "salesforce.md")
- [SAP OData](sapodata.md "sapodata.md")
- [Snowflake](snowflake.md "snowflake.md")
- [Upsolver](upsolver.md "upsolver.md")
- [Zendesk](zendesk.md "zendesk.md")
- [Zoho CRM](connectors-zoho-crm.md "connectors-zoho-crm.md")
