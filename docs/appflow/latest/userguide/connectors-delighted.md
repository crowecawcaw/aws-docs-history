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

## Connecting Amazon AppFlow to your Delighted

account

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

| **Object**        | **Field**          | **Data type** | **Supported filters** |
| ----------------- | ------------------ | ------------- | --------------------- | ------------------------ | -------- | -------- |
| Bounce            | bounced_at         | DateTime      |                       |
| email             | String             |               |                       | name                     | String   |          |
| person_id         | String             |               |                       | since                    | DateTime | EQUAL_TO |
| until             | DateTime           | EQUAL_TO      |
| Metric            | detractor_count    | Integer       |                       |
| detractor_percent | Double             |               |                       | nps                      | Integer  |          |
| passive_count     | Integer            |               |                       | passive_percent          | Double   |          |
| promoter_count    | Integer            |               |                       | promoter_percent         | Double   |          |
| response_count    | Integer            |               |                       | since                    | DateTime | EQUAL_TO |
| trend             | String             | EQUAL_TO      |                       | until                    | DateTime | EQUAL_TO |
| People            | created_at         | DateTime      |                       |
| email             | String             | EQUAL_TO      |                       | id                       | String   |          |
| last_responded_at | DateTime           |               |                       | last_sent_at             | DateTime |          |
| name              | String             |               |                       | next_survey_scheduled_at | DateTime |          |
| phone_number      | String             | EQUAL_TO      |                       | since                    | DateTime | EQUAL_TO |
| until             | DateTime           | EQUAL_TO      |
| Survey Response   | additional_answers | List          |                       |
| comment           | String             |               |                       | created_at               | DateTime |          |
| id                | String             |               |                       | notes                    | List     |          |
| order             | String             | EQUAL_TO      |                       | permalink                | String   |          |
| person            | String             |               |                       | person_email             | String   | EQUAL_TO |
| person_id         | String             | EQUAL_TO      |                       | person_properties        | Struct   |          |
| score             | Integer            |               |                       | since                    | DateTime | EQUAL_TO |
| survey_type       | String             |               |                       | tags                     | List     |          |
| trend             | String             | EQUAL_TO      |                       | until                    | DateTime | EQUAL_TO |
| updated_at        | DateTime           |               |                       | updated_since            | DateTime | EQUAL_TO |
| updated_until     | DateTime           | EQUAL_TO      |
| Unsubscribe       | email              | String        |                       |
| name              | String             |               |                       | person_id                | String   |          |
| since             | DateTime           | EQUAL_TO      |                       | unsubscribed_at          | DateTime |          |
| until             | DateTime           | EQUAL_TO      |
