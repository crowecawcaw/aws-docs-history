# BambooHR connector for Amazon AppFlow

BambooHR is a human resources software as a service (SaaS) solution. If you’re a
BambooHR user, your account contains data on employees and applicants, such as employee
information, benefits, vacation time, openings, reports, files, and more. You can use Amazon AppFlow to
transfer data from BambooHR to certain AWS services or other supported applications.

## Amazon AppFlow support for BambooHR

Amazon AppFlow supports BambooHR as follows.

**Supported as a data source?**
Yes. You can use Amazon AppFlow to transfer data from BambooHR.

**Supported as a data destination?**
No. You can't use Amazon AppFlow to transfer data to BambooHR.

## Before you begin

To use Amazon AppFlow to transfer data from BambooHR to supported destinations, you must meet these
requirements:

- You have an account with BambooHR that contains the data that you want to transfer. For more
  information about the BambooHR data objects that Amazon AppFlow supports, see [Supported objects](#bamboohr-objects "#bamboohr-objects").
- In the API keys settings for your account, you've created an API key for Amazon AppFlow. Amazon AppFlow
  uses the API key to make authenticated calls to your account and securely access your data. For
  more information, see [Authentication](https://documentation.bamboohr.com/docs#authentication "https://documentation.bamboohr.com/docs#authentication") in the BambooHR documentation.

Note the value of your API key. When you connect to your BambooHR account, you
provide this value to Amazon AppFlow.

## Connecting Amazon AppFlow

to your BambooHR account

To connect Amazon AppFlow to your BambooHR account,
provide details from your BambooHR project so that Amazon AppFlow can access your data. If you
haven't yet configured your BambooHR project for Amazon AppFlow integration, see [Before you begin](#bamboohr-prereqs "#bamboohr-prereqs").

###### To connect to BambooHR

1. Sign in to the AWS Management Console and open the Amazon AppFlow console at [https://console.aws.amazon.com/appflow/](https://console.aws.amazon.com/appflow/ "https://console.aws.amazon.com/appflow/").
2. In the navigation pane on the left, choose **Connections**.
3. On the **Manage connections** page, for **Connectors**,
   choose **BambooHR**.
4. Choose **Create connection**.
5. In the **Connect to BambooHR**
   window, enter the following information:
   - **API key** – Enter your API key.
   - **Instance URL** – The URL of the
     instance where you want to run the operation, for example,
     https://api.bamboohr.com/api/gateway.php/amazonawstest.
   - **Zone (Optional)** – The time zone that you access Amazon AppFlow
     from.

6. Optionally, under **Data encryption**, choose **Customize
   encryption settings (advanced)** if you want to encrypt your data with a customer
   managed key in the AWS Key Management Service (AWS KMS).

By default, Amazon AppFlow encrypts your data with a KMS key that AWS creates, uses, and manages
for you. Choose this option if you want to encrypt your data with your own KMS key instead.

Amazon AppFlow always encrypts your data during transit and at rest. For more information, see
[Data protection in Amazon AppFlow](data-protection.md "data-protection.md").

If you want to use a KMS key from the current AWS account, select this key under
**Choose an AWS KMS key**. If you want to use a KMS key from a different
AWS account, enter the Amazon Resource Name (ARN) for that key. 7. For **Connection name**, enter a name for your connection. 8. Choose **Connect**. 9. In the window that appears, sign in to your BambooHR account, and grant access
to Amazon AppFlow.

On the **Manage connections** page, your new connection appears in the
**Connections** table. When you create a flow
that uses BambooHR as the data source, you can select this connection.

## Transferring data from BambooHR with a flow

To transfer data from BambooHR, create an Amazon AppFlow flow, and choose BambooHR as the data
source. For the steps to create a flow, see [Creating flows in Amazon AppFlow](create-flow.md "create-flow.md").

When you configure the flow, choose the data object that you want to transfer. For the objects
that Amazon AppFlow supports for BambooHR, see [Supported objects](#bamboohr-objects "#bamboohr-objects").

Also, choose the destination where you want to transfer the data object that you selected.
For more information about how to configure your destination, see [Supported destinations](#bamboohr-destinations "#bamboohr-destinations").

## Supported destinations

When you create a flow that uses BambooHR as the data source, you can set the destination to any of the following connectors:

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

When you create a flow that uses BambooHR as the data source, you can transfer any of the
following data objects to supported destinations:

| **Object**                 | **Field**              | **Data type**            | **Supported filters** |
| -------------------------- | ---------------------- | ------------------------ | --------------------- |
| Company Files              | Company Name           | String                   |                       |
| Id                         | Integer                |                          |
| can Upload Files           | String                 |                          |
| files                      | List                   |                          |
| Deduction types            | Additional Description | String                   |                       |
| Allowable Benefit Types    | List                   |                          |
| Can BeCollected By Trax    | Boolean                |                          |
| Deduction Note             | String                 |                          |
| Deduction Note Link        | String                 |                          |
| Deduction Note Link Text   | String                 |                          |
| Deduction Type Name        | String                 |                          |
| Default Deduction Code     | String                 |                          |
| Hide Annual Max            | Boolean                |                          |
| Id                         | String                 |                          |
| Managed Deduction Type     | String                 |                          |
| Non Benefit Deduction Type | Boolean                |                          |
| Sub Type Text              | String                 |                          |
| Sub Types                  | List                   |                          |
| Employee Dependents        | Address Line 1         | String                   |                       |
| Address Line 2             | String                 |                          |
| City                       | String                 |                          |
| Country                    | String                 |                          |
| Date Of Birth              | Date                   |                          |
| Employee Id                | String                 |                          |
| First Name                 | String                 |                          |
| Gender                     | String                 |                          |
| Home Phone                 | String                 |                          |
| Id                         | String                 |                          |
| Is Student                 | String                 |                          |
| Is Us Citizen              | String                 |                          |
| Last Name                  | String                 |                          |
| Masked SIN                 | String                 |                          |
| Masked SSN                 | String                 |                          |
| Middle Name                | String                 |                          |
| Relationship               | String                 |                          |
| State                      | String                 |                          |
| Zip Code                   | String                 |                          |
| Employees                  | Can Upload Photo       | Boolean                  |                       |
| Department                 | List                   |                          |
| Display Name               | String                 |                          |
| Division                   | List                   |                          |
| Employee photo url         | String                 |                          |
| First Name                 | String                 |                          |
| ID                         | String                 | EQUAL_TO                 |
| Instagram                  | String                 |                          |
| Job Title                  | List                   |                          |
| Last Changed               | DateTime               | GREATER_THAN_OR_EQUAL_TO |
| Last Name                  | String                 |                          |
| LinkedIn                   | String                 |                          |
| Location                   | List                   |                          |
| Manager                    | String                 |                          |
| Mobile Phone               | String                 |                          |
| Photo Uploaded             | Boolean                |                          |
| Preferred Name             | String                 |                          |
| Pronouns                   | List                   |                          |
| Work Email                 | String                 |                          |
| Work Phone                 | String                 |                          |
| Work Phone Extension       | String                 |                          |
| Training Type              | Category               | Struct                   |                       |
| Description                | String                 |                          |
| Due From Hire Date         | List                   |                          |
| Frequency                  | String                 |                          |
| Id                         | String                 |                          |
| Link Url                   | String                 |                          |
| Renewable                  | Boolean                |                          |
| Required                   | Boolean                |                          |
| Training Type              | String                 |                          |
| Users                      | Email                  | String                   |                       |
| Employee Id                | Integer                |                          |
| First Name                 | String                 |                          |
| Id                         | Integer                |                          |
| Last Login                 | DateTime               |                          |
| Last Name                  | String                 |                          |
| Status                     | String                 |                          |
