# Freshdesk connector for Amazon AppFlow

Freshdesk is an online customer service solution. If you're a Freshdesk
user, your account contains data about your customer engagements, including agents, conversations,
and satisfaction ratings. You can use Amazon AppFlow to transfer data from
Freshdesk to certain AWS services or other supported applications.

## Amazon AppFlow support for Freshdesk

Amazon AppFlow supports Freshdesk as follows.

**Supported as a data source?**
Yes. You can use Amazon AppFlow to transfer data from Freshdesk.

**Supported as a data destination?**
No. You can't use Amazon AppFlow to transfer data to Freshdesk.

## Before you begin

To use Amazon AppFlow to transfer data from Freshdesk to supported destinations, you must meet these
requirements:

- You have an account with Freshdesk that contains the data that you want to transfer. For more
  information about the Freshdesk data objects that Amazon AppFlow supports, see [Supported objects](#freshdesk-objects "#freshdesk-objects").

Note the following values because you specify them in the connection settings in
Amazon AppFlow.

- The API key from the profile settings of your Freshdesk account. The API key
  authenticates third-party services like Amazon AppFlow to access your account. For the steps to find
  the key, see [How to find your API key](https://support.freshdesk.com/en/support/solutions/articles/215517-how-to-find-your-api-key "https://support.freshdesk.com/en/support/solutions/articles/215517-how-to-find-your-api-key") at the Freshdesk support site.
- Your Freshdesk address.

## Connecting Amazon AppFlow to your Freshdesk

account

To connect Amazon AppFlow to your Freshdesk account, provide your API key and
Freshdesk address.

###### To connect to Freshdesk

1. Sign in to the AWS Management Console and open the Amazon AppFlow console at [https://console.aws.amazon.com/appflow/](https://console.aws.amazon.com/appflow/ "https://console.aws.amazon.com/appflow/").
2. In the navigation pane on the left, choose **Connections**.
3. On the **Manage connections** page, for **Connectors**,
   choose **Freshdesk**.
4. Choose **Create connection**.
5. In the **Connect to Freshdesk**
   window, enter the following information:
   - **API key** – The API key from your Freshdesk profile
     settings.
   - **Instance URL** – Your Freshdeskaddress, such as
     `https:`my-company-name`.freshdesk.com`.

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
that uses Freshdesk as the data source, you can select this connection.

## Transferring data from Freshdesk with a flow

To transfer data from Freshdesk, create an Amazon AppFlow flow, and choose Freshdesk as the data
source. For the steps to create a flow, see [Creating flows in Amazon AppFlow](create-flow.md "create-flow.md").

When you configure the flow, choose the data object that you want to transfer. For the objects
that Amazon AppFlow supports for Freshdesk, see [Supported objects](#freshdesk-objects "#freshdesk-objects").

Also, choose the destination where you want to transfer the data object that you selected.
For more information about how to configure your destination, see [Supported destinations](#freshdesk-destinations "#freshdesk-destinations").

## Supported destinations

When you create a flow that uses Freshdesk as the data source, you can set the destination to any of the following connectors:

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

When you create a flow that uses Freshdesk as the data source, you can transfer any of the
following data objects to supported destinations:

| **Object**          | **Field**          | **Data type**                                             | **Supported filters** |
| ------------------- | ------------------ | --------------------------------------------------------- | --------------------- | ------------------- | -------- | --------------------------------------------------------- |
| Agent               | Available          | Boolean                                                   |                       |
| Available Since     | DateTime           |                                                           |                       | Contact             | Map      |                                                           |
| Created At          | DateTime           |                                                           |                       | Email               | String   | EQUAL_TO                                                  |
| ID                  | Long               |                                                           |                       | Mobile              | Long     | EQUAL_TO                                                  |
| Occasional          | Boolean            |                                                           |                       | Phone               | Long     | EQUAL_TO                                                  |
| Signature           | String             |                                                           |                       | Ticket Scope        | Long     |                                                           |
| Type                | String             |                                                           |                       | Updated At          | DateTime |                                                           |
| Business Hour       | Business Hour      | Map                                                       |                       |
| Created At          | DateTime           |                                                           |                       | Description         | String   |                                                           |
| ID                  | Long               |                                                           |                       | Is Default          | Boolean  |                                                           |
| Name                | String             |                                                           |                       | Time Zone           | String   |                                                           |
| Updated At          | DateTime           |                                                           |
| Comment             | Answer             | Boolean                                                   |                       |
| Body                | String             |                                                           |                       | Body Text           | String   |                                                           |
| Created At          | DateTime           |                                                           |                       | Forum ID            | Long     |                                                           |
| ID                  | Long               |                                                           |                       | Published           | Boolean  |                                                           |
| Spam                | Boolean            |                                                           |                       | Topic ID            | Long     |                                                           |
| Trash               | Boolean            |                                                           |                       | Updated At          | DateTime |                                                           |
| User ID             | Long               |                                                           |
| Company             | Account Tier       | String                                                    |                       |
| Created At          | DateTime           | EQUAL_TO, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO |                       | Custom Field        | Map      |                                                           |
| Description         | String             |                                                           |                       | Domain              | List     |                                                           |
| Domain              | String             | EQUAL_TO                                                  |                       | Health Score        | String   |                                                           |
| ID                  | Long               |                                                           |                       | Industry            | String   |                                                           |
| Name                | String             |                                                           |                       | Note                | String   |                                                           |
| Renewal Date        | Date               |                                                           |                       | Updated At          | DateTime | EQUAL_TO, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO |
| Contact             | Active             | Boolean                                                   | EQUAL_TO              |
| Address             | String             |                                                           |                       | Company ID          | Long     | EQUAL_TO                                                  |
| Created At          | DateTime           | LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO, EQUAL_TO |                       | Custom Fields       | Map      |                                                           |
| Description         | String             |                                                           |                       | Email               | String   | EQUAL_TO                                                  |
| ID                  | Long               |                                                           |                       | Job Title           | String   |                                                           |
| Language            | String             | EQUAL_TO                                                  |                       | Mobile              | String   | EQUAL_TO                                                  |
| Name                | String             |                                                           |                       | Other Companies     | List     |                                                           |
| Phone               | String             | EQUAL_TO                                                  |                       | Tag                 | String   | EQUAL_TO                                                  |
| Time Zone           | String             | EQUAL_TO                                                  |                       | Twitter Id          | String   | EQUAL_TO                                                  |
| Updated At          | DateTime           | LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO           |
| Conversation        | Attachment         | List                                                      |                       |
| Bcc Email           | List               |                                                           |                       | Body                | String   |                                                           |
| Body Text           | String             |                                                           |                       | Cc Email            | List     |                                                           |
| Created At          | DateTime           |                                                           |                       | From Email          | String   |                                                           |
| ID                  | Long               |                                                           |                       | Incoming            | Boolean  |                                                           |
| Last Edited At      | DateTime           |                                                           |                       | Last Edited User ID | Long     |                                                           |
| Private             | Boolean            |                                                           |                       | Source              | Long     |                                                           |
| Support Email       | String             |                                                           |                       | Ticket ID           | Long     |                                                           |
| To Email            | String             |                                                           |                       | Updated At          | DateTime |                                                           |
| User ID             | Long               |                                                           |
| Email Config        | Active             | Boolean                                                   |                       |
| Created At          | DateTime           |                                                           |                       | Group ID            | Long     |                                                           |
| ID                  | Long               |                                                           |                       | Name                | String   |                                                           |
| Primary Role        | Boolean            |                                                           |                       | Product Id          | Long     |                                                           |
| Reply Email         | String             |                                                           |                       | To Email            | String   |                                                           |
| Updated At          | DateTime           |                                                           |
| Email Inbox         | Active             | Boolean                                                   | EQUAL_TO              |
| Created At          | DateTime           |                                                           |                       | Custom Mailbox      | Map      |                                                           |
| Default Reply Email | Boolean            |                                                           |                       | Forward Email       | String   | EQUAL_TO                                                  |
| Freshdesk Mailbox   | Map                |                                                           |                       | Group ID            | Long     | EQUAL_TO                                                  |
| Mailbox Type        | String             |                                                           |                       | Name                | String   |                                                           |
| Product ID          | Long               | EQUAL_TO                                                  |                       | Support_Email       | String   | EQUAL_TO                                                  |
| Updated At          | DateTime           |                                                           |                       | id                  | Long     |                                                           |
| Forum               | Description        | String                                                    |                       |
| Forum Category ID   | Long               |                                                           |                       | Forum Type          | Long     |                                                           |
| Forum Visibility    | Long               |                                                           |                       | ID                  | Long     |                                                           |
| Name                | String             |                                                           |                       | Position            | Long     |                                                           |
| Posts Count         | Long               |                                                           |                       | Topics Count        | Long     |                                                           |
| Forum Category      | Created At         | DateTime                                                  |                       |
| Description         | String             |                                                           |                       | ID                  | Long     |                                                           |
| Name                | String             |                                                           |                       | Updated At          | DateTime |                                                           |
| Group               | Auto Ticket Assign | Long                                                      |                       |
| Business Hour Id    | Long               |                                                           |                       | Created At          | DateTime |                                                           |
| Description         | String             |                                                           |                       | Escalate To         | Long     |                                                           |
| ID                  | Long               |                                                           |                       | Name                | String   |                                                           |
| Unassigned For      | String             |                                                           |                       | Updated At          | DateTime |                                                           |
| Product             | Created At         | DateTime                                                  |                       |
| Description         | String             |                                                           |                       | ID                  | Long     |                                                           |
| Name                | String             |                                                           |                       | Updated At          | DateTime |                                                           |
| Role                | Created At         | DateTime                                                  |                       |
| Default             | Boolean            |                                                           |                       | Description         | String   |                                                           |
| ID                  | Long               |                                                           |                       | Name                | String   |                                                           |
| Updated At          | DateTime           |                                                           |
| Satisfaction Rating | Agent ID           | Long                                                      |                       |
| Created At          | DateTime           |                                                           |                       | Created_Since       | DateTime | EQUAL_TO                                                  |
| Feedback            | String             |                                                           |                       | Group ID            | Long     |                                                           |
| ID                  | Long               |                                                           |                       | Rating              | Map      |                                                           |
| Survey ID           | Long               |                                                           |                       | Ticket ID           | Long     |                                                           |
| Updated_At          | DateTime           |                                                           |                       | User ID             | Long     | EQUAL_TO                                                  |
| Skill               | Agent              | List                                                      |                       |
| Condtion            | List               |                                                           |                       | Created At          | DateTime |                                                           |
| ID                  | Long               |                                                           |                       | Match Type          | String   |                                                           |
| Name                | String             |                                                           |                       | Rank                | String   |                                                           |
| Updated At          | DateTime           |                                                           |
| Solution            | Created At         | DateTime                                                  |                       |
| Description         | String             |                                                           |                       | ID                  | Long     |                                                           |
| Name                | String             |                                                           |                       | Term                | String   | CONTAINS                                                  |
| Updated At          | DateTime           |                                                           |
| Survey              | ID                 | Long                                                      |                       |
| Question            | List               |                                                           |                       | Title               | String   |                                                           |
| Ticket              | Agent ID           | Integer                                                   | EQUAL_TO              |
| Cc Email            | List               |                                                           |                       | Created At          | DateTime | LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO, EQUAL_TO |
| Custom Field        | Map                |                                                           |                       | Due By              | DateTime | EQUAL_TO                                                  |
| Email Config Id     | Long               |                                                           |                       | Fr Due By           | DateTime | EQUAL_TO                                                  |
| Fr Escalated        | Boolean            |                                                           |                       | Fwd Email           | List     |                                                           |
| Group ID            | Long               | EQUAL_TO                                                  |                       | ID                  | Long     |                                                           |
| Is Escalated        | Boolean            |                                                           |                       | Priority            | Long     | EQUAL_TO                                                  |
| Product ID          | Long               |                                                           |                       | Reply Cc Email      | List     |                                                           |
| Requester ID        | Long               |                                                           |                       | Responder ID        | Long     |                                                           |
| Source              | Long               |                                                           |                       | Spam                | Boolean  |                                                           |
| Status              | Long               | EQUAL_TO                                                  |                       | Subject             | String   |                                                           |
| Tag                 | String             | EQUAL_TO                                                  |                       | To email            | List     |                                                           |
| Type                | String             | EQUAL_TO                                                  |                       | Updated At          | DateTime | LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO           |
| Time Entry          | Agent ID           | Long                                                      | EQUAL_TO              |
| Billable            | Boolean            | EQUAL_TO                                                  |                       | Company ID          | Long     | EQUAL_TO                                                  |
| Created At          | DateTime           |                                                           |                       | Executed After      | DateTime | EQUAL_TO                                                  |
| Executed At         | DateTime           |                                                           |                       | Executed Before     | DateTime | EQUAL_TO                                                  |
| ID                  | Long               |                                                           |                       | Note                | String   |                                                           |
| Start Time          | DateTime           |                                                           |                       | Ticket ID           | Long     |                                                           |
| Time Spent          | String             |                                                           |                       | Timer Running       | Boolean  |                                                           |
| Updated At          | DateTime           |                                                           |
| Topic               | Created At         | DateTime                                                  |                       |
| Forum ID            | Long               |                                                           |                       | Hit                 | Long     |                                                           |
| ID                  | Long               |                                                           |                       | Locked              | Boolean  |                                                           |
| Merged Topic ID     | Long               |                                                           |                       | Post Count          | Long     |                                                           |
| Published           | String             |                                                           |                       | Replied At          | DateTime |                                                           |
| Replied By          | DateTime           |                                                           |                       | Stamp Type          | Long     |                                                           |
| Sticky              | Boolean            |                                                           |                       | Title               | String   |                                                           |
| Updated At          | DateTime           |                                                           |                       | User ID             | Long     |                                                           |
| User Vote           | Long               |                                                           |
