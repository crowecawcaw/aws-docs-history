# DocuSign Monitor connector for Amazon AppFlow

DocuSign Monitor provides data about digital agreements that are processed through
DocuSign. If you're a DocuSign user, your account contains monitoring data about your DocuSign
activity. You can use Amazon AppFlow to transfer your monitoring data to certain AWS services or other
supported applications.

## Amazon AppFlow support for DocuSign Monitor

Amazon AppFlow supports DocuSign Monitor as follows.

**Supported as a data source?**
Yes. You can use Amazon AppFlow to transfer data from DocuSign Monitor.

**Supported as a data destination?**
No. You can't use Amazon AppFlow to transfer data to DocuSign Monitor.

## Before you begin

To use Amazon AppFlow to transfer data from DocuSign Monitor to supported destinations, you must meet these
requirements:

- You have an account with DocuSign that contains the data that you want to transfer. For
  more information about the DocuSign Monitor data objects that Amazon AppFlow supports, see [Supported objects](#docusign-monitor-objects "#docusign-monitor-objects").
- In the settings for your Docusign account, you've created an app and integration key for
  Amazon AppFlow. The app provides the client credentials that Amazon AppFlow uses to access your data securely
  when it makes authenticated calls to your account. For more information, see [Configure your app](https://developers.docusign.com/platform/configure-app/ "https://developers.docusign.com/platform/configure-app/") in
  the DocuSign Developer documentation.
- In the settings for your app, you've done the following:
  - Created a secret key.
  - Added a redirect URL for Amazon AppFlow.

  Redirect URLs have the following format:

  ```
  https://`region`.console.aws.amazon.com/appflow/oauth
  ```

  In this URL, _region_ is the code for the AWS Region
  where you use Amazon AppFlow to transfer data from DocuSign Monitor. For example, the code for the US East (N. Virginia)
  Region is `us-east-1`. For that Region, the URL is the following:

  ```
  https://us-east-1.console.aws.amazon.com/appflow/oauth
  ```

  For the AWS Regions that Amazon AppFlow supports, and their codes, see [Amazon AppFlow endpoints and quotas](../../../general/latest/gr/appflow.md "../../../general/latest/gr/appflow.md")
  in the _AWS General Reference._

From your app settings, note your integration key and secret key because you specify these
values in the connection settings in Amazon AppFlow.

## Connecting Amazon AppFlow to your DocuSign account

To connect Amazon AppFlow to your DocuSign account, provide the integration key and secret key from
your app so that Amazon AppFlow can access your data. If you haven't yet configured your DocuSign account
for Amazon AppFlow integration, see [Before you begin](#docusign-monitor-prereqs "#docusign-monitor-prereqs").

###### To connect to DocuSign Monitor

1. Sign in to the AWS Management Console and open the Amazon AppFlow console at [https://console.aws.amazon.com/appflow/](https://console.aws.amazon.com/appflow/ "https://console.aws.amazon.com/appflow/").
2. In the navigation pane on the left, choose **Connections**.
3. On the **Manage connections** page, for **Connectors**,
   choose **DocuSign Monitor**.
4. Choose **Create connection**.
5. In the **Connect to DocuSign Monitor** window, enter the following
   information:
   - **Client ID** – The integration key from your app
     settings.
   - **Client secret** – The secret key from your app
     settings.

6. Optionally, under **Data encryption**, choose **Customize
   encryption settings (advanced)** if you want to encrypt your data with a customer
   managed key in the AWS Key Management Service (AWS KMS).

By default, Amazon AppFlow encrypts your data with a KMS key that AWS creates, uses, and manages
for you. Choose this option if you want to encrypt your data with your own KMS key instead.

Amazon AppFlow always encrypts your data during transit and at rest. For more information, see
[Data protection in Amazon AppFlow](data-protection.md "data-protection.md").

If you want to use a KMS key from the current AWS account, select this key under
**Choose an AWS KMS key**. If you want to use a KMS key from a different
AWS account, enter the Amazon Resource Name (ARN) for that key. 7. For **Connection name**, enter a name for your connection. 8. Choose **Continue**. 9. In the window that appears, sign in to your DocuSign account, and grant access to
Amazon AppFlow.

On the **Manage connections** page, your new connection appears in the
**Connections** table. When you create a flow
that uses DocuSign Monitor as the data source, you can select this connection.

## Transferring data from DocuSign Monitor with a flow

To transfer data from DocuSign Monitor, create an Amazon AppFlow flow, and choose DocuSign Monitor as the data
source. For the steps to create a flow, see [Creating flows in Amazon AppFlow](create-flow.md "create-flow.md").

When you configure the flow, choose the data object that you want to transfer. For the objects
that Amazon AppFlow supports for DocuSign Monitor, see [Supported objects](#docusign-monitor-objects "#docusign-monitor-objects").

Also, choose the destination where you want to transfer the data object that you selected.
For more information about how to configure your destination, see [Supported destinations](#docusign-monitor-destinations "#docusign-monitor-destinations").

## Supported destinations

When you create a flow that uses DocuSign Monitor as the data source, you can set the destination to any of the following connectors:

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

When you create a flow that uses Docusign Monitor as the data source, you can transfer any of the
following data objects to supported destinations:

| **Object**                     | **Field** | **Data type**                    | **Supported filters**            |
| ------------------------------ | --------- | -------------------------------- | -------------------------------- | -------------------- | ------- | -------------------------------- |
| Monitoring Data                | accountId | String                           | CONTAINS, EQUAL_TO, NOT_EQUAL_TO |
| action                         | String    | CONTAINS, EQUAL_TO, NOT_EQUAL_TO |                                  | affectedUserId       | String  | CONTAINS, EQUAL_TO, NOT_EQUAL_TO |
| affectedUserIsMemberOfDomain   | Boolean   | EQUAL_TO, NOT_EQUAL_TO           |                                  | application          | String  |                                  |
| begin_end_time                 | DateTime  | BETWEEN                          |                                  | browser              | String  | CONTAINS                         |
| city                           | String    | CONTAINS, EQUAL_TO, NOT_EQUAL_TO |                                  | country              | String  | CONTAINS, EQUAL_TO, NOT_EQUAL_TO |
| customerVisible                | String    |                                  |                                  | data                 | Struct  |                                  |
| device                         | String    | CONTAINS                         |                                  | environment          | String  |                                  |
| eventId                        | String    | CONTAINS, EQUAL_TO, NOT_EQUAL_TO |                                  | field                | String  | CONTAINS, EQUAL_TO, NOT_EQUAL_TO |
| integratorKey                  | String    | CONTAINS, EQUAL_TO, NOT_EQUAL_TO |                                  | ipAddress            | String  | CONTAINS, EQUAL_TO, NOT_EQUAL_TO |
| ipAddressLocation              | Struct    |                                  |                                  | isUserMemberOfDomain | Boolean | EQUAL_TO, NOT_EQUAL_TO           |
| latitude                       | Double    | EQUAL_TO, NOT_EQUAL_TO           |                                  | longitude            | Double  | EQUAL_TO, NOT_EQUAL_TO           |
| object                         | String    | CONTAINS, EQUAL_TO, NOT_EQUAL_TO |                                  | organizationId       | String  | CONTAINS, EQUAL_TO, NOT_EQUAL_TO |
| os                             | String    | CONTAINS                         |                                  | property             | String  | CONTAINS, EQUAL_TO, NOT_EQUAL_TO |
| proxyLevel                     | String    |                                  |                                  | proxyStatus          | String  |                                  |
| proxyType                      | String    |                                  |                                  | referencedUserId     | String  |                                  |
| referencedUserIsMemberOfDomain | Boolean   |                                  |                                  | result               | String  | CONTAINS, EQUAL_TO, NOT_EQUAL_TO |
| site                           | String    |                                  |                                  | source               | String  |                                  |
| state                          | String    | CONTAINS, EQUAL_TO, NOT_EQUAL_TO |                                  | timestamp            | String  |                                  |
| traceToken                     | String    |                                  |                                  | userAgent            | String  | CONTAINS                         |
| userAgentClientInfo            | Struct    |                                  |                                  | userId               | String  | CONTAINS, EQUAL_TO, NOT_EQUAL_TO |
| version                        | String    |                                  |
