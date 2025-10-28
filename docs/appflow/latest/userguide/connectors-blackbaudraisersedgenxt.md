# Blackbaud Raiser's Edge NXT connector for Amazon AppFlow

Blackbaud Raiser's Edge NXT is a customer relationship management (CRM) software as a service (SaaS)
solution for nonprofit organizations. If you’re a Blackbaud Raiser's Edge NXT user, your account contains
data on prospects, analytics, gift management, and more. You can use Amazon AppFlow to transfer data from
Blackbaud Raiser's Edge NXT to certain AWS services or other supported applications.

## Amazon AppFlow support for Blackbaud Raiser's Edge NXT

Amazon AppFlow supports Blackbaud Raiser's Edge NXT as follows.

**Supported as a data source?**

Yes. You can use Amazon AppFlow to transfer data from Blackbaud Raiser's Edge NXT.

**Supported as a data destination?**

No. You can't use Amazon AppFlow to transfer data to Blackbaud Raiser's Edge NXT.

## Before you begin

To use Amazon AppFlow to transfer data from Blackbaud Raiser's Edge NXT to supported destinations, you must meet these
requirements:

- You have an account with Blackbaud Raiser's Edge NXT that contains the data that you want to transfer. For more
  information about the Blackbaud Raiser's Edge NXT data objects that Amazon AppFlow supports, see [Supported objects](#blackbaudraisersedgenxt-objects "#blackbaudraisersedgenxt-objects").
- In your Blackbaud SKY Developer account, you've created a SKY developer app for Amazon AppFlow. The
  app provides the client credentials that Amazon AppFlow uses to access your data securely when it makes
  authenticated calls to your account. You can use default settings for the Grant type, the
  authorization tokens URL, and the authorization code URL, or use your own. For information
  about how to create a developer app, see [Applications](https://developer.blackbaud.com/skyapi/docs/applications "https://developer.blackbaud.com/skyapi/docs/applications") in the SKY
  API documentation.
- In the setting for Scopes, you've defined access to Blackbaud data with the option
  **Full data access.**
- You've configured the app with one or more redirect URLs for
  Amazon AppFlow.

Redirect URLs have the following format:

```
https://`region`.console.aws.amazon.com/appflow/oauth
```

In this URL, _region_ is the code for the AWS Region
where you use Amazon AppFlow to transfer data from Blackbaud Raiser's Edge NXT. For example, the code for the US East (N. Virginia)
Region is `us-east-1`. For that Region, the URL is the following:

```
https://us-east-1.console.aws.amazon.com/appflow/oauth
```

For the AWS Regions that Amazon AppFlow supports, and their codes, see [Amazon AppFlow endpoints and quotas](../../../general/latest/gr/appflow.md "../../../general/latest/gr/appflow.md")
in the _AWS General Reference._

Note the client ID, client secret, and subscription key from the settings for your app. You
provide these values to Amazon AppFlow when you create your connection.

## Connecting Amazon AppFlow

to your Blackbaud Raiser's Edge NXT account

To connect Amazon AppFlow to your Blackbaud Raiser's Edge NXT account, provide details from your SKY
developer app so that Amazon AppFlow can access your data. If you haven't yet configured your
Blackbaud Raiser's Edge NXT account for Amazon AppFlow integration, see [Before you begin](#blackbaudraisersedgenxt-prereqs "#blackbaudraisersedgenxt-prereqs").

###### To connect to Blackbaud Raiser's Edge NXT

1. Sign in to the AWS Management Console and open the Amazon AppFlow console at [https://console.aws.amazon.com/appflow/](https://console.aws.amazon.com/appflow/ "https://console.aws.amazon.com/appflow/").
2. In the navigation pane on the left, choose **Connections**.
3. On the **Manage connections** page, for **Connectors**,
   choose **Blackbaud Raiser's Edge NXT**.
4. Choose **Create connection**.
5. In the **Connect to Blackbaud Raiser's Edge NXT** window, enter the following
   information:
   - **Connection name** — Enter a name for your connection.
   - **Client ID** — The client ID in your Blackbaud Raiser's Edge NXT
     project.
   - **Client secret** — The client secret in your
     Blackbaud Raiser's Edge NXT project.
   - **Subscription key** — The subscription key in your
     Blackbaud Raiser's Edge NXT project.

6. Optionally, under **Data encryption**, choose **Customize
   encryption settings (advanced)** if you want to encrypt your data with a customer
   managed key in the AWS Key Management Service (AWS KMS).

By default, Amazon AppFlow encrypts your data with a KMS key that AWS creates, uses, and manages
for you. Choose this option if you want to encrypt your data with your own KMS key instead.

Amazon AppFlow always encrypts your data during transit and at rest. For more information, see
[Data protection in Amazon AppFlow](data-protection.md "data-protection.md").

If you want to use a KMS key from the current AWS account, select this key under
**Choose an AWS KMS key**. If you want to use a KMS key from a different
AWS account, enter the Amazon Resource Name (ARN) for that key. 7. Choose **Connect**. 8. In the window that appears, sign in to your Blackbaud Raiser's Edge NXT account, and grant access
to Amazon AppFlow.

On the **Manage connections** page, your new connection appears in the
**Connections** table. When you create a flow
that uses Blackbaud Raiser's Edge NXT as the data source, you can select this connection.

## Transferring data from Blackbaud Raiser's Edge NXT with a flow

To transfer data from Blackbaud Raiser's Edge NXT, create an Amazon AppFlow flow, and choose Blackbaud Raiser's Edge NXT as the data
source. For the steps to create a flow, see [Creating flows in Amazon AppFlow](create-flow.md "create-flow.md").

When you configure the flow, choose the data object that you want to transfer. For the objects
that Amazon AppFlow supports for Blackbaud Raiser's Edge NXT, see [Supported objects](#blackbaudraisersedgenxt-objects "#blackbaudraisersedgenxt-objects").

Also, choose the destination where you want to transfer the data object that you selected.
For more information about how to configure your destination, see [Supported destinations](#blackbaudraisersedgenxt-destinations "#blackbaudraisersedgenxt-destinations").

## Supported destinations

When you create a flow that uses Blackbaud Raiser's Edge NXT as the data source, you can set the destination to any of the following connectors:

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

When you create a flow that uses Blackbaud Raiser's Edge NXT as the data source, you can transfer any of the
following data objects to supported destinations:

| **Object**                     | **Field**              | **Data type** | **Supported filters** |
| ------------------------------ | ---------------------- | ------------- | --------------------- | -------------------------------- | -------- | -------- |
| Action                         | Category               | String        |                       |
| Completed                      | Boolean                |               |                       | Completed Date                   | DateTime |          |
| Computed Status                | String                 | EQUAL_TO      |                       | Constituent ID                   | String   |          |
| Date                           | DateTime               |               |                       | Date Added                       | DateTime | EQUAL_TO |
| Date Modified                  | DateTime               |               |                       | Description                      | String   |          |
| End Time                       | String                 |               |                       | Fundraisers                      | List     |          |
| ID                             | String                 |               |                       | Last Modified                    | DateTime | EQUAL_TO |
| List ID                        | String                 | EQUAL_TO      |                       | Location                         | String   |          |
| Opportunity ID                 | String                 |               |                       | Outcome                          | String   |          |
| Priority                       | String                 |               |                       | Start Time                       | String   |          |
| Status                         | String                 |               |                       | Status Code                      | String   | EQUAL_TO |
| Summary                        | String                 |               |                       | Type                             | String   |          |
| Address                        | Address Lines          | String        |                       |
| City                           | String                 |               |                       | Constituent ID                   | String   | EQUAL_TO |
| Country                        | String                 |               |                       | County                           | String   |          |
| Date Added                     | DateTime               | EQUAL_TO      |                       | Date Modified                    | DateTime |          |
| Do Not Mail                    | Boolean                |               |                       | End                              | DateTime |          |
| Formatted Address              | String                 |               |                       | ID                               | String   |          |
| Inactive                       | Boolean                |               |                       | Include Inactive                 | Boolean  | EQUAL_TO |
| Last Modified                  | DateTime               | EQUAL_TO      |                       | Postal Code                      | String   |          |
| Preferred                      | Boolean                |               |                       | Seasonal End                     | Struct   |          |
| Seasonal Start                 | Struct                 |               |                       | Start                            | DateTime |          |
| State                          | String                 |               |                       | Type                             | String   |          |
| Appeal                         | Category               | String        |                       |
| Date Added                     | DateTime               | EQUAL_TO      |                       | Date Modified                    | DateTime |          |
| Description                    | String                 |               |                       | End Date                         | DateTime |          |
| Goal                           | Struct                 |               |                       | ID                               | String   |          |
| Inactive                       | Boolean                |               |                       | Include Inactive                 | Boolean  | EQUAL_TO |
| Last Modified                  | DateTime               | EQUAL_TO      |                       | Lookup ID                        | String   |          |
| Start Date                     | DateTime               |               |
| Campaign                       | Category               | String        |                       |
| Date Added                     | DateTime               | EQUAL_TO      |                       | Date Modified                    | DateTime |          |
| Description                    | String                 |               |                       | End Date                         | DateTime |          |
| Goal                           | Struct                 |               |                       | ID                               | String   |          |
| Inactive                       | Boolean                |               |                       | Include Inactive                 | Boolean  | EQUAL_TO |
| Last Modified                  | DateTime               | EQUAL_TO      |                       | Lookup ID                        | String   |          |
| Start Date                     | DateTime               |               |
| Constituent                    | Address                | Struct        |                       |
| Age                            | Integer                |               |                       | Birthdate                        | Struct   |          |
| Constituent Code               | String                 | EQUAL_TO      |                       | Constituent ID                   | String   | EQUAL_TO |
| Custom Field Category          | String                 | EQUAL_TO      |                       | Date Added                       | DateTime | EQUAL_TO |
| Date Modified                  | DateTime               |               |                       | Deceased                         | Boolean  |          |
| Email                          | Struct                 |               |                       | First                            | String   |          |
| Former Name                    | String                 |               |                       | Fundraiser Status                | String   | EQUAL_TO |
| Gender                         | String                 |               |                       | Gives Anonymously                | Boolean  |          |
| ID                             | String                 |               |                       | Inactive                         | Boolean  |          |
| Include Deceased               | Boolean                | EQUAL_TO      |                       | Include Inactive                 | Boolean  | EQUAL_TO |
| Last                           | String                 |               |                       | Last Modified                    | DateTime | EQUAL_TO |
| List ID                        | String                 | EQUAL_TO      |                       | Lookup ID                        | String   |          |
| Marital Status                 | String                 |               |                       | Middle                           | String   |          |
| Name                           | String                 |               |                       | Online Presence                  | Struct   |          |
| Phone                          | Struct                 |               |                       | Postal Code                      | String   | EQUAL_TO |
| Preferred Name                 | String                 |               |                       | Spouse                           | Struct   |          |
| Suffix                         | String                 |               |                       | Suffix 2                         | String   |          |
| Title                          | String                 |               |                       | Title 2                          | String   |          |
| Type                           | String                 |               |
| Custom Field                   | Category               | String        | EQUAL_TO              |
| Comment                        | String                 |               |                       | Date                             | DateTime |          |
| Date Added                     | DateTime               | EQUAL_TO      |                       | Date Modified                    | DateTime |          |
| Gift ID                        | Integer                | EQUAL_TO      |                       | ID                               | String   |          |
| Last Modified                  | DateTime               | EQUAL_TO      |                       | Parent ID                        | String   |          |
| Type                           | String                 |               |                       | Value                            | String   | EQUAL_TO |
| Education                      | Campus                 | String        |                       |
| Class Of Degree                | String                 |               |                       | Constituent ID                   | String   |          |
| Date Added                     | DateTime               | EQUAL_TO      |                       | Date Entered                     | Struct   |          |
| Date Graduated                 | Struct                 |               |                       | Date Left                        | Struct   |          |
| Date Modified                  | DateTime               |               |                       | Degree                           | String   |          |
| Faculty                        | String                 |               |                       | GPA                              | Double   |          |
| ID                             | String                 |               |                       | Known Name                       | String   |          |
| Last Modified                  | DateTime               | EQUAL_TO      |                       | Majors                           | List     |          |
| Minors                         | List                   |               |                       | Primary                          | Boolean  |          |
| Registration Number            | String                 |               |                       | School                           | String   |          |
| Social Organization            | String                 |               |                       | Status                           | String   |          |
| String                         | String                 |               |                       | Subject Of Study                 | String   |          |
| Type                           | String                 |               |                       | class Of                         | String   |          |
| Email Address                  | Address                | String        |                       |
| Constituent ID                 | String                 | EQUAL_TO      |                       | Date Added                       | DateTime | EQUAL_TO |
| Date Modified                  | DateTime               |               |                       | Do Not Email                     | Boolean  |          |
| ID                             | String                 |               |                       | Inactive                         | Boolean  |          |
| Include Inactive               | Boolean                | EQUAL_TO      |                       | Last Modified                    | DateTime | EQUAL_TO |
| Primary                        | Boolean                |               |                       | Type                             | String   |          |
| Event                          | Attended Count         | Integer       |                       |
| Attending Count                | Integer                |               |                       | Capacity                         | Integer  |          |
| Category                       | Struct                 |               |                       | Date Added                       | DateTime | EQUAL_TO |
| Date Modified                  | DateTime               |               |                       | End Date                         | Date     |          |
| End Time                       | String                 |               |                       | Event Category                   | String   | EQUAL_TO |
| Event ID                       | String                 | EQUAL_TO      |                       | Goal                             | Double   |          |
| ID                             | String                 |               |                       | Inactive                         | Boolean  |          |
| Include Inactive               | Boolean                | EQUAL_TO      |                       | Invited Count                    | Integer  |          |
| Last Modified                  | DateTime               | EQUAL_TO      |                       | Lookup ID                        | String   | EQUAL_TO |
| Name                           | String                 | EQUAL_TO      |                       | Percent Of Goal                  | Integer  |          |
| Revenue                        | Double                 |               |                       | Start Date                       | Date     |          |
| Start Date From                | Date                   | EQUAL_TO      |                       | Start Date To                    | DateTime | EQUAL_TO |
| Start Time                     | String                 |               |
| Event Participant              | Attended               | Boolean       |                       |
| Attended Filter                | Boolean                | EQUAL_TO      |                       | Class Of                         | String   |          |
| Contact ID                     | String                 |               |                       | Date Added                       | DateTime | EQUAL_TO |
| Date Modified                  | DateTime               |               |                       | Do Not Call                      | Boolean  |          |
| Do Not Email                   | Boolean                |               |                       | Donations                        | Double   |          |
| Email                          | String                 |               |                       | Email Eligible Filter            | Boolean  | EQUAL_TO |
| Fees Paid Filter               | Boolean                | EQUAL_TO      |                       | First Name                       | String   |          |
| Former Name                    | String                 |               |                       | Guests                           | Struct   |          |
| Host                           | Struct                 |               |                       | ID                               | String   |          |
| Invitation Status              | String                 | EQUAL_TO      |                       | Is Constituent                   | Boolean  |          |
| Is Constituent Filter          | Boolean                | EQUAL_TO      |                       | Last Modified                    | DateTime | EQUAL_TO |
| Last Name                      | String                 |               |                       | Lookup ID                        | String   |          |
| Memberships                    | Struct                 |               |                       | Middle Name                      | String   |          |
| Name                           | String                 | EQUAL_TO      |                       | Name Tag                         | String   |          |
| Online Data Health             | String                 | EQUAL_TO      |                       | Participant Option ID            | String   | EQUAL_TO |
| Participant Options            | Struct                 |               |                       | Participation Level              | String   | EQUAL_TO |
| Participation Level            | Struct                 |               |                       | Phone                            | String   |          |
| Phone Call Eligible Filter     | Boolean                | EQUAL_TO      |                       | Preferred Name                   | String   |          |
| RSVP Date                      | Struct                 |               |                       | RSVP Status                      | String   | EQUAL_TO |
| Registration Form              | Struct                 |               |                       | Registration Form IDs            | String   | EQUAL_TO |
| Registration Form Include Type | String                 | EQUAL_TO      |                       | Revenue                          | Double   |          |
| Seat                           | String                 |               |                       | Suffix                           | String   |          |
| Summary Note                   | String                 |               |                       | Title                            | String   |          |
| Total Paid                     | Double                 |               |                       | Total Registration Fees          | Double   |          |
| Fund                           | Category               | String        |                       |
| Date Added                     | DateTime               | EQUAL_TO      |                       | Date Modified                    | DateTime |          |
| Description                    | String                 |               |                       | End Date                         | DateTime |          |
| Fund ID                        | Integer                | EQUAL_TO      |                       | Goal                             | Struct   |          |
| ID                             | String                 |               |                       | Inactive                         | Boolean  |          |
| Include Inactive               | Boolean                | EQUAL_TO      |                       | Last Modified                    | DateTime | EQUAL_TO |
| Lookup ID                      | String                 |               |                       | Start Date                       | DateTime |          |
| Type                           | String                 |               |
| Fundraiser Assignment          | Amount                 | Struct        |                       |
| Appeal ID                      | String                 |               |                       | Campaign ID                      | String   |          |
| Constituent ID                 | String                 | EQUAL_TO      |                       | End                              | DateTime |          |
| Fund ID                        | String                 |               |                       | Fundraiser ID                    | String   |          |
| ID                             | String                 |               |                       | Include Inactive                 | Boolean  | EQUAL_TO |
| Start                          | DateTime               |               |                       | Type                             | String   |          |
| Gift                           | Acknowledgement Status | String        | EQUAL_TO              |
| Acknowledgements               | List                   |               |                       | Amount                           | Struct   |          |
| Appeal ID                      | String                 | EQUAL_TO      |                       | Balance                          | Struct   |          |
| Batch Number                   | String                 |               |                       | Campaign ID                      | String   | EQUAL_TO |
| Constituency                   | String                 |               |                       | Constituent ID                   | String   | EQUAL_TO |
| Date                           | DateTime               |               |                       | Date Added                       | DateTime | EQUAL_TO |
| Date Modified                  | DateTime               |               |                       | End Gift Amount                  | Double   | EQUAL_TO |
| End Gift Date                  | DateTime               | EQUAL_TO      |                       | Fund ID                          | String   | EQUAL_TO |
| Fundraisers                    | List                   |               |                       | Gift Splits                      | List     |          |
| Gift Status                    | String                 |               |                       | Gift Type                        | String   | EQUAL_TO |
| ID                             | String                 |               |                       | Is Anonymous                     | Boolean  |          |
| Last Modified                  | DateTime               | EQUAL_TO      |                       | Linked Gifts                     | List     |          |
| List ID                        | String                 | EQUAL_TO      |                       | Lookup ID                        | String   |          |
| Origin                         | String                 |               |                       | Payments                         | List     |          |
| Post Date                      | DateTime               |               |                       | Post Status                      | String   | EQUAL_TO |
| Receipt Status                 | String                 | EQUAL_TO      |                       | Receipts                         | List     |          |
| Reference                      | String                 |               |                       | Soft Credits                     | List     |          |
| Start Gift Amount              | Double                 | EQUAL_TO      |                       | Start Gift Date                  | DateTime | EQUAL_TO |
| Subtype                        | String                 |               |                       | Type                             | String   |          |
| Gift Batch                     | Actual Amount          | Double        |                       |
| Added By                       | String                 |               |                       | Approved                         | Boolean  | EQUAL_TO |
| Batch Description              | String                 |               |                       | Batch Number                     | String   | EQUAL_TO |
| Created By                     | String                 |               |                       | Created On                       | DateTime |          |
| Date Added                     | DateTime               |               |                       | Has Exceptions                   | Boolean  | EQUAL_TO |
| ID                             | String                 |               |                       | Is Approved                      | Boolean  |          |
| Number Of Gifts                | Integer                |               |                       | Search Text                      | String   | EQUAL_TO |
| Membership                     | Category               | String        |                       |
| Constituent ID                 | String                 |               |                       | Date Added                       | DateTime | EQUAL_TO |
| Date Modified                  | DateTime               |               |                       | Dues                             | Struct   |          |
| Expires                        | DateTime               |               |                       | ID                               | String   |          |
| Joined                         | DateTime               |               |                       | Last Modified                    | DateTime | EQUAL_TO |
| Members                        | List                   |               |                       | Program                          | String   |          |
| Standing                       | String                 |               |                       | Subcategory                      | String   |          |
| Note                           | Constituent ID         | String        |                       |
| Date                           | Struct                 |               |                       | Date Added                       | DateTime | EQUAL_TO |
| Date Modified                  | DateTime               |               |                       | ID                               | String   |          |
| Last Modified                  | DateTime               | EQUAL_TO      |                       | Summary                          | String   |          |
| Text                           | String                 |               |                       | Type                             | String   |          |
| Online Presence                | Address                | String        |                       |
| Constituent ID                 | String                 | EQUAL_TO      |                       | Date Added                       | DateTime | EQUAL_TO |
| Date Modified                  | DateTime               |               |                       | ID                               | String   |          |
| Inactive                       | Boolean                |               |                       | Include Inactive                 | Boolean  | EQUAL_TO |
| Last Modified                  | DateTime               | EQUAL_TO      |                       | Primary                          | Boolean  |          |
| Type                           | String                 |               |
| Opportunity                    | Ask Amount             | Struct        |                       |
| Ask Date                       | DateTime               |               |                       | Campaign ID                      | String   |          |
| Constituent ID                 | String                 | EQUAL_TO      |                       | Date Added                       | DateTime | EQUAL_TO |
| Date Modified                  | DateTime               |               |                       | Deadline                         | DateTime |          |
| Expected Amount                | Struct                 |               |                       | Expected Date                    | DateTime |          |
| Fund ID                        | String                 |               |                       | Funded Amount                    | Struct   |          |
| Funded Date                    | DateTime               |               |                       | Fundraisers                      | List     |          |
| ID                             | String                 |               |                       | Inactive                         | Boolean  |          |
| Include Inactive               | Boolean                | EQUAL_TO      |                       | Last Modified                    | DateTime | EQUAL_TO |
| Linked Gifts                   | List                   |               |                       | List ID                          | String   | EQUAL_TO |
| Name                           | String                 |               |                       | Purpose                          | String   |          |
| Status                         | String                 |               |
| Package                        | Appeal ID              | String        | EQUAL_TO              |
| Category                       | String                 |               |                       | Date Added                       | DateTime | EQUAL_TO |
| Date Modified                  | DateTime               |               |                       | Default Gift Aamount             | Struct   |          |
| Description                    | String                 |               |                       | End                              | DateTime |          |
| Goal                           | Struct                 |               |                       | ID                               | String   |          |
| Inactive                       | Boolean                |               |                       | Include Inactive                 | Boolean  | EQUAL_TO |
| Last Modified                  | DateTime               | EQUAL_TO      |                       | Lookup ID                        | String   |          |
| Notes                          | String                 |               |                       | Recipient Count                  | Integer  |          |
| Start                          | DateTime               |               |
| Phone                          | Constituent ID         | String        | EQUAL_TO              |
| Date Added                     | DateTime               |               |                       | Date Modified                    | DateTime |          |
| Do Not Call                    | Boolean                |               |                       | ID                               | String   |          |
| Inactive                       | Boolean                |               |                       | Number                           | String   |          |
| Primary                        | Boolean                |               |                       | Type                             | String   |          |
| Relationship                   | Comment                | String        |                       |
| Constituent ID                 | String                 |               |                       | Date Added                       | DateTime | EQUAL_TO |
| Date Modified                  | DateTime               |               |                       | End                              | Struct   |          |
| ID                             | String                 |               |                       | Is Constituent Head Of Household | Boolean  |          |
| Is Organization Contact        | Boolean                |               |                       | Is Primary Business              | Boolean  |          |
| Is Spouse                      | Boolean                |               |                       | Is Spouse Head Of Household      | Boolean  |          |
| Last Modified                  | DateTime               | EQUAL_TO      |                       | Name                             | String   |          |
| Organization Contact Type      | String                 |               |                       | Position                         | String   |          |
| Reciprocal Relationship ID     | String                 |               |                       | Reciprocal Type                  | String   |          |
| Relation ID                    | String                 |               |                       | Start                            | Struct   |          |
| Type                           | String                 |               |
