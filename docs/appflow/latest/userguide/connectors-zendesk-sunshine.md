# Zendesk Sunshine connector for Amazon AppFlow

Zendesk Sunshine is an application that helps builders create custom experiences on the
Zendesk platform for ticketing and customer service. If you're a Zendesk Sunshine user, your
account contains data about your Zendesk objects and their relationships.
You can use Amazon AppFlow to transfer data from
Zendesk Sunshine to certain AWS services or other supported applications.

## Amazon AppFlow support for Zendesk Sunshine

Amazon AppFlow supports Zendesk Sunshine as follows.

**Supported as a data source?**
Yes. You can use Amazon AppFlow to transfer data from Zendesk Sunshine.

**Supported as a data destination?**
No. You can't use Amazon AppFlow to transfer data to Zendesk Sunshine.

## Before you begin

To use Amazon AppFlow to transfer data from Zendesk Sunshine to supported destinations, you must meet these
requirements:

- You have an account with Zendesk that contains the data that you want to transfer. For
  more information about the Zendesk Sunshine data objects that Amazon AppFlow supports, see [Supported objects](#zendesk-sunshine-objects "#zendesk-sunshine-objects").
- In your account, you've activated custom objects. For the steps to activate, see [Enabling custom objects](https://developer.zendesk.com/documentation/custom-data/custom-objects/getting-started-with-custom-objects/#enabling-custom-objects "https://developer.zendesk.com/documentation/custom-data/custom-objects/getting-started-with-custom-objects/#enabling-custom-objects") in the Zendesk Developers documentation.
- In your account settings, you've created an OAuth client for Amazon AppFlow. The OAuth client
  provides the client credentials that Amazon AppFlow uses to access your data securely with
  authenticated calls to your account.
- You've configured your OAuth client with one or more redirect URLs for Amazon AppFlow.

Redirect URLs have the following format:

```
https://`region`.console.aws.amazon.com/appflow/oauth
```

In this URL, _region_ is the code for the AWS Region
where you use Amazon AppFlow to transfer data from Zendesk Sunshine. For example, the code for the US East (N. Virginia)
Region is `us-east-1`. For that Region, the URL is the following:

```
https://us-east-1.console.aws.amazon.com/appflow/oauth
```

For the AWS Regions that Amazon AppFlow supports, and their codes, see [Amazon AppFlow endpoints and quotas](../../../general/latest/gr/appflow.md "../../../general/latest/gr/appflow.md")
in the _AWS General Reference._

In the settings for your OAuth client, note the client ID and client secret. You provide
these values to Amazon AppFlow when you connect to your Zendesk account.

## Connecting Amazon AppFlow to Zendesk Sunshine

To connect Amazon AppFlow to Zendesk Sunshine, provide the client credentials from your OAuth
client so that Amazon AppFlow can access your data. If you haven't yet configured your Zendesk Sunshine
project for Amazon AppFlow integration, see [Before you begin](#zendesk-sunshine-prereqs "#zendesk-sunshine-prereqs").

###### To connect to Zendesk Sunshine

1. Sign in to the AWS Management Console and open the Amazon AppFlow console at [https://console.aws.amazon.com/appflow/](https://console.aws.amazon.com/appflow/ "https://console.aws.amazon.com/appflow/").
2. In the navigation pane on the left, choose **Connections**.
3. On the **Manage connections** page, for **Connectors**,
   choose **Zendesk Sunshine**.
4. Choose **Create connection**.
5. In the **Connect to Zendesk Sunshine** window, enter the following
   information:
   - **Custom authorization tokens URL** and **Custom authorization
     code URL** – For each of these fields, enter your Zendesk subdomain. You can
     find the subdomain in the URL that you visit when you sign in to Zendesk. For example, in the
     account URL `https://my-account.zendesk.com`, the subdomain is
     `my-account`.
   - **Client ID** and **Client secret** – The
     client credentials that Zendesk assigned to your OAuth client.

6. Optionally, under **Data encryption**, choose **Customize
   encryption settings (advanced)** if you want to encrypt your data with a customer
   managed key in the AWS Key Management Service (AWS KMS).

By default, Amazon AppFlow encrypts your data with a KMS key that AWS creates, uses, and manages
for you. Choose this option if you want to encrypt your data with your own KMS key instead.

Amazon AppFlow always encrypts your data during transit and at rest. For more information, see
[Data protection in Amazon AppFlow](data-protection.md "data-protection.md").

If you want to use a KMS key from the current AWS account, select this key under
**Choose an AWS KMS key**. If you want to use a KMS key from a different
AWS account, enter the Amazon Resource Name (ARN) for that key. 7. For **Connection name**, enter a name for your connection. 8. Choose **Continue**. 9. In the window that appears, sign in to your Zendesk account, and grant access to
Amazon AppFlow.

On the **Manage connections** page, your new connection appears in the
**Connections** table. When you create a flow
that uses Zendesk Sunshine as the data source, you can select this connection.

## Transferring data from Zendesk Sunshine with a flow

To transfer data from Zendesk Sunshine, create an Amazon AppFlow flow, and choose Zendesk Sunshine as the data
source. For the steps to create a flow, see [Creating flows in Amazon AppFlow](create-flow.md "create-flow.md").

When you configure the flow, choose the data object that you want to transfer. For the objects
that Amazon AppFlow supports for Zendesk Sunshine, see [Supported objects](#zendesk-sunshine-objects "#zendesk-sunshine-objects").

Also, choose the destination where you want to transfer the data object that you selected.
For more information about how to configure your destination, see [Supported destinations](#zendesk-sunshine-destinations "#zendesk-sunshine-destinations").

## Supported destinations

When you create a flow that uses Zendesk Sunshine as the data source, you can set the destination to any of the following connectors:

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

## Supported objects

When you create a flow that uses Zendesk Sunshine as the data source, you can transfer any of the
following data objects to supported destinations:

| **Object**                          | **Field**  | **Data type**                                | **Supported filters** |
| ----------------------------------- | ---------- | -------------------------------------------- | --------------------- |
| Custom Object Type Permission       | Data       | Struct                                       |                       |
| Custom Relationship Type Permission | Data       | Struct                                       |                       |
| Object Record                       | Attributes | Struct                                       |                       |
| Created At                          | DateTime   | GREATER_THAN_OR_EQUAL_TO, BETWEEN, LESS_THAN |
| External Id                         | String     |                                              |
| Id                                  | String     |                                              |
| Type                                | String     |                                              |
| Updated At                          | DateTime   | GREATER_THAN_OR_EQUAL_TO, BETWEEN, LESS_THAN |
| Object Type                         | Created At | String                                       |                       |
| Key                                 | String     |                                              |
| Schema                              | Struct     |                                              |
| Updated At                          | String     |                                              |
| Relationship Type                   | Created At | String                                       |                       |
| Key                                 | String     |                                              |
| Source                              | String     |                                              |
| Target                              | Struct     |                                              |
| Updated At                          | String     |                                              |
| Relationship Type Record            | Created At | String                                       |                       |
| Id                                  | String     |                                              |
| Relationship Type                   | String     |                                              |
| Source                              | String     |                                              |
| Target                              | String     |                                              |
