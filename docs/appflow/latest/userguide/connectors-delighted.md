# Delighted connector for Amazon AppFlow

Delighted is a cloud-based survey tool that helps its users distribute surveys and
then collect and analyze the feedback. If you're a Delighted user, then your account
contains data about your survey responses. You can use Amazon AppFlow to transfer data from
Delighted to certain AWS services or other supported applications.

## Amazon AppFlow support for Delighted

Amazon AppFlow supports Delighted as follows.

**Supported as a data source?**
Yes. You can use Amazon AppFlow to transfer data from Delighted.

**Supported as a data destination?**
No. You can't use Amazon AppFlow to transfer data to Delighted.

## Before you begin

To use Amazon AppFlow to transfer data from Delighted to supported destinations, you must
have an account with Delighted that contains the data that you want to transfer. For
more information about the Delighted data objects that Amazon AppFlow supports, see [Supported objects](#delighted-objects "#delighted-objects").

From your account settings, note the API key. You provide this value to Amazon AppFlow when you
create a connection to your Delighted account. For more information about
Delighted API keys, see [Authentication](https://app.delighted.com/docs/api?gclid=Cj0KCQiAq5meBhCyARIsAJrtdr7AtSu0W6hS8OmoyWdqLMzzNUNTd9TQ8DoGMwsRitprPQrZNCMXZ-gaAqbDEALw_wcB#authentication "https://app.delighted.com/docs/api?gclid=Cj0KCQiAq5meBhCyARIsAJrtdr7AtSu0W6hS8OmoyWdqLMzzNUNTd9TQ8DoGMwsRitprPQrZNCMXZ-gaAqbDEALw_wcB#authentication") in the Delighted API documentation.

## Connecting Amazon AppFlow to your Delighted account

To connect Amazon AppFlow to your Delighted account, provide the API key from your Delighted
account settings so that Amazon AppFlow can access your data.

###### To connect to Delighted

1. Sign in to the AWS Management Console and open the Amazon AppFlow console at [https://console.aws.amazon.com/appflow/](https://console.aws.amazon.com/appflow/ "https://console.aws.amazon.com/appflow/").
2. In the navigation pane on the left, choose **Connections**.
3. On the **Manage connections** page, for **Connectors**,
   choose **Delighted**.
4. Choose **Create connection**.
5. In the **Connect to Delighted** window, for **API
   Key**, enter a test or live API key from your Delighted account.
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
that uses Delighted as the data source, you can select this connection.

## Transferring data from Delighted with a flow

To transfer data from Delighted, create an Amazon AppFlow flow, and choose Delighted as the data
source. For the steps to create a flow, see [Creating flows in Amazon AppFlow](create-flow.md "create-flow.md").

When you configure the flow, choose the data object that you want to transfer. For the objects
that Amazon AppFlow supports for Delighted, see [Supported objects](#delighted-objects "#delighted-objects").

Also, choose the destination where you want to transfer the data object that you selected.
For more information about how to configure your destination, see [Supported destinations](#delighted-destinations "#delighted-destinations").

## Supported destinations

When you create a flow that uses Delighted as the data source, you can set the destination to any of the following connectors:

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

When you create a flow that uses Delighted as the data source, you can transfer any of the
following data objects to supported destinations:

| **Object**                  | **Field**           | **Data type** | **Supported filters** |
| --------------------------- | ------------------- | ------------- | --------------------- |
| Bounce                      | bounced\_at         | DateTime      |                       |
| email                       | String              |               |
| name                        | String              |               |
| person\_id                  | String              |               |
| since                       | DateTime            | EQUAL\_TO     |
| until                       | DateTime            | EQUAL\_TO     |
| Metric                      | detractor\_count    | Integer       |                       |
| detractor\_percent          | Double              |               |
| nps                         | Integer             |               |
| passive\_count              | Integer             |               |
| passive\_percent            | Double              |               |
| promoter\_count             | Integer             |               |
| promoter\_percent           | Double              |               |
| response\_count             | Integer             |               |
| since                       | DateTime            | EQUAL\_TO     |
| trend                       | String              | EQUAL\_TO     |
| until                       | DateTime            | EQUAL\_TO     |
| People                      | created\_at         | DateTime      |                       |
| email                       | String              | EQUAL\_TO     |
| id                          | String              |               |
| last\_responded\_at         | DateTime            |               |
| last\_sent\_at              | DateTime            |               |
| name                        | String              |               |
| next\_survey\_scheduled\_at | DateTime            |               |
| phone\_number               | String              | EQUAL\_TO     |
| since                       | DateTime            | EQUAL\_TO     |
| until                       | DateTime            | EQUAL\_TO     |
| Survey Response             | additional\_answers | List          |                       |
| comment                     | String              |               |
| created\_at                 | DateTime            |               |
| id                          | String              |               |
| notes                       | List                |               |
| order                       | String              | EQUAL\_TO     |
| permalink                   | String              |               |
| person                      | String              |               |
| person\_email               | String              | EQUAL\_TO     |
| person\_id                  | String              | EQUAL\_TO     |
| person\_properties          | Struct              |               |
| score                       | Integer             |               |
| since                       | DateTime            | EQUAL\_TO     |
| survey\_type                | String              |               |
| tags                        | List                |               |
| trend                       | String              | EQUAL\_TO     |
| until                       | DateTime            | EQUAL\_TO     |
| updated\_at                 | DateTime            |               |
| updated\_since              | DateTime            | EQUAL\_TO     |
| updated\_until              | DateTime            | EQUAL\_TO     |
| Unsubscribe                 | email               | String        |                       |
| name                        | String              |               |
| person\_id                  | String              |               |
| since                       | DateTime            | EQUAL\_TO     |
| unsubscribed\_at            | DateTime            |               |
| until                       | DateTime            | EQUAL\_TO     |
