# Snapchat Ads connector for Amazon AppFlow

You can use the Snapchat Ads connector in Amazon AppFlow to transfer data about the ads that
you run on Snapchat. After you connect Amazon AppFlow to your ad account with Snapchat business, you can
transfer data about your ads, campaigns, customer segments, and more. You can transfer this data
to certain AWS services or other supported applications.

## Amazon AppFlow support for Snapchat Ads

Amazon AppFlow supports Snapchat Ads as follows.

**Supported as a data source?**
Yes. You can use Amazon AppFlow to transfer data from Snapchat Ads.

**Supported as a data destination?**
No. You can't use Amazon AppFlow to transfer data to Snapchat Ads.

## Before you begin

To use Amazon AppFlow to transfer data from Snapchat Ads to supported destinations, you must meet these
requirements:

- You have a Snapchat business account, and you've used it to create an ad account. The ad
  account contains the data that you want to transfer with Amazon AppFlow. For more information about ad
  accounts, see [Create an
  Ad Account](https://businesshelp.snapchat.com/s/article/create-ad-account?language=en_US "https://businesshelp.snapchat.com/s/article/create-ad-account?language=en_US") in the Snapchat Business Help Center.
- In your Snapchat account, you've created an OAuth app for Amazon AppFlow. The app provides the
  credentials that Amazon AppFlow uses to access your data securely when it makes authenticated calls to
  your account. For the steps to create an app, see [Activate Access to
  the Snapchat Marketing API](https://businesshelp.snapchat.com/s/article/api-apply?language=en_US "https://businesshelp.snapchat.com/s/article/api-apply?language=en_US") in the Snapchat Business Help Center.
- You've configured the OAuth app with one or more redirect URLs for Amazon AppFlow.

Redirect URLs have the following format:

```
https://`region`.console.aws.amazon.com/appflow/oauth
```

In this URL, _region_ is the code for the AWS Region
where you use Amazon AppFlow to transfer data from Snapchat Ads. For example, the code for the US East (N. Virginia)
Region is `us-east-1`. For that Region, the URL is the following:

```
https://us-east-1.console.aws.amazon.com/appflow/oauth
```

For the AWS Regions that Amazon AppFlow supports, and their codes, see [Amazon AppFlow endpoints and quotas](../../../general/latest/gr/appflow.md "../../../general/latest/gr/appflow.md")
in the _AWS General Reference._

From the OAuth app settings, note the values for Snap client ID and Snap client secret key.
You provide these values to Amazon AppFlow when you connect to your Snapchat account.

## Connecting Amazon AppFlow to your Snapchat Ads account

To connect Amazon AppFlow to Snapchat Ads, provide the credentials from the OAuth app in your
Snapchat account so that Amazon AppFlow can access your data. If you haven't yet configured your Snapchat
account for Amazon AppFlow integration, see [Before you begin](#snapchat-ads-prereqs "#snapchat-ads-prereqs").

###### To connect to Snapchat Ads

1. Sign in to the AWS Management Console and open the Amazon AppFlow console at [https://console.aws.amazon.com/appflow/](https://console.aws.amazon.com/appflow/ "https://console.aws.amazon.com/appflow/").
2. In the navigation pane on the left, choose **Connections**.
3. On the **Manage connections** page, for **Connectors**,
   choose **Snapchat Ads**.
4. Choose **Create connection**.
5. In the **Connect to Snapchat Ads** window, enter the following
   information:
   - **Client ID** — The Snap client ID from your OAuth app.
   - **Client secret** — The Snap client secret key from your OAuth
     app.

6. Optionally, under **Data encryption**, choose **Customize
   encryption settings (advanced)** if you want to encrypt your data with a customer
   managed key in the AWS Key Management Service (AWS KMS).

By default, Amazon AppFlow encrypts your data with a KMS key that AWS creates, uses, and manages
for you. Choose this option if you want to encrypt your data with your own KMS key instead.

Amazon AppFlow always encrypts your data during transit and at rest. For more information, see
[Data protection in Amazon AppFlow](data-protection.md "data-protection.md").

If you want to use a KMS key from the current AWS account, select this key under
**Choose an AWS KMS key**. If you want to use a KMS key from a different
AWS account, enter the Amazon Resource Name (ARN) for that key. 7. For **Connection name**, enter a name for your connection. 8. Choose **Connect**. 9. In the window that appears, sign in to your Snapchat account, and grant access to
Amazon AppFlow.

On the **Manage connections** page, your new connection appears in the
**Connections** table. When you create a flow
that uses Snapchat Ads as the data source, you can select this connection.

## Transferring data from Snapchat Ads with a flow

To transfer data from Snapchat Ads, create an Amazon AppFlow flow, and choose Snapchat Ads as the data
source. For the steps to create a flow, see [Creating flows in Amazon AppFlow](create-flow.md "create-flow.md").

When you configure the flow, choose the data object that you want to transfer. For the objects
that Amazon AppFlow supports for Snapchat Ads, see [Supported objects](#snapchat-ads-objects "#snapchat-ads-objects").

Also, choose the destination where you want to transfer the data object that you selected.
For more information about how to configure your destination, see [Supported destinations](#snapchat-ads-destinations "#snapchat-ads-destinations").

## Supported destinations

When you create a flow that uses Snapchat Ads as the data source, you can set the destination to any of the following connectors:

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

When you create a flow that uses Snapchat Ads as the data source, you can transfer any of the
following data objects to supported destinations:

| **Object**                      | **Field**             | **Data type** | **Supported filters** |
| ------------------------------- | --------------------- | ------------- | --------------------- |
| Ad Account                      | Advertiser            | String        |                       |
| Advertiser Organization Id      | String                |               |
| Agency Representing Client      | Boolean               |               |
| Billing Center Id               | String                |               |
| Billing Type                    | String                |               |
| Client Paying Invoices          | Boolean               |               |
| Created At                      | DateTime              |               |
| Currency                        | String                |               |
| Funding Source Ids              | List                  |               |
| Id                              | String                |               |
| Lifetime Spend Cap Micro        | Long                  |               |
| Name                            | String                |               |
| Organization Id                 | String                |               |
| Status                          | String                |               |
| Timezone                        | String                |               |
| Type                            | String                |               |
| Update At                       | DateTime              |               |
| Ad Squad                        | Auto Bid              | Boolean       |                       |
| Bid Micro                       | Long                  |               |
| Bid Strategy                    | String                |               |
| Billing Event                   | String                |               |
| Campaign Id                     | String                |               |
| Created At                      | DateTime              |               |
| Creation State                  | String                |               |
| Daily Budget Micro              | Long                  |               |
| Deleted                         | Boolean               |               |
| Delivery Constraint             | String                |               |
| Delivery Status                 | List                  |               |
| Id                              | String                |               |
| Name                            | String                |               |
| Optimization Goal               | String                |               |
| Pacing Type                     | String                |               |
| Placement V2                    | Struct                |               |
| Read Deleted Entities           | Boolean               | EQUAL_TO      |
| Skadnetwork Properties          | Struct                |               |
| Start Time                      | DateTime              |               |
| Status                          | String                |               |
| Target Bid                      | Boolean               |               |
| Targeting                       | Struct                |               |
| Targeting Reach Status          | String                |               |
| Type                            | String                |               |
| Update At                       | DateTime              |               |
| Ad Under Ad Account             | Ad Squad Id           | String        |                       |
| Created At                      | DateTime              |               |
| Creative Id                     | String                |               |
| Deleted                         | Boolean               |               |
| Delivery Status                 | List                  |               |
| Id                              | String                |               |
| Name                            | String                |               |
| Read Deleted Entities           | Boolean               | EQUAL_TO      |
| Render Type                     | String                |               |
| Review Status                   | String                |               |
| Review Status Reasons           | List                  |               |
| Status                          | String                |               |
| Type                            | String                |               |
| Update At                       | DateTime              |               |
| Ad Under Campaign               | Ad Squad Id           | String        |                       |
| Approval Type                   | String                |               |
| Created At                      | DateTime              |               |
| Creative Id                     | String                |               |
| Delivery Status                 | List                  |               |
| Id                              | String                |               |
| Name                            | String                |               |
| Render Type                     | String                |               |
| Review Status                   | String                |               |
| Review Status Reasons           | List                  |               |
| Status                          | String                |               |
| Type                            | String                |               |
| Update At                       | DateTime              |               |
| Campaign                        | Ad Account Id         | String        |                       |
| Created At                      | DateTime              |               |
| Daily Budget Micro              | Long                  |               |
| Deleted                         | Boolean               |               |
| Delivery Status                 | List                  |               |
| End Time                        | DateTime              |               |
| Id                              | String                |               |
| Name                            | String                |               |
| Objective                       | String                |               |
| Read Deleted Entities           | Boolean               | EQUAL_TO      |
| Start Time                      | DateTime              |               |
| Status                          | String                |               |
| Update At                       | DateTime              |               |
| Creative                        | Ad Account Id         | String        |                       |
| Ad Product                      | String                |               |
| Brand Name                      | String                |               |
| Call To Action                  | String                |               |
| Created At                      | DateTime              |               |
| Headline                        | String                |               |
| Id                              | String                |               |
| Longform Video Properties       | Struct                |               |
| Name                            | String                |               |
| Packaging Status                | String                |               |
| Render Type                     | String                |               |
| Review Status                   | String                |               |
| Shareable                       | Boolean               |               |
| Top Snap Crop Position          | String                |               |
| Top Snap Media Id               | String                |               |
| Type                            | String                |               |
| Update At                       | DateTime              |               |
| Media                           | Ad Account Id         | String        |                       |
| Created At                      | DateTime              |               |
| File Name                       | String                |               |
| Id                              | String                |               |
| Is Demo Media                   | Boolean               |               |
| Media Status                    | String                |               |
| Name                            | String                |               |
| Type                            | String                |               |
| Update At                       | DateTime              |               |
| Visibility                      | String                |               |
| Organization                    | Accepted Term Version | String        |                       |
| Ad Accounts                     | List                  |               |
| Address Line 1                  | String                |               |
| Administrative District Level 1 | String                |               |
| Business Type                   | String                |               |
| Configuration Settings          | Struct                |               |
| Contact Email                   | String                |               |
| Contact Name                    | String                |               |
| Contact Phone                   | String                |               |
| Contact Phone Optin             | Boolean               |               |
| Country                         | String                |               |
| Created At                      | DateTime              |               |
| Id                              | String                |               |
| Is Agency                       | Boolean               |               |
| Locality                        | String                |               |
| Marketing Optin                 | Boolean               |               |
| My Display Name                 | String                |               |
| My Invited Email                | String                |               |
| My Member Id                    | String                |               |
| Name                            | String                |               |
| Postal Code                     | String                |               |
| Roles                           | List                  |               |
| State                           | String                |               |
| Tax Type                        | String                |               |
| Type                            | String                |               |
| Update At                       | DateTime              |               |
| created By Caller               | Boolean               |               |
| Segment                         | Ad Account Id         | String        |                       |
| Approximate Number Users        | Integer               |               |
| Created At                      | DateTime              |               |
| Description                     | String                |               |
| Id                              | String                |               |
| Name                            | String                |               |
| Retention In Days               | Integer               |               |
| Source Type                     | String                |               |
| Status                          | String                |               |
| Targetable Status               | String                |               |
| Update At                       | DateTime              |               |
| Upload Status                   | String                |               |
| Visible To                      | List                  |               |
| organization Id                 | String                |               |
