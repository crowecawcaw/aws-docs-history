# Mailchimp connector for Amazon AppFlow

Mailchimp is a marketing automation platform and email marketing service. If you're
a Mailchimp user, your account contains data about your email campaigns, such as open and
click details, segments, and automations. You can use Amazon AppFlow to transfer data from
Mailchimp to certain AWS services or other supported applications.

## Amazon AppFlow support for Mailchimp

Amazon AppFlow supports Mailchimp as follows.

**Supported as a data source?**
Yes. You can use Amazon AppFlow to transfer data from Mailchimp.

**Supported as a data destination?**
No. You can't use Amazon AppFlow to transfer data to Mailchimp.

## Before you begin

To use Amazon AppFlow to transfer data from Mailchimp to supported destinations, you must meet these
requirements:

- You have an account with Mailchimp that contains the data that you want to transfer. For more
  information about the Mailchimp data objects that Amazon AppFlow supports, see [Supported objects](#mailchimp-objects "#mailchimp-objects").
- In your account, you've created an API key. For the steps to create one, see [About API Keys](https://mailchimp.com/help/about-api-keys/ "https://mailchimp.com/help/about-api-keys/") in the
  Mailchimp Help Center.

Note the API key from your account settings. You provide it to Amazon AppFlow when you connect to
your Mailchimp account.

## Connecting Amazon AppFlow to your Mailchimp account

To connect Amazon AppFlow to your Mailchimp account, provide your API key so that Amazon AppFlow
can access your data. If you haven't yet configured your Mailchimp account for Amazon AppFlow
integration, see [Before you begin](#mailchimp-prereqs "#mailchimp-prereqs").

###### To connect to Mailchimp

1. Sign in to the AWS Management Console and open the Amazon AppFlow console at [https://console.aws.amazon.com/appflow/](https://console.aws.amazon.com/appflow/ "https://console.aws.amazon.com/appflow/").
2. In the navigation pane on the left, choose **Connections**.
3. On the **Manage connections** page, for **Connectors**,
   choose **Mailchimp**.
4. Choose **Create connection**.
5. In the **Connect to Mailchimp** window, enter the following
   information:
   - **API Key** – The API key from your Mailchimp account
     settings.
   - **Instance URL** – The Mailchimp Marketing API URL that
     provides access to your Mailchimp data. These URLs have the form
     `https://`data-center`.api.mailchimp.com`,
     where _data-center_ is the data center for your
     account. For more information, see API structure in the
     Mailchimp Marketing API documentation.

6. Optionally, under **Data encryption**, choose **Customize
   encryption settings (advanced)** if you want to encrypt your data with a customer
   managed key in the AWS Key Management Service (AWS KMS).

By default, Amazon AppFlow encrypts your data with a KMS key that AWS creates, uses, and manages
for you. Choose this option if you want to encrypt your data with your own KMS key instead.

Amazon AppFlow always encrypts your data during transit and at rest. For more information, see
[Data protection in Amazon AppFlow](data-protection.md "data-protection.md").

If you want to use a KMS key from the current AWS account, select this key under
**Choose an AWS KMS key**. If you want to use a KMS key from a different
AWS account, enter the Amazon Resource Name (ARN) for that key. 7. For **Connection name**, enter a name for your connection. 8. Choose **Connect**.

On the **Manage connections** page, your new connection appears in the
**Connections** table. When you create a flow
that uses Mailchimp as the data source, you can select this connection.

## Transferring data from Mailchimp with a flow

To transfer data from Mailchimp, create an Amazon AppFlow flow, and choose Mailchimp as the data
source. For the steps to create a flow, see [Creating flows in Amazon AppFlow](create-flow.md "create-flow.md").

When you configure the flow, choose the data object that you want to transfer. For the objects
that Amazon AppFlow supports for Mailchimp, see [Supported objects](#mailchimp-objects "#mailchimp-objects").

Also, choose the destination where you want to transfer the data object that you selected.
For more information about how to configure your destination, see [Supported destinations](#mailchimp-destinations "#mailchimp-destinations").

## Supported destinations

When you create a flow that uses Mailchimp as the data source, you can set the destination to any of the following connectors:

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

When you create a flow that uses Mailchimp as the data source, you can transfer any of the
following data objects to supported destinations:

| **Object**              | **Field**      | **Data type**           | **Supported filters**   |
| ----------------------- | -------------- | ----------------------- | ----------------------- |
| Abuse Report            | Campaign ID    | String                  |                         |
| Date                    | String         |                         |
| Email Address           | String         |                         |
| Email ID                | String         |                         |
| ID                      | Integer        |                         |
| List ID                 | String         |                         |
| List Is Active          | Boolean        |                         |
| Merge Field             | Struct         |                         |
| Vip                     | Boolean        |                         |
| Automation              | Create Time    | DateTime                | LESS_THAN, GREATER_THAN |
| Email Sent              | Integer        |                         |
| ID                      | String         |                         |
| Recipient               | Struct         |                         |
| Report Summary          | Struct         |                         |
| Setting                 | Struct         |                         |
| Start Time              | DateTime       | LESS_THAN, GREATER_THAN |
| Status                  | String         | EQUAL_TO                |
| Tracking                | Struct         |                         |
| Trigger Setting         | Struct         |                         |
| Campaign                | Ab Split Opts  | Struct                  |                         |
| Archive Url             | String         |                         |
| Content Type            | String         |                         |
| Create Time             | DateTime       | LESS_THAN, GREATER_THAN |
| Delivery Status         | Struct         |                         |
| Email Sent              | Integer        |                         |
| Folder ID               | String         | EQUAL_TO                |
| ID                      | String         |                         |
| List ID                 | String         | EQUAL_TO                |
| Long Archive Url        | String         |                         |
| Member ID               | String         | EQUAL_TO                |
| Need Block Refresh      | Boolean        |                         |
| Parent Campaign ID      | String         |                         |
| Recipient               | Struct         |                         |
| Report Summary          | Struct         |                         |
| Resendable              | Boolean        |                         |
| Rss Opts                | Struct         |                         |
| Send Time               | DateTime       | LESS_THAN, GREATER_THAN |
| Setting                 | Struct         |                         |
| Social Card             | Struct         |                         |
| Sort Field              | String         | EQUAL_TO                |
| Status                  | String         | EQUAL_TO                |
| Tracking                | Struct         |                         |
| Type                    | String         | EQUAL_TO                |
| Variate Settings        | Struct         |                         |
| Web ID                  | Integer        |                         |
| Click Detail            | Ab Split       | Struct                  |                         |
| Campaign ID             | String         |                         |
| Click Percentage        | Float          |                         |
| ID                      | String         |                         |
| Last Click              | String         |                         |
| Total Click             | Integer        |                         |
| Unique Click            | Integer        |                         |
| Unique Click Percentage | Float          |                         |
| Url                     | String         |                         |
| List                    | Beamer Address | String                  |                         |
| Campaign Default        | Struct         |                         |
| Campaign Last Sent      | DateTime       | LESS_THAN, GREATER_THAN |
| Contact                 | Struct         |                         |
| Date Created            | DateTime       | LESS_THAN, GREATER_THAN |
| Double Optin            | Boolean        |                         |
| Email                   | String         | EQUAL_TO                |
| Email Type Option       | Boolean        |                         |
| Has Ecommerce Store     | Boolean        | EQUAL_TO                |
| Has Welcome             | Boolean        |                         |
| ID                      | String         |                         |
| Include Total Contact   | Boolean        | EQUAL_TO                |
| List Rating             | Integer        |                         |
| Marketing Permission    | Boolean        |                         |
| Module                  | Struct         |                         |
| Name                    | String         |                         |
| Notify On Subscribe     | String         |                         |
| Notify On Unsubscribe   | String         |                         |
| Permission Reminder     | String         |                         |
| Sort Field              | String         | EQUAL_TO                |
| Stats                   | Struct         |                         |
| Subscribe Url Short     | String         |                         |
| Use Archive Bar         | Boolean        |                         |
| Visibility              | String         |                         |
| Web_ID                  | Integer        |                         |
| subscribe Url Long      | String         |                         |
| Open Detail             | Campaign ID    | String                  |                         |
| Contact Status          | String         |                         |
| Email Address           | String         |                         |
| Email ID                | String         |                         |
| List ID                 | String         |                         |
| List is Active          | Boolean        |                         |
| Merge Field             | Struct         |                         |
| Open                    | Struct         |                         |
| Open Count              | Integer        |                         |
| Since                   | DateTime       | EQUAL_TO                |
| Vip                     | Boolean        |                         |
| Segment                 | Created At     | DateTime                | LESS_THAN, GREATER_THAN |
| ID                      | Integer        |                         |
| Include Cleaned         | Boolean        | EQUAL_TO                |
| Include Unsubscribed    | Boolean        | EQUAL_TO                |
| List ID                 | String         |                         |
| Member Count            | Integer        |                         |
| Name                    | String         |                         |
| Option                  | Struct         |                         |
| Type                    | String         | EQUAL_TO                |
| Updated At              | DateTime       | LESS_THAN, GREATER_THAN |
| Segment Member          | Email Address  | String                  |                         |
| Email Client            | String         |                         |
| Email Type              | String         |                         |
| ID                      | String         |                         |
| Include Cleaned         | Boolean        | EQUAL_TO                |
| Include Unsubscribed    | Boolean        | EQUAL_TO                |
| Interest                | Struct         |                         |
| Ip Opt                  | String         |                         |
| Ip Signup               | String         |                         |
| Language                | String         |                         |
| Last Changed            | String         |                         |
| Last Note               | Struct         |                         |
| List ID                 | String         |                         |
| Location                | Struct         |                         |
| Member Rating           | Integer        |                         |
| Merge Field             | Struct         |                         |
| Stats                   | Struct         |                         |
| Status                  | String         |                         |
| Timestamp Opt           | String         |                         |
| Timestamp Signup        | String         |                         |
| Unique Email ID         | String         |                         |
| Vip                     | Boolean        |                         |
| Store                   | Address        | Struct                  |                         |
| Automation              | Struct         |                         |
| Connected Site          | Struct         |                         |
| Created At              | String         |                         |
| Currency Code           | String         |                         |
| Domain                  | String         |                         |
| Email Address           | String         |                         |
| ID                      | String         |                         |
| Is Syncing              | Boolean        |                         |
| List ID                 | String         |                         |
| List Is Active          | Boolean        |                         |
| Money Format            | String         |                         |
| Name                    | String         |                         |
| Phone                   | String         |                         |
| Platform                | String         |                         |
| Primary Locale          | String         |                         |
| Timezone                | String         |                         |
| Updated At              | String         |                         |
| Unsubscribed            | Campaign ID    | String                  |                         |
| Email Address           | String         |                         |
| Email ID                | String         |                         |
| List ID                 | String         |                         |
| List Is Active          | Boolean        |                         |
| Merge Field             | Struct         |                         |
| Reason                  | String         |                         |
| Timestamp               | String         |                         |
| Vip                     | Boolean        |                         |
