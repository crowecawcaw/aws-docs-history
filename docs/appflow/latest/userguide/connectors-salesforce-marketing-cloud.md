# Salesforce Marketing Cloud connector for

Amazon AppFlow

Marketing Cloud is a Salesforce platform for digital marketing that helps its customers
manage campaigns across multiple channels, including email, mobile, and social. If you use
Marketing Cloud, you can also use Amazon AppFlow to transfer your data to certain AWS services or other
supported applications.

###### Topics

- [Salesforce Marketing Cloud support](#salesforce-marketing-cloud-support "#salesforce-marketing-cloud-support")
- [Before you begin](#salesforce-marketing-cloud-prereqs "#salesforce-marketing-cloud-prereqs")
- [Connecting Amazon AppFlow to your Salesforce
  Marketing Cloud account](#salesforce-marketing-cloud-connecting "#salesforce-marketing-cloud-connecting")
- [Transferring data from Salesforce Marketing
  Cloud with a flow](#salesforce-marketing-cloud-transfer-data "#salesforce-marketing-cloud-transfer-data")
- [Supported objects](#salesforce-marketing-cloud-reference-objects "#salesforce-marketing-cloud-reference-objects")
- [Supported
  destinations](#salesforce-marketing-cloud-reference-destinations "#salesforce-marketing-cloud-reference-destinations")

## Salesforce Marketing Cloud support

Amazon AppFlow supports Salesforce Marketing Cloud as follows.

**Supported as a data source?**

Yes. You can use Amazon AppFlow to transfer data from your Marketing Cloud account.

**Supported as a data destination?**

No. You can't use Amazon AppFlow to transfer data to your Marketing Cloud account.

## Before you begin

Before you can use Amazon AppFlow to transfer data from Marketing Cloud, you need the
following:

- A Salesforce Marketing Cloud account that contains the data that you want to transfer. For
  more information about the Marketing Cloud data objects that Amazon AppFlow supports, see [Supported objects](#salesforce-marketing-cloud-reference-objects "#salesforce-marketing-cloud-reference-objects").
- A Marketing Cloud _package_ so that Amazon AppFlow can access
  your data. In Marketing Cloud, you create packages to add custom functionality to your account.
  For the steps to create a package, see [Create and Install Packages](https://developer.salesforce.com/docs/marketing/marketing-cloud/guide/install-packages.html "https://developer.salesforce.com/docs/marketing/marketing-cloud/guide/install-packages.html") in the Marketing Cloud documentation.

When you create a package for Amazon AppFlow integration, do the following:

1. Add an API integration component to the package.
2. Set the integration type of the component to server-to-server.
3. Grant read access to every data object that you want to transfer with Amazon AppFlow.
4. The Salesforce Marketing Cloud connector now supports fetching records from the data
   extension. If you want to fetch data extension records, you need to add the read and write
   scopes to your package.
5. After you create the package, note the following properties. You need them to create a
   connection in Amazon AppFlow:
   - Client ID
   - Client secret
   - Authentication base URI
   - REST base URI or SOAP base URI (You can use either one; it doesn't matter which one you
     use)

## Connecting Amazon AppFlow to your Salesforce

Marketing Cloud account

To connect Amazon AppFlow to your Marketing Cloud account, provide details about the package so that
Amazon AppFlow can access your data. To learn how to create a package, see [Before you begin](#salesforce-marketing-cloud-prereqs "#salesforce-marketing-cloud-prereqs").

###### To connect to Salesforce Marketing Cloud

1.  Sign in to the AWS Management Console and open the Amazon AppFlow console at [https://console.aws.amazon.com/appflow/](https://console.aws.amazon.com/appflow/ "https://console.aws.amazon.com/appflow/").
2.  In the navigation pane on the left, choose **Connections**.
3.  On the **Manage connections** page, for **Connectors**,
    choose **Salesforce Marketing Cloud**.
4.  Choose **Create connection**.
5.  In the **Connect to Salesforce Marketing Cloud** window, provide the
    following details:

        * **Custom authorization tokens URL** – The authentication base
         URI that's assigned to your Marketing Cloud package. Provide the subdomain to complete the
         URI shown in the console:
         `https://`subdomain`.auth.marketingcloudapis.com/v2/token`.
        * **Client ID** – The client ID that is assigned to your Marketing
         Cloud package.
        * **Client secret** – The client secret that is assigned to your
         Marketing Cloud package.
        * **Salesforce Marketing Cloud Subdomain Endpoint** – The REST
         base URI or SOAP base URI that is assigned to your Marketing Cloud package. These URIs looks
         similar to the following examples:




        	+ `https://`subdomain`.rest.marketingcloudapis.com/`
        	+ `https://`subdomain`.soap.marketingcloudapis.com/`
        In these examples, *subdomain* is the same value that
         you provide for the custom authorization tokens URL.


        You must provide either the REST or SOAP URI, but the one that you use doesn't matter.
         With either one, Amazon AppFlow connects to your Marketing Cloud package, and it transfers data by
         using the REST or SOAP endpoint as needed.

    For more information about the authentication, REST, and SOAP URIs for Marketing Cloud
    packages, see [Your Subdomain and Your Tenant's Endpoints](https://developer.salesforce.com/docs/marketing/marketing-cloud/guide/your-subdomain-tenant-specific-endpoints.html "https://developer.salesforce.com/docs/marketing/marketing-cloud/guide/your-subdomain-tenant-specific-endpoints.html") in the Marketing Cloud
    documentation.

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
that uses Salesforce Marketing Cloud as the data source, you can select this connection.

## Transferring data from Salesforce Marketing

Cloud with a flow

To transfer data from Marketing Cloud, create an Amazon AppFlow flow, and choose Salesforce
Marketing Cloud as the data source. To learn how to create a flow, see [Creating flows in Amazon AppFlow](create-flow.md "create-flow.md").

When you configure the flow, choose the data object that you want to transfer. For more
information about the objects that Amazon AppFlow supports for Marketing Cloud, see [Supported objects](#salesforce-marketing-cloud-reference-objects "#salesforce-marketing-cloud-reference-objects").

Also choose the destination where you want to transfer the data object that you selected.
For more information on how to configure your destination, see [Supported
destinations](#salesforce-marketing-cloud-reference-destinations "#salesforce-marketing-cloud-reference-destinations").

## Supported objects

When you create a flow that uses Salesforce Marketing Cloud as the data source, you can
transfer the following data objects from your Marketing Cloud account:

- Activity
- Bounce Event
- Click Event
- Content Area
- Data Extension
- Email
- Forwarded Email Event
- Forwarded Email OptInEvent
- Link
- Link Send
- List
- List Subscriber
- Not Sent Event
- Open Event
- Send
- Sent Event
- Subscriber
- Survey Event
- Unsub Event
- Audit Events
- Campaigns
- Interactions
- Content Assets

## Supported

destinations

When you create a flow that uses Salesforce Marketing Cloud as the data source, you can set the destination to any of the following connectors:

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
