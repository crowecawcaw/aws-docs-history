# Productboard connector for Amazon AppFlow

Productboard is a product management solution. If you're a Productboard user,
your account contains data about the projects in your roadmap, such as products, features, and
status. You can use Amazon AppFlow to transfer data from
Productboard to certain AWS services or other supported applications.

## Amazon AppFlow support for Productboard

Amazon AppFlow supports Productboard as follows.

**Supported as a data source?**
Yes. You can use Amazon AppFlow to transfer data from Productboard.

**Supported as a data destination?**
No. You can't use Amazon AppFlow to transfer data to Productboard.

## Before you begin

To use Amazon AppFlow to transfer data from Productboard to supported destinations, you must
have an account with Productboard that contains the data that you want to transfer.

From the Public API settings in your account, note the access token because you provide this
value to Amazon AppFlow when you connect to Productboard. For the steps to get the token, see
[Public API Access Token](https://developer.productboard.com/#section/Authentication/Public-API-Access-Token "https://developer.productboard.com/#section/Authentication/Public-API-Access-Token") in the Productboard API Reference.

## Connecting Amazon AppFlow to your Productboard account

To connect Amazon AppFlow to your Productboard account, provide the access token from your
account settings so that Amazon AppFlow can access your data.

###### To connect to Productboard

1. Sign in to the AWS Management Console and open the Amazon AppFlow console at [https://console.aws.amazon.com/appflow/](https://console.aws.amazon.com/appflow/ "https://console.aws.amazon.com/appflow/").
2. In the navigation pane on the left, choose **Connections**.
3. On the **Manage connections** page, for **Connectors**,
   choose **Productboard**.
4. Choose **Create connection**.
5. In the **Connect to Productboard** window, for **Access
   Token**, enter your access token.
6. Optionally, under **Data encryption**, choose **Customize
   encryption settings (advanced)** if you want to encrypt your data with a customer
   managed key in the AWS Key Management Service (AWS KMS).

By default, Amazon AppFlow encrypts your data with a KMS key that AWS creates, uses, and manages
for you. Choose this option if you want to encrypt your data with your own KMS key instead.

Amazon AppFlow always encrypts your data during transit and at rest. For more information, see
[Data protection in Amazon AppFlow](data-protection.md "data-protection.md").

If you want to use a KMS key from the current AWS account, select this key under
**Choose an AWS KMS key**. If you want to use a KMS key from a different
AWS account, enter the Amazon Resource Name (ARN) for that key. 7. Choose **Connect**.

On the **Manage connections** page, your new connection appears in the
**Connections** table. When you create a flow
that uses Productboard as the data source, you can select this connection.

## Transferring data from Productboard with a flow

To transfer data from Productboard, create an Amazon AppFlow flow, and choose Productboard as the data
source. For the steps to create a flow, see [Creating flows in Amazon AppFlow](create-flow.md "create-flow.md").

When you configure the flow, choose the data object that you want to transfer. For the objects
that Amazon AppFlow supports for Productboard, see [Supported objects](#productboard-objects "#productboard-objects").

Also, choose the destination where you want to transfer the data object that you selected.
For more information about how to configure your destination, see [Supported destinations](#productboard-destinations "#productboard-destinations").

## Supported destinations

When you create a flow that uses Productboard as the data source, you can set the destination to any of the following connectors:

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

When you create a flow that uses Productboard as the data source, you can transfer any of the
following data objects to supported destinations:

| **Object**              | **Field** | **Data type** | **Supported filters** |
| ----------------------- | --------- | ------------- | --------------------- |
| Component               | CreatedAt | String        |                       |
| Description             | String    |               |
| Id                      | String    |               |
| Links                   | Struct    |               |
| Name                    | String    |               |
| Owner                   | Struct    |               |
| Parent                  | Struct    |               |
| UpdatedAt               | String    |               |
| Custom Field Definition |           |               |                       |
| Custom Field Value      |           |               |                       |
| Feature                 | Archived  | Boolean       | EQUAL_TO              |
| CreatedAt               | String    |               |
| Description             | String    |               |
| Id                      | String    |               |
| Links                   | Struct    |               |
| Name                    | String    |               |
| Owner                   | Struct    |               |
| Owner Email             | String    | EQUAL_TO      |
| Parent                  | Struct    |               |
| Parent Id               | String    | EQUAL_TO      |
| Status                  | Struct    |               |
| Status Id               | String    | EQUAL_TO      |
| Status Name             | String    | EQUAL_TO      |
| Time Frame              | Struct    |               |
| Type                    | String    |               |
| UpdatedAt               | String    |               |
| Feature status          | Completed | Boolean       |                       |
| Id                      | String    |               |
| Name                    | String    |               |
| Product                 | CreatedAt | String        |                       |
| Description             | String    |               |
| Id                      | String    |               |
| Links                   | Struct    |               |
| Name                    | String    |               |
| Owner                   | Struct    |               |
| UpdatedAt               | String    |               |
