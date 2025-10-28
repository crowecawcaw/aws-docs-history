# Freshsales connector for Amazon AppFlow

Freshsales is a Customer Relationship Management (CRM) service that helps companies
leverage customer data and interactions. If you’re a Freshsales user, your account
contains information about communication, timelines, meetings, chats, workflows, and more. You
can use Amazon AppFlow to transfer data from Freshsales to certain AWS services or other supported
applications.

## Amazon AppFlow support for Freshsales

Amazon AppFlow supports Freshsales as follows.

**Supported as a data source?**
Yes. You can use Amazon AppFlow to transfer data from Freshsales.

**Supported as a data destination?**
No. You can't use Amazon AppFlow to transfer data to Freshsales.

## Before you begin

To use Amazon AppFlow to transfer data from Freshsales to supported destinations, you must
have an account with Freshsales that contains the data that you want to transfer. For
more information about the Freshsales data objects that Amazon AppFlow supports, see [Supported objects](#freshsales-objects "#freshsales-objects").

From the API settings of your Freshsales account, note the value of your API key.
When you connect to your Freshsales account, you provide this value to Amazon AppFlow. For
more information, see [How to find my API key?](https://support.freshsales.io/en/support/solutions/articles/220099-how-to-find-my-api-key- "https://support.freshsales.io/en/support/solutions/articles/220099-how-to-find-my-api-key-") on the Freshsales support site.

## Connecting Amazon AppFlow

to your Freshsales account

To connect Amazon AppFlow to your Freshsales account,
provide details from your Freshsales project so that Amazon AppFlow can access your data. If you
haven't yet configured your Freshsales project for Amazon AppFlow integration, see [Before you begin](#freshsales-prereqs "#freshsales-prereqs").

###### To connect to Freshsales

1. Sign in to the AWS Management Console and open the Amazon AppFlow console at [https://console.aws.amazon.com/appflow/](https://console.aws.amazon.com/appflow/ "https://console.aws.amazon.com/appflow/").
2. In the navigation pane on the left, choose **Connections**.
3. On the **Manage connections** page, for **Connectors**,
   choose **Freshsales**.
4. Choose **Create connection**.
5. In the **Connect to Freshsales**
   window, enter the following information:
   - **API key** – Enter the word **token** in this
     field.
   - **API secret key** – Enter your secret key. This is named “Your
     API Key” in the Freshsales console, for example,
     **sfg999666t673t7t82**.
   - **Instance URL** – Enter the URL for your Freshsales
     instance, for example,
     https://my-freshsales-instance.myfreshworks.com/crm1/sales.

6. Optionally, under **Data encryption**, choose **Customize
   encryption settings (advanced)** if you want to encrypt your data with a customer
   managed key in the AWS Key Management Service (AWS KMS).

By default, Amazon AppFlow encrypts your data with a KMS key that AWS creates, uses, and manages
for you. Choose this option if you want to encrypt your data with your own KMS key instead.

Amazon AppFlow always encrypts your data during transit and at rest. For more information, see
[Data protection in Amazon AppFlow](data-protection.md "data-protection.md").

If you want to use a KMS key from the current AWS account, select this key under
**Choose an AWS KMS key**. If you want to use a KMS key from a different
AWS account, enter the Amazon Resource Name (ARN) for that key. 7. For **Connection name**, enter a name for your connection. 8. Choose **Connect**. 9. In the window that appears, sign in to your Freshsales account, and grant access
to Amazon AppFlow.

On the **Manage connections** page, your new connection appears in the
**Connections** table. When you create a flow
that uses Freshsales as the data source, you can select this connection.

## Transferring data from Freshsales with a flow

To transfer data from Freshsales, create an Amazon AppFlow flow, and choose Freshsales as the data
source. For the steps to create a flow, see [Creating flows in Amazon AppFlow](create-flow.md "create-flow.md").

When you configure the flow, choose the data object that you want to transfer. For the objects
that Amazon AppFlow supports for Freshsales, see [Supported objects](#freshsales-objects "#freshsales-objects").

Also, choose the destination where you want to transfer the data object that you selected.
For more information about how to configure your destination, see [Supported destinations](#freshsales-destinations "#freshsales-destinations").

## Supported destinations

When you create a flow that uses Freshsales as the data source, you can set the destination to any of the following connectors:

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

When you create a flow that uses Freshsales as the data source, you can transfer any of the
following data objects to supported destinations:

| **Object** | **Field** | **Data type** | **Supported filters** |
| ---------- | --------- | ------------- | --------------------- |
| accounts   |           |               |                       |
| contacts   |           |               |                       |
