# Asana connector for Amazon AppFlow

Asana is a cloud-based team collaboration solution that helps teams organize,
plan, and complete tasks and projects. If you're an Asana user, your account contains
data about your workspaces, projects, tasks, teams, and more.
You can use Amazon AppFlow to transfer data from
Asana to certain AWS services or other supported applications.

## Amazon AppFlow support for Asana

Amazon AppFlow supports Asana as follows.

**Supported as a data source?**
Yes. You can use Amazon AppFlow to transfer data from Asana.

**Supported as a data destination?**
No. You can't use Amazon AppFlow to transfer data to Asana.

## Before you begin

To use Amazon AppFlow to transfer data from Asana to supported destinations, you must meet these
requirements:

- You have an account with Asana that contains the data that you want to transfer. For more
  information about the Asana data objects that Amazon AppFlow supports, see [Supported objects](#asana-objects "#asana-objects").
- In your Asana account settings, you've created either of the following
  resources for Amazon AppFlow. These resources provide credentials that Amazon AppFlow uses to
  access your data securely when it makes authenticated calls to your account.

  - A Developer App, which supports OAuth 2.0 authentication. For information about how to
    create a Developer App, see [OAuth](https://developers.asana.com/docs/oauth "https://developers.asana.com/docs/oauth") in the Asana Developers documentation.
  - A personal access token. For more information, see [Personal access token](https://developers.asana.com/docs/personal-access-token "https://developers.asana.com/docs/personal-access-token")
    in the Asana Developers documentation.

- If you created an OAuth app, you've configured it with one or more redirect URLs for
  Amazon AppFlow.

Redirect URLs have the following format:

```
https://`region`.console.aws.amazon.com/appflow/oauth
```

In this URL, _region_ is the code for the AWS Region
where you use Amazon AppFlow to transfer data from Asana. For example, the code for the US East (N. Virginia)
Region is `us-east-1`. For that Region, the URL is the following:

```
https://us-east-1.console.aws.amazon.com/appflow/oauth
```

For the AWS Regions that Amazon AppFlow supports, and their codes, see [Amazon AppFlow endpoints and quotas](../../../general/latest/gr/appflow.md "../../../general/latest/gr/appflow.md")
in the _AWS General Reference._

If you created a Developer App, note the client ID and client secret. If you created a
personal access token, note the token value. You provide these values to Amazon AppFlow when you connect
to your Asana account.

## Connecting Amazon AppFlow to your Asana account

To connect Amazon AppFlow to your Asana account, provide the client credentials from
your Developer App, or provide a personal access token. If you haven't yet configured your
Asana account for Amazon AppFlow integration, see [Before you begin](#asana-prereqs "#asana-prereqs").

###### To connect to Asana

1. Sign in to the AWS Management Console and open the Amazon AppFlow console at [https://console.aws.amazon.com/appflow/](https://console.aws.amazon.com/appflow/ "https://console.aws.amazon.com/appflow/").
2. In the navigation pane on the left, choose **Connections**.
3. On the **Manage connections** page, for **Connectors**,
   choose **Asana**.
4. Choose **Create connection**.
5. In the **Connect to Asana** window, for **Select
   authentication type**, choose how to authenticate Amazon AppFlow with your Asana
   account when it requests to access your data:

   - Choose **OAuth2** to authenticate Amazon AppFlow with the client ID and client
     secret from an Asana Developer App. Then enter values for **Client ID** and
     **Client secret**.
   - Choose **PAT** to authenticate Amazon AppFlow with a personal access token.
     Then enter the token value for **Personal access token**.

6. In the **Connect to Asana** window, enter the following
   information:
7. Optionally, under **Data encryption**, choose **Customize
   encryption settings (advanced)** if you want to encrypt your data with a customer
   managed key in the AWS Key Management Service (AWS KMS).

By default, Amazon AppFlow encrypts your data with a KMS key that AWS creates, uses, and manages
for you. Choose this option if you want to encrypt your data with your own KMS key instead.

Amazon AppFlow always encrypts your data during transit and at rest. For more information, see
[Data protection in Amazon AppFlow](data-protection.md "data-protection.md").

If you want to use a KMS key from the current AWS account, select this key under
**Choose an AWS KMS key**. If you want to use a KMS key from a different
AWS account, enter the Amazon Resource Name (ARN) for that key. 8. For **Connection name**, enter a name for your connection. 9. Choose **Connect**. 10. In the window that appears, sign in to your Asana account, and grant access
to Amazon AppFlow.

On the **Manage connections** page, your new connection appears in the
**Connections** table. When you create a flow
that uses Asana as the data source, you can select this connection.

## Transferring data from Asana with a flow

To transfer data from Asana, create an Amazon AppFlow flow, and choose Asana as the data
source. For the steps to create a flow, see [Creating flows in Amazon AppFlow](create-flow.md "create-flow.md").

When you configure the flow, choose the data object that you want to transfer. For the objects
that Amazon AppFlow supports for Asana, see [Supported objects](#asana-objects "#asana-objects").

Also, choose the destination where you want to transfer the data object that you selected.
For more information about how to configure your destination, see [Supported destinations](#asana-destinations "#asana-destinations").

## Supported destinations

When you create a flow that uses Asana as the data source, you can set the destination to any of the following connectors:

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

When you create a flow that uses Asana as the data source, you can transfer any of the
following data objects to supported destinations:

| **Object**                  | **Field**               | **Data type**                                                      | **Supported filters** |
| --------------------------- | ----------------------- | ------------------------------------------------------------------ | --------------------- |
| Audit Log Event             | actor                   | Struct                                                             |                       |
| actor\_type                 | String                  | EQUAL\_TO                                                          |
| context                     | Struct                  |                                                                    |
| created\_at                 | DateTime                |                                                                    |
| details                     | Struct                  |                                                                    |
| event\_category             | String                  |                                                                    |
| event\_type                 | String                  | EQUAL\_TO                                                          |
| gid                         | String                  |                                                                    |
| resource                    | Struct                  |                                                                    |
| start\_end\_at              | DateTime                | GREATER\_THAN\_OR\_EQUAL\_TO, LESS\_THAN\_OR\_EQUAL\_TO            |
| Goal                        | current\_status\_update | Struct                                                             |                       |
| due\_on                     | Date                    |                                                                    |
| followers                   | List                    |                                                                    |
| gid                         | String                  |                                                                    |
| html\_notes                 | String                  |                                                                    |
| is\_workspace\_level        | Boolean                 | EQUAL\_TO                                                          |
| liked                       | Boolean                 |                                                                    |
| likes                       | List                    |                                                                    |
| metric                      | Struct                  |                                                                    |
| name                        | String                  |                                                                    |
| notes                       | String                  |                                                                    |
| num\_likes                  | Integer                 |                                                                    |
| owner                       | Struct                  |                                                                    |
| resource\_type              | String                  |                                                                    |
| start\_on                   | Date                    |                                                                    |
| status                      | String                  |                                                                    |
| team                        | Struct                  |                                                                    |
| time\_period                | Struct                  |                                                                    |
| workspace                   | Struct                  |                                                                    |
| Portfolio                   | color                   | String                                                             |                       |
| created\_at                 | DateTime                |                                                                    |
| created\_by                 | Struct                  |                                                                    |
| current\_status\_update     | Struct                  |                                                                    |
| custom\_field\_settings     | List                    |                                                                    |
| due\_on                     | Date                    |                                                                    |
| gid                         | String                  |                                                                    |
| members                     | List                    |                                                                    |
| name                        | String                  |                                                                    |
| owner                       | Struct                  |                                                                    |
| permalink\_url              | String                  |                                                                    |
| public                      | Boolean                 |                                                                    |
| resource\_type              | String                  |                                                                    |
| start\_on                   | Date                    |                                                                    |
| workspace                   | Struct                  |                                                                    |
| Project                     | archived                | Boolean                                                            | EQUAL\_TO             |
| color                       | String                  |                                                                    |
| completed                   | Boolean                 |                                                                    |
| completed\_at               | DateTime                |                                                                    |
| completed\_by               | Struct                  |                                                                    |
| created\_at                 | DateTime                |                                                                    |
| created\_from\_template     | Struct                  |                                                                    |
| current\_status             | Struct                  |                                                                    |
| current\_status\_update     | Struct                  |                                                                    |
| custom\_field\_settings     | List                    |                                                                    |
| custom\_fields              | List                    |                                                                    |
| default\_view               | String                  |                                                                    |
| due\_date                   | Date                    |                                                                    |
| due\_on                     | Date                    |                                                                    |
| followers                   | List                    |                                                                    |
| gid                         | String                  |                                                                    |
| html\_notes                 | String                  |                                                                    |
| icon                        | String                  |                                                                    |
| is\_template                | Boolean                 |                                                                    |
| members                     | List                    |                                                                    |
| modified\_at                | DateTime                |                                                                    |
| name                        | String                  |                                                                    |
| notes                       | String                  |                                                                    |
| owner                       | Struct                  |                                                                    |
| permalink\_url              | String                  |                                                                    |
| public                      | Boolean                 |                                                                    |
| resource\_type              | String                  |                                                                    |
| start\_on                   | Date                    |                                                                    |
| team                        | Struct                  |                                                                    |
| workspace                   | Struct                  |                                                                    |
| Section                     | created\_at             | DateTime                                                           |                       |
| gid                         | String                  |                                                                    |
| name                        | String                  |                                                                    |
| project                     | Struct                  |                                                                    |
| resource\_type              | String                  |                                                                    |
| Tag                         | color                   | String                                                             |                       |
| created\_at                 | DateTime                |                                                                    |
| followers                   | List                    |                                                                    |
| gid                         | String                  |                                                                    |
| name                        | String                  |                                                                    |
| notes                       | String                  |                                                                    |
| permalink\_url              | String                  |                                                                    |
| resource\_type              | String                  |                                                                    |
| workspace                   | Struct                  |                                                                    |
| Task                        | approval\_status        | String                                                             |                       |
| assignee                    | Struct                  |                                                                    |
| assignee\_section           | Struct                  |                                                                    |
| assignee\_status            | String                  |                                                                    |
| completed                   | Boolean                 | EQUAL\_TO                                                          |
| completed\_at               | DateTime                | LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO            |
| completed\_by               | Struct                  |                                                                    |
| completed\_on               | Date                    | EQUAL\_TO, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO |
| created\_at                 | DateTime                | LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO            |
| custom\_fields              | List                    |                                                                    |
| dependencies                | List                    |                                                                    |
| dependents                  | List                    |                                                                    |
| due\_at                     | DateTime                | LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO            |
| due\_on                     | Date                    | EQUAL\_TO, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO |
| external                    | Struct                  |                                                                    |
| followers                   | List                    |                                                                    |
| gid                         | String                  |                                                                    |
| has\_attachment             | Boolean                 | EQUAL\_TO                                                          |
| hearted                     | Boolean                 |                                                                    |
| hearts                      | List                    |                                                                    |
| html\_notes                 | String                  |                                                                    |
| is\_blocked                 | Boolean                 | EQUAL\_TO                                                          |
| is\_blocking                | Boolean                 | EQUAL\_TO                                                          |
| is\_rendered\_as\_separator | Boolean                 |                                                                    |
| is\_subtask                 | Boolean                 | EQUAL\_TO                                                          |
| liked                       | Boolean                 |                                                                    |
| likes                       | List                    |                                                                    |
| memberships                 | List                    |                                                                    |
| modified\_at                | DateTime                | LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO            |
| modified\_on                | Date                    | EQUAL\_TO, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO |
| name                        | String                  |                                                                    |
| notes                       | String                  |                                                                    |
| num\_hearts                 | Integer                 |                                                                    |
| num\_likes                  | Integer                 |                                                                    |
| num\_subtasks               | Integer                 |                                                                    |
| parent                      | Struct                  |                                                                    |
| permalink\_url              | String                  |                                                                    |
| projects                    | List                    |                                                                    |
| resource\_subtype           | String                  | EQUAL\_TO                                                          |
| resource\_type              | String                  |                                                                    |
| start\_at                   | DateTime                |                                                                    |
| start\_on                   | Date                    | EQUAL\_TO, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO |
| tags                        | List                    |                                                                    |
| text                        | String                  | EQUAL\_TO                                                          |
| workspace                   | Struct                  |                                                                    |
| Team                        | description             | String                                                             |                       |
| gid                         | String                  |                                                                    |
| html\_description           | String                  |                                                                    |
| name                        | String                  |                                                                    |
| organization                | Struct                  |                                                                    |
| permalink\_url              | String                  |                                                                    |
| resource\_type              | String                  |                                                                    |
| visibility                  | String                  |                                                                    |
| User                        | email                   | String                                                             |                       |
| gid                         | String                  |                                                                    |
| name                        | String                  |                                                                    |
| photo                       | Struct                  |                                                                    |
| resource\_type              | String                  |                                                                    |
| workspaces                  | List                    |                                                                    |
| Workspace                   | email\_domains          | List                                                               |                       |
| gid                         | String                  |                                                                    |
| is\_organization            | Boolean                 |                                                                    |
| name                        | String                  |                                                                    |
| resource\_type              | String                  |                                                                    |
