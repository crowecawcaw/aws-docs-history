# Braintree connector for Amazon AppFlow

Braintree is an online payment processing solution. If you're a Braintree
user, your account contains data about your transactions. You can use Amazon AppFlow to transfer data from
Braintree to certain AWS services or other supported applications.

## Amazon AppFlow support for Braintree

Amazon AppFlow supports Braintree as follows.

**Supported as a data source?**
Yes. You can use Amazon AppFlow to transfer data from Braintree.

**Supported as a data destination?**
No. You can't use Amazon AppFlow to transfer data to Braintree.

## Before you begin

To use Amazon AppFlow to transfer data from Braintree to supported destinations, you must meet these
requirements:

- You have an account with Braintree that contains the data that you want to
  transfer.
- In the API settings for your account, you've created an API key for Amazon AppFlow. The API key
  provides the credentials that Amazon AppFlow uses to access your data securely when it makes
  authenticated calls to your account. For more information, see [Important Gateway Credentials](https://developer.paypal.com/braintree/articles/control-panel/important-gateway-credentials "https://developer.paypal.com/braintree/articles/control-panel/important-gateway-credentials") in the Braintree documentation.

From your API key settings, note the values for public key and private key. You provide
these values to Amazon AppFlow when you connect to your Braintree account.

## Connecting Amazon AppFlow to your Braintree account

To connect Amazon AppFlow to your Braintree account, provide the credentials from your
Braintree API key so that Amazon AppFlow can access your data. If you haven't yet configured
your Braintree account for Amazon AppFlow integration, see [Before you begin](#braintree-prereqs "#braintree-prereqs").

###### To connect to Braintree

1.  Sign in to the AWS Management Console and open the Amazon AppFlow console at [https://console.aws.amazon.com/appflow/](https://console.aws.amazon.com/appflow/ "https://console.aws.amazon.com/appflow/").
2.  In the navigation pane on the left, choose **Connections**.
3.  On the **Manage connections** page, for **Connectors**,
    choose **Braintree**.
4.  Choose **Create connection**.
5.  In the **Connect to Braintree** window, enter the following
    information:
    - **Public Key** – The public key value from the API key in your
      Braintree account.
    - **Private Key** – The private key value from the API key in your
      Braintree account.
    - **Braintree Instance Url** – Choose one of the following:

          + **https://payments.braintree-api.com/graphql** – Connects to
           the Braintree production environment.
          + **https://payments.sandbox.braintree-api.com/graphql** –
           Connects to the Braintree sandbox environment.

      For more information about these environments, see [Try It
      Out](https://developer.paypal.com/braintree/articles/get-started/try-it-out "https://developer.paypal.com/braintree/articles/get-started/try-it-out") in the Braintree documentation.

6.  Optionally, under **Data encryption**, choose **Customize
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
that uses Braintree as the data source, you can select this connection.

## Transferring data from Braintree with a flow

To transfer data from Braintree, create an Amazon AppFlow flow, and choose Braintree as the data
source. For the steps to create a flow, see [Creating flows in Amazon AppFlow](create-flow.md "create-flow.md").

## Supported destinations

When you create a flow that uses Braintree as the data source, you can set the destination to any of the following connectors:

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
