# SendGrid connector for Amazon AppFlow

SendGrid is a marketing automation platform and email marketing service. If you're
a SendGrid user, your account contains data about your SendGrid activity, such
as your lists, segments, and campaigns. You can use Amazon AppFlow to transfer data from
SendGrid to certain AWS services or other supported applications.

## Amazon AppFlow support for SendGrid

Amazon AppFlow supports SendGrid as follows.

**Supported as a data source?**
Yes. You can use Amazon AppFlow to transfer data from SendGrid.

**Supported as a data destination?**
No. You can't use Amazon AppFlow to transfer data to SendGrid.

## Before you begin

To use Amazon AppFlow to transfer data from SendGrid to supported destinations, you must meet these
requirements:

- You have an account with SendGrid that contains the data that you want to transfer. For more
  information about the SendGrid data objects that Amazon AppFlow supports, see [Supported objects](#sendgrid-objects "#sendgrid-objects").
- You've configured your account with the following settings:
  - You've enabled two-factor authentication. For the steps to enable it, see [Two-Factor
    Authentication](https://docs.sendgrid.com/ui/account-and-settings/two-factor-authentication "https://docs.sendgrid.com/ui/account-and-settings/two-factor-authentication") in the SendGrid documentation.
  - You've created an API key that grants full access to your account. For the steps to
    create one, see [API
    Keys](https://docs.sendgrid.com/ui/account-and-settings/api-keys "https://docs.sendgrid.com/ui/account-and-settings/api-keys") in the SendGrid documentation.

Note the API key from your account settings. You provide it to Amazon AppFlow when you connect to
your SendGrid account.

## Connecting Amazon AppFlow

to your SendGrid account

To connect Amazon AppFlow to your SendGrid account, provide your API key so that Amazon AppFlow
can access your data. If you haven't yet configured your SendGrid account for Amazon AppFlow
integration, see [Before you begin](#sendgrid-prereqs "#sendgrid-prereqs").

###### To connect to SendGrid

1. Sign in to the AWS Management Console and open the Amazon AppFlow console at [https://console.aws.amazon.com/appflow/](https://console.aws.amazon.com/appflow/ "https://console.aws.amazon.com/appflow/").
2. In the navigation pane on the left, choose **Connections**.
3. On the **Manage connections** page, for **Connectors**,
   choose **SendGrid**.
4. Choose **Create connection**.
5. In the **Connect to SendGrid** window, for **API
   Key**, enter the API key from your SendGrid account settings.
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
that uses SendGrid as the data source, you can select this connection.

## Transferring data from SendGrid with a flow

To transfer data from SendGrid, create an Amazon AppFlow flow, and choose SendGrid as the data
source. For the steps to create a flow, see [Creating flows in Amazon AppFlow](create-flow.md "create-flow.md").

When you configure the flow, choose the data object that you want to transfer. For the objects
that Amazon AppFlow supports for SendGrid, see [Supported objects](#sendgrid-objects "#sendgrid-objects").

Also, choose the destination where you want to transfer the data object that you selected.
For more information about how to configure your destination, see [Supported destinations](#sendgrid-destinations "#sendgrid-destinations").

## Supported destinations

When you create a flow that uses SendGrid as the data source, you can set the destination to any of the following connectors:

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

When you create a flow that uses SendGrid as the data source, you can transfer any of the
following data objects to supported destinations:

| **Object**                           | **Field**      | **Data type**     | **Supported filters** |
| ------------------------------------ | -------------- | ----------------- | --------------------- |
| Category                             | Category       | String            |                       |
| Contact                              | Address Line 1 | String            |                       |
| Address Line 2                       | String         |                   |
| Alternate Email                      | List           |                   |
| City                                 | String         |                   |
| Country                              | String         |                   |
| Created At                           | String         |                   |
| Custom Field                         | Struct         |                   |
| Email                                | String         |                   |
| Event Timestamp                      | DateTime       | BETWEEN           |
| Facebook                             | String         |                   |
| First Name                           | String         |                   |
| ID                                   | String         |                   |
| Last Name                            | String         |                   |
| Line                                 | String         |                   |
| List Id                              | List           |                   |
| Metadata                             | Struct         |                   |
| Phone Number                         | String         |                   |
| Postal Code                          | String         |                   |
| Segment Id                           | List           |                   |
| State Province Region                | String         |                   |
| Unique Name                          | String         |                   |
| Updated At                           | String         |                   |
| Whatsapp                             | String         |                   |
| List                                 | Contact Count  | Integer           |                       |
| ID                                   | String         |                   |
| Metadata                             | Struct         |                   |
| Name                                 | String         |                   |
| Marketing Campaign Stats Automation  | Aggregation    | String            |                       |
| Automation ID                        | List           | EQUAL_TO          |
| ID                                   | String         |                   |
| Stats                                | Struct         |                   |
| Step ID                              | String         |                   |
| Marketing Campaign Stats Single Send | Ab Phase       | String            |                       |
| Ab Variation                         | String         |                   |
| Aggregation                          | String         |                   |
| ID                                   | String         |                   |
| Single Send ID                       | List           | EQUAL_TO          |
| Stats                                | Struct         |                   |
| Segment                              | Contact Count  | Integer           |                       |
| Created At                           | String         |                   |
| ID                                   | String         |                   |
| Name                                 | String         |                   |
| Next Sample Update                   | String         |                   |
| No Parent List ID                    | Boolean        | EQUAL_TO          |
| Parent List ID                       | String         |                   |
| Parent List ID                       | String         | EQUAL_TO          |
| Query Version                        | String         |                   |
| Sample Updated At                    | String         |                   |
| Status                               | Struct         |                   |
| Updated At                           | String         |                   |
| Single Send                          | Abtest         | Struct            |                       |
| Category                             | List           | EQUAL_TO          |
| Created At                           | String         |                   |
| ID                                   | String         |                   |
| Is Abtest                            | Boolean        |                   |
| Name                                 | String         | EQUAL_TO          |
| Send At                              | String         |                   |
| Status                               | String         | EQUAL_TO          |
| Updated At                           | String         |                   |
| Stats                                | Aggregated By  | String            | EQUAL_TO              |
| Date                                 | String         |                   |
| StartDate                            | DateTime       | BETWEEN, EQUAL_TO |
| Stats                                | List           |                   |
| Unsubscribe Group                    | Description    | String            |                       |
| ID                                   | Integer        | EQUAL_TO          |
| Is Default                           | Boolean        |                   |
| Last Email Sent At                   | Integer        |                   |
| Name                                 | String         |                   |
| Unsubscribe                          | Integer        |                   |
