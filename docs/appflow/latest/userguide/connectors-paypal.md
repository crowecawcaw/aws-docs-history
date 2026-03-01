# PayPal connector for Amazon AppFlow

PayPal is a payments system that facilitates online money transfers between
parties, such as transfers between customers and online vendors. If you're a PayPal
user, your account contains data about your transactions, such as their payers, dates, and
statuses. You can use Amazon AppFlow to transfer data from
PayPal to certain AWS services or other supported applications.

## Amazon AppFlow support for PayPal

Amazon AppFlow supports PayPal as follows.

**Supported as a data source?**
Yes. You can use Amazon AppFlow to transfer data from PayPal.

**Supported as a data destination?**
No. You can't use Amazon AppFlow to transfer data to PayPal.

## Before you begin

To use Amazon AppFlow to transfer data from PayPal to supported destinations, you must meet these
requirements:

- You have an account with PayPal that contains the data that you want to transfer. For more
  information about the PayPal data objects that Amazon AppFlow supports, see [Supported objects](#paypal-objects "#paypal-objects").
- In PayPal Developer, you've created a REST API app for Amazon AppFlow. The app
  provides the client credentials that Amazon AppFlow uses to access your data securely when it makes
  authenticated calls to your account. For the steps to create an app, see [How
  do I create REST API credentials?](https://www.paypal.com/us/cshelp/article/how-do-i-create-rest-api-credentials-ts1949 "https://www.paypal.com/us/cshelp/article/how-do-i-create-rest-api-credentials-ts1949") in the PayPal Help Center.
- You have configured the app with one or more redirect URLs for Amazon AppFlow.

Redirect URLs have the following format:

```
https://`region`.console.aws.amazon.com/appflow/oauth
```

In this URL, _region_ is the code for the AWS Region
where you use Amazon AppFlow to transfer data from PayPal. For example, the code for the US East (N. Virginia)
Region is `us-east-1`. For that Region, the URL is the following:

```
https://us-east-1.console.aws.amazon.com/appflow/oauth
```

For the AWS Regions that Amazon AppFlow supports, and their codes, see [Amazon AppFlow endpoints and quotas](../../../general/latest/gr/appflow.md "../../../general/latest/gr/appflow.md")
in the _AWS General Reference._

Note the client ID and secret from the settings for your REST API app. You provide these
values to Amazon AppFlow when you connect to your PayPal account.

## Connecting Amazon AppFlow to your PayPal account

To connect Amazon AppFlow to your PayPal account, provide the client credentials from
your REST API app so that Amazon AppFlow can access your data. If you haven't yet configured your
PayPal account for Amazon AppFlow integration, see [Before you begin](#paypal-prereqs "#paypal-prereqs").

###### To connect to PayPal

1. Sign in to the AWS Management Console and open the Amazon AppFlow console at [https://console.aws.amazon.com/appflow/](https://console.aws.amazon.com/appflow/ "https://console.aws.amazon.com/appflow/").
2. In the navigation pane on the left, choose **Connections**.
3. On the **Manage connections** page, for **Connectors**,
   choose **PayPal**.
4. Choose **Create connection**.
5. In the **Connect to PayPal** window, enter the following
   information:
   - **Authorization tokens URL** – Do one of the following:
     - To connect to a REST API app in the PayPal Live environment, choose
       **https://api-m.paypal.com/v1/oauth2/token**.
     - To connect to a REST API app in the PayPal Sandbox environment, choose
       **https://api-m.sandbox.paypal.com/v1/oauth2/token**.

   - **Client ID** – The client ID of your REST API app in
     PayPal Developer.
   - **Client secret** – The secret of your REST API app in
     PayPal Developer.
   - **Instance URL** – Do one of the following:
     - To connect to a REST API app in the PayPal Live environment, choose
       **https://api-m.paypal.com**.
     - To connect to a REST API app in the PayPal Sandbox environment, choose
       **https://api-m.sandbox.paypal.com**.

6. Optionally, under **Data encryption**, choose **Customize
   encryption settings (advanced)** if you want to encrypt your data with a customer
   managed key in the AWS Key Management Service (AWS KMS).

By default, Amazon AppFlow encrypts your data with a KMS key that AWS creates, uses, and manages
for you. Choose this option if you want to encrypt your data with your own KMS key instead.

Amazon AppFlow always encrypts your data during transit and at rest. For more information, see
[Data protection in Amazon AppFlow](data-protection.md "data-protection.md").

If you want to use a KMS key from the current AWS account, select this key under
**Choose an AWS KMS key**. If you want to use a KMS key from a different
AWS account, enter the Amazon Resource Name (ARN) for that key. 7. For **Connection name**, enter a name for your connection. 8. Choose **Connect**. 9. In the window that appears, sign in to your PayPal account, and grant access
to Amazon AppFlow.

On the **Manage connections** page, your new connection appears in the
**Connections** table. When you create a flow
that uses PayPal as the data source, you can select this connection.

## Transferring data from PayPal with a flow

To transfer data from PayPal, create an Amazon AppFlow flow, and choose PayPal as the data
source. For the steps to create a flow, see [Creating flows in Amazon AppFlow](create-flow.md "create-flow.md").

When you configure the flow, choose the data object that you want to transfer. For the objects
that Amazon AppFlow supports for PayPal, see [Supported objects](#paypal-objects "#paypal-objects").

Also, choose the destination where you want to transfer the data object that you selected.
For more information about how to configure your destination, see [Supported destinations](#paypal-destinations "#paypal-destinations").

## Supported destinations

When you create a flow that uses PayPal as the data source, you can set the destination to any of the following connectors:

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

When you create a flow that uses PayPal as the data source, you can transfer any of the
following data objects to supported destinations:

| **Object**                     | **Field**    | **Data type** | **Supported filters** |
| ------------------------------ | ------------ | ------------- | --------------------- |
| Transaction                    | Auction Info | Struct        |                       |
| Balance Affecting Records Only | String       | EQUAL_TO      |
| Cart Info                      | Struct       |               |
| Date Range                     | DateTime     | BETWEEN       |
| Incentive Info                 | Struct       |               |
| Last Refreshed Date Time       | String       |               |
| Payer Info                     | Struct       |               |
| Payment Instrument Type        | String       | EQUAL_TO      |
| Shipping Info                  | Struct       |               |
| Store ID                       | String       | EQUAL_TO      |
| Store Info                     | Struct       |               |
| Terminal ID                    | String       | EQUAL_TO      |
| Transaction Currency           | String       | EQUAL_TO      |
| Transaction ID                 | String       | EQUAL_TO      |
| Transaction Info               | Struct       |               |
| Transaction Status             | String       | EQUAL_TO      |
| Transaction Type               | String       | EQUAL_TO      |
