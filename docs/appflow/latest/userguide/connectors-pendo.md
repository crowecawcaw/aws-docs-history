# Pendo connector for Amazon AppFlow

Pendo is a product analytics solution that helps teams record, monitor, and
analyze data about the user experience in their apps. If you're a Pendo user, your
account contains data about your users and their behavior in your product.
You can use Amazon AppFlow to transfer data from
Pendo to certain AWS services or other supported applications.

## Amazon AppFlow support for Pendo

Amazon AppFlow supports Pendo as follows.

**Supported as a data source?**
Yes. You can use Amazon AppFlow to transfer data from Pendo.

**Supported as a data destination?**
No. You can't use Amazon AppFlow to transfer data to Pendo.

## Before you begin

To use Amazon AppFlow to transfer data from Pendo to supported destinations, you must meet these
requirements:

- You have an account with Pendo that contains the data that you want to transfer. For more
  information about the Pendo data objects that Amazon AppFlow supports, see [Supported objects](#pendo-objects "#pendo-objects").
- In your Pendo account, you've created an integration key for Amazon AppFlow, and
  you've configured the key to allow write access. For the steps to create a key, see [Authentication](https://developers.pendo.io/docs/?bash#authentication "https://developers.pendo.io/docs/?bash#authentication") in the
  Pendo Developers documentation.

Note the value of the integration key. You provide this value to Amazon AppFlow when you connect to
your Pendo account.

## Connecting Amazon AppFlow to your Pendo account

To connect Amazon AppFlow to your Pendo account, provide the value of your integration
key so that Amazon AppFlow can access your data. If you haven't yet configured your Pendo
account for Amazon AppFlow integration, see [Before you begin](#pendo-prereqs "#pendo-prereqs").

###### To connect to Pendo

1. Sign in to the AWS Management Console and open the Amazon AppFlow console at [https://console.aws.amazon.com/appflow/](https://console.aws.amazon.com/appflow/ "https://console.aws.amazon.com/appflow/").
2. In the navigation pane on the left, choose **Connections**.
3. On the **Manage connections** page, for **Connectors**,
   choose **Pendo**.
4. Choose **Create connection**.
5. In the **Connect to Pendo** window, for **API
   key**, enter the value of the integration key from your Pendo
   account.
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
that uses Pendo as the data source, you can select this connection.

## Transferring data from Pendo with a flow

To transfer data from Pendo, create an Amazon AppFlow flow, and choose Pendo as the data
source. For the steps to create a flow, see [Creating flows in Amazon AppFlow](create-flow.md "create-flow.md").

When you configure the flow, choose the data object that you want to transfer. For the objects
that Amazon AppFlow supports for Pendo, see [Supported objects](#pendo-objects "#pendo-objects").

Also, choose the destination where you want to transfer the data object that you selected.
For more information about how to configure your destination, see [Supported destinations](#pendo-destinations "#pendo-destinations").

## Supported destinations

When you create a flow that uses Pendo as the data source, you can set the destination to any of the following connectors:

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

When you create a flow that uses Pendo as the data source, you can transfer any of the
following data objects to supported destinations:

| **Object**                           | **Field**   | **Data type**                                                                                    | **Supported filters**            |
| ------------------------------------ | ----------- | ------------------------------------------------------------------------------------------------ | -------------------------------- |
| Account                              | Account ID  | String                                                                                           | EQUAL_TO, NOT_EQUAL_TO, CONTAINS |
| Metadata                             | Struct      |                                                                                                  |
| Parent Account                       | Boolean     | EQUAL_TO                                                                                         |
| Event                                | Account ID  | String                                                                                           | EQUAL_TO, NOT_EQUAL_TO, CONTAINS |
| App ID                               | Long        | LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO, EQUAL_TO, NOT_EQUAL_TO |
| Date Time Range                      | DateTime    | BETWEEN                                                                                          |
| Day                                  | Long        | EQUAL_TO, NOT_EQUAL_TO                                                                           |
| Num Event                            | Long        | LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO, EQUAL_TO, NOT_EQUAL_TO |
| Number Minute                        | Long        | LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO, EQUAL_TO, NOT_EQUAL_TO |
| Page ID                              | String      | EQUAL_TO, NOT_EQUAL_TO, CONTAINS                                                                 |
| Parameter                            | String      |                                                                                                  |
| Remote IP                            | String      | EQUAL_TO, NOT_EQUAL_TO, CONTAINS                                                                 |
| Server                               | String      | EQUAL_TO, NOT_EQUAL_TO, CONTAINS                                                                 |
| User Agent                           | String      | EQUAL_TO, NOT_EQUAL_TO, CONTAINS                                                                 |
| Visitor ID                           | String      | EQUAL_TO, NOT_EQUAL_TO, CONTAINS                                                                 |
| Feature                              | App ID      | Long                                                                                             |                                  |
| App Wide                             | Boolean     |                                                                                                  |
| Color                                | String      |                                                                                                  |
| Created At                           | Long        |                                                                                                  |
| Created By User                      | Struct      |                                                                                                  |
| Created Designer Version             | String      |                                                                                                  |
| Daily Merge First                    | Long        |                                                                                                  |
| Daily Rollup First                   | Long        |                                                                                                  |
| Dirty                                | Boolean     |                                                                                                  |
| Element Initial Tag                  | String      |                                                                                                  |
| Element Path Rule                    | List        |                                                                                                  |
| Element Selection Type               | String      |                                                                                                  |
| Event Property Configuration         | List        |                                                                                                  |
| Group                                | Struct      |                                                                                                  |
| ID                                   | String      |                                                                                                  |
| Is Core Event                        | Boolean     |                                                                                                  |
| Kind                                 | String      |                                                                                                  |
| Last Updated At                      | Long        |                                                                                                  |
| Last Updated By User                 | Struct      |                                                                                                  |
| Name                                 | String      |                                                                                                  |
| Root Version ID                      | String      |                                                                                                  |
| Stable Version ID                    | String      |                                                                                                  |
| Suggested Match                      | String      |                                                                                                  |
| Valid Through                        | Long        |                                                                                                  |
| Feature Event                        | Account ID  | String                                                                                           | EQUAL_TO, NOT_EQUAL_TO, CONTAINS |
| App ID                               | Long        | LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO, EQUAL_TO, NOT_EQUAL_TO |
| Date Time Range                      | DateTime    | BETWEEN                                                                                          |
| Day                                  | Long        | EQUAL_TO, NOT_EQUAL_TO                                                                           |
| Feature ID                           | String      | EQUAL_TO, NOT_EQUAL_TO, CONTAINS                                                                 |
| Num Event                            | Long        | LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO, EQUAL_TO, NOT_EQUAL_TO |
| Number Minute                        | Long        | LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO, EQUAL_TO, NOT_EQUAL_TO |
| Parameter                            | String      |                                                                                                  |
| Remote IP                            | String      | EQUAL_TO, NOT_EQUAL_TO, CONTAINS                                                                 |
| Server                               | String      | EQUAL_TO, NOT_EQUAL_TO, CONTAINS                                                                 |
| User Agent                           | String      | EQUAL_TO, NOT_EQUAL_TO, CONTAINS                                                                 |
| Visitor ID                           | String      | EQUAL_TO, NOT_EQUAL_TO, CONTAINS                                                                 |
| Guide                                | App ID      | Long                                                                                             |                                  |
| App IDS                              | List        |                                                                                                  |
| Attribute                            | Struct      |                                                                                                  |
| Audience                             | List        |                                                                                                  |
| Audience UI Hint                     | Struct      |                                                                                                  |
| Authored Language                    | String      |                                                                                                  |
| Created At                           | Long        |                                                                                                  |
| Created By User                      | Struct      |                                                                                                  |
| Current First Eligible To Be Seen At | Long        |                                                                                                  |
| Editor Type                          | String      |                                                                                                  |
| Email Configuration                  | Struct      |                                                                                                  |
| Email State                          | String      |                                                                                                  |
| ID                                   | String      |                                                                                                  |
| Is Module                            | Boolean     |                                                                                                  |
| Is Multi Step                        | Boolean     |                                                                                                  |
| Is Top Level                         | Boolean     |                                                                                                  |
| Is Training                          | Boolean     |                                                                                                  |
| Kind                                 | String      |                                                                                                  |
| Last Updated At                      | Long        |                                                                                                  |
| Last Updated By User                 | Struct      |                                                                                                  |
| Launch Method                        | String      |                                                                                                  |
| Name                                 | String      |                                                                                                  |
| Poll                                 | List        |                                                                                                  |
| Published At                         | Long        |                                                                                                  |
| Recurrence                           | Long        |                                                                                                  |
| Recurrence Eligibility Window        | Long        |                                                                                                  |
| Reset At                             | Long        |                                                                                                  |
| Root Version ID                      | String      |                                                                                                  |
| Shows After                          | Long        |                                                                                                  |
| Stable Version ID                    | String      |                                                                                                  |
| State                                | String      |                                                                                                  |
| Step                                 | List        |                                                                                                  |
| Guide Event                          | Account ID  | String                                                                                           | EQUAL_TO, NOT_EQUAL_TO, CONTAINS |
| Account IDS                          | List        | EQUAL_TO, NOT_EQUAL_TO, CONTAINS                                                                 |
| App ID                               | Long        | LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO, EQUAL_TO, NOT_EQUAL_TO |
| Browser Time                         | Long        | LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO, EQUAL_TO, NOT_EQUAL_TO |
| Country                              | String      | EQUAL_TO, NOT_EQUAL_TO, CONTAINS                                                                 |
| Date Time Range                      | DateTime    | BETWEEN                                                                                          |
| Element Path                         | String      | EQUAL_TO, NOT_EQUAL_TO, CONTAINS                                                                 |
| Event ID                             | String      | EQUAL_TO, NOT_EQUAL_TO, CONTAINS                                                                 |
| Guide ID                             | String      | EQUAL_TO, NOT_EQUAL_TO, CONTAINS                                                                 |
| Guide Seen Reason                    | String      | EQUAL_TO, NOT_EQUAL_TO, CONTAINS                                                                 |
| Guide Step ID                        | String      | EQUAL_TO, NOT_EQUAL_TO, CONTAINS                                                                 |
| Language                             | String      | EQUAL_TO, NOT_EQUAL_TO, CONTAINS                                                                 |
| Latitude                             | Double      | LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO, EQUAL_TO, NOT_EQUAL_TO |
| Load Time                            | Long        | LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO, EQUAL_TO, NOT_EQUAL_TO |
| Longitude                            | Double      | LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO, EQUAL_TO, NOT_EQUAL_TO |
| Old Visitor ID                       | String      | EQUAL_TO, NOT_EQUAL_TO, CONTAINS                                                                 |
| Region                               | String      | EQUAL_TO, NOT_EQUAL_TO, CONTAINS                                                                 |
| Remote IP                            | String      | EQUAL_TO, NOT_EQUAL_TO, CONTAINS                                                                 |
| ServerName                           | String      | EQUAL_TO, NOT_EQUAL_TO, CONTAINS                                                                 |
| Title                                | String      | EQUAL_TO, NOT_EQUAL_TO, CONTAINS                                                                 |
| Type                                 | String      | EQUAL_TO, NOT_EQUAL_TO, CONTAINS                                                                 |
| UI Element Action                    | String      | EQUAL_TO, NOT_EQUAL_TO, CONTAINS                                                                 |
| UI Element ID                        | String      | EQUAL_TO, NOT_EQUAL_TO, CONTAINS                                                                 |
| UI Element Text                      | String      | EQUAL_TO, NOT_EQUAL_TO, CONTAINS                                                                 |
| UI Element Type                      | String      | EQUAL_TO, NOT_EQUAL_TO, CONTAINS                                                                 |
| URL                                  | String      | EQUAL_TO, NOT_EQUAL_TO, CONTAINS                                                                 |
| User Agent                           | String      | EQUAL_TO, NOT_EQUAL_TO, CONTAINS                                                                 |
| Visitor ID                           | String      | EQUAL_TO, NOT_EQUAL_TO, CONTAINS                                                                 |
| Page                                 | App ID      | Long                                                                                             |                                  |
| Color                                | String      |                                                                                                  |
| Created At                           | Long        |                                                                                                  |
| Created By User                      | Struct      |                                                                                                  |
| Daily Merge First                    | Long        |                                                                                                  |
| Daily Rollup First                   | Long        |                                                                                                  |
| Dirty                                | Boolean     |                                                                                                  |
| Group                                | Struct      |                                                                                                  |
| ID                                   | String      |                                                                                                  |
| Is Auto Tagged                       | Boolean     |                                                                                                  |
| Is Core Event                        | Boolean     |                                                                                                  |
| Kind                                 | String      |                                                                                                  |
| Last Updated At                      | Long        |                                                                                                  |
| Last Updated By User                 | Struct      |                                                                                                  |
| Name                                 | String      |                                                                                                  |
| Root Version ID                      | String      |                                                                                                  |
| Rule                                 | List        |                                                                                                  |
| Rules Json                           | String      |                                                                                                  |
| Stable Version ID                    | String      |                                                                                                  |
| Suggested Name                       | String      |                                                                                                  |
| Valid Through                        | Long        |                                                                                                  |
| Page Event                           | Account ID  | String                                                                                           | EQUAL_TO, NOT_EQUAL_TO, CONTAINS |
| App ID                               | Long        | LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO, EQUAL_TO, NOT_EQUAL_TO |
| Date Time Range                      | DateTime    | BETWEEN                                                                                          |
| Day                                  | Long        | EQUAL_TO, NOT_EQUAL_TO                                                                           |
| Num Event                            | Long        | LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO, EQUAL_TO, NOT_EQUAL_TO |
| Number Minute                        | Long        | LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO, EQUAL_TO, NOT_EQUAL_TO |
| Page ID                              | String      | EQUAL_TO, NOT_EQUAL_TO, CONTAINS                                                                 |
| Parameter                            | String      |                                                                                                  |
| Remote IP                            | String      | EQUAL_TO, NOT_EQUAL_TO, CONTAINS                                                                 |
| Server                               | String      | EQUAL_TO, NOT_EQUAL_TO, CONTAINS                                                                 |
| User Agent                           | String      | EQUAL_TO, NOT_EQUAL_TO, CONTAINS                                                                 |
| Visitor ID                           | String      | EQUAL_TO, NOT_EQUAL_TO, CONTAINS                                                                 |
| Poll Event                           | Account ID  | String                                                                                           | EQUAL_TO, NOT_EQUAL_TO, CONTAINS |
| Account IDS                          | Struct      | EQUAL_TO, NOT_EQUAL_TO, CONTAINS                                                                 |
| App ID                               | Long        | LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO, EQUAL_TO, NOT_EQUAL_TO |
| Browser Time                         | Long        | LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO, EQUAL_TO, NOT_EQUAL_TO |
| Country                              | String      | EQUAL_TO, NOT_EQUAL_TO, CONTAINS                                                                 |
| Date Time Range                      | DateTime    | BETWEEN                                                                                          |
| Element Path                         | String      | EQUAL_TO, NOT_EQUAL_TO, CONTAINS                                                                 |
| Event Id                             | String      | EQUAL_TO, NOT_EQUAL_TO, CONTAINS                                                                 |
| Guide ID                             | String      | EQUAL_TO, NOT_EQUAL_TO, CONTAINS                                                                 |
| Guide Step ID                        | String      | EQUAL_TO, NOT_EQUAL_TO, CONTAINS                                                                 |
| Language                             | String      | EQUAL_TO, NOT_EQUAL_TO, CONTAINS                                                                 |
| Latitude                             | Double      | LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO, EQUAL_TO, NOT_EQUAL_TO |
| Load Time                            | Long        | LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO, EQUAL_TO, NOT_EQUAL_TO |
| Longitude                            | Double      | LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO, EQUAL_TO, NOT_EQUAL_TO |
| Old Visitor ID                       | String      | EQUAL_TO, NOT_EQUAL_TO, CONTAINS                                                                 |
| Poll ID                              | String      | EQUAL_TO, NOT_EQUAL_TO, CONTAINS                                                                 |
| Poll Response                        | String      | EQUAL_TO, NOT_EQUAL_TO                                                                           |
| Poll Type                            | String      | EQUAL_TO, NOT_EQUAL_TO, CONTAINS                                                                 |
| Region                               | String      | EQUAL_TO, NOT_EQUAL_TO, CONTAINS                                                                 |
| Remote IP                            | String      | EQUAL_TO, NOT_EQUAL_TO, CONTAINS                                                                 |
| ServerName                           | String      | EQUAL_TO, NOT_EQUAL_TO, CONTAINS                                                                 |
| Title                                | String      | EQUAL_TO, NOT_EQUAL_TO, CONTAINS                                                                 |
| Type                                 | String      | EQUAL_TO, NOT_EQUAL_TO, CONTAINS                                                                 |
| URL                                  | String      | EQUAL_TO, NOT_EQUAL_TO, CONTAINS                                                                 |
| User Agent                           | String      | EQUAL_TO, NOT_EQUAL_TO, CONTAINS                                                                 |
| Visitor ID                           | String      | EQUAL_TO, NOT_EQUAL_TO, CONTAINS                                                                 |
| Report                               | Aggregation | Struct                                                                                           |                                  |
| Created At                           | Long        |                                                                                                  |
| Created By User                      | Struct      |                                                                                                  |
| Definition                           | Struct      |                                                                                                  |
| ID                                   | String      |                                                                                                  |
| Kind                                 | String      |                                                                                                  |
| Last Run At                          | Long        |                                                                                                  |
| Last Updated At                      | Long        |                                                                                                  |
| Last Updated By User                 | Struct      |                                                                                                  |
| Level                                | String      |                                                                                                  |
| Name                                 | String      |                                                                                                  |
| Owned By User                        | Struct      |                                                                                                  |
| Root Version ID                      | String      |                                                                                                  |
| Scope                                | String      |                                                                                                  |
| Share                                | String      |                                                                                                  |
| Shared                               | Boolean     |                                                                                                  |
| Stable Version ID                    | String      |                                                                                                  |
| Target                               | String      |                                                                                                  |
| Type                                 | String      |                                                                                                  |
| Report Data                          |             |                                                                                                  |                                  |
| Track Event                          | Account ID  | String                                                                                           | EQUAL_TO, NOT_EQUAL_TO, CONTAINS |
| App ID                               | Long        | LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO, EQUAL_TO, NOT_EQUAL_TO |
| Date Time Range                      | DateTime    | BETWEEN                                                                                          |
| Day                                  | Long        | LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO, EQUAL_TO, NOT_EQUAL_TO |
| Num Event                            | Long        | LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO, EQUAL_TO, NOT_EQUAL_TO |
| Number Minute                        | Long        | LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO, EQUAL_TO, NOT_EQUAL_TO |
| Parameter                            | String      |                                                                                                  |
| Property                             | Struct      |                                                                                                  |
| Remote IP                            | String      | EQUAL_TO, NOT_EQUAL_TO, CONTAINS                                                                 |
| Server                               | String      | EQUAL_TO, NOT_EQUAL_TO, CONTAINS                                                                 |
| Track Type ID                        | String      | EQUAL_TO, NOT_EQUAL_TO, CONTAINS                                                                 |
| User Agent                           | String      | EQUAL_TO, NOT_EQUAL_TO, CONTAINS                                                                 |
| Visitor ID                           | String      | EQUAL_TO, NOT_EQUAL_TO, CONTAINS                                                                 |
| Visitor                              | Identified  | Boolean                                                                                          | EQUAL_TO                         |
| Metadata                             | Struct      |                                                                                                  |
| Visitor ID                           | String      | EQUAL_TO, NOT_EQUAL_TO, CONTAINS                                                                 |
