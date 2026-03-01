# Smartsheet connector for Amazon AppFlow

Smartsheet is a spreadsheet-based online collaboration service that helps teams plan
and track their projects and initiatives. If you're a Smartsheet user, your account
contains data about your sheets, such as their dates when created, dates when modified, owners,
access levels, and more. You can use Amazon AppFlow to transfer data from
Smartsheet to certain AWS services or other supported applications.

## Amazon AppFlow support for Smartsheet

Amazon AppFlow supports Smartsheet as follows.

**Supported as a data source?**
Yes. You can use Amazon AppFlow to transfer data from Smartsheet.

**Supported as a data destination?**
No. You can't use Amazon AppFlow to transfer data to Smartsheet.

## Before you begin

To use Amazon AppFlow to transfer data from Smartsheet to supported destinations, you must meet these
requirements:

- You have an account with Smartsheet that contains the data that you want to transfer. For more
  information about the Smartsheet data objects that Amazon AppFlow supports, see [Supported objects](#smartsheet-objects "#smartsheet-objects").
- In your Smartsheet account, you've created an app for Amazon AppFlow. The app provides the
  client credentials that Amazon AppFlow uses to access your data securely when it makes authenticated
  calls to your account. For the steps to create an app, see [OAuth Walkthrough](https://smartsheet.redoc.ly/#section/OAuth-Walkthrough "https://smartsheet.redoc.ly/#section/OAuth-Walkthrough") in the
  _Smartsheet API Reference (2.0.0)_.
- You've configured the app with one or more redirect URLs for Amazon AppFlow.

Redirect URLs have the following format:

```
https://`region`.console.aws.amazon.com/appflow/oauth
```

In this URL, _region_ is the code for the AWS Region
where you use Amazon AppFlow to transfer data from Smartsheet. For example, the code for the US East (N. Virginia)
Region is `us-east-1`. For that Region, the URL is the following:

```
https://us-east-1.console.aws.amazon.com/appflow/oauth
```

For the AWS Regions that Amazon AppFlow supports, and their codes, see [Amazon AppFlow endpoints and quotas](../../../general/latest/gr/appflow.md "../../../general/latest/gr/appflow.md")
in the _AWS General Reference._

Note the client ID and secret from the settings for your app. You provide these values to
Amazon AppFlow when you connect to your Smartsheet account.

## Connecting Amazon AppFlow to your Smartsheet account

To connect Amazon AppFlow to your Smartsheet account, provide the client credentials from
your app so that Amazon AppFlow can access your data. If you haven't yet configured your
Smartsheet account for Amazon AppFlow integration, see [Before you begin](#smartsheet-prereqs "#smartsheet-prereqs").

###### To connect to Smartsheet

1. Sign in to the AWS Management Console and open the Amazon AppFlow console at [https://console.aws.amazon.com/appflow/](https://console.aws.amazon.com/appflow/ "https://console.aws.amazon.com/appflow/").
2. In the navigation pane on the left, choose **Connections**.
3. On the **Manage connections** page, for **Connectors**,
   choose **Smartsheet**.
4. Choose **Create connection**.
5. In the **Connect to Smartsheet** window, enter the following
   information:
   - **Authorization tokens URL** – Do one of the following:
     - To connect to the Smartsheet US region, choose
       **https://api.smartsheet.com/2.0/token**.
     - To connect to the Smartsheet EU region, choose
       **https://api.smartsheet.eu/2.0/token**.

   - **Authorization code URL** – Do one of the following:
     - To connect to the Smartsheet US region, choose
       **https://api.smartsheet.com/b/authorize**.
     - To connect to the Smartsheet EU region, choose
       **https://api.smartsheet.eu/b/authorize**.

   - **Client ID** – The client ID from app in your
     Smartsheet account.
   - **Client secret** – The client secret from the app in your
     Smartsheet account.
   - **Instance URL** – Do one of the following:
     - To connect to the Smartsheet US region, choose
       **https://api.smartsheet.com**.
     - To connect to the Smartsheet EU region, choose
       **https://api.smartsheet.eu**.

6. Optionally, under **Data encryption**, choose **Customize
   encryption settings (advanced)** if you want to encrypt your data with a customer
   managed key in the AWS Key Management Service (AWS KMS).

By default, Amazon AppFlow encrypts your data with a KMS key that AWS creates, uses, and manages
for you. Choose this option if you want to encrypt your data with your own KMS key instead.

Amazon AppFlow always encrypts your data during transit and at rest. For more information, see
[Data protection in Amazon AppFlow](data-protection.md "data-protection.md").

If you want to use a KMS key from the current AWS account, select this key under
**Choose an AWS KMS key**. If you want to use a KMS key from a different
AWS account, enter the Amazon Resource Name (ARN) for that key. 7. For **Connection name**, enter a name for your connection. 8. Choose **Connect**. 9. In the window that appears, sign in to your Smartsheet account, and grant access to Amazon AppFlow.

On the **Manage connections** page, your new connection appears in the
**Connections** table. When you create a flow
that uses Smartsheet as the data source, you can select this connection.

## Transferring data from Smartsheet with a flow

To transfer data from Smartsheet, create an Amazon AppFlow flow, and choose Smartsheet as the data
source. For the steps to create a flow, see [Creating flows in Amazon AppFlow](create-flow.md "create-flow.md").

When you configure the flow, choose the data object that you want to transfer. For the objects
that Amazon AppFlow supports for Smartsheet, see [Supported objects](#smartsheet-objects "#smartsheet-objects").

Also, choose the destination where you want to transfer the data object that you selected.
For more information about how to configure your destination, see [Supported destinations](#smartsheet-destinations "#smartsheet-destinations").

## Supported destinations

When you create a flow that uses Smartsheet as the data source, you can set the destination to any of the following connectors:

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

When you create a flow that uses SmartSheet as the data source, you can transfer any of the
following data objects to supported destinations:

| **Object**                  | **Field**         | **Data type**            | **Supported filters** |
| --------------------------- | ----------------- | ------------------------ | --------------------- |
| Event                       | Access Token Name | Integer                  |                       |
| Action                      | String            |                          |
| Additional Details          | Struct            |                          |
| Event Id                    | String            |                          |
| Event Timestamp             | DateTime          |                          |
| Object Id                   | String            |                          |
| Object Type                 | String            |                          |
| Request User Id             | Integer           |                          |
| Since                       | DateTime          | GREATER_THAN_OR_EQUAL_TO |
| Source                      | String            |                          |
| User Id                     | Integer           |                          |
| List Sheet                  | Access Level      | String                   |                       |
| Created At                  | DateTime          |                          |
| Id                          | Integer           |                          |
| Modified At                 | DateTime          |                          |
| Modified Since              | DateTime          | GREATER_THAN_OR_EQUAL_TO |
| Name                        | String            |                          |
| Permalink                   | String            |                          |
| Source                      | Struct            |                          |
| Version                     | Integer           |                          |
| Row Metadata                | Access Level      | String                   |                       |
| Attachment                  | List              |                          |
| Column                      | List              |                          |
| Conditional Format          | String            |                          |
| Created At                  | DateTime          |                          |
| Created By                  | Struct            |                          |
| Discussion                  | List              |                          |
| Expanded                    | Boolean           |                          |
| Filter Id                   | String            | EQUAL_TO                 |
| Filtered Out                | Boolean           |                          |
| Format                      | String            |                          |
| Id                          | Integer           |                          |
| In Critical Path            | Boolean           |                          |
| Locked                      | Boolean           |                          |
| Locked For User             | Boolean           |                          |
| Modified At                 | DateTime          |                          |
| Modified By                 | Struct            |                          |
| Permalink                   | String            |                          |
| Proofs                      | Struct            |                          |
| Row Number                  | Integer           |                          |
| Rows Modified Since         | DateTime          | GREATER_THAN             |
| Sheet Id                    | Integer           |                          |
| Sibling Id                  | Integer           |                          |
| Total Row Count             | Integer           |                          |
| Version                     | Integer           |                          |
| Sheet Data                  |                   |                          |                       |
| Sheet Metadata              | Access Level      | String                   |                       |
| Attachment                  | List              |                          |
| Cell Image Upload Enabled   | Boolean           |                          |
| Column                      | List              |                          |
| Created At                  | DateTime          |                          |
| Cross Sheet Reference       | List              |                          |
| Dependencies Enabled        | Boolean           |                          |
| Discussion                  | List              |                          |
| Effective Attachment Option | List              |                          |
| Favorite                    | Boolean           |                          |
| Filter                      | List              |                          |
| From Id                     | Integer           |                          |
| Gantt Config                | Struct            |                          |
| Gantt Enabled               | Boolean           |                          |
| Has Summary Field           | Boolean           |                          |
| Id                          | Integer           |                          |
| Is Multi Picklist Enabled   | Boolean           |                          |
| Modified At                 | DateTime          |                          |
| Name                        | String            |                          |
| Owner                       | String            |                          |
| Owner Id                    | Integer           |                          |
| Permalink                   | String            |                          |
| Project Setting             | Struct            |                          |
| Read Only                   | Boolean           |                          |
| Resource Management Enabled | Boolean           |                          |
| Resource Management Type    | String            |                          |
| Show Parent Rows For Filter | Boolean           |                          |
| Source                      | Struct            |                          |
| Summary                     | Struct            |                          |
| Total Row Count             | Integer           |                          |
| User Permission             | Struct            |                          |
| User Setting                | Struct            |                          |
| Version                     | Integer           |                          |
| Workspace                   | Struct            |                          |
